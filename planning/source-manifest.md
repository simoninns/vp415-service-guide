# VP415 Service Guide — Source Material Manifest

Survey of everything in [unsorted-source-material/](../unsorted-source-material/), what it is,
and where it belongs in the site. Compiled 2026-08-23.

Companion machine-readable files:

- [source-inventory.csv](source-inventory.csv) — every source file with size and pixel dimensions (1525 files).
- [service-manual-page-map.csv](service-manual-page-map.csv) — all 197 service-manual scan pages
  mapped to chapter / section / module / content type / Philips sheet code / **canonical source file**.

---

## 1. Headline numbers

| Category | Files | Size |
| --- | --- | --- |
| Images (scans, photos, diagrams, screenshots) | 554 | 2.30 GB |
| PDFs | 7 | 107 MB |
| Vendor OCR output (markdown + JSON + downscaled JPEGs) | 650 text + 271 jpeg | 14 MB |
| Firmware dumps (ROM / BIN / HEX) | 28 | 0.5 MB |
| Office documents (docx / pptx / xlsx) | 9 | 8.8 MB |
| Archives (zip) | 6 | 0.1 MB |
| **Total** | **1525** | **2477 MB** |
| **Unique by content** | | **1749 MB** |
| **Byte-identical duplication** | | **728 MB** |

The git repository is **1.68 GiB packed** with no LFS — which is almost exactly the unique-content
figure above, because git already stores identical blobs once. See §2.1 and
[implementation-plan.md](implementation-plan.md) §"Asset strategy" for what that means in practice.

---

## 2. The service manual — primary source

`unsorted-source-material/vp415 service manual/`

| Item | Size | Detail |
| --- | --- | --- |
| `Original PNG/` | 1.1 GB | **197 page scans**, 300 dpi colour. One-panel pages are 2482×3510; two-panel captures are 4964×3510. |
| `A4/` | 300 MB | 104 files — **100% byte-identical duplicates** of the matching `Original PNG/` files |
| `A4 bifold/` | 429 MB | 59 files — **100% byte-identical duplicates** of the matching `Original PNG/` files |
| `A4 trifold/` | 243 MB | 17 files — **not duplicates.** Stitched three-panel composites, ~6980×3515, that exist nowhere else |
| `Philips VP415 Service Manual (hires).pdf` | 84 MB | 179 pages. Not a wrapper of the PNGs — see §2.2 |

### 2.1 The `A4*` folders

Verified by SHA-256 and byte comparison across all 180 files:

- `A4/` and `A4 bifold/` together are **728 MB of exact duplication** of `Original PNG/`. They
  carry one piece of information the originals do not: which **physical fold class** each page
  belongs to. That information is now captured in the `fold` column of the page map, so the two
  folders can be deleted with zero loss.
- `A4 trifold/` is different in kind. A trifold sheet is three panels wide (~7000 px); the scanner
  could only capture two panels at a time, so the manual's 17 trifold sheets appear in
  `Original PNG/` as **34 overlapping two-panel captures**, and `A4 trifold/` holds the
  **stitched complete sheet**. Verified on sheet 021_022 (wiring diagram player, CS 7 831): the
  stitched file contains the whole diagram, while pages 021 and 022 are left and right captures
  that overlap in the middle panel.

**Consequence:** for the 17 trifold sheets the stitched file is the only complete rendering and is
the one to publish. The page map's new `publish_source` column records this — 180 canonical files
for 197 logical pages.

The three folders are a complete, non-overlapping partition of the 197 pages
(104 + 59 + 34 = 197 — verified).

### 2.2 The "hires" PDF is a different capture, not a copy

`Philips VP415 Service Manual (hires).pdf` was produced by Adobe Acrobat Paper Capture and uses
MRC compression: a 150 ppi greyscale JPX background plus a **600 ppi 1-bit JBIG2 mask** for the
line art. It has 179 pages, not 197, because trifold sheets are single pages there — so its
pagination does **not** match the PNG page numbering.

The 600 ppi mask is nominally finer than the 300 dpi colour scans, but Acrobat's JBIG2 encoder
performs symbol substitution, which can silently swap visually-similar glyphs. That makes it
unsafe as the authoritative source for part numbers and component references on schematics. The
repo owner's assessment — PNG scans preferred — holds. Keep the PDF as a convenience download,
not as an image source.

