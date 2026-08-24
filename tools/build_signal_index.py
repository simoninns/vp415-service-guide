#!/usr/bin/env python3
"""Phase 7: fill in the *Modules* column of the alphabetical signal listing.

  docs/modules/*/index.md                 -.
  docs/circuit-description/modules/*.md    -> docs/system/signal-listing.md

The manual's signal listing (CS 7 830) gives 243 mnemonics, their meanings and
their active levels, and nothing else - it never says which board a signal comes
from or goes to. The wiring diagrams do say, but they are fold-out scans: there
is no machine-readable interconnection list anywhere in the source material.

So the column is built the only way the material allows: **a signal is credited
to a module when that module's page, or that module's page in the chapter 7
circuit description, mentions the mnemonic**. That is an index of where the
signal is *described*, not a netlist, and the page says so. Where a module page
states the direction itself - the `Out` / `Outputs to` row of its summary table
- the module is marked as the source with a bullet, so a reader can see at a
glance which end of the wire to start from.

Matching is normalised by dropping everything but letters, digits, `/` and `+`,
so `HF-OUT 1` on the listing finds `HF-OUT1` in the prose and `COMM1` finds
`COMM-1`. On the module pages, which are this site's own prose and code-quote
every mnemonic, only backticked text is matched. Chapter 7 is a transcription of
the manual, which prints signal names as bare capitals in running text, so there
bare all-caps tokens of three characters or more are matched as well. Two lists
keep that honest:

  AMBIGUOUS  mnemonics that are also something else in running text and would
             produce false hits - `CS` is a Philips sheet code, `Q1` is a
             connector on module Q, `B` is a typewriter B in a checksum note.
             Never matched; their column is left empty.
  ALIASES    spellings the pages use that normalisation alone does not reach.

Usage
  tools/build_signal_index.py            rewrite the column in place
  tools/build_signal_index.py --check    exit 1 if the page is out of date
  tools/build_signal_index.py --report   what matched what, to stdout
"""
from __future__ import annotations

import argparse
import collections
import pathlib
import re
import sys

ROOT = pathlib.Path(__file__).resolve().parent.parent
PAGE = ROOT / 'docs/system/signal-listing.md'
MODULES = ROOT / 'docs/modules'
CHAPTER7 = ROOT / 'docs/circuit-description/modules'

# Mnemonics that mean something else in running text more often than they mean
# the signal. Checked by hand against every hit they produced; see the phase 7
# findings for the contexts.
AMBIGUOUS = {
    'B', 'G', 'R',          # single letters: video signals, but also prose
    'CS',                   # 'no CS code printed' - the Philips sheet code
    'Q1', 'Q2', 'Q3', 'Q4', # module Q's connectors, module Y's decoder outputs
    'Q1,2', 'Q3,4',
}

# Spellings the pages use that normalisation does not reach on its own.
ALIASES = {
    'HF-AUD': ['HFAUD'],
    'CS 1-8': ['CS1', 'CS2', 'CS3', 'CS4', 'CS5', 'CS6', 'CS7', 'CS8'],
    'SD 0-7': ['SD0', 'SD1', 'SD2', 'SD3', 'SD4', 'SD5', 'SD6', 'SD7'],
    'CP-1': ['CP1'], 'CP-2': ['CP2'],
    'HF-OUT 1': ['HF-OUT1'], 'HF-OUT 2': ['HF-OUT2'],
    'RC5 IN(B)': ['RC5-IN(B)'],
    'DTR 1': ['DTR1'], 'DTR 2': ['DTR2'], 'DTR 3': ['DTR3'],
}

# Module directory -> the label used in the column. The remote control is not a
# lettered module, so it gets its own.
def label(slug: str) -> str:
    return 'RC' if slug == 'remote-control' else slug[0].upper()


def loose(name: str) -> str:
    return re.sub(r'[^A-Z0-9/+]', '', name.upper())


def read_signals(text: str) -> list[str]:
    """The first column of the listing's table, in the manual's own order."""
    out = []
    for line in text.splitlines():
        m = re.match(r'^\| `([^`]+)` \|', line)
        if m:
            out.append(m.group(1))
    return out


def lookup(signals: list[str]) -> dict[str, list[str]]:
    """Normalised mnemonic -> the signals it stands for."""
    lut = collections.defaultdict(list)
    for sig in signals:
        if sig in AMBIGUOUS:
            continue
        for spelling in [sig] + ALIASES.get(sig, []):
            lut[loose(spelling)].append(sig)
    return lut


# A bare mnemonic in the chapter 7 transcription: capitals, digits, hyphens and
# slashes, not already inside a code span or a longer word.
BARE = re.compile(r'(?<![`\w-])([A-Z][A-Z0-9]{2,}(?:[-/][A-Z0-9]+)*)(?![\w-])')


