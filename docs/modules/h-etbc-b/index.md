---
title: Module H - ETBC-B
description: >-
  ETBC-B, the first half of the electronic timebase corrector.
search:
  boost: 2
---

# Module H - ETBC-B

ETBC-B, the first half of the electronic timebase corrector.

## Overview

ETBC B is half of the **electronic time-base correction** system — the half
that does the correcting. It carries two CCD delay lines for coarse correction
(**± 17 μs**) and two variable LC delay lines for fine correction
(**± 50 ns**), and it treats video and audio in parallel: IC7201 is the video
CCD, IC7203 the audio CCD.

Correction is needed because disc, centring and motor tolerances shift the line
phase of the video read off the disc by as much as ± 17 μs against the
reference. Earlier players corrected that mechanically, with a tangential
mirror; the VP415 has no tangential mirror and does it electronically instead.

| | |
| --- | --- |
| Designation | **H** — ETBC B |
| Modification levels | 5 (unchanged through production) |
| Data sheet | `CS 7 844`, page 049 |
| Circuit diagram | `CS 6 874`, page 048 |
| Connectors | `H1`, `H2` |
| In | `CV-DOC` from [video drop-out correction module L](../l-video-dropout-correction/index.md) · `HFAUD` |
| Out | `CV-TBC` to [video processor module C](../c-video-processor/index.md) · `HFATBC` to [audio processor module A](../a-audio-processor/index.md) |
| Controlled by | `TANG-ER` and `BURST-ER`, both from [ETBC C module I](../i-etbc-c/index.md) |

## The board

<div class="sheet-pair" markdown>
<figure class="sheet sheet--photo" markdown>
[![Module H, component side of the board](assets/web/h-etbc-b-top-preview.webp)](assets/web/h-etbc-b-top-zoom.webp)
<figcaption>
  Module H, component side.
</figcaption>
</figure>
<figure class="sheet sheet--photo" markdown>
[![Module H, solder side of the board](assets/web/h-etbc-b-bottom-preview.webp)](assets/web/h-etbc-b-bottom-zoom.webp)
<figcaption>
  Module H, solder side.
</figcaption>
</figure>
</div>

## Where it sits in the player

Lying flat across the front of the chassis, between
[G](../g-genlock/index.md) and [I](../i-etbc-c/index.md) — see the
[module and connector lay-out](../../system/module-layout.md).

## Circuit description

`CV-DOC` arrives on `2H2` and passes emitter follower T7013 and a ≤ 6.6 MHz
low-pass filter — needed to keep the CCD from aliasing — into CCD memory
IC7201. How long the CCD delays the signal depends on its clock rate, and the
clock oscillator on pin 14 is a VCO (IC7206) driven by `TANG-ER`, the measured
time error generated on [ETBC C module I](../i-etbc-c/index.md) and arriving
here on `4H1`. Since `TANG-ER` is a measure of the error and also sets the
delay, the two modules close a loop around the time base.

The corrected video leaves as `CV-TBC` for
[video processor module C](../c-video-processor/index.md); the audio path does
the same job on `HFAUD` through IC7203 and leaves as `HFATBC`.

The full text is in
[chapter 7, module H](../../circuit-description/modules/h-etbc-b.md).

## Adjustments

Five adjustments — CCD delay, CCD level, video amplitude and the two
time-error trims.

!!! info "Required"

    Test disc · scope · DC supply

    Load the test disc; still picture, colour bar (picture no. 6200).

**1) R3012, R3013 — CCD pass-through, limiter frequency sweep**

- Measure `CV-DOC` on `2H2` (A channel) and `CV-TBC` on `2H1` (B channel).
- Short-circuit C2003 (pin 9 of IC7206 to ground).
- Display the first lines of the video signal using the delayed timebase.
- Adjust R3012 for a delay of **70 μs ± 1 μs** between the two signals.
- Remove the short circuit on C2003.
- Connect the DC supply as a variable voltage to the junction of R3001, R3002
  and C2001 (`TANG-ER`).
- Measure the delay between `CV-DOC` and `CV-TBC` as a function of that
  voltage:

    | `TANG-ER` | Delay |
    | --- | --- |
    | 0 V | 46 μs ± 1.5 μs |
    | +3 V | 70 μs ± 1 μs |
    | +5 V | 91 μs ± 1.5 μs |

- Correct deviations with R3013.

**2) R3063 — CCD adjust**

