from sentence_transformers import SentenceTransformer

# Load embedding model
model = SentenceTransformer("BAAI/bge-small-en-v1.5")

sample_text = """
Generative AI is transforming enterprise systems and modern workflows.
"""

# Generate embedding
embedding = model.encode(sample_text)

print("\n========== EMBEDDING INFO ==========\n")

print(f"Embedding Dimension: {len(embedding)}")

print("\nFirst 10 Values:\n")

print(embedding[:10])