def scan(text: str, module: str, lut, hits, sources, *, out_rows=False,
         bare=False) -> None:
    """Credit every mnemonic in `text` to `module`."""
    for m in re.finditer(r'`([^`\n]{1,14})`', text):
        for sig in lut.get(loose(m.group(1)), []):
            hits[sig].add(module)
    if bare:
        for m in BARE.finditer(text):
            for sig in lut.get(loose(m.group(1)), []):
                hits[sig].add(module)
    if not out_rows:
        return
    # `| Out |` and `| Outputs to |` rows of the summary table state direction.
    for row in re.finditer(r'^\| Out(?:puts to)? \| (.*) \|$', text, re.M):
        for m in re.finditer(r'`([^`\n]{1,14})`', row.group(1)):
            for sig in lut.get(loose(m.group(1)), []):
                sources[sig].add(module)


def collect(signals: list[str]):
    lut = lookup(signals)
    hits: dict[str, set] = collections.defaultdict(set)
    sources: dict[str, set] = collections.defaultdict(set)

    slugs = sorted(p.name for p in MODULES.iterdir() if p.is_dir()
                   and (p / 'index.md').exists())
    for slug in slugs:
        scan((MODULES / slug / 'index.md').read_text(), slug, lut, hits,
             sources, out_rows=True)

    # Chapter 7 is a page per module, named for the same slug as the module
    # page it pairs with: `docs/circuit-description/modules/h-etbc-b.md`. Its
    # own index page describes no circuit, so it is skipped, and modules Q, V
    # and the remote control have no page there at all. Module U's page carries
    # Ua, Ub and Uc; all three are the one board.
    known = set(slugs)
    for page in sorted(CHAPTER7.glob('*.md')):
        if page.stem == 'index' or page.stem not in known:
            continue
        # The front matter is this site's own summary, not the manual's text.
        body = re.sub(r'\A---\n.*?\n---\n', '', page.read_text(), flags=re.S)
        scan(body, page.stem, lut, hits, sources, bare=True)
    return hits, sources


def column(sig: str, hits, sources) -> str:
    mods = sorted(hits.get(sig, ()), key=lambda s: (s == 'remote-control', s))
    cells = []
    for slug in mods:
        link = f'[{label(slug)}](../modules/{slug}/index.md)'
        cells.append(f'**{link}**' if slug in sources.get(sig, ()) else link)
    return ' '.join(cells)


def rewrite(text: str, hits, sources) -> str:
    signals = read_signals(text)
    credited = sum(1 for s in signals if hits.get(s))
    # The page states the coverage; keep it true.
    text = re.sub(r'\*\*\d+ of the \d+\*\* mnemonics are credited',
                  f'**{credited} of the {len(signals)}** mnemonics are credited',
                  text)
    out = []
    for line in text.splitlines(keepends=True):
        m = re.match(r'^\| `([^`]+)` \| (.*?) \| (.*?) \|(?: .*\|)? *$', line)
        if m:
            sig, meaning, level = m.group(1), m.group(2), m.group(3)
            out.append(f'| `{sig}` | {meaning} | {level} | '
                       f'{column(sig, hits, sources)} |\n')
            continue
        if re.match(r'^\| Signal \| Meaning \| Active / level \|', line):
            out.append('| Signal | Meaning | Active / level | Modules |\n')
            continue
        if re.match(r'^\| --- \| --- \| --- \|', line):
            out.append('| --- | --- | --- | --- |\n')
            continue
        out.append(line)
    return ''.join(out)


def main() -> None:
    ap = argparse.ArgumentParser(description=__doc__,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument('--check', action='store_true',
                    help='exit 1 if the page is not what this tool would write')
    ap.add_argument('--report', action='store_true',
                    help='print the index instead of writing it')
    args = ap.parse_args()

    text = PAGE.read_text()
    signals = read_signals(text)
    hits, sources = collect(signals)
    new = rewrite(text, hits, sources)

    if args.report:
        for sig in signals:
            mods = ' '.join(sorted(label(s) for s in hits.get(sig, ())))
            src = ' '.join(sorted(label(s) for s in sources.get(sig, ())))
            print(f'{sig:<12} {mods:<28} {"source: " + src if src else ""}')
        credited = sum(1 for s in signals if hits.get(s))
        print(f'\n{credited} of {len(signals)} signals credited to a module; '
              f'{len(AMBIGUOUS)} mnemonics excluded as ambiguous', file=sys.stderr)
        return

    if args.check:
        if new != text:
            sys.exit(f'{PAGE.relative_to(ROOT)} is out of date - '
                     f'run tools/build_signal_index.py')
        print(f'{PAGE.relative_to(ROOT)} is up to date')
        return

    PAGE.write_text(new)
    credited = sum(1 for s in signals if hits.get(s))
    print(f'{PAGE.relative_to(ROOT)}: {credited} of {len(signals)} signals '
          f'credited to a module')


if __name__ == '__main__':
    main()
