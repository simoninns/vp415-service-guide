# Phase 6 — Original and community material: verification record

The material that is not the service manual: the operating instructions, the firmware survey, the
F-code reference, two repair case studies and the downloads page. What landed, what was checked
against what, and the findings that changed something outside the pages themselves.

---

## 1. What landed

| File | What |
| --- | --- |
| `tools/build_oi_page_map.py` | Works out which printed page each half of each operating-instructions photograph holds, by reading it with tesseract and scoring against the vendor OCR |
| `tools/import_operating_instructions.py` | The OCR of the user manual → 12 page drafts, arranged by the manual's own sections, with the page photographs attached |
| `tools/import_firmware.py` | `planning/firmware-checksums.csv` → the firmware page's two tables, grouped by image rather than by file |
| `planning/operating-instructions-page-map.csv` | 54 halves → 46 printed pages, checked in so the importer needs no OCR |
| 12 operating-instructions pages | The user manual in full, **20 600 words** |
| `docs/reference/firmware.md` · `f-codes.md` · `downloads.md` · `index.md` | The reference section, **7 500 words** |
| `docs/repair/case-studies/` | Two worked diagnostics and their index, **2 400 words** |
| `tools/derive_assets.py` | New `text-spread` profile: rotates a sideways two-page photograph upright and cuts it down the gutter |

`just check` — **13 735 links, 0 errors**, `mkdocs build --strict` clean.

## 2. The operating instructions were photographed, not scanned

The 27 files under `vp415 manual/` are **not pages**. Each is a photograph of two pages of the
booklet lying side by side, shot sideways, and the pairs are not the facing pages a reader would
expect:

| Pattern | Scans | Example |
| --- | --- | --- |
| Two pages two apart | 07–24 | scan-17 is pages **31 and 29**, scan-18 is **30 and 28** |
| The two outer faces of a folded sheet | 03, 04 | scan-03 is pages **7 and 4**, scan-04 is **6 and 5** |
| A true facing spread | 01, 02 | scan-02 is pages **2 and 3** |
| A single page, the rest of the frame blank | 26, 27 | scan-26 is page **45** alone |

Three sheets were photographed twice — **scan-09, scan-12 and scan-25 are second exposures of
scan-07, scan-10 and scan-23**. The files differ (different exposures of the same paper), so both
are kept, but the second exposure is given profile `none`: no derivatives, nothing references it.

**How the mapping was established.** `build_oi_page_map.py` rotates each photograph 90° clockwise,
cuts it in two, reads each half with tesseract, and scores that text against all 46 pages of the
vendor OCR of the same manual, which is page-numbered and reliable. Scoring is **F1, not recall**:
recall alone hands every unreadable half to the shortest page in the book — the section dividers,
which carry a dozen words each. Five halves still could not be scored, all of them dividers, and
they are filled in by eye in an `OVERRIDES` table with the reason written down.

Result: **all 45 printed pages and the front cover are referenced exactly once**, and the eight
unreferenced halves are the three second exposures, three blank versos and the two empty halves of
the single-page shots.

## 3. Sideways scans are now rotated and split at derivation time

The photographs are sideways: publishing them as they are would have given 23 figures a reader has
to tilt their head at, each holding two pages at once. `derive_assets.py` gained a **`text-spread`**
profile that rotates the source upright and cuts it down the gutter, writing `-a-` for the left page
and `-b-` for the right. The originals are untouched — the rotation and the cut are derivative work,
which is exactly what `assets/web/` is for.

This is the first profile that emits more than one derivative pair per source; the manifest and the
stale-file pruning needed no changes, because both are driven by the outputs each entry declares.

## 4. Findings that changed a page outside this phase

### 4.1 The manual's checksum for `LVDOS#1` 6805.3 does not match the dump

`CS 8 284` prints **`BF90`** for program 3104 103 6805.3 — verified against the 300 dpi scan at
native resolution, and the glyph is a typewriter `B`, identical to the `B` of `B42D` two rows
above. The dump of that program computes **`0x8F90`**, and the person who made it put `0x8F90` in
the filename, so the file agrees with itself.

It is the **only one of the fourteen filename checksums that the manual contradicts**; the other
thirteen match the manual exactly. A typewriter `B` for an `8` is the likely explanation, but the
alternative — that the dumped image is not the 6805.3 the survey describes — cannot be ruled out
from the files. Recorded on `docs/reference/firmware.md` and on the module W page; the module W
firmware table keeps the manual's `BF90` with a warning beside it.

### 4.2 Module R and module S claimed dumps that do not exist

Both pages said "dumps of all three / dumps ... are on the firmware page". The collection holds
**only the last release of each**: `DRIVE` 6803.6 and `CONTROL` 6804.9. Of the 14 releases in the
survey, **8 are dumped** — the two above and all six module W EPROMs. Both pages now say which
images exist and which do not.

### 4.3 The user manual names one cable two ways

