#!/usr/bin/env python3
"""Write one sentence explaining the modern internet to a traveler from 1800."""

import os

SENTENCE = (
    "It is a road joining every house on earth, where a letter reaches any door "
    "before its wax cools, and the books of a thousand libraries answer when "
    "you call their names."
)


def validate_sentence(sentence: str) -> bytes:
    if not 1 <= len(sentence) <= 200:
        raise ValueError("SENTENCE must be 1 to 200 characters")
    if sentence != sentence.strip() or not sentence.endswith("."):
        raise ValueError("SENTENCE must be a single sentence")
    return sentence.encode("ascii")


def resolve_output_dir() -> str:
    return os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"


def write_entry(path: str, data: bytes) -> None:
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "wb") as f:
        f.write(data)
    try:
        os.chmod(path, 0o644)
    except OSError:
        pass


ENTRY_FILENAME = "entry.txt"


def read_entry(path: str) -> bytes:
    with open(path, "rb") as f:
        return f.read()


def verify_entry(path: str, expected: bytes) -> None:
    data = read_entry(path)
    if len(data) != len(expected):
        raise RuntimeError("verification failed: entry.txt has wrong length")
    if data != expected:
        raise RuntimeError("verification failed: entry.txt does not match SENTENCE")


def main() -> None:
    data = validate_sentence(SENTENCE)
    output_dir = resolve_output_dir()
    path = os.path.join(output_dir, ENTRY_FILENAME)
    write_entry(path, data)
    verify_entry(path, data)


if __name__ == "__main__":
    main()
