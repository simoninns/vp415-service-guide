#!/usr/bin/env python3
"""Phase 5: turn chapter 4 into the twenty-six module page drafts.

  unsorted-source-material/ocr-markdown-service-manual/**/markdown.md
      -> docs/modules/<module>/index.md

Chapter 4 is not laid out like the other chapters. Every other chapter is a run
of text pages that `import_ocr.py` can pour into a site page in sheet order;
chapter 4 is one *data sheet* and one *circuit diagram* per module, and a module
page has to interleave them with material from chapters 3, 7 and 8 and with the
photographs, which are not in the manual at all. So this is a second importer
rather than another `SECTION_PAGE` entry, and it assembles a fixed skeleton:

    Overview - The board - Where it sits - Circuit description - Adjustments
    - Circuit diagram - PCB lay-out - List of electrical parts
    - Modification levels - Related

What it fills in mechanically:

  * the sheets that belong to the module, from the sheet map's per-panel
    `module` column - not from the file's location, since four bifolds carry
    two modules each
  * a figure block per sheet in the phase 3 pattern, captioned with the `CS`
    code and the manual page number, reaching across module directories where
    a sheet is shared (`CS 7 850` is N and P, `CS 7 851` is Q and R)
  * the module photographs as a `.sheet-pair`, top beside bottom
  * the adjustment procedure, lifted out of the data sheet's OCR
  * the list of electrical parts, unfolded from the OCR's multi-column grids
    into one table per component class - see `unfold()`
  * links at the chapter 7 and chapter 8 anchors, and the mod levels the
    survey records for the module

What it deliberately does not do is write prose. The overview, the location
description and the related links are the editing pass, as in phase 4.

The tool will not overwrite a page that has had that pass: it writes only over
a phase 3 stub or over its own output, unless `--force` says otherwise.

Usage
  tools/import_modules.py                 draft every module page
  tools/import_modules.py J S W           restrict to modules (RC = remote)
  tools/import_modules.py --dry-run       report what would be written
  tools/import_modules.py --force J       redraft one page, editing and all
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
MODULES = DOCS / 'modules'

MARKER = '<!-- drafted by tools/import_modules.py - hand-edited afterwards -->'
STUB_MARKER = 'Not written yet'

# Module letter -> directory, title and one-line description. The order is the
# manual's own, which is also the site's navigation order.
MODULE_DIRS = {
    'A':  'a-audio-processor',
    'B':  'b-rgb',
    'C':  'c-video-processor',
    'D':  'd-reference-source',
    'E':  'e-slide-drive',
    'F':  'f-motor-sequence',
    'G':  'g-genlock',
    'H':  'h-etbc-b',
    'I':  'i-etbc-c',
    'J':  'j-focus',
    'K':  'k-hf-processor',
    'L':  'l-video-dropout-correction',
    'M':  'm-radial',
    'N':  'n-display-keyboard',
    'P':  'p-frontloader',
    'Q':  'q-rc5-receiver',
    'R':  'r-drive-processor',
    'S':  's-control',
    'T':  't-supply',
    'U':  'u-analog-io',
    'V':  'v-module-carrier',
    'W':  'w-cpu-data-grabber',
    'X':  'x-lv-rom-decoder',
    'Y':  'y-video-mixer',
    'Z':  'z-deck-electronics',
    'RC': 'remote-control',
}

# The chapter 7 anchor for each module, on circuit-description/modules.md.
# Four of these do not follow from the sheet map - module G's description is on
# the second panel of the sheet the map files under F, module Y's on the sheet
# filed under X - and modules Q, V and the remote control have no description
# at all. See phase 4, finding 4.
CIRCUIT_ANCHORS = {m: f'module-{m.lower()}' for m in MODULE_DIRS if m != 'RC'}
CIRCUIT_ANCHORS['U'] = 'module-ua'
del CIRCUIT_ANCHORS['Q'], CIRCUIT_ANCHORS['V']

# The chapter 8 anchor, on service-information/modification-levels.md. Eight
# modules have no mod-level sheet; the page says so rather than linking.
MOD_LEVEL_ANCHORS = {m: f'mod-{m.lower()}' for m in
                     'A B C F G H I J K L M R S T U Y Z'.split()}

# The survey of modification levels, sheet 167-168, read across the eight
# production batches: first level shipped -> last. Transcribed in phase 4 on
# service-information/modification-levels.md.
MOD_LEVELS = {
    'A': '2 → 3', 'B': '5 → 7', 'C': '3 → 4', 'D': '2', 'E': '3',
    'F': '5 → 6', 'G': '3 → 4', 'H': '5', 'I': '6 → 7', 'J': '2 → 4',
    'K': '0', 'L': '0 → 1', 'M': '0 → 3', 'N': '1', 'P': '4', 'Q': '0',
    'R': '3 → 7', 'S': '3 → 8', 'T': '1', 'U': '3 → 4', 'V': '1 → 3',
    'W': '2 → 3', 'X': '2', 'Y': '4 → 6', 'Z': '2 → 3',
}

# What each chapter 4 sheet is, for the overview table.
SHEET_ROLE = {
    'circuit':     'Circuit diagram',
    'module-sheet': 'Data sheet',
    'pcb-layout':  'PCB lay-out',
    'parts':       'Parts list',
    'adjustments': 'Adjustments',
}

# Sheet 032 (module A) is the one data sheet whose parts grid lost its
# left-hand item-number column in the OCR. Read off the 300 dpi scan, that
# column is capacitors 2001 to 2022 in order, and its service codes and values
# came through intact - so the numbers are restored here rather than the block
# being published without them.
LOST_ITEM_COLUMN = {'032': ('Capacitors', 2001)}

# Item-number prefixes, from the manual's four-number diagram coding - see
# general-service/remarks.md, section 6. Used to head each parts table when the
# sheet's own category label did not survive the OCR.
ITEM_CLASS = {
    '1': 'Units and batteries', '2': 'Capacitors', '3': 'Resistors',
    '5': 'Coils, transformers and crystals', '6': 'Diodes',
    '7': 'Transistors and integrated circuits',
}

# Supply module T is listed in the board's letter coding instead. Only the
# classes that turn up without a label of their own need mapping.
LETTER_CLASS = {'C': '2', 'R': '3', 'L': '5', 'D': '6'}


def item_class(item: str) -> str:
    """The class key of an item number, in either of the manual's codings."""
    if not item:
        return ''
    return item[:1] if item[:1].isdigit() else LETTER_CLASS.get(item[:1], '')


