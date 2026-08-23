#!/usr/bin/env python3
"""Phase 4: turn the vendor OCR markdown into chapter page drafts.

  unsorted-source-material/ocr-markdown-service-manual/**/markdown.md
      -> docs/<section>/<page>.md

One draft page per site page, assembled from the sheets the sheet map assigns
to it, in manual order. For each sheet the tool:

  * reads the OCR markdown named by the sheet map's `ocr_path` (one read per
    file - the two panels of a bifold share a scan and share an OCR page)
  * strips the trailing Philips `CS` code, which belongs in the caption
  * drops the OCR's own `img-NN.jpeg` references: those are downscaled
    extracts and are never published (see the plan's source-of-truth rule)
  * unpicks the LaTeX the OCR wraps units in - `\\(700\\mathrm{mV}/75\\Omega\\)`
    back to `700 mV / 75 Ω`
  * demotes every heading two levels, since the OCR emits everything as `#`
    and each sheet sits under an `##` of its own
  * tidies the GFM tables, which are good but padded
  * appends the sheet's scan as a figure in the phase 3 pattern, captioned
    with the `CS` code and the manual page number

What comes out is a *draft*. The OCR is good but not perfect and the manual's
two-column pages come out interleaved, so every page gets a human editing pass
afterwards - that pass is the substance of phase 4, not this script.

The tool will not overwrite a page that has been through that pass: it writes
only over a phase 3 stub or over its own output, both of which it recognises,
unless `--force` says otherwise.

Usage
  tools/import_ocr.py                     draft every phase 4 page
  tools/import_ocr.py --pages overview    restrict to pages under a prefix
  tools/import_ocr.py --dry-run           report what would be written
  tools/import_ocr.py --force             overwrite hand-edited pages too
"""
from __future__ import annotations

import argparse
import csv
import os
import pathlib
import re
import sys

ROOT = pathlib.Path(__file__).resolve().parent.parent
SHEET_MAP = ROOT / 'planning/service-manual-sheet-map.csv'
MIGRATION_LOG = ROOT / 'planning/migration-log.csv'
DOCS = ROOT / 'docs'

MARKER = '<!-- drafted by tools/import_ocr.py - hand-edited afterwards -->'
STUB_MARKER = 'Not written yet'

# Where each (chapter, section) of the manual lands on the site. Phase 4 covers
# chapters 1, 2, 3, 5, 6, 7 and 8; chapter 4 is phase 5 and is absent here.
SECTION_PAGE = {
    ('1', 'divider'):              'overview/index.md',
    ('1', 'technical-data'):       'overview/technical-data.md',
    ('1', 'controls-connections'): 'overview/controls-and-connections.md',
    ('1', 'connector-pinning'):    'overview/connector-pinning.md',

    ('2', 'divider'):             'general-service/index.md',
    ('2', 'remarks'):             'general-service/remarks.md',
    ('2', 'warnings'):            'general-service/warnings.md',
    ('2', 'modification-levels'): 'general-service/modification-levels.md',
    ('2', 'adjustments'):         'general-service/adjustments.md',
    ('2', 'demounting'):          'general-service/demounting.md',
    ('2', 'service-hints'):       'general-service/service-hints.md',
    ('2', 'service-tools'):       'general-service/service-tools.md',
    ('2', 'symbols'):             'general-service/symbols.md',

    ('3', 'divider'):        'system/index.md',
    ('3', 'module-layout'):  'system/module-layout.md',
    ('3', 'signal-listing'): 'system/signal-listing.md',
    ('3', 'wiring-diagram'): 'system/wiring-diagrams.md',
    ('3', 'block-diagrams'): 'system/block-diagrams.md',
    # Sheet 027 is bound at the end of chapter 3, but the manual's own contents
    # page files it under chapter 2. Follow the contents page - see below.
    ('3', 'semiconductors'): 'general-service/semiconductor-connections.md',

    ('5', 'divider'):          'parts/index.md',
    ('5', 'exploded-views'):   'parts/exploded-views.md',
    ('5', 'parts-mechanical'): 'parts/mechanical-parts.md',
    ('5', 'parts-electrical'): 'parts/electrical-parts.md',

    ('6', 'divider'):       'repair/index.md',
    ('6', 'repair-method'): 'repair/diagnostic-mode.md',
    ('6', 'fault-finding'): 'repair/fault-finding.md',

    ('7', 'divider'):             'circuit-description/index.md',
    ('7', 'circuit-description'): 'circuit-description/index.md',
    ('7', 'laservision-system'):  'circuit-description/laservision-system.md',
    ('7', 'optical-deck'):        'circuit-description/optical-deck.md',
    ('7', 'vp400-series'):        'circuit-description/vp400-series.md',
    ('7', 'module-description'):  'circuit-description/modules.md',

    ('8', 'divider'):             'service-information/index.md',
    ('8', 'service-information'): 'service-information/index.md',
    ('8', 'modification-levels'): 'service-information/modification-levels.md',
    ('8', 'software-releases'):   'service-information/software-releases.md',
    ('8', 'fault-symptoms'):      'service-information/fault-symptoms.md',
}

