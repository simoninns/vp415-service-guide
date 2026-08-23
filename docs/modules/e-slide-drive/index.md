---
title: Module E - Slide drive
description: >-
  Slide (carriage) drive for coarse radial positioning.
---

# Module E - Slide drive

Slide (carriage) drive for coarse radial positioning.

## Overview

The slide drive module drives the slide motor, which moves the laser detection
unit under the disc so that the tracks can be read. The slide is driven by a
**stepping motor**, and each step moves it by roughly **50 track spaces**.

| | |
| --- | --- |
| Designation | **E** — slide drive |
| Modification levels | 3 (unchanged through production) |
| Data sheet | `CS 7 841`, page 042 |
| Circuit diagram | `CS 6 871`, page 043 |
| Connectors | `E1`, `E2` |
| Driven by | [drive processor module R](../r-drive-processor/index.md) — `COMM 1-4` and `SL-PWR` |

## The board

<div class="sheet-pair" markdown>
<figure class="sheet sheet--photo" markdown>
[![Module E, component side of the board](assets/web/e-slide-drive-top-preview.webp)](assets/web/e-slide-drive-top-zoom.webp)
<figcaption>
  Module E, component side.
</figcaption>
</figure>
<figure class="sheet sheet--photo" markdown>
[![Module E, solder side of the board](assets/web/e-slide-drive-bottom-preview.webp)](assets/web/e-slide-drive-bottom-zoom.webp)
<figcaption>
  Module E, solder side.
</figcaption>
</figure>
</div>

## Where it sits in the player

Lying flat across the front of the chassis, first of the row
E–[F](../f-motor-sequence/index.md)–[G](../g-genlock/index.md)–[H](../h-etbc-b/index.md)–[I](../i-etbc-c/index.md)
— see the [module and connector lay-out](../../system/module-layout.md).

## Circuit description

The motor coils are switched by pulses on `COMM 1-4`. `SL-PWR` selects between
holding power and moving power through an astable multivibrator built around
transistors 7002 and 7003 — the coils are held at a lower current when the
slide is stationary, so the motor does not cook. All the drive signals come
from [drive processor module R](../r-drive-processor/index.md).

The full text is in
[chapter 7, module E](../../circuit-description/modules.md#module-e).

## Adjustments

The manual gives **no adjustment procedure** for this module: the data sheet
carries only the PCB lay-out and the parts list.

## Circuit diagram

<figure class="sheet sheet--fold" markdown>
[![Slide drive module E - circuit diagram](assets/web/cs-6-871-circuit-p043-preview.webp)](assets/web/cs-6-871-circuit-p043-zoom.webp)
<figcaption>
  Slide drive module E - circuit diagram.
  <span class="cs">CS 6 871</span>
  <span class="src">service manual page 043</span>
</figcaption>
</figure>

## PCB lay-out

<figure class="sheet sheet--fold" markdown>
[![Slide drive module E (mod level 3) - PCB / parts](assets/web/cs-7-841-module-sheet-p042-preview.webp)](assets/web/cs-7-841-module-sheet-p042-zoom.webp)
<figcaption>
  Slide drive module E (mod level 3) - PCB / parts.
  <span class="cs">CS 7 841</span>
  <span class="src">service manual page 042</span>
</figcaption>
</figure>

## List of electrical parts

**NFR25 Resistors**

| Item | Service code number | Value | Rating |
| --- | --- | --- | --- |
| 3026 | 4822 111 30483 | 1 Ω |  |
| 3027 | 4822 111 30483 | 1 Ω |  |

**Capacitors**

| Item | Service code number | Value | Rating |
| --- | --- | --- | --- |
| 2001 | 4822 122 30053 | 680 pF | 100 V |
| 2002 | 4822 121 50959 | 3.9 nF | 63 V |
| 2007 | 4822 124 22027 | 47 μF | 25 V |
| 2008 | 4822 124 22027 | 47 μF | 25 V |

## Modification levels

Module E carried **modification level 3 in every production batch** and has no
mod-level sheet in chapter 8 — nothing about it changed that needed
documenting.

## Related

- [Module circuit descriptions](../../circuit-description/modules.md#module-e) — the chapter 7 text in full
- [The optical deck](../../circuit-description/optical-deck.md) — what the slide is moving, and why
- [Fault-finding charts](../../repair/fault-finding.md) — slide and start-up faults
- [Module and connector lay-out](../../system/module-layout.md) — connector positions
