from tools.retriever import get_relevant_pages
from tools.clinical_search import clinical_search


def extract_all_sections(pages):

    relevant_pages = pages

    combined_text = "\n".join(
        page.text
        for page in relevant_pages
    )

    question = """
Extract the following as JSON.

{
  "demographics":"",
  "admission_date":"",
  "discharge_date":"",
  "principal_diagnosis":"",
  "secondary_diagnosis":[],
  "hospital_course":"",
  "procedures":[],
  "medications":[],
  "allergies":"",
  "follow_up":"",
  "pending_results":[],
  "discharge_condition":""
}

Rules:

1. Never hallucinate.
2. If unavailable use NOT_FOUND.
3. Return JSON only.
"""

    return clinical_search(
        question,
        combined_text
    )