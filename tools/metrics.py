# tools/metrics.py

def calculate_evidence_coverage(
        extracted_data
):

    total = len(extracted_data)

    grounded = 0

    for field, info in extracted_data.items():

        if info.get("sources"):

            grounded += 1

    return round(
        grounded / total * 100,
        2
    )