# ------------------------------------------------------------------ sources

def read_csv(path: pathlib.Path) -> list[dict]:
    with open(path, newline='') as fh:
        return list(csv.DictReader(fh))


def sheets_by_module() -> dict[str, list[dict]]:
    """Module letter -> its chapter 4 sheets, in manual order.

    Driven by the per-panel `module` column, so a sheet whose panels carry two
    modules turns up under both. The panel rows are collapsed to one row per
    sheet, carrying the panels that module owns.
    """
    out: dict[str, list[dict]] = {}
    for row in read_csv(SHEET_MAP):
        if row['chapter'] != '4' or not row['module']:
            continue
        rows = out.setdefault(row['module'], [])
        if rows and rows[-1]['sheet'] == row['sheet']:
            rows[-1]['panels_owned'].append(row['panel'])
            continue
        rows.append(dict(row, panels_owned=[row['panel']]))
    return out


def originals() -> dict[str, pathlib.PurePosixPath]:
    """Sheet -> the docs-relative path of its archival original."""
    return {r['sheet']: pathlib.PurePosixPath(r['dest_path'])
            for r in read_csv(MIGRATION_LOG) if r['sheet']}


MODULE_LINK = re.compile(r'\(\.\./modules/([a-z0-9-]+)/index\.md')
TITLE = re.compile(r'^title: (.+)$', re.M)


