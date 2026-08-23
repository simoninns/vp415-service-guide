---
title: Module B - RGB
description: >-
  PAL-to-RGB decoding and the RGB TTL output.
---

# Module B - RGB

PAL-to-RGB decoding and the RGB TTL output.

## Overview

The RGB module is the player's colour decoder. It takes the drop-out- and
time-base-corrected composite video from
[video processor module C](../c-video-processor/index.md), splits it into
luminance and chrominance, and decodes it two ways at once: as **R, G and B**
for [video mixer module Y](../y-video-mixer/index.md) by way of
[analog I/O module Ua](../u-analog-io/index.md), and as **Y, R−Y and B−Y** for
the encoder on [analog I/O module Ub](../u-analog-io/index.md).

| | |
| --- | --- |
| Designation | **B** — RGB |
| Modification levels | 5 → 7 |
| Data sheet | `CS 7 838`, pages 035–036 |
| Circuit diagram | `CS 6 868`, page 034 |
| Connectors | `B1`, `B2`, `B3` |
| Key devices | IC7201 multistandard decoder · IC7202 colour transient improver · IC7203 PAL decoder |

## The board

<div class="sheet-pair" markdown>
<figure class="sheet sheet--photo" markdown>
[![Module B, component side of the board](assets/web/b-rgb-top-preview.webp)](assets/web/b-rgb-top-zoom.webp)
<figcaption>
  Module B, component side.
</figcaption>
</figure>
<figure class="sheet sheet--photo" markdown>
[![Module B, solder side of the board](assets/web/b-rgb-bottom-preview.webp)](assets/web/b-rgb-bottom-zoom.webp)
<figcaption>
  Module B, solder side.
</figcaption>
</figure>
</div>

## Where it sits in the player

Second of the four boards in the left-hand cage, between
[A](../a-audio-processor/index.md) and
[C](../c-video-processor/index.md) — see the
[module and connector lay-out](../../system/module-layout.md).

## Circuit description

The incoming CVBS on `1B1` is filtered on the emitter of T7001, so that the
luminance signal Y appears on the emitter of T7002 with its amplitude set by
R3080; band-pass filtering through L5004 and C2005 puts the chrominance signal
on pin 15 of IC7201.

IC7201 decodes chroma into R−Y and B−Y, using the 8.86 MHz crystal 5005 for
sub-carrier regeneration. IC7202 sharpens the colour transitions — the colour
transient improver — with the amplitudes of (R−Y) and (B−Y) set by R3082 and
R3084; because improving the transient costs time, the Y signal is delayed to
match inside the same IC. Those three signals leave for
[module Ub](../u-analog-io/index.md) on `10B3`, `9B2` and `10B2`.

In parallel, IC7203 decodes luminance and chrominance to R, G and B, which
leave through output stages T7006, T7008 and T7010 on `2B3`, `3B3` and `4B3`.
R3045 sets their DC level, referenced to the black level of the video signal.

The full text is in
[chapter 7, module B](../../circuit-description/modules.md#module-b).

## Adjustments

Seven adjustments — the longest procedure of any module in the player.

!!! info "Required"

    Test disc · dual-beam scope with X-deflection via the B channel, or a
    vector scope if one is available.

    Load the test disc; still picture, colour pattern (picture no. 6200).

**1) L5002 and L5003 — notch filter**

- Measure the luminance signal on `10B3` with the scope, line triggered
  (Fig. B1 on the sheet).
- Adjust L5002 until the chroma rests in the luminance signal have disappeared.
- Adjust L5003 until overshoot *a* and undershoot *b* have the same amplitude.

**2) L5004 — bandpass**

- Measure the chroma signal on pin 15 of IC7201 with the scope.
- Adjust L5004 for minimum overshoot in the chroma signal.

**3) R3015 and L5007 — delay line**

- Measure the (R−Y) signal at `9B2` on the A channel and the (B−Y) signal on
  `10B2` on the B channel, both AC coupled.
- Switch the scope to X-deflection and adjust until the vector diagram appears
  (Fig. B2 on the sheet). The colour spots lie at a distance **B** from the
  origin O.
