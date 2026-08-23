---
title: Module W - CPU + data grabber
description: >-
  CPU and data grabber, with the SCSI interface to the host.
---

<!-- drafted by tools/import_modules.py - hand-edited afterwards -->

# Module W - CPU + data grabber

CPU and data grabber, with the SCSI interface to the host.

## Overview

| | |
| --- | --- |
| Designation | **W** |
| Modification levels | 2 → 3 |
| Parts list | `CS 7 857`, page 083 |
| PCB lay-out | `—`, page 084 |
| Circuit diagram | `CS 6 889`, pages 085, 086 |
| Circuit diagram | `CS 6 890`, pages 087, 088 |
| PCB lay-out | `CS 8 122`, page 089 |
| PCB lay-out | `CS 7 858`, page 090 |

## The board

<div class="sheet-pair" markdown>
<figure class="sheet sheet--photo" markdown>
[![Module W, component side of the board](assets/web/w-cpu-data-grabber-top-preview.webp)](assets/web/w-cpu-data-grabber-top-zoom.webp)
<figcaption>
  Module W, component side.
</figcaption>
</figure>
<figure class="sheet sheet--photo" markdown>
[![Module W, solder side of the board](assets/web/w-cpu-data-grabber-bottom-preview.webp)](assets/web/w-cpu-data-grabber-bottom-zoom.webp)
<figcaption>
  Module W, solder side.
</figcaption>
</figure>
</div>

## Where it sits in the player

See the [module and connector lay-out](../../system/module-layout.md).

## Circuit description

[Chapter 7, module W](../../circuit-description/modules.md#module-w).

## Adjustments

None.

## Circuit diagram

<figure class="sheet sheet--fold" markdown>
[![CPU + data grabber module W - circuit diagram](assets/web/cs-6-889-circuit-p085-086-preview.webp)](assets/web/cs-6-889-circuit-p085-086-zoom.webp)
<figcaption>
  CPU + data grabber module W - circuit diagram.
  <span class="cs">CS 6 889</span>
  <span class="src">service manual pages 085, 086</span>
</figcaption>
</figure>

<figure class="sheet sheet--fold" markdown>
[![CPU + data grabber module W - circuit diagram (EPROM section)](assets/web/cs-6-890-circuit-p087-088-preview.webp)](assets/web/cs-6-890-circuit-p087-088-zoom.webp)
<figcaption>
  CPU + data grabber module W - circuit diagram (EPROM section).
  <span class="cs">CS 6 890</span>
  <span class="src">service manual pages 087, 088</span>
</figcaption>
</figure>

## PCB lay-out

<figure class="sheet" markdown>
[![List of electrical parts module W (EPROMs)](assets/web/cs-7-857-parts-p083-preview.webp)](assets/web/cs-7-857-parts-p083-zoom.webp)
<figcaption>
  List of electrical parts module W (EPROMs).
  <span class="cs">CS 7 857</span>
  <span class="src">service manual page 083</span>
</figcaption>
</figure>

<figure class="sheet sheet--fold" markdown>
[![CPU + data grabber module W (mod level 2) - PCB / parts](assets/web/pcb-layout-p084-preview.webp)](assets/web/pcb-layout-p084-zoom.webp)
<figcaption>
  CPU + data grabber module W (mod level 2) - PCB / parts.
  <span class="src">service manual page 084</span>
</figcaption>
</figure>

<figure class="sheet sheet--fold" markdown>
[![CPU + data grabber module W - PCB lay-out (later revision)](assets/web/cs-8-122-pcb-layout-p089-preview.webp)](assets/web/cs-8-122-pcb-layout-p089-zoom.webp)
<figcaption>
  CPU + data grabber module W - PCB lay-out (later revision).
  <span class="cs">CS 8 122</span>
  <span class="src">service manual page 089</span>
</figcaption>
</figure>

<figure class="sheet sheet--fold" markdown>
[![CPU + data grabber module W - PCB lay-out](assets/web/cs-7-858-pcb-layout-p090-preview.webp)](assets/web/cs-7-858-pcb-layout-p090-zoom.webp)
<figcaption>
  CPU + data grabber module W - PCB lay-out.
  <span class="cs">CS 7 858</span>
  <span class="src">service manual page 090</span>
</figcaption>
</figure>

## List of electrical parts

**Eproms (programmed)**

| Item | Service code number | Value | Rating |
| --- | --- | --- | --- |
| 7201 IC1 | 4822 209 51258 | TMS 27128 sync |  |
| 7224 IC24 | 4822 209 51259 | TMS 27128 descrambler |  |
| 7247 IC47 | 4822 209 51261 | TMS 27128 LV DOS 1 |  |
| 7248 IC48 | 4822 209 51262 | TMS 27128 LV DOS 2 |  |

**Crystals**

| Item | Service code number | Value | Rating |
| --- | --- | --- | --- |
| 5001 X1 | 4822 242 71628 | 8MHz |  |

**Resistor networks**

| Item | Service code number | Value | Rating |
| --- | --- | --- | --- |
| 3003 R3 | 4822 116 90247 | 9x 220 Ω |  |
| 3004 R4 | 4822 116 90248 | 9x 330 Ω |  |
| 3005 R5 | 4822 116 90247 | 9x 220 Ω |  |
| 3006 R6 | 4822 116 90248 | 9x 330 Ω |  |
| 3007 R7 | 4822 116 90251 | 9x 3.3kΩ |  |

**Capacitors**

| Item | Service code number | Value | Rating |
| --- | --- | --- | --- |
| 2001 |  |  |  |
| 2002 |  |  |  |
| 2003 |  |  |  |
| 2004 |  |  |  |
| 2005 |  |  |  |
| 2006 |  |  |  |
| 2007 |  |  |  |
| 2102 |  |  |  |
| 2177 |  |  |  |

**Other**

| Item | Service code number | Value | Rating |
| --- | --- | --- | --- |
| c1 | 4822 122 31413 | 150 pF |  |
| c2 | 5322 122 32072 | 33 pF |  |
| c3 | 5322 124 21749 | 10 μF | 63 V |
| c39.. | 4822 122 30103 | 22 nF | 63 V |
| c4 | 4822 124 22027 | 47 μF | 25 V |
| c5 | 5322 122 32072 | 33 pF |  |
| c6 | 4822 122 30103 | 22 nF | 63 V |
| c7 | 4822 124 22027 | 47 μF | 25 V |

## Modification levels

The manual has no modification-level sheet for this module.

## Related

- [Module circuit descriptions](../../circuit-description/modules.md)
- [VP400 series architecture](../../circuit-description/vp400-series.md)
- [Modification levels](../../general-service/modification-levels.md)
- [Connector pinning](../../overview/connector-pinning.md)
- [Modification levels per module](../../service-information/modification-levels.md)
- [Software releases](../../service-information/software-releases.md)
- [Module and connector lay-out](../../system/module-layout.md)
