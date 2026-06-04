# agents/discharge_agent.py

from agents.extractor import extract_all_sections
from agents.summary_generator import parse_extraction

from tools.trace_logger import log_step
from tools.summary_validator import validate_summary


def initialize_state(
        patient_id,
        pages
):

    return {

        "patient_id": patient_id,

        "pages": pages,

        "extracted_data": {},

        "review_flags": [],

        "trace_log": []
    }


def run_agent(state):

    print(
        "\nRunning Unified Extraction..."
    )

    raw_result = extract_all_sections(
        state["pages"]
    )

    parsed_result = parse_extraction(
        raw_result
    )

    state["extracted_data"] = parsed_result

    trace = {

        "step": 1,

        "reasoning":
            "Unified Extraction",

        "tool":
            "extract_all_sections",

        "input":
            "all patient pages",

        "result":
            str(parsed_result)[:1000],

        "next_decision":
            "validate summary"
    }

    log_step(
        state["patient_id"],
        trace
    )

    state["trace_log"].append(
        trace
    )

    validation_flags = validate_summary(
        parsed_result
    )

    state["review_flags"].extend(
        validation_flags
    )

    return state