- Short-circuit pins 1–2 or 3–4 of delay line L5008: the spots move in to a
  distance **A**. Removing the short moves them back out to **B**.
- Adjust L5007 until the spots (at **B**) are as small as possible.
- Adjust R3015 until OB is twice OA, alternately shorting the delay line.

**4) C2015 — oscillator frequency**

- Connect the scope as in 3).
- Short-circuit pins 1–2 or 3–4 of delay line L5008.
- Adjust C2015 until the colour spots of the vector diagram are minimal.

**5) R3080 — luminance signal amplitude**

- Measure the G signal on `3B3` at line frequency (Fig. B3 on the sheet).
- Adjust R3080 for an average amplitude of **700 mV ± 7 mV**.

**6) R3082, R3084 — colour difference signal amplitude**

- Measure the R signal on `2B3` and adjust R3082 to the same amplitude for
  yellow, magenta and red.
- Measure the B signal on `4B3` and adjust R3084 to the same amplitude for
  cyan, magenta and blue (Fig. B3).

**7) R3045 — black level**

- Measure the output B signal on `4B3`.
- Adjust R3045 for a black level of **0 V ± 50 mV** (Fig. B3).

**Adjustment when an item is replaced**

| Replaced | Adjust |
| --- | --- |
| IC7201 | R3015, R3082, R3084, C2015, L5006, L5007 |
| IC7202 | R3080 |
| IC7203 | R3055, R3080, R3082, R3084 |
| R3080 | R3207 — *on [analog I/O module U](../u-analog-io/index.md)* |
| R3082 | R3305 — *on [analog I/O module U](../u-analog-io/index.md)* |
| R3084 | R3315 — *on [analog I/O module U](../u-analog-io/index.md)* |

## Circuit diagram

<figure class="sheet sheet--fold" markdown>
[![RGB module B - circuit diagram](assets/web/cs-6-868-circuit-p034-preview.webp)](assets/web/cs-6-868-circuit-p034-zoom.webp)
<figcaption>
  RGB module B - circuit diagram.
  <span class="cs">CS 6 868</span>
  <span class="src">service manual page 034</span>
</figcaption>
</figure>

## PCB lay-out

<figure class="sheet sheet--fold" markdown>
[![RGB module B (mod level 5) - adjustments / PCB / parts](assets/web/cs-7-838-module-sheet-p035-036-preview.webp)](assets/web/cs-7-838-module-sheet-p035-036-zoom.webp)
<figcaption>
  RGB module B (mod level 5) - adjustments / PCB / parts.
  <span class="cs">CS 7 838</span>
  <span class="src">service manual pages 035, 036</span>
</figcaption>
</figure>

## List of electrical parts

**Crystals**

| Item | Service code number | Value |
| --- | --- | --- |
| 5005 | 4822 242 70304 | 8.867238 MHz |

**Delay lines**

| Item | Service code number | Type |
| --- | --- | --- |
| 5008 | 4822 320 40051 | DL711 |

**Coils**

| Item | Service code number | Value |
| --- | --- | --- |
| 5001 | 4822 156 10993 | 150 μH |
| 5002 | 4822 157 52873 | 5.5 μH |
| 5003 | 4822 157 52875 | 66 μH |
| 5004 | 4822 157 52874 | 12.5 μH |
| 5006 | 4822 156 10995 | 10 μH |
| 5007 | 5322 156 21341 | 10 μH |

**Potentiometers**

| Item | Service code number | Value |
| --- | --- | --- |
| 3015 | 4822 100 10359 | 220 Ω |
| 3045 | 5322 101 14066 | 10 kΩ |
| 3080 | 5322 100 10117 | 2.2 kΩ |
| 3082 | 5322 100 10117 | 2.2 kΩ |
| 3084 | 5322 100 10117 | 2.2 kΩ |

**Trimcapacitors**

| Item | Service code number | Value |
| --- | --- | --- |
| 2015 | 4822 125 50092 | 40 pF |

**Capacitors**