### Manual structure (8 chapters, verified page by page)

| Chapter | Pages | Contents |
| --- | --- | --- |
| Front matter | 001–002 | Cover, chapter-tab contents |
| 1 | 003–006 | Technical data; controls, indicators, connections; connector pinning |
| 2 | 007–017, 027 | Remarks, warnings, modification levels, adjustments, demounting, service hints, service tools, symbols, semiconductor connections |
| 3 | 018–026 | Module and connector lay-out, signal listing, wiring diagrams, block diagrams |
| 4 | 028–100 | **Survey of modules + modules A to Z + remote control** |
| 5 | 101–105, 119–124 | Exploded views, mechanical parts lists, electrical parts lists |
| 6 | 106–117 | Repair method, diagnostic software, error codes, fault-finding charts |
| 7 | 118, 125–163 | Circuit description (LaserVision system, optical deck, VP400 series, per-module descriptions) |
| 8 | 164–197 | Service information, modification levels per module, software releases, fault symptoms |

**Two ordering quirks the site must correct** (the physical binder is out of order):

1. Page **027** (*Connections of semiconductors*, CS 8 121) is listed under Chapter 2 in the
   contents but is bound at the end of Chapter 3.
2. Pages **119–124** (optical-deck exploded view, mechanical and electrical parts lists) are
   Chapter 5 content but are bound *after* the Chapter 7 divider on page 118.

The page map CSV records the *logical* chapter, not the binder order.

### Philips sheet codes

Every drawing carries a `CS n nnn` code in the bottom-right corner. Two families matter:

- `CS 7 8xx` — **module data sheets**: adjustments, PCB lay-out, list of electrical parts
- `CS 6 8xx` — **circuit diagrams**

These codes are captured in the page map and give an independent check on page attribution.
Note `CS 8 122` (page 089) is a later-revision PCB lay-out for module W that supersedes
`CS 7 858` (page 090) — both are present in the manual.

### Modules covered by chapter 4

| Mod | Description | Data sheet page(s) | Circuit diagram page(s) |
| --- | --- | --- | --- |
| A | Audio processor | 032 | 033 |
| B | RGB | 035–036 | 034 |
| C | Video processor | 037 | 038, 039 |
| D | Reference source | 041 | 040 |
| E | Slide drive | 042 | 043 |
| F | Motor + sequence | 045 | 044 |
| G | Gen lock | 046 | 047, 048 |
| H | ETBC B | 049 | 048* |
| I | ETBC C | 050 | 051, 052 |
| J | Focus | 053 | 053 (same sheet) |
| K | HF processor | 054 | 055 |
| L | Video drop-out correction | 057 | 056 |
| M | Radial | 058 | 059 |
| N | Display + keyboard | 061 | 060 |
| P | Frontloader | 062 | — |
| Q | RC5 receiver circuit | 063 | 063 |
| R | Drive processor | 063–064 | 065–066 |
| S | Control | 069–070 | 067–068 |
| T | Supply | 071–072 | 073 |
| U | Analog I/O (Ua / Ub / Uc) | 075–078, 081–082 | 074, 079, 080 |
| V | Module carrier | 030–031 | — |
| W | CPU + data grabber (Wa / Wb) | 083–084, 089–090 | 085–088 |
| X | LV-ROM decoder | 091–092 | 093 |
| Y | Video mixer | 096–097 | 094–095 |
| Z | Deck electronics | 098 | 099 |
| RC | Remote control transmitter | 100 | 100 |

\* Page 048 (CS 6 874) sits between the Gen-lock and ETBC-B sheets and its right-hand title block
is not legible at survey resolution. **Flagged for verification in Phase 2.**

---

## 3. Vendor OCR of the documentation *(added by the repo owner)*

`unsorted-source-material/ocr-markdown-service-manual/`

Seven `ocr-playground-download-*` folders, each holding one source PDF's output as
`pages/page-N/markdown.md` + `page-metadata.json`, plus a whole-document `markdown.md`.

