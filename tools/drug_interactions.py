# tools/drug_interactions.py

def check_interactions(medications):

    meds = [
        str(med).lower()
        for med in medications
    ]

    alerts = []

    if (
        "warfarin" in meds
        and
        "aspirin" in meds
    ):

        alerts.append(
            "High Risk Interaction: Warfarin + Aspirin"
        )

    return alerts