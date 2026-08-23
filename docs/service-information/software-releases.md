---
title: Software releases
description: >-
  Every EPROM release for the VP410 and VP415 — program numbers, revision
  levels, checksums and service code numbers — and what changed at each.
---

# Software releases

Six sheets: a survey of every EPROM release across the VP410 and VP415, then a
description per program of what changed at each revision.

Dumps of these EPROMs, with sizes and SHA-256 checksums, are on the
[firmware](../reference/firmware.md) page. How to read a set's software
revision without opening it — the `?=` F-code — is on
[general service → modification levels](../general-service/modification-levels.md).

## Survey of software releases VP410/415

| Module | Item | Name | Program nbr<br>3104 103 … | SW rev. level | Introduction date | Checksum | Service code nbr<br>4822 209 … |
| --- | --- | --- | --- | --- | --- | --- | --- |
| [Drive proc. (R)](../modules/r-drive-processor/index.md) | 7204 | DRIVE | 6803.4 | 1.5 | 1986-10-30 | `B5F1` | 51257 |
| | | | 6803.5 | 1.6 | 1986-11-24 | `9DB6` | 51257 |
| | | | 6803.6 | 1.7 | 1987-02-23 | `68FF` | 51257 |
| [Control (S)](../modules/s-control/index.md) | 7202 | CONTROL | 6804.4 | 1.4 | 1986-10-30 | `1F53` | 51256 |
| | | | 6804.5 | 1.5 | 1986-11-24 | `2B55` | 51256 |
| | | | 6804.6 | 1.6 | 1987-02-09 | `5D44` | 51256 |
| | | | 6804.7 | 1.7 | 1987-02-23 | `C699` | 51256 |
| | | | 6804.9 | 1.8 | 1987-03-19 | `6728` | 51256 |
| [CPU (W)](../modules/w-cpu-data-grabber/index.md) \* | 7201 | SYNC | 6808.0 | 1.0 | 1986-10-30 | `D120` | 51258 |
| [CPU (W)](../modules/w-cpu-data-grabber/index.md) \* | 7224 | DESCR. | 6807.0 | 1.0 | 1986-10-30 | `1FBE` | 51259 |
| [CPU (W)](../modules/w-cpu-data-grabber/index.md) \* | 7247 | LVDOS#1 | 6805.2 | 1.3 | 1986-10-30 | `B42D` | 51261 \*\* |
| | | | 6805.3 | 1.4 | 1986-11-24 | `BF90` | 51261 \*\* |
| [CPU (W)](../modules/w-cpu-data-grabber/index.md) \* | 7248 | LVDOS#2 | 6806.2 | 1.3 | 1986-10-30 | `1A1C` | 51262 \*\* |
| | | | 6806.3 | 1.4 | 1986-11-24 | `56D7` | 51262 \*\* |

\* Only VP415.

\*\* **Order both service code numbers of LV-DOS** when the program number of
the EPROMs in the set to be repaired deviates from the latest program number.

The checksums are Philips' own 16-bit sums, and they are the quickest way to
identify an EPROM you have in front of you.

<figure class="sheet" markdown>
[![Survey of software releases VP410/415: a table of every EPROM release with module, item number, name, program number, software revision level, introduction date, checksum and service code number](assets/web/cs-8-284-table-p187-preview.webp)](assets/web/cs-8-284-table-p187-zoom.webp)
<figcaption>
  Survey of software releases VP410/415. This sheet is bound sideways in the
  manual; an upright scan of the same table is on the
  <a href="../../reference/firmware/">firmware</a> page.
  <span class="cs">CS 8 284</span>
  <span class="src">service manual page 187</span>
</figcaption>
</figure>

## Description of software modifications

### DRIVE (on module R)

| Program no.<br>3104 103 … | Changed with respect to earlier release | Ref. doc<br>AR33 | SW rev. level |
| --- | --- | --- | --- |
| 6803.4 | First release | — | 1.5 |
| 6803.5 | Eject of disc tray when no disc has been inserted<br>Delayed closing of radial mirror loop at start-up of motor<br>Improved SCAN FRWD action<br>Improved jump behaviour<br>Adaptation of STAND-BY command | 2125-087 | 1.6 |
| 6803.6 | Improved catch-in behaviour, instant jump<br>Influence of phase of 2-PPR signal deleted<br>Adaptation of 2-PPR signal<br>Measurement of radial mirror sensitivity adapted<br>Error code report commutation added — codes 77 and 78 | 2125-100 | 1.7 |

!!! note "Error codes 77 and 78"

    Release 6803.6 added them, which is why they do not appear in the
    [error code table](../repair/error-codes.md) — that sheet was printed
    against an earlier release.

