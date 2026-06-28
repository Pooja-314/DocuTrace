import fitz
from pprint import pprint

pdf_path = "data/Generative_Artificial_Intelligence_Evolving_Techno.pdf"

doc = fitz.open(pdf_path)

document_pages = []

for page_num, page in enumerate(doc):

    text = page.get_text()

    page_data = {
        "page_number": page_num + 1,
        "text": text,
        "char_count": len(text),
        "word_count": len(text.split()),
    }

    document_pages.append(page_data)

doc.close()

print("\n========== FIRST PAGE OBJECT ==========\n")

pprint(document_pages[0])

