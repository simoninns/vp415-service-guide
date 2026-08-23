# Phase 3 — Site skeleton: verification record

What was built, what was measured, and the one finding that changed the plan.

---

## 1. What landed

| File | What |
| --- | --- |
| `mkdocs.yml` | Material theme, explicit `nav:` over all 86 pages, plugins, `pymdownx` set, `validation:` rules |
| `docs/index.md` | The landing page, written in full |
| 85 stub pages | Front-matter title and description, H1, and a placeholder naming their sources |
| `docs/stylesheets/extra.css` | Figure and caption treatment for scanned Philips sheets |
| `justfile` | `check` / `check-external` rewritten to link-check under the Pages base path |
| `.github/workflows/deploy.yml` | `push` trigger enabled, per Phase 0's note |

## 2. Page inventory — 86 pages

| Section | Pages |
| --- | --- |
| Landing page | 1 |
| Overview (ch. 1) | 4 |
| General service (ch. 2) | 10 |
| System (ch. 3) | 5 |
| Modules (ch. 4) | 27 — index plus 26 modules |
| Parts (ch. 5) | 4 |
| Repair (ch. 6) | 7 — including 3 case-study pages |
| Circuit description (ch. 7) | 5 |
| Service information (ch. 8) | 4 |
| Operating instructions | 12 |
| Reference | 7 — including 3 calibration pages |

The plan's estimate was "~120 markdown files"; the layout it specifies comes to 86. The difference
is that the plan counted the section directories, not their contents.

`docs/modules/q-rc5-receiver/` was created in this phase. Phase 2 never made it, because module Q
owns no originals of its own — its RC5 circuit is panel 1 of `CS 7 851`, which is filed under
module R. The page exists and cross-references R in both directions.

## 3. Stub source citations are generated, not typed

Each stub's placeholder admonition names the manual pages and Philips `CS` sheets its content will
come from. Those lists were built by reading `service-manual-sheet-map.csv` and mapping each row
to a page, rather than by transcribing the plan's tables — so a stub cannot cite a page the
Phase 1 attribution does not support.

The mapping is one-to-one by `(chapter, section)` except in two places:

- **Chapter 6 maps by sheet.** The sheet map groups pages 107–111 as one `repair-method` section,
  but they are four different things: 107 is the chapter's title page and contents, 108–110 are
  the diagnostic software, and **111 is the error code table**. Splitting on the section column
  would have put the error codes on the wrong page. Checked against each sheet's own title.
- **Chapter 7 and chapter 8 rows cite twice.** A per-module row — say the module J circuit
  description on page 148, or its mod-level table on page 176 — is cited both on the chapter page
  that owns it and on `modules/j-focus/index.md`, because Phase 5 pulls it onto the module page.

Every row in the sheet map resolves to a page: the generator exits on an unmapped row, and it ran
clean over all 273 rows.

## 4. The module stubs carry their notes forward

The 26 module stubs each carry the intended section order for the finished page, and the
module-specific notes this plan records, so Phase 5 cannot lose them:

- **J** — the 6210/6211 BCE-vs-ECB pinout erratum
- **S** and **W** — the 8041 firmware ambiguity, stated as an open question rather than a fact
- **N** / **P** and **Q** / **R** — the two sheets that cover two modules each, cross-referenced
  in both directions
- **B** and **Z** — links to their calibration guides
- **U** — the Ua / Ub / Uc division
- **W** — that `CS 8 122` supersedes `CS 7 858`, and that page 089's OCR contains a hallucinated
  parts run

## 5. Finding: the site as planned exceeded the GitHub Pages 1 GB limit

The plan published the archival originals as a "download the full sheet" link on every figure.
Measured on the first strict build:

| Part of the site | Size |
| --- | --- |
| `assets/originals/` | 918.2 MB |
| `assets/web/` derivatives | 197.9 MB |
| HTML | 3.5 MB |
| Everything else | 2.7 MB |
| **Total** | **1122.2 MB** |

**GitHub Pages will not publish a site larger than 1 GB** (1073.7 MB), so the site was already
over before phases 4–6 add anything. Excluding the originals takes it to **197 MB**.

What a reader actually loses is small, because the derivatives are not thumbnails:

| Zoom derivative | Count | Resolution |
| --- | --- | --- |
| Schematics, photographs, module photographs, scope traces | 240 | the scan's native resolution |
| Text and table pages | 117 | 2000 px wide, against a 2482 px original |

So every circuit diagram, PCB lay-out, fold-out and photograph on the site already opens at the
resolution it was captured at. Only the 117 text pages are downscaled, and only to 81 % of
original width; the loss beyond that is lossless WebP versus q82.

**Owner's decision: publish neither the originals nor a link to them.** `mkdocs.yml` excludes
`docs/**/assets/originals/` via `exclude_docs`, the figure pattern in `extra.css` carries no
download link, and the landing page says plainly that the lossless originals live in the
repository rather than on the site. The originals remain the single committed copy of every scan —
the one-copy rule is untouched; only what gets *published* changed.

## 6. Finding: `lychee` cannot resolve the site's links without a root

`site_url` is set, so mkdocs writes root-relative links — `/vp415-service-guide/modules/j-focus/`.
Run against `site/` directly, `lychee` flagged **103 of them as errors**: it resolves a
root-relative link against a root directory, and no such directory was given.

`--root-dir` needs a directory in which `/vp415-service-guide/` exists, which `site/` is not.
The fix in the `justfile` is a symlink in a temporary directory, so the build output does not have
to move:

```
root=$(mktemp -d)
ln -s "$PWD/site" "$root/vp415-service-guide"
lychee --offline --include-fragments --root-dir "$root" "$root/vp415-service-guide"
```

This was a latent trap rather than a broken link: every link in the site was in fact correct.

## 7. Verification

| Check | Result |
| --- | --- |
| `mkdocs build --strict` | passes, no warnings, 2.0 s |
| `just check` (strict build + offline link check) | **0 errors**, 9595 links OK, 397 unique |
| `mkdocs serve` | every page renders; home, a module page, a case study, a calibration page and `search_index.json` all return 200 |
| Rendered site size | 197 MB |
| Originals in the build output | none — `site/**/assets/` contains `web/` only |
| Visual check | home page and module J screenshotted: tabs, palette toggle, grid cards, admonitions, module sidebar, prev/next footer and the edit link all render |

`--strict` is meaningful here rather than nominal: `validation:` is configured so an omitted file,
an absolute link, an unrecognised link or a dead anchor each fail the build.

## 8. Note on the toolchain

`mkdocs-material` 9.7.6 prints a banner on every build about backward-incompatible changes coming
in MkDocs 2.0 — that all plugins and theme overrides will break, with no migration path. It is
informational, not an error, and this site is pinned through the flake, so nothing moves until the
pin does. Worth knowing before anyone upgrades nixpkgs.
