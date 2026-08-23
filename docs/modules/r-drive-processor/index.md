---
title: Module R - Drive processor
description: >-
  Drive processor: the microcontroller running the deck servos.
---

<!-- drafted by tools/import_modules.py - hand-edited afterwards -->

# Module R - Drive processor

Drive processor: the microcontroller running the deck servos.

## Overview

| | |
| --- | --- |
| Designation | **R** |
| Modification levels | 3 → 7 |
| Parts list | `CS 7 851`, pages 063, 064, panels 2+3 |
| Circuit diagram | `CS 6 883`, pages 065, 066 |

## The board

<div class="sheet-pair" markdown>
<figure class="sheet sheet--photo" markdown>
[![Module R, component side of the board](assets/web/r-drive-processor-top-preview.webp)](assets/web/r-drive-processor-top-zoom.webp)
<figcaption>
  Module R, component side.
</figcaption>
</figure>
<figure class="sheet sheet--photo" markdown>
[![Module R, solder side of the board](assets/web/r-drive-processor-bottom-preview.webp)](assets/web/r-drive-processor-bottom-zoom.webp)
<figcaption>
  Module R, solder side.
</figcaption>
</figure>
</div>

## Where it sits in the player

See the [module and connector lay-out](../../system/module-layout.md).

## Circuit description

[Chapter 7, module R](../../circuit-description/modules.md#module-r).

## Adjustments

None.

## Circuit diagram

<figure class="sheet sheet--fold" markdown>
[![Drive processor module R - circuit diagram](assets/web/cs-6-883-circuit-p065-066-preview.webp)](assets/web/cs-6-883-circuit-p065-066-zoom.webp)
<figcaption>
  Drive processor module R - circuit diagram.
  <span class="cs">CS 6 883</span>
  <span class="src">service manual pages 065, 066</span>
</figcaption>
</figure>

## PCB lay-out

<figure class="sheet sheet--fold" markdown>
[![RC5 circuit module Q; list of electrical parts module R](assets/web/cs-7-851-circuit-p063-064-preview.webp)](assets/web/cs-7-851-circuit-p063-064-zoom.webp)
<figcaption>
  RC5 circuit module Q; list of electrical parts module R.
  <span class="cs">CS 7 851</span>
  <span class="src">service manual pages 063, 064</span>
</figcaption>
</figure>

## List of electrical parts

**Eproms (programmed)**

| Item | Service code number | Value | Rating |
| --- | --- | --- | --- |
| 7204 | 4822 209 51257 | TMS 27128 drive |  |

**Crystals**

| Item | Service code number | Value | Rating |
| --- | --- | --- | --- |
| 5001 | 4822 242 71663 | 12 MHz |  |

**Coils**

| Item | Service code number | Value | Rating |
| --- | --- | --- | --- |
| 5002 | 4822 158 10101 | 5.3 μH |  |
| 5003 | 4822 158 10101 | 5.3 μH |  |
| 5004 | 4822 157 51316 | 120 μH |  |

**Hours counter**

| Item | Service code number | Value | Rating |
| --- | --- | --- | --- |
| 2001 | 4822 124 22027 | 47 μF | 25 V |
| 2002 | 4822 124 22027 | 47 μF | 25 V |
| 2003 | 4822 124 22027 | 47 μF | 25 V |
| 2004 | 4822 124 22029 | 2.2 μF | 63 V |
| 2005 | 4822 122 31644 | 2.2 nF |  |
| 2006 | 4822 122 32975 | 33 pF |  |
| 2007 | 4822 122 32975 | 33 pF |  |
| 2008 | 4822 122 31972 | 39 pF |  |
| 2009 | 4822 122 32504 | 15 pF |  |
| 2010 | 4822 122 32482 | 22 pF |  |
| 2011 | 4822 122 31759 | 22 nF |  |
| 2012 | 4822 122 31759 | 22 nF |  |
| 2013 | 4822 122 31759 | 22 nF |  |
| 2014 | 4822 122 31759 | 22 nF |  |
| 2015 | 4822 122 31759 | 22 nF |  |
| 2016 | 5322 121 54072 | 820 pF | 250 V |
| 2017 | 5322 121 54072 | 820 pF | 250 V |
| 2018 | 4822 124 22187 | 15 pF | 63 V |
| 2101 | 4822 122 31759 | 22 nF |  |
| 2102 | 4822 122 31759 | 22 nF |  |
| 2103 | 4822 122 31759 | 22 nF |  |
| 2104 | 4822 122 31759 | 22 nF |  |
| 2105 | 4822 122 31759 | 22 nF |  |
| 2106 | 4822 122 31759 | 22 nF |  |
| 2107 | 4822 122 31759 | 22 nF |  |
| 2108 | 4822 122 31759 | 22 nF |  |
| 2109 | 4822 122 31759 | 22 nF |  |
| 2110 | 4822 122 31759 | 22 nF |  |
| 2111 | 4822 122 31759 | 22 nF |  |
| 2112 | 4822 122 31759 | 22 nF |  |
| 2113 | 4822 122 31759 | 22 nF |  |
| 2114 | 4822 122 31759 | 22 nF |  |
| 2115 | 4822 122 31759 | 22 nF |  |
| 2116 | 4822 122 31759 | 22 nF |  |
| 2117 | 4822 122 31759 | 22 nF |  |
| 2118 | 4822 122 31759 | 22 nF |  |
| 2119 | 4822 122 31759 | 22 nF |  |
| 2120 | 4822 122 31759 | 22 nF |  |
| 2121 | 4822 122 31759 | 22 nF |  |
| 2122 | 4822 122 31759 | 22 nF |  |
| 3065 | 4822 344 40081 | Hours counter |  |

## Modification levels

[Chapter 8, module R](../../service-information/modification-levels.md#mod-r).

## Related

- [Module circuit descriptions](../../circuit-description/modules.md)
- [VP400 series architecture](../../circuit-description/vp400-series.md)
- [Modification levels](../../general-service/modification-levels.md)
- [Diagnostic mode](../../repair/diagnostic-mode.md)
- [Fault-finding charts](../../repair/fault-finding.md)
- [Fault symptoms](../../service-information/fault-symptoms.md)
- [Modification levels per module](../../service-information/modification-levels.md)
- [Software releases](../../service-information/software-releases.md)
- [Module and connector lay-out](../../system/module-layout.md)
