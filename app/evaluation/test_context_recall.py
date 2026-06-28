from context_recall import (
    evaluate_context_recall
)

question = (
    "How has Generative AI evolved?"
)

retrieved_context = """
Generative AI evolved from earlier AI
systems.

Since 2017, research has increasingly
focused on natural language processing
and generative applications.

Large language models accelerated
this trend.
"""

result = evaluate_context_recall(

    question,

    retrieved_context

)

print(
    "\nContext Recall Result:\n"
)

print(
    f"Label: {result['label']}"
)

print(
    f"Recall: {result['recall']}"
)