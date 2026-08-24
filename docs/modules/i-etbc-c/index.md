---
title: Module I - ETBC-C
description: >-
  ETBC-C, the second half of the electronic timebase corrector.
search:
  boost: 2
---

# Module I - ETBC-C

ETBC-C, the second half of the electronic timebase corrector.

## Overview

ETBC C is the other half of the electronic time-base correction system — the
half that *measures*. It compares the video read off the disc against the
reference and produces the two control signals
[ETBC B module H](../h-etbc-b/index.md) corrects with: **`TANG-ER` (coarse)**
and **`BURST-ER` (fine)**.

The measurement is made at two levels of precision:

- **Coarse** — comparing the syncs in `CV-TBM` against `RAMP-EN`, the reference
  timing signal from
  [reference source module D](../d-reference-source/index.md).
- **Fine** — from the *special burst*, a 3.75 MHz signal inserted during the
  sync pulses. It exists only in video coming off a disc.

| | |
| --- | --- |
| Designation | **I** — ETBC C |
| Modification levels | 6 → 7 |
| Data sheet | `CS 7 845`, page 050 (mod level 6) |
| Circuit diagram | `CS 6 875`, page 051 |
| Connectors | `I1`, `I2` |
| In | `CV-TBM` from [module H](../h-etbc-b/index.md) · `RAMP-EN` from [module D](../d-reference-source/index.md) |
| Out | `TANG-ER`, `BURST-ER` to [module H](../h-etbc-b/index.md) |

## The board

<div class="sheet-pair" markdown>
<figure class="sheet sheet--photo" markdown>
[![Module I, component side of the board](assets/web/i-etbc-c-top-preview.webp)](assets/web/i-etbc-c-top-zoom.webp)
<figcaption>
  Module I, component side.
</figcaption>
</figure>
<figure class="sheet sheet--photo" markdown>
[![Module I, solder side of the board](assets/web/i-etbc-c-bottom-preview.webp)](assets/web/i-etbc-c-bottom-zoom.webp)
<figcaption>
  Module I, solder side.
</figcaption>
</figure>
</div>

## Where it sits in the player

Lying flat across the front of the chassis, last of the row behind
[H](../h-etbc-b/index.md) — see the
[module and connector lay-out](../../system/module-layout.md).

## Circuit description

`CV-TBM` reaches pin 9 of synchronisation IC7203, which low-pass filters it and
separates the syncs; the line sync `HMANCH` appears on pin 20. One-shot
IC7201-2A turns that into a constant-length pulse, and a second pulse of the
same length (**T1 = 33 μs**) is derived from `RAMP-EN`.

Comparing the relative timing of those two in 7202-2A and 7202-2B puts a
current proportional to the time error into one of the collectors of 7004 and
7005 — with **T2 = 4.7 μs** in the timing diagram, the case where the disc's
time base is longer than the reference, which is what happens when the disc
turns too slowly.

The full text, including the special burst detector, is in
[chapter 7, module I](../../circuit-description/modules/i-etbc-c.md).

## Adjustments

One adjustment: the special burst separator.

!!! info "Required"

    Test disc · scope

    Load the test disc; still picture, colour bar (picture no. 6200).

**1) L5001 — special burst separator**

- Measure the signal on the base of TS7029 with the scope, line frequent.
- Adjust L5001 for **maximum amplitude of the special burst signal**.

## Circuit diagram

<figure class="sheet sheet--fold" markdown>
[![ETBC-C module I - circuit diagram](assets/web/cs-6-875-circuit-p051-preview.webp)](assets/web/cs-6-875-circuit-p051-zoom.webp)
<figcaption>
  ETBC-C module I - circuit diagram.
  <span class="cs">CS 6 875</span>
  <span class="src">service manual page 051</span>
</figcaption>
</figure>

## PCB lay-out

<figure class="sheet sheet--fold" markdown>
[![ETBC-C module I (mod level 6) - adjustments / PCB / parts](assets/web/cs-7-845-module-sheet-p050-preview.webp)](assets/web/cs-7-845-module-sheet-p050-zoom.webp)
<figcaption>
  ETBC-C module I (mod level 6) - adjustments / PCB / parts.
  <span class="cs">CS 7 845</span>
  <span class="src">service manual page 050</span>
</figcaption>
</figure>

## List of electrical parts

The sheet is printed for a **mod level 6** board; see the modification levels
below for what level 7 changes.

**Coils**

| Item | Service code number | Value |
| --- | --- | --- |
| 5001 | 4822 156 11003 | 12 μH |

**NFR25 resistors**

