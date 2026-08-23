---
title: Module T - Supply
description: >-
  Switched-mode power supply.
---

<!-- drafted by tools/import_modules.py - hand-edited afterwards -->

# Module T - Supply

Switched-mode power supply.

## Overview

| | |
| --- | --- |
| Designation | **T** |
| Modification levels | 1 |
| Data sheet | `CS 7 853`, pages 071, 072 |
| Circuit diagram | `CS 6 885`, page 073 |

## The board

<figure class="sheet sheet--photo" markdown>
[![Module T, component side of the board](assets/web/t-supply-top-preview.webp)](assets/web/t-supply-top-zoom.webp)
<figcaption>
  Module T, component side.
</figcaption>
</figure>

## Where it sits in the player

See the [module and connector lay-out](../../system/module-layout.md).

## Circuit description

[Chapter 7, module T](../../circuit-description/modules.md#module-t).

## Adjustments

Required

Test disc

Voltmeter

Adjustment conditions

Rotating disc

# Adjustments

1) R503 (DC Voltage)

-Measure the DC voltage on 3T2 (+5)

-Adjust R503 for 5.2V (±0.1V)

## Circuit diagram

<figure class="sheet sheet--fold" markdown>
[![Supply module T - circuit diagram (switched mode power supply)](assets/web/cs-6-885-circuit-p073-preview.webp)](assets/web/cs-6-885-circuit-p073-zoom.webp)
<figcaption>
  Supply module T - circuit diagram (switched mode power supply).
  <span class="cs">CS 6 885</span>
  <span class="src">service manual page 073</span>
</figcaption>
</figure>

## PCB lay-out

<figure class="sheet sheet--fold" markdown>
[![Supply module T (mod level 1) - adjustments / PCB / parts](assets/web/cs-7-853-module-sheet-p071-072-preview.webp)](assets/web/cs-7-853-module-sheet-p071-072-zoom.webp)
<figcaption>
  Supply module T (mod level 1) - adjustments / PCB / parts.
  <span class="cs">CS 7 853</span>
  <span class="src">service manual pages 071, 072</span>
</figcaption>
</figure>

## List of electrical parts

**Fuses**

| Item | Service code number | Value | Rating |
| --- | --- | --- | --- |
| F911 | 4822 253 30024 | 1.6 A |  |
| F912 | 4822 253 30024 | 1.6 A |  |
| F913 | 4822 253 10048 | 3.15 A |  |

**Circuits**

| Item | Service code number | Value | Rating |
| --- | --- | --- | --- |
| D501 | 5322 209 82349 | Hybride circuit SMPS |  |

**Other**

| Item | Service code number | Value | Rating |
| --- | --- | --- | --- |
| T101 | 5322 146 40322 | aux trafo |  |
| T201 | 5322 142 60363 | impuls trafo |  |
| T401 | 4822 142 70056 | current trafo |  |
| T901 | 5322 146 30531 | power trafo |  |
| V001 | 4822 130 50438 | Rectifier KBU8-K |  |

**Coils**

| Item | Service code number | Value | Rating |
| --- | --- | --- | --- |
| L001 | 4822 157 52981 | 350 μH |  |
| L002 | 4822 158 30208 | Mains choke |  |
| L701 | 4822 157 52979 | Triple choke |  |

**Potentiometers**

| Item | Service code number | Value | Rating |
| --- | --- | --- | --- |
| R402 | 4822 101 10793 | 5 kΩ |  |
| R503 | 4822 101 10792 | 1 kΩ |  |

**NTC Resistors**

| Item | Service code number | Value | Rating |
| --- | --- | --- | --- |
| R001 | 5322 116 40077 | 7 Ω |  |

**PTC Resistors**

| Item | Service code number | Value | Rating |
| --- | --- | --- | --- |
| R801 | 4822 116 40032 | 2.3 Ω - 5 Ω |  |

**Wire wound Resistors**

