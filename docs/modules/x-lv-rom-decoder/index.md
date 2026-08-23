---
title: Module X - LV-ROM decoder
description: >-
  LV-ROM decoder: recovering data from the disc's data tracks.
---

# Module X - LV-ROM decoder

LV-ROM decoder: recovering data from the disc's data tracks.

## Overview

The LV-ROM decoder is the board that turns the digital audio channels of a
LaserVision disc into computer data. It demodulates and error-corrects the
EFM-coded data and hands the two serial streams — `DLCF` and `DRCF` — with
their error flags to
[data grabber module W](../w-cpu-data-grabber/index.md).

!!! info "How LV-ROM data is stored"

    The format is the Compact Disc's: 16-bit words at 44 100 samples per
    second, alternating left and right, giving **176.4 kB/s**. The data is
    organised in **blocks of 98 frames**, each frame 12 byte-pairs — 6 `DLCF`
    and 6 `DRCF`, so 24 bytes.

    A block is:

    | | |
    | --- | --- |
    | Sync pattern | 12 bytes |
    | Header | 4 bytes |
    | Data | 2048 bytes |
    | Unused | 8 bytes |
    | CRC — error detection and correction | 280 bytes |
    | **Total** | **2352 bytes** |

    A block is read in **1/75 s**. The disc turns at TV frame rate, 25 Hz, so
    **three blocks are read per revolution** — which is why dividing a block
    number by three gives the frame number, and why the player addresses the
    disc by frame.

| | |
| --- | --- |
| Designation | **X** — LV-ROM decoder |
| Modification levels | 2 (unchanged through production) |
| Data sheet | `CS 7 859`, pages 091–092 (mod level 3) |
| Circuit diagram | `CS 6 891`, page 093 |
| Connector | `X1` — to [module W](../w-cpu-data-grabber/index.md) |
| Crystal | 5601, **4.2336 MHz** |
| Out | `DLCF`, `DRCF` data · `CLCF` bit clock · `STR1`, `STR2` strobes · `ELCF`, `ERCF` error flags |

## The board

<div class="sheet-pair" markdown>
<figure class="sheet sheet--photo" markdown>
[![Module X, component side of the board](assets/web/x-lv-rom-decoder-top-preview.webp)](assets/web/x-lv-rom-decoder-top-zoom.webp)
<figcaption>
  Module X, component side.
</figcaption>
</figure>
<figure class="sheet sheet--photo" markdown>
[![Module X, solder side of the board](assets/web/x-lv-rom-decoder-bottom-preview.webp)](assets/web/x-lv-rom-decoder-bottom-zoom.webp)
<figcaption>
  Module X, solder side.
</figcaption>
</figure>
</div>

## Where it sits in the player

In the sandwich, with [W](../w-cpu-data-grabber/index.md) and
[Y](../y-video-mixer/index.md), beneath the main module carrier — see
[demounting](../../general-service/demounting.md) for getting at it, and the
[module and connector lay-out](../../system/module-layout.md) for where the
sandwich sits.

## Circuit description

The disc encoding is a **cross-interleaved Reed–Solomon code**, protecting
against dust and scratches, with each byte carried as a 14-bit word — **EFM**,
eight-to-fourteen modulation. An EFM word must have at least two and no more
than ten zeros between adjacent ones; because that rule could break at a word
boundary, **three merging bits** are inserted between each pair of words.

Each frame is therefore:

| | |
| --- | --- |
| Sync pattern | 24 bits |
| Control and display | 14 bits |
| Data (24 × 14) | 336 bits |
| Parity (8 × 14) | 112 bits |
| Merging (34 × 3) | 102 bits |

Over a block of 98 frames the control-and-display words accumulate into a
block label in time — minutes, seconds and 1/75 seconds.

The full text is in
[chapter 7, module X](../../circuit-description/modules.md#module-x).

## Adjustments

One adjustment, and it needs a **frequency counter** rather than a scope — the
only adjustment in the player that does.

!!! info "Required"

    Frequency counter

    The set in its **stand-by** position.

**1) L5501 — demodulator frequency**

- Short-circuit pin 6 of IC6501 to ground.
- Measure with the frequency counter on pin 22 of IC6501 (clock).
- Adjust L5501 for **4.32 MHz ± 1 kHz**. The voltage on the junction of R3510
  and R3511 should then be **5 V ± 0.1 V**.
- Remove the short circuit on pin 6.

## Circuit diagram

<figure class="sheet sheet--fold" markdown>
[![LV-ROM decoder module X - circuit diagram](assets/web/cs-6-891-circuit-p093-preview.webp)](assets/web/cs-6-891-circuit-p093-zoom.webp)
<figcaption>
  LV-ROM decoder module X - circuit diagram.
  <span class="cs">CS 6 891</span>
  <span class="src">service manual page 093</span>
</figcaption>
</figure>

## PCB lay-out

<figure class="sheet sheet--fold" markdown>
[![LV-ROM decoder module X (mod level 3) - adjustments / PCB / parts](assets/web/cs-7-859-module-sheet-p091-092-preview.webp)](assets/web/cs-7-859-module-sheet-p091-092-zoom.webp)
<figcaption>
  LV-ROM decoder module X (mod level 3) - adjustments / PCB / parts.
  <span class="cs">CS 7 859</span>
  <span class="src">service manual pages 091, 092</span>
</figcaption>
</figure>

## List of electrical parts

**Crystals**

