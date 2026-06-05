from config.gemini import llm


SEARCH_PROMPT = """
You are a clinical extraction agent.

Question:
{question}

Clinical Documents:
{document}

Rules:

1. Use ONLY explicitly stated information.

2. Never hallucinate.

3. Never infer.

4. If information does not exist return:
NOT_FOUND

5. Keep answer concise.

6. Return only extracted information.
"""


def clinical_search(
        question,
        document
):

    response = llm.invoke(
        SEARCH_PROMPT.format(
            question=question,
            document=document[:12000]
        )
    )

    return response.content
