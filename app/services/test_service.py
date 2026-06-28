from app.services.document_service import answer_question
from pprint import pprint

result = answer_question(
    "How has Generative AI evolved?"
)

print(result.keys())
pprint(result)