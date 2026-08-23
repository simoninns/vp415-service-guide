#!/usr/bin/env python3
"""Phase 6: turn the vendor OCR of the operating instructions into page drafts.

  unsorted-source-material/ocr-markdown-service-manual/**/Philips-VP415-
      Operating-Instructions.pdf/pages/page-NN/markdown.md
      -> docs/operating-instructions/<page>.md

The user manual is one run of prose across 45 numbered pages, not a set of
self-contained sheets like the service manual, so this tool is arranged around
the manual's eight sections rather than around its pages: PAGE_SECTION says
which site page each printed page belongs to, and every site page gets the text
of its pages in order, followed by the photographs of those pages.

For each printed page the tool:

  * reads the OCR markdown for that page (printed page N is the OCR's page
    N + 1 - the OCR counts the front cover)
  * drops the OCR's own `img-NN.jpeg` references and the bare page number the
    OCR leaves at the foot of the page
  * unpicks the LaTeX the OCR wraps units in, as tools/import_ocr.py does
  * demotes every heading, since the OCR emits everything as `#`
  * leaves a `<!-- printed page N -->` marker, so the editing pass can tell
    where one page ended and the next began

and then appends one figure per page, from the halves that derive_assets.py
cuts out of the sideways two-page photographs. Which half is which page is in
planning/operating-instructions-page-map.csv - see tools/build_oi_page_map.py.
Three sheets were photographed twice; the second exposure is not published.

What comes out is a *draft*: the OCR runs the manual's two columns together in
places and its tables need work. The editing pass afterwards is the substance
of the job, and the tool will not overwrite a page that has had one.

Usage
  tools/import_operating_instructions.py              draft every page
  tools/import_operating_instructions.py --pages installation.md technical-data.md
  tools/import_operating_instructions.py --dry-run    report what would be written
  tools/import_operating_instructions.py --force      overwrite hand-edited pages
"""
from __future__ import annotations

import argparse
import csv
import pathlib
import re
import sys

ROOT = pathlib.Path(__file__).resolve().parent.parent
PAGE_MAP = ROOT / 'planning/operating-instructions-page-map.csv'
OCR = (ROOT / 'unsorted-source-material/ocr-markdown-service-manual'
       / 'ocr-playground-download-20260821T150015Z'
       / 'Philips-VP415-Operating-Instructions.pdf' / 'pages')
DOCS = ROOT / 'docs/operating-instructions'
WEB = 'assets/web'

MARKER = ('<!-- drafted by tools/import_operating_instructions.py'
          ' - hand-edited afterwards -->')
STUB_MARKER = 'Not written yet'

# printed page -> site page. Page 0 is the front cover; the manual's own
# section dividers open the page of the section they announce. Pages 17 and 25
# are blank and 46 does not exist.
PAGE_SECTION = {
    0: 'index.md', 1: 'index.md',
    2: 'controls-and-connections.md', 3: 'controls-and-connections.md',
    4: 'introduction.md', 5: 'introduction.md', 6: 'introduction.md',
    7: 'installation.md', 8: 'installation.md',
    9: 'controls-and-connections.md',
    10: 'playing-a-disc.md', 11: 'playing-a-disc.md',
    12: 'special-play-functions.md', 13: 'special-play-functions.md',
    14: 'special-play-functions.md', 15: 'special-play-functions.md',
    16: 'special-play-functions.md',
    18: 'interactive-play.md', 19: 'interactive-play.md',
    20: 'f-code-programming.md', 21: 'f-code-programming.md',
    22: 'f-code-programming.md', 23: 'f-code-programming.md',
    24: 'f-code-programming.md',
    26: 'f-code-commands.md', 27: 'f-code-commands.md',
    28: 'f-code-commands.md', 29: 'f-code-commands.md',
    30: 'f-code-commands.md', 31: 'f-code-commands.md',
    32: 'f-code-commands.md', 33: 'f-code-commands.md',
    34: 'f-code-commands.md', 35: 'f-code-commands.md',
    36: 'scsi-operation.md', 37: 'scsi-operation.md', 38: 'scsi-operation.md',
    39: 'scsi-operation.md', 40: 'scsi-operation.md', 41: 'scsi-operation.md',
    42: 'maintenance.md', 43: 'maintenance.md',
    44: 'technical-data.md', 45: 'technical-data.md',
}

