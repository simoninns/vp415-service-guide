---
title: Module L - Video drop-out correction
description: >-
  Video drop-out detection and correction.
---

<!-- drafted by tools/import_modules.py - hand-edited afterwards -->

# Module L - Video drop-out correction

Video drop-out detection and correction.

## Overview

| | |
| --- | --- |
| Designation | **L** |
| Modification levels | 0 → 1 |
| Circuit diagram | `CS 6 878`, page 056 |
| Data sheet | `CS 7 848`, page 057 |

## The board

<div class="sheet-pair" markdown>
<figure class="sheet sheet--photo" markdown>
[![Module L, component side of the board](assets/web/l-video-dropout-correction-top-preview.webp)](assets/web/l-video-dropout-correction-top-zoom.webp)
<figcaption>
  Module L, component side.
</figcaption>
</figure>
<figure class="sheet sheet--photo" markdown>
[![Module L, solder side of the board](assets/web/l-video-dropout-correction-bottom-preview.webp)](assets/web/l-video-dropout-correction-bottom-zoom.webp)
<figcaption>
  Module L, solder side.
</figcaption>
</figure>
</div>

## Where it sits in the player

See the [module and connector lay-out](../../system/module-layout.md).

## Circuit description

[Chapter 7, module L](../../circuit-description/modules.md#module-l).

## Adjustments

# Required

Scope

Test disc

# Adjustment conditions

Load test disc.

Still picture, picture no. 10800.

# Adjustments

1) R3065, L5007 (Delay 64 µs)

- Picture no. 10800 is visible on the picture screen as shown in fig. L1.

DROP OUT SIGNALS

Fig. L1

MDA:00589

- Adjust L5007 until drop-out A gives a white completion of the vertical lines at the right place and drop-out B gives minimum distortion at the place indicated.
- Adjust R3065 until drop-out B is invisible and drop-out C causes a black line without any white stripes or dots.

2) L5003, R3050 (MTF)

- Search for picture no. 1000 (blue).
- Using the scope, measure the CVBS OUT-signal on BNC3 (rear), 75Ω terminated, triggered line frequent.
- Switch SK2 on Analog I/O module U in pos. NOT ENCODED (pressed).
- Adjust L5003 for min. amplitude of the chroma signal.
- Measure the CVBS OUT-signal (NOT ENCODED) on BNC3 with the scope and search the multi-burst signal in the VITS (line 20) by means of the delayed time base (see fig. L2).

VITS SIGNALS LINE 20

Fig. L2

MDA:00589

- Adjust R3050 until the amplitude of MBI = MBIV.

# Adjustment when item replaced

replaced

Components in CLOCK GEN.

IC7203

adjust

L5007

R3065, R3050

## Circuit diagram

<figure class="sheet sheet--fold" markdown>
[![Video drop-out correction module L - circuit diagram](assets/web/cs-6-878-circuit-p056-preview.webp)](assets/web/cs-6-878-circuit-p056-zoom.webp)
<figcaption>
  Video drop-out correction module L - circuit diagram.
  <span class="cs">CS 6 878</span>
  <span class="src">service manual page 056</span>
</figcaption>
</figure>

## PCB lay-out

<figure class="sheet sheet--fold" markdown>
[![Video drop-out correction module L (mod level 0) - adjustments / PCB / parts](assets/web/cs-7-848-module-sheet-p057-preview.webp)](assets/web/cs-7-848-module-sheet-p057-zoom.webp)
<figcaption>
  Video drop-out correction module L (mod level 0) - adjustments / PCB / parts.
  <span class="cs">CS 7 848</span>
  <span class="src">service manual page 057</span>
</figcaption>
</figure>

## List of electrical parts

**Delay lines**

| Item | Service code number | Value | Rating |
| --- | --- | --- | --- |
| 5001 | 4822 320 40081 | DL470NS |  |

**Coils**

| Item | Service code number | Value | Rating |
| --- | --- | --- | --- |
| 5002 | 4822 157 52869 | 34 µH |  |
| 5003 | 4822 156 11003 | 12 µH |  |
| 5004 | 4822 156 11007 | 212 µH |  |
| 5005 | 4822 156 11007 | 212 µH |  |
| 5006 | 4822 156 21324 | 100 µH |  |
| 5007 | 4822 156 10997 | 1.7 µH |  |

**Potentiometers**

| Item | Service code number | Value | Rating |
| --- | --- | --- | --- |
| 3050 | 4822 100 11087 | 2.2 kΩ |  |
| 3065 | 4822 100 20151 | 1 kΩ |  |

**Capacitors**

| Item | Service code number | Value | Rating |
| --- | --- | --- | --- |
| 2001 | 4822 122 32082 | 4.7 µF |  |
| 2002 | 4822 124 22027 | 47 µF | 25 V |
| 2003 | 4822 122 31759 | 22 nF |  |
| 2004 | 5322 124 21749 | 10 µF | 63 V |
| 2005 | 5322 124 21749 | 10 µF | 63 V |
| 2006 | 4822 121 41608 | 100 nF | 100 V |
| 2007 | 4822 122 31759 | 22 nF |  |
| 2008 | 4822 122 31759 | 22 nF |  |
| 2009 | 4822 122 32975 | 470 pF |  |
| 2010 | 4822 122 32974 | 100 pF |  |
| 2011 | 4822 122 31759 | 22 nF |  |
| 2012 | 4822 122 31839 | 82 pF |  |
| 2013 | 5322 122 31847 | 1 nF |  |
| 2014 | 4822 122 31759 | 22 nF |  |
| 2015 | 4822 124 22027 | 47 µF | 25 V |
| 2016 | 4822 124 22029 | 2.2 µF | 63 V |
| 2017 | 4822 122 32974 | 100 pF |  |
| 2018 | 4822 122 32974 | 100 pF |  |
| 2019 | 4822 122 31759 | 22 nF |  |
| 2020 | 4822 121 41719 | 1 µF | 10% 100 V |
| 2021 | 4822 122 32442 | 10 nF |  |
| 2022 | 4822 122 32442 | 10 nF |  |
| 2023 | 4822 122 31759 | 22 nF |  |
| 2024 | 4822 124 22031 | 4.7 µF | 63 V |
| 2025 | 4822 124 22028 | 1 µF | 63 V |
| 2026 | 4822 122 31759 | 22 nF |  |
| 2027 | 4822 121 41608 | 100 nF | 100 V |
| 2028 | 4822 122 32974 | 100 pF |  |
| 2029 | 4822 122 32974 | 100 pF |  |
| 2030 | 4822 122 31759 | 22 nF |  |
| 2031 | 4822 124 22027 | 47 µF | 25 V |
| 2032 | 4822 121 41785 | 270 nF | 10% 100 V |
| 2033 | 4822 122 31759 | 22 nF |  |
| 2034 | 4822 122 32482 | 22 pF |  |
| 2035 | 4822 122 31759 | 22 nF |  |
| 2036 | 4822 122 31759 | 22 nF |  |
| 2037 | 4822 122 31759 | 22 nF |  |
| 2038 | 4822 122 31839 | 82 pF |  |
| 2039 | 4822 122 31759 | 22 nF |  |

## Modification levels

[Chapter 8, module L](../../service-information/modification-levels.md#mod-l).

## Related

- [Module circuit descriptions](../../circuit-description/modules.md)
- [VP400 series architecture](../../circuit-description/vp400-series.md)
- [Adjustments](../../general-service/adjustments.md)
- [Fault symptoms](../../service-information/fault-symptoms.md)
- [Modification levels per module](../../service-information/modification-levels.md)
- [Module and connector lay-out](../../system/module-layout.md)
