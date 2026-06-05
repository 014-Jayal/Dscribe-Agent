SECTION_KEYWORDS = {

    "demographics": [
        "patient",
        "gender",
        "female",
        "male"
    ],

    "admission_date": [
        "admission",
        "date of admission"
    ],

    "discharge_date": [
        "discharge",
        "date of discharge"
    ],

    "principal_diagnosis": [
        "diagnosis",
        "final diagnosis"
    ],

    "secondary_diagnosis": [
        "diagnosis",
        "comorbid"
    ],

    "hospital_course": [
        "hospital course",
        "treatment",
        "presented"
    ],

    "procedures": [
        "procedure",
        "operation",
        "surgery"
    ],

    "medications": [
        "medication",
        "medicine",
        "drug",
        "tablet",
        "capsule"
    ],

    "allergies": [
        "allergy",
        "allergies"
    ],

    "follow_up": [
        "follow up",
        "review after"
    ],

    "pending_results": [
        "awaited",
        "pending",
        "awaiting"
    ],

    "discharge_condition": [
        "discharge condition",
        "stable"
    ]
}


def get_relevant_pages(
        pages,
        section_name
):

    keywords = SECTION_KEYWORDS.get(
        section_name,
        []
    )

    matched_pages = []

    for page in pages:

        page_text = page.text.lower()

        for keyword in keywords:

            if keyword.lower() in page_text:

                matched_pages.append(page)

                break

    if not matched_pages:

        matched_pages = pages[:5]

    return matched_pages
