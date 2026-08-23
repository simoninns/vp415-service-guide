---
title: Module R - Drive processor
description: >-
  Drive processor: the microcontroller running the deck servos.
search:
  boost: 2
---

# Module R - Drive processor

Drive processor: the microcontroller running the deck servos.

## Overview

The drive processor runs the deck. Everything on it happens under
microprocessor IC7201, with a 16 K ROM (IC7204) beside it, and it does eight
distinct jobs:

1. Accept and interpret commands from [control module S](../s-control/index.md)
2. Radial tracking and access
3. Manchester code reading
4. Display-on-screen drive
5. The start-up sequence of the disc drive
6. Local control — **standby** and **eject**
7. Audio and video switching
8. **Service diagnostics** — the error codes

| | |
| --- | --- |
| Designation | **R** — drive processor |
| Modification levels | 3 → 7 |
| Data sheet | `CS 7 851`, pages 063–064, panels 2–3 |
| Circuit diagram | `CS 6 883`, pages 065–066 |
| Connectors | `R1`, `R2` |
| Processor | IC7201, 12 MHz (crystal 5001) |
| Firmware | IC7204 — `DRIVE`, TMS 27128, program 3104 103 6803.4 → 6803.6 |
| Talks to module S over | the S-bus, through IC7203, 7206, 7207 and 7216 |

!!! note "This module's data sheet carries module Q as well"

    `CS 7 851` is a trifold: panel 1 is the RC5 circuit of
    [module Q](../q-rc5-receiver/index.md), panel 2 is this module's parts
    list, panel 3 its PCB lay-out.

## The board

<div class="sheet-pair" markdown>
<figure class="sheet sheet--photo" markdown>
[![Module R, component side of the board](assets/web/r-drive-processor-top-preview.webp)](assets/web/r-drive-processor-top-zoom.webp)
<figcaption>
  Module R, component side.
</figcaption>
</figure>
<figure class="sheet sheet--photo" markdown>
[![Module R, solder side of the board](assets/web/r-drive-processor-bottom-preview.webp)](assets/web/r-drive-processor-bottom-zoom.webp)
<figcaption>
  Module R, solder side.
</figcaption>
</figure>
</div>

## Where it sits in the player

One of the two large boards at the right of the chassis, beside
[control module S](../s-control/index.md) and in front of the perforated
screen over [supply module T](../t-supply/index.md) — see the
[module and connector lay-out](../../system/module-layout.md).

## Circuit description

**Command input.** Commands from and responses to module S run over the S-bus:
IC7203 is the port expander through which IC7201 reaches the handshake signals
`DAV` and `DAK`, IC7207 the data input latch, IC7206 the data output latch,
and the handshakes are serviced by D-type flip-flops 7216-2A and 2B.

**Slide motor.** Driven in software. The slide is a stepping motor fed by the
four phase signals `COMM-1`–`COMM-4` and `SL-PWR` from port expander IC7202,
through [slide drive module E](../e-slide-drive/index.md). During normal play
the slide moves when the radial mirror approaches the limit of its deflection:
the mirror offset is measured by comparing `SP-POS` — the radial error from
the mirror drive — against DAC 7218 in IC7210-2A, and the result, `RAD-MIR`,
goes to pin 31 of IC7203.

**Manchester codes.** IC7211 is a dedicated device that reads the Manchester
codes out of the clipped video `CL-VID` and stores them on board for the
processor to read over the data bus, with `ATN`, `TX/RX`, `STB` and `IRQ`
handshaking to IC7201.

Drive and switching signals leave through three 8-bit shift registers, IC7213,
IC7214 and IC7215.

