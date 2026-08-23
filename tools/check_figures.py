#!/usr/bin/env python3
"""Phase 7: check the figures on every page.

Four rules, all of them things a reader loses silently when they are broken:

  1. Every image has alt text, and it describes the picture rather than
     repeating the file name.
  2. Every <figure> has a <figcaption>. A picture with no caption is an
     ornament.
  3. A figure derived from a manual sheet - its derivative is named
     `...-p<page>-preview.webp` - carries the service manual page number in a
     `<span class="src">`, and if the sheet has a Philips CS code in its name,
     the code in a `<span class="cs">`. That is what lets a reader with the
     paper manual find the same sheet.
  4. The inline image is the `-preview` derivative and the link around it
     points at the `-zoom` one, which is what glightbox opens.

Run by `just check`, so a figure that breaks one of them fails the build rather
than reaching the site.

Usage
  tools/check_figures.py            check docs/
  tools/check_figures.py --list     also print every figure it accepted
"""
from __future__ import annotations

import argparse
import pathlib
import re
import sys

ROOT = pathlib.Path(__file__).resolve().parent.parent
DOCS = ROOT / 'docs'

FIGURE = re.compile(r'<figure[^>]*>(.*?)</figure>', re.S)
IMAGE = re.compile(r'!\[(?P<alt>.*?)\]\((?P<src>[^)]+)\)')
LINKED_IMAGE = re.compile(r'\[!\[(?P<alt>.*?)\]\((?P<src>[^)]+)\)\]\((?P<href>[^)]+)\)')
SHEET_PAGE = re.compile(r'-p(\d{3})(?:-\d{3})*-preview\.webp$')
CS_CODE = re.compile(r'^(cs-\d-\d{3})-')

MIN_ALT = 12


def check(page: pathlib.Path, verbose: bool) -> list[str]:
    text = page.read_text()
    rel = page.relative_to(ROOT)
    problems = []

    for m in IMAGE.finditer(text):
        alt, src = m.group('alt').strip(), m.group('src')
        line = text[:m.start()].count('\n') + 1
        if len(alt) < MIN_ALT:
            problems.append(f'{rel}:{line}: alt text too short for {src}: {alt!r}')
        elif alt.lower().rstrip('.') in pathlib.Path(src).stem.replace('-', ' '):
            problems.append(f'{rel}:{line}: alt text repeats the file name: {alt!r}')
        elif verbose:
            print(f'  ok {rel}:{line} {pathlib.Path(src).name}')

    for m in FIGURE.finditer(text):
        body = m.group(1)
        line = text[:m.start()].count('\n') + 1
        if '<figcaption>' not in body:
            problems.append(f'{rel}:{line}: figure without a <figcaption>')
            continue
        img = LINKED_IMAGE.search(body)
        if not img:
            if IMAGE.search(body):
                problems.append(f'{rel}:{line}: figure image is not linked to its -zoom derivative')
            continue
        src, href = img.group('src'), img.group('href')
        name = pathlib.Path(src).name
        if '-preview.webp' in name and href.replace('-zoom.webp', '-preview.webp') != src:
            problems.append(f'{rel}:{line}: {name} does not link to its own -zoom derivative')
        sheet = SHEET_PAGE.search(name)
        if sheet and 'class="src"' not in body:
            problems.append(f'{rel}:{line}: {name} comes from manual page '
                            f'{sheet.group(1)} but the caption gives no page number')
        if sheet and CS_CODE.match(name) and 'class="cs"' not in body:
            problems.append(f'{rel}:{line}: {name} has a CS code but the caption does not print it')
    return problems


def main() -> None:
    ap = argparse.ArgumentParser(description=__doc__,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument('--list', action='store_true', help='print every figure checked')
    args = ap.parse_args()

    pages = sorted(DOCS.rglob('*.md'))
    problems = [p for page in pages for p in check(page, args.list)]
    images = sum(len(IMAGE.findall(page.read_text())) for page in pages)
    if problems:
        for p in problems:
            print(p, file=sys.stderr)
        sys.exit(f'{len(problems)} figure problem(s) in {len(pages)} pages')
    print(f'{images} images on {len(pages)} pages: alt text, captions and '
          f'sheet numbers all present')


if __name__ == '__main__':
    main()
