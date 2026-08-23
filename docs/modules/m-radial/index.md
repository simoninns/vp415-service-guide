---
title: Module M - Radial
description: >-
  Radial servo: fine tracking and jump control.
---

<!-- drafted by tools/import_modules.py - hand-edited afterwards -->

# Module M - Radial

Radial servo: fine tracking and jump control.

## Overview

| | |
| --- | --- |
| Designation | **M** |
| Modification levels | 0 → 3 |
| Data sheet | `CS 7 849`, page 058 |
| Circuit diagram | `CS 6 879`, page 059 |

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

See the [module and connector lay-out](../../system/module-layout.md).

## Circuit description

[Chapter 7, module M](../../circuit-description/modules.md#module-m).

## Adjustments

None.

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

[Chapter 8, module M](../../service-information/modification-levels.md#mod-m).

## Related

- [Module circuit descriptions](../../circuit-description/modules.md)
- [VP400 series architecture](../../circuit-description/vp400-series.md)
- [Fault symptoms](../../service-information/fault-symptoms.md)
- [Modification levels per module](../../service-information/modification-levels.md)
- [Module and connector lay-out](../../system/module-layout.md)
