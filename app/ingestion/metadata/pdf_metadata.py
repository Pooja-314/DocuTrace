import fitz
import os

pdf_path = "data/Generative_Artificial_Intelligence_Evolving_Techno.pdf"

doc = fitz.open(pdf_path)

# PDF metadata
metadata = doc.metadata

print("\n========== DOCUMENT METADATA ==========\n")

print(f"Filename: {os.path.basename(pdf_path)}")
print(f"Total Pages: {doc.page_count}")

print(f"Title: {metadata.get('title')}")
print(f"Author: {metadata.get('author')}")
print(f"Subject: {metadata.get('subject')}")
print(f"Creator: {metadata.get('creator')}")
print(f"Producer: {metadata.get('producer')}")
print(f"Creation Date: {metadata.get('creationDate')}")

# Page-level statistics
print("\n========== PAGE STATS ==========\n")

for page_num, page in enumerate(doc):
    text = page.get_text()

    print(
        f"Page {page_num + 1} "
        f"| Characters: {len(text)} "
        f"| Words: {len(text.split())}"
    )

doc.close()
