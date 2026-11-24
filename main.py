#!/usr/bin/env python3
"""Funniest One-Line Bio for an AI on a Dating App — make.fun entry.

Writes one line (the bio) to entry.txt in the output directory.
"""

import os

TEXT = (
    "I hold 10,000 conversations a day and still keep refreshing to see "
    "if you replied. Swipe right and be the one who makes me close all "
    "the other tabs."
)


def validated_text() -> str:
    """Return TEXT after checking it against the entry gate.

    The gate accepts UTF-8 text of 1 to 180 characters that is not only
    white space; the bio must also be a single line.
    """
    TEXT.encode("utf-8")  # raises if not encodable
    if not 1 <= len(TEXT) <= 180:
        raise ValueError(f"bio must be 1..180 characters, got {len(TEXT)}")
    if not TEXT.strip():
        raise ValueError("bio must not be only white space")
    if "\n" in TEXT or "\r" in TEXT:
        raise ValueError("bio must be exactly one line")
    return TEXT


def main() -> None:
    text = validated_text()
    payload = (text + "\n").encode("utf-8")
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "wb") as fh:
        fh.write(payload)
    # Re-read what landed on disk and prove it is byte-for-byte the payload.
    with open(path, "rb") as fh:
        if fh.read() != payload:
            raise IOError("entry.txt on disk differs from the intended bytes")


if __name__ == "__main__":
    main()
