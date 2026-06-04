import re

PENDING_TERMS = [
    "awaited",
    "pending",
    "awaiting",
    "in process",
    "report awaited"
]


def detect_pending(text):

    findings = []

    sentences = re.split(
        r"[.\n]",
        text
    )

    for sentence in sentences:

        sentence = sentence.strip()

        if not sentence:
            continue

        for term in PENDING_TERMS:

            if term.lower() in sentence.lower():

                findings.append(sentence)

                break

    return findings