The full text — all eight functions, plus the S-bus description — is in
[chapter 7, module R](../../circuit-description/modules.md#module-r).

## Adjustments

The manual gives **no adjustment procedure** for this module. What it does
carry, and what makes this board the one you reach for first in a fault, is
the diagnostic software: see
[diagnostic mode](../../repair/diagnostic-mode.md) and the
[error codes](../../repair/error-codes.md).

## Circuit diagram

<figure class="sheet sheet--fold" markdown>
[![Drive processor module R - circuit diagram](assets/web/cs-6-883-circuit-p065-066-preview.webp)](assets/web/cs-6-883-circuit-p065-066-zoom.webp)
<figcaption>
  Drive processor module R - circuit diagram.
  <span class="cs">CS 6 883</span>
  <span class="src">service manual pages 065, 066</span>
</figcaption>
</figure>

## PCB lay-out

<figure class="sheet sheet--fold" markdown>
[![RC5 circuit module Q; list of electrical parts module R](assets/web/cs-7-851-circuit-p063-064-preview.webp)](assets/web/cs-7-851-circuit-p063-064-zoom.webp)
<figcaption>
  RC5 circuit module Q; list of electrical parts module R.
  <span class="cs">CS 7 851</span>
  <span class="src">service manual pages 063, 064</span>
</figcaption>
</figure>

## List of electrical parts

**EPROMs (programmed)**

| Item | Service code number | Type |
| --- | --- | --- |
| 7204 | 4822 209 51257 | TMS 27128 — `DRIVE` |

**Crystals**

| Item | Service code number | Value |
| --- | --- | --- |
| 5001 | 4822 242 71663 | 12 MHz |

**Coils**

| Item | Service code number | Value |
| --- | --- | --- |
| 5002 | 4822 158 10101 | 5.3 μH |
| 5003 | 4822 158 10101 | 5.3 μH |
| 5004 | 4822 157 51316 | 120 μH |

**Hours counter**

| Item | Service code number | Description |
| --- | --- | --- |
| 3065 | 4822 344 40081 | Hours counter |

**Capacitors**

| Item | Service code number | Value | Rating |
| --- | --- | --- | --- |
| 2001 | 4822 124 22027 | 47 μF | 25 V |
| 2002 | 4822 124 22027 | 47 μF | 25 V |
| 2003 | 4822 124 22027 | 47 μF | 25 V |
| 2004 | 4822 124 22029 | 2.2 μF | 63 V |
| 2005 | 4822 122 31644 | 2.2 nF | |
| 2006 | 4822 122 32975 | 33 pF | |
| 2007 | 4822 122 32975 | 33 pF | |
| 2008 | 4822 122 31972 | 39 pF | |
| 2009 | 4822 122 32504 | 15 pF | |
| 2010 | 4822 122 32482 | 22 pF | |
| 2011 | 4822 122 31759 | 22 nF | |
| 2012 | 4822 122 31759 | 22 nF | |
| 2013 | 4822 122 31759 | 22 nF | |
| 2014 | 4822 122 31759 | 22 nF | |
| 2015 | 4822 122 31759 | 22 nF | |
| 2016 | 5322 121 54072 | 820 pF | 250 V |
| 2017 | 5322 121 54072 | 820 pF | 250 V |
| 2018 | 4822 124 22187 | 15 μF | 63 V |
| 2101 – 2122 | 4822 122 31759 | 22 nF | |

Items 2101 to 2122 are the supply decoupling and are all the same 22 nF
capacitor; the sheet lists them individually.

## Firmware

One programmed device: the `DRIVE` EPROM at IC7204.

| Program | SW rev. | Introduced | Philips sum16 | Service code number |
| --- | --- | --- | --- | --- |
| 3104 103 6803.4 | 1.5 | 1986-10-30 | `B5F1` | 4822 209 51257 |
| 3104 103 6803.5 | 1.6 | 1986-11-24 | `9DB6` | 4822 209 51257 |
| 3104 103 6803.6 | 1.7 | 1987-02-23 | `68FF` | 4822 209 51257 |

The sum is the quickest way to identify an EPROM you have in front of you, and
the level of the board follows it: **6803.5 is mod level 4, 6803.6 is mod level
6**. What changed at each release is on
[software releases](../../service-information/software-releases.md) —
including that 6803.6 added **error codes 77 and 78**, which is why they are
missing from the manual's own error code table.

**Only the last of the three is in the collection**: 6803.6, sum16 `0x68FF`,
held four times over under different names. It is on the
[firmware](../../reference/firmware.md) page with its size and SHA-256; 6803.4
and 6803.5 have not been dumped.

## Modification levels

The busiest board in the player: **level 3 at first shipment, level 7 by the
last batch**, plus one correction that applies to every level.

- **Correction to the service manual** — R3064 becomes R3069, R3064 becomes
  R3080, C2019 10 μF → 22 μF.
- **Level 4** — EPROM IC7204 `DRIVE` 6803.4 → **6803.5**, which is also the
  fix for fault symptom **A 2**, no eject when no disc has been inserted.
- **Level 5** — R3070 and R3071 (100 k) added, improving the `DR` signal; and
  C2004 2 μF → 10 μF as a temporary way of stopping the drive resetting.
- **Level 6** — EPROM `DRIVE` 6803.5 → **6803.6**.
- **Level 7** — C2018 15 μF → 68 μF, which stops the tray ejecting at start-up
  (fault symptom **A 1**); and the **finger protection circuit for the front
  loader** added: R3064–R3067, C2019, TS7007 and TS7008.

Full tables, with service code numbers:
[chapter 8, module R](../../service-information/modification-levels.md#mod-r).

## Related

- [Diagnostic mode](../../repair/diagnostic-mode.md) — the self-test this module runs
- [Error codes](../../repair/error-codes.md) — what it reports, and what each code means
- [Software releases](../../service-information/software-releases.md) — what changed in `DRIVE` 6803.4, .5 and .6
- [Firmware](../../reference/firmware.md) — dumps of the `DRIVE` EPROM, with checksums
- [Module circuit descriptions](../../circuit-description/modules.md#module-r) — the chapter 7 text in full
- [Modification levels per module](../../service-information/modification-levels.md#mod-r) — five levels of changes
- [Fault symptoms](../../service-information/fault-symptoms.md) — symptoms A 1 and A 2 are fixed here
- [Module Q — RC5 receiver](../q-rc5-receiver/index.md) — shares this data sheet
- [Electrical parts](../../parts/electrical-parts.md) — the collective list of standard components by service code number; the connectors are in [mechanical parts](../../parts/mechanical-parts.md#module-connectors)
