#!/usr/bin/env python3
"""Flag drift between CONTENT_MAP.md's status column and reality: a row
marked done (✅/🟡) whose referenced file doesn't exist, or a row marked
unstarted (🔲) whose file actually already exists.

This exists because CONTENT_MAP.md's status is hand-maintained prose, not
derived from the filesystem - unlike docs/index.md's stats block, which
update_stats.py regenerates automatically. Hand-maintained status columns
drift; this script is the periodic reality check.

Usage:
    python scripts/check_content_map.py          # report only
    python scripts/check_content_map.py --fix     # also auto-fix 🔲 -> ✅ where the file now exists

--fix only ever flips 🔲 to ✅ (a file existing is unambiguous good news). It
never flips ✅/🟡 to 🔲 when a file is missing — that could mean the file was
accidentally deleted/renamed, which needs a human to look at, not a script
silently "fixing" it by downgrading the status.
"""
import argparse
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
CONTENT_MAP_FILE = ROOT / "CONTENT_MAP.md"

DONE_MARKERS = ("✅", "🟡")
TODO_MARKER = "🔲"
PATH_RE = re.compile(r"`(docs/[^`]+\.md)`")


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("--fix", action="store_true", help="auto-flip 🔲 -> ✅ where the file already exists")
    args = parser.parse_args()

    original_lines = CONTENT_MAP_FILE.read_text(encoding="utf-8").splitlines()
    new_lines = list(original_lines)
    mismatches = []
    fixed = []
    checked = 0

    for i, raw_line in enumerate(original_lines):
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
            if args.fix:
                new_lines[i] = raw_line.replace(TODO_MARKER, "✅", 1)
                fixed.append(rel_path)
            else:
                mismatches.append((rel_path, "🔲-nak jelölve, de a fájl MÁR létezik", line))

    print(f"{checked} sor ellenőrizve, amelyek konkrét fájlra hivatkoznak.\n", file=sys.stderr)

    if fixed:
        CONTENT_MAP_FILE.write_text("\n".join(new_lines) + "\n", encoding="utf-8")
        print(f"{len(fixed)} sor automatikusan javítva (🔲 -> ✅) a CONTENT_MAP.md-ben:")
        for rel_path in fixed:
            print(f"  {rel_path}")
        print("\nFontos: a CONTENT_MAP.md módosult — add hozzá a commithoz (git add CONTENT_MAP.md)")
        print("és futtasd újra a parancsot/commitot.")

    if not mismatches and not fixed:
        print("Nincs eltérés a CONTENT_MAP.md állapot-oszlopa és a valós fájlok között.")
        return

    if mismatches:
        print(f"\n{len(mismatches)} eltérés, amit NEM javítunk automatikusan — nézd át kézzel:\n")
        for rel_path, issue, line in mismatches:
            print(f"  {rel_path}: {issue}")
            print(f"    sor: {line}")

    if mismatches or fixed:
        sys.exit(1)


if __name__ == "__main__":
    main()
