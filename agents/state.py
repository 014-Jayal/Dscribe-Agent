from typing import TypedDict, List, Dict


class AgentState(TypedDict):

    patient_id: str

    pages: list

    classified_pages: list

    extracted_data: Dict

    conflicts: List[str]

    pending_results: List[str]

    review_flags: List[str]

    trace_log: List[dict]

    completed_sections: List[str]

    current_goal: str

    step_count: int