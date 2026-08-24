---
title: Module T - Supply
description: >-
  Switched-mode power supply.
search:
  boost: 2
---

# Module T - Supply

Switched-mode power supply.

## Overview

The supply module produces the four stabilised rails the player runs on —
**+12 V, −12 V, +5 V and −5 V** — from a **parallel switched-mode** circuit,
with a current monitor protecting it against overload and an auxiliary supply
generating the starting voltage for the driver stage.

!!! danger "Mains-side servicing"

    Most of this board is at mains potential and is **not** isolated from it.
    The primary side carries rectified mains on large reservoir capacitors that
    stay charged after the player is switched off and unplugged.

    Read [warnings](../../general-service/warnings.md) before working on this
    module — including the isolating-transformer rule and the earthing checks
    that follow any repair on it.

| | |
| --- | --- |
| Designation | **T** — supply |
| Modification levels | 1 (unchanged through production) |
| Data sheet | `CS 7 853`, pages 071–072 |
| Circuit diagram | `CS 6 885`, page 073 |
| Connectors | `T1`, `T2` |
| Rails | +12 V, −12 V, +5 V, −5 V, plus the `+12SB` / `+5SB` / `−5SB` standby rails |
| Mains selector | `X002` 110 V / `X003` 240 V, on the board |
| Fuses | F911 and F912 **T1.6 A 250 V**, F913 **3.15 A** |

!!! note "This module is numbered differently from every other"

    Supply module T is listed in the **board's own letter/number coding** —
    `C001`, `R101`, `V203`, `F911` — not the four-number diagram coding used
    everywhere else in the manual. See
    [remarks, section 6](../../general-service/remarks.md), which calls this
    module out by name.

## The board

<figure class="sheet sheet--photo" markdown>
[![Module T, component side of the board](assets/web/t-supply-top-preview.webp)](assets/web/t-supply-top-zoom.webp)
<figcaption>
  Module T, component side.
</figcaption>
</figure>

## Where it sits in the player

At the right-hand rear of the chassis behind its perforated screen, beside
[control module S](../s-control/index.md) — see the
[module and connector lay-out](../../system/module-layout.md). Only one
photograph of this board exists in the collection, the component side.

## Circuit description

Bridge rectifier V001 rectifies the mains. Its output — unstabilised against
mains variation — supplies the parallel switched-mode circuit built around
transformer T901 and switching transistor V203. The switching pulses on T901's
primary are transformed to the secondary windings 12-1, 11-2, 10-3 and
x921–x922, each with the usual forward rectifier — series and freewheel diode,
coil and smoothing capacitor — producing the four stabilised rails.

V203 is controlled from pin 5 of the command circuit D501 (a hybrid SMPS
circuit) through driver transistor V303 and driver transformer T201. The
driver stage's own supply is made by rectifying pulses from winding 10-3 with
V301 and C301; the +15 V starting voltage comes from the auxiliary supply.

The full text, including the current monitor and the standby rails, is in
[chapter 7, module T](../../circuit-description/modules/t-supply.md).

## Adjustments

One adjustment: the +5 V rail.

!!! info "Required"

    Test disc · voltmeter

    Rotating disc.

**1) R503 — DC voltage**

- Measure the DC voltage on `3T2` (`+5`).
- Adjust R503 for **5.2 V ± 0.1 V**.

## Circuit diagram

<figure class="sheet sheet--fold" markdown>
[![Supply module T - circuit diagram (switched mode power supply)](assets/web/cs-6-885-circuit-p073-preview.webp)](assets/web/cs-6-885-circuit-p073-zoom.webp)
<figcaption>
  Supply module T - circuit diagram (switched mode power supply).
  <span class="cs">CS 6 885</span>
  <span class="src">service manual page 073</span>
</figcaption>
</figure>

## PCB lay-out

<figure class="sheet sheet--fold" markdown>
[![Supply module T (mod level 1) - adjustments / PCB / parts](assets/web/cs-7-853-module-sheet-p071-072-preview.webp)](assets/web/cs-7-853-module-sheet-p071-072-zoom.webp)
<figcaption>
  Supply module T (mod level 1) - adjustments / PCB / parts.
  <span class="cs">CS 7 853</span>
  <span class="src">service manual pages 071, 072</span>
</figcaption>
</figure>

## List of electrical parts

**Fuses**

| Item | Service code number | Value | Rating |
| --- | --- | --- | --- |
| F911 | 4822 253 30024 | 1.6 A |  |
| F912 | 4822 253 30024 | 1.6 A |  |
| F913 | 4822 253 10048 | 3.15 A |  |

**Circuits**

| Item | Service code number | Value | Rating |
| --- | --- | --- | --- |
| D501 | 5322 209 82349 | Hybride circuit SMPS |  |

**Other**

| Item | Service code number | Value | Rating |
| --- | --- | --- | --- |
| T101 | 5322 146 40322 | aux trafo |  |
| T201 | 5322 142 60363 | impuls trafo |  |
| T401 | 4822 142 70056 | current trafo |  |
| T901 | 5322 146 30531 | power trafo |  |
| V001 | 4822 130 50438 | Rectifier KBU8-K |  |

**Coils**

| Item | Service code number | Value | Rating |
| --- | --- | --- | --- |
| L001 | 4822 157 52981 | 350 μH |  |
| L002 | 4822 158 30208 | Mains choke |  |
| L701 | 4822 157 52979 | Triple choke |  |

