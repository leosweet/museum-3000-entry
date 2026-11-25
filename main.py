#!/usr/bin/env python3
"""Museum of the Year 3000 entry.

Writes one museum label — the label a museum in the year 3000 puts beside
an ordinary object from today — to /output/entry.txt.

Deterministic by design: no network, no randomness, no clock. The label is
a fixed string, so every run writes byte-for-byte identical output.
"""

import os

# The label itself. It answers the brief's core ask — a museum in the year
# 3000 labelling an ordinary object from today — by misreading the smoke
# alarm as a small white bird, i.e. a future curator's wrong-but-plausible
# reading of a familiar thing, not a description of the object as we know it.
LABEL = (
    "Smoke alarm, c. 2025. A small white bird, fixed to the ceiling, "
    "that screamed whenever its humans attempted to cook."
)

EXPECTED_LENGTH = 116


def validate_label(label: str) -> None:
    """Guard the label's fixed form before anything is written.

    The entry is one single-line label of exactly 116 characters; any
    drift here would silently change the submitted artifact, so fail loudly
    with the exact check that broke and the value that broke it.
    """
    if not isinstance(label, str) or not label:
        raise ValueError(f"label must be a non-empty string, got {label!r}")
    if len(label) != EXPECTED_LENGTH:
        raise ValueError(
            f"label must be {EXPECTED_LENGTH} characters, "
            f"got {len(label)}: {label!r}"
        )
    if label != label.strip():
        raise ValueError(f"label has leading/trailing whitespace: {label!r}")
    if "\n" in label or "\r" in label:
        raise ValueError(f"label must be a single line, got newline in: {label!r}")
    if "  " in label:
        raise ValueError(f"label has a double space: {label!r}")
    if not label.endswith("."):
        raise ValueError(f"label must end with a full stop: {label!r}")


def main() -> None:
    validate_label(LABEL)
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(LABEL)


if __name__ == "__main__":
    main()
