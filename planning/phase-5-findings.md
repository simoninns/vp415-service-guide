# Phase 5 — Module pages: verification record

Chapter 4 of the service manual — the twenty-six module pages — written from the vendor OCR and
the 300 dpi scans. What landed, what was corrected, and the findings that changed something
outside the pages themselves.

---

## 1. What landed

| File | What |
| --- | --- |
| `tools/import_modules.py` | Chapter 4 → module page drafts: sheets from the sheet map's per-panel `module` column, figures in the phase 3 pattern, photographs as a `.sheet-pair`, adjustments lifted from the data sheet OCR, parts lists unfolded from the OCR's multi-column grids, and the "Related" list read off the site's own back-links |
| 26 module pages + `docs/modules/index.md` | Chapter 4, written; **36 400 words** |
| `docs/index.md` | The "being built" note now says the whole service manual is written |

## 2. Page inventory

All twenty-six pages carry the same ten sections, in the order the phase 3 stubs specified:
overview, the board, where it sits, circuit description, adjustments, circuit diagram, PCB
lay-out, list of electrical parts, modification levels, related. Modules S, W and the remote
control carry an extra section (firmware, firmware, mechanical parts respectively); modules Q and
V carry a connector or "what the manual does not contain" section instead of material that does
not exist.

**Every one of the 57 chapter 4 sheets is referenced**, and **all 44 module photographs are
placed**. The two sheets that carry two modules each appear on both pages, with the panel
attribution stated in the caption and in the overview table:

| Sheet | Panels 1–2 | Panel 3 |
| --- | --- | --- |
| `CS 7 850`, pages 061–062 | module N | module P |
| `CS 7 851`, pages 063–064 | module Q (panel 1) | module R (panels 2–3) |

`just check` — 13 396 links, 0 errors.

## 3. How the pages were built

`import_modules.py` drafted every page; then each page was edited by hand against its sheet
rendered from the 300 dpi scan, and the prose written from the chapter 7 circuit description and
the chapter 8 modification levels.

The importer is a second tool rather than another `SECTION_PAGE` entry in `import_ocr.py` because
chapter 4 is not a run of text pages: it is one data sheet and one circuit diagram per module,
which have to be interleaved with material from chapters 3, 7 and 8 and with the photographs,
which are not in the manual at all.

Three things it does that phase 4's importer did not need to:

- **Reads the sheet map per panel.** Four bifolds carry two modules, so a module's sheets cannot
  be found from the file's location — `CS 7 851` is filed under module R but its first panel is
  module Q.
- **Unfolds the parts grids.** The manual prints bulk parts three or four components wide; the OCR
  flattens that to one long row. The groups are cut from the right, so a row whose leading item
  cell the OCR lost still parses (see finding 2).
- **Drops the component locator grids.** Every data sheet prints an item-against-grid-square index
  above its lay-out, hundreds of entries. It belongs to the drawing, not the parts list, and the
  lay-out figure carries it.

## 4. Transcription accuracy

Twenty-two data sheets were read at 1560 px and their parts and adjustment blocks cropped and read
at native 300 dpi resolution where the value column mattered:

032, 035–036, 037, 041, 042, 045, 046, 049, 050, 053, 054, 057, 058, 061–062, 063–064, 069–070,
071–072, 081, 082, 083, 091–092, 096–097, 098, 100 — plus the module J circuit diagram, `CS 6 876`,
and the module and connector lay-out, `CS 7 829`.

Errors found and corrected:

| Where | OCR said | The scan says |
| --- | --- | --- |
| Module A, adjustment 1 | output voltage **1.6 Vpp** | **1,8 Vpp** — published as 1.8 Vpp |
| Module A, adjustment 1 | R3003, R3005 (Audio **demo**) | Audio **demod** |
| Module F, item 2031 | 4822 122 **32978** | 4822 122 **32976** |
| Module H, items 2005 and 2008 | 4822 122 **31758** | 4822 122 **31759** |
| Module H, adjustment 1 | **+6V** : 91 μsec | **+5V** : 91 μsec |
| Module U, adjustment 5 | pin 12-**IC7551** (+MP4) | pin 12–**IC7651** (=MP4) |
| Module Z, item 6020 | GP1S**D**4 Photo interruptor | GP1S**04** photo interrupter |
| Module Z, item 2054 | **66** nF | **68** nF |
| Modules C, H, Y | category heading **Cells** / **Colts** | **Coils** |
| Module X | category heading **NPR25 Resistors** | **NFR25 Resistors** |
| Module K | category heading **PCB-5-067** | not a heading at all — the sheet's PCB stamp |

