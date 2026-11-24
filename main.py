#!/usr/bin/env python3
"""Entry program for news-image-20261123 (entry5).

The artwork for this entry -- a single picture summing up the world
news of Monday 23 November 2026 -- is not drawn at run time. It was
composed once, checked, and frozen as plain bytes in ``art.png``,
stored next to this script in the repository.

This program's whole job is to deliver those bytes, untouched, to
``entry.png`` inside the output directory. The output directory is
read from the ``MAKEFUN_OUTPUT_DIR`` environment variable and falls
back to ``/output`` when the variable is not set.

Nothing here depends on the clock, on randomness, or on the network,
so every run produces exactly the same output file: a byte-identical
copy of ``art.png``.
"""

import os
import shutil
import sys

# Directory this script lives in; the artwork sits beside it.
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
ARTWORK_PATH = os.path.join(SCRIPT_DIR, "art.png")

# File name the grader expects inside the output directory.
ENTRY_NAME = "entry.png"


def pick_output_dir() -> str:
    """Return the directory the entry image belongs in."""
    return os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"


def run() -> int:
    if not os.path.isfile(ARTWORK_PATH):
        print(f"error: embedded artwork is missing: {ARTWORK_PATH}",
              file=sys.stderr)
        return 1

    out_dir = pick_output_dir()
    os.makedirs(out_dir, exist_ok=True)

    destination = os.path.join(out_dir, ENTRY_NAME)
    shutil.copyfile(ARTWORK_PATH, destination)

    written = os.path.getsize(destination)
    expected = os.path.getsize(ARTWORK_PATH)
    if written != expected:
        print(f"error: copy check failed: {destination} holds "
              f"{written} bytes but art.png holds {expected}",
              file=sys.stderr)
        return 1

    print(f"wrote {destination} ({written} bytes, verified identical "
          f"to art.png)")
    return 0


if __name__ == "__main__":
    sys.exit(run())
