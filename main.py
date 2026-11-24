"""Publish the finished news page image as this entry's output.

The page itself — a one-image summary of Monday 23 November 2026's
world news — is finalised ahead of time and stored in this repository
as ``art.png``.  This program simply copies that file into the output
directory under the name the grader expects, ``entry.png``.

Only the Python standard library is used, there is no network access,
and the copy is a plain byte-for-byte transfer, so running the
program any number of times always yields the identical output file.
"""

import os
import shutil
import sys
from pathlib import Path

SOURCE_NAME = "art.png"
OUTPUT_NAME = "entry.png"
FALLBACK_OUTPUT_DIR = "/output"


def output_directory() -> Path:
    """Return the directory the grader collects output from."""
    configured = os.environ.get("MAKEFUN_OUTPUT_DIR")
    if configured:
        return Path(configured)
    return Path(FALLBACK_OUTPUT_DIR)


def main() -> None:
    source = Path(__file__).resolve().parent / SOURCE_NAME
    if not source.is_file():
        print(f"error: source image not found: {source}", file=sys.stderr)
        sys.exit(1)
    destination_dir = output_directory()
    destination_dir.mkdir(parents=True, exist_ok=True)
    destination = destination_dir / OUTPUT_NAME
    shutil.copyfile(source, destination)
    print(f"wrote {destination} ({destination.stat().st_size} bytes)")


if __name__ == "__main__":
    main()
