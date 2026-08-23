#!/usr/bin/env python3
"""Phase 2a: migrate source material into its final home under docs/.

There is exactly one copy of any given file in this repository. Rather than
leaving originals in unsorted-source-material/ and generating a second web copy
beside them, each file is `git mv`d into docs/<section>/assets/originals/ and
unsorted-source-material/ empties out.

Two maps drive the moves, and between them they account for every file:

  planning/service-manual-sheet-map.csv   the 180 canonical service-manual sheets,
                                          named by Philips CS code and scan page
  tools/asset_map.csv                     everything else - photographs, firmware,
                                          scope traces, the operating instructions

A file is moved only if it is accounted for in tools/asset_map.csv. Rows marked
`source-text` (the vendor OCR, consumed by tools/import_ocr.py in phase 4) and
`exclude` stay where they are, so unsorted-source-material/ does not empty out
until phase 4.

Every move is appended to planning/migration-log.csv, so the rename never loses
the provenance of a file.

Usage
  tools/migrate.py --dry-run                 show the whole plan, move nothing
  tools/migrate.py --all                     migrate everything
  tools/migrate.py --section modules         migrate one section
  tools/migrate.py --section modules/j-focus migrate one module
  tools/migrate.py --all --no-git            plain rename instead of `git mv`
"""
from __future__ import annotations

import argparse
import collections
import csv
import pathlib
import re
import subprocess
import sys

ROOT = pathlib.Path(__file__).resolve().parent.parent
SHEET_MAP = ROOT / 'planning/service-manual-sheet-map.csv'
ASSET_MAP = ROOT / 'tools/asset_map.csv'
LOG = ROOT / 'planning/migration-log.csv'

SCAN_ROOT = 'unsorted-source-material/vp415 service manual'

LOG_FIELDS = ['source_path', 'dest_path', 'origin', 'disposition', 'profile',
              'sheet', 'cs_code', 'notes']

# The dispositions that describe a file with a home under docs/.
MOVING = {'publish', 'download', 'convert'}

# module letter -> docs/modules/<slug>; must agree with tools/build_asset_map.py
MODULE_SLUG = {
    'A': 'a-audio-processor',   'B': 'b-rgb',              'C': 'c-video-processor',
    'D': 'd-reference-source',  'E': 'e-slide-drive',      'F': 'f-motor-sequence',
    'G': 'g-genlock',           'H': 'h-etbc-b',           'I': 'i-etbc-c',
    'J': 'j-focus',             'K': 'k-hf-processor',     'L': 'l-video-dropout-correction',
    'M': 'm-radial',            'N': 'n-display-keyboard', 'P': 'p-frontloader',
    'Q': 'q-rc5-receiver',      'R': 'r-drive-processor',  'S': 's-control',
    'T': 't-supply',            'U': 'u-analog-io',        'V': 'v-module-carrier',
    'W': 'w-cpu-data-grabber',  'X': 'x-lv-rom-decoder',   'Y': 'y-video-mixer',
    'Z': 'z-deck-electronics',  'RC': 'remote-control',
}

# manual chapter -> the section directory it becomes on the site
CHAPTER_DIR = {
    'front': 'docs',
    '1': 'docs/overview',
    '2': 'docs/general-service',
    '3': 'docs/system',
    '4': 'docs/modules',
    '5': 'docs/parts',
    '6': 'docs/repair',
    '7': 'docs/circuit-description',
    '8': 'docs/service-information',
}

# content_type -> derivative profile. Fold-outs override this to `schematic`
# whatever they carry, because a bifold table needs native resolution as much as
# a bifold schematic does.
TEXTUAL = {'text', 'table', 'contents', 'cover', 'divider', 'parts', 'adjustments'}


def slug(text: str) -> str:
    return re.sub(r'[^a-z0-9]+', '-', text.lower()).strip('-')


def page_part(sheet: str) -> str:
    """'053' -> 'p053';  '061_062' -> 'p061-062'."""
    return 'p' + sheet.replace('_', '-')


def sheet_dest(rows: list[dict]) -> tuple[str, str, str]:
    """-> (dest_dir, dest_name, profile) for one sheet's panel rows.

    A sheet is one physical piece of paper and therefore one file, even when its
    panels belong to two different modules. It is filed under the module holding
    the most panels (panel 1 wins a tie) and cross-referenced from the other.
    """
    first = rows[0]
    chapter, section = first['chapter'], first['section']
    base = CHAPTER_DIR[chapter]

    if chapter == '4' and section == 'module':
        tally = collections.Counter(r['module'] for r in rows)
        top = max(tally.values())
        module = next(r['module'] for r in rows if tally[r['module']] == top)
        base = f'{base}/{MODULE_SLUG[module]}'

    content_type = first['content_type']
    name_stem = slug(f"{first['cs_code']} {content_type}") if first['cs_code'] \
        else slug(content_type)
    name = f'{name_stem}-{page_part(first["sheet"])}.webp'

    profile = 'text-page' if (content_type in TEXTUAL and first['fold'] == 'A4') \
        else 'schematic'
    return f'{base}/assets/originals', name, profile