| Item | Service code number | Value | Rating |
| --- | --- | --- | --- |
| 2001 | 4822 124 22027 | 47 μF | 25 V |
| 2002 | 4822 124 22027 | 47 μF | 25 V |
| 2003 | 4822 122 31974 | 820 pF | |
| 2004 | 4822 122 31965 | 220 pF | |
| 2005 | 4822 122 31966 | 27 pF | |
| 2006 | 4822 122 31766 | 120 pF | |
| 2007 | 4822 122 31783 | 2.7 nF | |
| 2008 | 4822 124 22186 | 150 μF | 25 V |
| 2009 | 4822 122 31759 | 22 nF | |
| 2010 | 4822 122 31759 | 22 nF | |
| 2011 | 4822 124 22188 | 3.3 μF | 63 V |
| 2012 | 4822 122 31916 | 5.6 nF | |
| 2013 | 4822 122 32183 | 56 nF | |
| 2014 | 4822 121 42915 | 330 pF | |
| 2015 | 4822 125 50092 | 40 pF | trimmer |
| 2016 | 4822 122 32442 | 10 nF | |
| 2017 | 4822 122 32442 | 10 nF | |
| 2018 | 4822 121 41756 | 330 nF | 10% 63 V |
| 2019 | 4822 122 33002 | 68 pF | |
| 2020 | 4822 122 33002 | 68 pF | |
| 2021 | 4822 121 41719 | 1 μF | 10% 100 V |
| 2022 | 4822 121 41719 | 1 μF | 10% 100 V |
| 2023 | 4822 121 42915 | 330 pF | |
| 2024 | 4822 122 32974 | 100 pF | |
| 2025 | 4822 122 32974 | 100 pF | |
| 2026 | 4822 124 22186 | 150 μF | 25 V |
| 2027 | 4822 122 31759 | 22 nF | |
| 2028 | 5322 124 21643 | 22 μF | 40 V |
| 2029 | 4822 122 33008 | 120 nF | 50 V |
| 2030 | 4822 122 33008 | 120 nF | 50 V |
| 2031 | 4822 122 33008 | 120 nF | 50 V |
| 2032 | 4822 122 31759 | 22 nF | |
| 2033 | 4822 122 31759 | 22 nF | |
| 2034 | 4822 122 31759 | 22 nF | |
| 2038 | 4822 121 41608 | 100 nF | 100 V |
| 2039 | 4822 121 41608 | 100 nF | 100 V |
| 2040 | 4822 121 41874 | 270 nF | 63 V |

*Transcribed from the sheet above; the vendor OCR of this sheet's parts columns
was unusable, so every row here was read off the 300 dpi scan.*

## Modification levels

The module shipped at level 5 and reached level 7 in the last production batch;
the mod-level sheet records two further changes at level 8.

- **Level 6** — R3031 3k6 → 3k3 and L5003 66 μH → 31 μH, to make the (R−Y) /
  (B−Y) arrange level symmetrical.
- **Level 7** — IC7202 TDA4560 → TDA4565/V4, R3021 and R3022 exchange values
  (10 Ω ↔ 1 k), R3031 back to 3k6, and three corrections to the circuit
  diagram's pin numbering around IC7202.
- **Level 8** — pins 27 and 28 of IC7203 short-circuited, which cures the white
  stripes at switch-on (fault symptom **A 4**); and a 22 k resistor added
  between the base of TS7012 and `7B3` (`CV-E/I`), curing colour loss when two
  disc drives run synchronously and the slave is in still mode. That second
  change also needs a link between `9C1` and `7B3` on
  [module carrier V](../v-module-carrier/index.md).

Full tables, with service code numbers:
[chapter 8, module B](../../service-information/modification-levels.md#mod-b).

## Related

- [Module circuit descriptions](../../circuit-description/modules.md#module-b) — the chapter 7 text in full
- [Modification levels per module](../../service-information/modification-levels.md#mod-b) — what changed at levels 6 to 8
- [Fault symptoms](../../service-information/fault-symptoms.md) — symptom A 4 involves this module
- [Fault-finding charts](../../repair/fault-finding.md) — the no-colour and no-picture charts
- [Adjustments](../../general-service/adjustments.md) — replacing module B means adjusting R3305 and R3315 on module U
