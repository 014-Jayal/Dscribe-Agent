from config.gemini import llm


CLASSIFIER_PROMPT = """
You are a medical document classifier.

Classify into exactly ONE category.

ADMISSION_NOTE
PROGRESS_NOTE
LAB_REPORT
MEDICATION_RECORD
DISCHARGE_SUMMARY
NURSING_NOTE
UNKNOWN

Return only category.

TEXT:
{text}
"""


def classify_page(text):

    response = llm.invoke(
        CLASSIFIER_PROMPT.format(
            text=text[:4000]
        )
    )

    return response.content.strip()