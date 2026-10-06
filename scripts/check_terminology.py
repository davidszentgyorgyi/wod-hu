#!/usr/bin/env python3
"""Flag likely terminology drift: an English term from TERMINOLOGY.md appears
in an article, but its confirmed Hungarian equivalent never shows up anywhere
in that same file.

This is a heuristic, not a hard rule — false positives happen (e.g. a term
used only inside a game-title proper noun, or inside a source-link URL).
Treat the output as a worklist for human review, not an auto-fix.

Usage:
    python scripts/check_terminology.py
"""
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
TERMINOLOGY_FILE = ROOT / "TERMINOLOGY.md"
DOCS_DIR = ROOT / "docs"

# English terms that are expected to appear untranslated in running prose —
# brand/title names (kept as-is, like "Star Wars"), proper nouns (clan/tribe
# names), or deliberately dual-form terms. Checking these produces mostly
# noise, so they're excluded rather than chased file-by-file.
IGNORE_ENGLISH_TERMS = {
    "world of darkness",
    "vampire: the masquerade",
    "masquerade",  # only flag the standalone *rule* (checked via the Hungarian glossary entry, not here)
    "anarch",  # dual-form by design: "Anarch / Elkötelezetlenek" - either is fine
    "malkavian",  # clan name stays untranslated; only the member demonym is "Malkavita"
    "oblivion",  # "Wraith: The Oblivion" game title
    "shadow",  # too generic a word; collides with proper nouns like "Shadow Lords"
    "tradition",  # ambiguous across game lines (VTM Hagyomány vs Mage Tradíció/Mágusrend)
}

# Cell text that means "no real Hungarian term to check against".
SKIP_MARKERS = (
    "fordítatlan",
    "nincs rögzítve",
    "nyitott",
    "nincs javaslat",
)


def clean_cell(cell: str) -> str:
    cell = cell.strip()
    cell = re.sub(r"\[([^\]]+)\]\([^)]+\)", r"\1", cell)  # [text](link) -> text
    cell = re.sub(r"\*\*|\*|`", "", cell)  # bold/italic/code markers
    cell = re.sub(r"\(.*?\)", "", cell)  # drop parenthetical notes
    return cell.strip()


def split_row(line: str) -> list:
    line = line.strip()
    if line.startswith("|"):
        line = line[1:]
    if line.endswith("|"):
        line = line[:-1]
    return [c.strip() for c in line.split("|")]


def is_separator_row(cells: list) -> bool:
    return all(re.fullmatch(r":?-+:?", c.strip()) for c in cells if c.strip())


def extract_pairs() -> list:
    """Returns a list of (english, hungarian) tuples found in TERMINOLOGY.md tables."""
    pairs = []
    header_pair_indices = []
    in_meta_table = False
    for raw_line in TERMINOLOGY_FILE.read_text(encoding="utf-8").splitlines():
        line = raw_line.strip()
        if line.startswith("### Szervezeti címek"):
            in_meta_table = True  # natural-language rules table, not strict term pairs
        elif line.startswith("#"):
            in_meta_table = False
        if not line.startswith("|") or in_meta_table:
            header_pair_indices = []
            continue
        cells = split_row(line)
        if is_separator_row(cells):
            continue
        lower = [c.lower() for c in cells]
        if "angol" in lower:
            header_pair_indices = [i for i, c in enumerate(lower) if c == "angol"]
            continue
        if not header_pair_indices:
            continue
        for angol_idx in header_pair_indices:
            magyar_idx = angol_idx + 1
            if magyar_idx >= len(cells):
                continue
            english_raw = clean_cell(cells[angol_idx])
            hungarian_raw = clean_cell(cells[magyar_idx])
            if not english_raw or not hungarian_raw:
                continue
            if any(marker in hungarian_raw.lower() for marker in SKIP_MARKERS):
                continue
            if any(marker in cells[magyar_idx].lower() for marker in SKIP_MARKERS):
                continue
            # Multiple alternatives separated by " / " - check each as its own pair
            for h in hungarian_raw.split(" / "):
                h = h.strip()
                if h and h.lower() != english_raw.lower():
                    pairs.append((english_raw, h))
    # Dedup while preserving order
    seen = set()
    unique_pairs = []
    for p in pairs:
        if p not in seen:
            seen.add(p)
            unique_pairs.append(p)
    return unique_pairs


def word_present(text: str, term: str) -> bool:
    pattern = r"(?<!\w)" + re.escape(term) + r"(?!\w)"
    return re.search(pattern, text, re.IGNORECASE) is not None


def main() -> None:
    pairs = extract_pairs()
    print(f"Loaded {len(pairs)} English->Hungarian term pairs from TERMINOLOGY.md\n", file=sys.stderr)

    # Attribution footers link to the English source article by its English
    # title/URL slug - that's correct, not drift. Strip them before scanning.
    attribution_re = re.compile(
        r'!!! info "Forrás és licenc".*?(?=\n\S|\Z)', re.DOTALL
    )

    findings = []
    for path in sorted(DOCS_DIR.rglob("*.md")):
        text = attribution_re.sub("", path.read_text(encoding="utf-8"))
        rel = path.relative_to(ROOT)
        for english, hungarian in pairs:
            if english.lower() in IGNORE_ENGLISH_TERMS:
                continue
            if word_present(text, english) and not word_present(text, hungarian):
                findings.append((rel, english, hungarian))

    if not findings:
        print("No terminology drift found.")
        return

    print(f"{len(findings)} potential terminology drift finding(s) — review, don't auto-fix:\n")
    for rel, english, hungarian in findings:
        print(f"  {rel}: found '{english}' but not '{hungarian}'")


if __name__ == "__main__":
    main()
