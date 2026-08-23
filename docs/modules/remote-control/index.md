---
title: Remote control transmitter
description: >-
  The RC53 infrared remote control handset shipped with the player.
---

# Remote control transmitter

The RC53 infrared remote control handset shipped with the player.

## Overview

The **RC53** infrared handset, shared between the VP410 and the VP415. Its
sheet is the last in chapter 4, and the only one in the manual that carries an
**exploded view, a mechanical parts list, a PCB lay-out and a circuit diagram
on one page**.

The handset is built around a **SAA3006P** keyboard scanner and RC5 encoder,
running from four **R03P 1.5 V** cells with a CSB429 ceramic resonator. Its
output goes two ways — infrared through LEDs 6003 and 6004, and a **wired
remote** socket — and both reach
[RC5 receiver module Q](../q-rc5-receiver/index.md) in the player.

| | |
| --- | --- |
| Type | **RC53** — RC53/VP410/VP415 transmitter |
| Sheet | `CS 7 862`, page 100 |
| Service code number | 4822 218 20607 — transmitter complete |
| Batteries | 4 × R03P 1.5 V (the sheet also gives 4 × LR03) |
| Encoder | 7001 SAA3006P |
| Resonator | 1001 CSB429 |

## The board

<div class="sheet-pair" markdown>
<figure class="sheet sheet--photo" markdown>
[![Module RC, component side of the board](assets/web/remote-control-top-preview.webp)](assets/web/remote-control-top-zoom.webp)
<figcaption>
  Module RC, component side.
</figcaption>
</figure>
<figure class="sheet sheet--photo" markdown>
[![Module RC, solder side of the board](assets/web/remote-control-bottom-preview.webp)](assets/web/remote-control-bottom-zoom.webp)
<figcaption>
  Module RC, solder side.
</figcaption>
</figure>
</div>

## Where it sits in the player

It does not — it is the only item on this site that lives outside the machine.
The player's end of the link is
[RC5 receiver module Q](../q-rc5-receiver/index.md), behind the front panel.

## Circuit description

The manual gives **no prose circuit description** for the handset; what it
gives is the circuit diagram on the sheet, which is legible enough to follow.

The keyboard is a matrix — `X0`–`X7` against `Y0`–`Y7`, with `Z0`–`Z3`
selecting the system — scanned by IC7001, a SAA3006P *keyboard scanner and
system select* with the timing and coding functions on the same chip. The
`DATA` output on pin 8 drives 7002 (BC548B) and 7003 (BC328-40), which switch
the two infrared LEDs 6003 and 6004 (CQY89A-2) through R3004, a 0.62 Ω
current-setting resistor. The same data line feeds the **wired RC** socket.
6005 (BA317) and the RC network on `OSC` complete the oscillator and reset
arrangement, and C2001, 1000 μF, holds the supply up during a transmit burst.

## Adjustments

None — there is nothing on the handset to adjust.

## The sheet

`CS 7 862` carries everything about the handset on one page: the key layout as
the user sees it, an exploded view of the sixteen mechanical parts, the PCB
lay-out with its wiring to the keyboard, and the circuit diagram of the
encoder.

<figure class="sheet sheet--fold" markdown>
[![Remote control RC53/VP410/VP415 transmitter - exploded view / PCB](assets/web/cs-7-862-module-sheet-p100-preview.webp)](assets/web/cs-7-862-module-sheet-p100-zoom.webp)
<figcaption>
  Remote control RC53/VP410/VP415 transmitter - exploded view / PCB.
  <span class="cs">CS 7 862</span>
  <span class="src">service manual page 100</span>
</figcaption>
</figure>

## List of electrical parts

**Batteries**

4 × R03P 1.5 V.

**Crystals**

| Item | Service code number | Type |
| --- | --- | --- |
| 1001 | 4822 242 71498 | CSB429 |

**Integrated circuits**

| Item | Service code number | Type |
| --- | --- | --- |
| 7001 | 4822 209 81891 | SAA3006P |

**Transistors**

| Item | Service code number | Type |
| --- | --- | --- |
| 7002 | 4822 130 40937 | BC548B |
| 7003 | 4822 130 41715 | BC328-40 |

**LEDs**

| Item | Service code number | Type |
| --- | --- | --- |
| 6003 | 4822 130 31332 | CQY89A-2 |
| 6004 | 4822 130 31332 | CQY89A-2 |

**Diodes**

| Item | Service code number | Type |
| --- | --- | --- |
| 6005 | 4822 130 30847 | BA317 |

**Capacitors**

| Item | Service code number | Value | Rating |
| --- | --- | --- | --- |
| 2001 | 4822 124 21341 | 1000 μF | 8 V |

**Resistors**

| Item | Service code number | Value |
| --- | --- | --- |
| 3004 | 4822 110 73027 | 0.62 Ω |

## Mechanical parts

The exploded view numbers the parts 1 to 16:

| No. | Service code number | Part |
| --- | --- | --- |
| 1 | 4822 218 20607 | Transmitter complete |
| 2 | 4822 432 30284 | Top cover |
| 3 | 4822 410 25423 | Knob assembly |
| 4 | 4822 276 80313 | Switch panel |
| 5 | 4822 432 30283 | Casing |
| 6 | 4822 492 62879 | Battery contact |
| 7 | 4822 492 62881 | Battery contact |
| 8 | 4822 492 62883 | Battery contact |
| 9 | 4822 267 50418 | Connector |
| 10 | 4822 492 62904 | Spring |
| 11 | 4822 432 30282 | Bottom |
| 12 | 4822 432 30281 | Battery lid |
| 13 | 4822 214 50358 | Printed board |
| 14 | 4822 256 90506 | LED holder |
| 15 | 4822 492 62882 | Battery contact |
| 16 | 4822 267 50443 | Connector |

## Modification levels

The handset has **no entry in the modification level survey and no mod-level
sheet** — it is ordered complete, as 4822 218 20607.

## Related

- [Module Q — RC5 receiver](../q-rc5-receiver/index.md) — the player's end of the link
- [Controls, indicators and connections](../../overview/controls-and-connections.md) — what each key does
- [Special play functions](../../operating-instructions/special-play-functions.md) — the keys in use
- [F-code programming](../../operating-instructions/f-code-programming.md) — the `GO TO` and numeric keys
- [Electrical parts](../../parts/electrical-parts.md) — the transmitter and receiver service codes
