# VP415 Service Guide — Source Material Manifest

Survey of everything in [unsorted-source-material/](../unsorted-source-material/), what it is,
and where it belongs in the site. Compiled 2026-08-23.

> **Status: the space-reclamation pass in §11 has been carried out.** The source tree went from
> **2477 MB to 1041 MB**. See §11.0 for exactly what was done. Figures elsewhere in this document
> describe the tree *after* that pass unless marked "originally".

Companion machine-readable files:

- `source-inventory.csv` — every source file with size and pixel dimensions (1361 files).
- `service-manual-sheet-map.csv` — all 180 service-manual sheets,
  keyed by **panel** (273 rows), mapped to chapter / section / module / content type / Philips
  sheet code / vendor-OCR path / **canonical source file**. Replaces the old page-keyed map; see
  [phase-1-findings.md](phase-1-findings.md) §6.
- [phase-1-findings.md](phase-1-findings.md) — the Phase 1 verification record.

---

## 1. Headline numbers

| Category | Files | Size | Originally |
| --- | --- | --- | --- |
| Images (scans, photos, diagrams) | 662 | 1041 MB | 554 files, 2357 MB |
| PDFs | 6 | 24 MB | 7 files, 107 MB |
| Vendor OCR output (markdown + JSON + downscaled JPEGs) | 650 text + 271 jpeg | 14 MB | unchanged |
| Firmware dumps (ROM / BIN / HEX) | 28 | 0.5 MB | unchanged |
| Office documents (docx / pptx / xlsx) | 9 | 8.8 MB | unchanged |
| Archives (zip) | 6 | 0.1 MB | unchanged |
| **Total** | **1361** | **1041 MB** | **1525 files, 2477 MB** |

The git repository was **1.68 GiB packed** with no LFS — almost exactly the original
unique-content figure, because git already stores identical blobs once. The deletions above
shrink every fresh checkout but do **not** shrink the pack; see §11.3.

---

## 2. The service manual — primary source

`unsorted-source-material/vp415 service manual/`

| Item | Size | Detail |
| --- | --- | --- |
| `Original PNG/` | 402 MB | **163 page scans**, 300 dpi colour, **lossless WebP**. One-panel pages are 2482×3510; two-panel captures are 4964×3510. The 34 trifold captures were deleted in Phase 1. |
| `A4 trifold/` | 126 MB | 17 files, now **lossless WebP** — **not duplicates.** Stitched three-panel composites, ~6980×3515, that exist nowhere else |
| ~~`A4/`~~ | — | *deleted* — was 104 files / 300 MB, 100% byte-identical to `Original PNG/` |
| ~~`A4 bifold/`~~ | — | *deleted* — was 59 files / 429 MB, 100% byte-identical to `Original PNG/` |
| ~~`Philips VP415 Service Manual (hires).pdf`~~ | — | *deleted* at the owner's request; available elsewhere on the web. Was 84 MB / 179 pages — see §2.2 |

The folder name `Original PNG/` is now a slight misnomer; renaming it is deferred to the migration
in the plan's Phase 2a, where these files move into `docs/` and get meaningful names anyway.

### 2.1 The `A4*` folders

Verified by SHA-256 and byte comparison across all 180 files:

- `A4/` and `A4 bifold/` together were **728 MB of exact duplication** of `Original PNG/`. They
  carried one piece of information the originals do not: which **physical fold class** each page
  belongs to. That information is captured in the `fold` column of the sheet map, verified
  byte-for-byte against the folders, so the two folders were deleted with zero loss. All 163 files
  were re-verified identical at deletion time.
- `A4 trifold/` is different in kind. A trifold sheet is three panels wide (~7000 px); the scanner
  could only capture two panels at a time, so the manual's 17 trifold sheets appear in
  `Original PNG/` as **34 overlapping two-panel captures**, and `A4 trifold/` holds the
  **stitched complete sheet**. Verified on sheet 021_022 (wiring diagram player, CS 7 831): the
  stitched file contains the whole diagram, while pages 021 and 022 are left and right captures
  that overlap in the middle panel.

