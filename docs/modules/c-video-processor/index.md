---
title: Module C - Video processor
description: >-
  Video processing between the drop-out corrector and the mixer.
search:
  boost: 2
---

# Module C - Video processor

Video processing between the drop-out corrector and the mixer.

## Overview

The video processor is the player's video source selector. It switches between
internal video from the disc (`CV-TBC`), external video (`CV-EXT`) and
composite sync; inserts the index frame number and index characters; generates
the sandcastle pulse the [RGB module](../b-rgb/index.md) needs; and produces
the clamp pulses that hold the black level steady so the index information can
be inserted at all.

| | |
| --- | --- |
| Designation | **C** — video processor |
| Modification levels | 3 → 4 |
| Data sheet | page 037 (no `CS` code printed) |
| Circuit diagram | `CS 6 869`, page 038 |
| Connectors | `C1`, `C2`, `C3` |
| Note | Composite sync can only be selected when internal video is selected — the player uses it during **pause** and **goto**. |

## The board

<div class="sheet-pair" markdown>
<figure class="sheet sheet--photo" markdown>
[![Module C, component side of the board](assets/web/c-video-processor-top-preview.webp)](assets/web/c-video-processor-top-zoom.webp)
<figcaption>
  Module C, component side.
</figcaption>
</figure>
<figure class="sheet sheet--photo" markdown>
[![Module C, solder side of the board](assets/web/c-video-processor-bottom-preview.webp)](assets/web/c-video-processor-bottom-zoom.webp)
<figcaption>
  Module C, solder side.
</figcaption>
</figure>
</div>

## Where it sits in the player

Third of the four boards in the left-hand cage, between
[B](../b-rgb/index.md) and [D](../d-reference-source/index.md) — see the
[module and connector lay-out](../../system/module-layout.md).

## Circuit description

`CV-TBC`, the time-base-corrected video from
[ETBC B module H](../h-etbc-b/index.md), arrives on `3C1` and reaches switch
IC7201-3A, which is controlled by `CV/CS` from
[drive processor module R](../r-drive-processor/index.md) and chooses between
video and composite sync. The composite sync itself is made by IC7201-3C,
switching between two DC levels — 4 V for video level at pin 5 and 3.3 V for
top sync at pin 3 — under `CSREF` from
[reference source module D](../d-reference-source/index.md).

The output of IC7201-3A goes to IC7201-3B, controlled by `CV-E/I` from module R
to select internal or external video. External video comes from
[analog I/O module U](../u-analog-io/index.md) on `9C2` through a ×2 amplifier
(T7001, T7002). The selected signal passes emitter follower T7003 to the base
of T7008 and is clamped at 4 V by T7004, whose gate is driven by clamp pulses
generated in IC7202.

The full text is in
[chapter 7, module C](../../circuit-description/modules/c-video-processor.md).

## Adjustments

Two adjustments.

!!! info "Required"

    Test disc · voltmeter · scope

    Load the test disc; still picture, colour bar (picture no. 6200).

**1) R3035 — frequency**

- Measure the DC voltage on pin 18 of IC7202.
- Adjust R3035 for **5.5 V ± 0.5 V**.

**2) R3045 — horizontal blanking**

- Search for a white picture (e.g. picture no. 7500).
- Measure sandcastle pulse `SC` on `3C2` with the scope (A channel).
- Measure the G signal on `3B3` with the scope (B channel) and trigger on it.
- Adjust R3045 for a difference of **0.5 μs** between `SC` and the G signal —
  Fig. C1 on the sheet shows the two waveforms and the interval.

**Adjustment when an item is replaced**

| Replaced | Adjust |
| --- | --- |
| IC7202 | R3035, R3045 |
| IC7203 | R3045 |

## Circuit diagram

<figure class="sheet sheet--fold" markdown>
[![Video processor module C - circuit diagram](assets/web/cs-6-869-circuit-p038-preview.webp)](assets/web/cs-6-869-circuit-p038-zoom.webp)
<figcaption>
  Video processor module C - circuit diagram.
  <span class="cs">CS 6 869</span>
  <span class="src">service manual page 038</span>
</figcaption>
</figure>

## PCB lay-out

