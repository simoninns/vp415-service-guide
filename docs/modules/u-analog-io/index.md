---
title: Module U - Analog I/O
description: >-
  Analog I/O in three parts - Ua audio/CVBS, Ub video, Uc teletext.
search:
  boost: 2
---

# Module U - Analog I/O

Analog I/O in three parts - Ua audio/CVBS, Ub video, Uc teletext.

## Overview

Analog I/O is the player's whole back panel on one board: every audio and
video input and output, the PAL encoder, and the teletext bypass. The manual
divides it into **three parts**, and keeps that division in the circuit
diagrams, the circuit descriptions and the adjustments:

| Part | What it does | Circuit diagram |
| --- | --- | --- |
| **Ua** | CVBS and audio — I/O selection, DC restoration of external video, sync in and out, `FAS-REL` horizontal shift | `CS 6 886`, page 074 |
| **Ub** | Video — re-encodes −(R−Y) and −(B−Y) to PAL chroma, mixes luminance and chroma, re-inserts disc text and new syncs, and outputs CVBS to SCART and to `BNC3` | `CS 6 887`, page 079 |
| **Uc** | TXT — the teletext bypass to the CVBS encoder, built around eye-height restorer IC7651 | `CS 6 888`, page 080 |

| | |
| --- | --- |
| Designation | **U** — analog I/O |
| Modification levels | 3 → 4 |
| Data sheets | `CS 7 854`, pages 075–076 and 077–078 (PCB lay-out) · page 081 and `CS 7 856`, page 082 (adjustments and parts) |
| Connectors | `U1`, `U2`, `U3` — `U1` is the 32-way to the module carrier |
| Sockets | `BNC1`–`BNC6`, A/V Euroconnector (SCART), cinch audio in and out |
| Crystals | 5302 **4.433619 MHz** (PAL sub-carrier) · 5602 **13.875 MHz** (teletext) |
| Switches | `SK2` **ENCODED / NOT ENCODED** · `S601` teletext delay · `DS1`–`DS8` DIP switches |

!!! tip "`SK2` is the switch other modules' adjustments keep asking for"

    Four other modules — [B](../b-rgb/index.md), [H](../h-etbc-b/index.md),
    [K](../k-hf-processor/index.md) and
    [L](../l-video-dropout-correction/index.md) — have adjustments that begin
    "press `SK2` on analog I/O module U to **NOT ENCODED**". It is on this
    board, and it must go back to its earlier position afterwards.

## The board

<div class="sheet-pair" markdown>
<figure class="sheet sheet--photo" markdown>
[![Module U, component side of the board](assets/web/u-analog-io-top-preview.webp)](assets/web/u-analog-io-top-zoom.webp)
<figcaption>
  Module U, component side.
</figcaption>
</figure>
<figure class="sheet sheet--photo" markdown>
[![Module U, solder side of the board](assets/web/u-analog-io-bottom-preview.webp)](assets/web/u-analog-io-bottom-zoom.webp)
<figcaption>
  Module U, solder side.
</figcaption>
</figure>
</div>

## Where it sits in the player

Lying flat over the top of the chassis at the back, carrying the rear panel —
so it is the module you have to move to reach almost anything else. See the
[module and connector lay-out](../../system/module-layout.md), and
[demounting](../../general-service/demounting.md) for how to get it out.

## Circuit description

**Ua — CVBS and audio.** The composite sync reference `CS-REF'` becomes the
sync out signal through buffer T7109/T7110, which sets the 2 Vpp amplitude and
the output impedance, and leaves on `BNC6`. External sync or CVBS comes in on
`BNC4` and `BNC5` through buffer T7111/T7112 and goes to
[reference source module D](../d-reference-source/index.md) as `CS-EXT`; the
input is high impedance and the output deliberately low, for immunity to
disturbance. `FAS-REL` is a simple adjustable 0–8 V DC that sets the phase
relation between incoming and outgoing sync — a horizontal shift of **+4 μs to
−4 μs**, adjustable from the rear of the player.

