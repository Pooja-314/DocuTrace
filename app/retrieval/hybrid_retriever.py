import fitz
import faiss
import numpy as np
import re
from rank_bm25 import BM25Okapi
from sentence_transformers import SentenceTransformer
from langchain_text_splitters import RecursiveCharacterTextSplitter

# ---------------------------------
# Load Embedding Model
# ---------------------------------

model = SentenceTransformer("BAAI/bge-small-en-v1.5")


# =====================================
# Text Cleanup
# =====================================


def clean_page_text(text):

    text = re.sub(
        r"Vol\.:\(.*?\)",
        "",
        text
    )

    text = re.sub(
        r"https://doi\.org/[^\s]+",
        "",
        text
    )
    
    text = re.sub(
        r"Accepted:.*?\n",
        "",
        text
    )

    text = re.sub(
        r"Published online:.*?\n",
        "",
        text
    )

    text = re.sub(
        r"© The Author\(s\).*?\n",
        "",
        text
    )

    return text
# ---------------------------------
# Chunking
# ---------------------------------

text_splitter = RecursiveCharacterTextSplitter(
    chunk_size=500,
    chunk_overlap=100
)

# ---------------------------------
# Load PDF
# ---------------------------------

pdf_path = "data/Generative_Artificial_Intelligence_Evolving_Techno.pdf"

doc = fitz.open(pdf_path)

# =====================================
# Metadata Chunking
# =====================================

chunk_records = []

for page_num, page in enumerate(
    doc,
    start=1
):

    # Skip References + License Pages

    if page_num >= 18:
        continue

    page_text = clean_page_text(
        page.get_text()
    )

    print(
        f"Processing Page {page_num}"
    )

    page_chunks = text_splitter.split_text(
        page_text
    )

    for chunk_idx, chunk in enumerate(
        page_chunks
    ):

        if len(chunk.strip()) < 100:
            continue

        chunk_records.append(
            {
                "text": chunk,
                "page": page_num,
                "chunk_id":
                f"chunk_{page_num}_{chunk_idx}"
            }
        )

# ---------------------------------
# Build Chunks List
# ---------------------------------

chunks = [
    record["text"]
    for record in chunk_records
]

print(
    f"\nTotal Chunks: {len(chunks)}"
)


print(
    "\n========== SAMPLE RECORD ==========\n"
)

print(
    chunk_records[0]
)

print(
    "\n========== REFERENCE CHECK ==========\n"
)

for record in chunk_records:

    if "References" in record["text"]:

        print(
            f"\nPage: {record['page']}"
        )

        print(
            record["text"][:1000]
        )

        break
    
# =================================
# DENSE RETRIEVAL (FAISS)
# =================================

embeddings = model.encode(chunks)

embeddings = np.array(embeddings).astype("float32")

dimension = embeddings.shape[1]

index = faiss.IndexFlatL2(dimension)

index.add(embeddings)

# =================================
# BM25 RETRIEVAL
# =================================

tokenized_chunks = [chunk.split() for chunk in chunks]

bm25 = BM25Okapi(tokenized_chunks)

# =================================
# QUERY
# =================================

query = "What is Generative AI?"

# =================================
# Hybrid Retrieval Function
# =================================

def hybrid_retrieve(
    query,
    top_k=3
):

    # -----------------------------
    # FAISS SEARCH
    # -----------------------------

    query_embedding = model.encode(
        [query]
    )

    query_embedding = np.array(
        query_embedding
    ).astype("float32")

    distances, faiss_indices = index.search(
        query_embedding,
        top_k
    )

    faiss_results = list(
        faiss_indices[0]
    )
    # -----------------------------
    # BM25 SEARCH
    # -----------------------------

    tokenized_query = query.split()

    scores = bm25.get_scores(
        tokenized_query
    )

    bm25_indices = sorted(

        range(len(scores)),

        key=lambda i: scores[i],

        reverse=True

    )[:top_k]

    # -----------------------------
    # RRF Fusion
    # -----------------------------

    rrf_scores = {}

    rrf_k = 60

    for rank, idx in enumerate(
        faiss_results
    ):

        rrf_scores[idx] = (
            rrf_scores.get(idx, 0)
            +
            1 / (rrf_k + rank + 1)
        )

    for rank, idx in enumerate(
        bm25_indices
    ):

        rrf_scores[idx] = (
            rrf_scores.get(idx, 0)
            +
            1 / (rrf_k + rank + 1)
        )

    final_results = sorted(

        rrf_scores.items(),

        key=lambda x: x[1],

        reverse=True

    )

    retrieved_chunks = []

    for idx, score in final_results[:top_k]:

        retrieved_chunks.append(
            chunk_records[idx]
)

    return retrieved_chunks