- Search for picture no. 470 (white).
- Measure `CV-TBM` on pin 1 of IC7201 with the scope.
- Adjust R3063 for a black-level amplitude of **3.2 Vpp**. Fig. H1 on the sheet
  shows the `CV-TBM` signal on `7H1`, with top white, black level, sync bottom,
  colour burst and special burst marked.

**3) R3087 — video adjust**

- Measure `CVBS OUT` on `BNC3` at the rear with the scope, 75 Ω terminated.
- Press switch `SK2` on [analog I/O module U](../u-analog-io/index.md) to the
  **NOT ENCODED** position.
- Adjust R3087 for a CVBS amplitude (top white to sync bottom) of **1 Vpp**.
- Return `SK2` to its earlier position.

**4) R3134 — video time errors**

- Search picture no. 1000 (blue) and adjust R3134 for minimum dark bars.
- Search picture no. 1800 (yellow) and adjust R3134 for minimum red stripes.
- Repeat if necessary.

**5) R3122 — audio time errors**

- Put the player into normal play with sound modulation.
- Measure the AC signal on the emitter of TS7029 and adjust R3122 for minimum
  AC.

!!! warning "Adjustment 5 may not apply to your board"

    One of the level-5 changes deletes the audio correction circuit, TS7029
    among the parts removed. If the transistor is not on the board, this
    adjustment has gone with it. Check before you go looking for it.

**Adjustment when an item is replaced**

| Replaced | Adjust |
| --- | --- |
| IC7201 | R3063, R3087 |
| IC7206 | R3012, R3013 |

## Circuit diagram

<figure class="sheet sheet--fold" markdown>
[![ETBC-B module H - circuit diagram](assets/web/cs-6-874-circuit-p048-preview.webp)](assets/web/cs-6-874-circuit-p048-zoom.webp)
<figcaption>
  ETBC-B module H - circuit diagram.
  <span class="cs">CS 6 874</span>
  <span class="src">service manual page 048</span>
</figcaption>
</figure>

## PCB lay-out

<figure class="sheet sheet--fold" markdown>
[![ETBC-B module H (mod level 5) - adjustments / PCB / parts](assets/web/cs-7-844-module-sheet-p049-preview.webp)](assets/web/cs-7-844-module-sheet-p049-zoom.webp)
<figcaption>
  ETBC-B module H (mod level 5) - adjustments / PCB / parts.
  <span class="cs">CS 7 844</span>
  <span class="src">service manual page 049</span>
</figcaption>
</figure>

## List of electrical parts

**Coils**

| Item | Service code number | Value | Rating |
| --- | --- | --- | --- |
| 5001 | 4822 156 11002 | 7.7 μH |  |
| 5002 | 4822 156 10998 | 3 μH |  |
| 5003 | 4822 156 11001 | 6 μH |  |
| 5004 | 4822 156 11001 | 6 μH |  |
| 5005 | 4822 156 11001 | 6 μH |  |
| 5006 | 4822 156 11001 | 6 μH |  |
| 5007 | 4822 156 11001 | 6 μH |  |
| 5008 | 4822 156 10998 | 3 μH |  |
| 5009 | 4822 156 11004 | 26.5 μH |  |
| 5010 | 4822 156 11006 | 54 μH |  |
| 5011 | 4822 156 11004 | 26.5 μH |  |

**Potentiometers**

| Item | Service code number | Value | Rating |
| --- | --- | --- | --- |
| 3012 | 5322 101 10627 | 10 kΩ |  |
| 3013 | 5322 101 10628 | 22 kΩ |  |
| 3063 | 4822 100 20151 | 1 kΩ |  |
| 3087 | 4822 100 10254 | 1 kΩ |  |
| 3122 | 5322 101 10628 | 22 kΩ |  |
| 3134 | 5322 101 10628 | 22 kΩ |  |

**Fuse Resistors**

| Item | Service code number | Value | Rating |
| --- | --- | --- | --- |
| 3137 | 4822 111 10165 | 10Ω |  |
| 3138 | 4822 111 10165 | 10Ω |  |

**Capacitors**

