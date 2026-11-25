#!/usr/bin/env python3
"""One Star, Written in Sap - make.fun entry.

Writes a single one-line 1-star review, in the voice of a houseplant
reviewing its human owner, to /output/entry.txt (pure stdlib).

The chosen line was picked from ten candidates judged against the
house judge's brief: the plant's own grievance at the centre, a real
laugh through a surprising turn, a plant's view of its care, a genuine
one-star review, and fresh specific detail - no stock phrases about
drama queens, dramatic wilting, being ignored, no-drainage mugs,
coffee watering, or "photosynthesizing out of spite".

Winner: the "thrive on neglect" reversal. "Thrive on neglect" is a
real phrase plant shops print on tags; the plant corrects it - it
thrives on water and merely survives on neglect - and the gap between
the two is the reason for the single star.
"""

import os
from pathlib import Path

ENTRY = (
    "One star. She tells guests I 'thrive on neglect'. "
    "I thrive on water. I survive on neglect. "
    "There is a difference, and it is killing me."
)

MAX_CHARS = 279


def main() -> None:
    text = ENTRY.strip()
    if not text:
        raise SystemExit("entry is empty")
    if len(text) > MAX_CHARS:
        raise SystemExit(f"entry is {len(text)} chars, over the 279 limit")
    if "\n" in text:
        raise SystemExit("entry must be a single line")

    out_dir = Path(os.environ.get("OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    out_path = out_dir / "entry.txt"
    out_path.write_text(text, encoding="utf-8")
    print(f"wrote {len(text)} chars to {out_path}")


if __name__ == "__main__":
    main()
