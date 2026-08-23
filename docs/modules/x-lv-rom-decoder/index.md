---
title: Module X - LV-ROM decoder
description: >-
  LV-ROM decoder: recovering data from the disc's data tracks.
---

<!-- drafted by tools/import_modules.py - hand-edited afterwards -->

# Module X - LV-ROM decoder

LV-ROM decoder: recovering data from the disc's data tracks.

## Overview

| | |
| --- | --- |
| Designation | **X** |
| Modification levels | 2 |
| Data sheet | `CS 7 859`, pages 091, 092 |
| Circuit diagram | `CS 6 891`, page 093 |

## The board

<div class="sheet-pair" markdown>
<figure class="sheet sheet--photo" markdown>
[![Module X, component side of the board](assets/web/x-lv-rom-decoder-top-preview.webp)](assets/web/x-lv-rom-decoder-top-zoom.webp)
<figcaption>
  Module X, component side.
</figcaption>
</figure>
<figure class="sheet sheet--photo" markdown>
[![Module X, solder side of the board](assets/web/x-lv-rom-decoder-bottom-preview.webp)](assets/web/x-lv-rom-decoder-bottom-zoom.webp)
<figcaption>
  Module X, solder side.
</figcaption>
</figure>
</div>

## Where it sits in the player

See the [module and connector lay-out](../../system/module-layout.md).

## Circuit description

[Chapter 7, module X](../../circuit-description/modules.md#module-x).

## Adjustments

# Required

Frequency counter

# Adjustment conditions

Stand-by position of the set

# Adjustments

1) L5501 (Demod. freq.)

- Short-circuit pin 6-IC6501 to ground.
- Measure with the frequency counter on 22-IC6501 (clock)
- Adjust L5501 for a frequency of 4.32 MHz ± 1 kHz. (the voltage on junction R3510/R3511 should than be 5 V ± 0.1 V).
- Remove the short circuit of pin 6.

## Circuit diagram

<figure class="sheet sheet--fold" markdown>
[![LV-ROM decoder module X - circuit diagram](assets/web/cs-6-891-circuit-p093-preview.webp)](assets/web/cs-6-891-circuit-p093-zoom.webp)
<figcaption>
  LV-ROM decoder module X - circuit diagram.
  <span class="cs">CS 6 891</span>
  <span class="src">service manual page 093</span>
</figcaption>
</figure>

## PCB lay-out

<figure class="sheet sheet--fold" markdown>
[![LV-ROM decoder module X (mod level 3) - adjustments / PCB / parts](assets/web/cs-7-859-module-sheet-p091-092-preview.webp)](assets/web/cs-7-859-module-sheet-p091-092-zoom.webp)
<figcaption>
  LV-ROM decoder module X (mod level 3) - adjustments / PCB / parts.
  <span class="cs">CS 7 859</span>
  <span class="src">service manual pages 091, 092</span>
</figcaption>
</figure>

## List of electrical parts

**Crystals**

| Item | Service code number | Value | Rating |
| --- | --- | --- | --- |
| 5601 | 4822 242 71461 | 4.2336 MHz |  |

**Coils**

| Item | Service code number | Value | Rating |
| --- | --- | --- | --- |
| 5501 | 4822 156 21155 | 7.95 μH |  |
| 5503 | 4822 156 20966 | 47 μH |  |
| 5504 | 4822 156 20966 | 47 μH |  |
| 5505 | 4822 156 20966 | 47 μH |  |
| 5506 | 4822 158 10101 | 5.3 μH |  |
| 5507 | 4822 158 10101 | 5.3 μH |  |
| 5508 | 4822 158 10101 | 5.3 μH |  |
| 5701 | 4822 156 21026 | 34 μH |  |
| 5702 | 4822 156 11005 | 42.5 μH |  |
| 5703 | 4822 156 11005 | 42.5 μH |  |
| 5704 | 4822 156 21113 | 52 μH |  |

**NFR25 Resistors**

| Item | Service code number | Value | Rating |
| --- | --- | --- | --- |
| 3549 | 4822 111 30492 | 2.2 Ω |  |

**Capacitors**

