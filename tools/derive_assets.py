#!/usr/bin/env python3
"""Phase 2b: build the web derivatives from the archival originals.

  docs/**/assets/originals/  ->  docs/**/assets/web/   (gitignored)

For each original an inline `-preview.webp` and a lightbox `-zoom.webp` are
written beside each other in the sibling web/ directory, sized by the profile
the file carries in planning/migration-log.csv:

  profile       preview          zoom
  text-page     1400px q82       2000px q82
  text-spread   1400px q82       2000px q82   (rotated upright and split in two)
  schematic     1600px q80       native q80
  module-photo  1400px q82       native q82
  photo         1400px q82       native q82
  scope-trace   1400px q82       native q82
  none          -                -            (firmware, PDFs, office documents)

The operating-instructions photographs are sideways two-page sheets, so
`text-spread` rotates each one upright and cuts it down the gutter, writing
`-a-` for the left page and `-b-` for the right. Which printed page each half
holds is not the derivation's business: the page numbering was resolved when the
operating-instructions pages were written, and lives in those pages.

Nothing is ever upscaled: a target wider than the source yields the source size.
Every save strips metadata, so no EXIF reaches the published site.

Each web/ directory carries a .manifest.json recording the source SHA-256, the
profile and the size and dimensions of each output. A re-run hashes the sources
and skips any whose hash and outputs are unchanged, so `just derive` after a
first run costs seconds.

Usage
  tools/derive_assets.py                 derive everything that is out of date
  tools/derive_assets.py --force         re-derive regardless of the manifest
  tools/derive_assets.py --jobs 4        limit concurrency (default: all cores)
  tools/derive_assets.py --dry-run       report what would be built
  tools/derive_assets.py docs/modules    restrict to a subtree
"""
from __future__ import annotations

import argparse
import concurrent.futures
import csv
import hashlib
import json
import os
import pathlib
import subprocess
import sys
import tempfile

ROOT = pathlib.Path(__file__).resolve().parent.parent
LOG = ROOT / 'planning/migration-log.csv'
MANIFEST = '.manifest.json'
MANIFEST_VERSION = 1

# The plan's derivative sizing table. `None` means native resolution.
PROFILES = {
    'text-page':    {'preview': (1400, 82), 'zoom': (2000, 82)},
    'text-spread':  {'preview': (1400, 82), 'zoom': (2000, 82)},
    'schematic':    {'preview': (1600, 80), 'zoom': (None, 80)},
    'module-photo': {'preview': (1400, 82), 'zoom': (None, 82)},
    'photo':        {'preview': (1400, 82), 'zoom': (None, 82)},
    'scope-trace':  {'preview': (1400, 82), 'zoom': (None, 82)},
    'none':         {},
}

IMAGE_SUFFIXES = {'.webp', '.png', '.jpg', '.jpeg', '.tif', '.tiff'}

# Profiles whose source is one photograph of two pages lying side by side,
# shot sideways: rotate 90 degrees clockwise, then cut down the middle.
SPLIT_PROFILES = {'text-spread'}

# Cap on the total size of docs/**/assets/web/, from the phase 2 exit criteria.
SIZE_BUDGET_MB = 350


def sha256(path: pathlib.Path) -> str:
    h = hashlib.sha256()
    with open(path, 'rb') as fh:
        for chunk in iter(lambda: fh.read(1 << 20), b''):
            h.update(chunk)
    return h.hexdigest()


def load_profiles() -> dict[str, str]:
    """dest path under docs/ -> derivative profile, from the migration log."""
    if not LOG.exists():
        return {}
    return {r['dest_path']: r['profile'] for r in csv.DictReader(open(LOG))}


def profile_for(rel: str, profiles: dict[str, str]) -> str:
    """The migration log is authoritative; anything else falls back on its suffix."""
    named = profiles.get(rel)
    if named:
        return named
    return 'photo' if pathlib.Path(rel).suffix.lower() in IMAGE_SUFFIXES else 'none'


def header(path: pathlib.Path) -> tuple[int, int]:
    out = subprocess.run(['vipsheader', '-f', 'width', str(path)],
                         capture_output=True, text=True, check=True).stdout
    w = int(out.strip())
    out = subprocess.run(['vipsheader', '-f', 'height', str(path)],
                         capture_output=True, text=True, check=True).stdout
    return w, int(out.strip())