**Consequence:** for the 17 trifold sheets the stitched file is the only complete rendering and is
the one to publish. The sheet map's `publish_source` column records this — 180 canonical files
for 180 sheets (273 panels).

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
repo owner’s assessment — the scans are the better source — holds, and the PDF has been deleted at
their request; it is available elsewhere on the web.

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

The sheet map CSV records the *logical* chapter, not the binder order.

### Philips sheet codes

Every drawing carries a `CS n nnn` code in the bottom-right corner. Two families matter:

- `CS 7 8xx` — **module data sheets**: adjustments, PCB lay-out, list of electrical parts
- `CS 6 8xx` — **circuit diagrams**

These codes are captured in the sheet map and give an independent check on attribution. Phase 1
recovered 89 of them from the vendor OCR, taking coverage to 180 of 197 pages; `CS 6 881` and
`CS 6 882` are absent from the document entirely.
Note `CS 8 122` (page 089) is a later-revision PCB lay-out for module W that supersedes
`CS 7 858` (page 090) — both are present in the manual.

### Modules covered by chapter 4

| Mod | Description | Data sheet page(s) | Circuit diagram page(s) |
| --- | --- | --- | --- |
| A | Audio processor | 032 | 033 |
| B | RGB | 035–036 | 034 |
| C | Video processor | 037 | 038 |
| D | Reference source | 041 | 039_040 (whole sheet, CS 6 870) |
| E | Slide drive | 042 | 043 |
| F | Motor + sequence | 045 | 044 |
| G | Gen lock | 046 | 047 |
| H | ETBC B | 049 | 048 (CS 6 874)* |
| I | ETBC C | 050 | 051 |
| J | Focus | 053 | 052 (CS 6 876) |
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

\* Page 048 (`CS 6 874`) was flagged as illegible at survey resolution. **Resolved in Phase 1:**
read at full resolution, its title block is *ETBC B MODULE (mod level 5)*, boxed **H**. The title
block sits at the sheet's top right, not bottom right, which is why the survey missed it.

**Two attribution errors were corrected in Phase 1** — page 052 is module **J**, not I, and
sheet 039_040 is module **D** throughout, not C+D. See
[phase-1-findings.md](phase-1-findings.md) §1.

---

## 3. Vendor OCR of the documentation *(added by the repo owner)*

`unsorted-source-material/ocr-markdown-service-manual/`

Six `ocr-playground-download-*` folders, each holding one source PDF's output as
`pages/page-N/markdown.md` + `page-metadata.json`, plus a whole-document `markdown.md`.

| Folder timestamp | Document | Pages | Global page offset |
| --- | --- | --- | --- |
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
| `PNG/vp415-colour300dpi-fixed_Page_102…105, 120.png` | 2048 px **cropped** derivatives of manual pages 102–105 and 120 — not duplicates. Lower resolution, but the crop isolates the drawing from the page. See §11.2 |

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

---

## 11. Coverage check

Everything in `unsorted-source-material/` has a destination. Nothing is orphaned.

### 11.0 What has been done

| Action | Result |
| --- | --- |
| Deleted `vp415 service manual/A4/` (104 files) | −300 MB. All 163 files re-verified byte-identical to `Original PNG/` immediately before deletion |
| Deleted `vp415 service manual/A4 bifold/` (59 files) | −429 MB, same verification |
| Deleted `Philips VP415 Service Manual (hires).pdf` | −84 MB, at the owner's request (available elsewhere on the web) |
| Converted 214 scans to **lossless WebP** — 197 in `Original PNG/`, 17 in `A4 trifold/` | 1287 MB → 698 MB, **−589 MB (45.8%)** |

**Source tree: 2477 MB → 1041 MB.**

Every conversion was verified before its PNG was removed: `cwebp -lossless -z 6`, then
`magick compare -metric AE` against the source requiring **exactly 0** differing pixels, plus a
dimension match and a non-empty output. Any file failing either check kept both copies and was
logged. **214 of 214 passed; zero failures.** Compression level `z 6` was chosen over `z 9` after
measuring identical output size at one-fifth the encode time.

