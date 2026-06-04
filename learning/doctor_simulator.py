def doctor_edit(summary):

    edited = summary

    edited = edited.replace(
        "Hemodynamically stable",
        "Clinically stable at discharge"
    )

    edited = edited.replace(
        "NOT_FOUND",
        "Not documented"
    )

    edited = edited.replace(
        "Review immediately",
        "Follow-up immediately"
    )

    return edited