"""Shared parsing helpers for TERMINOLOGY.md, used by check_terminology.py and
lookup_term.py. Not a script itself - nothing to run here directly.
"""
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
TERMINOLOGY_FILE = ROOT / "TERMINOLOGY.md"
DOCS_DIR = ROOT / "docs"

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
    """Returns a list of (english, hungarian, context_line) tuples found in
    TERMINOLOGY.md tables. context_line is the raw markdown row, useful for
    lookup_term.py to show the full note/source column, not just the pair.
    """
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
                    pairs.append((english_raw, h, raw_line.strip()))
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