Six sheets had parts columns the OCR could not be trusted on at all; those lists were transcribed
from the scan and the page says so: **B, C, D, I, U, X and Y**.

One inconsistency is the manual's own and has been left as printed, with a note on the page:
module F item **2052** is given as `4822 122 31759`, **18 nF**, where the same service code is
22 nF everywhere else in the manual.

## 5. Findings

### 5.1 The module J pinout erratum is real, and the devices are power transistors

Carried into phase 5 from the manifest: *the service manual prints the 6210/6211 pinout as BCE; it
should be ECB*, from the error-7 investigation. Reading `CS 6 876` at 300 dpi identifies what they
are — **6210 is a BD436 and 6211 a BD437**, the complementary output pair driving the objective
coil through `FOCACT`. That makes the erratum worth the danger admonition it now has on the module
J page: fitted to the printed order the focus amplifier cannot work, and the transistors may not
survive it.

### 5.2 Sheet 032 lost a whole item-number column in the OCR

The first capacitor block of module A's data sheet — 22 rows — came through with its service codes
and values intact and its item numbers gone. Read off the scan the block is capacitors **2001 to
2022 in order**, so the numbers are restored in `import_modules.py` (`LOST_ITEM_COLUMN`) rather
than the block being published without them. It is the only sheet needing that treatment; the
others that lost a column lost it in a way that could not be reconstructed, and were transcribed
by hand instead.

### 5.3 Module Q is barely in the manual at all, and two `CS` sheets are missing

Module Q has **no data sheet, no parts list, no mod-level sheet and no chapter 7 circuit
description**. Its only appearance is the RC5 circuit on panel 1 of `CS 7 851`. The sheet numbers
`CS 6 881` and `CS 6 882` — which fall exactly between module N's circuit diagram (`CS 6 880`) and
module R's (`CS 6 883`), where module Q's own diagram would sit — **are absent from this printing
of the document entirely**. Recorded on the module Q page as a warning admonition rather than left
as a silent gap.

### 5.4 Module H's adjustment 5 may not apply to the board in front of you

The chapter 8 sheet for module H records a level-5 change deleting the audio correction circuit,
**TS7029 among the parts removed**. Adjustment 5 on the data sheet measures on the emitter of
TS7029. Since the survey shows module H at level 5 in *every* production batch, a board may or may
not have the transistor. Flagged on the page rather than reproducing an adjustment that cannot be
carried out.

### 5.5 Module W's parts list is the only one that gives both codings

Every other module page lists components in the diagram's four-number coding — except supply
module T, which uses the board's letter coding, as `remarks` section 6 says. Module W's sheet gives
**both**, side by side: `7201 IC1`, `2102 c39`. The parts table on that page keeps both columns.
This also meant `import_modules.py` had to accept letter-coded item numbers, which is what makes
module T's list parse at all.

### 5.6 `--force` was made refuse to run without named modules

An early run of `tools/import_modules.py --force` with no arguments re-drafted every page,
destroying the editing pass on seven of them. The tool now errors unless the modules are named:
`--force` exists to redraft one page, not to wipe a phase. The same footgun exists in
`import_ocr.py` and is worth the same guard if that tool is ever run again.

---

## 6. Exit criteria

| Criterion | Status |
| --- | --- |
| All 26 module pages complete | **yes** — every page carries all ten sections |
| Every module photograph placed | **yes** — 44 of 44 |
| Every `CS` sheet panel referenced from exactly one module page | **yes** — 57 sheets; the two shared sheets are shown on both pages with their panel attribution stated |
| `mkdocs build --strict` passes | **yes** |
| `just check` | **yes** — 13 396 links, 0 errors |
