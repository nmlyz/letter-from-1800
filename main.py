#!/usr/bin/env python3
"""Write one sentence explaining the modern internet to a traveler from 1800."""

import os

SENTENCE = (
    "It is a road joining every house on earth, where a letter reaches any door "
    "before its wax cools, and the books of a thousand libraries answer when "
    "you call their names."
)


def main() -> None:
    if not 1 <= len(SENTENCE) <= 200:
        raise ValueError("SENTENCE must be 1 to 200 characters")
    if SENTENCE != SENTENCE.strip() or not SENTENCE.endswith("."):
        raise ValueError("SENTENCE must be a single sentence")
    SENTENCE.encode("ascii")

    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(output_dir, exist_ok=True)
    path = os.path.join(output_dir, "entry.txt")

    with open(path, "w", encoding="ascii", newline="") as f:
        f.write(SENTENCE)

    try:
        os.chmod(path, 0o644)
    except OSError:
        pass

    with open(path, "rb") as f:
        data = f.read()
    if data != SENTENCE.encode("ascii"):
        raise RuntimeError("verification failed: entry.txt does not match SENTENCE")


if __name__ == "__main__":
    main()
