import json
from pathlib import Path

MEMORY_FILE = Path(
    "memory/learned_rules.json"
)

def load_rules():

    if not MEMORY_FILE.exists():
        return []

    with open(
        MEMORY_FILE,
        "r",
        encoding="utf-8"
    ) as f:

        return json.load(f)

def save_rule(rule):

    rules = load_rules()

    if rule not in rules:
        rules.append(rule)

    with open(
        MEMORY_FILE,
        "w",
        encoding="utf-8"
    ) as f:

        json.dump(
            rules,
            f,
            indent=4
        )