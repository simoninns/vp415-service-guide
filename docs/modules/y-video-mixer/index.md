---
title: Module Y - Video mixer
description: >-
  Video mixer: mode switching, clamping and mixing of video sources.
---

# Module Y - Video mixer

Video mixer: mode switching, clamping and mixing of video sources.

## Overview

The video mixer is what lets a VP415 put computer text and graphics on top of
disc video. It takes RGB from the disc — by way of
[RGB module B](../b-rgb/index.md) and
[analog I/O module Ua](../u-analog-io/index.md) — and RGB (TTL) from the host
computer, and combines them in one of **five modes**:

| Mode | | What you see |
| --- | --- | --- |
| 1 | **LV disc** | video from the LaserVision disc only |
| 2 | **Computer** | signals from the host computer only |
| 3 | **Enhanced** | LV at 100%, and 57% inside a window — the computer's "black" signal generates windows in which the video is shown at reduced intensity |
| 4 | **Mix** | 62% LV + 38% computer — a transparent overlay |
| 5 | **Hard key** | 100% LV *or* 100% computer — computer text and graphics inserted into the video |

The mode is selected by `VP0`–`VP2` from
[control module S](../s-control/index.md).

| | |
| --- | --- |
| Designation | **Y** — video mixer (the manual's survey calls it *VID MIX*) |
| Modification levels | 4 → 6 |
| Data sheet | `CS 7 860`, pages 096–097 (mod level 4) |
| Circuit diagram | `CS 6 892`, pages 094–095 — mode switch, buffer + clamp, mixers |
| Connectors | `Y1` `Y2` `Y3` (RGB TTL in) `Y4` `Y5` |
| Built from | TCA240 transistor arrays — five "mixers" per channel |

## The board

<div class="sheet-pair" markdown>
<figure class="sheet sheet--photo" markdown>
[![Module Y, component side of the board](assets/web/y-video-mixer-top-preview.webp)](assets/web/y-video-mixer-top-zoom.webp)
<figcaption>
  Module Y, component side.
</figcaption>
</figure>
<figure class="sheet sheet--photo" markdown>
[![Module Y, solder side of the board](assets/web/y-video-mixer-bottom-preview.webp)](assets/web/y-video-mixer-bottom-zoom.webp)
<figcaption>
  Module Y, solder side.
</figcaption>
</figure>
</div>

## Where it sits in the player

In the sandwich, with [W](../w-cpu-data-grabber/index.md) and
[X](../x-lv-rom-decoder/index.md), beneath the main module carrier — see
[demounting](../../general-service/demounting.md) and the
[module and connector lay-out](../../system/module-layout.md).

## Circuit description

The board is **three identical channels**; the manual describes the red one
and leaves green and blue to follow. Each channel is built from TCA240
transistor arrays, which the description labels A to E:

| Device | Mixer |
| --- | --- |
| IC7151-2b | A |
| IC7152-2a | B |
| IC7152-2b | C |
| IC7153-2b | D |
| IC7153-2a | E |

`VP0`–`VP2` are decoded in IC7458 into one-of-five outputs `Q0`–`Q4`, and each
mode switches a different combination of mixers:

| Mode | Output | A | B | C | D | E |
| --- | --- | --- | --- | --- | --- | --- |
| 1 | LV disc | off | off | off | off | **on** |
| 2 | Computer | off | off | **on** | **on** | off |
| 3 | Enhanced | **on** | off | off | **on** | **on** |
| 4 | Mix | off | **on** | off | **on** | **on** |
| 5 | Hard key | off | off | **on** | **on** | — |

The full text is in
[chapter 7, module Y](../../circuit-description/modules.md#module-y).

## Adjustments

The manual gives **no adjustment procedure** for this module: the data sheet
carries the PCB lay-out and the parts list only.

## Circuit diagram

<figure class="sheet sheet--fold" markdown>
[![Video mixer module Y - circuit diagram (mode switch / buffer+clamp / mixers)](assets/web/cs-6-892-circuit-p094-095-preview.webp)](assets/web/cs-6-892-circuit-p094-095-zoom.webp)
<figcaption>
  Video mixer module Y - circuit diagram (mode switch / buffer+clamp / mixers).
  <span class="cs">CS 6 892</span>
  <span class="src">service manual pages 094, 095</span>
</figcaption>
</figure>

## PCB lay-out

<figure class="sheet sheet--fold" markdown>
[![Video mixer module Y (mod level 4) - parts](assets/web/cs-7-860-module-sheet-p096-097-preview.webp)](assets/web/cs-7-860-module-sheet-p096-097-zoom.webp)
<figcaption>
  Video mixer module Y (mod level 4) - parts.
  <span class="cs">CS 7 860</span>
  <span class="src">service manual pages 096, 097</span>
</figcaption>
</figure>

## List of electrical parts

**Coils**

| Item | Service code number | Value |
| --- | --- | --- |
| 5401 | 4822 156 21026 | 34 μH |

**NFR25 resistors**

| Item | Service code number | Value |
| --- | --- | --- |
| 3406 | 4822 111 30483 | 1 Ω |
| 3407 | 4822 111 30483 | 1 Ω |
| 3408 | 4822 111 30483 | 1 Ω |

**Capacitors — the three channels**

The 21xx, 22xx and 23xx blocks are the red, green and blue channels, and they
are **identical, part for part**:

| Item (R / G / B) | Service code number | Value | Rating |
| --- | --- | --- | --- |
| 2101 / 2201 / 2301 | 4822 122 32425 | 2.2 pF | |
| 2102 / 2202 / 2302 | 4822 124 22027 | 47 μF | 25 V |
| 2103 / 2203 / 2303 | 5322 122 32839 | 100 nF | |
| 2104 / 2204 / 2304 | 5322 122 32839 | 100 nF | |
| 2105 / 2205 / 2305 | 5322 122 32839 | 100 nF | |
| 2106 / 2206 / 2306 | 5322 122 32839 | 100 nF | |
| 2107 / 2207 / 2307 | 5322 122 32839 | 100 nF | |
| 2108 / 2208 / 2308 | 5322 122 32839 | 100 nF | |
| 2109 / 2209 / 2309 | 5322 122 32839 | 100 nF | |
| 2110 / 2210 / 2310 | 5322 122 32839 | 100 nF | |
| 2111 / 2211 / 2311 | 5322 122 32839 | 100 nF | |
| 2112 / 2212 / 2312 | 5322 122 32839 | 100 nF | |
| 2113 / 2213 / 2313 | 5322 122 32839 | 100 nF | |
| 2114 / 2214 / 2314 | 4822 124 22027 | 47 μF | 25 V |
| 2115 / 2215 / 2315 | 5322 122 32839 | 100 nF | |
| 2116 / 2216 / 2316 | 5322 122 32839 | 100 nF | |
| 2117 / 2217 / 2317 | 5322 122 32839 | 100 nF | |
| 2118 / 2218 / 2318 | 4822 121 41719 | 1 μF | 10% 100 V |

**Capacitors — common**

| Item | Service code number | Value | Rating |
| --- | --- | --- | --- |
| 2401 | 5322 122 32839 | 100 nF | |
| 2402 | 5322 122 32839 | 100 nF | |
| 2403 | 5322 122 32839 | 100 nF | |
| 2404 | 5322 122 32839 | 100 nF | |
| 2405 | 5322 122 32839 | 100 nF | |
| 2406 | 5322 122 32839 | 100 nF | |
| 2407 | 5322 122 32839 | 100 nF | |
| 2408 | 5322 122 32839 | 100 nF | |
| 2409 | 5322 124 21711 | 100 μF | 25 V |
| 2410 | 5322 124 21711 | 100 μF | 25 V |
| 2411 | 5322 124 21711 | 100 μF | 25 V |
| 2412 | 5322 122 32839 | 100 nF | |
| 2413 | 5322 122 32839 | 100 nF | |
| 2414 | 4822 124 22027 | 47 μF | 25 V |
| 2415 | 4822 124 22029 | 2.2 μF | 63 V |
| 2416 | 4822 122 32856 | 8.2 nF | |
| 2417 | 4822 122 31965 | 220 pF | |
| 2418 | 4822 122 31769 | 18 pF | |
| 2419 | 5322 124 21711 | 100 μF | 25 V |
| 2420 | 5322 122 32839 | 100 nF | |
| 2421 | 4822 122 31056 | 12 pF | |

*The vendor OCR lost the item numbers of the third channel's column and the
whole of the fourth; both were re-read off the 300 dpi scan. The three channels
being identical is the sheet's own arrangement, not an editorial compression —
each item is printed individually there.*

## Modification levels

The module shipped at level 4 — the level the data sheet is printed for — and
reached level 6 in the third production batch:

- **Level 5** — D6404 BB112 → BB809, a correction to the service manual; and
  C2416 8.2 nF → 100 pF, curing **horizontal distortion of the computer
  overlay** (fault symptom **D 3**).
- **Level 6** — R3429, a 10 MΩ chip resistor, added in parallel with C2415 to
  cure **jitter of the computer overlay** (fault symptom **D 4**).

Note that the parts list above is the level-4 list, so C2416 appears there as
8.2 nF.

Full tables, with service code numbers:
[chapter 8, module Y](../../service-information/modification-levels.md#mod-y).

## Related

- [Module circuit descriptions](../../circuit-description/modules.md#module-y) — the chapter 7 text in full, including the mixer tables
- [Modification levels per module](../../service-information/modification-levels.md#mod-y) — the level-5 and level-6 changes
- [Fault symptoms](../../service-information/fault-symptoms.md) — the computer-overlay entries
- [Interactive play](../../operating-instructions/interactive-play.md) — the modes seen from the user's side
- [Module S — Control](../s-control/index.md) — sends `VP0`–`VP2`
- [Module U — Analog I/O](../u-analog-io/index.md) — feeds the disc RGB in and takes the mixed RGB out
