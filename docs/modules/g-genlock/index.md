---
title: Module G - Gen lock
description: >-
  Genlock: locking the player's timing to an external video reference.
search:
  boost: 2
---

# Module G - Gen lock

Genlock: locking the player's timing to an external video reference.

## Overview

Genlock locks the disc — in both frame and line — to the sync generator on
[reference source module D](../d-reference-source/index.md). Because the player
is an RGB machine, the colour sub-carrier does not have to be synchronised, so
locking to the highly accurate internal sync generator is enough. That has a
practical consequence: text can be put on screen *before the disc turns*, keyed
to the same sync the disc will later lock to. The disc's video can equally be
locked to an external video or sync signal.

Locking is done by pulling the rotational speed of the disc about, through the
motor control on [module F](../f-motor-sequence/index.md); that in turn
controls the phase of the video read off the disc, `CV-DOC`.

!!! info "How long locking takes"

    Synchronisation has two stages. The internal sync generator locks to the
    external signal — **up to 7 s**, and it can start while the disc is still
    stationary. Then the disc locks to the internal sync generator — **up to
    3 s**. If the phase of the external sync is reset arbitrarily during a
    programme, both happen at once and the total can be **7 s**.

| | |
| --- | --- |
| Designation | **G** — gen lock |
| Modification levels | 3 → 4 |
| Data sheet | `CS 7 843`, page 046 |
| Circuit diagram | `CS 6 873`, page 047 |
| Connectors | `G1`, `G2` |
| Key device | IC7205 sync separator, VCO centre frequency **4.5 MHz**, pulled by varicap 6014 |

## The board

<div class="sheet-pair" markdown>
<figure class="sheet sheet--photo" markdown>
[![Module G, component side of the board](assets/web/g-genlock-top-preview.webp)](assets/web/g-genlock-top-zoom.webp)
<figcaption>
  Module G, component side.
</figcaption>
</figure>
<figure class="sheet sheet--photo" markdown>
[![Module G, solder side of the board](assets/web/g-genlock-bottom-preview.webp)](assets/web/g-genlock-bottom-zoom.webp)
<figcaption>
  Module G, solder side.
</figcaption>
</figure>
</div>

## Where it sits in the player

Lying flat across the front of the chassis, between
[F](../f-motor-sequence/index.md) and [H](../h-etbc-b/index.md) — see the
[module and connector lay-out](../../system/module-layout.md).

## Circuit description

Sync separator IC7205 runs a 4.5 MHz VCO controlled by varicap 6014. Its
outputs are:

| Pin | Signal | |
| --- | --- | --- |
| 20 | `LPO` | line pulse out, from `CV-DOC` |
| 19 | `M-LOCK` | `CV-DOC` and VCO locked |
| 15 | `MCO` | motor control out — duty cycle proportional to speed error |
| 4 | `DEM-BK` | burst key pulse from the demodulated video |
| 8 | | frame pulse |
| 3 | | 4.5 MHz clock |
| 6 | | composite sync derived from `CV-DOC` |

Inside IC7205 the disc's line pulses — derived from `CV-DOC` — are phase
compared against the reference line frequency, which is the 4.5 MHz clock
divided by 288. The phase difference changes the duty cycle of `MCO`, which is
the input to the motor control on [module F](../f-motor-sequence/index.md); so
the disc's line pulses end up phase-locked to the reference. Pins 4, 6 and 8
are combined by IC7206-2B and T7018 into `DEM-BK`, with the pulses suppressed
around the vertical sync.

The full text is in
[chapter 7, module G](../../circuit-description/modules/g-genlock.md).

## Adjustments

One adjustment: the VCO centre frequency.

!!! info "Required"

    Test disc · voltmeter

    Rotating disc.

**1) L5001 — VCO**

- Measure the DC voltage on `4G2`.
- Adjust L5001 until it is **0 V ± 2 V**.

!!! warning "With the set cold"

    The sheet's own note: in the cold state of the set, adjust for **+2 V**.

**Adjustment when an item is replaced**

| Replaced | Adjust |
| --- | --- |
| IC7205 | L5001 |

## Circuit diagram

<figure class="sheet sheet--fold" markdown>
[![Gen lock module G - circuit diagram](assets/web/cs-6-873-circuit-p047-preview.webp)](assets/web/cs-6-873-circuit-p047-zoom.webp)
<figcaption>
  Gen lock module G - circuit diagram.
  <span class="cs">CS 6 873</span>
  <span class="src">service manual page 047</span>
</figcaption>
</figure>

## PCB lay-out

<figure class="sheet sheet--fold" markdown>
[![Gen lock module G (mod level 3) - adjustments / PCB / parts](assets/web/cs-7-843-module-sheet-p046-preview.webp)](assets/web/cs-7-843-module-sheet-p046-zoom.webp)
<figcaption>
  Gen lock module G (mod level 3) - adjustments / PCB / parts.
  <span class="cs">CS 7 843</span>
  <span class="src">service manual page 046</span>