**Ub — video.** `LUM` arrives on `9aU1` from
[RGB module B](../b-rgb/index.md) through the adjustable-gain buffer
T7201/T7202/T7203 to C2204, and is clamped to about 0 V black level by FET
7204 under `BPCLP`. T7205 and T7206 then strip the syncs — T7206's base sits at
ground, so T7205 passes nothing negative — unless `NS-VID` on `6cU1` is high,
which turns on T7217, pulls T7206's base negative and leaves the original
syncs in place.

**Uc — TXT.** CVBS from the disc enters IC7651 at pin 27; the text data is
separated and comes out on pin 15, with the **6.9375 MHz** bit clock
regenerated on pin 14. The data passes IC7657-8C, IC7658 and IC7661 and is
inserted into the CVBS as `INS-TXT` on the Ub diagram. IC7658 is a
variable-length shift register whose length is set by the DIP switches and by
the time difference between `CS-REF` and the sync on pin 25 of IC7651 — which
is why the switch setting and adjustment 6 below both matter.

The full text is in chapter 7, in three parts:
[Ua](../../circuit-description/modules/u-analog-io.md#module-ua),
[Ub](../../circuit-description/modules/u-analog-io.md#module-ub) and
[Uc](../../circuit-description/modules/u-analog-io.md#module-uc).

## Adjustments

Seven adjustments, and the ones on the video output are the reference for the
whole player.

!!! info "Required"

    Test disc · scope

    Load the test disc; still picture, picture no. 6200 (colour bar, EBU test
    signal). **The drive may not be locked to an external video source.**

**1) R3263, R3207, R3240, R3315, R3305 — CVBS amplitudes**

- Measure `CVBS OUT` (ENCODED) on `BNC3` line frequent, terminated in 75 Ω —
  Fig. U1 on the sheet shows the colour-bar waveform with the 700 mV and
  300 mV levels marked.
- Adjust **R3263** for a sync amplitude of **300 mV** relative to black level.
- Adjust **R3207** for a white amplitude of **700 mV** relative to black level.
- Adjust **R3315** until the top of the chroma signal during the **yellow** bar
  is at the same level as white (700 mV).
- Adjust **R3305** until the top of the chroma signal during the **cyan** bar
  is at the same level as white.
- Search for picture no. 8200 (black) and switch the index off.
- Measure `CVBS OUT` frame frequent and display lines 16–20: the VITS and the
  24-bit code appear as TXT info (Fig. U2).
- Adjust **R3240** for an amplitude of **460 mV ± 20 mV** in lines 16–20.

**2) C2315 — chroma sub-carrier**

- Channel A: `CVBS OUT` (ENCODED) on `BNC3`.
- Channel B: the CVBS signal on the emitter of TS7105 (NOT ENCODED).
- Switch the scope to A+B, adding the two.
- Adjust C2315 for minimum amplitude variation in the chroma signal.

**3) L5202 — chroma notch**

- Measure `CVBS OUT` (ENCODED) on `BNC3` line frequent, terminated in 75 Ω.
- Adjust L5202 for **maximum** amplitude of the chroma signal.

**4) R3309, R3319 — burst amplitude**

- Switch the drive to **STAND BY**.
- Measure `CVBS OUT` (ENCODED) on `BNC3` line frequent, terminated in 75 Ω.
- Short pins 10 and 12 of IC7351; adjust **R3309** for a burst amplitude of
  **210 mV ± 10 mV**; remove the short.
- Short pins 5 and 12 of IC7351; adjust **R3319** for **210 mV ± 10 mV**;
  remove the short. The burst amplitude then rises to about 300 mV.

**5) L5601 — eye-height restorer**

- Measure the AC signal on pin 12 of IC7651 (= `MP4`), using a 1:10 FET probe
  or a probe of less than 3 pF.
- Adjust L5601 for maximum amplitude of the AC signal.

**6) S601 — delay control**

- Set S601 for a delay of about **130 ns** — pins 1 and 16 of S601
  interconnected, LSB bit `P0` = 1. See the Uc diagram.

**7) R3530 — beep amplitude**

- Interconnect pins 12 and 14 of IC7553.
- Measure the beep on the cinch output `AUD-1OUT` and adjust R3530 for
  **300 mVpp ± 50 mV**.

**Adjustment when an item is replaced**

| Replaced | Adjust |
| --- | --- |
| IC7351 | R3305, R3315 |
| RGB module | R3305, R3315 |