| Item | Service code number | Value | Rating |
| --- | --- | --- | --- |
| 2501 |  |  |  |
| 2502 |  |  |  |
| 2505 |  |  |  |
| 2506 |  |  |  |
| 2507 |  |  |  |
| 2508 |  |  |  |
| 2511 |  |  |  |
| 2512 |  |  |  |
| 2513 |  |  |  |
| 2514 |  |  |  |
| 2515 |  |  |  |
| 2519 |  |  |  |
| 2520 |  |  |  |
| 2521 |  |  |  |
| 2522 |  |  |  |
| 2523 |  |  |  |
| 2525 |  |  |  |
| 2527 |  |  |  |
| 2538 |  |  |  |
| 2539 |  |  |  |
| 2540 |  |  |  |
| 2541 |  |  |  |

**Other**

| Item | Service code number | Value | Rating |
| --- | --- | --- | --- |
|  | 4822 121 51099 | 22 nF | 63 V |
|  | 4822 122 31759 | 22 nF |  |
|  | 4822 121 51099 | 22 nF | 63 V |
|  | 5322 124 21643 | 22 μF | 40 V |
|  | 4822 122 31644 | 2.2 nF |  |
|  | 4822 122 31759 | 22 nF |  |
|  | 4822 122 31644 | 2.2 nF |  |
|  | 4822 122 31759 | 22 nF |  |
|  | 5322 124 21643 | 22 μF | 40 V |
|  | 4822 122 31759 | 22 nF |  |
|  | 4822 122 31974 | 820 pF |  |
|  | 4822 121 41608 | 100 nF | 100 V |
|  | 4822 122 31759 | 22 nF |  |
|  | 4822 121 41608 | 100 nF | 100 V |
|  | 4822 122 31759 | 22 nF |  |
|  | 5322 124 21643 | 22 μF | 40 V |
|  | 5322 124 21643 | 22 μF | 40 V |
|  | 4822 121 41936 | 2.2 μF | 10% 100 V |
|  | 4822 122 31759 | 22 nF |  |
|  | 4822 122 31759 | 22 nF |  |
|  | 4822 124 22028 | 1 μF | 63 V |
|  | 4822 122 31965 | 220 pF |  |
|  | 5322 124 21643 | 22 μF | 40 V |
|  | 4822 122 33002 | 68 pF |  |
|  | 4822 122 32976 | 470 pF |  |
|  | 4822 122 31759 | 22 nF |  |
|  | 4822 122 32976 | 470 pF |  |
|  | 4822 122 31759 | 22 nF |  |
|  | 4822 122 32442 | 10 nF |  |
|  | 4822 121 42915 | 330 pF |  |
|  | 4822 122 31759 | 22 nF |  |
|  | 4822 122 31974 | 820 pF |  |
|  | 4822 122 31644 | 2.2 nF |  |
|  | 4822 122 31974 | 820 pF |  |
|  | 4822 121 41608 | 100 nF | 100 V |
|  | 4822 122 33002 | 68 pF |  |
|  | 4822 122 31759 | 22 nF |  |
|  | 4822 121 50632 | 1.5 nF | 250 V |
|  | 4822 122 31759 | 22 nF |  |
|  | 4822 122 31768 | 160 pF |  |
|  | 5322 124 21643 | 22 μF | 40 V |
|  | 4822 122 32442 | 10 nF |  |
|  | 5322 124 21643 | 22 μF | 40 V |
|  | 5322 124 21643 | 22 μF | 40 V |
|  | 4822 122 32482 | 22 pF |  |
|  | 5322 124 21643 | 22 μF | 40 V |
|  | 5322 124 21643 | 22 μF | 40 V |
|  | 4822 121 41608 | 100 nF | 100 V |
|  | 4822 122 31974 | 820 pF |  |
|  | 5322 124 21643 | 22 μF | 40 V |
|  | 5322 124 21643 | 22 μF | 40 V |
|  | 4822 121 41608 | 100 nF | 100 V |
|  | 5322 124 21643 | 22 μF | 40 V |

## Modification levels

The manual has no modification-level sheet for this module.

## Related

- [Module circuit descriptions](../../circuit-description/modules.md)
- [Modification levels per module](../../service-information/modification-levels.md)
- [Module and connector lay-out](../../system/module-layout.md)
