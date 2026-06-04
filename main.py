# main.py

from tools.patient_loader import (
    load_patient_folder
)

from agents.discharge_agent import (
    initialize_state,
    run_agent
)


PATIENT_FOLDER = "patient_data"

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

print(
    "\n========== EXTRACTED DATA ==========\n"
)

if isinstance(
        final_state["extracted_data"],
        dict
):

    for key, value in final_state[
        "extracted_data"
    ].items():

        print(
            f"\n{key.upper()}"
        )

        print("-" * 50)

        print(value)

else:

    print(
        final_state["extracted_data"]
    )

print(
    "\n========== REVIEW FLAGS ==========\n"
)

for flag in final_state[
    "review_flags"
]:

    print(flag)

print(
    "\n========== TRACE ==========\n"
)

for step in final_state[
    "trace_log"
]:

    print(step)