!!! important "Replacing the whole module"

    Module U is one of the four modules that must be adjusted even when the
    board is swapped complete: adjust **R3305** (R−Y gain) and **R3315** (B−Y
    gain). See [adjustments](../../general-service/adjustments.md).

## Circuit diagram

<figure class="sheet sheet--fold" markdown>
[![Analog I/O module Ua (CVBS + audio part) - circuit diagram](assets/web/cs-6-886-circuit-p074-preview.webp)](assets/web/cs-6-886-circuit-p074-zoom.webp)
<figcaption>
  Analog I/O module Ua (CVBS + audio part) - circuit diagram.
  <span class="cs">CS 6 886</span>
  <span class="src">service manual page 074</span>
</figcaption>
</figure>

<figure class="sheet sheet--fold" markdown>
[![Analog I/O module Ub (video part) - circuit diagram](assets/web/cs-6-887-circuit-p079-preview.webp)](assets/web/cs-6-887-circuit-p079-zoom.webp)
<figcaption>
  Analog I/O module Ub (video part) - circuit diagram.
  <span class="cs">CS 6 887</span>
  <span class="src">service manual page 079</span>
</figcaption>
</figure>

<figure class="sheet sheet--fold" markdown>
[![Analog I/O module Uc (TXT part) - circuit diagram](assets/web/cs-6-888-circuit-p080-preview.webp)](assets/web/cs-6-888-circuit-p080-zoom.webp)
<figcaption>
  Analog I/O module Uc (TXT part) - circuit diagram.
  <span class="cs">CS 6 888</span>
  <span class="src">service manual page 080</span>
</figcaption>
</figure>

## PCB lay-out

<figure class="sheet sheet--fold" markdown>
[![Analog I/O module U (mod level 3) - parts](assets/web/cs-7-854-module-sheet-p075-076-preview.webp)](assets/web/cs-7-854-module-sheet-p075-076-zoom.webp)
<figcaption>
  Analog I/O module U (mod level 3) - parts.
  <span class="cs">CS 7 854</span>
  <span class="src">service manual pages 075, 076</span>
</figcaption>
</figure>

<figure class="sheet sheet--fold" markdown>
[![Analog I/O module U - parts (continued)](assets/web/cs-7-854-module-sheet-p077-078-preview.webp)](assets/web/cs-7-854-module-sheet-p077-078-zoom.webp)
<figcaption>
  Analog I/O module U - parts (continued).
  <span class="cs">CS 7 854</span>
  <span class="src">service manual pages 077, 078</span>
</figcaption>
</figure>

<figure class="sheet" markdown>
[![Analog I/O module U - adjustments](assets/web/adjustments-p081-preview.webp)](assets/web/adjustments-p081-zoom.webp)
<figcaption>
  Analog I/O module U - adjustments.
  <span class="src">service manual page 081</span>
</figcaption>
</figure>

<figure class="sheet sheet--fold" markdown>
[![Analog I/O module U - adjustments (continued) / connector detail](assets/web/cs-7-856-adjustments-p082-preview.webp)](assets/web/cs-7-856-adjustments-p082-zoom.webp)
<figcaption>
  Analog I/O module U - adjustments (continued) / connector detail.
  <span class="cs">CS 7 856</span>
  <span class="src">service manual page 082</span>
</figcaption>
</figure>

## List of electrical parts

**Crystals**

| Item | Service code number | Value |
| --- | --- | --- |
| 5302 | 4822 242 70323 | 4.433619 MHz |
| 5602 | 4822 242 71417 | 13.875 MHz |

**Coils**

| Item | Service code number | Value |
| --- | --- | --- |
| 5201 | 4822 156 21324 | 100 μH |
| 5202 | 4822 156 10996 | 15 μH |
| 5301 | 4822 156 10996 | 15 μH |
| 5601 | 4822 156 10996 | 15 μH |

**Potentiometers**

