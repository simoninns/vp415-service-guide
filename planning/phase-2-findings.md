# Phase 2 — migration and asset pipeline: verification record

Companion to [implementation-plan.md](implementation-plan.md) § Phase 2. Everything the plan
asked for landed; this records what was built, how it was verified, and the four things the
work turned up that the plan did not anticipate.

---

## 1. What landed

| | |
| --- | --- |
| `tools/migrate.py` | `git mv` from `unsorted-source-material/` into `docs/**/assets/originals/` |
| `tools/derive_assets.py` | `docs/**/assets/originals/` → `docs/**/assets/web/` (gitignored) |
| `planning/migration-log.csv` | 400 rows: original path → new path, with profile and provenance |
| `justfile` | gained `just migrate` alongside the existing `just derive` |

**400 files migrated** — 180 canonical service-manual sheets driven by
[service-manual-sheet-map.csv](service-manual-sheet-map.csv), and 220 photographs, scope traces,
firmware images and documents driven by [../tools/asset_map.csv](../tools/asset_map.csv).

`unsorted-source-material/` went from **1041 MB / 1155 files to 32 MB / 755 files**. What is left
is exactly what the plan said would be left: 492 vendor-OCR files that `tools/import_ocr.py`
consumes in phase 4, and 263 files the asset map marks `exclude`. Four directories remain —
`ocr-markdown-service-manual/`, `pdfs/`, `VP415 ROM dumps/` and `Microcontroller dumps/`. Empty
directories left behind by `git mv` were removed.

## 2. Naming

Manual sheets are named for their Philips sheet code, their content and their scan page, so a
file name alone says what the file is and where in the manual it came from:

```
docs/modules/j-focus/assets/originals/cs-7-846-module-sheet-p053.webp
docs/system/assets/originals/cs-7-831-figure-p021-022.webp     # a trifold, pages 21-22
docs/overview/assets/originals/divider-p003.webp               # the 17 sheets with no code
```

Sheets route by manual chapter, except chapter 4, which routes by module letter to
`docs/modules/<slug>/`. **A sheet is one piece of paper and therefore one file**, so the two
sheets whose panels span two modules are filed under the module holding the most panels and
cross-referenced from the other — the rule carried forward from phase 1:

| Sheet | Panels | Filed under | Also referenced from |
| --- | --- | --- | --- |
| `CS 7 850` (061_062) | 1–2 module N, 3 module P | `modules/n-display-keyboard/` | module P |
| `CS 7 851` (063_064) | 1 module Q, 2–3 module R | `modules/r-drive-processor/` | module Q |

Both are noted in `migration-log.csv`, in the `notes` column, as `[panels span modules …]`.
Module Q therefore owns no originals of its own — correct, not an omission.

## 3. Derivative profiles

`migrate.py` assigns each sheet a profile from its `content_type`, with one override: **a fold-out
is always `schematic`**, whatever it carries. A bifold table is half-size on the page relative to
an A4 one and needs native resolution just as much as a bifold schematic does.

Measured output, all 714 derivatives:

| Profile | n | preview total | zoom total | median zoom | largest zoom |
| --- | --- | --- | --- | --- | --- |
| `schematic` | 100 | 12.9 MB | 84.0 MB | 708 KB | 4.0 MB (7766 px trifold) |
| `text-page` | 117 | 19.7 MB | 32.1 MB | 250 KB | 774 KB |
| `photo` | 50 | 4.0 MB | 13.5 MB | 255 KB | 617 KB |
| `module-photo` | 43 | 5.3 MB | 23.3 MB | 489 KB | 1.0 MB |
| `scope-trace` | 47 | 1.5 MB | 1.6 MB | 32 KB | 148 KB |

43 originals produce no derivative and are meant not to — firmware images, PDFs and the `.pptx` /
`.xlsx` / `.docx` editable sources.

## 4. Done-when, verified

| Criterion | Result |
| --- | --- |
| `just derive` from clean completes | **44 s** on 16 cores, 714 files; a warm re-run is **1.9 s** |
| `docs/**/assets/web/` under 350 MB | **189 MB** — 54 % of budget |
| the manifest accounts for every emitted file | 714 emitted, 714 claimed, 0 unclaimed, 0 claimed-but-absent; every recorded byte count matches the file on disk |
| `git status` shows no untracked originals | clean — all 400 are staged renames, and `git check-ignore` confirms `.gitignore:5` catches `docs/assets/web/`, `docs/modules/*/assets/web/` and `docs/reference/calibration/assets/web/` alike |