<figure class="sheet" markdown>
[![Description of software modifications: the DRIVE program on module R, listing each program number, what changed with respect to the earlier release, the reference document and the software revision level](assets/web/cs-8-285-text-p188-preview.webp)](assets/web/cs-8-285-text-p188-zoom.webp)
<figcaption>
  Description of software modifications — DRIVE.
  <span class="cs">CS 8 285</span>
  <span class="src">service manual page 188</span>
</figcaption>
</figure>

### CONTROL (on module S)

| Program no.<br>3104 103 … | Changed with respect to earlier release | Ref. doc<br>AR33 | SW rev. level |
| --- | --- | --- | --- |
| 6804.4 | First release | — | 1.4 |
| 6804.5 | Several problems on S-bus, RC-5 and F-code communication solved | 2125-089 | 1.5 |
| 6804.6 | Improved goto time and chapter CLV<br>Improved chapter play CAV<br>Prevent "stand by" when drive is in "replay" mode | 2125-098 | 1.6 |
| 6804.7 | Correction on the "stand by" problem described under rel. 1.6<br>Improved character display in programming mode | 2125-106 | 1.7 |
| 6804.8 | **Not produced** | | — |
| 6804.9 | Switching the interval in the S-bus task when the eject button is pressed in the "ready" mode of the drive — this avoids switching to "stand by" after the interval time elapses (75 s)<br>Changed acknowledge handling of the F-code interpreter<br>Improved chapter play when drive is in replay<br>Repeat LED off when drive is in the "ready" mode | 2125-116 | 1.8 |

<figure class="sheet" markdown>
[![Description of software modifications: the CONTROL program on module S, with six releases from 6804.4 to 6804.9](assets/web/cs-8-286-table-p189-preview.webp)](assets/web/cs-8-286-table-p189-zoom.webp)
<figcaption>
  Software — CONTROL (on module S).
  <span class="cs">CS 8 286</span>
  <span class="src">service manual page 189</span>
</figcaption>
</figure>

### SYNC (on module W)

| Program no.<br>3104 103 … | Changed with respect to earlier release | Ref. doc | SW rev. level |
| --- | --- | --- | --- |
| 6808.0 | First release | — | 1.0 |

<figure class="sheet" markdown>
[![Description of software modifications: the SYNC program on module W, first release only](assets/web/cs-8-287-table-p190-preview.webp)](assets/web/cs-8-287-table-p190-zoom.webp)
<figcaption>
  Software — SYNC (on module W).
  <span class="cs">CS 8 287</span>
  <span class="src">service manual page 190</span>
</figcaption>
</figure>

### DESCRAMBLER (on module W)

| Program no.<br>3104 103 … | Changed with respect to earlier release | Ref. doc | SW rev. level |
| --- | --- | --- | --- |
| 6807.0 | First release | — | 1.0 |

<figure class="sheet" markdown>
[![Description of software modifications: the DESCRAMBLER program on module W, first release only](assets/web/cs-8-288-table-p191-preview.webp)](assets/web/cs-8-288-table-p191-zoom.webp)
<figcaption>
  Software — DESCRAMBLER (on module W).
  <span class="cs">CS 8 288</span>
  <span class="src">service manual page 191</span>
</figcaption>
</figure>

### LV-DOS#1 + LV-DOS#2 (on module W)

| Program no.<br>3104 103 … | Changed with respect to earlier release | Ref. doc<br>AR33 | SW rev. level |
| --- | --- | --- | --- |
| 6805.2 + 6806.2 | First release | — | 1.3 |
| 6805.3 + 6806.3 | Prevent hang-up of drive at internal communication between LV-DOS and CONTROL<br>"Reset to default command" replaced by setting the defaults with separate F-code commands | 2125-088 | 1.4 |

!!! important "Ordering LV-DOS EPROMs"

    When ordering a service code number for an LV-DOS EPROM, the program number
    in the set should be checked. The delivered EPROM is always equipped with
    the latest software release. **If the set to be repaired is equipped with a
    lower release level, both LV-DOS#1 and LV-DOS#2 should be ordered and
    replaced.**

<figure class="sheet" markdown>
[![Description of software modifications: LV-DOS#1 and LV-DOS#2 on module W, with the two releases and the note that both EPROMs must be ordered together](assets/web/cs-8-289-table-p192-preview.webp)](assets/web/cs-8-289-table-p192-zoom.webp)
<figcaption>
  Software — LV-DOS#1 + LV-DOS#2 (on module W).
  <span class="cs">CS 8 289</span>
  <span class="src">service manual page 192</span>
</figcaption>
</figure>
