# Phase 1 — page attribution findings

Verification record for the five Phase 1 tasks. Compiled 2026-08-23.

Three independent sources were used throughout:

- **vendor OCR** — `ocr-markdown-service-manual/`, the high-accuracy commercial OCR. Authoritative
  for CS codes, prose and tables. It renders each schematic as an image, so **title-block text
  drawn inside a diagram does not appear in it**.
- **tesseract** — run locally over all 197 full-resolution scans at 0.45 scale. This is the only
  text source for the title blocks inside the drawings.
- **direct reading** — full-resolution crops read by eye, for anything the two disagreed on.

---

## 1. Title blocks — three resolved, and two attribution errors found

On a Philips circuit sheet the title block sits at the **top right** of the frame and the `CS`
code at the **bottom left**. The earlier survey looked bottom-right, which is why three pages read
as illegible.

| Page | CS code | Title block as printed | Module |
| --- | --- | --- | --- |
| 044 | `CS 6 872` | MOTOR + SEQUENCE MODULE (mod level 5) | **F** — as mapped |
| 048 | `CS 6 874` | ETBC B MODULE (mod level 5) | **H** — as mapped |
| 052 | `CS 6 876` | FOCUS MODULE (mod level 2) | **J** — was mapped as I ❌ |

### Page 052 is module J, not module I — corrected

Two independent confirmations beyond the title block:

- the boxed module letter beside the title reads **J**;
- the vendor OCR of the page's component locator table lists **6210** and **6211**, the two
  transistors named in the module-J focus erratum (manifest §6). They appear on no other sheet.

Module I (ETBC C) therefore has one circuit sheet, page 051 (`CS 6 875`), not two.

### Page 039 is module D, not module C — corrected

Found while checking the trifold sheets. Sheet `CS 6 870` (trifold 039_040) is **one schematic
spanning all three panels**, titled *REF. SOURCE MODULE (mod level 2)* with a boxed **D**. There is
no module C content anywhere on it. Page 039 was simply the left two-panel capture of that
schematic.

Module C's circuit is therefore page 038 (`CS 6 869`) alone. The manifest's module table, which
listed C's circuit as "038, 039", is corrected to match.

Both errors have the same cause: a *captured page* is an artefact of the scanner, not a unit of
the document. See §6.

## 2. The `CS 6 8xx` sequence — 881 and 882 are absent

`CS 6 881` and `CS 6 882` appear **nowhere** in the vendor OCR corpus or the tesseract sweep of
all 197 pages. Every other code from 867 to 893 is present and accounted for.

The gap falls between `CS 6 880` (page 060, module N circuit) and `CS 6 883` (sheet 065_066,
module R circuit). The pages physically between them are the two data sheets `CS 7 850`
(modules N and P) and `CS 7 851` (modules Q and R) — and modules **P** and **Q** are precisely
the two modules in that run whose circuits are drawn *on* their data sheet rather than on a
separate `CS 6` sheet. The most economical reading is that 881 and 882 were allocated to circuit
sheets for P and Q that this printing folds into the data sheets. **This is inference, not a
reading** — the codes are simply not in the document.

## 3. The trifold stitches are resampled — captures deleted anyway

Measured for all 17 sheets: a patch was taken from each two-panel capture and the best-matching
position located in the stitched composite.

- **No sheet produces a pixel-exact match at any alignment.** The best-aligned sheets
  (021_022, 030_031, 067_068, 069_070, 085_086, 091_092, 096_097) still differ on **0.4–3.4 %**
  of pixels, at PSNR 23–31 dB.
- Stitched heights vary from **3510 to 3569 px** where every capture is exactly 3510, so the
  stitch applied a deskew/rotation — which necessarily resamples.
- Visually the two are equivalent: at 4× zoom the differences are sub-pixel edge shifts on line
  art, not a loss of detail. The stitch is *different*, not *worse*.
- The stitched width equals capA + capB − overlap in every case, so **no content is cropped**.
- Completeness was checked per sheet: 16 of 17 stitches OCR their expected `CS` code directly, and
  063_064's was confirmed by eye.

**Decision taken: the 34 two-panel captures were deleted** (−172 MB; the plan's ~490 MB estimate
predated the WebP conversion). The stitched composite is now the archival copy for all 17 trifold
sheets. Every trifold row already published from the stitch, so no `publish_source` changed.
The captures remain recoverable from git history.

## 4. `ocr_path` — added