| Item | Service code number | Value |
| --- | --- | --- |
| 3129 | 4822 111 30513 | 15 Ω |
| 3130 | 4822 111 30513 | 15 Ω |

**Capacitors**

| Item | Service code number | Value | Rating |
| --- | --- | --- | --- |
| 2001 | 5322 124 21643 | 22 μF | 40 V |
| 2002 | 4822 122 31759 | 22 nF | |
| 2003 | 4822 122 32974 | 100 pF | |
| 2004 | 4822 122 31783 | 2.7 nF | |
| 2005 | 4822 122 31767 | 150 pF | |
| 2006 | 5322 124 21643 | 22 μF | 40 V |
| 2007 | 4822 122 31759 | 22 nF | |
| 2008 | 4822 122 31759 | 22 nF | |
| 2009 | 4822 122 31969 | 3.3 nF | |
| 2010 | 4822 122 31969 | 3.3 nF | |
| 2011 | 4822 122 31759 | 22 nF | |
| 2012 | 4822 122 31781 | 1.5 nF | |
| 2013 | 4822 122 31781 | 1.5 nF | |
| 2014 | 4822 124 22027 | 47 μF | 25 V |
| 2015 | 4822 121 41608 | 100 nF | 100 V |
| 2017 | 4822 122 31783 | 2.7 nF | |
| 2019 | 4822 122 32976 | 470 pF | |
| 2020 | 4822 122 32974 | 100 pF | |
| 2023 | 4822 121 41545 | 33 nF | 250 V |
| 2024 | 4822 121 41874 | 270 nF | 63 V |
| 2025 | 4822 122 31774 | 56 pF | |
| 2026 | 5322 124 21643 | 22 μF | 40 V |
| 2027 | 4822 122 32504 | 15 pF | |
| 2028 | 4822 122 31774 | 56 pF | |
| 2029 | 4822 122 31784 | 4.7 nF | |
| 2034 | 4822 122 31759 | 22 nF | |
| 2037 | 5322 122 31647 | 1 nF | |
| 2041 | 4822 122 31759 | 22 nF | |
| 2042 | 4822 122 31775 | 680 pF | |
| 2043 | 4822 122 32482 | 22 pF | |
| 2044 | 4822 122 31772 | 47 pF | |
| 2045 | 4822 122 32542 | 47 nF | |
| 2046 | 4822 122 31774 | 56 pF | |
| 2048 | 4822 122 32142 | 270 pF | |
| 2049 | 5322 122 31647 | 1 nF | |
| 2050 | 4822 124 22031 | 4.7 μF | 63 V |
| 2051 | 4822 122 31759 | 22 nF | |
| 2052 | 4822 121 51051 | 4.7 nF | 160 V |
| 2053 | 4822 122 32891 | 68 nF | |
| 2054 | 4822 124 22031 | 4.7 μF | 63 V |
| 2057 | 4822 124 22031 | 4.7 μF | 63 V |
| 2058 | 4822 121 41757 | 470 nF | 10% 63 V |
| 2059 | 4822 121 42915 | 330 pF | |
| 2060 | 5322 124 21643 | 22 μF | 40 V |
| 2061 | 4822 122 32153 | 1.8 nF | |
| 2063 | 5322 124 21711 | 100 μF | 25 V |
| 2064 | 5322 124 21711 | 100 μF | 25 V |

*The vendor OCR lost the item-number column of the sheet's first capacitor
block and the rating column of its second; both were re-read off the 300 dpi
scan.*

## Modification levels

The module shipped at level 6 and went to level 7 in the second production
batch, with two changes:

- C2046 56 pF → 47 pF, to reduce disturbance of the time-error measurement.
- C2015, C2023 and C2024 changed from polyester to ceramic chip capacitors of
  the same value, improving the HF filtering in the sync separator.

Full tables, with service code numbers:
[chapter 8, module I](../../service-information/modification-levels.md#mod-i).

## Related

- [Module I circuit description](../../circuit-description/modules/i-etbc-c.md) — the chapter 7 text in full
- [Module H — ETBC B](../h-etbc-b/index.md) — corrects the error this module measures
- [The LaserVision system](../../circuit-description/laservision-system.md) — the special burst and why it is there
- [Modification levels per module](../../service-information/modification-levels.md#mod-i) — the two level-7 changes
- [Module and connector lay-out](../../system/module-layout.md) — connector positions
- [Electrical parts](../../parts/electrical-parts.md) — the collective list of standard components by service code number; the connectors are in [mechanical parts](../../parts/mechanical-parts.md#module-connectors)