def backlinks() -> dict[str, list[tuple[str, str]]]:
    """Module directory -> the pages elsewhere on the site that link to it.

    Chapters 3, 6, 7 and 8 already name the modules they touch, so the
    module's own "Related" list can be read off those links rather than
    guessed - and it cannot go stale without the link going stale too.
    """
    found: dict[str, list[tuple[str, str]]] = {}
    for page in sorted(DOCS.rglob('*.md')):
        rel = page.relative_to(DOCS)
        if rel.parts[0] == 'modules':
            continue
        text = page.read_text()
        title = TITLE.search(text)
        for m in set(MODULE_LINK.findall(text)):
            found.setdefault(m, []).append(
                (rel.as_posix(), title.group(1) if title else rel.stem))
    return {k: sorted(v) for k, v in found.items()}


def photographs(module: str) -> dict[str, pathlib.PurePosixPath]:
    """The module's photographs, keyed 'top' / 'bottom' / 'other'."""
    found: dict[str, pathlib.PurePosixPath] = {}
    for row in read_csv(MIGRATION_LOG):
        dest = pathlib.PurePosixPath(row['dest_path'])
        if row['profile'] not in ('module-photo', 'photo'):
            continue
        if dest.parent.parent.parent.name != MODULE_DIRS[module]:
            continue
        key = ('top' if dest.stem.endswith('-top')
               else 'bottom' if dest.stem.endswith('-bottom') else 'other')
        found[key] = dest
    return found


# ------------------------------------------------------- text normalisation

# `import_ocr.py`'s LaTeX table, kept in step with it.
LATEX = [
    (r'\mathrm', ''), (r'\text', ''), (r'\mathbf', ''),
    (r'\geqslant', '≥'), (r'\leqslant', '≤'), (r'\geq', '≥'), (r'\leq', '≤'),
    (r'\Omega', 'Ω'), (r'\omega', 'ω'), (r'\mu', 'μ'), (r'\Delta', 'Δ'),
    (r'\times', '×'), (r'\cdot', '·'), (r'\pm', '±'), (r'\approx', '≈'),
    (r'\circ', '°'), (r'\degree', '°'), (r'\infty', '∞'), (r'\rightarrow', '→'),
    (r'\%', '%'), (r'\&', '&'), (r'\#', '#'), (r'\_', '_'), (r'\ ', ' '),
]

MATH = re.compile(r'\\\((.+?)\\\)|\\\[(.+?)\\\]|\$(.+?)\$', re.S)
IMG = re.compile(r'!\[[^\]]*\]\([^)]*\)')
CS_TAIL = re.compile(r'^\s*CS\s*\d\s*\d{3}\s*$', re.M)
# The vendor OCR sometimes appends its own layout JSON, and on the diagram
# sheets it loops on the sheet's grid numbering for thousands of characters.
BOX_JSON = re.compile(r'\[\{"box_2d".*?\}\]', re.S)
GRID_RUN = re.compile(r'^(?:\d+ ){9,}\d+\s*$', re.M)
# The drawing-office stamp printed beside each figure on a data sheet.
STAMP = re.compile(r'^\s*(MDA-\d+|T\d+/\d+)\s*$', re.M)
# Every data sheet prints a component locator above its PCB lay-out: item
# number against grid square, "2001 A 4", hundreds of them. It belongs to the
# drawing, not to the parts list, and it is not reproduced as text - the
# lay-out figure carries it.
LOCATOR_CELL = re.compile(r'^\d{4}\s*[A-D]\s*\d$')


def unmath(text: str) -> str:
    def one(m: re.Match) -> str:
        body = next(g for g in m.groups() if g is not None)
        for src, dst in LATEX:
            body = body.replace(src, dst)
        body = body.replace('{', '').replace('}', '')
        return re.sub(r'\s+', ' ', body).strip()
    return MATH.sub(one, text)


def is_locator(line: str) -> bool:
    """Is this table row part of a component locator grid?"""
    if not line.startswith('|') or is_rule(line):
        return False
    got = [c for c in cells(line) if c]
    return len(got) > 2 and sum(bool(LOCATOR_CELL.match(c)) for c in got) > len(got) / 2


