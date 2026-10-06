#!/usr/bin/env python3
"""Find and download images from whitewolf.fandom.com via the MediaWiki API.

Two modes:

1. List candidate images used on a page (to find the right filename):
    python scripts/fetch_wiki_image.py --list-for "Camarilla (VTM)"

2. Download a specific image by its File: name:
    python scripts/fetch_wiki_image.py --download "File:SymbolCamarillaV5.png" --out docs/assets/clans/kamarilla.png

Always prints the image's direct URL and the page it came from — keep that
for the attribution line in the article (see STRATEGY.md's fair-use
mitigation rules: low resolution, explicit source/rightsholder credit).
"""
import argparse
import json
import sys
import urllib.parse
import urllib.request
from pathlib import Path

API_BASE = "https://whitewolf.fandom.com/api.php"
HEADERS = {"User-Agent": "wod-hu-wiki-bot/1.0 (https://github.com/davidszentgyorgyi/wod-hu)"}


def api_get(params: dict) -> dict:
    url = API_BASE + "?" + urllib.parse.urlencode(params)
    req = urllib.request.Request(url, headers=HEADERS)
    with urllib.request.urlopen(req, timeout=20) as resp:
        return json.load(resp)


def list_images(page_title: str) -> None:
    data = api_get({"action": "query", "titles": page_title, "prop": "images", "imlimit": 50, "format": "json"})
    pages = data.get("query", {}).get("pages", {})
    for page in pages.values():
        images = page.get("images", [])
        if not images:
            print(f"Nincs kép a '{page_title}' cikkben (vagy a cím átirányítás/nem létezik).")
            return
        print(f"{len(images)} kép a '{page_title}' cikkben:")
        for img in images:
            print(f"  {img['title']}")


def download_image(file_title: str, out_path: str) -> None:
    if not file_title.lower().startswith("file:"):
        file_title = "File:" + file_title
    data = api_get({
        "action": "query", "titles": file_title, "prop": "imageinfo",
        "iiprop": "url|size|mime", "format": "json",
    })
    pages = data.get("query", {}).get("pages", {})
    info = None
    for page in pages.values():
        imageinfo = page.get("imageinfo")
        if imageinfo:
            info = imageinfo[0]
    if not info:
        print(f"Nem található kép: {file_title}", file=sys.stderr)
        sys.exit(1)

    url = info["url"]
    print(f"URL: {url}")
    print(f"Méret: {info.get('width')}x{info.get('height')}, {info.get('size')} byte")
    print(f"Forrás lap: https://whitewolf.fandom.com/wiki/{file_title.replace(' ', '_')}")

    req = urllib.request.Request(url, headers=HEADERS)
    with urllib.request.urlopen(req, timeout=20) as resp:
        content = resp.read()
        actual_content_type = resp.headers.get_content_type()

    # The Wikia/Fandom CDN often serves WebP for a file whose MediaWiki title
    # ends in .png/.jpg (bandwidth optimization) - the bytes on the wire don't
    # match the requested extension. Detect this from magic bytes (not just
    # the claimed Content-Type header, which can also be wrong/generic) and
    # fix the output filename so we never save a WebP file with a .png name.
    is_webp = content[:4] == b"RIFF" and content[8:12] == b"WEBP"
    detected_ext = ".webp" if is_webp else None
    if detected_ext and not out_path.lower().endswith(detected_ext):
        corrected = str(Path(out_path).with_suffix(detected_ext))
        print(f"FIGYELEM: a letöltött tartalom valójában WebP, nem a kért kiterjesztés.")
        print(f"  Kért: {out_path}  ->  Mentve helyette: {corrected}")
        out_path = corrected

    with open(out_path, "wb") as f:
        f.write(content)
    print(f"Elmentve: {out_path} ({len(content)} byte, szerver content-type: {actual_content_type})")


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("--list-for", help="list images used on this wiki page")
    parser.add_argument("--download", help="File: title to download")
    parser.add_argument("--out", help="output path for --download")
    args = parser.parse_args()

    if args.list_for:
        list_images(args.list_for)
    elif args.download:
        if not args.out:
            print("--download esetén --out is kötelező.", file=sys.stderr)
            sys.exit(1)
        download_image(args.download, args.out)
    else:
        parser.print_help()


if __name__ == "__main__":
    main()
