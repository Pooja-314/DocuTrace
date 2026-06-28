# =====================================
# Faithfulness Evaluator
# =====================================

import ollama


def evaluate_faithfulness(
    question,
    context,
    answer
):

    evaluation_prompt = f"""
You are a document evaluation system.

QUESTION:
{question}

CONTEXT:
{context}

ANSWER:
{answer}

Evaluate whether the answer is supported
by the context.

Return ONLY in this format:

LABEL: SUPPORTED

CONFIDENCE: 0.95

or

LABEL: UNSUPPORTED

CONFIDENCE: 0.25
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
    confidence = 0.0

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
            "CONFIDENCE:"
        ):

            try:

                confidence = float(

                    line.split(
                        ":",
                        1
                    )[1]
                    .strip()

                )

            except:

                confidence = 0.0

    return {

        "label": label,

        "confidence": confidence

    }