def encode(src: pathlib.Path, dest: pathlib.Path, width: int | None, quality: int,
           src_width: int) -> dict:
    """Write one WebP derivative. `width` None, or wider than the source, means native."""
    spec = f'{dest}[Q={quality},strip]'
    if width is None or width >= src_width:
        subprocess.run(['vips', 'copy', str(src), spec], check=True,
                       capture_output=True)
    else:
        # --height is a bound, not a target: constrain the width only, so a
        # landscape fold-out and a portrait text page both come out `width` wide.
        subprocess.run(['vips', 'thumbnail', str(src), spec, str(width),
                        '--height', '1000000'], check=True, capture_output=True)
    w, h = header(dest)
    return {'bytes': dest.stat().st_size, 'width': w, 'height': h}


def halves(src: pathlib.Path, tmp: pathlib.Path) -> list[tuple[str, pathlib.Path]]:
    """Rotate a sideways two-page sheet upright and cut it down the gutter."""
    upright = tmp / 'upright.v'
    subprocess.run(['vips', 'rot', str(src), str(upright), 'd90'], check=True,
                   capture_output=True)
    w, h = header(upright)
    cuts = [('a', 0, w // 2), ('b', w // 2, w - w // 2)]
    out = []
    for side, left, width in cuts:
        page = tmp / f'{side}.v'
        subprocess.run(['vips', 'crop', str(upright), str(page),
                        str(left), '0', str(width), str(h)], check=True,
                       capture_output=True)
        out.append((side, page))
    return out


def derive_one(src: pathlib.Path, web: pathlib.Path, prof: str) -> dict:
    src_w, src_h = header(src)
    entry = {'source_sha256': sha256(src), 'source_bytes': src.stat().st_size,
             'source_width': src_w, 'source_height': src_h,
             'profile': prof, 'outputs': {}}
    if prof in SPLIT_PROFILES:
        with tempfile.TemporaryDirectory() as td:
            for side, page in halves(src, pathlib.Path(td)):
                page_w, _ = header(page)
                for kind, (width, quality) in PROFILES[prof].items():
                    dest = web / f'{src.stem}-{side}-{kind}.webp'
                    entry['outputs'][dest.name] = encode(page, dest, width,
                                                         quality, page_w)
        return entry
    for kind, (width, quality) in PROFILES[prof].items():
        dest = web / f'{src.stem}-{kind}.webp'
        entry['outputs'][dest.name] = encode(src, dest, width, quality, src_w)
    return entry


def up_to_date(entry: dict | None, src: pathlib.Path, web: pathlib.Path,
               prof: str, digest: str) -> bool:
    if not entry or entry.get('profile') != prof or entry.get('source_sha256') != digest:
        return False
    for name, rec in entry.get('outputs', {}).items():
        out = web / name
        if not out.exists() or out.stat().st_size != rec['bytes']:
            return False
    return True


# Sources for pages that are deferred: the originals stay in the repository,
# but nothing references them, and mkdocs excludes the directory, so deriving
# them would only cost disk. See "deferred out of phase 6" in the plan.
DEFERRED = ('docs/reference/calibration',)


def originals_dirs(roots: list[pathlib.Path]) -> list[pathlib.Path]:
    seen: set[pathlib.Path] = set()
    for root in roots:
        if not root.exists():
            continue
        for d in root.rglob('originals'):
            if d.is_dir() and d.parent.name == 'assets' \
                    and not d.as_posix().startswith(
                        tuple(f'{ROOT.as_posix()}/{p}/' for p in DEFERRED)):
                seen.add(d)
    return sorted(seen)


def main() -> None:
    ap = argparse.ArgumentParser(description=__doc__,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument('paths', nargs='*', default=None, metavar='PATH',
                    help='subtrees to derive (default: docs/)')
    ap.add_argument('--force', action='store_true', help='ignore the manifest, rebuild all')
    ap.add_argument('--jobs', type=int, default=os.cpu_count() or 4)
    ap.add_argument('--dry-run', action='store_true', help='report what is out of date')
    args = ap.parse_args()

    roots = [ROOT / p for p in args.paths] if args.paths else [ROOT / 'docs']
    profiles = load_profiles()
    dirs = originals_dirs(roots)
    if not dirs:
        print('no docs/**/assets/originals/ directories yet')
        return

    jobs, skipped, no_profile = [], 0, 0
    manifests: dict[pathlib.Path, dict] = {}

    for originals in dirs:
        web = originals.parent / 'web'
        mf_path = web / MANIFEST
        old = {}
        if mf_path.exists() and not args.force:
            try:
                loaded = json.loads(mf_path.read_text())
                if loaded.get('version') == MANIFEST_VERSION:
                    old = loaded.get('entries', {})
            except json.JSONDecodeError:
                pass
        entries: dict[str, dict] = {}
        # Outputs are named from the source stem, so two originals in one
        # directory sharing a stem would silently overwrite each other.
        claimed: dict[str, pathlib.Path] = {}
        for src in sorted(p for p in originals.rglob('*') if p.is_file()):
            rel = str(src.relative_to(ROOT))
            prof = profile_for(rel, profiles)
            if prof == 'none':
                continue
            if src.suffix.lower() not in IMAGE_SUFFIXES:
                no_profile += 1
                continue
            if src.stem in claimed:
                sys.exit(f'derivative name collision in {originals.relative_to(ROOT)}:\n'
                         f'  {claimed[src.stem].name} and {src.name} both derive to '
                         f'{src.stem}-preview.webp\n'
                         '  rename one of them so the derivative stems differ')
            claimed[src.stem] = src
            digest = sha256(src)
            prior = old.get(src.name)
            if up_to_date(prior, src, web, prof, digest):
                entries[src.name] = prior
                skipped += 1
                continue
            jobs.append((src, web, prof))
        manifests[web] = entries

    print(f'{len(dirs)} asset directories: {len(jobs)} to derive, {skipped} up to date'
          + (f', {no_profile} non-image skipped' if no_profile else ''))
    if args.dry_run:
        for src, _, prof in jobs[:40]:
            print(f'  {prof:12s} {src.relative_to(ROOT)}')
        if len(jobs) > 40:
            print(f'  ... and {len(jobs) - 40} more')
        return

    for web in manifests:
        web.mkdir(parents=True, exist_ok=True)

    failures = []
    if jobs:
        with concurrent.futures.ThreadPoolExecutor(max_workers=args.jobs) as pool:
            futures = {pool.submit(derive_one, s, w, p): (s, w) for s, w, p in jobs}
            for i, fut in enumerate(concurrent.futures.as_completed(futures), 1):
                src, web = futures[fut]
                try:
                    manifests[web][src.name] = fut.result()
                except subprocess.CalledProcessError as exc:
                    failures.append((src, exc.stderr.decode(errors='replace').strip()))
                if i % 25 == 0 or i == len(jobs):
                    print(f'  {i}/{len(jobs)}', end='\r', flush=True)
        print()

    total = 0
    for web, entries in manifests.items():
        keep = {name for e in entries.values() for name in e['outputs']} | {MANIFEST}
        for stale in web.iterdir():
            if stale.is_file() and stale.name not in keep:
                stale.unlink()
        web.joinpath(MANIFEST).write_text(
            json.dumps({'version': MANIFEST_VERSION, 'entries': entries},
                       indent=1, sort_keys=True) + '\n')
        total += sum(o['bytes'] for e in entries.values() for o in e['outputs'].values())

    files = sum(len(e['outputs']) for entries in manifests.values() for e in entries.values())
    mb = total / 1024 / 1024
    print(f'{files} derivatives, {mb:.0f} MB in docs/**/assets/web/'
          f' (budget {SIZE_BUDGET_MB} MB)')

    if failures:
        print(f'\n{len(failures)} FAILED:')
        for src, err in failures[:10]:
            print(f'  {src.relative_to(ROOT)}: {err.splitlines()[-1] if err else "?"}')
        sys.exit(1)
    if mb > SIZE_BUDGET_MB:
        sys.exit(f'over the {SIZE_BUDGET_MB} MB budget')


if __name__ == '__main__':
    main()
