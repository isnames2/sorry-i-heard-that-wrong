#!/usr/bin/env python3
"""Write the smart speaker's apology to the make.fun output file.

Entry for "Sorry, I Heard That Wrong" (u-kiencx-sorry-i-heard-that-wrong-1858c729):
one line, the apology a smart speaker gives after mishearing its owner.
Pure Python standard library only; output is byte-identical on every run.
"""
import os
from pathlib import Path

ENTRY = "Sorry — I heard 'wake me at seven' as 'wake the neighbours.' They are up. You are not."
# 86 characters, within the 140-character gate.


def main() -> None:
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    (out_dir / "entry.txt").write_text(ENTRY, encoding="utf-8")


if __name__ == "__main__":
    main()
