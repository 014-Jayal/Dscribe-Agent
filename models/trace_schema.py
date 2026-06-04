from pydantic import BaseModel


class TraceStep(BaseModel):
    step: int

    reasoning: str

    action: str

    tool_input: str

    tool_output: str

    next_decision: str