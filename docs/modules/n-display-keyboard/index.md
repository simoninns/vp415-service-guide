---
title: Module N - Display + keyboard
description: >-
  Front-panel display and keyboard.
---

<!-- drafted by tools/import_modules.py - hand-edited afterwards -->

# Module N - Display + keyboard

Front-panel display and keyboard.

## Overview

| | |
| --- | --- |
| Designation | **N** |
| Modification levels | 1 |
| Circuit diagram | `CS 6 880`, page 060 |
| Data sheet | `CS 7 850`, pages 061, 062, panels 1+2 |

## Where it sits in the player

See the [module and connector lay-out](../../system/module-layout.md).

## Circuit description

[Chapter 7, module N](../../circuit-description/modules.md#module-n).

## Adjustments

None.

## Circuit diagram

<figure class="sheet" markdown>
[![Display + keyboard module N - circuit diagram](assets/web/cs-6-880-circuit-p060-preview.webp)](assets/web/cs-6-880-circuit-p060-zoom.webp)
<figcaption>
  Display + keyboard module N - circuit diagram.
  <span class="cs">CS 6 880</span>
  <span class="src">service manual page 060</span>
</figcaption>
</figure>

## PCB lay-out

<figure class="sheet sheet--fold" markdown>
[![Display + keyboard module N (mod level 1) - PCB / parts](assets/web/cs-7-850-module-sheet-p061-062-preview.webp)](assets/web/cs-7-850-module-sheet-p061-062-zoom.webp)
<figcaption>
  Display + keyboard module N (mod level 1) - PCB / parts.
  <span class="cs">CS 7 850</span>
  <span class="src">service manual pages 061, 062</span>
</figcaption>
</figure>

## List of electrical parts

**Capacitors**

| Item | Service code number | Value | Rating |
| --- | --- | --- | --- |
| 2001 | 4822 121 41608 | 100 nF | 100 V |
| 2002 | 4822 124 22027 | 47 μF | 25 V |
| 2101 | 4822 122 30103 | 22 nF | 63 V |
| 2102 | 4822 122 30103 | 22 nF | 63 V |

**Buzzer**

| Item | Service code number | Value | Rating |
| --- | --- | --- | --- |
| 1005 | 4822 280 10151 | Buzzer SD120901 |  |
| 2102 | 4822 122 30103 | 22 nF | 63 V |

**LEDs**

| Item | Service code number | Value | Rating |
| --- | --- | --- | --- |
| 6001 | 4822 130 80111 | TLSR5101 |  |

**Resistor networks**

| Item | Service code number | Value | Rating |
| --- | --- | --- | --- |
| 3002 | 4822 116 90249 | 9x 270 Ω |  |

## Modification levels

The manual has no modification-level sheet for this module.

## Related

- [Module circuit descriptions](../../circuit-description/modules.md)
- [VP400 series architecture](../../circuit-description/vp400-series.md)
- [Fault-finding charts](../../repair/fault-finding.md)
- [Modification levels per module](../../service-information/modification-levels.md)
- [Module and connector lay-out](../../system/module-layout.md)
