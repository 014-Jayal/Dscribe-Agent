from rapidfuzz import fuzz

def similarity_score(
    original,
    edited
):

    return fuzz.ratio(
        original,
        edited
    )