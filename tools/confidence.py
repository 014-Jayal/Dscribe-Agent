# tools/confidence.py

def calculate_confidence(
        value,
        sources_count=0
):

    if value in [
        None,
        "",
        [],
        "NOT_FOUND"
    ]:
        return 0.0

    if sources_count >= 2:
        return 0.95

    if sources_count == 1:
        return 0.85

    return 0.70