Every row carries `ocr_path`, resolving to its
`ocr-playground-download-*/…/pages/page-N/markdown.md`. All resolve; 197 distinct files.

The five-part page offsets are confirmed by the folder names themselves
(`…part2of5-pages045-072.pdf`) **and** independently by content: across the 108 rows that already
carried a CS code, the vendor OCR at the computed offset agreed **108 times out of 108, with zero
contradictions**. A wrong offset could not produce that.

### CS codes recovered

The same pass filled `cs_code` for **89 rows** that were previously blank, read from the vendor
OCR. Coverage went from 91/197 to **180/197**.

The remaining 17 blanks carry no code at all — verified by eye on a sample. Eight are chapter
dividers (003, 007, 018, 028, 101, 106, 118, 164), one is the front-matter contents (002), and
the rest (009, 010, 032, 037, 081, 084, 132, 135) have a blank bottom-left corner on the sheet.

### One vendor-OCR defect worth knowing

The vendor OCR of **page 089** (module W PCB lay-out, `CS 8 122`) contains a long hallucinated run
of the form `2001 A1 2002 A 2007 A 2011 C11 …` continuing for several thousand tokens. The page is
a dense component-locator grid. Phase 4 must not import that page's table unchecked.

## 5. `tools/asset_map.csv` — written

All **1155** files under `unsorted-source-material/` are accounted for, with no unmapped file and
**no destination collisions**:

| Disposition | Files | Meaning |
| --- | --- | --- |
| `source-text` | 492 | vendor OCR markdown/JSON consumed by `tools/import_ocr.py` |
| `exclude` | 263 | 256 downscaled OCR `img-*.jpeg`, 6 zips, 1 uncompressed PDF |
| `publish` | 181 | site assets with derivatives |
| `page-map` | 180 | service-manual scans; governed by `service-manual-sheet-map.csv` |
| `download` | 33 | 28 firmware images, 3 datasheets, the operating-instructions PDF, 1 PDF |
| `convert` | 6 | docx/xlsx/txt converted to markdown in phase 6 |

Regenerated by `tools/build_asset_map.py`, which also documents the derivative profiles.

### `source-inventory.csv` refreshed

It still listed the 172 deleted BBC Master AIV OCR files. Now **1155 rows**, matching the tree
exactly — verified both ways, no file on disk missing from it and no row without a file.

## 6. The map is now keyed by panel, not by captured page

`service-manual-page-map.csv` (197 page rows) is replaced by
**`service-manual-sheet-map.csv` (273 panel rows)**, built by `tools/build_sheet_map.py`.

A captured page is an artefact of the scanner. It could hold two thirds of one drawing, or the
tail of one module's sheet and the head of another's — which is exactly what produced the page 039
and page 052 errors. A **panel**, the A4-sized face the sheet folds into, is the real unit:

| Fold | Panels | Sheets | Panel rows |
| --- | --- | --- | --- |
| A4 | 1 | 104 | 104 |
| bifold | 2 | 59 | 118 |
| trifold | 3 | 17 | 51 |
| | | **180** | **273** |

Each panel row names its own module, so a sheet covering two modules is now expressible. Having
checked every sheet, exactly **two** do:

| Sheet | CS code | Panel 1 | Panel 2 | Panel 3 |
| --- | --- | --- | --- | --- |
| 061_062 | `CS 7 850` | N — display + keyboard | N | P — frontloader |
| 063_064 | `CS 7 851` | Q — RC5 circuit + RC5 mirror | R — parts list | R — drive processor lay-out |

Both were read directly from the stitched sheets. Sheet 039_040, previously split C/D, is module D
throughout (§1).

Consequence for Phase 5: the plan's rule *"every CS sheet is referenced from exactly one module
page"* must become **every sheet panel** is referenced from exactly one module page. Sheets
`CS 7 850` and `CS 7 851` are each referenced from two module pages.

The map keeps `scan_pages` (e.g. `061+062`) so citations to a printed page number still resolve,
and `ocr_path` per panel so the Phase 4 text import is unaffected — 197 distinct OCR pages, as
before.

---

## Done-when check

- Sheet map: 273 rows, **no unresolved `publish_source` (180 distinct files) and no unresolved
  `ocr_path` (197 distinct files)**; every module A–Z and RC has at least one panel.
- `asset_map.csv`: **1155 of 1155** files accounted for, zero unmapped, zero collisions.
