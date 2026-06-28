import fitz  # PyMuPDF

pdf_path = "data/Generative_Artificial_Intelligence_Evolving_Techno.pdf"

doc = fitz.open(pdf_path)

full_text = ""

for page_num, page in enumerate(doc):
    text = page.get_text()

    print(f"\n--- PAGE {page_num + 1} ---\n")
    print(text[:1000])  # print first 1000 chars

    full_text += text

doc.close()

print("\n\n========== FULL DOCUMENT LOADED ==========")
print(f"Total Characters: {len(full_text)}")