The sheet map's `publish_source` column points at the `.webp` files; all 180 canonical paths
re-verified as resolving.

### 11.1 Remaining redundancy — acted on after phase 8

Everything below except the firmware dumps was deleted in the post-phase-8 cleanup, along with the
rest of `unsorted-source-material/`. See the plan's closing section.

| Item | Size | Why it was left |
| --- | --- | --- |
| Firmware dumps — 28 files, 11 distinct images | 0.5 MB | **Kept as-is by decision.** The filenames carry provenance (`domesday_6807_descrambler` ↔ `W 3104 103 6807 0 CPU V1_0 0x1FBE.BIN`), and publishing SHA-256 for every file makes the aliasing self-evident without deleting anything. See §11.5 |
| `*.zip` | 6 files, 0.1 MB | Contents already present unpacked |
| `pdfs/…Operating Instructions - uncompressed.pdf` | 20 MB | Superseded by the compressed PDF plus the 27 page scans — but confirm the compressed copy is legible first |
| `ocr-markdown-service-manual/**/img-*.jpeg` | 271 files, ~10 MB | Downscaled by the OCR vendor; never published. Delete once the OCR text has been imported in Phase 4 |

Also deleted since: the **BBC Master AIV User Guide** OCR (1.4 MB, 78 pages) — out of scope for a
VP415 service guide.

### 11.2 Not redundant despite appearances — keep

| Item | Why |
| --- | --- |
| `A4 trifold/` (17 files, 126 MB) | the only complete rendering of the 17 three-panel fold-out sheets |
| ~~`Original PNG/` pages belonging to trifold sheets (34 pages)~~ | **deleted in Phase 1** (−172 MB). The stitches were measured and do resample (0.4–3.4 % of pixels differ, PSNR 23–31 dB, deskewed), but they crop nothing and are visually equivalent, so the stitch is now the archival copy. See [phase-1-findings.md](phase-1-findings.md) §3 |
| `Disassembly guide/PNG/vp415-colour300dpi-fixed_Page_*.png` (5 files, 3.6 MB) | **correction:** an earlier draft called these duplicates of manual pages 102–105 and 120. They are not — they are 2048 px **cropped** derivatives that isolate the drawing from the page. Lower resolution than the originals we hold, but the cropping is editorial work worth keeping until the asset pipeline reproduces it |
| `Module Layout.pptx`, `RGB Module diagram.pptx`, `Deck electronics potentiometers.pptx` | editable sources for annotated diagrams whose exported PNG/JPG is also present; the annotations are only editable here |

### 11.3 Important caveat about repository size

The deletions and the WebP conversion shrink the **working tree and every fresh checkout** — from
2477 MB to 1041 MB — but they do **not** shrink `.git`. Git stores blobs by content hash, so
`A4/` and `A4 bifold/` already cost nothing extra in the 1.68 GiB pack, and deleting a file never
reclaims its history. The pack will in fact *grow* slightly when the WebP files are committed,
because both the old PNGs and the new WebP files then exist in history.

Reducing the actual repository size required rewriting history with `git filter-repo` and
force-pushing. **Done in Phase 1b** — pack 1.68 GiB → 1.04 GiB, force-pushed to `origin`, all six
commits preserved and every stripped path verified absent from every object. The 1.04 GiB pack
against a 1041 MB working tree means it is now essentially just current content.

### 11.4 Firmware finding — settled after phase 8

Every VP415 8041 microcontroller dump in the collection decodes to the **same 1 KB image**
(0x0000–0x03F0):

- `Complete/D8041AHC_NEC_VP415_Module_S_Control.hex` and
  `Complete/D8041AHC_NEC_VP415_Module_W_CPU.hex` are byte-identical (2891 bytes each).
- The larger loose files of the same names (8848 bytes) differ from each other only by a leading
  blank line and a trailing newline; their HEX records are identical, and they are the same 1 KB
  image repeated three times — the classic artefact of reading a 1 K device in a larger socket.
