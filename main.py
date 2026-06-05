from tools.patient_loader import (
    load_patient_folder
)

from agents.discharge_agent import (
    initialize_state,
    run_agent
)


PATIENT_FOLDER = "patient_data"


def main():

    pages = load_patient_folder(
        PATIENT_FOLDER
    )

    print(
        f"Loaded {len(pages)} pages"
    )

    state = initialize_state(
        patient_id="patient_1",
        pages=pages
    )

    final_state = run_agent(
        state
    )

    summary = final_state[
        "extracted_data"
    ]

    print(
        "\n\n========== FINAL OUTPUT ==========\n"
    )

    for section, value in summary.items():

        print(
            f"\n{section.upper()}"
        )

        print("=" * 80)

        print(value)

    print(
        "\n\n========== TRACE ==========\n"
    )

    for step in final_state[
        "trace_log"
    ]:

        print(step)


if __name__ == "__main__":

    main()
