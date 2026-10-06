#!/usr/bin/env python3
"""Fetch a URL's raw HTML/text via plain HTTP — no AI summarization involved.

Why this exists: during terminology research this session, a WebFetch-style
AI summary of a login-walled forum page confidently described detailed
content (subforum breakdowns) that didn't exist — the page was just a login
screen, and the summarizer filled in plausible-sounding detail instead of
admitting it saw nothing. Raw HTTP has no such failure mode: what you get is
exactly what the server sent, byte for byte.

Rule of thumb: before trusting any AI-summarized fetch of a page that might
be login-gated, paywalled, or otherwise suspect, re-fetch it with this script
and grep the raw output yourself for the specific claim you want to verify.

Usage:
    python scripts/safe_fetch.py "https://example.com/page" --out scratch/page.html
    python scripts/safe_fetch.py "https://example.com/page" --grep "keresett-szlug"
"""
import argparse
import re
import sys
import urllib.request

DEFAULT_HEADERS = {
    "User-Agent": (
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
        "(KHTML, like Gecko) Chrome/120.0 Safari/537.36"
    )
}


def fetch(url: str) -> str:
    req = urllib.request.Request(url, headers=DEFAULT_HEADERS)
    with urllib.request.urlopen(req, timeout=20) as resp:
        charset = resp.headers.get_content_charset() or "utf-8"
        return resp.read().decode(charset, errors="replace")


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("url")
    parser.add_argument("--out", help="save raw content to this file instead of printing it")
    parser.add_argument("--grep", help="only print lines (with context) matching this substring/regex")
    parser.add_argument("--context", type=int, default=1, help="lines of context around --grep matches (default 1)")
    args = parser.parse_args()

    html = fetch(args.url)

    if args.grep:
        pattern = re.compile(args.grep, re.IGNORECASE)
        lines = html.splitlines()
        hits = [i for i, line in enumerate(lines) if pattern.search(line)]
        if not hits:
            print(f"Nincs találat '{args.grep}'-ra a nyers HTML-ben. Ez FONTOS jel —", file=sys.stderr)
            print("ha egy AI-összegzés részletes tartalmat ígért ehhez a szóhoz,", file=sys.stderr)
            print("és itt nincs nyoma, az összegzés valószínűleg hallucináció.", file=sys.stderr)
            sys.exit(1)
        for i in hits:
            lo, hi = max(0, i - args.context), min(len(lines), i + args.context + 1)
            print("\n".join(lines[lo:hi]))
            print("---")
        return

    if args.out:
        with open(args.out, "w", encoding="utf-8") as f:
            f.write(html)
        print(f"Elmentve: {args.out} ({len(html)} karakter nyers HTML)", file=sys.stderr)
    else:
        print(html)


if __name__ == "__main__":
    main()
