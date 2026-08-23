---
title: Module M - Radial
description: >-
  Radial servo: fine tracking and jump control.
search:
  boost: 2
---

# Module M - Radial

Radial servo: fine tracking and jump control.

## Overview

The radial module supplies the current that drives the **radial mirror**,
keeping the laser beam on the required track in every play mode — and throwing
it deliberately across tracks when a jump is wanted.

| | |
| --- | --- |
| Designation | **M** — radial |
| Modification levels | 0 → 3 |
| Data sheet | `CS 7 849`, page 058 (mod level 1) |
| Circuit diagram | `CS 6 879`, page 059 |
| Connectors | `M1`, `M2` |
| In | `RAD-ER` radial error, from the deck · `RLS` radial loop switch and `CP1`/`CP2` course pulses, from [drive processor module R](../r-drive-processor/index.md) |
| Out | mirror drive current · a level-shifted copy of the drive signal, back to module R |

## The board

<div class="sheet-pair" markdown>
<figure class="sheet sheet--photo" markdown>
[![Module M, component side of the board](assets/web/m-radial-top-preview.webp)](assets/web/m-radial-top-zoom.webp)
<figcaption>
  Module M, component side.
</figcaption>
</figure>
<figure class="sheet sheet--photo" markdown>
[![Module M, solder side of the board](assets/web/m-radial-bottom-preview.webp)](assets/web/m-radial-bottom-zoom.webp)
<figcaption>
  Module M, solder side.
</figcaption>
</figure>
</div>

## Where it sits in the player

Rearmost of the four boards in the right-hand cage, behind
[L](../l-video-dropout-correction/index.md) — see the
[module and connector lay-out](../../system/module-layout.md).

## Circuit description

In normal play `RAD-ER` — proportional to how far the beam has strayed from
the track — passes a phase compensation network and limiter IC7100-2B to the
radial loop switch, transistor 7002. That switch is driven from the
microprocessor on
[drive processor module R](../r-drive-processor/index.md) and is closed only
while a track is being followed. The error is then amplified in IC7100-2A and
fed to the mirror through output transistors 7010–7013.

The mirror's deflection range is limited, so the drive signal is also sent back
to module R through level shifter IC7101-2A, and too large a deflection is
taken up by moving the slide instead. The level shifter turns a signal that
swings both positive and negative into a positive signal with the same
variation.

For a **jump**, the beam is thrown across one or more tracks by a fast
deflection of the mirror: course pulse `CP1` forward, `CP2` reverse, both fed
into the same radial amplifier. During a jump `RLS` opens the radial loop.

The full text is in
[chapter 7, module M](../../circuit-description/modules.md#module-m).

## Adjustments

The manual gives **no adjustment procedure** for this module: the data sheet
carries only the PCB lay-out and the parts list.

## Circuit diagram

<figure class="sheet sheet--fold" markdown>
[![Radial module M - circuit diagram](assets/web/cs-6-879-circuit-p059-preview.webp)](assets/web/cs-6-879-circuit-p059-zoom.webp)
<figcaption>
  Radial module M - circuit diagram.
  <span class="cs">CS 6 879</span>
  <span class="src">service manual page 059</span>
</figcaption>
</figure>

## PCB lay-out

<figure class="sheet sheet--fold" markdown>
[![Radial module M (mod level 1) - PCB / parts](assets/web/cs-7-849-module-sheet-p058-preview.webp)](assets/web/cs-7-849-module-sheet-p058-zoom.webp)
<figcaption>
  Radial module M (mod level 1) - PCB / parts.
  <span class="cs">CS 7 849</span>
  <span class="src">service manual page 058</span>
</figcaption>
</figure>

## List of electrical parts

**PTC Resistors**

| Item | Service code number | Value | Rating |
| --- | --- | --- | --- |
| 3033 | 4822 116 40026 | 5.6 Ω |  |

**NFR Resistors**

| Item | Service code number | Value | Rating |
| --- | --- | --- | --- |
| 3090 | 4822 111 30492 | 2.2 Ω |  |
| 3093 | 4822 111 30492 | 2.2 Ω |  |

**Capacitors**

| Item | Service code number | Value | Rating |
| --- | --- | --- | --- |
| 2001 | 5322 122 31647 | 1 nF |  |
| 2002 | 5322 122 31647 | 1 nF |  |
| 2003 | 4822 122 31768 | 180 pF |  |
| 2004 | 4822 121 50538 | 6.8 nF | 63 V |
| 2010 | 4822 121 50538 | 6.8 nF | 63 V |
| 2011 | 4822 121 41874 | 270 nF | 63 V |
| 2012 | 4822 122 31644 | 2.2 nF |  |
| 2013 | 4822 122 32975 | 33 pF |  |
| 2014 | 4822 121 41876 | 220 nF | 20% 63 V |
| 2015 | 5322 122 31848 | 33 nF |  |
| 2020 | 4822 124 22027 | 47 μF | 25 V |
| 2021 | 4822 124 22027 | 47 μF | 25 V |
| 2022 | 5322 122 31848 | 33 nF |  |
| 2023 | 5322 122 31848 | 33 nF |  |

## Modification levels

The module shipped at level 0 and reached level 3 in the last production batch
— the busiest change history of the servo boards:

- **Level 1** — TS7023 and TS7024 (BC558B) added with R3085 and R3086 (47 k),
  to avoid a DC offset when the radial mirror is unloaded.
- **Level 2** — those four parts deleted again, because the new drive software
  6803.5 on
  [drive processor module R](../r-drive-processor/index.md) made them
  unnecessary. Also at level 2: R3001–R3010, C2002, C2004 and TS7001 deleted
  with source and drain of TS7001 shorted, improving jump behaviour, and TS7004
  deleted.
- **Level 3** — C2024 (10 pF) added, to stop IC7100 oscillating.

Full tables, with service code numbers:
[chapter 8, module M](../../service-information/modification-levels.md#mod-m).

## Related

- [Module circuit descriptions](../../circuit-description/modules.md#module-m) — the chapter 7 text in full
- [Modification levels per module](../../service-information/modification-levels.md#mod-m) — three levels of changes, one of them a reversal
- [Fault symptoms](../../service-information/fault-symptoms.md) — the playability entries reach this module
- [Software releases](../../service-information/software-releases.md) — drive software 6803.5, which the level-2 change depends on
- [The optical deck](../../circuit-description/optical-deck.md) — the radial mirror itself
- [Module R — Drive processor](../r-drive-processor/index.md) — supplies `RLS`, `CP1` and `CP2`
- [Electrical parts](../../parts/electrical-parts.md) — the collective list of standard components by service code number; the connectors are in [mechanical parts](../../parts/mechanical-parts.md#module-connectors)
