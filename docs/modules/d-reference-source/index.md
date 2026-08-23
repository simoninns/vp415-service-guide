---
title: Module D - Reference source
description: >-
  The player's master reference source: system clocks and sync.
search:
  boost: 2
---

# Module D - Reference source

The player's master reference source: system clocks and sync.

## Overview

The reference source generates every video timing signal the player needs, and
it has to do so very accurately. It runs in one of three modes:

1. **Stand alone** — the 5 MHz crystal is locked to the 10 MHz crystal
   oscillator.
2. **Composite sync external** (`CS-EXT`) — the 5 MHz crystal is locked to an
   external sync signal.
3. **Non-standard composite sync** (`NS-CS`) — the 5 MHz crystal is locked to
   the sync coming out of the sandwich by way of
   [analog I/O module U](../u-analog-io/index.md).

If no sync arrives in mode 2 or 3, the module falls back to stand-alone by
itself.

| | |
| --- | --- |
| Designation | **D** — reference source |
| Modification levels | 2 (unchanged through production) |
| Data sheet | `CS 7 840`, page 041 |
| Circuit diagram | `CS 6 870`, pages 039–040 |
| Connectors | `D1`, `D2`, `D3` |
| Key devices | 5001 5 MHz crystal · 5002 10 MHz crystal · IC7063 sync generator |

## The board

<div class="sheet-pair" markdown>
<figure class="sheet sheet--photo" markdown>
[![Module D, component side of the board](assets/web/d-reference-source-top-preview.webp)](assets/web/d-reference-source-top-zoom.webp)
<figcaption>
  Module D, component side.
</figcaption>
</figure>
<figure class="sheet sheet--photo" markdown>
[![Module D, solder side of the board](assets/web/d-reference-source-bottom-preview.webp)](assets/web/d-reference-source-bottom-zoom.webp)
<figcaption>
  Module D, solder side.
</figcaption>
</figure>
</div>

## Where it sits in the player

Rearmost of the four boards in the left-hand cage, behind
[C](../c-video-processor/index.md) — see the
[module and connector lay-out](../../system/module-layout.md).

## Circuit description

In stand-alone mode the 5 MHz crystal 5001 is locked to the 10 MHz crystal
5002, with inputs `8D2` and `4D2` high impedance; the devices in use are 5002,
7059-2A, 7060-4A, 7061-2B, 7062-3A and 7061-2A. With `CS-S/NS` at +5 V the
5 MHz crystal locks instead to `CS-EXT` on `8D2` (7050–7057 and 7068); with
`CS-S/NS` pulled to ground it locks to `NS-CS` on `10D1` (7068). Both of those
signals reach the module through
[analog I/O module Ua](../u-analog-io/index.md), and `CS-S/NS` itself comes
from [video mixer module Y](../y-video-mixer/index.md); the selection is made
by three NAND gates in IC7068.

`CS-EXT` may be clean composite sync or a whole CVBS signal. If it is CVBS, a
hum remover (IC7050, IC7051) strips the video content, a clamp pulse generator
(IC7053) switches FET T7021 to fix the DC level, and a sync slicer
(IC7054–IC7057) derives composite sync from it.

Sync generator IC7063 treats its sync input as the master, so that its outputs
stay in phase; it compares phase internally and its `PHASE` output drives the
varicap 6013 that pulls the 5 MHz oscillator. If no composite sync is present
at all, IC7063 raises "no sync" on pin 13, which brings the 10 MHz reference
oscillator into use through switch IC7062-3A.

