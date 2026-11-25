#!/usr/bin/env python3
"""Museum of the Year 3000 entry.

Writes one museum label — the label a museum in the year 3000 puts beside
an ordinary object from today — to /output/entry.txt.

Deterministic by design: no network, no randomness, no clock. The label is
a fixed string, so every run writes byte-for-byte identical output.
"""

import os

LABEL = (
    "Smoke alarm, c. 2025. A small white bird, fixed to the ceiling, "
    "that screamed whenever its humans attempted to cook."
)


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(LABEL)


if __name__ == "__main__":
    main()
