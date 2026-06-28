import ollama


def evaluate_context_recall(
    question,
    retrieved_context
):

    evaluation_prompt = f"""
You are a retrieval evaluation system.

QUESTION:
{question}

RETRIEVED CONTEXT:
{retrieved_context}

Evaluate whether the retrieved context
contains enough information to answer
the question completely.

Return ONLY:

LABEL: HIGH

RECALL: 0.95

or

LABEL: MEDIUM

RECALL: 0.50

or

LABEL: LOW

RECALL: 0.10
"""

    response = ollama.chat(

        model="phi3",

        messages=[
            {
                "role": "user",
                "content": evaluation_prompt
            }
        ]
    )

    result = response[
        "message"
    ][
        "content"
    ].strip()

    label = "UNKNOWN"
    recall = 0.0

    for line in result.split("\n"):

        line = line.strip()

        upper_line = line.upper()

        if upper_line.startswith(
            "LABEL:"
        ):

            label = (
                line.split(
                    ":",
                    1
                )[1]
                .strip()
            )

        elif upper_line.startswith(
            "RECALL:"
        ):

            try:

                recall = float(

                    line.split(
                        ":",
                        1
                    )[1]
                    .strip()

                )

            except:

                recall = 0.0

    return {

        "label": label,

        "recall": recall

    }