The full text is in
[chapter 7, module D](../../circuit-description/modules.md#module-d).

## Adjustments

The manual gives **no adjustment procedure** for this module: the data sheet
carries only the PCB lay-out and the parts list.

## Circuit diagram

<figure class="sheet sheet--fold" markdown>
[![Reference source module D - circuit diagram](assets/web/cs-6-870-circuit-p039-040-preview.webp)](assets/web/cs-6-870-circuit-p039-040-zoom.webp)
<figcaption>
  Reference source module D - circuit diagram.
  <span class="cs">CS 6 870</span>
  <span class="src">service manual pages 039, 040</span>
</figcaption>
</figure>

## PCB lay-out

<figure class="sheet sheet--fold" markdown>
[![Reference source module D (mod level 2) - PCB / parts](assets/web/cs-7-840-module-sheet-p041-preview.webp)](assets/web/cs-7-840-module-sheet-p041-zoom.webp)
<figcaption>
  Reference source module D (mod level 2) - PCB / parts.
  <span class="cs">CS 7 840</span>
  <span class="src">service manual page 041</span>
</figcaption>
</figure>

## List of electrical parts

**Crystals**

| Item | Service code number | Value |
| --- | --- | --- |
| 5001 | 4822 242 70362 | 5 MHz |
| 5002 | 4822 242 71664 | 10 MHz |

**NFR25 resistors**

| Item | Service code number | Value |
| --- | --- | --- |
| 3001 | 4822 111 30483 | 1 Ω |
| 3002 | 4822 111 30483 | 1 Ω |
| 3003 | 4822 111 30483 | 1 Ω |

**Capacitors**

| Item | Service code number | Value | Rating |
| --- | --- | --- | --- |
| 2020 | 4822 121 42915 | 330 pF | |
| 2021 | 4822 122 33012 | 150 nF | 50 V |
| 2022 | 4822 122 31784 | 4.7 nF | |
| 2023 | 4822 122 32542 | 47 nF | |
| 2024 | 5322 122 32839 | 100 nF | |
| 2025 | 4822 122 32976 | 470 pF | |
| 2026 | 4822 122 32974 | 100 pF | |
| 2027 | 4822 122 32972 | 1 nF | |
| 2028 | 4822 122 32972 | 1 nF | |
| 2030 | 4822 124 20942 | 1.5 μF | 25 V |
| 2039 | 4822 122 33007 | 330 nF | 25 V |
| 2040 | 4822 122 32972 | 1 nF | |
| 2041 | 4822 122 32442 | 10 nF | |
| 2042 | 5322 122 31848 | 33 nF | |
| 2043 | 4822 122 32972 | 1 nF | |
| 2044 | 4822 122 31644 | 2.2 nF | |
| 2045 | 4822 122 33012 | 150 nF | 50 V |
| 2046 | 4822 122 31766 | 120 pF | |
| 2047 | 4822 122 32974 | 100 pF | |
| 2048 | 4822 122 32442 | 10 nF | |
| 2049 | 4822 122 33008 | 120 nF | 50 V |
| 2100 – 2122 | 5322 122 32839 | 100 nF | |
| 2124 – 2130 | 5322 122 32839 | 100 nF | |
| 2131 | 5322 124 10455 | 68 μF | 6.3 V |
| 2132 | 4822 124 20977 | 15 μF | 16 V |
| 2133 | 4822 124 20977 | 15 μF | 16 V |
| 2134 | 4822 124 20977 | 15 μF | 16 V |
| 2135 | 4822 124 40963 | 33 μF | 10 V |
| 2136 | 4822 124 22191 | 15 μF | 10 V |

Items 2100 to 2130 are the supply decoupling and are all the same 100 nF chip
capacitor; the sheet lists them individually. There is no item 2123, and the
board has no 2029 or 2031–2038.

*Transcribed from the sheet above: the vendor OCR read this sheet's item column
and its value column into two unrelated tables, so the rows here were re-read
off the 300 dpi scan.*

## Modification levels

Module D carried **modification level 2 in every production batch** and has no
mod-level sheet in chapter 8 — nothing about it changed that needed
documenting.

## Related

- [Module circuit descriptions](../../circuit-description/modules.md#module-d) — the chapter 7 text in full
- [Error 9 — frame lock](../../repair/case-studies/error-9-frame-lock.md) — a worked investigation in which this module is a candidate
- [Fault-finding charts](../../repair/fault-finding.md) — the "no sync" paths come back here
- [VP400 series architecture](../../circuit-description/vp400-series.md) — where the reference timing fits
- [Module and connector lay-out](../../system/module-layout.md) — connector positions
- [Modification levels per module](../../service-information/modification-levels.md#survey-of-modification-levels) — module D has no mod-level sheet: the survey shows it at level 2 in every production batch
- [Electrical parts](../../parts/electrical-parts.md) — the collective list of standard components by service code number; the connectors are in [mechanical parts](../../parts/mechanical-parts.md#module-connectors)