| Item | Service code number | Value | Rating |
| --- | --- | --- | --- |
| 2001 | 4822 121 41874 | 270 nF | 63 V |
| 2002 | 4822 122 32541 | 27 nF |  |
| 2003 | 4822 122 31916 | 5.6 nF |  |
| 2004 | 4822 122 31971 | 10 pF |  |
| 2005 | 4822 122 31759 | 22 nF |  |
| 2006 | 5322 124 21643 | 22 μF | 40 V |
| 2007 | 4822 124 22027 | 47 μF | 25 V |
| 2008 | 4822 122 31759 | 22 nF |  |
| 2009 | 4822 122 31767 | 150 pF |  |
| 2010 | 4822 122 31767 | 150 pF |  |
| 2011 | 4822 124 22027 | 47 μF | 25 V |
| 2012 | 5322 122 32839 | 100 nF |  |
| 2013 | 4822 121 41719 | 1 μF | 10% 100 V |
| 2014 | 5322 122 32839 | 100 nF |  |
| 2015 | 5322 124 21749 | 10 μF | 63 V |
| 2016 | 4822 122 32442 | 10 nF |  |
| 2017 | 4822 124 22188 | 3.3 μF | 63 V |
| 2018 | 4822 122 32442 | 10 nF |  |
| 2019 | 5322 122 32839 | 100 nF |  |
| 2020 | 5322 122 32839 | 100 nF |  |
| 2021 | 5322 124 21643 | 22 μF | 40 V |
| 2022 | 5322 124 21643 | 22 μF | 40 V |
| 2023 | 4822 124 22188 | 3.3 μF | 63 V |
| 2024 | 5322 124 21749 | 10 μF | 63 V |
| 2025 | 4822 122 32442 | 10 nF |  |
| 2026 | 5322 124 21749 | 10 μF | 63 V |
| 2027 | 5322 124 21749 | 10 μF | 63 V |
| 2028 | 4822 122 32442 | 10 nF | PCB 3/1/64 |
| 2029 | 4822 124 22027 | 47 μF | 25 V |
| 2030 | 5322 122 31647 | 1 nF |  |
| 2031 | 5322 124 21643 | 22 μF | 40 V |
| 2032 | 4822 124 22027 | 47 μF | 25 V |
| 2033 | 4822 124 22027 | 47 μF | 25 V |
| 2034 | 5322 124 21643 | 22 μF | 40 V |
| 2035 | 4822 122 31759 | 22 nF |  |
| 2036 | 5322 124 21643 | 22 μF | 40 V |
| 2037 | 4822 124 22027 | 47 μF | 25 V |
| 2038 | 4822 124 22027 | 47 μF | 25 V |
| 2040 | 4822 124 22027 | 47 μF | 25 V |
| 2042 | 4822 124 22027 | 47 μF | 25 V |
| 2043 | 4822 124 22027 | 47 μF | 25 V |
| 2044 | 4822 122 31759 | 22 nF |  |
| 2045 | 5322 124 21749 | 10 μF | 63 V |
| 2046 | 4822 122 31759 | 22 nF |  |
| 2047 | 4822 122 31759 | 22 nF |  |
| 2050 | 4822 122 32142 | 270 pF |  |
| 2051 | 4822 122 31759 | 22 nF |  |
| 2052 | 4822 122 31759 | 22 nF |  |
| 2053 | 4822 124 22028 | 1 μF | 63 V |
| 2054 | 5322 122 32839 | 130 nF |  |
| 2055 | 5322 124 21643 | 22 μF | 40 V |
| 2057 | 4822 122 31759 | 22 nF |  |
| 2057 | 5322 124 21643 | 22 μF | 40 V |
| 2058 | 4822 122 31759 | 22 nF |  |

## Modification levels

Module H is at **level 5 in every production batch**, but the chapter 8 sheet
still records four changes made within that level:

- R3072 3k4 → 2k4 and C2070 47 pF → 39 pF — a fault in the diagram.
- R3013 22 k potentiometer → 2k2, improving VCO adjustment on CLV discs.
- A large deletion — C2059/2061/2064, R3115–R3125, L5009–L5011, D6013 and
  TS7026/TS7029, with R3127 620 Ω → 22 k and R3130 470 Ω → 1 k — because the
  audio correction was found not to be necessary.
- C2001 270 nF → 220 nF — another fault in the diagram.

Full tables, with service code numbers:
[chapter 8, module H](../../service-information/modification-levels.md#mod-h).

## Related

- [Module H circuit description](../../circuit-description/modules/h-etbc-b.md) — the chapter 7 text in full
- [Module I — ETBC C](../i-etbc-c/index.md) — measures the error this module corrects
- [The LaserVision system](../../circuit-description/laservision-system.md) — why the time base needs correcting at all
- [Modification levels per module](../../service-information/modification-levels.md#mod-h) — the four level-5 changes
- [Adjustments](../../general-service/adjustments.md) — check `CVBS OUT` after replacing this module
- [Electrical parts](../../parts/electrical-parts.md) — the collective list of standard components by service code number; the connectors are in [mechanical parts](../../parts/mechanical-parts.md#module-connectors)