# The OCR's page 1 is the front cover.
PRINTED_OFFSET = 1

# Second exposures of a sheet that was already photographed. They stay in the
# repository as the originals they are, but nothing references them.
DUPLICATE_SCANS = {'operating-instructions-scan-09.jpg',
                   'operating-instructions-scan-12.jpg',
                   'operating-instructions-scan-25.jpg'}


# ------------------------------------------------------------------ sources

def page_images() -> dict[int, tuple[str, str]]:
    """printed page -> (scan file, half), skipping the second exposures."""
    out: dict[int, tuple[str, str]] = {}
    with open(PAGE_MAP, newline='') as fh:
        for row in csv.DictReader(fh):
            if not row['printed_page'] or row['scan'] in DUPLICATE_SCANS:
                continue
            out[int(row['printed_page'])] = (row['scan'], row['half'])
    return out


# ------------------------------------------------------- text normalisation

LATEX = [
    (r'\mathrm', ''), (r'\text', ''), (r'\mathbf', ''),
    (r'\geqslant', '≥'), (r'\leqslant', '≤'), (r'\geq', '≥'), (r'\leq', '≤'),
    (r'\Omega', 'Ω'), (r'\omega', 'ω'), (r'\mu', 'μ'), (r'\Delta', 'Δ'),
    (r'\times', '×'), (r'\cdot', '·'), (r'\pm', '±'), (r'\approx', '≈'),
    (r'\circ', '°'), (r'\degree', '°'), (r'\infty', '∞'), (r'\rightarrow', '→'),
    (r'\%', '%'), (r'\&', '&'), (r'\#', '#'), (r'\_', '_'), (r'\ ', ' '),
]

MATH = re.compile(r'\\\((.+?)\\\)|\\\[(.+?)\\\]|\$(.+?)\$', re.S)
IMG = re.compile(r'^!\[[^\]]*\]\([^)]*\)\s*$', re.M)
HEADING = re.compile(r'^(#{1,6})\s+', re.M)


def unmath(text: str) -> str:
    def one(m: re.Match) -> str:
        body = next(g for g in m.groups() if g is not None)
        for src, dst in LATEX:
            body = body.replace(src, dst)
        body = body.replace('{', '').replace('}', '')
        return re.sub(r'\s+', ' ', body).strip()
    return MATH.sub(one, text)


def tidy_tables(text: str) -> str:
    out = []
    for line in text.split('\n'):
        if line.startswith('|') and line.rstrip().endswith('|'):
            cells = line.strip().split('|')
            line = '|'.join([cells[0]]
                            + [f' {c.strip()} ' if c.strip() else ' '
                               for c in cells[1:-1]]
                            + [cells[-1]])
            line = line.rstrip()
        out.append(line)
    return '\n'.join(out)


def strip_folio(text: str, printed: int) -> str:
    """Drop the bare page number the OCR leaves at the foot of the page."""
    lines = text.rstrip().split('\n')
    while lines and lines[-1].strip() in ('', str(printed)):
        lines.pop()
    return '\n'.join(lines)


def normalise(text: str, printed: int, base_level: int = 2) -> str:
    text = IMG.sub('', text)
    text = strip_folio(text, printed)
    text = unmath(text)
    text = tidy_tables(text)
    text = HEADING.sub(lambda m: '#' * min(6, len(m.group(1)) + base_level - 1) + ' ',
                       text)
    return re.sub(r'\n{3,}', '\n\n', text).strip()


def headings(text: str) -> list[str]:
    return [m.group(1).strip() for m in re.finditer(r'^#+\s+(.+)$', text, re.M)]


# --------------------------------------------------------------- assembling

