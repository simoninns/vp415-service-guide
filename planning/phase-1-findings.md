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

## 1. The three unread title blocks — resolved

All three were read directly from full-resolution crops. On a Philips circuit sheet the title
block sits at the **top right** of the frame and the `CS` code at the **bottom left** — the
earlier survey looked bottom-right, which is why they read as illegible.

| Page | CS code | Title block as printed | Module |
| --- | --- | --- | --- |
| 044 | `CS 6 872` | MOTOR + SEQUENCE MODULE (mod level 5) | **F** — agrees with the map |
| 048 | `CS 6 874` | ETBC B MODULE (mod level 5) | **H** — agrees with the map |
| 052 | `CS 6 876` | FOCUS MODULE (mod level 2) | **J** — the map says I ⚠ |

**Page 052 is module J, not module I.** Two independent confirmations beyond the title block:

- the boxed module letter next to the title reads **J**;
- the vendor OCR of the page's component locator table lists **6210** and **6211**, the two
  transistors named in the module-J focus erratum (manifest §6). They appear on no other sheet.

Module I (ETBC C) therefore has one circuit sheet, page 051 (`CS 6 875`), not two.

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

## 3. The trifold stitches are resampled, not lossless joins

Measured for all 17 sheets: a patch was taken from each two-panel capture and the best-matching
position located in the stitched composite.

- **No sheet produces a pixel-exact match at any alignment.** The best-aligned sheets
  (021_022, 030_031, 067_068, 069_070, 085_086, 091_092, 096_097) still differ on **0.4–3.4 %**
  of pixels, at PSNR 23–31 dB.
- Stitched heights vary from **3510 to 3569 px** where every capture is exactly 3510, so the
  stitch applied a deskew/rotation — which necessarily resamples.
- Visually the two are equivalent: at 4× zoom the differences are sub-pixel edge shifts on line
  art, not a loss of detail. The stitch is *different*, not *worse*.
- The stitched width equals capA + capB − overlap in every case, so no content is cropped away.

By the plan's own criterion — *"if it resamples or misaligns, keep the captures"* — the 34
two-panel captures stay. See the decision list.

## 4. `ocr_path` — added

Every one of the 197 rows now carries `ocr_path`, resolving to its
`ocr-playground-download-*/…/pages/page-N/markdown.md`. All 197 resolve; 197 distinct files.

The five-part page offsets are confirmed by the folder names themselves
(`…part2of5-pages045-072.pdf`) **and** independently by content: across the 108 rows that already
carried a CS code, the vendor OCR at the computed offset agreed **108 times out of 108, with zero
contradictions**. A wrong offset could not produce that.

### CS codes recovered

The same pass filled `cs_code` for **89 rows** that were previously blank, read from the vendor
OCR. Coverage goes from 91/197 to **180/197**.

The remaining 17 blanks carry no code at all — verified by eye on a sample. Eight are chapter
dividers (003, 007, 018, 028, 101, 106, 118, 164), one is the front-matter contents (002), and
the rest (009, 010, 032, 037, 081, 084, 132, 135) have a blank bottom-left corner on the sheet.

## 5. `tools/asset_map.csv` — written

All **1189** files under `unsorted-source-material/` are accounted for, with no unmapped file and
**no destination collisions**:

| Disposition | Files | Meaning |
| --- | --- | --- |
| `page-map` | 214 | service-manual scans; governed by `service-manual-page-map.csv` |
| `source-text` | 492 | vendor OCR markdown/JSON consumed by `tools/import_ocr.py` |
| `exclude` | 263 | 256 downscaled OCR `img-*.jpeg`, 6 zips, 1 uncompressed PDF |
| `publish` | 181 | site assets with derivatives |
| `download` | 33 | 28 firmware images, 3 datasheets, the operating-instructions PDF, 1 PDF |
| `convert` | 6 | docx/xlsx/txt converted to markdown in phase 6 |

Regenerated by `tools/build_asset_map.py`, which also documents the derivative profiles.

### `source-inventory.csv` refreshed

It still listed the 172 deleted BBC Master AIV OCR files. Now **1189 rows**, matching the tree
exactly — verified both ways, no file on disk missing from it and no row without a file.

---

## Open decisions

See the plan's decisions list. In short: whether to correct page 052 to module J, how the map
should express a sheet covering two modules, and whether to keep the 34 trifold captures.