<figure class="sheet sheet--fold" markdown>
[![Video processor module C (mod level 3) - PCB / parts](assets/web/module-sheet-p037-preview.webp)](assets/web/module-sheet-p037-zoom.webp)
<figcaption>
  Video processor module C (mod level 3) - PCB / parts.
  <span class="src">service manual page 037</span>
</figcaption>
</figure>

## List of electrical parts

**Coils**

| Item | Service code number | Value |
| --- | --- | --- |
| 5001 | 4822 156 10992 | 117 μH |

**Potentiometers**

| Item | Service code number | Value |
| --- | --- | --- |
| 3035 | 5322 101 10666 | 47 kΩ |
| 3045 | 5322 101 10666 | 47 kΩ |

**NTC resistors**

| Item | Service code number | Value |
| --- | --- | --- |
| 3105 | 4822 116 30251 | 150 kΩ 0.5 W |

**Fuse resistors**

| Item | Service code number | Value |
| --- | --- | --- |
| 3065 | 4822 111 10165 | 10 Ω |
| 3108 | 4822 111 90357 | 33 Ω |

**NFR25 resistors**

| Item | Service code number | Value |
| --- | --- | --- |
| 3033 | 4822 111 30508 | 10 Ω |
| 3107 | 4822 111 30593 | 3.3 Ω |

**Capacitors**

| Item | Service code number | Value | Rating |
| --- | --- | --- | --- |
| 2001 | 4822 124 22027 | 47 μF | 25 V |
| 2002 | 4822 124 22027 | 47 μF | 25 V |
| 2003 | 4822 122 31759 | 22 nF | |
| 2004 | 4822 121 42688 | 68 nF | 100 V |
| 2005 | 4822 124 22027 | 47 μF | 25 V |
| 2007 | 4822 122 31759 | 22 nF | |
| 2008 | 4822 122 31769 | 18 pF | |
| 2009 | 4822 122 31759 | 22 nF | |
| 2010 | 5322 124 21749 | 10 μF | 63 V |
| 2011 | 5322 124 21711 | 100 μF | 25 V |
| 2012 | 4822 122 31759 | 22 nF | |
| 2013 | 4822 122 32442 | 10 nF | |
| 2014 | 5322 122 32839 | 100 nF | |
| 2015 | 4822 121 51051 | 4.7 nF | 63 V |
| 2016 | 4822 122 32442 | 10 nF | |
| 2017 | 4822 121 41876 | 220 nF | 20% 63 V |
| 2018 | 4822 124 22031 | 4.7 μF | 63 V |
| 2019 | 4822 121 41837 | 560 nF | 20% 100 V |
| 2020 | 5322 122 32839 | 100 nF | |
| 2021 | 4822 122 31971 | 10 pF | |
| 2022 | 4822 122 31759 | 22 nF | |
| 2023 | 4822 122 32974 | 100 pF | |
| 2024 | 4822 122 32974 | 100 pF | |
| 2025 | 4822 122 31759 | 22 nF | |
| 2026 | 5322 122 32839 | 100 nF | |
| 2027 | 4822 122 31965 | 220 pF | |
| 2028 | 4822 122 31316 | 100 pF | |
| 2101 | 4822 124 22027 | 47 μF | 25 V |

There is no item 2006 on a level-3 board — see the modification levels below.

## Modification levels

The module shipped at level 3 and went to level 4 early in production, because
the amplification of the external CVBS signal was too small. R3007 changed from
130 Ω to 120 Ω, and **C2006 (22 nF), R3014, R3077 and R3078 were added** —
which is why item 2006 is missing from the level-3 parts list above.

Full table, with service code numbers:
[chapter 8, module C](../../service-information/modification-levels.md#mod-c).

## Related

- [Module C circuit description](../../circuit-description/modules/c-video-processor.md) — the chapter 7 text in full
- [Modification levels per module](../../service-information/modification-levels.md#mod-c) — what changed at level 4
- [Fault-finding charts](../../repair/fault-finding.md) — the no-picture charts
- [Module B — RGB](../b-rgb/index.md) — the sandcastle pulse from this module drives its RGB switching
- [Module and connector lay-out](../../system/module-layout.md) — connector positions
- [Electrical parts](../../parts/electrical-parts.md) — the collective list of standard components by service code number; the connectors are in [mechanical parts](../../parts/mechanical-parts.md#module-connectors)
