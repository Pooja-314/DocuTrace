import ollama


def evaluate_answer_relevancy(
    question,
    answer
):

    evaluation_prompt = f"""
You are an answer evaluation system.

QUESTION:
{question}

ANSWER:
{answer}

Evaluate how well the answer addresses
the user's question.

Return ONLY:

LABEL: RELEVANT

CONFIDENCE: 0.95

or

LABEL: NOT_RELEVANT

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