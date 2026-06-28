import fitz
from langchain_text_splitters import RecursiveCharacterTextSplitter
pdf_path = "data/Generative_Artificial_Intelligence_Evolving_Techno.pdf"

# Load PDF
doc = fitz.open(pdf_path)

full_text = ""

for page in doc:
    full_text += page.get_text()

doc.close()

# Recursive chunker
text_splitter = RecursiveCharacterTextSplitter(
    chunk_size=1000,
    chunk_overlap=200,
    separators=["\n\n", "\n", ".", " ", ""]
)

chunks = text_splitter.split_text(full_text)

print("\n========== CHUNK STATS ==========\n")

print(f"Total Chunks: {len(chunks)}")

for i, chunk in enumerate(chunks[:3]):

    print(f"\n--- CHUNK {i+1} ---\n")
    print(chunk[:1000])
    print("\nChunk Length:", len(chunk))

