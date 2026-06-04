def check_interactions(
        medications
):

    meds = [
        med.lower()
        for med in medications
    ]

    alerts = []

    if (
        "warfarin" in meds
        and
        "aspirin" in meds
    ):

        alerts.append(
            "Severe interaction: Warfarin + Aspirin"
        )

    return alerts