| Folder timestamp | Document | Pages | Global page offset |
| --- | --- | --- | --- |
| `…T145947Z` | BBC Master AIV User Guide | 78 | n/a (separate document) |
| `…T150015Z` | Philips VP415 Operating Instructions | 46 | n/a (separate document) |
| `…T150529Z` | Service Manual part 1 of 5 | 44 | pages 001–044 |
| `…T150604Z` | Service Manual part 2 of 5 | 28 | pages 045–072 |
| `…T150708Z` | Service Manual part 3 of 5 | 20 | pages 073–092 |
| `…T150737Z` | Service Manual part 4 of 5 | 47 | pages 093–139 |
| `…T150802Z` | Service Manual part 5 of 5 | 58 | pages 140–197 |

Quality is high: proper headings, GFM tables, correct unit symbols (`μm`, `Ω`, `≤`). This is the
text source for every prose and table page in the site — far better than re-OCRing locally.

**Constraint from the repo owner: the `img-NN.jpeg` files in these folders are downscaled by the
OCR process and must not be used on the site.** Every published image comes from
`Original PNG/` or from the high-resolution photograph folders.

---

## 4. Photographs of the modules

`unsorted-source-material/Module photos/`

| Item | Detail | Destination |
| --- | --- | --- |
| `Plug in modules/` | **43 photographs**, ~4700×1140 each, top and bottom of every plug-in module: A, B, C, D, E, F, G, H, I, J, K, L, M, P, R, S, T (top only), U, W, X, Y — plus remote control top and bottom | One per module page, in that module's asset folder |
| `Module Layout.jpg` | 1200 px annotated overhead shot of the opened player naming all 18 in-situ modules | Chapter 3 — module lay-out |
| `Module Layout.pptx` | Editable source of the above (photo + text callouts) | Keep as editable source |
| `Module V diagram.jpg` | Module carrier V | Module V page |

The plug-in-module photographs are the single most valuable non-manual asset: nothing in the
original manual shows what a module actually looks like.

---

## 5. Deck electronics (module Z) and RGB (module B) working material

`unsorted-source-material/Module Z diagrams/`

- `Deck electronics potentiometers.png` (5.2 MB) + `.pptx` — photo of the deck electronics with
  every adjustment potentiometer annotated: 3040 HF amplitude, 3058 focus/radial ratio,
  3088 tilt offset, 3076 radial balance, 3066 focus gain, 3079 radial gain
- `Deck electronics potentiometer layout.png` + `.pptx` — simplified location diagram
- `Module Z diagrams/` — 6 scope traces: Focus Gain, Focus Radial Ratio, HF Amplitude,
  Radial Balance, Radial Gain, Tilt Offset

`unsorted-source-material/VP415 repair/RGB Module calibration/`

- `Calibration and adjustment of RGB Module.docx` — a substantial original guide by the repo
  owner: prerequisites (test disc alternatives now that the Philips 6" test disc is unobtainable —
  *Jason and the Argonauts* PAL CAV side 4 frame 51420), extender-cable construction, 3D-printed
  disc clamp, front-loader simulation jumper, then step-by-step black level / notch filter /
  chroma / vector adjustments. Also documents R89 and R90, two potentiometers present on
  mod-level-9 boards that the service manual does not show.
- `RGB Module diagram.png` + `.pptx` — annotated board photo locating 3015, 3045, 3080, 3082,
  3084, 5002, 5003, 5004, 5007, 2015, R89, R90, connectors B1/B2/B3 and the probe ground
- `documentation images/` — 15 scope captures keyed to the steps in the guide
- 15 further `Adjustment <ref> pre/post.png` scope captures

**This is original authored content, not manual reproduction.** It belongs in a "Calibration
and adjustment" area alongside the manual's own terser procedure.

---

## 6. Repair case studies

`unsorted-source-material/VP415 repair/`

