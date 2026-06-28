from evaluation_runner import (
    run_evaluation
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

generated_answer = """
Generative AI evolved toward natural
language processing and generative
applications after 2017.
"""

result = run_evaluation(

    question,

    retrieved_context,

    generated_answer
)

print(
    "\n========== EVALUATION REPORT ==========\n"
)

print(
    f"Faithfulness: "
    f"{result['faithfulness']['label']} "
    f"({result['faithfulness']['confidence']})"
)

print(
    f"Answer Relevancy: "
    f"{result['answer_relevancy']['label']} "
    f"({result['answer_relevancy']['confidence']})"
)

print(
    f"Context Precision: "
    f"{result['context_precision']['label']} "
    f"({result['context_precision']['precision']})"
)

print(
    f"Context Recall: "
    f"{result['context_recall']['label']} "
    f"({result['context_recall']['recall']})"
)