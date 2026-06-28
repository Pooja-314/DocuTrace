import fitz

from rank_bm25 import BM25Okapi
from langchain_text_splitters import RecursiveCharacterTextSplitter

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
    chunk_size=500,
    chunk_overlap=100
)

chunks = text_splitter.split_text(full_text)

print(f"\nTotal Chunks: {len(chunks)}")

# -----------------------------
# Tokenize for BM25
# -----------------------------

tokenized_chunks = [chunk.split() for chunk in chunks]

# -----------------------------
# Build BM25 Index
# -----------------------------

bm25 = BM25Okapi(tokenized_chunks)

# -----------------------------
# Query
# -----------------------------

query = "What is Generative AI?"

tokenized_query = query.split()

# -----------------------------
# Search
# -----------------------------

scores = bm25.get_scores(tokenized_query)

top_k = 3

top_indices = sorted(
    range(len(scores)),
    key=lambda i: scores[i],
    reverse=True
)[:top_k]

print("\n========== BM25 RESULTS ==========\n")

for rank, idx in enumerate(top_indices):

    print(f"\n--- RESULT {rank+1} ---\n")

    print(chunks[idx][:1000])

    print("\nBM25 Score:", scores[idx])