| Item | Detail |
| --- | --- |
| `Diagnostic mode reports error 9.docx` | Frame-lock error 9 investigation — candidate modules L / G / D, signal-by-signal tests on module G with expected vs measured results, supply-rail checks |
| `Module G 1G1.png`, `2G1.png`, `3G2.png`, `6G1.png`, `6G2.png`, `8G1.png`, `E 7014.png` | Scope traces referenced by the error-9 document |
| `7/Diagnostic mode reports error 7.docx` | Focus error 7 investigation — FOC-EN / !FPI / FOC-IND handshake, module J JFET replacement, objective coil continuity. **Records a service-manual erratum: 6210 and 6211 pinout is printed BCE, should be ECB.** |
| `7/*.png` | 4 scope traces for the error-7 investigation |

These map directly onto the manual's Chapter 6 error codes and make excellent worked examples.
The 6210/6211 erratum should be surfaced on module J's page.

---

## 7. Disassembly guide

`unsorted-source-material/Disassembly guide/`

| Item | Detail |
| --- | --- |
| `VP415 Cabinet exploded diagram.jpg`, `Drive assembly`, `Front-loader`, `Sandwich` | 2048 px cleaned-up exploded views |
| `VP415 Push out tray manually.jpg`, `Remove IO module U.jpg`, `Remove optical deck.jpg`, `Remove sandwich.jpg`, `Upper case and front-loader.jpg` | Step illustrations |
| `Philips-VP415-Back-panel annotated.jpg` | Annotated rear panel |
| `PNG/Untitled-1…5.png` | 1024 px line-art versions of the demounting steps |
| `PNG/vp415-colour300dpi-fixed_Page_102…105, 120.png` | Duplicates of manual pages — **use the `Original PNG/` copies instead** |

---

## 8. Firmware and microcontroller dumps

`unsorted-source-material/VP415 ROM dumps/`

| File | Notes |
| --- | --- |
| `VP415 ROM images/R 3104 103 6803 6 DRIVE V1_7 0x68FF.BIN` | Module R drive processor |
| `VP415 ROM images/S 3104 103 6804 9 CONTROL V1_8 0x6728.BIN` | Module S control |
| `VP415 ROM images/W 3104 103 6805 2/3, 6806 2/3, 6807 0, 6808 0 …BIN` | Module W — CPU V1_3 / V1_4, descrambler (6807), sequencer (6808) |
| `VP410 S Module - Control A 3104 103 68114.BIN` | VP410 variant |
| `domesday_scsi_6807.rom`, `domesday_scsi_6808.rom`, `domesday_6803_drive.bin`, `drive_rom_sdi.BIN` | Earlier/alternate dumps |
| `VP415 ROM version survey.png` (1.7 MB) / `.jpg` | Table of which ROM versions appear in which players |
| `Rom descriptions.txt` | Provenance note from "Jules" identifying 6807 as the descrambler (7224) and 6808 as the sequencer (7201) |
| `old VP415 ROMs/` | Two duplicate module W images |

`unsorted-source-material/Microcontroller dumps/`

| File | Notes |
| --- | --- |
| `Complete/D8041AHC_NEC_VP415_Module_S_Control.hex` | Module S 8041 slave CPU |
| `Complete/D8041AHC_NEC_VP415_Module_W_CPU.hex` | Module W 8041 slave CPU (UPI-41) |
| `Complete/D8041AHC_NEC_VP410_Module_S_Control.hex` | VP410 variant |
| `D8041AHC_NEC.pdf`, `D8741A.pdf` | NEC / Intel datasheets |
| Loose `…2.hex`, `…3.hex` files | Partial dumps — supersede with the `Complete/` versions |

Checksums are embedded in several filenames (`0x68FF`, `0x6728`, `0xB42D`, …) and should be
verified and published in a firmware table.

---

## 9. Exterior photographs

| Folder | Count | Detail |
| --- | --- | --- |
| `Pictures/415Photos/415Photos/` | 22 JPG, 3504×2336 | Front, rear, tray, badging, BBC Domesday disc, remote handset, connected to a BBC Master |
| `Pictures/DSC00262…00284.JPG` | 9 JPG, 3264×2448 | Front panel and rear panel detail, type labels, connector close-ups |
| `Pictures/Philips VP415 LaserVision Player.jpg` / `… Rear.jpg` | 2 | Clean product shots |
| `title picture.jpg` | 1 | Disc on the deck with the case open — good site hero image |

Destination: Chapter 1 (controls, indicators, connections) and the site landing page.

---

## 10. Other documents

