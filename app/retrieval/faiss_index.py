import fitz
import faiss
import numpy as np

from sentence_transformers import SentenceTransformer
from langchain_text_splitters import RecursiveCharacterTextSplitter

# -----------------------------
# Load embedding model
# -----------------------------

model = SentenceTransformer("BAAI/bge-small-en-v1.5")

# -----------------------------
# Load PDF
# -----------------------------

pdf_path = "data/Generative_Artificial_Intelligence_Evolving_Techno.pdf"

doc = fitz.open(pdf_path)

full_text = ""

for page in doc:
    full_text += page.get_text()

doc.close()

# -----------------------------
# Chunking
# -----------------------------

text_splitter = RecursiveCharacterTextSplitter(
    chunk_size=1000,
    chunk_overlap=200
)

chunks = text_splitter.split_text(full_text)

print(f"\nTotal Chunks: {len(chunks)}")

# -----------------------------
# Generate embeddings
# -----------------------------

embeddings = model.encode(chunks)

embeddings = np.array(embeddings).astype("float32")

print(f"\nEmbedding Shape: {embeddings.shape}")

# -----------------------------
# Create FAISS index
# -----------------------------

dimension = embeddings.shape[1]

index = faiss.IndexFlatL2(dimension)

index.add(embeddings)

print(f"\nFAISS Index Size: {index.ntotal}")

# -----------------------------
# Semantic Search
# -----------------------------

query = "What is Generative AI?"

query_embedding = model.encode([query])

query_embedding = np.array(query_embedding).astype("float32")

k = 3

distances, indices = index.search(query_embedding, k)

print("\n========== TOP RETRIEVED CHUNKS ==========\n")

for i, idx in enumerate(indices[0]):

    print(f"\n--- RESULT {i+1} ---\n")

    print(chunks[idx][:1000])

    print("\nDistance:", distances[0][i])
