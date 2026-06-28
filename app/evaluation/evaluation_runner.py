from app.evaluation.faithfulness import (
    evaluate_faithfulness
)

from app.evaluation.answer_relevancy import (
    evaluate_answer_relevancy
)

from app.evaluation.context_precision import (
    evaluate_context_precision
)

from app.evaluation.context_recall import (
    evaluate_context_recall
)


def run_evaluation(

    question,

    retrieved_context,

    generated_answer

):

    faithfulness = evaluate_faithfulness(

        question,

        retrieved_context,

        generated_answer
    )

    answer_relevancy = evaluate_answer_relevancy(

        question,

        generated_answer
    )

    context_precision = evaluate_context_precision(

        question,

        retrieved_context
    )

    context_recall = evaluate_context_recall(

        question,

        retrieved_context
    )

    return {

        "faithfulness":
        faithfulness,

        "answer_relevancy":
        answer_relevancy,

        "context_precision":
        context_precision,

        "context_recall":
        context_recall
    }