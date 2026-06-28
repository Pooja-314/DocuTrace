import fitz
import faiss
import numpy as np

from rank_bm25 import BM25Okapi
from sentence_transformers import (
    SentenceTransformer,
    CrossEncoder
)

from langchain_text_splitters import RecursiveCharacterTextSplitter

# =====================================
# Models
# =====================================

embedding_model = SentenceTransformer(
    "BAAI/bge-small-en-v1.5"
)

reranker = CrossEncoder(
    "cross-encoder/ms-marco-MiniLM-L-6-v2"
)

# =====================================
# Load PDF
# =====================================

pdf_path = "data/Generative_Artificial_Intelligence_Evolving_Techno.pdf"

doc = fitz.open(pdf_path)

full_text = ""

for page in doc:
    full_text += page.get_text()

doc.close()

# =====================================
# Chunking
# =====================================

text_splitter = RecursiveCharacterTextSplitter(
    chunk_size=1000,
    chunk_overlap=200
)

chunks = text_splitter.split_text(full_text)

# =====================================
# Dense Retrieval
# =====================================

embeddings = embedding_model.encode(chunks)

embeddings = np.array(embeddings).astype("float32")

dimension = embeddings.shape[1]

index = faiss.IndexFlatL2(dimension)

index.add(embeddings)


# =====================================
# Rerank Function
# =====================================

def rerank_results(
    query,
    retrieved_chunks,
    top_k=3
):

    pairs = [
        [query, record["text"]]
        for record in retrieved_chunks
    ]

    scores = reranker.predict(
        pairs
    )

    reranked_results = sorted(
        zip(retrieved_chunks, scores),
        key=lambda x: x[1],
        reverse=True
    )

    final_records = []

    for record, score in reranked_results[:top_k]:

        record["rerank_score"] = float(score)

        final_records.append(
        record
        )

    return final_records

