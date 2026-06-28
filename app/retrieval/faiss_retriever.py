import fitz
import faiss
import numpy as np

from sentence_transformers import SentenceTransformer
from langchain_text_splitters import RecursiveCharacterTextSplitter

# =====================================
# Load Model
# =====================================

model = SentenceTransformer(
    "BAAI/bge-small-en-v1.5"
)

# =====================================
# Load PDF Once
# =====================================

pdf_path = (
    "data/Generative_Artificial_"
    "Intelligence_Evolving_Techno.pdf"
)

doc = fitz.open(pdf_path)

full_text = ""

for page in doc:
    full_text += page.get_text()

doc.close()

# =====================================
# Chunking
# =====================================

text_splitter = RecursiveCharacterTextSplitter(
    chunk_size=500,
    chunk_overlap=100
)

chunks = text_splitter.split_text(
    full_text
)

# =====================================
# Build Embeddings
# =====================================

embeddings = model.encode(
    chunks
)

embeddings = np.array(
    embeddings
).astype("float32")

# =====================================
# Build Index
# =====================================

dimension = embeddings.shape[1]

index = faiss.IndexFlatL2(
    dimension
)

index.add(
    embeddings
)

# =====================================
# Retrieval Function
# =====================================

def retrieve(
    query,
    top_k=3
):

    query_embedding = model.encode(
        [query]
    )

    query_embedding = np.array(
        query_embedding
    ).astype("float32")

    distances, indices = index.search(
        query_embedding,
        top_k
    )

    results = []

    for idx in indices[0]:

        results.append(
            chunks[idx]
        )

    return results