def build_plan() -> list[dict]:
    """Every move this repository will ever make, sheet-map rows first."""
    accounted = {r['path']: r for r in csv.DictReader(open(ASSET_MAP))}
    plan: list[dict] = []

    # --- the 180 canonical service-manual sheets ---------------------------
    by_sheet: dict[str, list[dict]] = collections.defaultdict(list)
    for row in csv.DictReader(open(SHEET_MAP)):
        by_sheet[row['sheet']].append(row)

    for sheet, rows in sorted(by_sheet.items()):
        rows.sort(key=lambda r: int(r['panel']))
        src = f"{SCAN_ROOT}/{rows[0]['publish_source']}"
        if src not in accounted:
            sys.exit(f'not accounted for in asset_map.csv: {src}')
        if accounted[src]['disposition'] != 'page-map':
            sys.exit(f'expected disposition page-map for {src}')
        dest_dir, dest_name, profile = sheet_dest(rows)
        modules = sorted({r['module'] for r in rows if r['module']})
        notes = rows[0]['title']
        if len(modules) > 1:
            notes += f" [panels span modules {', '.join(modules)}]"
        plan.append(dict(source_path=src, dest_path=f'{dest_dir}/{dest_name}',
                         origin='sheet-map', disposition='publish', profile=profile,
                         sheet=sheet, cs_code=rows[0]['cs_code'], notes=notes))

    # --- everything else with a home under docs/ ---------------------------
    for row in accounted.values():
        if row['disposition'] not in MOVING:
            continue
        if not row['dest_dir'] or not row['dest_name']:
            sys.exit(f"disposition {row['disposition']} without a destination: {row['path']}")
        plan.append(dict(source_path=row['path'],
                         dest_path=f"{row['dest_dir']}/{row['dest_name']}",
                         origin='asset-map', disposition=row['disposition'],
                         profile=row['profile'], sheet='', cs_code='', notes=row['notes']))

    clashes = [d for d, n in collections.Counter(e['dest_path'] for e in plan).items() if n > 1]
    if clashes:
        sys.exit('destination collision:\n  ' + '\n  '.join(sorted(clashes)))
    return plan


def matches(entry: dict, sections: list[str]) -> bool:
    if not sections:
        return True
    rel = entry['dest_path'][len('docs/'):]
    return any(rel == s or rel.startswith(s.rstrip('/') + '/') for s in sections)


def read_log() -> set[str]:
    if not LOG.exists():
        return set()
    return {r['dest_path'] for r in csv.DictReader(open(LOG))}


def append_log(entries: list[dict]) -> None:
    new = not LOG.exists()
    with open(LOG, 'a', newline='') as fh:
        w = csv.DictWriter(fh, LOG_FIELDS)
        if new:
            w.writeheader()
        w.writerows(entries)


def main() -> None:
    ap = argparse.ArgumentParser(description=__doc__,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument('--section', action='append', default=[], metavar='PATH',
                    help="section under docs/ to migrate, e.g. 'modules/j-focus'")
    ap.add_argument('--all', action='store_true', help='migrate every section')
    ap.add_argument('--dry-run', action='store_true', help='report the plan, move nothing')
    ap.add_argument('--no-git', action='store_true', help='plain rename instead of `git mv`')
    args = ap.parse_args()

    if not args.all and not args.section and not args.dry_run:
        ap.error('give --all or at least one --section (or --dry-run to inspect)')

    plan = [e for e in build_plan() if matches(e, args.section)]
    if not plan:
        sys.exit('nothing selected - check the --section value against the target layout')

    logged = read_log()
    todo, done, missing = [], [], []
    for e in plan:
        src, dest = ROOT / e['source_path'], ROOT / e['dest_path']
        if dest.exists() and not src.exists():
            done.append(e)
        elif src.exists():
            todo.append(e)
        else:
            missing.append(e)

    print(f'{len(plan)} files selected: {len(todo)} to move, {len(done)} already migrated', end='')
    print(f', {len(missing)} MISSING' if missing else '')
    if missing:
        for e in missing[:20]:
            print(f"  missing: {e['source_path']}")
        sys.exit('source files are missing and their destinations do not exist')

    by_dir = collections.Counter(e['dest_path'].rsplit('/', 1)[0] for e in todo)
    for d, n in sorted(by_dir.items()):
        print(f'  {n:5d}  {d}')

    if args.dry_run or not todo:
        if args.dry_run:
            print('\ndry run - nothing moved')
        return

    moved = []
    for e in todo:
        src, dest = ROOT / e['source_path'], ROOT / e['dest_path']
        dest.parent.mkdir(parents=True, exist_ok=True)
        if args.no_git:
            src.rename(dest)
        else:
            subprocess.run(['git', 'mv', '--', str(src), str(dest)], cwd=ROOT, check=True)
        moved.append(e)

    append_log([e for e in moved if e['dest_path'] not in logged])
    print(f'\nmoved {len(moved)} files; provenance in {LOG.relative_to(ROOT)}')

    left = sum(1 for p in (ROOT / 'unsorted-source-material').rglob('*') if p.is_file())
    print(f'{left} files still under unsorted-source-material/')


if __name__ == '__main__':
    main()
