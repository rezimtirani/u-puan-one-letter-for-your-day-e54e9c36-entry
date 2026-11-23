"""One Letter for Your Day.

The whole entry is a single letter: W.
Behind it sits the word for the day: "Why am I still awake?"
It is 5 in the morning, the work never stopped, and the question
is the most honest one the day has produced.
"""

import os

LETTER = "W"
OUTPUT_PATH = "/output/entry.txt"


def check_letter(letter):
    if len(letter) != 1:
        raise ValueError("entry must be exactly one character")
    if not ("A" <= letter <= "Z"):
        raise ValueError("entry must be a capital letter A-Z")
    return letter


def write_entry(letter, path):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="ascii") as handle:
        handle.write(letter)


def verify_entry(path, letter):
    with open(path, "rb") as handle:
        raw = handle.read()
    if len(raw) != 1:
        raise ValueError(f"entry file must hold exactly one byte, got {len(raw)}")
    if raw.decode("ascii") != letter:
        raise ValueError("entry file does not hold the chosen letter")
    return raw.decode("ascii")


def main():
    letter = check_letter(LETTER)
    write_entry(letter, OUTPUT_PATH)
    seen = verify_entry(OUTPUT_PATH, letter)
    print(f"wrote {OUTPUT_PATH}: {seen!r}")


if __name__ == "__main__":
    main()
