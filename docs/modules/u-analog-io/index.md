---
title: Module U - Analog I/O
description: >-
  Analog I/O in three parts - Ua audio/CVBS, Ub video, Uc teletext.
---

<!-- drafted by tools/import_modules.py - hand-edited afterwards -->

# Module U - Analog I/O

Analog I/O in three parts - Ua audio/CVBS, Ub video, Uc teletext.

## Overview

| | |
| --- | --- |
| Designation | **U** |
| Modification levels | 3 → 4 |
| Circuit diagram | `CS 6 886`, page 074 |
| Data sheet | `CS 7 854`, pages 075, 076 |
| Data sheet | `CS 7 854`, pages 077, 078 |
| Circuit diagram | `CS 6 887`, page 079 |
| Circuit diagram | `CS 6 888`, page 080 |
| Adjustments | `—`, page 081 |
| Adjustments | `CS 7 856`, page 082 |

## The board

<div class="sheet-pair" markdown>
<figure class="sheet sheet--photo" markdown>
[![Module U, component side of the board](assets/web/u-analog-io-top-preview.webp)](assets/web/u-analog-io-top-zoom.webp)
<figcaption>
  Module U, component side.
</figcaption>
</figure>
<figure class="sheet sheet--photo" markdown>
[![Module U, solder side of the board](assets/web/u-analog-io-bottom-preview.webp)](assets/web/u-analog-io-bottom-zoom.webp)
<figcaption>
  Module U, solder side.
</figcaption>
</figure>
</div>

## Where it sits in the player

See the [module and connector lay-out](../../system/module-layout.md).

## Circuit description

[Chapter 7, module U](../../circuit-description/modules.md#module-ua).

## Adjustments

# Required

Test disc

Scope

# Adjustment conditions

Load test disc.

Still picture, picture no. 6200 (colour bar EBU test signal).

Disc drive may not be locked to an external video source.

# Adjustments

1) R3263, R3207, R3240, R3315, R3305 (CVBS amplitudes)

- Measure the CVBS OUT signal (ENCODED) on BNC3 (linefrequent) with the scope (see fig. U1). Terminate the signal with 75 Ω.

Fig. U1

- Adjust R3263 for a sync-amplitude of 300mV relative to black level.
- Adjust R3207 for a white amplitude of 700mV relative to black level.
- Adjust R3315 until the upper side of the chroma signal during the yellow bar lies at the same level as the white signal (700 mV).
- Adjust R3305 until the upper side of the chroma signal during the cyan bar lies at the same level as the white signal.
- Search for picture number 8200 (black) and switch off the index.
- Measure the CVBS OUT signal, frame frequent and display the lines 16-20 of the video signal. The VITS- and 24 bit code are displayed as TXT info (see Fig. U2).
- Adjust R3240 for an amplitude of 460mV (± 20mV) of the signal in lines 16-20.

TXT AMPLITUDE

Fig. U2

MDA.00590

2) C2315 (chroma subcarrier)

- Measure with the scope (channel A) the CVBS OUT-signal on BNC3 (ENCODED).
- Measure with the scope (channel B) the CVBS signal on E-TS7105 (NOT ENCODED).
- Switch the scope to A+B, adding the 2 signals.
- Adjust C2315 for minimum amplitude variations in the chroma signal.

3) L5202 (chroma notch)

- Measure the CVBS OUT signal (ENCODED) on BNC3 with the scope (line-frequent). Terminate the signal with 75Ω
- Adjust L5202 for maximum amplitude of the chroma signal.

4) R3309, R3319 (burst amplitude)

- Switch the drive into the STAND BY position.
- Measure the CVBS OUT signal (ENCODED) on BNC3 with the scope (line frequent).Terminate the signal with 75Ω
- Short circuit pins 10 and 12 of IC7351.
- Adjust R3309 for a burst amplitude of 210mV (± 10mV)
- Remove short circuiting of pins 10 and 12.
- Short circuit pins 5 and 12 of IC7351.
- Adjust R3319 for a burst amplitude of 210mV (± 10mV)
- Remove short circuit of pins 5 and 12. (The burst amplitude will increase to approx 300 mV).

## Circuit diagram

<figure class="sheet sheet--fold" markdown>
[![Analog I/O module Ua (CVBS + audio part) - circuit diagram](assets/web/cs-6-886-circuit-p074-preview.webp)](assets/web/cs-6-886-circuit-p074-zoom.webp)
<figcaption>
  Analog I/O module Ua (CVBS + audio part) - circuit diagram.
  <span class="cs">CS 6 886</span>
  <span class="src">service manual page 074</span>
</figcaption>
</figure>

<figure class="sheet sheet--fold" markdown>
[![Analog I/O module Ub (video part) - circuit diagram](assets/web/cs-6-887-circuit-p079-preview.webp)](assets/web/cs-6-887-circuit-p079-zoom.webp)
<figcaption>
  Analog I/O module Ub (video part) - circuit diagram.
  <span class="cs">CS 6 887</span>
  <span class="src">service manual page 079</span>