| Item | Service code number | Value | Rating |
| --- | --- | --- | --- |
| R201 | 4822 112 41107 | 1 kΩ |  |

**NFR25 Resistors**

| Item | Service code number | Value | Rating |
| --- | --- | --- | --- |
| R101 | 4822 111 30544 | 220 Ω |  |
| R202 | 4822 111 30526 | 47 Ω |  |
| R301 | 4822 111 30499 | 4.7 Ω |  |
| R701 | 4822 111 30526 | 47 Ω |  |
| R702 | 4822 111 30526 | 47 Ω |  |
| R706 | 4822 111 30526 | 47 Ω |  |

**VR25 Resistors**

| Item | Service code number | Value | Rating |
| --- | --- | --- | --- |
| R901 | 5322 116 64132 | 1 MΩ |  |

**PR37 Resistors**

| Item | Service code number | Value | Rating |
| --- | --- | --- | --- |
| R703 | 5322 116 55063 | 39 Ω |  |
| R704 | 5322 116 54909 | 1 kΩ |  |
| R707 | 5322 116 54909 | 1 kΩ |  |

**PR52 Resistors**

| Item | Service code number | Value | Rating |
| --- | --- | --- | --- |
| R203 | 5322 116 51093 | 15 Ω |  |

**VR68 Resistors**

| Item | Service code number | Value | Rating |
| --- | --- | --- | --- |
| R103 | 5322 116 53075 | 220 kΩ |  |

**Capacitors**

| Item | Service code number | Value | Rating |
| --- | --- | --- | --- |
| C001 | 4822 122 33042 | 3.3 nF |  |
| C002 | 4822 122 33042 | 3.3 nF |  |
| C004 | 5322 121 41721 | 470 nF | 10% 275 V |
| C006 | 5322 124 21798 | 220 μF | 10% 200 V |
| C007 | 5322 124 21798 | 220 μF | 10% 200 V |
| C101 | 4822 124 10367 | 4.7 μF | 25 V |
| C102 | 4822 121 40483 | 10 nF | 10% 400 V |
| C103 | 4822 122 31125 | 4.7 nF | 100 V |
| C104 | 4822 124 40744 | 68 μF | 40 V |
| C201 | 5322 121 44286 | 1 nF | 10% 630 V |
| C202 | 5322 121 44286 | 1 nF | 10% 630 V |
| C301 | 4822 121 40516 | 22 nF | 10% 250 V |
| C501 | 5322 121 40308 | 22 nF | 10% 400 V |
| C502 | 4822 121 40232 | 220 nF | 10% 100 V |
| C503 | 4822 121 40232 | 220 nF | 10% 100 V |
| C504 | 4822 122 30103 | 22 nF | 63 V |
| C506 | 4822 124 21314 | 10 μF | 16 V |
| C701 | 4822 121 40337 | 4.7 nF | 10% 630 V |
| C702 | 4822 121 40338 | 2.2 nF | 10% 630 V |
| C703 | 4822 124 40723 | 2.2 mF | 16 V |
| C704 | 4822 124 40723 | 2.2 mF | 16 V |
| C706 | 4822 121 40338 | 2.2 nF | 10% 630 V |
| C707 | 4822 124 40723 | 2.2 mF | 16 V |
| C801 | 5322 124 14081 | 6.8 μF | 25 V |
| C802 | 5322 124 14081 | 6.8 μF | 25 V |

## Modification levels

[Chapter 8, module T](../../service-information/modification-levels.md#mod-t).

## Related

- [Module circuit descriptions](../../circuit-description/modules.md)
- [Remarks](../../general-service/remarks.md)
- [Warnings](../../general-service/warnings.md)
- [Fault-finding charts](../../repair/fault-finding.md)
- [Fault symptoms](../../service-information/fault-symptoms.md)
- [Modification levels per module](../../service-information/modification-levels.md)
- [Module and connector lay-out](../../system/module-layout.md)
