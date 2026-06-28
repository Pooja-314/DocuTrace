from faithfulness import (
    evaluate_faithfulness
)

question = (
    "How has Generative AI evolved?"
)

context = """
Generative AI evolved from earlier AI systems.
Since 2017 the focus has shifted toward
natural language processing and generative
applications.
"""

answer = """
Generative AI evolved toward natural language
processing and generative applications after
2017.
"""

result = evaluate_faithfulness(

    question,
    context,
    answer
)

print(
    "\nFaithfulness Result:"
)


print(
    f"Label: {result['label']}"
)

print(
    f"Confidence: {result['confidence']}"
)