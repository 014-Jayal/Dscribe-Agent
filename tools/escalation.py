# tools/escalation.py

def generate_escalations(
        extracted_data
):

    flags = []

    for key, value in extracted_data.items():

        if (
            value == "NOT_FOUND"
            or value == []
            or value == ""
        ):

            flags.append(
                f"Clinician Review Required: {key}"
            )

    return flags