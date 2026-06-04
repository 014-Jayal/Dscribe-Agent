from pydantic import BaseModel
from typing import List


class SourceReference(BaseModel):
    value: str
    source_document: str
    page_number: int


class MedicationChange(BaseModel):
    medication: str
    change_type: str
    reason: str | None = None


class DischargeSummary(BaseModel):

    patient_demographics: str

    admission_date: str

    discharge_date: str

    principal_diagnosis: str

    secondary_diagnoses: List[str]

    hospital_course: str

    procedures: List[str]

    discharge_medications: List[str]

    medication_changes: List[MedicationChange]

    allergies: str

    follow_up_instructions: List[str]

    pending_results: List[str]

    discharge_condition: str

    conflicts: List[str]

    clinician_review_flags: List[str]