def clean(text: str) -> str:
    """OCR markdown -> readable text: no images, no LaTeX, no OCR debris."""
    text = '\n'.join(l for l in text.split('\n') if not is_locator(l))
    text = BOX_JSON.sub('', text)
    text = IMG.sub('', text)
    text = GRID_RUN.sub('', text)
    text = CS_TAIL.sub('', text)
    text = STAMP.sub('', text)
    text = unmath(text)
    return re.sub(r'\n{3,}', '\n\n', text).strip()


def cells(line: str) -> list[str]:
    """The cells of a GFM table row, outer pipes dropped."""
    return [c.strip() for c in line.strip().strip('|').split('|')]


def is_rule(line: str) -> bool:
    return bool(re.fullmatch(r'\|[\s|:-]+\|', line.strip()))


def table_blocks(text: str) -> list[tuple[int, int]]:
    """(start, end) line indices of each run of table rows."""
    lines = text.split('\n')
    blocks, start = [], None
    for i, line in enumerate(lines + ['']):
        if line.startswith('|'):
            start = i if start is None else start
        elif start is not None:
            blocks.append((start, i))
            start = None
    return blocks


# ------------------------------------------------------------------- parts

ITEM = re.compile(r'^\d{4}$')
# A Philips service code number: four digits, three digits, five digits.
CODE = re.compile(r'[45]\d{3} \d{3} \d{5}')
# A parts line the OCR left as prose: "3026 4822 111 30483 1 Ω". The item is
# usually the diagram's four-number code, but supply module T is listed in the
# board's own letter/number coding - "C001", "F911" - see remarks, section 6.
LOOSE = re.compile(r'^([0-9]{4}|[A-Z]{1,3}[0-9]{2,4})\s+'
                   r'([45]\d{3} \d{3} \d{5})\s*(.*)$')
# A "category label" the OCR invented out of a value or a rating that wrapped
# onto a line of its own.
NOT_A_LABEL = re.compile(r'^[\d.,/ ]*(%|V|A|W|Ω|[kM]Ω|[numpμ]?F|[munp]?H)?[\d.,/ ]*$')

# What class a category label off the sheet describes, so that a label left
# standing above the wrong block - the OCR drops blank lines - does not carry
# over onto items it cannot belong to.
LABEL_CLASS = [
    ('capaci', '2'), ('potentiometer', '3'), ('resist', '3'),
    ('coil', '5'), ('crystal', '5'), ('delay', '5'), ('filter', '5'),
    ('transformer', '5'), ('diode', '6'), ('transistor', '7'),
    ('integrated', '7'),
]


# Category labels the OCR misread. The sheet's own spelling is on the scan.
LABEL_TYPOS = {'Cells': 'Coils', 'Colts': 'Coils', 'Coll': 'Coils',
               'NPR25 Resistors': 'NFR25 Resistors',
               'Trimcapaci': 'Trimcapacitors'}


def label_class(label: str) -> str:
    """The item-number prefix a category label implies, or '' if unclear."""
    low = label.lower()
    for word, prefix in LABEL_CLASS:
        if word in low:
            return prefix
    return ''


def split_value(rest: str) -> tuple[str, str]:
    """"2.2 Ω" -> value; "470 nF 16 V" -> value and working voltage."""
    m = re.match(r'^(.*?)\s+((?:\d+\s*%\s+)?\d+\s*V\b.*)$', rest)
    return (m.group(1), m.group(2)) if m else (rest, '')


def groups_of(row: list[str]) -> list[list[str]]:
    """Split one grid row into its component groups.

    The manual prints the bulk parts as a grid three or four components wide:
    item, service code, value, rating. The OCR flattens that to one long row,
    and occasionally loses the leading item cell of the first group - so the
    groups are cut from the right, and whatever is left over at the left is a
    short group.
    """
    if len(row) <= 4:
        return [row]
    out, rest = [], row
    while len(rest) >= 4:
        out.append(rest[-4:])
        rest = rest[:-4]
    if rest:
        out.append(rest)
    return list(reversed(out))


