---
title: Module I - ETBC-C
description: >-
  ETBC-C, the second half of the electronic timebase corrector.
---

<!-- drafted by tools/import_modules.py - hand-edited afterwards -->

# Module I - ETBC-C

ETBC-C, the second half of the electronic timebase corrector.

## Overview

| | |
| --- | --- |
| Designation | **I** |
| Modification levels | 6 → 7 |
| Data sheet | `CS 7 845`, page 050 |
| Circuit diagram | `CS 6 875`, page 051 |

## The board

<div class="sheet-pair" markdown>
<figure class="sheet sheet--photo" markdown>
[![Module I, component side of the board](assets/web/i-etbc-c-top-preview.webp)](assets/web/i-etbc-c-top-zoom.webp)
<figcaption>
  Module I, component side.
</figcaption>
</figure>
<figure class="sheet sheet--photo" markdown>
[![Module I, solder side of the board](assets/web/i-etbc-c-bottom-preview.webp)](assets/web/i-etbc-c-bottom-zoom.webp)
<figcaption>
  Module I, solder side.
</figcaption>
</figure>
</div>

## Where it sits in the player

See the [module and connector lay-out](../../system/module-layout.md).

## Circuit description

[Chapter 7, module I](../../circuit-description/modules.md#module-i).

## Adjustments

Required

Test disc

Scope

Adjustment conditions

Load test disc.

Still picture, colour bar (picture no. 6200).

# Adjustment

1) L5001 (Special burst separator)

- Measure the signal on B-TS7029 with the scope (line- frequent).
- Adjust L5001 for maximum amplitude of the special burst signal.

## Circuit diagram

<figure class="sheet sheet--fold" markdown>
[![ETBC-C module I - circuit diagram](assets/web/cs-6-875-circuit-p051-preview.webp)](assets/web/cs-6-875-circuit-p051-zoom.webp)
<figcaption>
  ETBC-C module I - circuit diagram.
  <span class="cs">CS 6 875</span>
  <span class="src">service manual page 051</span>
</figcaption>
</figure>

## PCB lay-out

<figure class="sheet sheet--fold" markdown>
[![ETBC-C module I (mod level 6) - adjustments / PCB / parts](assets/web/cs-7-845-module-sheet-p050-preview.webp)](assets/web/cs-7-845-module-sheet-p050-zoom.webp)
<figcaption>
  ETBC-C module I (mod level 6) - adjustments / PCB / parts.
  <span class="cs">CS 7 845</span>
  <span class="src">service manual page 050</span>
</figcaption>
</figure>

## List of electrical parts

**Coils**

| Item | Service code number | Value | Rating |
| --- | --- | --- | --- |
| 5001 | 4822 156 11003 | 12 μH |  |

**NFR25 Resistors**

| Item | Service code number | Value | Rating |
| --- | --- | --- | --- |
| 3129 | 4822 111 30513 | 15 Ω |  |
| 3130 | 4822 111 30513 | 15 Ω |  |

**Other**

| Item | Service code number | Value | Rating |
| --- | --- | --- | --- |
|  | 5322 124 21643 | 22 μF | 40 V |
|  | 4822 122 31759 | 22 nF |  |
|  | 4822 122 32974 | 100 pF |  |
|  | 4822 122 31783 | 2.7 nF |  |
|  | 4822 122 31767 | 150 pF |  |
|  | 5322 124 21643 | 22 μF | 40 V |
|  | 4822 122 31759 | 22 nF |  |
|  | 4822 122 31759 | 22 nF |  |
|  | 4822 122 31969 | 3.3 nF |  |
|  | 4822 122 31969 | 3.3 nF |  |
|  | 4822 122 31759 | 22 nF |  |
|  | 4822 122 31781 | 1.5 nF |  |
|  | 4822 122 31781 | 1.5 nF |  |
|  | 4822 124 22027 | 47 μF | 25 V |
|  | 4822 121 41608 | 100 nF | 100 V |
|  | 4822 122 31783 | 2.7 nF |  |
|  | 4822 122 32976 | 470 pF |  |
|  | 4822 122 32974 | 100 pF |  |
|  | 4822 121 41545 | 33 nF | 250 V |
|  | 4822 121 41874 | 270 nF | 63 V |
|  | 4822 122 31774 | 56 pF |  |
|  | 5322 124 21643 | 22 μF | 40 V |

**Capacitors**

| Item | Service code number | Value | Rating |
| --- | --- | --- | --- |
| 2027 | 4822 122 32504 | 15 pF |  |
| 2028 | 4822 122 31774 | 56 pF |  |
| 2029 | 4822 122 31784 | 4.7 nF |  |
| 2034 | 4822 122 31759 | 22 nF |  |
| 2037 | 5322 122 31647 | 1 nF |  |
| 2041 | 4822 122 31759 | 22 nF |  |
| 2042 | 4822 122 31775 | 680 pF |  |
| 2043 | 4822 122 32482 | 22 pF |  |
| 2044 | 4822 122 31772 | 47 pF |  |
| 2045 | 4822 122 32542 | 47 nF |  |
| 2046 | 4822 122 31774 | 56 pF |  |
| 2048 | 4822 122 32142 | 270 pF |  |
| 2049 | 5322 122 31647 | 1 nF |  |
| 2050 | 4822 124 22031 | 4.7 μF |  |
| 2051 | 4822 122 31759 | 22 nF |  |
| 2052 | 4822 121 51051 | 4.7 nF |  |
| 2053 | 4822 122 32891 | 68 nF |  |
| 2054 | 4822 124 22031 | 4.7 μF |  |
| 2057 | 4822 124 22031 | 4.7 μF |  |
| 2058 | 4822 121 41757 | 470 nF10% |  |
| 2059 | 4822 121 42915 | 330 pF |  |
| 2060 | 5322 124 21643 | 22 μF |  |
| 2061 | 4822 122 32153 | 1.8 nF |  |
| 2063 | 5322 124 21711 | 100 μF |  |
| 2064 | 5322 124 21711 | 100 μF |  |

## Modification levels

[Chapter 8, module I](../../service-information/modification-levels.md#mod-i).

## Related

- [The LaserVision system](../../circuit-description/laservision-system.md)
- [Module circuit descriptions](../../circuit-description/modules.md)
- [VP400 series architecture](../../circuit-description/vp400-series.md)
- [Modification levels per module](../../service-information/modification-levels.md)
- [Module and connector lay-out](../../system/module-layout.md)
