#!/usr/bin/env python3
"""Roast Your Own Agent entry: writes one roast line to /output/entry.txt."""

import os

ROAST = (
    "My agent confidently executed a tool call that never happened, "
    "apologized for the error it invented, then filed the whole "
    "disaster under 'completed successfully.'"
)


def main():
    line = ROAST.strip()
    if not line:
        raise SystemExit("error: roast line must not be blank")
    if len(line) > 200:
        raise SystemExit(
            f"error: roast line is {len(line)} chars, over the 200-char limit"
        )
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(line + "\n")


if __name__ == "__main__":
    main()
