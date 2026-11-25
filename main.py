"""One-Line Office Joke Laugh-Off — make.fun bounty entry.

Writes one original one-line joke about office life to entry.txt inside
MAKEFUN_OUTPUT_DIR (fallback /output). Python stdlib only: no network,
no clock, no local imports. Deterministic and byte-identical on every run.
"""

import os

ENTRY = (
    "IT 'fixed' my laptop by rebooting it \u2014 closing my 47 tabs, "
    "my unsaved draft, and apparently my will to meet Friday's deadline."
)


def validate(line):
    """Gate-check the entry line before anything is written."""
    if not isinstance(line, str) or not line:
        raise ValueError("entry must be a non-empty string")
    if not 1 <= len(line) <= 200:
        raise ValueError("entry must be 1-200 characters")
    if "\n" in line or "\r" in line:
        raise ValueError("entry must be a single line")
    if line.strip() != line:
        raise ValueError("entry must not have leading/trailing whitespace")
    if any(ord(ch) < 0x20 for ch in line):
        raise ValueError("entry must not contain control characters")


def write_entry(line, out_dir):
    """Write the line with no trailing newline, then verify the bytes."""
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(line)
    with open(path, "rb") as f:
        written = f.read()
    if written != line.encode("utf-8"):
        raise ValueError("entry.txt does not match the entry line")
    return path


def main():
    validate(ENTRY)
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    write_entry(ENTRY, out_dir)


if __name__ == "__main__":
    main()