- Only `Complete/D8041AHC_NEC_VP410_Module_S_Control.hex` (VP410, 2893 bytes) is genuinely
  distinct.

Phase 6 published this as an open question — either the two 8041s genuinely run the same UPI-41
firmware, or one dump was saved under both names — on the grounds that the dump files alone cannot
tell the two apart. **They cannot, but the board photographs can, and they were already in the
repository.**

Both parts are marked `NEC D8041AHC 152`, lot `8710X7`, legible at native resolution in
`docs/modules/s-control/assets/originals/s-control-top.jpg` (IC7211) and
`docs/modules/w-cpu-data-grabber/assets/originals/w-cpu-data-grabber-top.jpg`. `D8041AHC` is the
mask-ROM UPI-41A — not the windowed `D8741A` EPROM, whose datasheet is also held — so the program
is fixed at manufacture and the `152` suffix is its ROM code. Two parts with the same ROM code hold
the same program.

The parts list corroborates it from the paper side: `4822 209 10914 — UPD8041AHC-152` is the only
8041 Philips lists, and it appears among the collective *standard* components, whereas every
programmed EPROM carries its own per-module service code. One stock code covers both positions.

Two limits worth recording. The evidence is the markings of one pair of boards, both from the same
lot, so strictly it establishes what Philips fitted in that build; a different modification level
could in principle differ. And the `152`-is-a-ROM-code step rests on standard NEC practice plus the
parts-list agreement — the `d8041ahc-nec.pdf` in the repository is an image-only scan with no text
layer, so it could not be checked against the datasheet itself.

The firmware page and both module pages now state the finding rather than the question.

### 11.5 Firmware checksums

[firmware-checksums.csv](firmware-checksums.csv) covers all **28** firmware files with: file size,
decoded image size and address range, the Philips 16-bit byte sum, and **SHA-256 of both the raw
file and the decoded image**. Intel HEX files are decoded before hashing, so a HEX and a raw BIN
holding the same firmware hash alike.

Two useful results:

- **The checksum embedded in each Philips filename is a 16-bit sum of all bytes.** Verified on all
  14 files that carry one — 14 match, 0 mismatch. Anyone dumping their own ROM can check it the
  same way, so the firmware page should publish this column.
- **28 files, 11 distinct images.** The duplication is now self-evident from the hashes, which is
  why every file is kept rather than pruned:

| # | Image | sum16 | SHA-256 | Files |
| --- | --- | --- | --- | --- |
| 1 | 8041 slave CPU, 1 KB | `0xFC62` | `35d258eb…` | **8** — every VP415 S-Control and W-CPU dump (see §11.4) |
| 2 | Module R drive, 16 KB | `0x68FF` | `6ec09eeb…` | 4 |
| 3 | Module W descrambler (6807), 16 KB | `0x1FBE` | `85049833…` | 3 |
| 4 | Module W sequencer (6808), 16 KB | `0xD120` | `bc7eb8ca…` | 3 |
| 5 | Module S control V1.8, 64 KB | `0x6728` | `e372542b…` | 2 |
| 6 | Module W CPU V1.3 (6805), 16 KB | `0xB42D` | `d929bc98…` | 2 |
| 7 | Module W CPU V1.3 (6806), 16 KB | `0x1A1C` | `e230f04b…` | 2 |
| 8 | VP410 8041 S-Control, 1 KB | `0xC014` | `b061c815…` | 1 |
| 9 | VP410 S-Control, 64 KB | `0xFC6F` | `9dee7647…` | 1 |
| 10 | Module W CPU V1.4 (6805), 16 KB | `0x8F90` | `ecdd68a6…` | 1 |
| 11 | Module W CPU V1.4 (6806), 16 KB | `0x56D7` | `d87e81e1…` | 1 |

The firmware page should group its table this way — by image, with the filenames listed as
aliases beneath — so a reader sees eleven pieces of firmware rather than twenty-eight downloads.