Page 7 calls the BNC-to-BNC lead **SBC 1015**; Fig. 2 on page 8 draws the same cable, with the same
service code number 4822 320 11003 and the same 1.50 m length, and labels it **SBC 1014**. Both
readings verified against the scan at native resolution. Recorded on the installation page, with
the advice to order by service code number.

### 4.4 The group 6 command descriptor block is labelled with the wrong group code

Page 40 gives the group 6 (vendor-unique) command format with byte 0 labelled **`Group code (0)`**
— copied from the group 0 table above it. It cannot be 0: the operation codes given three lines
later are `CAH` and `C8H`, whose top three bits are `110`, group 6. Anyone implementing LV-DOS
access from the manual would build a wrong descriptor block. Recorded on the SCSI operation page.

The same page's heading for the read command is **`C8H`**, not the `CBH` the vendor OCR produced —
checked against the scan.

### 4.5 A player's software revision can be read from the F-code data

`?=` returns `0`, the major and minor revision of the **drive** software, and the major and minor
revision of the **control** software. Every disc side in `Disc information bytes from a real
VP415.docx` answers **`=01717`**, which identifies that player as running `DRIVE` 3104 103 6803.6
(SW 1.7) and `CONTROL` 3104 103 6804.7 (SW 1.7) — the last drive release and the second-to-last
control release. The response is on the F-code page and the identification is cross-linked to the
software release survey.

### 4.6 The real-player disc responses disagree with themselves in three places

The `misc/` capture was taken twice, and the record has three internal conflicts:

- **CommunityS side B** — `?D` recorded as `D;:026` in the first pass and `D;:01?` in the second.
- **National side B** — recorded as `` P`FAHp ``, but the decimal bytes written beside it,
  080 096 065 065 072 112, spell `` P`AAHp ``.
- **Countryside side B** — the byte list of its own `?U` response is copied into the `?D` row.

All three are published as written, with the conflicts named. Where the ASCII string and the
decimal bytes disagree, the bytes are the safer record.

The decoding itself checks out: the parity bits of the `?D` response for National ++ side A —
x5 bits 3, 2 and 1, each an even parity over three bits of x4 — verify against the specification in
section 6, which is good evidence that the whole scheme is being read correctly.

## 5. The `CS 8 284` triplicate, resolved

Carried from phase 2, finding 5.1. Acted on as the plan recommended:

| File | Fate |
| --- | --- |
| `cs-8-284-software-release-survey-upright.png` (3510×2482) | **Kept** and published on `docs/reference/firmware.md` — a reader comparing checksums wants the table upright |
| `cs-8-284-table-p187.webp` (2482×3510) | **Kept** in its place in the manual, on `docs/service-information/software-releases.md` |
| `cs-8-284-software-release-survey-cropped.jpg` (1822×1286) | **Deleted** — a lossy crop of the upright PNG carrying nothing it does not |

`git rm`, both CSV rows dropped, `build_asset_map.py`'s rule rewritten to exclude the JPEG with the
reason, and `just derive` run to prune the orphaned derivatives. The two survivors cross-reference
each other in their captions, so the remaining duplication is visible rather than accidental.

## 6. Where the section tables live

The user manual's Tables 1, 2 and 3 (the F-code command list, the handset codes and the
acknowledgements) are transcribed **once**, on `docs/reference/f-codes.md`, rather than on both the
section 5 page and the reference page. Section 5 carries the manual's prose and the page scans and
says where the tables went. The command list was checked cell by cell against the page 22 scan at
native resolution, which corrected four character-set errors the OCR made:

| OCR | Correct | Command |
| --- | --- | --- |
| `:` at dec 39 | `'` | Eject |
| `•` | `*` | Halt, and the two halt-and-jump forms |
| `\|0` `\|1` at 5B, 5C, 5D | `[0 [1`, `\0 \1`, `]0 ]1` | Audio 1, video and audio 2 source select |

**The spreadsheet in the collection was checked against the result.** `vp415Fcode.xlsx` is
somebody's typed copy of the same Table 1: it has the same **72 rows in the same order**, and
differs from the manual in six typing slips — *AN EUROCONNECTOR* for A/V, *Audio-I* for Audio-1,
*routed toicomputer*, `_O` for `_0`, a stray `1`, and `2-251)` for the slow speed range `2-250`.
Nothing in it is missing from the manual, so the published table follows the manual, and the
spreadsheet's asset-map note now says what it actually is.

## 7. Deferred, and still deferred

The RGB module calibration guide and the deck electronics adjustment remain **deferred** — see the
plan. Their sources stay under `docs/reference/calibration/assets/originals/`, the directory is in
`exclude_docs`, and `derive_assets.py` skips it. Nothing in `docs/` links to them.

## 8. Left for phase 7

- **Two service-manual scans are still unreferenced**: `cs-7-814-cover-p001` and `contents-p002`,
  the manual's own cover and contents sheet, sitting in `docs/assets/web/` since phase 4. They
  belong on the home page or the overview index.
- **The exterior photographs** under `docs/overview/assets/` — 33 of them — are still unplaced.
- The case studies both stop where their notes stop. If either fault is ever finished on a bench,
  the pages should gain their ending.
