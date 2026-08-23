---
title: Module K - HF processor
description: >-
  HF processing of the raw signal off the disc.
---

# Module K - HF processor

HF processing of the raw signal off the disc.

## Overview

The HF processor is where the signal read off the disc is split in two. The HF
from the deck goes to a video section — high-pass filtered, frequency-response
corrected under the `MTF` voltage, then demodulated — and to an audio section,
where a low-pass filter takes out the FM audio carriers.

The frequency-response correction matters: the read-out diameter of the disc
changes the response of the pick-up, so `MTF` adapts for it.

| | |
| --- | --- |
| Designation | **K** — HF processor |
| Modification levels | 0 (unchanged through production) |
| Data sheet | `CS 7 847`, page 054 |
| Circuit diagram | `CS 6 877`, page 055 |
| Connectors | `K1`, `K2` |
| Out | `CV-DEM` on `6K2`, to [video drop-out correction module L](../l-video-dropout-correction/index.md) · `HF-AUD` on `1K1`, to [ETBC B module H](../h-etbc-b/index.md) |

## The board

<div class="sheet-pair" markdown>
<figure class="sheet sheet--photo" markdown>
[![Module K, component side of the board](assets/web/k-hf-processor-top-preview.webp)](assets/web/k-hf-processor-top-zoom.webp)
<figcaption>
  Module K, component side.
</figcaption>
</figure>
<figure class="sheet sheet--photo" markdown>
[![Module K, solder side of the board](assets/web/k-hf-processor-bottom-preview.webp)](assets/web/k-hf-processor-bottom-zoom.webp)
<figcaption>
  Module K, solder side.
</figcaption>
</figure>
</div>

## Where it sits in the player

Second of the four boards in the right-hand cage, between
[J](../j-focus/index.md) and
[L](../l-video-dropout-correction/index.md) — see the
[module and connector lay-out](../../system/module-layout.md).

## Circuit description

The HF signal is first filtered by the LC circuit 5003, 2014 and 2015. The
**video** path is taken from the collector of 7005, high-pass filtered above
2 MHz by 2004, 2005, 2006 and 5001, and amplified by 7002, 7003 and 7004. In
7002's collector circuit sits an LC circuit tuned to 8 MHz which is damped more
or less according to the `MTF` signal through 7001 — that is the
frequency-response adaptation. IC7201-2A demodulates the result, with the
output amplitude set by **R3043**; pin 16 carries demodulated video, and after
a < 5 MHz low-pass filter and IC7201-2B the composite video `CV-DEM` leaves on
`6K2`.

The **audio** path is taken from the emitter of 7005 through the feedback
amplifier 7006, 7007, 7008, with a < 2 MHz low-pass filter in 7006's collector
(5004 with 2019, 2020 and 2021). `HF-AUD` leaves on `1K1`.

The full text is in
[chapter 7, module K](../../circuit-description/modules.md#module-k).

## Adjustments

Two adjustments: the video amplitude, and three filter dips that need an HF
generator.

!!! info "Required"

    Test disc · scope · HF generator (100 kHz – 10 MHz)

    Load the test disc; still picture, picture no. 6200.

**1) R3043 — video amplitude**

- Measure `CVBS OUT` on `BNC3` at the rear with the scope, 75 Ω terminated.
- Press switch `SK2` on [analog I/O module U](../u-analog-io/index.md) to the
  **NOT ENCODED** position.
- Adjust R3043 until the signal is **1 Vpp ± 50 mV**.
- Return `SK2` to its earlier position.

**2) L5001, L5002, L5004 — audio dip 0.875 MHz, MTF, audio dip 2.8 MHz**

- Switch the drive into **STANDBY**.
- Connect an HF generator signal of 0.8 Vpp to `3K2`.
- Measure on pin 5 of IC7201-2A with the scope.
- Set the generator to **875 kHz** and adjust **L5001** for minimum amplitude.
- Set the generator to **8 MHz** at 40 mV and adjust **L5002** for maximum
  amplitude.
- Move the scope to `1K1` (`HF-AUD`).
- Set the generator to **2.8 MHz** at 20 mV and adjust **L5004** for minimum
  amplitude.

**Adjustment when an item is replaced**

| Replaced | Adjust |
| --- | --- |
| IC7201 | R3043 |

!!! important "Replacing the whole module"

    Module K is one of the four modules that must be adjusted even when the
    board is swapped complete: adjust **R3043** (video amplitude). See
    [adjustments](../../general-service/adjustments.md).

## Circuit diagram

<figure class="sheet sheet--fold" markdown>
[![HF processor module K - circuit diagram](assets/web/cs-6-877-circuit-p055-preview.webp)](assets/web/cs-6-877-circuit-p055-zoom.webp)
<figcaption>
  HF processor module K - circuit diagram.
  <span class="cs">CS 6 877</span>
  <span class="src">service manual page 055</span>
</figcaption>
</figure>

## PCB lay-out

