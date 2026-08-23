---
title: Module A - Audio processor
description: >-
  Audio demodulation and the audio output stages.
search:
  boost: 2
---

# Module A - Audio processor

Audio demodulation and the audio output stages.

## Overview

The audio processor takes the time-base-corrected HF audio signal from
[ETBC B module H](../h-etbc-b/index.md), splits it into the two FM audio
sub-carriers and demodulates them. The two channels are identical circuits;
only the component values differ, because the sub-carriers do not —
**audio 1 at 683 kHz, audio 2 at 1066 kHz**. Each channel has its own drop-out
correction, and the module can route either channel to either output.

| | |
| --- | --- |
| Designation | **A** — audio processor |
| Modification levels | 2 → 3 |
| Data sheet | page 032 (no `CS` code printed) |
| Circuit diagram | `CS 6 867`, page 033 |
| Connectors | `A1`, `A2` |
| Outputs to | [analog I/O module U](../u-analog-io/index.md) — `AUD1` on `3A1`, `AUD2` on `1A1` |

## The board

<div class="sheet-pair" markdown>
<figure class="sheet sheet--photo" markdown>
[![Module A, component side of the board](assets/web/a-audio-processor-top-preview.webp)](assets/web/a-audio-processor-top-zoom.webp)
<figcaption>
  Module A, component side.
</figcaption>
</figure>
<figure class="sheet sheet--photo" markdown>
[![Module A, solder side of the board](assets/web/a-audio-processor-bottom-preview.webp)](assets/web/a-audio-processor-bottom-zoom.webp)
<figcaption>
  Module A, solder side.
</figcaption>
</figure>
</div>

## Where it sits in the player

Front-most of the four boards in the left-hand cage, ahead of
[B](../b-rgb/index.md), [C](../c-video-processor/index.md) and
[D](../d-reference-source/index.md) — see the
[module and connector lay-out](../../system/module-layout.md).

## Circuit description

`HFATBC`, the time-base-corrected HF audio, arrives on `1A2` and is fed through
two identical channels. In each, a band-pass filter (L5007 for audio 1) feeds
demodulator IC6201-2A, whose output at pin 16 goes through a 50 kHz low-pass
filter and emitter follower T6101 to the source of FET 6102 — normally
conducting — and on through T6103/T6104/T6105 to the output switch.

Drop-out correction is a track-and-hold: the HF residue left in the demodulated
audio is band-pass filtered at 200 kHz around T6115, detected by
T6116/T6117/T6118, inverted by T6123 and used to switch FET 6102 off. C2003
then holds the last audio level for the duration of the drop-out, so there is
no plop. A drop-out detected in either channel operates the track-and-hold in
both.

Which channel reaches which output is set by `AUD-1ON` and `AUD-2ON`. With only
one channel selected, cross-coupling through 2007/3017 and 2021/3041 feeds that
channel to both outputs.

The full text is in
[chapter 7, module A](../../circuit-description/modules.md#module-a).

## Adjustments

The manual lists one adjustment: **the audio demodulator level.**

!!! info "Required"

    Test disc · scope

    Load the test disc, normal play, picture no. 6200–6500 for audio 1 and
    6600–6900 for audio 2 (replay), with 1 kHz audio modulation.

**1) R3003, R3005 — audio demodulator**

- Measure the output voltage on `1A1` and `3A1` (`AUD2` and `AUD1`) with the
  scope.
- Adjust R3003 and R3005 until the output voltage is **1.8 Vpp**.

**Adjustment when an item is replaced**

| Replaced | Adjust |
| --- | --- |
| IC6201 | R3005 |
| IC6202 | R3003 |

## Circuit diagram

<figure class="sheet sheet--fold" markdown>
[![Audio processor module A - circuit diagram](assets/web/cs-6-867-circuit-p033-preview.webp)](assets/web/cs-6-867-circuit-p033-zoom.webp)
<figcaption>
  Audio processor module A - circuit diagram.
  <span class="cs">CS 6 867</span>
  <span class="src">service manual page 033</span>
</figcaption>
</figure>

## PCB lay-out

<figure class="sheet sheet--fold" markdown>
[![Audio processor module A (mod level 2) - adjustments / PCB / parts](assets/web/module-sheet-p032-preview.webp)](assets/web/module-sheet-p032-zoom.webp)
<figcaption>
  Audio processor module A (mod level 2) - adjustments / PCB / parts.
  <span class="src">service manual page 032</span>
</figcaption>
</figure>

## List of electrical parts

**Filters**

| Item | Service code number | Value | Rating |
| --- | --- | --- | --- |
| 5007 | 4822 242 71658 | SLC3251 |  |
| 5008 | 4822 242 71659 | SLC3252 |  |

**Coils**

| Item | Service code number | Value | Rating |
| --- | --- | --- | --- |
| 5001 | 4822 156 20928 | 8 mH |  |
| 5002 | 4822 156 11009 | 130 μH |  |
| 5003 | 4822 156 11009 | 130 μH |  |
| 5004 | 4822 156 20928 | 8 mH |  |
| 5005 | 4822 156 11008 | 110 μH |  |
| 5006 | 4822 156 11008 | 110 μH |  |

