#!/usr/bin/env python3
"""Run every check that should pass before committing docs/ changes, in one
command, so no individual step gets forgotten.

Runs, in order, stopping at the first failure:
1. check_terminology.py  - terminology drift (heuristic, review findings)
2. check_content_map.py  - CONTENT_MAP.md status vs. actual files
3. update_stats.py       - regenerates the homepage stats block
4. mkdocs build --strict - catches build errors and nav gaps

Usage:
    python scripts/precommit.py
"""
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent

STEPS = [
    ("Terminológia-konzisztencia", [sys.executable, "scripts/check_terminology.py"]),
    ("CONTENT_MAP.md állapot-ellenőrzés (auto-fix)", [sys.executable, "scripts/check_content_map.py", "--fix"]),
    ("Statisztika frissítése", [sys.executable, "scripts/update_stats.py"]),
    ("MkDocs build (strict)", ["mkdocs", "build", "--strict"]),
]


def main() -> None:
    for name, cmd in STEPS:
        print(f"\n=== {name} ===")
        result = subprocess.run(cmd, cwd=ROOT)
        if result.returncode != 0:
            print(f"\n[HIBA] Megállt itt: {name} (exit code {result.returncode})")
            print("Javítsd a jelzett problémát, mielőtt újra futtatod vagy commitolsz.")
            sys.exit(result.returncode)

    print("\n[OK] Minden ellenőrzés rendben — commitolható.")
    print("Ne feledd: a check_terminology.py és check_content_map.py heurisztikák —")
    print("ha 0 találatot adtak, az jó jel, de emberi átolvasás helyettesítőjének")
    print("csak részben számítanak.")


if __name__ == "__main__":
    main()
