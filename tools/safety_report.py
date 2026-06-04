# tools/safety_report.py

def build_safety_report(
        review_flags
):

    return {

        "safe_for_review":
            len(review_flags) == 0,

        "review_flags":
            review_flags
    }