| Item | Service code number | Value |
| --- | --- | --- |
| 3149 | 4822 101 90063 | 10 kΩ |
| 3207 | 4822 100 20151 | 1 kΩ |
| 3240 | 5322 101 10691 | 4.7 kΩ |
| 3263 | 5322 101 10691 | 4.7 kΩ |
| 3305 | 4822 100 20151 | 1 kΩ |
| 3309 | 5322 101 10691 | 4.7 kΩ |
| 3315 | 4822 100 20151 | 1 kΩ |
| 3319 | 5322 101 10691 | 4.7 kΩ |
| 3530 | 5322 101 10627 | 10 kΩ |

**Fuse resistors**

| Item | Service code number | Value |
| --- | --- | --- |
| 3533 | 4822 111 30831 | 47 Ω |

**NFR25 resistors**

| Item | Service code number | Value |
| --- | --- | --- |
| 3001 | 4822 111 30508 | 10 Ω |
| 3002 | 4822 111 30515 | 18 Ω |
| 3003 | 4822 111 30511 | 12 Ω |
| 3004 | 4822 111 30511 | 12 Ω |
| 3010 | 4822 111 30483 | 1 Ω |
| 3011 | 4822 111 30483 | 1 Ω |
| 3012 | 4822 111 30483 | 1 Ω |
| 3013 | 4822 111 30483 | 1 Ω |

**Trim capacitors**

| Item | Service code number | Value |
| --- | --- | --- |
| 2315 | 4822 125 50062 | 10 pF |

**Capacitors**

| Item | Service code number | Value | Rating |
| --- | --- | --- | --- |
| 2001 | 4822 124 22027 | 47 μF | 25 V |
| 2002 | 4822 124 22027 | 47 μF | 25 V |
| 2003 | 4822 124 22027 | 47 μF | 25 V |
| 2005 | 4822 124 22027 | 47 μF | 25 V |
| 2006 | 4822 122 31965 | 220 pF | |
| 2007 | 4822 122 32975 | 33 pF | |
| 2101 | 4822 122 33011 | 470 nF | 16 V |
| 2102 | 4822 122 31759 | 22 nF | |
| 2103 | 4822 122 31767 | 150 pF | |
| 2104 | 4822 122 31759 | 22 nF | |
| 2105 | 4822 122 33011 | 470 nF | 16 V |
| 2106 | 4822 122 31759 | 22 nF | |
| 2107 | 4822 122 31767 | 150 pF | |
| 2108 | 4822 122 31759 | 22 nF | |
| 2109 | 4822 122 31759 | 22 nF | |
| 2110 | 4822 124 22027 | 47 μF | 25 V |
| 2111 | 4822 124 22027 | 47 μF | 25 V |
| 2112 | 4822 122 33011 | 470 nF | 16 V |
| 2113 | 4822 122 33011 | 470 nF | 16 V |
| 2114 | 4822 122 33007 | 330 nF | 25 V |
| 2201 | 4822 124 22029 | 2.2 μF | 63 V |
| 2202 | 4822 124 22027 | 47 μF | 25 V |
| 2203 | 5322 124 21749 | 10 μF | 63 V |
| 2204 | 4822 122 33011 | 470 nF | 16 V |
| 2205 | 4822 122 31759 | 22 nF | |
| 2206 | 4822 122 31839 | 82 pF | |
| 2207 | 4822 124 22027 | 47 μF | 25 V |
| 2208 | 4822 124 22027 | 47 μF | 25 V |
| 2301 | 4822 122 33011 | 470 nF | 16 V |
| 2302 | 4822 122 33011 | 470 nF | 16 V |
| 2304 | 4822 122 33011 | 470 nF | 16 V |
| 2305 | 4822 122 33011 | 470 nF | 16 V |
| 2307 | 4822 122 32975 | 33 pF | |
| 2308 | 4822 122 31759 | 22 nF | |
| 2309 | 4822 122 31767 | 150 pF | |
| 2310 | 4822 122 31767 | 150 pF | |
| 2311 | 4822 122 31759 | 22 nF | |
| 2312 | 4822 122 31839 | 82 pF | |
| 2313 | 4822 124 22027 | 47 μF | 25 V |
| 2314 | 5322 122 31848 | 33 nF | |
| 2315 | 4822 125 50062 | 10 pF | trimmer |
| 2316 | 4822 122 32482 | 22 pF | |
| 2318 | 4822 124 22027 | 47 μF | 25 V |
| 2319 | 5322 122 31848 | 33 nF | |
| 2323 | 5322 122 31848 | 33 nF | |
| 2324 | 4822 122 32442 | 10 nF | |
| 2325 | 4822 122 31759 | 22 nF | |
| 2501 | 4822 124 22028 | 1 μF | 63 V |
| 2502 | 4822 124 22028 | 1 μF | 63 V |
| 2503 | 4822 124 22028 | 1 μF | 63 V |
| 2504 | 4822 124 22028 | 1 μF | 63 V |
| 2505 | 4822 122 31969 | 3.3 nF | |
| 2506 | 4822 122 31969 | 3.3 nF | |
| 2507 | 4822 122 32975 | 33 pF | |
| 2508 | 4822 122 32975 | 33 pF | |
| 2509 | 4822 124 22188 | 3.3 μF | 63 V |
| 2510 | 4822 124 22188 | 3.3 μF | 63 V |
| 2511 | 4822 122 33009 | 270 nF | 25 V |
| 2512 | 5322 122 32839 | 100 nF | |
| 2513 | 5322 122 32839 | 100 nF | |
| 2514 | 4822 124 22027 | 47 μF | 25 V |
| 2515 | 4822 124 22027 | 47 μF | 25 V |
| 2516 | 4822 124 22027 | 47 μF | 25 V |
| 2601 | 4822 122 33011 | 470 nF | 16 V |
| 2602 | 4822 122 32891 | 68 nF | |
| 2603 | 4822 122 31966 | 27 pF | |
| 2604 | 4822 122 31759 | 22 nF | |
| 2605 | 4822 124 22187 | 15 μF | 63 V |
| 2606 | 4822 122 32442 | 10 nF | |
| 2607 | 4822 122 32504 | 15 pF | |
| 2608 | 5322 122 31647 | 1 nF | |
| 2609 | 4822 122 32975 | 33 pF | |
| 2610 | 4822 122 31759 | 22 nF | |
| 2611 | 4822 122 32142 | 270 pF | |
| 2612 | 4822 122 32974 | 100 pF | |
| 2613 | 4822 122 31773 | 560 pF | |
| 2614 | 4822 122 32976 | 470 pF | |
| 2615 | 4822 122 32442 | 10 nF | |
| 2616 – 2625 | 5322 122 31848 | 33 nF | |
| 2627 | 4822 122 32504 | 15 pF | |

