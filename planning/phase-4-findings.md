# Phase 4 — Chapter content: verification record

The seven non-module chapters of the service manual — 1, 2, 3, 5, 6, 7 and 8 — written up as
36 pages, from the vendor OCR and the 300 dpi scans. What landed, what was corrected, and the
five findings that changed something outside the pages themselves.

---

## 1. What landed

| File | What |
| --- | --- |
| `tools/import_ocr.py` | OCR markdown → page drafts: heading normalisation, LaTeX unpicking, table tidying, figure blocks in the phase 3 pattern |
| 36 pages under `docs/` | The seven chapters, written; ~57 700 words |
| `justfile` | `_lychee` gains `--index-files index.html` — see finding 5 |
| `docs/index.md` | The "being built" note now says which sections are written |
| `planning/service-manual-sheet-map.csv` | `cs_code` recorded for sheets 009 and 010 — see finding 1 |
| `planning/migration-log.csv` | 10 duplicate files dropped, 10 renamed or moved — see findings 1–3 |

## 2. Page inventory — 36 pages

| Chapter | Section | Pages | Sheets | Words |
| --- | --- | --- | --- | --- |
| 1 | `overview/` | 4 | 003–006 | 2 485 |
| 2 | `general-service/` | 10 | 007–017, 027 | 5 494 |
| 3 | `system/` | 5 | 018–026 | 3 824 |
| 5 | `parts/` | 4 | 101–105, 119–124 | 5 814 |
| 6 | `repair/` | 4 | 106–117 | 3 997 |
| 7 | `circuit-description/` | 5 | 118, 125–163 | 29 549 |
| 8 | `service-information/` | 4 | 164–197 | 6 133 |

Every one of the 120 sheets those chapters cover is referenced from exactly one page, and every
figure carries its Philips `CS` code and its manual page number in the caption.

`repair/case-studies/` is phase 6 and is not counted here.

## 3. How the pages were built

`tools/import_ocr.py` produced a first draft of every page: it reads the `ocr_path` the sheet map
names, strips the trailing `CS` code, drops the OCR's own downscaled `img-NN.jpeg` references,
unpicks the LaTeX the OCR wraps units in — `\(700\mathrm{mV}/75\Omega\)` back to `700 mV / 75 Ω` —
demotes the headings (the OCR emits everything as `#`), tidies the padded GFM tables, and appends
the sheet's scan as a figure. It refuses to overwrite a page that has been through the editing pass,
recognising its own marker and the phase 3 stub marker.

Then every page was edited by hand against its scan. That pass is where the work is: the OCR is
good but it flattens two-column layouts, loses table headers, and misreads about one mnemonic in
ten. Long, regular tables — the signal listing, the parts lists, the error codes, the modification
levels — were regenerated from the OCR by throwaway scripts rather than retyped, then corrected
against the scan.

## 4. Transcription accuracy

Sixteen sheets were read at 300 dpi and compared against the page, well past the plan's
"ten random pages":

004, 005, 006, 008, 009, 010, 015, 016, 017, 020 (exhaustively, all four columns), 027, 111,
113–117, 121, 136, 163, 186, 187–192.

Errors found and corrected:

- **The alphabetical signal listing, 22 of 243 mnemonics.** `+12SB` `+5SB` `−12SB` `−5SB` `0-RPM`
  `A1-E/I` `A2-E/I` `AUD1ON` `AUD2ON` `CLOX` `DAEC` `FSDE` `FPI` `MCO` `MCO-EN` `Q1,2`
  `RC5 IN(B)` `RLS` `STBY-BUT` `TILTOK` `TPI` `TX/RX`. The OCR also attached two notes to the
  wrong rows (`SDA`, `SDAT`) and split `TPI` across two rows. The page carries a note listing
  the corrections so a reader can check them.
- **Technical data, page 004.** The OCR emitted the whole *Video* block twice, and read the laser
  type as `AIGaAs`. The page has one *Video* section and reads `AlGaAs`.
- **Module D's output signals, page 143.** A two-column list the OCR emitted as 13 names followed
  by 11 descriptions, having run two pairs together. Re-paired against the scan and set as a table.

Left as printed, because they are the manual's own errors rather than the OCR's: *Course pulse*
for coarse (`CP-1`, `CP-2`), *Mains frequence*, *Recieved data*, `TANGER` for `TANG-ER`, and
`IIC` for I²C — the last is rendered `I²C` on the page.

## 5. Findings

### 5.1 Two sheets had no `CS` code in the sheet map, and they do have one

Sheets 009 (warnings) and 010 (modification levels) were recorded in phase 1 with an empty
`cs_code`. Both carry one: **`CS 7 819`** and **`CS 7 820`**. They were missed because these two
sheets print the code at the **bottom left**, not the bottom right where every other sheet puts it,
and print it with a dot — `CS 7.819`.

Fixed: `cs_code` recorded in `service-manual-sheet-map.csv` and `migration-log.csv`, and the two
originals renamed `text-p009.webp` → `cs-7-819-text-p009.webp` and `text-p010.webp` →
`cs-7-820-text-p010.webp` so that the file names carry the attribution like every other sheet's.

