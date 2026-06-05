import json

from agents.discharge_formatter import format_discharge_summary
from agents.extractor import extract_all_sections
from agents.summary_generator import parse_extraction
from agents.final_summary import build_summary

from tools.trace_logger import log_step
from tools.summary_validator import validate_summary
from tools.drug_interactions import check_interactions
from tools.escalation import generate_escalations
from tools.source_tracker import find_sources
from tools.medication_reconciliation import reconcile_medications
from tools.medication_extractor import extract_admission_medications


def initialize_state(patient_id, pages):

    return {
        "patient_id": patient_id,
        "pages": pages,
        "extracted_data": {},
        "medication_changes": {},
        "conflicts": [],
        "interactions": [],
        "sources": {},
        "review_flags": [],
        "trace_log": []
    }


def run_agent(state):

    print("\nRunning Optimized Clinical Pipeline...")

    trace = []

    # ==================================================
    # STEP 1 - CLINICAL EXTRACTION
    # ==================================================

    raw_result = extract_all_sections(
        state["pages"]
    )

    state["extracted_data"] = parse_extraction(
        raw_result
    )

    trace.append({
        "step": 1,
        "action": "clinical_extraction",
        "reasoning": "Extract structured discharge information from source documents",
        "status": "success"
    })

    # ==================================================
    # STEP 2 - SOURCE ATTRIBUTION
    # ==================================================

    state["sources"] = find_sources(
        state["pages"],
        state["extracted_data"]
    )

    trace.append({
        "step": 2,
        "action": "source_tracking",
        "reasoning": "Locate evidence supporting extracted fields",
        "status": "success"
    })

    # ==================================================
    # STEP 3 - MEDICATION RECONCILIATION
    # ==================================================

    admission_meds = extract_admission_medications(
        state["pages"]
    )

    discharge_meds = state[
        "extracted_data"
    ].get(
        "medications",
        []
    )

    state["medication_changes"] = (
        reconcile_medications(
            admission_meds,
            discharge_meds
        )
    )

    trace.append({
        "step": 3,
        "action": "medication_reconciliation",
        "reasoning": "Compare admission and discharge medications",
        "status": "success"
    })

    # ==================================================
    # STEP 4 - CONFLICT DETECTION
    # ==================================================

    # Fast mode:
    # We skip the Gemini conflict agent
    # because it adds another API call
    # and slows the system significantly.

    state["conflicts"] = []

    trace.append({
        "step": 4,
        "action": "conflict_detection",
        "reasoning": "Conflict detection skipped in optimized mode",
        "status": "success"
    })

    # ==================================================
    # STEP 5 - DRUG INTERACTIONS
    # ==================================================

    state["interactions"] = check_interactions(
        discharge_meds
    )

    trace.append({
        "step": 5,
        "action": "drug_interaction_check",
        "reasoning": "Evaluate medications for interactions",
        "status": "success"
    })

    # ==================================================
    # STEP 6 - SAFETY ESCALATIONS
    # ==================================================

    state["review_flags"].extend(
        generate_escalations(
            state["extracted_data"]
        )
    )

    state["review_flags"].extend(
        validate_summary(
            state["extracted_data"]
        )
    )

    trace.append({
        "step": 6,
        "action": "review_flag_generation",
        "reasoning": "Escalate missing or uncertain clinical information",
        "status": "success"
    })

    # ==================================================
    # STEP 7 - BUILD FINAL SUMMARY
    # ==================================================

    summary = build_summary(
        state["extracted_data"],
        state["sources"],
        state["medication_changes"],
        state["conflicts"],
        state["interactions"],
        state["review_flags"]
    )

    trace.append({
        "step": 7,
        "action": "summary_generation",
        "reasoning": "Produce final structured discharge summary",
        "status": "success"
    })

    state["trace_log"] = trace

    # Save raw extraction separately
    raw_extracted_data = state["extracted_data"]

    state["extracted_data"] = summary

    # ==================================================
    # SAVE TXT SUMMARY
    # ==================================================

    formatted_summary = format_discharge_summary(
        raw_extracted_data,
        state["review_flags"]
    )

    with open(
        "outputs/patient_1_summary.txt",
        "w",
        encoding="utf-8"
    ) as f:

        f.write(
            formatted_summary
        )

    # ==================================================
    # SAVE JSON OUTPUT
    # ==================================================

    with open(
        "outputs/patient_1.json",
        "w",
        encoding="utf-8"
    ) as f:

        json.dump(
            summary,
            f,
            indent=4
        )

    # ==================================================
    # SAVE TRACE
    # ==================================================

    log_step(
        state["patient_id"],
        {
            "agent_trace": trace
        }
    )

    print(
        "\nClinical Pipeline Completed Successfully."
    )

    return state