The item numbers are grouped by circuit section — 21xx for Ua, 23xx for the
encoder, 26xx for Uc — so the list has gaps by design. Items 2004, 2317,
2320–2322 and 2626 are not on the board.

*The vendor OCR read the first parts column of `CS 7 856` correctly and then
gave only the item numbers of the remaining three; those rows were re-read off
the 300 dpi scan.*

## Modification levels

The module shipped at level 3 — the level its data sheets are printed for —
and went to level 4 in the second production batch, with three changes:

- R3304 470 Ω → 330 Ω, because the arrange level was too small.
- R3350 and R3351 (100 Ω) added in series with C2302 and C2305, improving
  `CBL` to the encoder.
- IC7651 SAA5230/V3 → SAA5231/V3 — an availability change. **That is the
  teletext eye-height restorer**, the device adjustment 5 measures on.

Full tables, with service code numbers:
[chapter 8, module U](../../service-information/modification-levels.md#mod-u).

## Related

- [Adjustments](../../general-service/adjustments.md) — R3305 and R3315 must be set after a module swap, and after replacing module B
- [Module U circuit description](../../circuit-description/modules/u-analog-io.md) — Ua, Ub and Uc in full
- [Connector pinning](../../overview/connector-pinning.md) — what is on the SCART and the BNC sockets
- [Controls, indicators and connections](../../overview/controls-and-connections.md) — the rear panel this board carries
- [Modification levels per module](../../service-information/modification-levels.md#mod-u) — the level-4 changes
- [Demounting](../../general-service/demounting.md) — removing module U to reach the rest of the player
- [Module B — RGB](../b-rgb/index.md) — supplies the signals this board re-encodes
- [Electrical parts](../../parts/electrical-parts.md) — the collective list of standard components by service code number; the connectors are in [mechanical parts](../../parts/mechanical-parts.md#module-connectors)