</figcaption>
</figure>

## List of electrical parts

**Coils**

| Item | Service code number | Value | Rating |
| --- | --- | --- | --- |
| 5001 | 4822 156 11004 | 26.5 μH |  |

**Fuse Resistors**

| Item | Service code number | Value | Rating |
| --- | --- | --- | --- |
| 3001 | 4822 111 30846 | 6.8 Ω |  |
| 3002 | 5322 111 90376 | 4.7 Ω |  |
| 3004 | 5322 111 90376 | 4.7 Ω |  |
| 3051 | 5322 111 90376 | 4.7 Ω |  |

**NFR25 Resistors**

| Item | Service code number | Value | Rating |
| --- | --- | --- | --- |
| 3056 | 4822 111 30513 | 15 Ω |  |

**Capacitors**

| Item | Service code number | Value | Rating |
| --- | --- | --- | --- |
| 2001 | 4822 122 31644 | 2.2 nF |  |
| 2002 | 4822 122 32442 | 10 nF |  |
| 2003 | 4822 122 31644 | 2.2 nF |  |
| 2004 | 4822 122 31759 | 22 nF |  |
| 2005 | 4822 122 32442 | 10 nF |  |
| 2006 | 4822 124 22029 | 2.2 μF | 63 V |
| 2007 | 5322 124 21643 | 22 μF | 40 V |
| 2008 | 4822 124 21255 | 2.2 μF | 25 V |
| 2010 | 5322 124 21976 | 10 μF | 25 V |
| 2011 | 4822 122 32976 | 470 pF |  |
| 2012 | 4822 122 32541 | 27 nF |  |
| 2013 | 4822 122 31782 | 15 nF |  |
| 2014 | 5322 122 31647 | 1 nF |  |
| 2015 | 5322 124 21749 | 10 μF | 63 V |
| 2016 | 4822 124 22027 | 47 μF | 25 V |
| 2017 | 4822 122 31759 | 22 nF |  |
| 2018 | 5322 124 21643 | 22 μF | 40 V |
| 2019 | 4822 122 31759 | 22 nF |  |
| 2020 | 4822 124 22027 | 47 μF | 25 V |
| 2021 | 4822 122 31759 | 22 nF |  |
| 2022 | 5322 124 21643 | 22 μF | 40 V |
| 2023 | 5322 124 21711 | 100 μF | 25 V |
| 2024 | 5322 124 21643 | 22 μF | 40 V |
| 2025 | 4822 121 41608 | 100 nF | 100 V |
| 2026 | 4822 121 41608 | 100 nF | 100 V |
| 2027 | 4822 122 32974 | 100 pF |  |
| 2028 | 4822 122 32976 | 470 pF |  |
| 2029 | 4822 122 31759 | 22 nF |  |
| 2030 | 4822 122 31771 | 390 pF |  |
| 2031 | 5322 122 32104 | 33 pF |  |
| 2032 | 4822 122 31784 | 4.7 nF |  |
| 2033 | 4822 122 32976 | 470 pF |  |
| 2059 | 5322 124 14081 | 6.8 μF | 25 V |
| 2060 | 4822 122 31759 | 22 nF |  |
| 2061 | 4822 122 31965 | 220 pF |  |
| 2062 | 5322 124 21643 | 22 μF | 40 V |
| 2063 | 4822 122 31759 | 22 nF |  |
| 2064 | 4822 122 31759 | 22 nF |  |
| 2065 | 5322 124 21643 | 22 μF | 40 V |
| 2066 | 4822 122 31759 | 22 nF |  |
| 2067 | 4822 122 31774 | 56 pF |  |
| 2068 | 4822 122 31759 | 22 nF |  |
| 2069 | 4822 122 31072 | 47 pF |  |
| 2070 | 4822 124 22231 | 470 μF |  |

## Modification levels

The module shipped at level 3 and went to level 4, a single change: R3077
100 k → 91 k, which shifts the drop-out inhibit (`DO-INH`) window.

Full table, with service code numbers:
[chapter 8, module G](../../service-information/modification-levels.md#mod-g).

## Related

- [Module G circuit description](../../circuit-description/modules/g-genlock.md) — the chapter 7 text in full
- [Error 9 — frame lock](../../repair/case-studies/error-9-frame-lock.md) — a worked investigation, with scope traces taken on this module's connectors
- [Modification levels per module](../../service-information/modification-levels.md#mod-g) — the level-4 change
- [Fault-finding charts](../../repair/fault-finding.md) — the frame-lock paths
- [Module F — Motor + sequence](../f-motor-sequence/index.md) — receives `MCO` from here
- [The LaserVision system](../../circuit-description/laservision-system.md) — why locking matters at all
- [Electrical parts](../../parts/electrical-parts.md) — the collective list of standard components by service code number; the connectors are in [mechanical parts](../../parts/mechanical-parts.md#module-connectors)
