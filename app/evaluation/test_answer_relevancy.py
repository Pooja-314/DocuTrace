from answer_relevancy import (
    evaluate_answer_relevancy
)

question = (
    "How has Generative AI evolved?"
)

answer = """
Generative AI evolved toward natural
language processing and generative
applications after 2017.
"""

result = evaluate_answer_relevancy(

    question,

    answer

)

print(
    "\nAnswer Relevancy Result:\n"
)

print(
    f"Label: {result['label']}"
)

print(
    f"Confidence: {result['confidence']}"
)