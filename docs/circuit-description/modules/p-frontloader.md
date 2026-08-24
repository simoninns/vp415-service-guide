---
title: Module P - Frontloader
description: >-
  The front loader mechanism, its motor drive and its sensors.
---

# Module P — Frontloader

*See also the [module P page](../../modules/p-frontloader/index.md).*

The purpose of this module is to provide the required drive current to the motor of the front loading mechanism, which takes care, that the disc is positioned at the correct place in the player. Control signals are fed in from the drive processor module R and status signals are fed back to the drive processor. See Fig.P1.

## Circuit description

The front loader motor is a d.c. motor, which can be driven in two ways, for loading and unloading respectively. Therefore the motor is connected to a bridge circuit. See Fig. P2.

Loading: When the tray is partly pushed in, the start stop switch is connected to ground and ST-ST signal "L" is fed to drive processor R. At this moment the LMOT-L signal from drive processor R becomes "H" and transistors 7001, 7006 and 7004 will conduct. This causes current I1 to drive the motor and the tray will move further inside. When the tray is fully inside, the "tray inside" switch is closed and "I" becomes "L". LMOT-L becomes "L" again and all transistors are cut off. The motor will stop.

Unloading: When "EJECT" is pressed, the drive processor delivers an LMOT-R signal "H". Now transistors 7003, 7005 and 7007 will conduct and the motor is driven by current I2. As I2 is in direction opposite to I1, the tray will now move outwards. This continues until the ST-ST switch is open again and ST-ST signal "H" is fed to the drive processor. LMOT-R becomes low and all transistors are blocked again.

Protection device: When the tray is blocked during loading as well as during unloading, the LMOT-L and LMOT-R signals become "L" and the motor is not energized anymore.

*Fig.P1 FRONT LOADER CIRCUIT — see the sheet below.*

## The manual sheet

<figure class="sheet sheet--fold" markdown>
[![Module P - frontloader / Module R - drive processor](../assets/web/cs-7-897-text-p151-preview.webp)](../assets/web/cs-7-897-text-p151-zoom.webp)
<figcaption>
  Module P - frontloader / Module R - drive processor.
  <span class="cs">CS 7 897</span>
  <span class="src">service manual page 151</span>
</figcaption>
</figure>