**Potentiometers**

| Item | Service code number | Value | Rating |
| --- | --- | --- | --- |
| 3003 | 4822 100 11087 | 2.2 kΩ |  |
| 3005 | 4822 100 11087 | 2.2 kΩ |  |

**Capacitors**

| Item | Service code number | Value | Rating |
| --- | --- | --- | --- |
| 2001 | 4822 122 32808 | 1.2 nF |  |
| 2002 | 4822 122 32808 | 1.2 nF |  |
| 2003 | 4822 122 32856 | 8.2 nF |  |
| 2004 | 5322 124 21711 | 100 μF | 25 V |
| 2005 | 4822 122 32597 | 6.8 nF |  |
| 2006 | 4822 124 22189 | 6.8 μF | 63 V |
| 2007 | 5322 124 21749 | 10 μF | 63 V |
| 2008 | 5322 122 32839 | 100 nF |  |
| 2009 | 4822 122 32442 | 10 nF |  |
| 2010 | 4822 122 31759 | 22 nF |  |
| 2011 | 4822 122 31768 | 180 pF |  |
| 2012 | 4822 122 32975 | 33 pF |  |
| 2013 | 4822 122 31759 | 22 nF |  |
| 2014 | 4822 122 32442 | 10 nF |  |
| 2015 | 4822 122 32808 | 1.2 nF |  |
| 2016 | 4822 122 32808 | 1.2 nF |  |
| 2017 | 4822 122 32856 | 8.2 nF |  |
| 2018 | 5322 124 21711 | 100 μF | 25 V |
| 2019 | 4822 122 32597 | 6.8 nF |  |
| 2020 | 4822 124 22189 | 6.8 μF | 63 V |
| 2021 | 5322 124 21749 | 10 μF | 63 V |
| 2022 | 5322 122 32839 | 100 nF |  |
| 2023 | 4822 122 32442 | 10 nF |  |
| 2024 | 4822 122 31759 | 22 nF |  |
| 2025 | 4822 122 32482 | 22 pF |  |
| 2026 | 4822 122 31766 | 120 pF |  |
| 2027 | 4822 122 31759 | 22 nF |  |
| 2028 | 4822 122 32442 | 10 nF |  |
| 2030 | 4822 122 31759 | 22 nF |  |
| 2034 | 5322 124 21711 | 100 μF | 25 V |
| 2036 | 4822 122 31759 | 22 nF |  |
| 2037 | 4822 122 33007 | 330 nF | 25 V |
| 2039 | 4822 122 33007 | 330 nF | 25 V |
| 2046 | 4822 122 32927 | 220 nF |  |
| 2047 | 4822 122 32927 | 220 nF |  |
| 2048 | 5322 124 21711 | 100 μF | 25 V |
| 2049 | 5322 124 10512 | 68 μF | 20% 16 V |
| 2050 | 4822 122 32972 | 1 nF |  |
| 2051 | 4822 122 31783 | 2.7 nF |  |
| 2052 | 4822 122 31965 | 220 pF |  |
| 2053 | 4822 122 31774 | 56 pF |  |
| 2054 | 4822 122 31767 | 150 pF |  |
| 2055 | 4822 122 32442 | 10 nF |  |
| 2056 | 4822 122 31783 | 2.7 nF |  |
| 2057 | 5322 122 31647 | 1 nF |  |
| 2058 | 4822 122 31783 | 2.7 nF |  |
| 2059 | 4822 122 31965 | 220 pF |  |
| 2060 | 4822 122 31774 | 56 pF |  |
| 2061 | 4822 122 31767 | 150 pF |  |
| 2062 | 4822 122 32442 | 10 nF |  |
| 2064 | 4822 122 31783 | 2.7 nF |  |
| 2065 | 5322 124 10512 | 68 μF | 20% 16 V |
| 2066 | 5322 124 21749 | 10 μF | 63 V |
| 2069 | 5322 124 21749 | 10 μF | 63 V |

## Modification levels

The module shipped at level 2 and went to level 3 during production. At level 3
IC6203 and R3112/R3113/R3114 came out and were replaced by transistors
TS6112/TS6113 with R3075 and R3053 — an availability change that also improved
the signal-to-noise ratio and cost less.

Full table, with service code numbers:
[chapter 8, module A](../../service-information/modification-levels.md#mod-a).

## Related

- [Module circuit descriptions](../../circuit-description/modules.md#module-a) — the chapter 7 text in full
- [Modification levels per module](../../service-information/modification-levels.md#mod-a) — what changed at level 3
- [Adjustments](../../general-service/adjustments.md) — the general adjustment rules
- [VP400 series architecture](../../circuit-description/vp400-series.md) — where the audio path sits in the player
- [Module and connector lay-out](../../system/module-layout.md) — connector positions
- [Electrical parts](../../parts/electrical-parts.md) — the collective list of standard components by service code number; the connectors are in [mechanical parts](../../parts/mechanical-parts.md#module-connectors)
