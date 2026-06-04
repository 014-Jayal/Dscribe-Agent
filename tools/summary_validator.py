# tools/summary_validator.py

REQUIRED_FIELDS = [

    "principal_diagnosis",

    "medications",

    "follow_up",

    "discharge_condition"
]


def validate_summary(data):

    flags = []

    if not isinstance(
        data,
        dict
    ):

        flags.append(
            "Summary is not valid JSON"
        )

        return flags

    for field in REQUIRED_FIELDS:

        value = data.get(
            field,
            None
        )

        if (
            value is None
            or value == ""
            or value == []
            or value == "NOT_FOUND"
        ):

            flags.append(
                f"Missing {field}"
            )

    return flags