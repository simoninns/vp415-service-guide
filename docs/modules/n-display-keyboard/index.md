---
title: Module N - Display + keyboard
description: >-
  Front-panel display and keyboard.
---

# Module N - Display + keyboard

Front-panel display and keyboard.

## Overview

The front panel: ten indicator LEDs, a buzzer and two buttons — **STANDBY** and
**EJECT** — around a 16-bit LED driver, IC7201.

| | |
| --- | --- |
| Designation | **N** — display + keyboard |
| Modification levels | 1 (unchanged through production) |
| Data sheet | `CS 7 850`, pages 061–062, panels 1–2 |
| Circuit diagram | `CS 6 880`, page 060 |
| Connectors | `N1`, `NN1` |
| Driven from | [control module S](../s-control/index.md) over the P-bus — `SDAT`, `SCLT`, `DLEN` |
| Switches return to | [drive processor module R](../r-drive-processor/index.md) |

!!! note "This sheet carries two modules"

    `CS 7 850` is a trifold: panels 1 and 2 are module N, **panel 3 is
    [frontloader module P](../p-frontloader/index.md)**. The scan is filed
    here; module P's page shows the same sheet and reads panel 3 of it.

## Where it sits in the player

Behind the front panel, with [module Q](../q-rc5-receiver/index.md), where the
overhead photograph on the
[module and connector lay-out](../../system/module-layout.md) page cannot see
it. The board carries the LEDs and the two switches directly.

## Circuit description

IC7201 is fed over the P-bus from IC7211 on
[control module S](../s-control/index.md) as an 18-bit word: a leading 0, 16
data bits, and a terminating bit. Outputs Q1 to Q10 drive the LEDs; Q11 makes
the audio bleep, through IC7202 and transistor 7001.

With Q11 high, NAND IC7202-4A switches the generator IC7202-4B, R3012 and
C2001 off; pin 6 stays high and 7001 does not conduct — no bleep. With Q11 low,
pin 3 of IC7202-4A goes high and IC7202-4B oscillates at the RC time set by
R3012 and C2001, driving the buzzer.

The two front-panel switches are wired back to
[drive processor module R](../r-drive-processor/index.md), not to this board's
own logic.

The full text is in
[chapter 7, module N](../../circuit-description/modules.md#module-n).

## Adjustments

The manual gives **no adjustment procedure** for this module.

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

**Buzzer**

| Item | Service code number | Type |
| --- | --- | --- |
| 1005 | 4822 280 10151 | Buzzer SD120901 |

**LEDs**

| Item | Service code number | Type |
| --- | --- | --- |
| 6001 | 4822 130 80111 | TLSR5101 — red |
| 6002 … 6010 | 4822 130 80113 | TLSG5101 — green |

**Resistor networks**

| Item | Service code number | Value |
| --- | --- | --- |
| 3002 | 4822 116 90249 | 9 × 270 Ω |

**Capacitors**

| Item | Service code number | Value | Rating |
| --- | --- | --- | --- |
| 2001 | 4822 121 41608 | 100 nF | 100 V |
| 2002 | 4822 124 22027 | 47 μF | 25 V |
| 2101 | 4822 122 30103 | 22 nF | 63 V |
| 2102 | 4822 122 30103 | 22 nF | 63 V |

The LED positions on the lay-out are labelled with what they indicate: EJECT,
PAUSE, REPLAY, REPEAT, AUDIO 1, AUDIO 2, CAV, CLV and REMOTE CONTROL, with
6001 the red one beside the two switches.

## Modification levels

Module N carried **modification level 1 in every production batch** and has no
mod-level sheet in chapter 8 — nothing about it changed that needed
documenting.

## Related

- [Module circuit descriptions](../../circuit-description/modules.md#module-n) — the chapter 7 text in full
- [Controls, indicators and connections](../../overview/controls-and-connections.md) — what each indicator means to the user
- [Module S — Control](../s-control/index.md) — drives this board over the P-bus
- [Module P — Frontloader](../p-frontloader/index.md) — shares this data sheet
- [Fault-finding charts](../../repair/fault-finding.md) — dead-display paths
