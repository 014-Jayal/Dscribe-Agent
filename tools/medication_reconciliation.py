def reconcile_medications(

        admission_medications,

        discharge_medications

):

    admission_set = set(

        str(med).lower()

        for med in admission_medications
    )

    discharge_set = set(

        str(med).lower()

        for med in discharge_medications
    )

    added = list(
        discharge_set -
        admission_set
    )

    removed = list(
        admission_set -
        discharge_set
    )

    return {

        "added":
            added,

        "removed":
            removed,

        "modified":
            []
    }
