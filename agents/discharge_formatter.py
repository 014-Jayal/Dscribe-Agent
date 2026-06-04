# agents/discharge_formatter.py

def format_discharge_summary(
        extracted_data,
        review_flags
):

    return f"""
DISCHARGE SUMMARY
====================================================

Principal Diagnosis:
{extracted_data.get("principal_diagnosis")}

Secondary Diagnoses:
{', '.join(
    extracted_data.get(
        "secondary_diagnosis",
        []
    )
)}

Hospital Course:
{extracted_data.get("hospital_course")}

Procedures:
{', '.join(
    extracted_data.get(
        "procedures",
        []
    )
)}

Discharge Medications:
{', '.join(
    extracted_data.get(
        "medications",
        []
    )
)}

Allergies:
{extracted_data.get("allergies")}

Pending Results:
{', '.join(
    extracted_data.get(
        "pending_results",
        []
    )
)}

Follow Up:
{extracted_data.get("follow_up")}

Discharge Condition:
{extracted_data.get(
    "discharge_condition"
)}

----------------------------------------------------

CLINICIAN REVIEW FLAGS

{chr(10).join(review_flags)}
"""