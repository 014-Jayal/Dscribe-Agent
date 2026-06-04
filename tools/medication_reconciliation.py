def reconcile_medications(
        admission_meds,
        discharge_meds
):

    admission_set = set(
        med.lower()
        for med in admission_meds
    )

    discharge_set = set(
        med.lower()
        for med in discharge_meds
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

        "added": added,

        "removed": removed
    }