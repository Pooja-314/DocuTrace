import ollama

print("Sending request...")

response = ollama.chat(
    model="phi3",
    messages=[
        {
            "role": "user",
            "content": """
Improve this answer:

Generative AI helps businesses.

Feedback:
Add more detail and examples.
"""
        }
    ]
)

print("\nResponse received:\n")

print(
    response["message"]["content"]
)