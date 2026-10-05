#!/usr/bin/env python3
"""Generate translation-status stats and inject them into docs/index.md.

Counts complete articles vs. stubs (front matter `status: stub`), and finds
internal Markdown links that point at a .md file that doesn't exist yet.

Run manually: python scripts/update_stats.py
Also runs automatically before every Netlify build (see netlify.toml), so the
live site always shows a fresh count without anyone updating it by hand.
"""
import re
import sys
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parent.parent
DOCS_DIR = ROOT / "docs"
INDEX_FILE = DOCS_DIR / "index.md"
START_MARKER = "<!-- STATS:START -->"
END_MARKER = "<!-- STATS:END -->"

FRONTMATTER_RE = re.compile(r"^---\n(.*?)\n---\n", re.DOTALL)
LINK_RE = re.compile(r"\[[^\]]*\]\(([^)]+)\)")


def parse_frontmatter(text: str) -> dict:
    match = FRONTMATTER_RE.match(text)
    if not match:
        return {}
    try:
        return yaml.safe_load(match.group(1)) or {}
    except yaml.YAMLError:
        return {}


def is_internal_doc_link(target: str) -> bool:
    if target.startswith(("http://", "https://", "mailto:", "#")):
        return False
    stripped = target.split("#", 1)[0]
    if not stripped:
        return False
    return stripped.endswith(".md") or stripped.endswith("/")


def resolve_link(from_file: Path, target: str) -> Path:
    stripped = target.split("#", 1)[0]
    if stripped.endswith("/"):
        stripped += "index.md"
    return (from_file.parent / stripped).resolve()


def main() -> None:
    files = list(DOCS_DIR.rglob("*.md"))
    existing = {f.resolve() for f in files}

    total = 0
    stubs = 0
    broken_links = []

    for f in files:
        text = f.read_text(encoding="utf-8")
        frontmatter = parse_frontmatter(text)
        total += 1
        if frontmatter.get("status") == "stub":
            stubs += 1

        for match in LINK_RE.finditer(text):
            target = match.group(1).strip()
            if not is_internal_doc_link(target):
                continue
            resolved = resolve_link(f, target)
            if resolved not in existing:
                broken_links.append((f.relative_to(DOCS_DIR), target))

    complete = total - stubs

    block_lines = [
        START_MARKER,
        "",
        '!!! abstract "Fordítási állapot"',
        f"    - **Kész cikkek:** {complete}",
        f"    - **Stúbok (bővítésre várnak):** {stubs}",
        f"    - **Összes cikk:** {total}",
        f"    - **Hiányzó célra mutató linkek:** {len(broken_links)}",
        "",
        END_MARKER,
    ]
    block = "\n".join(block_lines)

    index_text = INDEX_FILE.read_text(encoding="utf-8")
    if START_MARKER not in index_text or END_MARKER not in index_text:
        print("ERROR: STATS markers not found in docs/index.md", file=sys.stderr)
        sys.exit(1)

    pattern = re.compile(re.escape(START_MARKER) + r".*?" + re.escape(END_MARKER), re.DOTALL)
    new_text = pattern.sub(block, index_text)
    INDEX_FILE.write_text(new_text, encoding="utf-8")

    print(f"Stats updated: {complete} kész / {stubs} stúb / {total} összes / {len(broken_links)} hiányzó link")
    for src, target in broken_links:
        print(f"  HIÁNYZÓ LINK: {src} -> {target}")


if __name__ == "__main__":
    main()