| Item | Service code number | Value |
| --- | --- | --- |
| 5601 | 4822 242 71461 | 4.2336 MHz |

**Coils**

| Item | Service code number | Value |
| --- | --- | --- |
| 5501 | 4822 156 21155 | 7.95 μH |
| 5503 | 4822 156 20966 | 47 μH |
| 5504 | 4822 156 20966 | 47 μH |
| 5505 | 4822 156 20966 | 47 μH |
| 5506 | 4822 158 10101 | 5.3 μH |
| 5507 | 4822 158 10101 | 5.3 μH |
| 5508 | 4822 158 10101 | 5.3 μH |
| 5701 | 4822 156 21026 | 34 μH |
| 5702 | 4822 156 11005 | 42.5 μH |
| 5703 | 4822 156 11005 | 42.5 μH |
| 5704 | 4822 156 21113 | 52 μH |

**NFR25 resistors**

| Item | Service code number | Value |
| --- | --- | --- |
| 3549 | 4822 111 30492 | 2.2 Ω |

**Capacitors**

| Item | Service code number | Value | Rating |
| --- | --- | --- | --- |
| 2501 | 4822 121 51099 | 22 nF | 63 V |
| 2502 | 4822 121 51099 | 22 nF | 63 V |
| 2505 | 4822 122 31644 | 2.2 nF | |
| 2506 | 4822 122 31644 | 2.2 nF | |
| 2507 | 5322 124 21643 | 22 μF | 40 V |
| 2508 | 4822 122 31974 | 820 pF | |
| 2511 | 4822 122 31759 | 22 nF | |
| 2512 | 4822 122 31759 | 22 nF | |
| 2513 | 5322 124 21643 | 22 μF | 40 V |
| 2514 | 4822 122 31759 | 22 nF | |
| 2515 | 4822 124 22028 | 1 μF | 63 V |
| 2519 | 5322 124 21643 | 22 μF | 40 V |
| 2520 | 4822 122 32976 | 470 pF | |
| 2521 | 4822 122 32976 | 470 pF | |
| 2522 | 4822 122 32442 | 10 nF | |
| 2523 | 4822 122 31759 | 22 nF | |
| 2525 | 4822 122 31644 | 2.2 nF | |
| 2527 | 4822 121 41608 | 100 nF | 100 V |
| 2538 | 4822 122 31759 | 22 nF | |
| 2539 | 4822 122 31759 | 22 nF | |
| 2540 | 5322 124 21643 | 22 μF | 40 V |
| 2541 | 5322 124 21643 | 22 μF | 40 V |
| 2542 | 4822 122 31759 | 22 nF | |
| 2543 | 5322 124 21643 | 22 μF | 40 V |
| 2545 | 4822 122 31759 | 22 nF | |
| 2546 | 4822 122 31759 | 22 nF | |
| 2601 | 4822 122 31759 | 22 nF | |
| 2602 | 4822 121 41608 | 100 nF | 100 V |
| 2603 | 4822 121 41608 | 100 nF | 100 V |
| 2604 | 5322 124 21643 | 22 μF | 40 V |
| 2605 | 4822 121 41936 | 2.2 μF | 10% 100 V |
| 2606 | 4822 122 31759 | 22 nF | |
| 2607 | 4822 122 31965 | 220 pF | |
| 2608 | 4822 122 33002 | 68 pF | |
| 2609 | 4822 122 31759 | 22 nF | |
| 2610 | 4822 122 31759 | 22 nF | |
| 2701 | 4822 121 42915 | 330 pF | |
| 2702 | 4822 122 31974 | 820 pF | |
| 2703 | 4822 122 31974 | 820 pF | |
| 2704 | 4822 122 33002 | 68 pF | |
| 2705 | 4822 121 50632 | 1.5 nF | 250 V |
| 2706 | 4822 122 31768 | 180 pF | |
| 2707 | 4822 122 32442 | 10 nF | |
| 2708 | 5322 124 21643 | 22 μF | 40 V |
| 2709 | 4822 122 32482 | 22 pF | |
| 2710 | 5322 124 21643 | 22 μF | 40 V |
| 2711 | 5322 124 21643 | 22 μF | 40 V |
| 2712 | 4822 121 41608 | 100 nF | 100 V |
| 2713 | 4822 122 31974 | 820 pF | |
| 2714 | 5322 124 21643 | 22 μF | 40 V |
| 2715 | 5322 124 21643 | 22 μF | 40 V |
| 2716 | 4822 121 41608 | 100 nF | 100 V |
| 2717 | 5322 124 21643 | 22 μF | 40 V |

*The vendor OCR read this sheet's four parts columns across rather than down
and lost the item numbers of the first two; the rows here were re-read off the
300 dpi scan.*

## Modification levels

Module X carried **modification level 2 in every production batch** and has no
mod-level sheet in chapter 8. The data sheet above is headed *mod level 3*,
which the survey does not record — read the board, not the sheet.

## Related

- [Module circuit descriptions](../../circuit-description/modules.md#module-x) — the chapter 7 text in full, including the block and frame formats
- [Module W — CPU + data grabber](../w-cpu-data-grabber/index.md) — takes this module's output on `W1`
- [SCSI operation](../../operating-instructions/scsi-operation.md) — what the host does with the data
- [Interactive play](../../operating-instructions/interactive-play.md) — what LV-ROM discs are for
- [Demounting](../../general-service/demounting.md) — getting the sandwich out
