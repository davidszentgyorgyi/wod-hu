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
import sys

from termlib import DOCS_DIR, ROOT, extract_pairs, word_present
import re

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
    "wraith",  # only flagged as drift when used as a bare creature noun; in practice it
               # almost always appears inside the "Wraith: The Oblivion"/"Wraith: A Feledés" title
    "hunter",  # "Hunter: The Reckoning"/"Hunter: A Leszámolás" title
    "demon",  # "Demon: The Fallen"/"Demon: A Bukottak" title
}

# Auto-detect "X: The Y" game-line titles (e.g. "Mummy: The Resurrection") and
# treat the creature word X as a brand term automatically, so a *new* game
# line added later doesn't need a manual entry above like the ones blamed on
# Wraith/Hunter/Demon did. Static IGNORE_ENGLISH_TERMS above stays for
# genuinely ambiguous/generic words (shadow, tradition) that this pattern
# can't catch.
GAME_TITLE_RE = re.compile(r"\b([A-Z][a-zA-Z]+): [Tt]he [A-Z][a-zA-Z]+")


def detect_game_title_brand_words(docs_dir) -> set:
    words = set()
    for path in docs_dir.rglob("*.md"):
        for match in GAME_TITLE_RE.finditer(path.read_text(encoding="utf-8")):
            words.add(match.group(1).lower())
    return words


def main() -> None:
    pairs = [(e, h) for e, h, _ctx in extract_pairs()]
    print(f"Loaded {len(pairs)} English->Hungarian term pairs from TERMINOLOGY.md\n", file=sys.stderr)

    # Attribution footers link to the English source article by its English
    # title/URL slug - that's correct, not drift. Strip them before scanning.
    attribution_re = re.compile(
        r'!!! info "Forrás és licenc".*?(?=\n\S|\Z)', re.DOTALL
    )
    # [Link text](url/slug) -> Link text - internal link targets are file
    # paths/slugs (often English-derived, e.g. hunter-a-leszamolas/index.md)
    # and should never count as "prose used the English term".
    link_target_re = re.compile(r"\[([^\]]*)\]\([^)]*\)")
    # attr_list / markdown-attributes blocks, e.g. ![alt](img){ .clan-logo }
    # or { width="280" } - CSS class names here (like "clan-logo") are not
    # prose and shouldn't count as an English word usage.
    attr_list_re = re.compile(r"\{[^{}]*\}")

    ignore_terms = IGNORE_ENGLISH_TERMS | detect_game_title_brand_words(DOCS_DIR)

    findings = []
    for path in sorted(DOCS_DIR.rglob("*.md")):
        text = attribution_re.sub("", path.read_text(encoding="utf-8"))
        text = link_target_re.sub(r"\1", text)
        text = attr_list_re.sub("", text)
        rel = path.relative_to(ROOT)
        for english, hungarian in pairs:
            if english.lower() in ignore_terms:
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
