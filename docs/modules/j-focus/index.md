---
title: Module J - Focus
description: >-
  Focus servo for the objective lens.
---

# Module J - Focus

Focus servo for the objective lens.

## Overview

The focus module drives the objective lens: at start-up it moves the objective
until the laser beam is focussed on the disc, and thereafter it keeps the spot
in focus under every play condition. The objective travels about **5 mm**, and
is driven by output transistors 6208–6211 supplying `FOCACT` — negative drives
the objective *up*, towards the disc; positive pulls it *down*.

| | |
| --- | --- |
| Designation | **J** — focus |
| Modification levels | 2 → 4 |
| Data sheet | `CS 7 846`, page 053 (mod level 2) |
| Circuit diagram | `CS 6 876`, page 052 |
| Connector | `J1` |
| In | `FOC-ER` focus error and `FPI` focus position indication, from the deck · `FOC-EN` focus enable, from [drive processor module R](../r-drive-processor/index.md) |
| Out | `FOCACT` to the objective coil · `FOC-IND` focus indication, back to module R |
| Output devices | 6210 **BD436** and 6211 **BD437**, with drivers 6208 and 6209 |

!!! danger "Erratum — the 6210 / 6211 pinout is printed wrong"

    The service manual prints the pinout of 6210 and 6211 (BD436 / BD437) as
    **BCE**. It should be **ECB**. Fit them to the printed order and the focus
    amplifier will not work — and the transistors may not survive it.

    Found and recorded in the
    [error 7 investigation](../../repair/case-studies/error-7-focus.md), where a
    focus fault on a real player turned out to hinge on it.

## The board

<div class="sheet-pair" markdown>
<figure class="sheet sheet--photo" markdown>
[![Module J, component side of the board](assets/web/j-focus-top-preview.webp)](assets/web/j-focus-top-zoom.webp)
<figcaption>
  Module J, component side.
</figcaption>
</figure>
<figure class="sheet sheet--photo" markdown>
[![Module J, solder side of the board](assets/web/j-focus-bottom-preview.webp)](assets/web/j-focus-bottom-zoom.webp)
<figcaption>
  Module J, solder side.
</figcaption>
</figure>
</div>

## Where it sits in the player

First of the four boards in the right-hand cage, ahead of
[K](../k-hf-processor/index.md), [L](../l-video-dropout-correction/index.md)
and [M](../m-radial/index.md) — see the
[module and connector lay-out](../../system/module-layout.md).

## Circuit description

**Start-up.** With the motor not yet turning, `FOC-EN` is low and `FPI` from
the deck electronics is high, so the objective sits at 0 V. When the drive
module has seen a disc reflection (`DR`), a correct slide position (`SPI`) and
laser on (`LA-STIA`), it takes `FOC-EN` high. `FPI` is still high, so the drive
voltage goes negative and the objective moves up; filters 2006, 2007, 3015,
3016 and 3017 feed back to slow that movement. Switch 6205 is still open, so
the loop is at maximum gain.

**Focus found.** When the beam comes into focus, `FPI` goes low, focus loop
switch 6206 closes and `FOC-IND` follows it low — which is the drive module's
signal that the turntable may be started. Switch 6205 closes at the same
moment, adding negative feedback and reducing the gain. From then on the
objective follows `FOC-ER`, held in focus by an average of about **−1 V** at
the output of 6208–6211.

**Focus not found.** `FPI` stays high, and 0.5 s later the drive module takes
`FOC-EN` low again: the drive voltage goes to 0 V and the objective falls. After
0.2 s `FOC-EN` goes high and the objective rises again. **The sequence is
repeated five times**, and if focus is still not found the player goes to
stand-by — which is exactly what
[error 7](../../repair/error-codes.md#error-7) reports.

The full text, including the behaviour on brief reflection disturbances, is in
[chapter 7, module J](../../circuit-description/modules.md#module-j).

## Adjustments

The manual gives **no adjustment procedure** for this module: the data sheet
carries only the PCB lay-out and the parts list.

## Circuit diagram

<figure class="sheet" markdown>
[![Focus module J - circuit diagram](assets/web/cs-6-876-circuit-p052-preview.webp)](assets/web/cs-6-876-circuit-p052-zoom.webp)
<figcaption>
  Focus module J - circuit diagram.
  <span class="cs">CS 6 876</span>
  <span class="src">service manual page 052</span>
</figcaption>
</figure>

## PCB lay-out

<figure class="sheet sheet--fold" markdown>
[![Focus module J (mod level 2) - PCB / parts / circuit](assets/web/cs-7-846-module-sheet-p053-preview.webp)](assets/web/cs-7-846-module-sheet-p053-zoom.webp)
<figcaption>
  Focus module J (mod level 2) - PCB / parts / circuit.
  <span class="cs">CS 7 846</span>
  <span class="src">service manual page 053</span>
</figcaption>
</figure>

## List of electrical parts

**NFR25 Resistors**

| Item | Service code number | Value | Rating |
| --- | --- | --- | --- |
| 3057 | 4822 111 30492 | 2.2 Ω |  |
| 3060 | 4822 111 30492 | 2.2 Ω |  |

**Capacitors**

| Item | Service code number | Value | Rating |
| --- | --- | --- | --- |
| 2001 | 4822 122 33011 | 470 nF | 16 V |
| 2002 | 4822 122 32442 | 10 nF |  |
| 2003 | 4822 122 31783 | 2.7 nF |  |
| 2004 | 5322 124 21643 | 22 μF | 40 V |
| 2005 | 5322 124 21643 | 22 μF | 40 V |
| 2006 | 4822 121 42527 | 180 nF | 63 V |
| 2007 | 4822 124 21314 | 10 μF | 10 V |
| 2008 | 4822 121 50841 | 2.2 nF | 160 V |
| 2011 | 4822 122 32442 | 10 nF |  |
| 2012 | 4822 121 41876 | 220 nF | 20% 63 V |
| 2013 | 4822 124 22031 | 4.7 μF | 63 V |
| 2014 | 4822 124 22188 | 3.3 μF | 63 V |
| 2015 | 4822 124 22027 | 47 μF | 25 V |
| 2016 | 4822 124 22027 | 47 μF | 25 V |

## Modification levels

The module shipped at level 2 — which is the level the data sheet above is
printed for — and reached level 4 in the last production batch:

- **Level 3** — R3025 4k7 → 2k7, improving playability.
- **Level 4** — R3055, a 10 k SFR25, added from connector `7J1` to ground, to
  stop `FOC-EN` going active while the drive is tri-stated.

Full tables, with service code numbers:
[chapter 8, module J](../../service-information/modification-levels.md#mod-j).

## Related

- [Error 7 — not in focus](../../repair/case-studies/error-7-focus.md) — a worked investigation on this module, and the source of the pinout erratum
- [Error codes](../../repair/error-codes.md#error-7) — what the player reports when focus is not found
- [Module circuit descriptions](../../circuit-description/modules.md#module-j) — the chapter 7 text in full
- [Modification levels per module](../../service-information/modification-levels.md#mod-j) — the level-3 and level-4 changes
- [The LaserVision system](../../circuit-description/laservision-system.md) — the optics the focus loop is holding
- [Module Z — Deck electronics](../z-deck-electronics/index.md) — supplies `FPI` and `FOC-ER`
