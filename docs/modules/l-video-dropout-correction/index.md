---
title: Module L - Video drop-out correction
description: >-
  Video drop-out detection and correction.
---

# Module L - Video drop-out correction

Video drop-out detection and correction.

## Overview

Two jobs on one board: **drop-out compensation** of the demodulated video, and
generation of the **`MTF` signal**.

When the drop-out detector sees a negative-going drop-out it throws the DO
switch, so the output becomes the video delayed by one line time (64 μs) in a
CCD memory — and stays there for as long as the drop-out lasts. Only the
luminance signal is corrected. `DO-INH` blocks the drop-out pulses, which is
needed so that correction does not happen during the data part of the video
signal.

`MTF` is a DC voltage that varies with the read-out diameter of the disc; it
goes to [HF processor module K](../k-hf-processor/index.md) to adapt the
frequency response of the HF signal.

| | |
| --- | --- |
| Designation | **L** — video drop-out correction |
| Modification levels | 0 → 1 |
| Data sheet | `CS 7 848`, page 057 |
| Circuit diagram | `CS 6 878`, page 056 |
| Connectors | `L1`, `L2` |
| In | `CV-DEM` on `1L1`, from [module K](../k-hf-processor/index.md) · `DO-INH` from [genlock module G](../g-genlock/index.md) |
| Out | `CV-DOC` on `1L2`, to [ETBC B module H](../h-etbc-b/index.md) · `MTF` back to module K |
| Delay line | 5001 DL470NS — 470 ns; the 64 μs line delay is the CCD |

## The board

<div class="sheet-pair" markdown>
<figure class="sheet sheet--photo" markdown>
[![Module L, component side of the board](assets/web/l-video-dropout-correction-top-preview.webp)](assets/web/l-video-dropout-correction-top-zoom.webp)
<figcaption>
  Module L, component side.
</figcaption>
</figure>
<figure class="sheet sheet--photo" markdown>
[![Module L, solder side of the board](assets/web/l-video-dropout-correction-bottom-preview.webp)](assets/web/l-video-dropout-correction-bottom-zoom.webp)
<figcaption>
  Module L, solder side.
</figcaption>
</figure>
</div>

## Where it sits in the player

Third of the four boards in the right-hand cage, between
[K](../k-hf-processor/index.md) and [M](../m-radial/index.md) — see the
[module and connector lay-out](../../system/module-layout.md).

## Circuit description

**Direct video.** `CV-DEM` from [module K](../k-hf-processor/index.md) arrives
on `1L1` at the base of 7001, goes from its emitter through the 470 ns delay
line 5001 to amplifier 7002/7003, and through emitter follower 7004 to drop-out
switch IC7201-2A. With no drop-out, the video passes emitter follower 7005 and
leaves on `1L2`.

**Drop-out detection.** IC7202, wired as a comparator, watches the demodulated
video through emitter follower 7006. Its output sits high at +12 V normally
and falls when the input drops below the reference — that transition is the
drop-out pulse which throws the switch to the delayed video.

The full text, including the DC restorer and the `MTF` generator, is in
[chapter 7, module L](../../circuit-description/modules.md#module-l).

## Adjustments

Two adjustments, one of them judged **by eye on the screen** rather than on a
scope.

!!! info "Required"

    Scope · test disc

    Load the test disc; still picture, picture no. 10800.

**1) R3065, L5007 — delay 64 μs**

Picture no. 10800 shows the drop-out test pattern (Fig. L1 on the sheet): a
still frame with drop-outs of 10 μs on line 44, 64 μs on line 132 and 20 μs on
line 200, over a greyscale.

- Adjust **L5007** until drop-out **A** gives a white completion of the
  vertical lines at the right place, and drop-out **B** gives minimum
  distortion at the place indicated.
- Adjust **R3065** until drop-out **B** is invisible and drop-out **C** causes
  a black line without white stripes or dots.

**2) L5003, R3050 — MTF**

- Search for picture no. 1000 (blue).
- Measure `CVBS OUT` on `BNC3` at the rear, 75 Ω terminated, triggered line
  frequent.
- Press switch `SK2` on [analog I/O module U](../u-analog-io/index.md) to the
  **NOT ENCODED** position.
- Adjust **L5003** for minimum amplitude of the chroma signal.
- Still on `BNC3`, find the multi-burst signal in the VITS on **line 20** using
  the delayed timebase (Fig. L2 on the sheet).
- Adjust **R3050** until the amplitude of `MBI` equals `MBIV`.

**Adjustment when an item is replaced**

| Replaced | Adjust |
| --- | --- |
| Components in the clock generator | L5007 |
| IC7203 | R3065, R3050 |

!!! important "Replacing the whole module"

    Module L is one of the four modules that must be adjusted even when the
    board is swapped complete: adjust **R3050** (`MTF`). See
    [adjustments](../../general-service/adjustments.md), which also points at
    adjustment 2 above for checking the VITS signals after replacing module H,
    K, L or Z.

## Circuit diagram

<figure class="sheet sheet--fold" markdown>
[![Video drop-out correction module L - circuit diagram](assets/web/cs-6-878-circuit-p056-preview.webp)](assets/web/cs-6-878-circuit-p056-zoom.webp)
<figcaption>
  Video drop-out correction module L - circuit diagram.
  <span class="cs">CS 6 878</span>
  <span class="src">service manual page 056</span>
