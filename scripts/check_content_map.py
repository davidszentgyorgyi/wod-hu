#!/usr/bin/env python3
"""Flag drift between CONTENT_MAP.md's status column and reality: a row
marked done (✅/🟡) whose referenced file doesn't exist, or a row marked
unstarted (🔲) whose file actually already exists.

This exists because CONTENT_MAP.md's status is hand-maintained prose, not
derived from the filesystem - unlike docs/index.md's stats block, which
update_stats.py regenerates automatically. Hand-maintained status columns
drift; this script is the periodic reality check.

Usage:
    python scripts/check_content_map.py
"""
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
CONTENT_MAP_FILE = ROOT / "CONTENT_MAP.md"

DONE_MARKERS = ("✅", "🟡")
TODO_MARKER = "🔲"
PATH_RE = re.compile(r"`(docs/[^`]+\.md)`")


def main() -> None:
    mismatches = []
    checked = 0

    for raw_line in CONTENT_MAP_FILE.read_text(encoding="utf-8").splitlines():
        line = raw_line.strip()
        if not line.startswith("|"):
            continue

        path_match = PATH_RE.search(line)
        if not path_match:
            continue  # row doesn't reference a concrete file - nothing to check

        rel_path = path_match.group(1)
        file_exists = (ROOT / rel_path).exists()
        checked += 1

        is_marked_done = any(m in line for m in DONE_MARKERS)
        is_marked_todo = TODO_MARKER in line

        if is_marked_done and not file_exists:
            mismatches.append((rel_path, "✅/🟡-nak jelölve, de a fájl NEM létezik", line))
        elif is_marked_todo and file_exists:
            mismatches.append((rel_path, "🔲-nak jelölve, de a fájl MÁR létezik", line))

    print(f"{checked} sor ellenőrizve, amelyek konkrét fájlra hivatkoznak.\n", file=sys.stderr)

    if not mismatches:
        print("Nincs eltérés a CONTENT_MAP.md állapot-oszlopa és a valós fájlok között.")
        return

    print(f"{len(mismatches)} eltérés — javítsd a CONTENT_MAP.md táblázatot:\n")
    for rel_path, issue, line in mismatches:
        print(f"  {rel_path}: {issue}")
        print(f"    sor: {line}")


if __name__ == "__main__":
    main()