| Item | Notes |
| --- | --- |
| `pdfs/Philips VP415 Operating Instructions.pdf` (+ uncompressed 20 MB) | User manual, 8 sections; OCR'd markdown available |
| `vp415 manual/image1…image27.jpg` | 27 photographic scans of the Operating Instructions, 3500×4956, page spreads — the high-resolution source for the user manual |
| `misc/Disc information bytes from a real VP415.docx` + `.pdf` | F-code `?D`/`?P`/`?U`/`?=` responses captured from a real player for each Domesday/BBC disc side |
| `misc/vp415Fcode.xlsx` | F-code reference table |
| `misc/MB88303-Fujitsu.pdf` | Fujitsu MB88303 datasheet |
| `ocr-markdown…/BBC-Master-AIV-User-Guide-1.pdf/` | BBC Master AIV User Guide, OCR'd (78 pages) — context for the Domesday system |

---

## 11. Coverage check

Everything in `unsorted-source-material/` has a destination. Nothing is orphaned.

### 11.1 Redundant copies — delete, no information lost

| Item | Size | Why |
| --- | --- | --- |
| `vp415 service manual/A4/` | 300 MB | byte-identical to `Original PNG/`; fold class preserved in the page map |
| `vp415 service manual/A4 bifold/` | 429 MB | byte-identical to `Original PNG/`; fold class preserved in the page map |
| `Disassembly guide/PNG/vp415-colour300dpi-fixed_Page_*.png` | 5 files | duplicates of manual pages 102–105, 120 |
| `VP415 ROM dumps/old VP415 ROMs/` | 3 files | `domesday_6807_descrambler 0x1FBE.rom` is byte-identical to both `domesday_scsi_6807.rom` and `W …6807 0 CPU V1_0 0x1FBE.BIN` |
| `VP415 ROM dumps/domesday_scsi_6807.rom` | 16 KB | same content under a third name |
| Loose `Microcontroller dumps/*.hex` (partial `2`/`3` variants) | 6 files | superseded by `Complete/` |
| `*.zip` | 6 files | contents already present unpacked |
| `pdfs/…Operating Instructions - uncompressed.pdf` | 20 MB | superseded by the compressed PDF plus the 27 page scans |
| `ocr-markdown-service-manual/**/img-*.jpeg` | 271 files, ~10 MB | downscaled by the OCR vendor; never published (owner's instruction) |

**Total reclaimed from the working tree: ~760 MB.**

### 11.2 Not redundant despite appearances — keep

| Item | Why |
| --- | --- |
| `A4 trifold/` (17 files, 243 MB) | the only complete rendering of the 17 three-panel fold-out sheets |
| `Original PNG/` pages belonging to trifold sheets (34 pages) | the un-stitched captures; keep until the stitch quality is confirmed (see the plan's Phase 1) |
| `Philips VP415 Service Manual (hires).pdf` | a different capture at 600 ppi bilevel, not a copy — §2.2 |
| `Module Layout.pptx`, `RGB Module diagram.pptx`, `Deck electronics potentiometers.pptx` | editable sources for annotated diagrams whose exported PNG/JPG is also present; the annotations are only editable here |

### 11.3 Important caveat about repository size

Deleting these files shrinks the **working tree and every fresh checkout**, but it does **not**
shrink `.git`. Git stores blobs by content hash, so `A4/` and `A4 bifold/` already cost nothing
extra in the 1.68 GiB pack — the pack is ~1.72 GB against 1.75 GB of unique content, i.e. it is
already close to minimal for this history.

Reducing the actual repository size requires rewriting history with `git filter-repo` and
force-pushing. With three commits and a single author, that is straightforward, and now — before
any site content exists — is the cheapest moment to do it. The plan covers this in Phase 1b, and
it is the repo owner's call.

A second, larger lever: **re-encoding the PNG scans as lossless WebP is pixel-identical and
roughly 45% smaller** (measured: 4.0 MB → 2.2 MB, 9.6 MB → 5.3 MB, 22 MB → 12 MB, all with an
absolute-error metric of exactly 0). Applied to `Original PNG/` and `A4 trifold/` that takes
1.35 GB down to about 740 MB with no quality loss whatsoever.
