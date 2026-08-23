---
title: Module K - HF processor
description: >-
  HF processing of the raw signal off the disc.
---

<!-- drafted by tools/import_modules.py - hand-edited afterwards -->

# Module K - HF processor

HF processing of the raw signal off the disc.

## Overview

| | |
| --- | --- |
| Designation | **K** |
| Modification levels | 0 |
| Data sheet | `CS 7 847`, page 054 |
| Circuit diagram | `CS 6 877`, page 055 |

## The board

<div class="sheet-pair" markdown>
<figure class="sheet sheet--photo" markdown>
[![Module K, component side of the board](assets/web/k-hf-processor-top-preview.webp)](assets/web/k-hf-processor-top-zoom.webp)
<figcaption>
  Module K, component side.
</figcaption>
</figure>
<figure class="sheet sheet--photo" markdown>
[![Module K, solder side of the board](assets/web/k-hf-processor-bottom-preview.webp)](assets/web/k-hf-processor-bottom-zoom.webp)
<figcaption>
  Module K, solder side.
</figcaption>
</figure>
</div>

## Where it sits in the player

See the [module and connector lay-out](../../system/module-layout.md).

## Circuit description

[Chapter 7, module K](../../circuit-description/modules.md#module-k).

## Adjustments

# Required

Test disc

Scope

HF generator (100 kHz - 10 MHz)

# Adjustment conditions

Load test disc

Still picture, picture no. 6200

# Adjustments

1) R3043 (Video amplitude)

- Using the scope, measure the CVBS OUT-signal on BNC3 (rear), 75Ω terminated.
- Switch SK2 on Analog I/O module U in pos. NOT ENCODED (pressed).
- Adjust R3043 until this signal is 1 Vpp ± 50 mV
- Switch SK2 back into the earlier position.

2) L5001, L5002, L5004 (Audio dip 0,875 MHz, MTF, Audio dip 2,8 MHz)

- Switch the drive into STANDBY mode.
- Connect an HF generator signal with an amplitude of 0.8 Vpp to 3K2.
- Measure the signal on 5-IC7201-2A with the scope.
- Set the generator to a frequency of 875 kHz and adjust L5001 for minimum amplitude of the scope signal.
- Set the generator to a frequency of 8 MHz and an amplitude of 40 mV and adjust L5002 for maximum amplitude of the scope signal.
- Measure the signal on 1K1 (HF-AUD) with the scope.
- Set the generator to a frequency of 2.8 MHz and an amplitude of 20 mV and adjust L5004 for minimum amplitude of the scope signal.

# Adjustment when item replaced

replaced

IC7201

adjust

R3043

## Circuit diagram

<figure class="sheet sheet--fold" markdown>
[![HF processor module K - circuit diagram](assets/web/cs-6-877-circuit-p055-preview.webp)](assets/web/cs-6-877-circuit-p055-zoom.webp)
<figcaption>
  HF processor module K - circuit diagram.
  <span class="cs">CS 6 877</span>
  <span class="src">service manual page 055</span>
</figcaption>
</figure>

## PCB lay-out

<figure class="sheet sheet--fold" markdown>
[![HF processor module K (mod level 0) - adjustments / PCB / parts](assets/web/cs-7-847-module-sheet-p054-preview.webp)](assets/web/cs-7-847-module-sheet-p054-zoom.webp)
<figcaption>
  HF processor module K (mod level 0) - adjustments / PCB / parts.
  <span class="cs">CS 7 847</span>
  <span class="src">service manual page 054</span>
</figcaption>
</figure>

## List of electrical parts

**Coils**

| Item | Service code number | Value | Rating |
| --- | --- | --- | --- |
| 5001 | 4822 156 10994 | 87 μH |  |
| 5002 | 4822 156 21147 | 7.2 μH |  |
| 5003 | 4822 156 11011 | 2.6 μH |  |
| 5004 | 4822 156 10994 | 87 μH |  |
| 5005 | 4822 156 10999 | 4.2 μH |  |
| 5006 | 4822 156 21026 | 34 μH |  |
| 5007 | 4822 157 52871 | 25 μH |  |
| 5008 | 4822 157 52871 | 25 μH |  |

