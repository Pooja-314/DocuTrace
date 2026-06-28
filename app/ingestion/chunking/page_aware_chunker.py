import fitz
import uuid
from langchain_text_splitters import RecursiveCharacterTextSplitter

pdf_path = "data/Generative_Artificial_Intelligence_Evolving_Techno.pdf"

doc = fitz.open(pdf_path)

text_splitter = RecursiveCharacterTextSplitter(
    chunk_size=1000,
    chunk_overlap=200,
    separators=["\n\n", "\n", ".", " ", ""]
)

all_chunks = []

for page_num, page in enumerate(doc):

    page_text = page.get_text()

    chunks = text_splitter.split_text(page_text)

    for chunk_idx, chunk in enumerate(chunks):

        chunk_obj = {
            "chunk_id": str(uuid.uuid4()),
            "document_name": "Generative_Artificial_Intelligence_Evolving_Techno.pdf",
            "page_number": page_num + 1,
            "chunk_index": chunk_idx,
            "text": chunk,
            "chunk_length": len(chunk),
        }

        all_chunks.append(chunk_obj)

doc.close()

print("\n========== FIRST PAGE-AWARE CHUNK ==========\n")

print(all_chunks[0])