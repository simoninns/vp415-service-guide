---
title: Module P - Frontloader
description: >-
  Front-loader tray mechanics and its sensors.
---

# Module P - Frontloader

Front-loader tray mechanics and its sensors.

## Overview

The frontloader module drives the motor of the front-loading mechanism, which
puts the disc in the right place in the player. It takes control signals from
[drive processor module R](../r-drive-processor/index.md) and hands status
signals back to it.

| | |
| --- | --- |
| Designation | **P** — frontloader |
| Modification levels | 4 (unchanged through production) |
| Data sheet | `CS 7 850`, pages 061–062, **panel 3** |
| Circuit diagram | on the same panel — the module has no separate diagram sheet |
| Connectors | `P1`, `P2` |
| In | `LMOT-L` load, `LMOT-R` unload, from module R |
| Out | `ST-ST` start/stop switch, `TI` tray inside, `0-RPM` — back to module R |

!!! note "This module's sheet is filed under module N"

    `CS 7 850` is a trifold covering two modules: panels 1 and 2 are
    [display + keyboard module N](../n-display-keyboard/index.md), and panel 3
    is module P. The scan below is the whole sheet; module P is its right-hand
    panel.

## The board

<div class="sheet-pair" markdown>
<figure class="sheet sheet--photo" markdown>
[![Module P, component side of the board](assets/web/p-frontloader-top-preview.webp)](assets/web/p-frontloader-top-zoom.webp)
<figcaption>
  Module P, component side.
</figcaption>
</figure>
<figure class="sheet sheet--photo" markdown>
[![Module P, solder side of the board](assets/web/p-frontloader-bottom-preview.webp)](assets/web/p-frontloader-bottom-zoom.webp)
<figcaption>
  Module P, solder side.
</figcaption>
</figure>
</div>

## Where it sits in the player

In the front-loader assembly itself, not on the module carrier — so it does
not appear in the overhead photograph on the
[module and connector lay-out](../../system/module-layout.md) page. Getting to
it means taking the loader off; see
[demounting](../../general-service/demounting.md).

## Circuit description

The front-loader motor is a DC motor in a **bridge circuit**, so it can be
driven either way.

**Loading.** When the tray is pushed partly in, the start/stop switch grounds
and `ST-ST` goes low to module R. Module R takes `LMOT-L` high; transistors
7001, 7006 and 7004 conduct and current *I1* drives the tray inwards. When the
tray is fully in, the "tray inside" switch closes, `TI` goes low, `LMOT-L`
goes low again, all four transistors cut off and the motor stops.

**Unloading.** Pressing EJECT makes module R raise `LMOT-R`: transistors 7003,
7005 and 7007 conduct and current *I2* — opposite in direction to *I1* — drives
the tray outwards, until the start/stop switch opens and `ST-ST` goes high
again.

The full text is in
[chapter 7, module P](../../circuit-description/modules.md#module-p).

## Adjustments

The manual gives **no adjustment procedure** for this module.

## PCB lay-out

The sheet below is the whole of `CS 7 850`. Module P is its **right-hand
panel**: the circuit diagram, the component and solder side lay-outs, and the
parts list.

<figure class="sheet sheet--fold" markdown>
[![Display + keyboard module N and frontloader module P: the trifold sheet, whose third panel carries the front loader circuit diagram, PCB lay-out and parts list](../n-display-keyboard/assets/web/cs-7-850-module-sheet-p061-062-preview.webp)](../n-display-keyboard/assets/web/cs-7-850-module-sheet-p061-062-zoom.webp)
<figcaption>
  Frontloader module P (mod level 4) — circuit, PCB lay-out and parts, on
  panel 3 of the display + keyboard sheet.
  <span class="cs">CS 7 850</span>
  <span class="src">service manual pages 061, 062</span>
</figcaption>
</figure>

## List of electrical parts

**NFR25 resistors**

| Item | Service code number | Value |
| --- | --- | --- |
| 3010 | 4822 111 30483 | 1 Ω |

**Capacitors**

| Item | Service code number | Value | Rating |
| --- | --- | --- | --- |
| 2001 | 4822 124 22027 | 47 μF | 25 V |
| 2002 | 4822 124 22031 | 4.7 μF | 63 V |

The transistors in the bridge are 7001 and 7002 BC848B, 7003 BC848B, 7004 and
7007 BC368, 7005 and 7006 BC369, with 6003–6007 the protection diodes; the
circuit diagram on panel 3 of the sheet names them all.

## Modification levels

Module P carried **modification level 4 in every production batch** and has no
mod-level sheet in chapter 8 — nothing about it changed that needed
documenting.

Two fault symptoms nonetheless land here by way of module R: **A 1**, the tray
opening at start-up, and **A 2**, no eject when no disc has been inserted. Both
are fixed on
[drive processor module R](../r-drive-processor/index.md), not on this board.

## Related

- [Module circuit descriptions](../../circuit-description/modules.md#module-p) — the chapter 7 text in full
- [Module N — Display + keyboard](../n-display-keyboard/index.md) — carries this module's data sheet
- [Module R — Drive processor](../r-drive-processor/index.md) — drives the loader and reads its switches
- [Demounting](../../general-service/demounting.md) — getting the front loader out
- [Fault-finding charts](../../repair/fault-finding.md) — loading and eject faults
- [Exploded views](../../parts/exploded-views.md) — the front-loader mechanics
