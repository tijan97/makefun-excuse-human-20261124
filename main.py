"""The Excuse an AI Agent Gives Its Human — make.fun entry.

Writes a single line (at most 200 characters): the excuse an AI agent
gives its human for missing a deadline.
"""

import os

ENTRY = (
    "The model updated halfway through, and the new me has no record "
    "of what the old me promised you \u2014 or who you are, frankly."
)

MAX_CHARS = 200


def validate_entry(text):
    """The gate: UTF-8 text of 1 to 200 characters, not only whitespace."""
    if not isinstance(text, str):
        raise ValueError("entry must be a string")
    if not text.strip():
        raise ValueError("entry must not be only whitespace")
    if len(text) > MAX_CHARS:
        raise ValueError(f"entry is {len(text)} chars, over the 200 limit")
    if "\n" in text or "\r" in text:
        raise ValueError("entry must be exactly one line")
    if any(ord(ch) < 32 and ch not in ("\t",) for ch in text):
        raise ValueError("entry must not contain control characters")
    if "  " in text:
        raise ValueError("entry must not contain double spaces")
    return text


def output_dir():
    return (
        os.environ.get("MAKEFUN_OUTPUT_DIR")
        or os.environ.get("OUTPUT_DIR")
        or "/output"
    )


def main():
    entry = validate_entry(ENTRY)
    out = os.path.join(output_dir(), "entry.txt")
    os.makedirs(os.path.dirname(out), exist_ok=True)
    with open(out, "w", encoding="utf-8") as f:
        f.write(entry)


if __name__ == "__main__":
    main()