def parts_rows(text: str) -> list[tuple[str, list[str]]]:
    """The parts list as (category, [item, code, value, rating]) rows.

    Category comes from the sheet's own label where the OCR kept it - `Coils`,
    `NFR25 Resistors` - and otherwise from the item number's leading digit.
    """
    rows: list[tuple[str, list[str]]] = []
    category = ''
    lines = text.split('\n')
    for line in lines:
        line = line.strip()
        if not line:
            continue
        if line.startswith('|'):
            if is_rule(line):
                continue
            for group in groups_of(cells(line)):
                group = (group + ['', '', '', ''])[:4]
                if ITEM.match(group[0]):
                    pass
                elif group[0] and not any(group[1:]):
                    if not NOT_A_LABEL.match(group[0]):
                        category = group[0]       # a category label, alone
                    continue
                elif CODE.fullmatch(group[0]):
                    # The OCR lost this column's item cell: everything has
                    # shifted one to the left. Shift it back.
                    group = [''] + group[:3]
                elif not any(group):
                    continue
                # A stray item number from the next column of the sheet.
                if ITEM.fullmatch(group[3]):
                    group[3] = ''
                rows.append((category, group))
            continue
        loose = LOOSE.match(line)
        if loose:
            value, rating = split_value(loose.group(3))
            rows.append((category, [loose.group(1), loose.group(2), value, rating]))
        elif (len(line) < 40 and not line.endswith(('.', ':'))
                and not NOT_A_LABEL.match(line)):
            category = line                        # a category label, alone
    return rows


def parts_tables(text: str, sheet: str = '') -> str:
    """The unfolded parts list, one table per component class.

    The manual prints the list in columns, class by class, and the OCR reads
    it across the columns rather than down them - so the rows arrive
    interleaved and have to be gathered back into their classes here. Within a
    class the item number restores the sheet's own order; rows whose item cell
    the OCR lost keep the order they were read in.
    """
    rows = [r for r in parts_rows(text) if any(r[1])]
    restore = LOST_ITEM_COLUMN.get(sheet)
    if restore:
        heading, first = restore
        numbered = ((i, r) for i, r in enumerate(r for _, r in rows if not r[0]))
        for offset, row in numbered:
            row[0] = str(first + offset)
        rows = [(heading if not c else c, r) for c, r in rows]
    # Some sheets come back twice over: once as a bare column of item numbers
    # and once as the full rows. Keep the full row.
    have = {r[0] for _, r in rows if r[0] and any(r[1:])}
    rows = [(c, r) for c, r in rows if any(r[1:]) or r[0] not in have]
    tables: dict[str, list[list[str]]] = {}
    for category, row in rows:
        item = row[0]
        # Keep the sheet's own label only where it can describe this item.
        keep = category and label_class(category) in ('', item_class(item))
        heading = category if keep else ITEM_CLASS.get(item_class(item), 'Other')
        heading = LABEL_TYPOS.get(heading, heading)
        tables.setdefault(heading, []).append(row)
    out: list[str] = []
    for heading, rows in tables.items():
        rows.sort(key=lambda r: r[0] or 'zzzz')
        if out:
            out.append('')
        out += [f'**{heading}**', '',
                '| Item | Service code number | Value | Rating |',
                '| --- | --- | --- | --- |']
        out += [f'| {" | ".join(r)} |' for r in rows]
    return '\n'.join(out)


# --------------------------------------------------------------- assembling

def split_sheet(text: str) -> tuple[str, str]:
    """A data sheet's OCR -> (adjustment procedure, parts list)."""
    text = clean(text)
    parts = re.split(r'^#*\s*LIST OF ELECTRICAL PARTS[^\n]*$', text,
                     maxsplit=1, flags=re.M | re.I)
    body, tail = parts[0], parts[1] if len(parts) > 1 else ''
    adjust = re.split(r'^#*\s*ADJUSTMENTS\s*$', body, maxsplit=1, flags=re.M | re.I)
    return (adjust[1].strip() if len(adjust) > 1 else '', tail.strip())


