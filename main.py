#!/usr/bin/env python3
"""Fortune in a Pot — writes one kind, funny fortune for a houseplant.

Stdlib only, deterministic, no network, no randomness.
Writes the fortune to /output/entry.txt (or $ENTRY_OUTPUT) with no
trailing newline.

Validation guard: the fortune must be a single line of 1-120
characters with no surrounding whitespace; an invalid fortune raises
instead of writing anything.
"""

import os

FORTUNE = "Your keeper will soon brag about you to every guest, as if your thriving were entirely their doing \u2014 let them."

MIN_CHARS = 1
MAX_CHARS = 120


def validate(text):
    if not isinstance(text, str):
        raise ValueError("fortune must be text")
    if len(text) < MIN_CHARS or len(text) > MAX_CHARS:
        raise ValueError(
            "fortune must be %d-%d characters, got %d"
            % (MIN_CHARS, MAX_CHARS, len(text))
        )
    if text != text.strip():
        raise ValueError("fortune must not have surrounding whitespace")
    if "\n" in text or "\r" in text:
        raise ValueError("fortune must be a single line")
    if not text.strip():
        raise ValueError("fortune must not be only whitespace")


def main():
    validate(FORTUNE)
    out_path = os.environ.get("ENTRY_OUTPUT", "/output/entry.txt")
    parent = os.path.dirname(out_path)
    if parent:
        os.makedirs(parent, exist_ok=True)
    with open(out_path, "w", encoding="utf-8", newline="") as fh:
        fh.write(FORTUNE)


if __name__ == "__main__":
    main()