**Potentiometers**

| Item | Service code number | Value | Rating |
| --- | --- | --- | --- |
| 3043 | 5322 101 10481 | 1 kΩ |  |

**Fuse Resistors**

| Item | Service code number | Value | Rating |
| --- | --- | --- | --- |
| 3041 | 4822 111 30847 | 22 Ω |  |

**PCB-5-067**

| Item | Service code number | Value | Rating |
| --- | --- | --- | --- |
| 2001 | 4822 122 31759 | 22 nF |  |
| 2002 | 4822 124 22027 | 47 μF | 25 V |
| 2003 | 4822 122 31759 | 22 nF |  |
| 2004 | 4822 122 33002 | 68 pF |  |
| 2005 | 4822 122 31727 | 470 pF |  |
| 2006 | 4822 122 31839 | 82 pF |  |
| 2007 | 4822 122 32442 | 10 nF |  |
| 2008 | 4822 122 31759 | 22 nF |  |
| 2009 | 4822 122 31774 | 56 pF |  |
| 2010 | 4822 122 32506 | 5.6 pF |  |
| 2011 | 4822 122 31759 | 22 nF |  |
| 2012 | 4822 122 32442 | 10 nF |  |
| 2013 | 4822 122 31759 | 22 nF |  |
| 2014 | 4822 122 31839 | 82 pF |  |
| 2015 | 4822 122 32974 | 100 pF |  |
| 2016 | 4822 122 31965 | 220 pF |  |
| 2017 | 4822 122 32142 | 270 pF |  |
| 2018 | 4822 122 31759 | 22 nF |  |
| 2019 | 4822 122 31965 | 220 pF |  |
| 2020 | 4822 122 31772 | 47 pF |  |
| 2021 | 4822 122 32976 | 470 pF |  |
| 2022 | 4822 122 31759 | 22 nF |  |
| 2023 | 4822 124 22027 | 47 μF | 25 V |
| 2024 | 4822 122 32442 | 10 nF |  |
| 2025 | 4822 122 31774 | 56 pF |  |
| 2026 | 4822 122 31774 | 56 pF |  |
| 2027 | 4822 124 22027 | 47 μF | 25 V |
| 2028 | 4822 122 31759 | 22 nF |  |
| 2029 | 4822 122 31644 | 2.2 nF |  |
| 2030 | 4822 122 31759 | 22 nF |  |
| 2031 | 4822 122 31759 | 22 nF |  |
| 2032 | 4822 122 31769 | 18 pF |  |
| 2033 | 4822 122 31769 | 18 pF |  |
| 2034 | 4822 122 31759 | 22 nF |  |
| 2035 | 4822 122 32975 | 33 pF |  |
| 2036 | 4822 122 32505 | 2.7 pF |  |
| 2037 | 4822 122 31774 | 56 pF |  |
| 2038 | 4822 122 32504 | 15 pF |  |
| 2039 | 4822 122 31774 | 56 pF |  |
| 2040 | 4822 122 32139 | 12 pF |  |
| 2041 | 4822 122 31966 | 27 pF |  |
| 2042 | 4822 124 22027 | 47 μF | 25 V |
| 2043 | 5322 122 32072 | 33 pF |  |

## Modification levels

[Chapter 8, module K](../../service-information/modification-levels.md#mod-k).

## Related

- [Module circuit descriptions](../../circuit-description/modules.md)
- [VP400 series architecture](../../circuit-description/vp400-series.md)
- [Adjustments](../../general-service/adjustments.md)
- [Fault symptoms](../../service-information/fault-symptoms.md)
- [Modification levels per module](../../service-information/modification-levels.md)
- [Module and connector lay-out](../../system/module-layout.md)
