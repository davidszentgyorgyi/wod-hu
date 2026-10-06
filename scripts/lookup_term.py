#!/usr/bin/env python3
"""Quick lookup: is this English term already in TERMINOLOGY.md, and what's
its status? Use this before translating any new concept, instead of
grepping TERMINOLOGY.md by hand.

Usage:
    python scripts/lookup_term.py Masquerade
    python scripts/lookup_term.py "blood potency"
    python scripts/lookup_term.py --hu Maszkabál     # search by Hungarian side instead

Matching is substring, case-insensitive, on whichever side you're searching.
Prints every matching row's full TERMINOLOGY.md table line, so you see the
confidence level and source note, not just the translation.
"""
import argparse
import sys

from termlib import extract_pairs


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("term", help="term to search for")
    parser.add_argument("--hu", action="store_true", help="search the Hungarian column instead of English")
    args = parser.parse_args()

    needle = args.term.lower()
    pairs = extract_pairs()

    matches = []
    for english, hungarian, context in pairs:
        haystack = hungarian.lower() if args.hu else english.lower()
        if needle in haystack:
            matches.append((english, hungarian, context))

    if not matches:
        side = "magyar" if args.hu else "angol"
        print(f"Nincs találat '{args.term}'-ra a TERMINOLOGY.md {side} oszlopában.")
        print("Ez azt jelenti: kövesd a kutatási protokollt (lásd .claude/skills/wod-forditas/SKILL.md),")
        print("mielőtt bármilyen fordítást használnál erre a fogalomra.")
        sys.exit(1)

    print(f"{len(matches)} találat '{args.term}'-ra:\n")
    seen_context = set()
    for english, hungarian, context in matches:
        if context in seen_context:
            continue
        seen_context.add(context)
        print(f"  {context}")


if __name__ == "__main__":
    main()