def figure(printed: int, scan: str, half: str, first_heading: str) -> str:
    stem = pathlib.PurePosixPath(scan).stem
    what = f' — {first_heading}' if first_heading else ''
    alt = f'Operating instructions page {printed}{what}'
    return (f'<figure class="sheet" markdown>\n'
            f'[![{alt}]({WEB}/{stem}-{half}-preview.webp)]'
            f'({WEB}/{stem}-{half}-zoom.webp)\n'
            f'<figcaption>\n'
            f'  Page {printed}.\n'
            f'  <span class="src">operating instructions page {printed}</span>\n'
            f'</figcaption>\n'
            f'</figure>')


def front_matter(existing: str) -> tuple[str, str]:
    if not existing.startswith('---\n'):
        return '', existing
    end = existing.find('\n---\n', 4)
    if end < 0:
        return '', existing
    return existing[:end + 5], existing[end + 5:]


def h1_of(body: str) -> str:
    m = re.search(r'^# (.+)$', body, re.M)
    return m.group(1) if m else ''


def lead_of(body: str) -> str:
    m = re.search(r'^# .+\n\n(.+?)\n', body, re.M)
    if not m or m.group(1).startswith(('!!!', '<', '|', '-')):
        return ''
    return m.group(1)


def draft(page: str, printed_pages: list[int],
          images: dict[int, tuple[str, str]]) -> str:
    path = DOCS / page
    existing = path.read_text() if path.exists() else ''
    fm, body = front_matter(existing)

    out = [fm.rstrip('\n'), '', MARKER, '', f'# {h1_of(body) or page}', '']
    lead = lead_of(body)
    if lead:
        out += [lead, '']

    figures = []
    for printed in printed_pages:
        src = OCR / f'page-{printed + PRINTED_OFFSET}' / 'markdown.md'
        text = ''
        if src.exists():
            text = normalise(src.read_text(errors='replace'), printed)
        else:
            print(f'  ! page {printed}: missing {src}', file=sys.stderr)
        out += [f'<!-- printed page {printed} -->', '']
        if text:
            out += [text, '']
        if printed in images:
            scan, half = images[printed]
            heads = headings(text)
            figures.append(figure(printed, scan, half, heads[0] if heads else ''))

    if figures:
        out += ['## The printed pages', '']
        out += ['\n\n'.join(figures), '']

    return '\n'.join(out).rstrip('\n') + '\n'


def writable(path: pathlib.Path, force: bool) -> bool:
    if force or not path.exists():
        return True
    text = path.read_text()
    return MARKER in text or STUB_MARKER in text


def main() -> None:
    ap = argparse.ArgumentParser(description=__doc__,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument('--pages', nargs='*', default=None, metavar='PAGE',
                    help='restrict to these site pages')
    ap.add_argument('--dry-run', action='store_true')
    ap.add_argument('--force', action='store_true',
                    help='overwrite pages that have had their editing pass')
    args = ap.parse_args()

    if args.force and not args.pages:
        sys.exit('--force needs --pages: it would otherwise re-draft the lot '
                 'and throw away every editing pass')

    images = page_images()
    pages: dict[str, list[int]] = {}
    for printed, page in sorted(PAGE_SECTION.items()):
        pages.setdefault(page, []).append(printed)
    if args.pages:
        pages = {p: v for p, v in pages.items() if p in set(args.pages)}

    written = skipped = 0
    for page in sorted(pages):
        path = DOCS / page
        if not writable(path, args.force):
            print(f'  = {page} (hand-edited, left alone)')
            skipped += 1
            continue
        text = draft(page, pages[page], images)
        n = len(pages[page])
        print(f'  {"?" if args.dry_run else "+"} {page} ({n} printed page{"s" * (n != 1)})')
        if not args.dry_run:
            path.write_text(text)
        written += 1

    verb = 'would write' if args.dry_run else 'wrote'
    print(f'{verb} {written} pages'
          + (f', {skipped} already edited' if skipped else ''))


if __name__ == '__main__':
    main()