Four sheets still have no `CS` code, and genuinely have none printed: 132, 135, and the chapter
dividers.

### 5.2 The disassembly guide was carrying every image twice

`unsorted-source-material/Disassembly guide/` held a `PNG/` subfolder that phase 2 migrated
alongside the named JPEGs, so `docs/general-service/assets/originals/` ended up with nine images
in two copies each: `untitled-1.png` and `vp415-push-out-tray-manually.jpg` are the same drawing,
and so on for eight more pairs. Compared pixel-wise, each JPEG is a lossy encode of its PNG at
identical dimensions — RMSE 0.6–1.0%, which is JPEG noise on an identical image.

Resolved under the one-copy rule: **the nine PNGs are kept and renamed to the descriptive names
the JPEGs carried; the nine JPEGs are deleted.** Lossless wins, meaningful names win.

A tenth file, `vp415-colour300dpi-fixed-page-120.png`, is a downscaled crop of manual sheet 120,
which is published in full and transcribed as a table. Deleted.

Net: 10 files and 20 derivatives removed; `docs/**/assets/web/` falls from 189 MB to 186 MB.

### 5.3 Two sets of assets were filed away from the page that uses them

- **Sheet 027, connections of semiconductors.** Bound at the end of chapter 3, so phase 2 filed it
  under `docs/system/`. The manual's own contents page files it under chapter 2, which is where
  the plan puts the page. Moved to `docs/general-service/assets/originals/`.
- **The four cleaned-up exploded views** — cabinet, sandwich, front loader, disc drive — were under
  `docs/general-service/` because that is where the disassembly guide landed. They are chapter 5
  material. Moved to `docs/parts/assets/originals/` and renamed
  `exploded-{cabinet,sandwich,frontloader,disc-drive}-clean.png`.

Both moves restore the plan's rule that an asset sits beside the markdown that uses it.

### 5.4 Chapter 7 describes 25 modules, and the sheet map only knows about 22

The sheet map's `module` column records one module per sheet, but four of chapter 7's sheets are
bifolds carrying two module descriptions each — J and K on 148, M and N on 150, P and R on 151,
S and T on 152 — and **module G's entire description is on the second panel of sheet 144**, which
the map records as module F. Module Y's is on sheet 162, recorded as module X.

Consequence for phase 5: do not use the sheet map's `module` column to find a module's chapter 7
text. `docs/circuit-description/modules.md` now carries all 25 descriptions with a stable anchor
each — `#module-a` through `#module-z`, plus `#module-ua`, `#module-ub`, `#module-uc` — and each
links forward to its module page. Phase 5 should link back.

Chapter 7 has **no** description for module Q (RC5 receiver), module V (module carrier) or the
remote control handset. Those three modules have circuit diagrams and parts lists in chapter 4 but
no prose anywhere in the manual.

### 5.5 The link check was reporting every cross-page anchor as broken

Phase 4 is the first phase to link at an anchor on another page — the fault-finding charts link to
individual error codes, the module descriptions link to module pages. All 17 such links were
reported by `just check` as *Cannot find fragment*.

The links and the anchors are both correct. mkdocs writes directory-style URLs
(`.../error-codes/#error-7`) and `lychee`, without being told otherwise, resolves the directory
rather than the `index.html` inside it, so it never sees the fragment. Fixed by adding
`--index-files index.html` to the `_lychee` recipe in the justfile.

`mkdocs build --strict` with `validation.anchors: warn` did not catch these either, in either
direction — it is not a substitute for the link check.

## 6. Exit criteria

| Criterion | Result |
| --- | --- |
| All seven chapters complete | **Yes** — 36 pages, 120 sheets, no stub markers left outside phases 5 and 6 |
| `mkdocs build --strict` passes | **Yes** |
| `just check` passes | **Yes** — 11 995 links, 1 005 unique, 0 errors |
| Spot-check against the original scans | **Yes** — 16 sheets read at 300 dpi; 25 transcription errors found and corrected, listed in §4 |

## 7. Notes for phase 5

- **Anchors to link at.** Module descriptions: `circuit-description/modules.md#module-x`.
  Modification levels: `service-information/modification-levels.md#mod-x`. Error codes:
  `repair/error-codes.md#error-N`.
- **Chapter 8 has no mod-level sheet for modules D, E, N, P, Q, V, W or X.** Those module pages
  should say so rather than leaving the section empty.
- **The `?=` revision request** is documented on `general-service/modification-levels.md`; module R
  and module S pages should link to it.
- **Error codes 77 and 78** were added by DRIVE release 6803.6 and so are absent from the error
  code sheet, `CS 8 114`. Noted on both pages.
- **Module J's erratum** — the 6210/6211 pinout printed as BCE where it should be ECB — was not
  touched in this phase. The package pinouts it contradicts are on
  `general-service/semiconductor-connections.md`, which is where the erratum should point.
