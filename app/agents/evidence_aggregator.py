# =====================================
# Simulated Retrieved Evidence
# =====================================

retrieved_evidence = [

    {
        "question":
        "How has AI evolved?",

        "page":
        3,

        "chunk_id":
        "chunk_3_2",

        "evidence":
        """
        AI evolved from symbolic approaches
        toward deep learning and large-scale
        neural networks.
        """
    },

    {
        "question":
        "What business impacts does GenAI create?",

        "page":
        15,

        "chunk_id":
        "chunk_15_11",

        "evidence":
        """
        Generative AI impacts business through
        automation, decision support,
        content generation, and software
        development acceleration.
        """
    }
]

# =====================================
# Aggregate Evidence
# =====================================

aggregated_context = ""

aggregated_sources = []

for item in retrieved_evidence:

    aggregated_context += f"""

QUESTION:
{item['question']}

EVIDENCE:
{item['evidence']}

SOURCE:
PAGE: {item['page']}
CHUNK_ID: {item['chunk_id']}

=========================
"""

    aggregated_sources.append({

        "page":
        item["page"],

        "chunk_id":
        item["chunk_id"]
    })

# =====================================
# Output
# =====================================

print(
    "\n========== AGGREGATED EVIDENCE ==========\n"
)

print(aggregated_context)

print(
    "\n========== SOURCE TRACE ==========\n"
)

for source in aggregated_sources:

    print(source)
