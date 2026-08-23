---
title: Module S - Control
description: >-
  Control: the player's main microcontroller and watchdog.
---

<!-- drafted by tools/import_modules.py - hand-edited afterwards -->

# Module S - Control

Control: the player's main microcontroller and watchdog.

## Overview

| | |
| --- | --- |
| Designation | **S** |
| Modification levels | 3 → 8 |
| Circuit diagram | `CS 6 884`, pages 067, 068 |
| Data sheet | `CS 7 852`, pages 069, 070 |

## The board

<div class="sheet-pair" markdown>
<figure class="sheet sheet--photo" markdown>
[![Module S, component side of the board](assets/web/s-control-top-preview.webp)](assets/web/s-control-top-zoom.webp)
<figcaption>
  Module S, component side.
</figcaption>
</figure>
<figure class="sheet sheet--photo" markdown>
[![Module S, solder side of the board](assets/web/s-control-bottom-preview.webp)](assets/web/s-control-bottom-zoom.webp)
<figcaption>
  Module S, solder side.
</figcaption>
</figure>
</div>

## Where it sits in the player

See the [module and connector lay-out](../../system/module-layout.md).

## Circuit description

[Chapter 7, module S](../../circuit-description/modules.md#module-s).

## Adjustments

None.

## Circuit diagram

<figure class="sheet sheet--fold" markdown>
[![Control module S - circuit diagram](assets/web/cs-6-884-circuit-p067-068-preview.webp)](assets/web/cs-6-884-circuit-p067-068-zoom.webp)
<figcaption>
  Control module S - circuit diagram.
  <span class="cs">CS 6 884</span>
  <span class="src">service manual pages 067, 068</span>
</figcaption>
</figure>

## PCB lay-out

<figure class="sheet sheet--fold" markdown>
[![Control module S (mod level 3) - parts](assets/web/cs-7-852-module-sheet-p069-070-preview.webp)](assets/web/cs-7-852-module-sheet-p069-070-zoom.webp)
<figcaption>
  Control module S (mod level 3) - parts.
  <span class="cs">CS 7 852</span>
  <span class="src">service manual pages 069, 070</span>
</figcaption>
</figure>

## List of electrical parts

**Eproms (programmed)**

| Item | Service code number | Value | Rating |
| --- | --- | --- | --- |
| 7202 | 4822 209 51256 | TMS 27512_control |  |

**Batteries**

| Item | Service code number | Value | Rating |
| --- | --- | --- | --- |
| 1002 | 4822 138 10032 | Battery 2.4 V |  |

**Crystals**

| Item | Service code number | Value | Rating |
| --- | --- | --- | --- |
| 5101 | 4822 242 70917 | 11.059 MHz |  |
| 5102 | 4822 242 70668 | 4 MHz |  |

**Coils**

| Item | Service code number | Value | Rating |
| --- | --- | --- | --- |
| 5001 | 4822 158 10101 | 5.3 μH |  |
| 5002 | 4822 158 10101 | 5.3 μH |  |
| 5003 | 4822 158 10101 | 5.3 μH |  |

**NFR25 Resistors**

| Item | Service code number | Value | Rating |
| --- | --- | --- | --- |
| 3028 | 4822 111 30483 | 1 Ω |  |

**Capacitors**

| Item | Service code number | Value | Rating |
| --- | --- | --- | --- |
| 2001 | 4822 124 22027 | 47 μF | 25 V |
| 2002 | 5322 124 21749 | 10 μF | 63 V |
| 2003 | 5322 124 21749 | 10 μF | 63 V |
| 2004 | 4822 122 31759 | 22 nF |  |
| 2005 | 4822 122 31759 | 22 nF |  |
| 2006 | 4822 122 31759 | 22 nF |  |
| 2007 | 4822 124 22027 | 47 μF | 25 V |
| 2008 | 4822 124 22029 | 2.2 μF | 63 V |
| 2009 | 4822 124 22027 | 47 μF | 25 V |
| 2010 | 4822 122 31759 | 22 nF |  |
| 2011 | 4822 122 31644 | 2.2 nF |  |
| 2012 | 4822 122 31966 | 27 pF |  |
| 2013 | 4822 122 31966 | 27 pF |  |
| 2014 | 4822 122 32976 | 470 pF |  |
| 2015 | 4822 122 32976 | 470 pF |  |
| 2016 | 4822 122 32975 | 33 pF |  |
| 2017 | 4822 122 32975 | 33 pF |  |
| 2018 | 4822 122 33009 | 270 nF | 25 V |
| 2019 | 4822 122 31644 | 2.2 nF |  |
| 2020 | 4822 122 32482 | 22 pF |  |
| 2021 | 4822 122 32482 | 22 pF |  |
| 2023 | 4822 124 22028 | 1 μF | 63 V |
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

## Modification levels

[Chapter 8, module S](../../service-information/modification-levels.md#mod-s).

## Related

- [Module circuit descriptions](../../circuit-description/modules.md)
- [VP400 series architecture](../../circuit-description/vp400-series.md)
- [Modification levels](../../general-service/modification-levels.md)
- [Fault-finding charts](../../repair/fault-finding.md)
- [Modification levels per module](../../service-information/modification-levels.md)
- [Software releases](../../service-information/software-releases.md)
- [Module and connector lay-out](../../system/module-layout.md)