</figcaption>
</figure>

## PCB lay-out

<figure class="sheet sheet--fold" markdown>
[![Video drop-out correction module L (mod level 0) - adjustments / PCB / parts](assets/web/cs-7-848-module-sheet-p057-preview.webp)](assets/web/cs-7-848-module-sheet-p057-zoom.webp)
<figcaption>
  Video drop-out correction module L (mod level 0) - adjustments / PCB / parts.
  <span class="cs">CS 7 848</span>
  <span class="src">service manual page 057</span>
</figcaption>
</figure>

## List of electrical parts

**Delay lines**

| Item | Service code number | Value | Rating |
| --- | --- | --- | --- |
| 5001 | 4822 320 40081 | DL470NS |  |

**Coils**

| Item | Service code number | Value | Rating |
| --- | --- | --- | --- |
| 5002 | 4822 157 52869 | 34 μH |  |
| 5003 | 4822 156 11003 | 12 μH |  |
| 5004 | 4822 156 11007 | 212 μH |  |
| 5005 | 4822 156 11007 | 212 μH |  |
| 5006 | 4822 156 21324 | 100 μH |  |
| 5007 | 4822 156 10997 | 1.7 μH |  |

**Potentiometers**

| Item | Service code number | Value | Rating |
| --- | --- | --- | --- |
| 3050 | 4822 100 11087 | 2.2 kΩ |  |
| 3065 | 4822 100 20151 | 1 kΩ |  |

**Capacitors**

| Item | Service code number | Value | Rating |
| --- | --- | --- | --- |
| 2001 | 4822 122 32082 | 4.7 μF |  |
| 2002 | 4822 124 22027 | 47 μF | 25 V |
| 2003 | 4822 122 31759 | 22 nF |  |
| 2004 | 5322 124 21749 | 10 μF | 63 V |
| 2005 | 5322 124 21749 | 10 μF | 63 V |
| 2006 | 4822 121 41608 | 100 nF | 100 V |
| 2007 | 4822 122 31759 | 22 nF |  |
| 2008 | 4822 122 31759 | 22 nF |  |
| 2009 | 4822 122 32975 | 470 pF |  |
| 2010 | 4822 122 32974 | 100 pF |  |
| 2011 | 4822 122 31759 | 22 nF |  |
| 2012 | 4822 122 31839 | 82 pF |  |
| 2013 | 5322 122 31847 | 1 nF |  |
| 2014 | 4822 122 31759 | 22 nF |  |
| 2015 | 4822 124 22027 | 47 μF | 25 V |
| 2016 | 4822 124 22029 | 2.2 μF | 63 V |
| 2017 | 4822 122 32974 | 100 pF |  |
| 2018 | 4822 122 32974 | 100 pF |  |
| 2019 | 4822 122 31759 | 22 nF |  |
| 2020 | 4822 121 41719 | 1 μF | 10% 100 V |
| 2021 | 4822 122 32442 | 10 nF |  |
| 2022 | 4822 122 32442 | 10 nF |  |
| 2023 | 4822 122 31759 | 22 nF |  |
| 2024 | 4822 124 22031 | 4.7 μF | 63 V |
| 2025 | 4822 124 22028 | 1 μF | 63 V |
| 2026 | 4822 122 31759 | 22 nF |  |
| 2027 | 4822 121 41608 | 100 nF | 100 V |
| 2028 | 4822 122 32974 | 100 pF |  |
| 2029 | 4822 122 32974 | 100 pF |  |
| 2030 | 4822 122 31759 | 22 nF |  |
| 2031 | 4822 124 22027 | 47 μF | 25 V |
| 2032 | 4822 121 41785 | 270 nF | 10% 100 V |
| 2033 | 4822 122 31759 | 22 nF |  |
| 2034 | 4822 122 32482 | 22 pF |  |
| 2035 | 4822 122 31759 | 22 nF |  |
| 2036 | 4822 122 31759 | 22 nF |  |
| 2037 | 4822 122 31759 | 22 nF |  |
| 2038 | 4822 122 31839 | 82 pF |  |
| 2039 | 4822 122 31759 | 22 nF |  |

## Modification levels

The module shipped at level 0 and went to level 1 in the second production
batch, with two changes:

- R3096 470 Ω → 560 Ω, adapting the video amplitudes.
- R3046 3k3 → 2k7, because the `MTF` regulation was not good enough.

Full tables, with service code numbers:
[chapter 8, module L](../../service-information/modification-levels.md#mod-l).

## Related

- [Module circuit descriptions](../../circuit-description/modules.md#module-l) — the chapter 7 text in full
- [Adjustments](../../general-service/adjustments.md) — R3050 must be set after a module swap
- [Error 9 — frame lock](../../repair/case-studies/error-9-frame-lock.md) — a worked investigation in which this module is a candidate
- [Fault symptoms](../../service-information/fault-symptoms.md) — the playability entries reach this module
- [Module K — HF processor](../k-hf-processor/index.md) — sends `CV-DEM`, receives `MTF`
- [Module H — ETBC B](../h-etbc-b/index.md) — takes `CV-DOC` from here
