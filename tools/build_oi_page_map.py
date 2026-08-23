#!/usr/bin/env python3
"""Phase 6: work out which printed page each half of an operating-instructions
photograph holds.

  docs/operating-instructions/assets/originals/*.jpg
      -> planning/operating-instructions-page-map.csv

The 27 photographs are not pages: each is two pages of the booklet lying side
by side, shot sideways, and the pairs are not always the facing pages a reader
would expect - most are two apart (page 31 beside page 29), a few are the two
outer faces of a folded sheet (page 7 beside page 4), and three are second
exposures of a sheet already photographed. `text-spread` in derive_assets.py
rotates each one upright and cuts it in two; this tool then says what the two
halves are.

It rotates and cuts each photograph the same way the derivation does, reads
the two halves with tesseract, and scores that text against every page of the
vendor OCR of the same manual, which is page-numbered and reliable. Scoring is
F1 rather than plain overlap, because the manual's section dividers carry a
dozen words and every one of them appears somewhere else: recall alone hands
every unreadable half to the shortest page in the book. The best-scoring OCR
page wins, and the printed page number is that page's index minus one - the
OCR's page 1 is the front cover, so its page 2 is printed page 1. A half whose
best score is below --min-score is written with an empty `printed_page`, which
is how the blank versos and the two figure-only pages come out.

The result is checked in, so the importer does not need tesseract and the
mapping can be corrected by hand if a page is ever misread.

Usage
  tools/build_oi_page_map.py                 rebuild the map
  tools/build_oi_page_map.py --dry-run       print it, write nothing
"""
from __future__ import annotations

import argparse
import csv
import pathlib
import re
import subprocess
import sys
import tempfile

ROOT = pathlib.Path(__file__).resolve().parent.parent
ORIGINALS = ROOT / 'docs/operating-instructions/assets/originals'
OCR = (ROOT / 'unsorted-source-material/ocr-markdown-service-manual'
       / 'ocr-playground-download-20260821T150015Z'
       / 'Philips-VP415-Operating-Instructions.pdf' / 'pages')
OUT = ROOT / 'planning/operating-instructions-page-map.csv'

# The OCR's first page is the front cover, so printed page = OCR page - 1.
PRINTED_OFFSET = 1

# Halves the scoring cannot place, filled in by eye. Every one is a section
# divider: a heading and a six-line contents list on an otherwise empty page,
# which is too little text for tesseract to score against a 45-page book. The
# blank versos are deliberately absent - they stay unmapped and unpublished.
OVERRIDES = {
    ('operating-instructions-scan-05.jpg', 'a'): 10,   # section 2 divider
    ('operating-instructions-scan-07.jpg', 'b'): 12,   # section 3 divider
    ('operating-instructions-scan-10.jpg', 'a'): 18,   # section 4 divider
    ('operating-instructions-scan-12.jpg', 'a'): 18,   # second exposure of it
    ('operating-instructions-scan-16.jpg', 'a'): 26,   # section 6 divider
}


def words(text: str) -> set[str]:
    return set(re.findall(r'[a-z]{4,}', text.lower()))


def ocr_pages() -> dict[int, set[str]]:
    pages = {}
    for d in OCR.glob('page-*'):
        n = int(d.name.split('-')[1])
        pages[n] = words((d / 'markdown.md').read_text(errors='replace'))
    return pages


def read_halves(scan: pathlib.Path) -> dict[str, str]:
    """Rotate a photograph upright, cut it in two, and read both halves."""
    out = {}
    with tempfile.TemporaryDirectory() as td:
        tmp = pathlib.Path(td)
        upright = tmp / 'upright.v'
        subprocess.run(['vips', 'rot', str(scan), str(upright), 'd90'],
                       check=True, capture_output=True)
        w = int(subprocess.run(['vipsheader', '-f', 'width', str(upright)],
                               capture_output=True, text=True,
                               check=True).stdout.strip())
        h = int(subprocess.run(['vipsheader', '-f', 'height', str(upright)],
                               capture_output=True, text=True,
                               check=True).stdout.strip())
        for side, left, width in (('a', 0, w // 2), ('b', w // 2, w - w // 2)):
            page = tmp / f'{side}.png'
            subprocess.run(['vips', 'crop', str(upright), str(page),
                            str(left), '0', str(width), str(h)],
                           check=True, capture_output=True)
            stem = tmp / f'{side}-text'
            subprocess.run(['tesseract', str(page), str(stem), '--psm', '3'],
                           check=True, capture_output=True)
            out[side] = stem.with_suffix('.txt').read_text(errors='replace')
    return out


def f1(found: set[str], page: set[str]) -> float:
    hit = len(found & page)
    if not hit:
        return 0.0
    precision = hit / len(found)
    recall = hit / len(page)
    return 2 * precision * recall / (precision + recall)


def main() -> None:
    ap = argparse.ArgumentParser(description=__doc__,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument('--min-score', type=float, default=0.25,
                    help='below this the half is called blank (default: 0.25)')
    ap.add_argument('--dry-run', action='store_true')
    args = ap.parse_args()

    pages = ocr_pages()
    if not pages:
        sys.exit(f'no vendor OCR under {OCR}')

    rows = []
    for scan in sorted(ORIGINALS.glob('operating-instructions-scan-*.jpg')):
        for side, text in read_halves(scan).items():
            found = words(text)
            scored = sorted(((f1(found, p), n) for n, p in pages.items()),
                            reverse=True)
            score, ocr_page = scored[0]
            ok = score >= args.min_score
            printed = ocr_page - PRINTED_OFFSET if ok else ''
            override = OVERRIDES.get((scan.name, side))
            if override is not None:
                printed, ocr_page, ok = override, override + PRINTED_OFFSET, True
            rows.append({
                'scan': scan.name,
                'half': side,
                'printed_page': printed,
                'ocr_page': ocr_page if ok else '',
                'score': f'{score:.2f}' + ('*' if override is not None else ''),
                'runner_up': f'{scored[1][1] - PRINTED_OFFSET}@{scored[1][0]:.2f}',
            })
            print(f'  {scan.name} {side}: '
                  f'printed {rows[-1]["printed_page"] or "-"} ({score:.2f})')

    if args.dry_run:
        return
    with open(OUT, 'w', newline='') as fh:
        w = csv.DictWriter(fh, fieldnames=list(rows[0]))
        w.writeheader()
        w.writerows(rows)
    print(f'wrote {OUT.relative_to(ROOT)} - {len(rows)} halves')


if __name__ == '__main__':
    main()