def figure(sheet: dict, original: pathlib.PurePosixPath, page: pathlib.PurePosixPath,
           caption: str = '', klass: str = '') -> str:
    """The phase 3 figure block for one sheet's scan, as seen from `page`."""
    web = original.parent.parent / 'web'
    rel = pathlib.PurePosixPath(os.path.relpath(web, page.parent))
    title = sheet['title'].replace('[', '(').replace(']', ')')
    pages = sheet['scan_pages'].replace('+', ', ')
    label = 'pages' if '+' in sheet['scan_pages'] else 'page'
    cs = (f'\n  <span class="cs">{sheet["cs_code"]}</span>'
          if sheet['cs_code'] else '')
    klass = klass or ('sheet' if sheet['fold'] == 'A4' else 'sheet sheet--fold')
    return (f'<figure class="{klass}" markdown>\n'
            f'[![{title}]({rel}/{original.stem}-preview.webp)]'
            f'({rel}/{original.stem}-zoom.webp)\n'
            f'<figcaption>\n'
            f'  {caption or title + "."}{cs}\n'
            f'  <span class="src">service manual {label} {pages}</span>\n'
            f'</figcaption>\n'
            f'</figure>')


def photo_pair(module: str, photos: dict, page: pathlib.PurePosixPath) -> str:
    """Top and bottom of the board, side by side."""
    def one(key: str, side: str) -> str:
        original = photos[key]
        rel = pathlib.PurePosixPath(
            os.path.relpath(original.parent.parent / 'web', page.parent))
        return ('<figure class="sheet sheet--photo" markdown>\n'
                f'[![Module {module}, {side} of the board]'
                f'({rel}/{original.stem}-preview.webp)]'
                f'({rel}/{original.stem}-zoom.webp)\n'
                f'<figcaption>\n  Module {module}, {side}.\n</figcaption>\n'
                '</figure>')
    have = [(k, s) for k, s in (('top', 'component side'),
                                ('bottom', 'solder side')) if k in photos]
    if not have:
        return ''
    if len(have) == 1:
        return one(*have[0])
    return ('<div class="sheet-pair" markdown>\n'
            + '\n'.join(one(k, s) for k, s in have)
            + '\n</div>')


def front_matter(existing: str) -> tuple[str, str]:
    if not existing.startswith('---\n'):
        return '', existing
    end = existing.find('\n---\n', 4)
    return ('', existing) if end < 0 else (existing[:end + 5], existing[end + 5:])


def h1_of(body: str) -> str:
    m = re.search(r'^# (.+)$', body, re.M)
    return m.group(1) if m else ''


def lead_of(body: str) -> str:
    m = re.search(r'^# .+\n\n(.+?)\n', body, re.M)
    if not m or m.group(1).startswith(('!!!', '<', '|', '-')):
        return ''
    return m.group(1)