**Potentiometers**

| Item | Service code number | Value | Rating |
| --- | --- | --- | --- |
| R402 | 4822 101 10793 | 5 kΩ |  |
| R503 | 4822 101 10792 | 1 kΩ |  |

**NTC Resistors**

| Item | Service code number | Value | Rating |
| --- | --- | --- | --- |
| R001 | 5322 116 40077 | 7 Ω |  |

**PTC Resistors**

| Item | Service code number | Value | Rating |
| --- | --- | --- | --- |
| R801 | 4822 116 40032 | 2.3 Ω - 5 Ω |  |

**Wire wound Resistors**

| Item | Service code number | Value | Rating |
| --- | --- | --- | --- |
| R201 | 4822 112 41107 | 1 kΩ |  |

**NFR25 Resistors**

| Item | Service code number | Value | Rating |
| --- | --- | --- | --- |
| R101 | 4822 111 30544 | 220 Ω |  |
| R202 | 4822 111 30526 | 47 Ω |  |
| R301 | 4822 111 30499 | 4.7 Ω |  |
| R701 | 4822 111 30526 | 47 Ω |  |
| R702 | 4822 111 30526 | 47 Ω |  |
| R706 | 4822 111 30526 | 47 Ω |  |

**VR25 Resistors**

| Item | Service code number | Value | Rating |
| --- | --- | --- | --- |
| R901 | 5322 116 64132 | 1 MΩ |  |

**PR37 Resistors**

| Item | Service code number | Value | Rating |
| --- | --- | --- | --- |
| R703 | 5322 116 55063 | 39 Ω |  |
| R704 | 5322 116 54909 | 1 kΩ |  |
| R707 | 5322 116 54909 | 1 kΩ |  |

**PR52 Resistors**

| Item | Service code number | Value | Rating |
| --- | --- | --- | --- |
| R203 | 5322 116 51093 | 15 Ω |  |

**VR68 Resistors**

| Item | Service code number | Value | Rating |
| --- | --- | --- | --- |
| R103 | 5322 116 53075 | 220 kΩ |  |

**Capacitors**

| Item | Service code number | Value | Rating |
| --- | --- | --- | --- |
| C001 | 4822 122 33042 | 3.3 nF |  |
| C002 | 4822 122 33042 | 3.3 nF |  |
| C004 | 5322 121 41721 | 470 nF | 10% 275 V |
| C006 | 5322 124 21798 | 220 μF | 10% 200 V |
| C007 | 5322 124 21798 | 220 μF | 10% 200 V |
| C101 | 4822 124 10367 | 4.7 μF | 25 V |
| C102 | 4822 121 40483 | 10 nF | 10% 400 V |
| C103 | 4822 122 31125 | 4.7 nF | 100 V |
| C104 | 4822 124 40744 | 68 μF | 40 V |
| C201 | 5322 121 44286 | 1 nF | 10% 630 V |
| C202 | 5322 121 44286 | 1 nF | 10% 630 V |
| C301 | 4822 121 40516 | 22 nF | 10% 250 V |
| C501 | 5322 121 40308 | 22 nF | 10% 400 V |
| C502 | 4822 121 40232 | 220 nF | 10% 100 V |
| C503 | 4822 121 40232 | 220 nF | 10% 100 V |
| C504 | 4822 122 30103 | 22 nF | 63 V |
| C506 | 4822 124 21314 | 10 μF | 16 V |
| C701 | 4822 121 40337 | 4.7 nF | 10% 630 V |
| C702 | 4822 121 40338 | 2.2 nF | 10% 630 V |
| C703 | 4822 124 40723 | 2.2 mF | 16 V |
| C704 | 4822 124 40723 | 2.2 mF | 16 V |
| C706 | 4822 121 40338 | 2.2 nF | 10% 630 V |
| C707 | 4822 124 40723 | 2.2 mF | 16 V |
| C801 | 5322 124 14081 | 6.8 μF | 25 V |
| C802 | 5322 124 14081 | 6.8 μF | 25 V |

## Modification levels

Module T carried **modification level 1 in every production batch**. The
mod-level sheet records one change at that level, and it is **VP410 only**: a
0.15 Ω / 1 W resistor added in series with fuse F913, curing horizontal stripes
in the picture at start-up — fault symptom **A 5**.

Full table, with the service code number:
[chapter 8, module T](../../service-information/modification-levels.md#mod-t).

## Related

- [Warnings](../../general-service/warnings.md) — **read first**: mains-side servicing, isolating transformer, earthing checks
- [Module T circuit description](../../circuit-description/modules/t-supply.md) — the chapter 7 text in full
- [Remarks](../../general-service/remarks.md) — why this board's component numbering differs
- [Fault symptoms](../../service-information/fault-symptoms.md) — symptom A 5, VP410 only
- [Fault-finding charts](../../repair/fault-finding.md) — dead-set and supply paths
- [Technical data](../../overview/technical-data.md) — mains voltage range and power consumption
- [Modification levels per module](../../service-information/modification-levels.md#mod-t) — what changed at each level, with service code numbers
- [Electrical parts](../../parts/electrical-parts.md) — the collective list of standard components by service code number; the connectors are in [mechanical parts](../../parts/mechanical-parts.md#module-connectors)
