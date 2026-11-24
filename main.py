#!/usr/bin/env python3
"""Write one sentence explaining the modern internet to a traveler from 1800.

The sentence uses only things a person of 1800 would already know -- a road,
a letter, sealing wax, and books -- and adds the one thing that would amaze
them most: every reader can also write. The books do not just answer; they
keep whatever page the reader writes, so the library grows with its readers.
"""

import os

SENTENCE_PARTS = (
    "It is a road joining every house on earth,",
    "where a letter reaches any door before its wax cools,",
    "and the books of a thousand libraries answer when you call their names,",
    "and keep any page you write.",
)

SENTENCE = " ".join(SENTENCE_PARTS)

ENTRY_FILENAME = "entry.txt"


def check_sentence(sentence: str) -> bytes:
    """Return the sentence as ASCII bytes, or raise if it breaks the rules."""
    if not 1 <= len(sentence) <= 200:
        raise ValueError("sentence must be 1 to 200 characters")
    if sentence != sentence.strip():
        raise ValueError("sentence must not start or end with whitespace")
    if "\n" in sentence or "\r" in sentence:
        raise ValueError("sentence must be a single line")
    if not sentence.endswith("."):
        raise ValueError("sentence must end with a period")
    if sentence.count(".") != 1:
        raise ValueError("sentence must contain exactly one period")
    return sentence.encode("ascii")


def output_path() -> str:
    base = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    return os.path.join(base, ENTRY_FILENAME)


def write_and_verify(path: str, data: bytes) -> None:
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "wb") as handle:
        handle.write(data)
    try:
        os.chmod(path, 0o644)
    except OSError:
        pass
    with open(path, "rb") as handle:
        saved = handle.read()
    if saved != data:
        raise RuntimeError("entry.txt does not match the sentence")


def main() -> None:
    data = check_sentence(SENTENCE)
    write_and_verify(output_path(), data)


if __name__ == "__main__":
    main()
