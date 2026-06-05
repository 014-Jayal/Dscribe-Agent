import re


def extract_admission_medications(pages):

    medications = []

    patterns = [

        r"thyroid.*treatment",

        r"thyroxine",

        r"levothyroxine",

        r"metformin",

        r"amlodipine",

        r"telmisartan"
    ]

    for page in pages:

        text = page.text.lower()

        for pattern in patterns:

            matches = re.findall(
                pattern,
                text
            )

            medications.extend(
                matches
            )

    return list(
        set(medications)
    )