<figure class="sheet sheet--fold" markdown>
[![HF processor module K (mod level 0) - adjustments / PCB / parts](assets/web/cs-7-847-module-sheet-p054-preview.webp)](assets/web/cs-7-847-module-sheet-p054-zoom.webp)
<figcaption>
  HF processor module K (mod level 0) - adjustments / PCB / parts.
  <span class="cs">CS 7 847</span>
  <span class="src">service manual page 054</span>
</figcaption>
</figure>

## List of electrical parts

**Coils**

| Item | Service code number | Value | Rating |
| --- | --- | --- | --- |
| 5001 | 4822 156 10994 | 87 μH |  |
| 5002 | 4822 156 21147 | 7.2 μH |  |
| 5003 | 4822 156 11011 | 2.6 μH |  |
| 5004 | 4822 156 10994 | 87 μH |  |
| 5005 | 4822 156 10999 | 4.2 μH |  |
| 5006 | 4822 156 21026 | 34 μH |  |
| 5007 | 4822 157 52871 | 25 μH |  |
| 5008 | 4822 157 52871 | 25 μH |  |

**Potentiometers**

| Item | Service code number | Value | Rating |
| --- | --- | --- | --- |
| 3043 | 5322 101 10481 | 1 kΩ |  |

**Fuse Resistors**

| Item | Service code number | Value | Rating |
| --- | --- | --- | --- |
| 3041 | 4822 111 30847 | 22 Ω |  |

**Capacitors**

| Item | Service code number | Value | Rating |
| --- | --- | --- | --- |
| 2001 | 4822 122 31759 | 22 nF |  |
| 2002 | 4822 124 22027 | 47 μF | 25 V |
| 2003 | 4822 122 31759 | 22 nF |  |
| 2004 | 4822 122 33002 | 68 pF |  |
| 2005 | 4822 122 31727 | 470 pF |  |
| 2006 | 4822 122 31839 | 82 pF |  |
| 2007 | 4822 122 32442 | 10 nF |  |
| 2008 | 4822 122 31759 | 22 nF |  |
| 2009 | 4822 122 31774 | 56 pF |  |
| 2010 | 4822 122 32506 | 5.6 pF |  |
| 2011 | 4822 122 31759 | 22 nF |  |
| 2012 | 4822 122 32442 | 10 nF |  |
| 2013 | 4822 122 31759 | 22 nF |  |
| 2014 | 4822 122 31839 | 82 pF |  |
| 2015 | 4822 122 32974 | 100 pF |  |
| 2016 | 4822 122 31965 | 220 pF |  |
| 2017 | 4822 122 32142 | 270 pF |  |
| 2018 | 4822 122 31759 | 22 nF |  |
| 2019 | 4822 122 31965 | 220 pF |  |
| 2020 | 4822 122 31772 | 47 pF |  |
| 2021 | 4822 122 32976 | 470 pF |  |
| 2022 | 4822 122 31759 | 22 nF |  |
| 2023 | 4822 124 22027 | 47 μF | 25 V |
| 2024 | 4822 122 32442 | 10 nF |  |
| 2025 | 4822 122 31774 | 56 pF |  |
| 2026 | 4822 122 31774 | 56 pF |  |
| 2027 | 4822 124 22027 | 47 μF | 25 V |
| 2028 | 4822 122 31759 | 22 nF |  |
| 2029 | 4822 122 31644 | 2.2 nF |  |
| 2030 | 4822 122 31759 | 22 nF |  |
| 2031 | 4822 122 31759 | 22 nF |  |
| 2032 | 4822 122 31769 | 18 pF |  |
| 2033 | 4822 122 31769 | 18 pF |  |
| 2034 | 4822 122 31759 | 22 nF |  |
| 2035 | 4822 122 32975 | 33 pF |  |
| 2036 | 4822 122 32505 | 2.7 pF |  |
| 2037 | 4822 122 31774 | 56 pF |  |
| 2038 | 4822 122 32504 | 15 pF |  |
| 2039 | 4822 122 31774 | 56 pF |  |
| 2040 | 4822 122 32139 | 12 pF |  |
| 2041 | 4822 122 31966 | 27 pF |  |
| 2042 | 4822 124 22027 | 47 μF | 25 V |
| 2043 | 5322 122 32072 | 33 pF |  |

## Modification levels

The survey records module K at **level 0 in every production batch**, but the
chapter 8 sheet documents a level-1 change: R3015 470 Ω → 120 Ω, to stop the
HF amplifier limiting at maximum resonant rise.

Full table, with service code numbers:
[chapter 8, module K](../../service-information/modification-levels.md#mod-k).

## Related

- [Module circuit descriptions](../../circuit-description/modules.md#module-k) — the chapter 7 text in full
- [Adjustments](../../general-service/adjustments.md) — R3043 must be set after a module swap
- [Fault symptoms](../../service-information/fault-symptoms.md) — this module appears in the playability entries
- [Modification levels per module](../../service-information/modification-levels.md#mod-k) — the level-1 change
- [Module L — Video drop-out correction](../l-video-dropout-correction/index.md) — takes `CV-DEM` from here
- [The LaserVision system](../../circuit-description/laservision-system.md) — what is on the HF signal in the first place
