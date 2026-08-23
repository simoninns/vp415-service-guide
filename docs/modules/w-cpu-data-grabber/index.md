---
title: Module W - CPU + data grabber
description: >-
  CPU and data grabber, with the SCSI interface to the host.
search:
  boost: 2
---

# Module W - CPU + data grabber

CPU and data grabber, with the SCSI interface to the host.

## Overview

Module W is one of the three **sandwich** boards — the part of the machine
that makes a VP415 rather than a VP410. It carries the **data grabber**, which
pulls LV-ROM data off the disc, and the **CPU** that serves it to the host over
SCSI.

The data grabber's job, in sequence:

1. Collect serial data from
   [LV-ROM decoder module X](../x-lv-rom-decoder/index.md).
2. Convert the two serial streams to parallel.
3. Establish lock with the block structure.
4. Read the header.
5. When the wanted header appears, store that block and the two following
   blocks in RAM.
6. Signal the CPU that the header and the three blocks are ready.

The data is unscrambled as it goes, and if error flags arrive with it the CPU
runs a correction routine to recover the corrupt data.

| | |
| --- | --- |
| Designation | **W** — CPU + data grabber (the manual's survey calls it *CPU DATAGR.*) |
| Modification levels | 2 → 3 |
| Parts list | `CS 7 857`, page 083 |
| PCB lay-out | page 084 (mod level 2) · `CS 7 858`, page 090 · **`CS 8 122`, page 089 — later revision** |
| Circuit diagrams | `CS 6 889`, pages 085–086 (with data processing module Wa) · `CS 6 890`, pages 087–088 (EPROM section, with LV-ROM interface module Wb) |
| Connector | `W1` — from [module X](../x-lv-rom-decoder/index.md) |
| Crystal | 5001 (X1), **8 MHz** |
| Firmware | four TMS 27128 EPROMs — see below |

!!! note "Two PCB lay-outs, and the later one supersedes"

    `CS 8 122` (page 089) is a **later revision** of the lay-out and supersedes
    `CS 7 858` (page 090). Both are reproduced below. Check which one matches
    the board in front of you before you use it to find a component.

## The board

<div class="sheet-pair" markdown>
<figure class="sheet sheet--photo" markdown>
[![Module W, component side of the board](assets/web/w-cpu-data-grabber-top-preview.webp)](assets/web/w-cpu-data-grabber-top-zoom.webp)
<figcaption>
  Module W, component side.
</figcaption>
</figure>
<figure class="sheet sheet--photo" markdown>
[![Module W, solder side of the board](assets/web/w-cpu-data-grabber-bottom-preview.webp)](assets/web/w-cpu-data-grabber-bottom-zoom.webp)
<figcaption>
  Module W, solder side.
</figcaption>
</figure>
</div>

## Where it sits in the player

In the sandwich — a second cage beneath the main module carrier, with
[X](../x-lv-rom-decoder/index.md) and [Y](../y-video-mixer/index.md). It is
not visible in the overhead photograph on the
[module and connector lay-out](../../system/module-layout.md) page;
[demounting](../../general-service/demounting.md) covers getting the sandwich
out.

## Circuit description

The board is organised around eight buses:

| Bus | Function |
| --- | --- |
| A | Address from CPU |
| B | Address from byte counter |
| C | RAM and EPROM address |
| D | Data to and from CPU |
| E | Data to and from RAM |
| F | Data — descrambler byte from EPROM |
| G | Data — descrambled data |
| H | Data from the shift registers (serial to parallel) |

Two of them are switched: with `ENW` = 0 the C address bus follows B and the E
data bus follows G; with `ENW` = 1 they follow A and D instead.

Serial data from the LV-ROM decoder — `DLCF` and `DRCF` — is clocked into shift
registers IC9–IC12 and appears as four parallel bytes on the H bus. `SA0`–`SA3`,
decoded from B0 and B1 of the byte counter, strobe the bytes out one at a time;
each is EXORed in IC16 and IC17 with a byte from the **descrambler EPROM** on
the F bus, and the descrambled result appears on the G bus. From there buffer
IC21 transfers it to RAM IC22, with the four header bytes going to header
register IC19/IC20 so the CPU can decide whether this is the sequence it wants.

**Input.** From connector `W1`: `DRCF` data right on pin 8, `DLCF` data left on
pin 4, `STR1` word strobe on pin 5, `STR2` byte strobe on pin 7, `CLCF` bit
clock on pin 6, `ERCF` and `ELCF` error flags right and left on pins 3 and 2,
ground on pin 1. IC2 and IC3 buffer them.

**Sync detector.** The start of a data block is a **12-byte sync pattern**.
EPROM IC1 with D-type flip-flops IC6 and IC7 forms a labyrinth that only
produces the `SNC` output pulse when the correct 96-bit pattern has passed
through it; that pulse starts the byte counter. `SYN` = 1 sets the count to
`000h`, and counting begins when `SYN` goes to 0.

The full text is in
[chapter 7, module W](../../circuit-description/modules.md#module-w).

## Adjustments

The manual gives **no adjustment procedure** for this module.

## Circuit diagram

<figure class="sheet sheet--fold" markdown>
[![CPU + data grabber module W - circuit diagram](assets/web/cs-6-889-circuit-p085-086-preview.webp)](assets/web/cs-6-889-circuit-p085-086-zoom.webp)
<figcaption>
  CPU + data grabber module W - circuit diagram.
  <span class="cs">CS 6 889</span>
  <span class="src">service manual pages 085, 086</span>
</figcaption>
</figure>

<figure class="sheet sheet--fold" markdown>
[![CPU + data grabber module W - circuit diagram (EPROM section)](assets/web/cs-6-890-circuit-p087-088-preview.webp)](assets/web/cs-6-890-circuit-p087-088-zoom.webp)
<figcaption>
  CPU + data grabber module W - circuit diagram (EPROM section).
  <span class="cs">CS 6 890</span>
  <span class="src">service manual pages 087, 088</span>
</figcaption>
</figure>

## PCB lay-out and parts sheet

Four sheets: the parts list, the mod-level-2 lay-out, and the two revisions of
the lay-out proper — the later `CS 8 122` first, then the earlier `CS 7 858`
it supersedes.

<figure class="sheet" markdown>
[![List of electrical parts module W (EPROMs)](assets/web/cs-7-857-parts-p083-preview.webp)](assets/web/cs-7-857-parts-p083-zoom.webp)
<figcaption>
  List of electrical parts module W (EPROMs).
  <span class="cs">CS 7 857</span>
  <span class="src">service manual page 083</span>
</figcaption>
</figure>

<figure class="sheet sheet--fold" markdown>
[![CPU + data grabber module W (mod level 2) - PCB / parts](assets/web/pcb-layout-p084-preview.webp)](assets/web/pcb-layout-p084-zoom.webp)
<figcaption>
  CPU + data grabber module W (mod level 2) - PCB / parts.
  <span class="src">service manual page 084</span>
</figcaption>
</figure>

<figure class="sheet sheet--fold" markdown>
[![CPU + data grabber module W - PCB lay-out (later revision)](assets/web/cs-8-122-pcb-layout-p089-preview.webp)](assets/web/cs-8-122-pcb-layout-p089-zoom.webp)
<figcaption>
  CPU + data grabber module W - PCB lay-out (later revision).
  <span class="cs">CS 8 122</span>
  <span class="src">service manual page 089</span>
</figcaption>
</figure>

<figure class="sheet sheet--fold" markdown>
[![CPU + data grabber module W - PCB lay-out](assets/web/cs-7-858-pcb-layout-p090-preview.webp)](assets/web/cs-7-858-pcb-layout-p090-zoom.webp)
<figcaption>
  CPU + data grabber module W - PCB lay-out.
  <span class="cs">CS 7 858</span>
  <span class="src">service manual page 090</span>
</figcaption>
</figure>

## List of electrical parts

**EPROMs (programmed)**

| Item | PCB | Service code number | Type |
| --- | --- | --- | --- |
| 7201 | IC1 | 4822 209 51258 | TMS 27128 — sync |
| 7224 | IC24 | 4822 209 51259 | TMS 27128 — descrambler |
| 7247 | IC47 | 4822 209 51261 | TMS 27128 — LV DOS 1 |
| 7248 | IC48 | 4822 209 51262 | TMS 27128 — LV DOS 2 |

**Crystals**

| Item | PCB | Service code number | Value |
| --- | --- | --- | --- |
| 5001 | X1 | 4822 242 71628 | 8 MHz |

**Resistor networks**

| Item | PCB | Service code number | Value |
| --- | --- | --- | --- |
| 3003 | R3 | 4822 116 90247 | 9 × 220 Ω |
| 3004 | R4 | 4822 116 90248 | 9 × 330 Ω |
| 3005 | R5 | 4822 116 90247 | 9 × 220 Ω |
| 3006 | R6 | 4822 116 90248 | 9 × 330 Ω |
| 3007 | R7 | 4822 116 90251 | 9 × 3.3 kΩ |

**Capacitors**

| Item | PCB | Service code number | Value | Rating |
| --- | --- | --- | --- | --- |
| 2001 | c1 | 4822 122 31413 | 150 pF | |
| 2002 | c2 | 5322 122 32072 | 33 pF | |
| 2003 | c3 | 5322 124 21749 | 10 μF | 63 V |
| 2004 | c4 | 4822 124 22027 | 47 μF | 25 V |
| 2005 | c5 | 5322 122 32072 | 33 pF | |
| 2006 | c6 | 4822 122 30103 | 22 nF | 63 V |
| 2007 | c7 | 4822 124 22027 | 47 μF | 25 V |
| 2102 – 2177 | c39 – c77 | 4822 122 30103 | 22 nF | 63 V |

This is the one board in the player whose parts list gives **both** codings
side by side — the diagram's four-number item and the board's own printed
reference. Items 2102–2177 are the supply decoupling, c39 to c77 on the board.

## Firmware

Four programmed EPROMs, and the 8041 slave processor.

| Item | PCB | Program | SW rev. | Philips sum16 | Service code number |
| --- | --- | --- | --- | --- | --- |
| 7201 | IC1 | `SYNC` 3104 103 6808.0 | 1.0 | `D120` | 4822 209 51258 |
| 7224 | IC24 | `DESCR.` 3104 103 6807.0 | 1.0 | `1FBE` | 4822 209 51259 |
| 7247 | IC47 | `LVDOS#1` 3104 103 6805.2 | 1.3 | `B42D` | 4822 209 51261 |
| 7247 | IC47 | `LVDOS#1` 3104 103 6805.3 | 1.4 | `BF90` | 4822 209 51261 |
| 7248 | IC48 | `LVDOS#2` 3104 103 6806.2 | 1.3 | `1A1C` | 4822 209 51262 |
| 7248 | IC48 | `LVDOS#2` 3104 103 6806.3 | 1.4 | `56D7` | 4822 209 51262 |

IC1 is the **sync detector** EPROM described above and IC24 the
**descrambler**; the two LV-DOS EPROMs are the CPU's own program. All four are
VP415-only. **All six images above are in the collection** — this is the only
module whose every release has been dumped — with sizes and SHA-256 on the
[firmware](../../reference/firmware.md) page.

!!! warning "The manual's checksum for 6805.3 does not match the dump"

    The survey prints `BF90` for `LVDOS#1` 6805.3, and the row above repeats
    it. The dump of that program computes **`0x8F90`**, and the person who made
    it put `0x8F90` in the filename — so the file agrees with itself and
    disagrees with the manual, uniquely among the fourteen checksums that can
    be checked. A typewriter `B` for an `8` is the likely explanation, but it
    is not proven: see [firmware](../../reference/firmware.md).

!!! important "Order both LV-DOS EPROMs together"

    The software survey's own footnote: when the program number of the EPROMs
    in a set deviates from the latest, **order both service code numbers of
    LV-DOS** — 4822 209 51261 and 4822 209 51262. They are a matched pair.

!!! warning "Open question: the module S and module W 8041 dumps are the same image"

    Every VP415 8041 slave-CPU dump in the collection this site is built from —
    eight files, saved under both **module S Control** and **module W CPU**
    names — decodes to the **same 1 KB image**: Philips sum16 `0xFC62`,
    SHA-256 `35d258eb…`.

    Either modules S and W genuinely share the same UPI-41 firmware, or one
    dump was saved under both names and the other device's image was never
    captured. The files cannot settle which, and neither is presented here as
    fact. Reading the 8041 on a real module W and comparing it against `0xFC62`
    would settle it. The same note is on
    [module S](../s-control/index.md) and on the
    [firmware](../../reference/firmware.md) page.

## Modification levels

The module shipped at level 2 — the level page 084's lay-out is printed for —
and went to level 3 in the second production batch. **There is no mod-level
sheet for module W in chapter 8**, so what changed is not documented there.
What did change in that period is the firmware: `LVDOS#1` 6805.2 → 6805.3 and
`LVDOS#2` 6806.2 → 6806.3, both dated 1986-11-24.

The later PCB lay-out `CS 8 122` is the other visible difference between early
and late boards.

## Related

- [Software releases](../../service-information/software-releases.md) — the `SYNC`, `DESCR.` and both `LVDOS` programs
- [Firmware](../../reference/firmware.md) — dumps with sizes, Philips sums and SHA-256
- [Module circuit descriptions](../../circuit-description/modules.md#module-w) — the chapter 7 text in full
- [Module X — LV-ROM decoder](../x-lv-rom-decoder/index.md) — feeds `DLCF`, `DRCF` and the error flags into `W1`
- [Module S — Control](../s-control/index.md) — the other end of the local bus, and the other 8041
- [SCSI operation](../../operating-instructions/scsi-operation.md) — what this board presents to the host
- [Connector pinning](../../overview/connector-pinning.md) — the SCSI connector
- [Demounting](../../general-service/demounting.md) — getting the sandwich out
- [Modification levels per module](../../service-information/modification-levels.md#survey-of-modification-levels) — the survey has module W going from level 2 to level 3, but chapter 8 carries no mod-level sheet for it: what changed is not documented
- [Electrical parts](../../parts/electrical-parts.md) — the collective list of standard components by service code number; the connectors are in [mechanical parts](../../parts/mechanical-parts.md#module-connectors)