# Sheets whose section rule sends them to the wrong page.
SHEET_PAGE = {
    # Chapter 6's contents sheet introduces the whole chapter, not the
    # diagnostic mode; the error code table earns a page of its own so that
    # phase 6's case studies can link straight at an individual code.
    '107': 'repair/index.md',
    '111': 'repair/error-codes.md',
}

# Sheets that carry no transcribable text: chapter dividers, and pages whose
# whole content is one drawing. The scan is the content, so the draft carries
# the figure alone.
FIGURE_ONLY_TYPES = {'divider', 'figure'}


# ------------------------------------------------------------------ sources

def read_csv(path: pathlib.Path) -> list[dict]:
    with open(path, newline='') as fh:
        return list(csv.DictReader(fh))


def sheets_by_page() -> dict[str, list[dict]]:
    """Site page -> the sheets that make it up, in manual order.

    A bifold or trifold sheet has one row per panel; they share a scan and an
    OCR page, so the sheet is collapsed to its first row.
    """
    pages: dict[str, list[dict]] = {}
    seen: set[str] = set()
    for row in read_csv(SHEET_MAP):
        if row['sheet'] in seen:
            continue
        seen.add(row['sheet'])
        page = SHEET_PAGE.get(row['sheet'])
        if page is None:
            page = SECTION_PAGE.get((row['chapter'], row['section']))
        if page is None:
            continue
        pages.setdefault(page, []).append(row)
    return pages


def asset_stems() -> dict[str, pathlib.PurePosixPath]:
    """Sheet -> the docs-relative path of its archival original."""
    return {r['sheet']: pathlib.PurePosixPath(r['dest_path'])
            for r in read_csv(MIGRATION_LOG) if r['sheet']}


# ------------------------------------------------------- text normalisation

# The OCR wraps units and inequalities in LaTeX. Undo it, longest first so
# that \leqslant is not eaten by \le.
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
CS_TAIL = re.compile(r'^\s*CS\s*\d\s*\d{3}\s*$', re.M)


def unmath(text: str) -> str:
    """Replace the OCR's inline LaTeX with the characters it stands for."""
    def one(m: re.Match) -> str:
        body = next(g for g in m.groups() if g is not None)
        for src, dst in LATEX:
            body = body.replace(src, dst)
        # Superscripts survive as 10^{-16}; keep them readable as 10⁻¹⁶ is
        # beyond a regex, so leave the caret form for the editing pass.
        body = body.replace('{', '').replace('}', '')
        body = re.sub(r'\s+', ' ', body).strip()
        return body
    return MATH.sub(one, text)


def tidy_tables(text: str) -> str:
    """The OCR pads every cell with two spaces. Trim to one."""
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


def normalise(text: str, base_level: int = 3) -> str:
    """OCR markdown -> draft body: no images, no LaTeX, headings at base_level."""
    text = IMG.sub('', text)
    text = CS_TAIL.sub('', text)
    text = unmath(text)
    text = tidy_tables(text)
    # Everything the OCR emits is `#`; a sheet's own headings sit under the
    # `##` the draft gives the sheet.
    text = HEADING.sub(lambda m: '#' * min(6, len(m.group(1)) + base_level - 1) + ' ', text)
    text = re.sub(r'\n{3,}', '\n\n', text)
    return text.strip()


