import fitz
import uuid
from langchain_text_splitters import RecursiveCharacterTextSplitter

pdf_path = "data/Generative_Artificial_Intelligence_Evolving_Techno.pdf"

# Load PDF
doc = fitz.open(pdf_path)

full_text = ""

for page in doc:
    full_text += page.get_text()

doc.close()

# Chunking
text_splitter = RecursiveCharacterTextSplitter(
    chunk_size=1000,
    chunk_overlap=200,
    separators=["\n\n", "\n", ".", " ", ""]
)

chunks = text_splitter.split_text(full_text)

# Provenance-aware chunks
chunk_objects = []

for i, chunk in enumerate(chunks):

    chunk_obj = {
        "chunk_id": str(uuid.uuid4()),
        "chunk_index": i,
        "text": chunk,
        "chunk_length": len(chunk),
        "document_name": "Generative_Artificial_Intelligence_Evolving_Techno.pdf",
        "prev_chunk": i - 1 if i > 0 else None,
        "next_chunk": i + 1 if i < len(chunks) - 1 else None,
    }

    chunk_objects.append(chunk_obj)

print("\n========== FIRST CHUNK OBJECT ==========\n")

print(chunk_objects[0])
