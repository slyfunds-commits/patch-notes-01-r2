"""Real-Life Patch Notes: The Comedy Changelog — Round 2 entry.

Writes one patch note to /output/entry.txt.
Keeper: "It Was 12% Full" — v3.3.3 bladder false-report line (101 chars).
"""

import os

ENTRY = "v3.3.3: fixed a bug where the bladder woke the user at 3 a.m. to report it was full. It was 12% full."


def main():
    text = ENTRY
    assert text == text.strip(), "entry must not have leading/trailing whitespace"
    assert 1 <= len(text.encode("utf-8")) <= 160, "entry must be 1-160 bytes"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(text)
    # Read back and verify: the file must hold exactly the entry, byte for byte.
    with open("/output/entry.txt", "rb") as f:
        raw = f.read()
    assert raw == text.encode("utf-8"), "entry.txt does not match ENTRY"
    assert b"\n" not in raw, "entry must be a single line"


if __name__ == "__main__":
    main()