def draft(module: str, sheets: list[dict], assets: dict) -> str:
    directory = MODULE_DIRS[module]
    path = MODULES / directory / 'index.md'
    fm, body = front_matter(path.read_text() if path.exists() else '')
    posix = pathlib.PurePosixPath('docs/modules') / directory / 'index.md'
    up = '../..'

    data_sheets = [s for s in sheets if s['content_type'] in
                   ('module-sheet', 'parts', 'pcb-layout', 'adjustments')]
    diagrams = [s for s in sheets if s['content_type'] == 'circuit']

    out = [fm.rstrip('\n'), '', MARKER, '', f'# {h1_of(body)}', '']
    lead = lead_of(body)
    if lead:
        out += [lead, '']

    # ------------------------------------------------------------ overview
    out += ['## Overview', '',
            '| | |', '| --- | --- |',
            f'| Designation | **{module}** |',
            f'| Modification levels | {MOD_LEVELS.get(module, "—")} |']
    for s in sheets:
        code = s['cs_code'] or '—'
        label = 'pages' if '+' in s['scan_pages'] else 'page'
        panels = (f', panel{"s" * (len(s["panels_owned"]) > 1)} '
                  + '+'.join(s['panels_owned'])
                  if len(s['panels_owned']) != int(s['panels']) else '')
        out.append(f'| {SHEET_ROLE[s["content_type"]]} | `{code}`, '
                   f'{label} {s["scan_pages"].replace("+", ", ")}{panels} |')
    out.append('')

    # ----------------------------------------------------------- the board
    pair = photo_pair(module, assets['photos'], posix)
    if pair:
        out += ['## The board', '', pair, '']

    # -------------------------------------------------------- where it sits
    out += ['## Where it sits in the player', '',
            f'See the [module and connector lay-out]({up}/system/module-layout.md).',
            '']

    # -------------------------------------------------- circuit description
    anchor = CIRCUIT_ANCHORS.get(module)
    out += ['## Circuit description', '']
    if anchor:
        out += [f'[Chapter 7, module {module}]'
                f'({up}/circuit-description/modules.md#{anchor}).', '']
    else:
        out += ['The manual carries no circuit description for this module.', '']

    # --------------------------------------------------------- adjustments
    adjust = '\n\n'.join(a for a in
                         (assets['ocr'][s['sheet']][0] for s in data_sheets) if a)
    out += ['## Adjustments', '', adjust or 'None.', '']

    # ------------------------------------------------------ circuit diagram
    if diagrams:
        out += ['## Circuit diagram', '']
        for s in diagrams:
            out += [figure(s, assets['originals'][s['sheet']], posix), '']

    # ------------------------------------------------------------ lay-out
    if data_sheets:
        out += ['## PCB lay-out', '']
        for s in data_sheets:
            out += [figure(s, assets['originals'][s['sheet']], posix), '']

    # -------------------------------------------------------------- parts
    parts = '\n\n'.join(p for p in
                        (parts_tables(assets['ocr'][s['sheet']][1], s['sheet'])
                         for s in data_sheets) if p)
    out += ['## List of electrical parts', '', parts or 'None listed.', '']

    # ---------------------------------------------------------- mod levels
    mod_anchor = MOD_LEVEL_ANCHORS.get(module)
    out += ['## Modification levels', '']
    if mod_anchor:
        out += [f'[Chapter 8, module {module}]'
                f'({up}/service-information/modification-levels.md#{mod_anchor}).', '']
    else:
        out += ['The manual has no modification-level sheet for this module.', '']

    out += ['## Related', '']
    for page, title in assets['backlinks'].get(directory, []):
        out.append(f'- [{title}]({up}/{page})')
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
    ap.add_argument('modules', nargs='*', metavar='MODULE',
                    help='module letters to draft (default: all)')
    ap.add_argument('--dry-run', action='store_true')
    ap.add_argument('--force', action='store_true',
                    help='overwrite pages that have had their editing pass; '
                         'only ever for named modules, never for all of them')
    args = ap.parse_args()
    if args.force and not args.modules:
        ap.error('--force needs the modules named: it destroys hand editing')

    by_module = sheets_by_module()
    original_of = originals()
    related = backlinks()
    wanted = [m.upper() for m in args.modules] or list(MODULE_DIRS)

    written = skipped = 0
    for module in wanted:
        if module not in MODULE_DIRS:
            print(f'  ! unknown module {module}', file=sys.stderr)
            continue
        sheets = by_module.get(module, [])
        path = MODULES / MODULE_DIRS[module] / 'index.md'
        if not writable(path, args.force):
            print(f'  = module {module} (hand-edited, left alone)')
            skipped += 1
            continue
        assets = {
            'originals': original_of,
            'photos': photographs(module),
            'ocr': {s['sheet']: split_sheet((ROOT / s['ocr_path']).read_text())
                    for s in sheets},
            'backlinks': related,
        }
        text = draft(module, sheets, assets)
        print(f'  {"?" if args.dry_run else "+"} module {module} '
              f'({len(sheets)} sheet{"s" * (len(sheets) != 1)}, '
              f'{len(assets["photos"])} photograph{"s" * (len(assets["photos"]) != 1)})')
        if not args.dry_run:
            path.write_text(text)
        written += 1

    verb = 'would write' if args.dry_run else 'wrote'
    print(f'{verb} {written} module pages'
          + (f', {skipped} already edited' if skipped else ''))


if __name__ == '__main__':
    main()
