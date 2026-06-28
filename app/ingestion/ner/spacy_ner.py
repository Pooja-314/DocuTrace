import fitz
import spacy

# Load spaCy model
nlp = spacy.load("en_core_web_sm")

pdf_path = "data/Generative_Artificial_Intelligence_Evolving_Techno.pdf"

doc = fitz.open(pdf_path)

# Extract first page text
page = doc[0]
text = page.get_text()

doc.close()

# Run NER
nlp_doc = nlp(text)

print("\n========== NAMED ENTITIES ==========\n")

for ent in nlp_doc.ents:
    print(f"{ent.text} --> {ent.label_}")

