# agents/extractor.py

from tools.clinical_search import clinical_search
from learning.memory import load_rules


def extract_all_sections(pages):

    combined_text = "\n".join(
        page.text
        for page in pages
    )

    learned_rules = load_rules()

    memory_section = ""

    if learned_rules:

        memory_section = (
            "\n\nPREVIOUS CLINICIAN PREFERENCES:\n"
            + "\n".join(
                f"- {rule}"
                for rule in learned_rules
            )
        )

    prompt = f"""
You are a Clinical Discharge Extraction Agent.

TASK:
Extract structured discharge information from the provided clinical documents.

CRITICAL SAFETY RULES:

1. NEVER hallucinate.
2. NEVER infer.
3. NEVER invent values.
4. ONLY use information explicitly found.
5. If unavailable return NOT_FOUND.
6. If conflicting values exist:
   return BOTH values.
7. Return VALID JSON ONLY.
8. No markdown.
9. No explanations.

IMPORTANT:

You may follow previously learned
clinician formatting preferences
ONLY if they do not conflict
with source documents.

{memory_section}

Search ALL pages carefully.

Demographics may appear under:
- Patient Details
- Registration
- Demographic Details
- Gender
- Age
- Patient Information

Admission Date may appear as:
- DOA
- Admission Date
- Date of Admission

Discharge Date may appear as:
- DOD
- Discharge Date
- Date of Discharge

Return JSON:

{{
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
}}
"""

    return clinical_search(
        prompt,
        combined_text[:25000]
    )