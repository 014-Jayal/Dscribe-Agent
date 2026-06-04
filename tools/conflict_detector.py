def detect_conflicts(data):

    conflicts = []

    principal = data.get(
        "principal_diagnosis",
        ""
    )

    secondary = data.get(
        "secondary_diagnosis",
        []
    )

    if (
        principal
        and
        principal in secondary
    ):

        conflicts.append(
            "Diagnosis duplication"
        )

    return conflicts