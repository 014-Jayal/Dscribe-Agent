# agents/summary_generator.py

import json


def parse_extraction(raw_output):

    if isinstance(raw_output, dict):
        return raw_output

    if not raw_output:
        return {}

    raw_output = str(raw_output).strip()

    if raw_output.startswith("```json"):
        raw_output = raw_output.replace(
            "```json",
            ""
        )

        raw_output = raw_output.replace(
            "```",
            ""
        )

    if raw_output.startswith("```"):
        raw_output = raw_output.replace(
            "```",
            ""
        )

    raw_output = raw_output.strip()

    try:

        return json.loads(raw_output)

    except Exception as e:

        return {
            "parse_error": str(e),
            "raw_output": raw_output
        }