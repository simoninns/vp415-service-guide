---
title: Module J - Focus
description: >-
  Focus servo for the objective lens.
---

<!-- drafted by tools/import_modules.py - hand-edited afterwards -->

# Module J - Focus

Focus servo for the objective lens.

## Overview

| | |
| --- | --- |
| Designation | **J** |
| Modification levels | 2 → 4 |
| Circuit diagram | `CS 6 876`, page 052 |
| Data sheet | `CS 7 846`, page 053 |

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

See the [module and connector lay-out](../../system/module-layout.md).

## Circuit description

[Chapter 7, module J](../../circuit-description/modules.md#module-j).

## Adjustments

None.

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

[Chapter 8, module J](../../service-information/modification-levels.md#mod-j).

## Related

- [The LaserVision system](../../circuit-description/laservision-system.md)
- [Module circuit descriptions](../../circuit-description/modules.md)
- [VP400 series architecture](../../circuit-description/vp400-series.md)
- [Fault-finding charts](../../repair/fault-finding.md)
- [Modification levels per module](../../service-information/modification-levels.md)
- [Module and connector lay-out](../../system/module-layout.md)
