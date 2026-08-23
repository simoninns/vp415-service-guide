---
title: Module Q - RC5 receiver
description: >-
  RC5 infrared receiver for the remote control handset.
search:
  boost: 2
---

# Module Q - RC5 receiver

RC5 infrared receiver for the remote control handset.

## Overview

Module Q is the infrared front end for the
[RC53 remote control handset](../remote-control/index.md): an IR receiver on
connector `Q1`, an RC5 mirror stage built around transistor 7001, and a wired
remote-control input on `Q2`. Its output, `RC5`, goes to
[control module S](../s-control/index.md).

It is the smallest module in the player, and the least documented one.

| | |
| --- | --- |
| Designation | **Q** — RC5 receiver (the manual's survey calls it *RC5 mirror*) |
| Modification levels | 0 (unchanged through production) |
| Circuit diagram | `CS 7 851`, pages 063–064, **panel 1** — filed under [module R](../r-drive-processor/index.md) |
| Connectors | `Q1` IR receiver · `Q2` wired remote control |
| Supply | `+5SB` — the standby rail, so the receiver is live with the player in standby |

!!! warning "What this printing of the manual does not contain"

    Module Q has **no data sheet, no PCB parts list and no mod-level sheet**,
    and chapter 7 gives it **no circuit description**. Sheets `CS 6 881` and
    `CS 6 882` — the numbers between module N's and module R's circuit
    diagrams, where module Q's own diagram would sit — are **missing from the
    document entirely**.

    What survives is the RC5 circuit on panel 1 of `CS 7 851`, below, plus the
    lay-out drawing of the small board. That is all the manual says about it.

## Where it sits in the player

Behind the front panel beside
[display + keyboard module N](../n-display-keyboard/index.md), where the
overhead photograph on the
[module and connector lay-out](../../system/module-layout.md) page cannot see
it. The lay-out drawing shows it as `IR-REC` with connectors `Q1` and `Q2`.

The `Q1` connector and the RC5 mirror itself are **on the module carrier**, not
on this board — the sheet's own note says so.

## Circuit description

Chapter 7 has no description of this module. What the RC5 circuit on the sheet
shows:

The IR receiver on `Q1` contains a photodiode, a preamplifier and a shaper, and
puts the demodulated RC5 bit stream out as `IR-REC` on `1Q1`/`2Q1`. That goes
to the RC5 mirror stage — transistor 7001 (BC558B) with R3001 220 k, R3002 and
R3003 33 k — which inverts and buffers it.

The wired remote-control socket on `Q2` feeds the same line as `RC5-INT`, so a
wired controller and the handset use one path. The combined `RC5` signal leaves
for [control module S](../s-control/index.md).

Both the IR receiver and the mirror run from `+5SB`, the standby supply.

## Adjustments

The manual gives **no adjustment procedure** for this module.

## Circuit diagram

The sheet below is the whole of `CS 7 851`. Module Q is its **left-hand
panel**: the RC5 circuit and the small lay-out of the RC5 mirror board. Panels
2 and 3 are [drive processor module R](../r-drive-processor/index.md).

<figure class="sheet sheet--fold" markdown>
[![RC5 circuit module Q on panel 1 of the sheet, with the IR receiver, the RC5 mirror stage and the wired remote control input; panels 2 and 3 carry the drive processor parts list and PCB lay-out](../r-drive-processor/assets/web/cs-7-851-circuit-p063-064-preview.webp)](../r-drive-processor/assets/web/cs-7-851-circuit-p063-064-zoom.webp)
<figcaption>
  RC5 circuit module Q — panel 1 of the drive processor sheet.
  <span class="cs">CS 7 851</span>
  <span class="src">service manual pages 063, 064</span>
</figcaption>
</figure>

## List of electrical parts

The manual prints **no parts list for module Q**. The components named on the
RC5 circuit are 7001 BC558B, R3001 220 k, R3002 and R3003 33 k; the receiver
itself, `R.C.-R`, is a service item in its own right:

| Designation | Service code number | Description |
| --- | --- | --- |
| R.C.-R | 4822 212 21449 | Remote control receiver |
| R.C.-T | 4822 218 20607 | Remote control transmitter |

Both are from the collective
[electrical parts list](../../parts/electrical-parts.md).

## Modification levels

Module Q carried **modification level 0 in every production batch** and has no
mod-level sheet in chapter 8.

## Related

- [Remote control transmitter](../remote-control/index.md) — the handset this module listens to
- [Module S — Control](../s-control/index.md) — receives the `RC5` signal
- [Module R — Drive processor](../r-drive-processor/index.md) — carries this module's sheet
- [Electrical parts](../../parts/electrical-parts.md) — the receiver and transmitter service codes
- [Module and connector lay-out](../../system/module-layout.md) — where `IR-REC` sits
- [Module circuit descriptions](../../circuit-description/modules.md#module-r) — chapter 7 gives module Q no section of its own; its RC5 circuit is described with module R, whose sheet carries it
- [Modification levels per module](../../service-information/modification-levels.md#survey-of-modification-levels) — module Q has no mod-level sheet: the survey shows it at level 0 in every production batch