# --------------------------------------------------------------- assembling

def figure(sheet: dict, original: pathlib.PurePosixPath, page: pathlib.PurePosixPath) -> str:
    """The phase 3 figure block for one sheet's scan, as seen from `page`."""
    web = original.parent.parent / 'web'
    rel = pathlib.PurePosixPath(os.path.relpath(web, page.parent))
    stem = original.stem
    classes = 'sheet' if sheet['fold'] == 'A4' else 'sheet sheet--fold'
    title = sheet['title'].replace('[', '(').replace(']', ')')
    pages = sheet['scan_pages'].replace('+', ', ')
    label = 'pages' if '+' in sheet['scan_pages'] else 'page'
    cs = (f'\n  <span class="cs">{sheet["cs_code"]}</span>'
          if sheet['cs_code'] else '')
    return (f'<figure class="{classes}" markdown>\n'
            f'[![{title}]({rel}/{stem}-preview.webp)]({rel}/{stem}-zoom.webp)\n'
            f'<figcaption>\n'
            f'  {title}.{cs}\n'
            f'  <span class="src">service manual {label} {pages}</span>\n'
            f'</figcaption>\n'
            f'</figure>')


def front_matter(existing: str) -> tuple[str, str]:
    """Split a page into its YAML front matter and the rest."""
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
    """The one-line description the phase 3 stub put under its H1."""
    m = re.search(r'^# .+\n\n(.+?)\n', body, re.M)
    if not m or m.group(1).startswith(('!!!', '<', '|', '-')):
        return ''
    return m.group(1)


def draft(page: str, sheets: list[dict], originals: dict[str, pathlib.PurePosixPath]) -> str:
    path = DOCS / page
    existing = path.read_text() if path.exists() else ''
    fm, body = front_matter(existing)
    posix = pathlib.PurePosixPath('docs') / page

    out = [fm.rstrip('\n'), '', MARKER, '',
           f'# {h1_of(body) or page}', '']
    lead = lead_of(body)
    if lead:
        out += [lead, '']

    for sheet in sheets:
        original = originals.get(sheet['sheet'])
        if original is None:
            print(f'  ! sheet {sheet["sheet"]} has no migrated original', file=sys.stderr)
            continue
        out.append(f'## {sheet["title"]}')
        out.append('')
        if sheet['content_type'] not in FIGURE_ONLY_TYPES:
            ocr = ROOT / sheet['ocr_path']
            if ocr.exists():
                text = normalise(ocr.read_text())
                if text:
                    out += [text, '']
            else:
                print(f'  ! sheet {sheet["sheet"]}: missing {sheet["ocr_path"]}',
                      file=sys.stderr)
        out.append(figure(sheet, original, posix))
        out.append('')

    return '\n'.join(out).rstrip('\n') + '\n'


def writable(path: pathlib.Path, force: bool) -> bool:
    if force or not path.exists():
        return True
    text = path.read_text()
    return MARKER in text or STUB_MARKER in text


def main() -> None:
    ap = argparse.ArgumentParser(description=__doc__,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument('--pages', nargs='*', default=None, metavar='PREFIX',
                    help='restrict to pages whose path starts with a prefix')
    ap.add_argument('--dry-run', action='store_true')
    ap.add_argument('--force', action='store_true',
                    help='overwrite pages that have had their editing pass')
    args = ap.parse_args()

    originals = asset_stems()
    pages = sheets_by_page()
    if args.pages:
        pages = {p: s for p, s in pages.items()
                 if any(p.startswith(pre) for pre in args.pages)}

    written = skipped = 0
    for page in sorted(pages):
        path = DOCS / page
        if not writable(path, args.force):
            print(f'  = {page} (hand-edited, left alone)')
            skipped += 1
            continue
        text = draft(page, pages[page], originals)
        n = len(pages[page])
        print(f'  {"?" if args.dry_run else "+"} {page} ({n} sheet{"s" * (n != 1)})')
        if not args.dry_run:
            path.write_text(text)
        written += 1

    verb = 'would write' if args.dry_run else 'wrote'
    print(f'{verb} {written} pages'
          + (f', {skipped} already edited' if skipped else ''))


if __name__ == '__main__':
    main()
