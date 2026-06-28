import fitz
import faiss
import numpy as np

from sentence_transformers import SentenceTransformer
from langchain_text_splitters import RecursiveCharacterTextSplitter

from golden_dataset import golden_dataset

# =====================================
# Load Embedding Model
# =====================================

model = SentenceTransformer(
    "BAAI/bge-small-en-v1.5"
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
# Embeddings
# =====================================

embeddings = model.encode(chunks)

embeddings = np.array(embeddings).astype("float32")

dimension = embeddings.shape[1]

index = faiss.IndexFlatL2(dimension)

index.add(embeddings)

# =====================================
# Evaluation
# =====================================

k = 3

print("\n========== PRECISION@K ==========\n")

for sample in golden_dataset:

    query = sample["query"]

    expected_keywords = sample["expected_keywords"]

    query_embedding = model.encode([query])

    query_embedding = np.array(query_embedding).astype(
        "float32"
    )

    distances, indices = index.search(query_embedding, k)

    retrieved_chunks = [
        chunks[idx]
        for idx in indices[0]
    ]

    relevant_count = 0

    for chunk in retrieved_chunks:

        chunk_lower = chunk.lower()

        if any(
            keyword.lower() in chunk_lower
            for keyword in expected_keywords
        ):
            relevant_count += 1

    precision_at_k = relevant_count / k

    print(f"\nQuery: {query}")

    print(f"Precision@{k}: {precision_at_k:.2f}")

