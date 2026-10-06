#!/usr/bin/env python3
"""Fetch a whitewolf.fandom.com article and strip it down to clean, readable
plain text for translation — no citation templates, galleries, infobox noise.

This exists to save context/tokens: the raw wikitext of a typical article is
full of {{b|...}} citation templates, <ref> tags, and gallery blocks that are
irrelevant to translating the actual prose. Cleaning it here, once, means the
translator (human or AI) reads a much shorter, denser file.

Usage:
    python scripts/fetch_source.py "Camarilla (VTM)" > /tmp/camarilla.txt
    python scripts/fetch_source.py "Camarilla (VTM)" --out scratch/camarilla.txt
"""
import argparse
import re
import sys
import urllib.parse
import urllib.request

API_BASE = "https://whitewolf.fandom.com/api.php"


def fetch_wikitext(title: str) -> str:
    params = {
        "action": "parse",
        "page": title,
        "prop": "wikitext",
        "format": "json",
    }
    url = API_BASE + "?" + urllib.parse.urlencode(params)
    req = urllib.request.Request(
        url,
        headers={"User-Agent": "wod-hu-wiki-bot/1.0 (https://github.com/davidszentgyorgyi/wod-hu)"},
    )
    with urllib.request.urlopen(req, timeout=20) as resp:
        import json
        data = json.load(resp)
    if "error" in data:
        raise SystemExit(f"API error: {data['error']}")
    return data["parse"]["wikitext"]["*"]


def clean_wikitext(text: str) -> str:
    # Drop galleries, infoboxes/templates, refs, and reference lists outright.
    text = re.sub(r"<gallery.*?</gallery>", "", text, flags=re.DOTALL)
    text = re.sub(r"<ref[^>]*?/>", "", text)
    text = re.sub(r"<ref[^>]*?>.*?</ref>", "", text, flags=re.DOTALL)
    text = re.sub(r"\{\{Reflist\}\}", "", text)

    # Strip balanced {{...}} templates (infobox, quotes, citations), including nested ones.
    def strip_templates(s: str) -> str:
        out = []
        depth = 0
        start = 0
        i = 0
        while i < len(s):
            if s[i : i + 2] == "{{":
                if depth == 0:
                    out.append(s[start:i])
                depth += 1
                i += 2
                continue
            if s[i : i + 2] == "}}":
                depth -= 1
                i += 2
                if depth == 0:
                    start = i
                continue
            i += 1
        out.append(s[start:])
        return "".join(out)

    text = strip_templates(text)

    # [[Category:...]] and interwiki links ([[de:...]], [[pl:...]]) -> drop whole line.
    text = re.sub(r"^\[\[(Category|[a-z]{2}):.*?\]\]\s*$", "", text, flags=re.MULTILINE)

    # Image/File links — drop entirely, bracket-depth aware (captions can contain
    # their own nested [[year links]], so a plain regex would leave trailing junk).
    def strip_image_links(s: str) -> str:
        out = []
        i = 0
        while i < len(s):
            if s[i : i + 2] == "[[" and (
                s[i:].lower().startswith("[[image:") or s[i:].lower().startswith("[[file:")
            ):
                depth = 0
                j = i
                while j < len(s):
                    if s[j : j + 2] == "[[":
                        depth += 1
                        j += 2
                        continue
                    if s[j : j + 2] == "]]":
                        depth -= 1
                        j += 2
                        if depth == 0:
                            break
                        continue
                    j += 1
                i = j
                continue
            out.append(s[i])
            i += 1
        return "".join(out)

    text = strip_image_links(text)

    # [[Link|Shown text]] -> Shown text ; [[Link]] -> Link
    text = re.sub(r"\[\[[^\]|]+\|([^\]]+)\]\]", r"\1", text)
    text = re.sub(r"\[\[([^\]]+)\]\]", r"\1", text)

    # Collapse '' / ''' emphasis markers to plain text (keep the words)
    text = re.sub(r"'{2,3}", "", text)

    # Collapse excess blank lines
    text = re.sub(r"\n{3,}", "\n\n", text)

    return text.strip()


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("title", help="whitewolf.fandom.com page title, e.g. 'Camarilla (VTM)'")
    parser.add_argument("--out", help="write to this file instead of stdout")
    parser.add_argument("--raw", action="store_true", help="skip cleaning, dump raw wikitext")
    args = parser.parse_args()

    wikitext = fetch_wikitext(args.title)
    result = wikitext if args.raw else clean_wikitext(wikitext)

    if args.out:
        with open(args.out, "w", encoding="utf-8") as f:
            f.write(result)
        print(f"Wrote {len(result)} chars to {args.out}", file=sys.stderr)
    else:
        print(result)


if __name__ == "__main__":
    main()
