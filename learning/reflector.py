import sys
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parent.parent

if str(PROJECT_ROOT) not in sys.path:
    sys.path.append(str(PROJECT_ROOT))

from config.gemini import llm

PROMPT = """
You are reviewing how a doctor edited an AI generated discharge summary.

ORIGINAL:
{original}

DOCTOR EDITED:
{edited}

Identify:

1. What changed?
2. Why was it changed?
3. What reusable rule should the AI learn?

Return JSON:

{{
    "change":"",
    "reason":"",
    "learned_rule":""
}}
"""

import json
import re

def generate_rule(original, edited):

    response = llm.invoke(
        PROMPT.format(
            original=original,
            edited=edited
        )
    )

    text = response.content

    try:

        text = text.replace(
            "```json",
            ""
        ).replace(
            "```",
            ""
        ).strip()

        data = json.loads(text)

        return data.get(
            "learned_rule",
            text
        )

    except Exception:

        match = re.search(
            r'"learned_rule"\s*:\s*"([^"]+)"',
            text
        )

        if match:
            return match.group(1)

        return text