import fitz
import faiss
import numpy as np
import ollama

from sentence_transformers import (
    SentenceTransformer,
    CrossEncoder
)

from langchain_text_splitters import (
    RecursiveCharacterTextSplitter
)

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


# =====================================
# Chunking
# =====================================

text_splitter = RecursiveCharacterTextSplitter(
    chunk_size=200,
    chunk_overlap=20
)

chunk_objects = []

for page_num, page in enumerate(doc):

    page_text = page.get_text()

    split_chunks = text_splitter.split_text(
        page_text
    )

    for chunk_idx, chunk in enumerate(
        split_chunks
    ):

        chunk_objects.append({

            "chunk_id":
            f"chunk_{page_num+1}_{chunk_idx}",

            "page_number":
            page_num + 1,

            "text":
            chunk
        })

chunks = [
    obj["text"]
    for obj in chunk_objects
]

doc.close()

# =====================================
# Embeddings
# =====================================

embeddings = embedding_model.encode(chunks)

embeddings = np.array(embeddings).astype("float32")

dimension = embeddings.shape[1]

# =====================================
# FAISS Index
# =====================================

index = faiss.IndexFlatL2(dimension)

index.add(embeddings)

# =====================================
# User Query
# =====================================

query = "What is Generative AI?"

# =====================================
# Retrieval
# =====================================

query_embedding = embedding_model.encode([query])

query_embedding = np.array(query_embedding).astype(
    "float32"
)

k = 2

distances, indices = index.search(
    query_embedding,
    k
)

retrieved_chunks = [
    chunk_objects[idx]
    for idx in indices[0]
]


# =====================================
# Reranking
# =====================================

pairs = [ 
    [query, chunk["text"]] 
    for chunk in retrieved_chunks 
    ]

scores = reranker.predict(pairs)

reranked_results = sorted(
    zip(retrieved_chunks, scores),
    key=lambda x: x[1],
    reverse=True
)

# =====================================
# Final Context
# =====================================

top_chunks = reranked_results[:1]

context = ""

for chunk_obj, score in top_chunks:

    context += f"""
PAGE: {chunk_obj['page_number']}
CHUNK: {chunk_obj['chunk_id']}

{chunk_obj['text'][:300]}
"""




# =====================================
# Prompt
# =====================================

prompt = f"""
You are DocuTrace, an enterprise document intelligence system.

STRICT RULES:
1. Answer ONLY from the provided context.
2. Do NOT invent information.
3. Use ONLY the provided PAGE and CHUNK_ID values.
4. NEVER create fake citations.
5. If answer is missing, say:
   "I could not find the answer in the document."

Context:
{context}

Question:
{query}

Return response in EXACT format:

ANSWER:
<grounded answer>

CITATIONS:
- PAGE: <page number>
  CHUNK_ID: <chunk id>
"""

# =====================================
# LLM Generation
# =====================================

response = ollama.chat(
    model="phi3",
    messages=[
        {
            "role": "user",
            "content": prompt
        }
    ]
)

# =====================================
# Output
# =====================================

print("\n========== GENERATED ANSWER ==========\n")

print(response["message"]["content"])

