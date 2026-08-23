#!/usr/bin/env python3
"""Phase 6: draft the firmware page from the checksum survey.

  planning/firmware-checksums.csv  ->  docs/reference/firmware.md

The collection holds 28 firmware files and 11 distinct images: the same ROM was
dumped more than once, under different names, and the only way to see that is to
hash them. So the page is built the other way round from the folder - one entry
per *image*, with the files that hold it listed underneath as aliases.

Grouping is by the SHA-256 of the decoded image, not of the file, so an Intel
HEX and a raw binary of the same ROM group together. What each image *is* -
which module, which device, which program number - is not in the checksum CSV
and cannot be inferred from the filenames alone, so it is carried here in
IMAGES, keyed by the Philips 16-bit sum, which is unique across the eleven.

Download links point at the file in the repository on GitHub: the archival
originals are deliberately not published with the site (see `exclude_docs` in
mkdocs.yml), and a firmware image is a file to fetch, not a page to read.

As with the other importers, what comes out is a draft: the tables are final,
the prose around them is not, and the tool will not overwrite a page that has
had its editing pass unless --force says so.

Usage
  tools/import_firmware.py              draft docs/reference/firmware.md
  tools/import_firmware.py --dry-run    print it, write nothing
  tools/import_firmware.py --force      overwrite a hand-edited page
"""
from __future__ import annotations

import argparse
import csv
import pathlib
import sys
import urllib.parse

ROOT = pathlib.Path(__file__).resolve().parent.parent
CHECKSUMS = ROOT / 'planning/firmware-checksums.csv'
MIGRATION_LOG = ROOT / 'planning/migration-log.csv'
PAGE = ROOT / 'docs/reference/firmware.md'
RAW = 'https://github.com/simoninns/vp415-service-guide/raw/main/'

MARKER = '<!-- drafted by tools/import_firmware.py - hand-edited afterwards -->'
STUB_MARKER = 'Not written yet'

# What each image is. Keyed by the Philips 16-bit sum of the decoded image;
# `order` is the reading order on the page, module first, then program number.
IMAGES = {
    '0x68FF': dict(order=1, module='R', module_page='r-drive-processor',
                   device='IC7204 EPROM', name='DRIVE',
                   program='3104 103 6803.6', version='1.7',
                   service_code='4822 209 51257'),
    '0x6728': dict(order=2, module='S', module_page='s-control',
                   device='IC7202 EPROM', name='CONTROL',
                   program='3104 103 6804.9', version='1.8',
                   service_code='4822 209 51256'),
    '0xFC62': dict(order=3, module='S / W', module_page='s-control',
                   module_md='[S](../modules/s-control/index.md) / '
                             '[W](../modules/w-cpu-data-grabber/index.md)',
                   device='8041 slave CPU', name='—',
                   program='not given by the manual', version='—',
                   service_code='—'),
    '0xD120': dict(order=4, module='W', module_page='w-cpu-data-grabber',
                   device='IC7201 EPROM', name='SYNC',
                   program='3104 103 6808.0', version='1.0',
                   service_code='4822 209 51258'),
    '0x1FBE': dict(order=5, module='W', module_page='w-cpu-data-grabber',
                   device='IC7224 EPROM', name='DESCR.',
                   program='3104 103 6807.0', version='1.0',
                   service_code='4822 209 51259'),
    '0xB42D': dict(order=6, module='W', module_page='w-cpu-data-grabber',
                   device='IC7247 EPROM', name='LVDOS#1',
                   program='3104 103 6805.2', version='1.3',
                   service_code='4822 209 51261'),
    '0x8F90': dict(order=7, module='W', module_page='w-cpu-data-grabber',
                   device='IC7247 EPROM', name='LVDOS#1',
                   program='3104 103 6805.3', version='1.4',
                   service_code='4822 209 51261'),
    '0x1A1C': dict(order=8, module='W', module_page='w-cpu-data-grabber',
                   device='IC7248 EPROM', name='LVDOS#2',
                   program='3104 103 6806.2', version='1.3',
                   service_code='4822 209 51262'),
    '0x56D7': dict(order=9, module='W', module_page='w-cpu-data-grabber',
                   device='IC7248 EPROM', name='LVDOS#2',
                   program='3104 103 6806.3', version='1.4',
                   service_code='4822 209 51262'),
    '0xFC6F': dict(order=10, module='VP410 S', module_page='',
                   device='EPROM', name='CONTROL A',
                   program='3104 103 6811.4', version='—',
                   service_code='—'),
    '0xC014': dict(order=11, module='VP410 S', module_page='',
                   device='8041 slave CPU', name='—',
                   program='not given by the manual', version='—',
                   service_code='—'),
}


def read_csv(path: pathlib.Path) -> list[dict]:
    with open(path, newline='') as fh:
        return list(csv.DictReader(fh))


