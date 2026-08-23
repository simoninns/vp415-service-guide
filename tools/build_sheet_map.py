#!/usr/bin/env python3
"""Phase 1 task 2/decision: re-key the manual index by panel rather than by capture.

The old map had one row per scanned page. That worked while the 34 two-panel trifold
captures existed, but a captured page is an artefact of the scanner, not of the document:
it could hold two thirds of one drawing, or the tail of one module's sheet and the head of
another's. With the captures now deleted, page rows index nothing physical.

A *panel* is the real unit: the A4-sized face the sheet folds into.

  A4 sheet      1 panel
  bifold sheet  2 panels   (4964 px = 2 x 2482)
  trifold sheet 3 panels   (published from the stitched composite)

Each panel row names the module that panel belongs to, so a sheet covering two modules is
expressible - which the old single-valued `module` column was not.

Panel -> capture correspondence for trifolds: the left capture held panels 1 and 2, the
right capture panels 2 and 3 (they overlapped in the middle). So panels 1 and 2 inherit the
left page's attribution and panel 3 the right page's, with explicit overrides below.
"""
import csv, pathlib, collections

ROOT = pathlib.Path(__file__).resolve().parent.parent
# One-time migration. The page-keyed source map was retired once this ran; recover it with
#   git show e3241b3:planning/service-manual-page-map.csv
SRC = ROOT/'planning/service-manual-page-map.csv'
OUT = ROOT/'planning/service-manual-sheet-map.csv'

PANELS = {'A4': 1, 'bifold': 2, 'trifold': 3}

# Corrections and per-panel overrides established by direct reading of the sheets.
# See planning/phase-1-findings.md.
PAGE_MODULE_FIX = {
    # page: (new module, why)
    '052': ('J', 'title block reads FOCUS MODULE (mod level 2), boxed J; locator table '
                 'lists 6210/6211, the module-J focus transistors'),
    '039': ('D', 'sheet CS 6 870 is one schematic across all three panels, titled '
                 'REF. SOURCE MODULE (mod level 2), boxed D - no module C content'),
}
PANEL_MODULE = {
    # (sheet, panel): module - only where a sheet's panels differ
    ('039_040', 1): 'D', ('039_040', 2): 'D', ('039_040', 3): 'D',
    ('061_062', 1): 'N', ('061_062', 2): 'N', ('061_062', 3): 'P',
    ('063_064', 1): 'Q', ('063_064', 2): 'R', ('063_064', 3): 'R',
}
PANEL_CONTENT = {
    ('063_064', 1): 'circuit',      # RC5 circuit + RC5 mirror, module Q
    ('063_064', 2): 'parts',        # list of electrical parts, module R
    ('063_064', 3): 'pcb-layout',   # drive processor lay-out, module R
    ('061_062', 3): 'module-sheet', # frontloader circuit + lay-out + parts, module P
}

def main():
    rows = list(csv.DictReader(open(SRC)))
    for r in rows:                                   # apply the page-level corrections
        if r['page'] in PAGE_MODULE_FIX:
            r['module'] = PAGE_MODULE_FIX[r['page']][0]

    bysheet = collections.OrderedDict()
    for r in rows:
        bysheet.setdefault(r['sheet'], []).append(r)

    out = []
    for sheet, rs in bysheet.items():
        fold = rs[0]['fold']
        n = PANELS[fold]
        for panel in range(1, n + 1):
            # trifold panels 1,2 come from the left capture, panel 3 from the right
            src = rs[0] if (n < 3 or panel < 3) else rs[-1]
            module = PANEL_MODULE.get((sheet, panel), src['module'])
            content = PANEL_CONTENT.get((sheet, panel), src['content_type'])
            pages = [x['page'] for x in rs]
            out.append({
                'sheet': sheet,
                'panel': panel,
                'panels': n,
                'fold': fold,
                'chapter': src['chapter'],
                'section': src['section'],
                'module': module,
                'content_type': content,
                'cs_code': src['cs_code'],
                'title': src['title'],
                'scan_pages': '+'.join(pages),
                'ocr_path': src['ocr_path'],
                'publish_source': src['publish_source'],
            })

    with open(OUT, 'w', newline='') as fh:
        w = csv.DictWriter(fh, fieldnames=list(out[0].keys()))
        w.writeheader()
        w.writerows(out)

    c = collections.Counter(r['fold'] for r in out)
    print(f'{len(bysheet)} sheets -> {len(out)} panel rows  ({OUT.relative_to(ROOT)})')
    for k in ('A4', 'bifold', 'trifold'):
        print(f'  {k:<8} {c[k]:4d} panels')
    print(f'\ndistinct publish_source: {len({r["publish_source"] for r in out})}')
    print(f'distinct ocr_path:       {len({r["ocr_path"] for r in out})}')
    multi = [s for s, rs in collections.Counter(
        (r['sheet'], r['module']) for r in out).items()]
    bysheet_mod = collections.defaultdict(set)
    for r in out:
        if r['module'].strip():
            bysheet_mod[r['sheet']].add(r['module'])
    two = {s: sorted(m) for s, m in bysheet_mod.items() if len(m) > 1}
    print(f'sheets covering more than one module: {two or "none"}')

if __name__ == '__main__':
    main()
