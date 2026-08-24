---
title: Module V - Module carrier
description: >-
  The module carrier: backplane wiring and connector pinning.
search:
  boost: 2
---

# Module V - Module carrier

The module carrier: backplane wiring and connector pinning.

## Overview

Module V is the **backplane**: the board every plug-in module plugs into, and
the wiring between them. It carries no active circuitry of its own — which is
why the manual gives it a PCB lay-out and nothing else — but it is the map you
need whenever a circuit diagram hands you a connector designation and you have
to find the other end of the wire.

| | |
| --- | --- |
| Designation | **V** — module carrier |
| Modification levels | 1 → 3 |
| PCB lay-out | `CS 7 836`, pages 030–031 — three panels: component side, solder side, and the mod-level-1 sheet |
| Circuit diagram | none — the module has no active circuit |
| Parts list | none |

## Where it sits in the player

It *is* the player's floor: the large board under the module cages, spanning
the chassis. Every module in the overhead photograph on the
[module and connector lay-out](../../system/module-layout.md) page is plugged
into it.

## Connector reference

The carrier's connectors are named after the module that plugs into them, and
the designation on a circuit diagram is read **pin first**: `6B2` is pin 6 of
connector `B2`, which belongs to [module B](../b-rgb/index.md).

| Group | Connectors |
| --- | --- |
| Plug-in modules, left cage | `A1` `A2` · `B1` `B2` `B3` · `C1` `C2` · `D1` `D2` `D3` |
| Flat modules, front row | `E1` · `F1` `F2` · `G1` `G2` · `H1` `H2` · `I1` `I2` |
| Plug-in modules, right cage | `J1` · `K1` `K2` · `L1` `L2` · `M1` `M2` |
| Large boards | `R1` `R2` · `S1` `S2` `S3` · `T1` `T2` |
| Analog I/O | `U1` — the 32-way |
| Sandwich | `WW1` · `XX1` |
| Front panel and loader | `NN1` · `OO1` `OO2` |
| Deck | `ZZ1` `ZZ4` `ZZ5` `ZZ6` |
| Rear panel | `RS232` |

Pin 1 of each connector is marked on both drawings. What travels between them
is on the [wiring diagrams](../../system/wiring-diagrams.md), and what each
signal name means is on the
[alphabetical signal listing](../../system/signal-listing.md).

<figure class="sheet sheet--fold sheet--photo" markdown>
[![The module carrier drawn as a clean line diagram, component side, with every connector labelled and its pin numbering shown: A1 and A2, B1 to B3, C1 and C2, D1 to D3, E1, F1, F2, G1, G2, H1, H2, I1, I2, J1, K1, K2, L1, L2, M1, M2, R1, R2, S1 to S3, T1, T2, U1, WW1, XX1, NN1, OO1, OO2, ZZ1, ZZ4, ZZ5, ZZ6 and the RS232 connector](assets/web/module-carrier-diagram-preview.webp)](assets/web/module-carrier-diagram-zoom.webp)
<figcaption>
  The module carrier, component side, redrawn clean — every connector with its
  designation and pin numbering. Easier to read than the scan below; the scan
  is the authority.
</figcaption>
</figure>

## Circuit description

Chapter 7 has **no circuit description for module V**, and none is needed: the
board is copper and connectors. Its behaviour is the
[wiring diagrams](../../system/wiring-diagrams.md).

One thing does get *added* to it, though. The level-8 modification on
[RGB module B](../b-rgb/index.md) — fault symptom **D 2**, colour loss when two
disc drives run synchronously and the slave is in still mode — requires **a
link between `9C1` and `7B3` on this board** as well as the resistor on module
B. If a player has that modification, expect a wire on the carrier.

## Adjustments

None — there is nothing on this board to adjust.

## PCB lay-out

The sheet is a trifold: **component side**, **solder side**, and a third panel
headed *module carrier V (mod level 1)*.

<figure class="sheet sheet--fold" markdown>
[![Module carrier V PCB lay-out: the component side and solder side of the backplane, with every module connector in position and its pin numbering](assets/web/cs-7-836-pcb-layout-p030-031-preview.webp)](assets/web/cs-7-836-pcb-layout-p030-031-zoom.webp)
<figcaption>
  Module carrier V — PCB lay-out, component and solder side.
  <span class="cs">CS 7 836</span>
  <span class="src">service manual pages 030, 031</span>
</figcaption>
</figure>

## List of electrical parts

The manual prints **no parts list for module V**. The only serviceable items on
the board are the connectors themselves.

## Modification levels

The survey records the carrier at **level 1 for most of production and level 3
in the last batch**, but there is no mod-level sheet for it in chapter 8, so
what changed between them is not documented.

## Related

- [Module and connector lay-out](../../system/module-layout.md) — the same connectors drawn in their physical positions
- [Wiring diagrams](../../system/wiring-diagrams.md) — what runs between them
- [Alphabetical signal listing](../../system/signal-listing.md) — what each signal name means
- [Connector pinning](../../overview/connector-pinning.md) — the external sockets
- [Fault symptoms](../../service-information/fault-symptoms.md) — symptom D 2 adds a link to this board
- [Module B — RGB](../b-rgb/index.md) — whose level-8 modification needs it
- [Module circuit descriptions](../../circuit-description/modules/index.md) — chapter 7 describes no circuit here: the carrier is a backplane, and every signal on it belongs to another module
- [Modification levels per module](../../service-information/modification-levels.md#survey-of-modification-levels) — the survey has module V going from level 1 to level 3, but chapter 8 carries no mod-level sheet for it: what changed is not documented
- [Electrical parts](../../parts/electrical-parts.md) — the collective list of standard components by service code number; the connectors are in [mechanical parts](../../parts/mechanical-parts.md#module-connectors)