def published() -> dict[str, str]:
    """source path in the checksum CSV -> path in the repository."""
    return {r['source_path']: r['dest_path'] for r in read_csv(MIGRATION_LOG)}


def kib(n: int) -> str:
    return f'{n // 1024} KB' if n >= 1024 and n % 1024 == 0 else f'{n:,} bytes'


def raw_url(dest: str) -> str:
    return RAW + urllib.parse.quote(dest)


def groups() -> list[dict]:
    """One entry per distinct image, in IMAGES order, files attached."""
    dest = published()
    by_image: dict[str, dict] = {}
    for row in read_csv(CHECKSUMS):
        entry = by_image.setdefault(row['sha256_image'], {
            'sha256': row['sha256_image'],
            'sum16': row['sum16'],
            'image_bytes': int(row['image_bytes']),
            'image_range': row['image_range'],
            'files': [],
        })
        entry['files'].append({
            'source': row['path'],
            'name': pathlib.PurePosixPath(row['path']).name,
            'folder': str(pathlib.PurePosixPath(row['path']).parent)
                      .replace('unsorted-source-material/', ''),
            'file_bytes': int(row['file_bytes']),
            'verified': row['checksum_verified'],
            'in_filename': row['checksum_in_filename'],
            'dest': dest.get(row['path'], ''),
        })
    out = []
    for entry in by_image.values():
        meta = IMAGES.get(entry['sum16'])
        if meta is None:
            sys.exit(f'no IMAGES entry for {entry["sum16"]} - add one')
        out.append({**entry, **meta})
    return sorted(out, key=lambda e: e['order'])


def image_table(images: list[dict]) -> str:
    head = ('| # | Module | Device | Name | Program | SW rev. | Size | Philips sum16 '
            '| SHA-256 of the image | Files |\n'
            '| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |')
    rows = []
    for n, img in enumerate(images, 1):
        module = img.get('module_md') or (
            f'[{img["module"]}](../modules/{img["module_page"]}/index.md)'
            if img['module_page'] else img['module'])
        rows.append(
            f'| {n} | {module} | {img["device"]} | {img["name"]} '
            f'| {img["program"]} | {img["version"]} | {kib(img["image_bytes"])} '
            f'| `{img["sum16"]}` | `{img["sha256"][:16]}…` | {len(img["files"])} |')
    return '\n'.join([head] + rows)


def file_table(images: list[dict]) -> str:
    head = ('| Image | File | In the collection as | Size on disk | Checksum in the name |\n'
            '| --- | --- | --- | --- | --- |')
    rows = []
    for n, img in enumerate(images, 1):
        for i, f in enumerate(sorted(img['files'], key=lambda f: f['source'])):
            link = f'[`{f["name"]}`]({raw_url(f["dest"])})' if f['dest'] else f'`{f["name"]}`'
            check = (f'`{f["in_filename"]}` — verified' if f['verified'] == 'match'
                     else '—')
            rows.append(f'| {n if i == 0 else ""} | {link} | `{f["folder"]}` '
                        f'| {f["file_bytes"]:,} bytes | {check} |')
    return '\n'.join([head] + rows)


def front_matter(existing: str) -> tuple[str, str]:
    if not existing.startswith('---\n'):
        return '', existing
    end = existing.find('\n---\n', 4)
    return (existing[:end + 5], existing[end + 5:]) if end > 0 else ('', existing)


def draft() -> str:
    images = groups()
    files = sum(len(i['files']) for i in images)
    verified = sum(1 for i in images for f in i['files'] if f['verified'] == 'match')
    fm, _ = front_matter(PAGE.read_text() if PAGE.exists() else '')
    return '\n'.join([
        fm.rstrip('\n'), '', MARKER, '',
        '# Firmware', '',
        f'**{files} files, {len(images)} distinct images.**', '',
        '## The images', '',
        image_table(images), '',
        '## Every file', '',
        f'{verified} of the {files} files carry a checksum in the filename, and '
        f'every one of them matches the sum computed here.', '',
        file_table(images), '',
    ]).rstrip('\n') + '\n'


def main() -> None:
    ap = argparse.ArgumentParser(description=__doc__,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument('--dry-run', action='store_true')
    ap.add_argument('--force', action='store_true',
                    help='overwrite a page that has had its editing pass')
    args = ap.parse_args()

    text = draft()
    if args.dry_run:
        print(text)
        return
    if PAGE.exists() and not args.force:
        current = PAGE.read_text()
        if MARKER not in current and STUB_MARKER not in current:
            sys.exit(f'{PAGE.relative_to(ROOT)} has been hand-edited; '
                     f'--force to overwrite it')
    PAGE.write_text(text)
    print(f'wrote {PAGE.relative_to(ROOT)}')


if __name__ == '__main__':
    main()
