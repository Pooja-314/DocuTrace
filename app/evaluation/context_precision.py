import ollama


def evaluate_context_precision(
    question,
    retrieved_context
):

    evaluation_prompt = f"""
You are a retrieval evaluation system.

QUESTION:
{question}

RETRIEVED CONTEXT:
{retrieved_context}

Evaluate how relevant the retrieved
context is for answering the question.

Return ONLY:

LABEL: HIGH

PRECISION: 0.95

or

LABEL: MEDIUM

PRECISION: 0.50

or

LABEL: LOW

PRECISION: 0.10
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
    
    print(
    "\nRAW RESPONSE:\n"
    )

    print(
        result
    )

    label = "UNKNOWN"
    precision = 0.0

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
            "PRECISION:"
        ):

            try:

                precision = float(

                    line.split(
                        ":",
                        1
                    )[1]
                    .strip()

                )

            except:

                precision = 0.0

    return {

        "label": label,

        "precision": precision

    }