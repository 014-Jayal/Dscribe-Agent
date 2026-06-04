import json
from pathlib import Path


def log_step(patient_id, step_data):

    trace_file = Path(
        f"traces/{patient_id}_trace.json"
    )

    if trace_file.exists():

        data = json.loads(
            trace_file.read_text()
        )

    else:
        data = []

    data.append(step_data)

    trace_file.write_text(
        json.dumps(
            data,
            indent=4
        )
    )