Also verified: all 400 logged destinations exist, all 400 sources are gone, no original under
`docs/` is missing from the log, and no image original was silently skipped.

## 5. Four findings

### 5.1 `CS 8 284` exists three times — needs an owner decision

`VP415 ROM dumps/VP415 ROM version survey.png` and `.jpg` are not a ROM survey. Both are the
manual's **`CS 8 284`, "Survey of software releases VP410/415"** — the same page as sheet 187,
rotated upright. The `.png` is the whole page (punch holes and the `CS 8 284` margin code
visible), the `.jpg` a crop of it. Content is identical in all three; they differ only in crop and
resolution (PSNR between the two reference copies is 13 dB purely because of the crop).

They are **kept for now** under honest names:

```
docs/reference/assets/originals/cs-8-284-software-release-survey-upright.png   3510x2482
docs/reference/assets/originals/cs-8-284-software-release-survey-cropped.jpg   1822x1286
docs/service-information/assets/originals/cs-8-284-table-p187.webp             2482x3510
```

This is a genuine violation of *one copy of everything*, deliberately not resolved unilaterally
because the upright scan is the more useful one for a reader: the manual's own copy is sideways.
**Recommendation for phase 6** — written up in full in
[implementation-plan.md](implementation-plan.md) § Phase 6, and listed under *Still genuinely
open*: keep `-upright.png`, delete `-cropped.jpg`, and have `docs/reference/firmware.md` use the
upright version while `docs/service-information/` keeps the manual sheet in its manual position,
the two pages cross-referencing each other. Owner's call.

### 5.2 Two stale titles left over from phase 1 — fixed

Phase 1 corrected the *module* attribution of two sheets but not their `title` text, which still
named the module they had been mistaken for:

| Sheet | Was | Now |
| --- | --- | --- |
| 052 (`CS 6 876`) | "ETBC-C module I - circuit diagram (continued)" | "Focus module J - circuit diagram" |
| 039_040 (`CS 6 870`) panels 1–2 | "Video processor module C - circuit diagram (sync generator)" | "Reference source module D - circuit diagram" |

Both corrected in the sheet map, consistent with the title-block readings recorded in
[phase-1-findings.md](phase-1-findings.md). This mattered: `migrate.py` writes the title into the
migration log, and phase 4 will write it into figure captions.

### 5.3 Derivative names could silently collide — guard added

Outputs are named `<source stem>-preview.webp` / `-zoom.webp`, so two originals sharing a stem in
one directory overwrite each other. Six directories have stem collisions; five are an image beside
its `.pptx` or `.docx` editable source and are harmless, because those carry profile `none`. The
sixth was real — the two `CS 8 284` files above, both `photo`, one silently clobbering the other.

`derive_assets.py` now **exits with an error** naming both files rather than producing a manifest
that disagrees with the disk. The first run of the verification caught this as a byte-count
mismatch, which is why the manifest records byte counts at all.

### 5.4 `build_asset_map.py` is no longer re-runnable

It classifies files by their path under `unsorted-source-material/`, and 400 of those paths no
longer exist. This is inherent to the one-copy design, not a defect. `asset_map.csv` is now a
historical record and the input to `migrate.py`; **`migration-log.csv` is the live index** of what
is where. `derive_assets.py` reads the profile from the migration log, not the asset map.

## 6. Carried forward

> **Phase 3.** `mkdocs.yml` must not let MkDocs copy `assets/originals/` into `site/` twice.
> The originals are published as the "download the full sheet" link, so they do need to reach
> `site/` — but exactly once, and `.manifest.json` should be excluded from the build.

> **Phase 4.** Figure markdown wants three things per image, all in `migration-log.csv`:
> the preview, the zoom, and the caption text (`cs_code` + `notes`). Consider a small
> `figure` macro rather than hand-writing the pair of paths 357 times.

> **Phase 5.** Module Q's page must pull its circuit from
> `modules/r-drive-processor/assets/originals/cs-7-851-circuit-p063-064.webp`, and module P's
> from `modules/n-display-keyboard/assets/originals/cs-7-850-module-sheet-p061-062.webp`.

> **Phase 6.** Resolve finding 5.1 — the recommendation and its alternative are recorded in
> [implementation-plan.md](implementation-plan.md) § Phase 6.