</figcaption>
</figure>

<figure class="sheet sheet--fold" markdown>
[![Analog I/O module Uc (TXT part) - circuit diagram](assets/web/cs-6-888-circuit-p080-preview.webp)](assets/web/cs-6-888-circuit-p080-zoom.webp)
<figcaption>
  Analog I/O module Uc (TXT part) - circuit diagram.
  <span class="cs">CS 6 888</span>
  <span class="src">service manual page 080</span>
</figcaption>
</figure>

## PCB lay-out

<figure class="sheet sheet--fold" markdown>
[![Analog I/O module U (mod level 3) - parts](assets/web/cs-7-854-module-sheet-p075-076-preview.webp)](assets/web/cs-7-854-module-sheet-p075-076-zoom.webp)
<figcaption>
  Analog I/O module U (mod level 3) - parts.
  <span class="cs">CS 7 854</span>
  <span class="src">service manual pages 075, 076</span>
</figcaption>
</figure>

<figure class="sheet sheet--fold" markdown>
[![Analog I/O module U - parts (continued)](assets/web/cs-7-854-module-sheet-p077-078-preview.webp)](assets/web/cs-7-854-module-sheet-p077-078-zoom.webp)
<figcaption>
  Analog I/O module U - parts (continued).
  <span class="cs">CS 7 854</span>
  <span class="src">service manual pages 077, 078</span>
</figcaption>
</figure>

<figure class="sheet" markdown>
[![Analog I/O module U - adjustments](assets/web/adjustments-p081-preview.webp)](assets/web/adjustments-p081-zoom.webp)
<figcaption>
  Analog I/O module U - adjustments.
  <span class="src">service manual page 081</span>
</figcaption>
</figure>

<figure class="sheet sheet--fold" markdown>
[![Analog I/O module U - adjustments (continued) / connector detail](assets/web/cs-7-856-adjustments-p082-preview.webp)](assets/web/cs-7-856-adjustments-p082-zoom.webp)
<figcaption>
  Analog I/O module U - adjustments (continued) / connector detail.
  <span class="cs">CS 7 856</span>
  <span class="src">service manual page 082</span>
</figcaption>
</figure>

## List of electrical parts

**Crystals**

| Item | Service code number | Value | Rating |
| --- | --- | --- | --- |
| 5302 | 4822 242 70323 | 4.433619 MHz |  |
| 5602 | 4822 242 71417 | 13.875 MHz |  |

**Coils**

| Item | Service code number | Value | Rating |
| --- | --- | --- | --- |
| 5201 | 4822 156 21324 | 100 μH |  |
| 5202 | 4822 156 10996 | 15 μH |  |
| 5301 | 4822 156 10996 | 15 μH |  |
| 5601 | 4822 156 10996 | 15 μH |  |

**Potentiometers**

| Item | Service code number | Value | Rating |
| --- | --- | --- | --- |
| 3149 | 4822 101 90063 | 10 kΩ |  |
| 3207 | 4822 100 20151 | 1 kΩ |  |
| 3240 | 5322 101 10691 | 4.7 kΩ |  |
| 3263 | 5322 101 10691 | 4.7 kΩ |  |
| 3305 | 4822 100 20151 | 1 kΩ |  |
| 3309 | 5322 101 10691 | 4.7 kΩ |  |
| 3315 | 4822 100 20151 | 1 kΩ |  |
| 3319 | 5322 101 10691 | 4.7 kΩ |  |
| 3530 | 5322 101 10627 | 10 kΩ |  |

**Fuse Resistors**

| Item | Service code number | Value | Rating |
| --- | --- | --- | --- |
| 3533 | 4822 111 30831 | 47 Ω |  |

**NFR25 Resistors**

| Item | Service code number | Value | Rating |
| --- | --- | --- | --- |
| 3001 | 4822 111 30508 | 10 Ω |  |
| 3002 | 4822 111 30515 | 18 Ω |  |
| 3003 | 4822 111 30511 | 12 Ω |  |
| 3004 | 4822 111 30511 | 12 Ω |  |
| 3010 | 4822 111 30483 | 1 Ω |  |
| 3011 | 4822 111 30483 | 1 Ω |  |
| 3012 | 4822 111 30483 | 1 Ω |  |
| 3013 | 4822 111 30483 | 1 Ω |  |

**Trim Capacitors**

| Item | Service code number | Value | Rating |
| --- | --- | --- | --- |
| 2315 | 4822 125 50062 | 10 pF |  |

## Modification levels

[Chapter 8, module U](../../service-information/modification-levels.md#mod-u).

## Related

- [Module circuit descriptions](../../circuit-description/modules.md)
- [VP400 series architecture](../../circuit-description/vp400-series.md)
- [Adjustments](../../general-service/adjustments.md)
- [Remarks](../../general-service/remarks.md)
- [Fault-finding charts](../../repair/fault-finding.md)
- [Modification levels per module](../../service-information/modification-levels.md)
- [Module and connector lay-out](../../system/module-layout.md)
