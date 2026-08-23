---
title: Module Y - Video mixer
description: >-
  Video mixer: mode switching, clamping and mixing of video sources.
---

<!-- drafted by tools/import_modules.py - hand-edited afterwards -->

# Module Y - Video mixer

Video mixer: mode switching, clamping and mixing of video sources.

## Overview

| | |
| --- | --- |
| Designation | **Y** |
| Modification levels | 4 → 6 |
| Circuit diagram | `CS 6 892`, pages 094, 095 |
| Data sheet | `CS 7 860`, pages 096, 097 |

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

See the [module and connector lay-out](../../system/module-layout.md).

## Circuit description

[Chapter 7, module Y](../../circuit-description/modules.md#module-y).

## Adjustments

None.

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

| Item | Service code number | Value | Rating |
| --- | --- | --- | --- |
| 5401 | 4822 156 21026 | 34 μH |  |

**NFR25 Resistors**

| Item | Service code number | Value | Rating |
| --- | --- | --- | --- |
| 3406 | 4822 111 30483 | 1 Ω |  |
| 3407 | 4822 111 30483 | 1 Ω |  |
| 3408 | 4822 111 30483 | 1 Ω |  |

**Capacitors**

| Item | Service code number | Value | Rating |
| --- | --- | --- | --- |
| 2101 | 4822 122 32425 | 2.2 pF |  |
| 2102 | 4822 124 22027 | 47 μF | 25 V |
| 2103 | 5322 122 32839 | 100 nF |  |
| 2104 | 5322 122 32839 | 100 nF |  |
| 2105 | 5322 122 32839 | 100 nF |  |
| 2106 | 5322 122 32839 | 100 nF |  |
| 2107 | 5322 122 32839 | 100 nF |  |
| 2108 | 5322 122 32839 | 100 nF |  |
| 2109 | 5322 122 32839 | 100 nF |  |
| 2110 | 5322 122 32839 | 100 nF |  |
| 2111 | 5322 122 32839 | 100 nF |  |
| 2112 | 5322 122 32839 | 100 nF |  |
| 2113 | 5322 122 32839 | 100 nF |  |
| 2114 | 4822 124 22027 | 47 μF | 25 V |
| 2115 | 5322 122 32839 | 100 nF |  |
| 2116 | 5322 122 32839 | 100 nF |  |
| 2117 | 5322 122 32839 | 100 nF |  |
| 2118 | 4822 121 41719 | 1 μF | 10% 100 V |
| 2201 | 4822 122 32425 | 2.2 pF |  |
| 2202 | 4822 124 22027 | 47 μF | 25 V |
| 2203 | 5322 122 32839 | 100 nF |  |
| 2204 | 5322 122 32839 | 100 nF |  |
| 2205 | 5322 122 32839 | 100 nF |  |
| 2206 | 5322 122 32839 | 100 nF |  |
| 2207 | 5322 122 32839 | 100 nF |  |
| 2208 | 5322 122 32839 | 100 nF |  |
| 2209 | 5322 122 32839 | 100 nF |  |
| 2210 | 5322 122 32839 | 100 nF |  |
| 2211 | 5322 122 32839 | 100 nF |  |
| 2212 | 5322 122 32839 | 100 nF |  |
| 2213 | 5322 122 32839 | 100 nF |  |
| 2214 | 4822 124 22027 | 47 μF | 25 V |
| 2215 | 5322 122 32839 | 100 nF |  |
| 2216 | 5322 122 32839 | 100 nF |  |
| 2217 | 5322 122 32839 | 100 nF |  |
| 2218 | 4822 121 41719 | 1 μF | 10% 100 V |
| 2301 |  |  |  |
| 2302 |  |  |  |
| 2303 |  |  |  |
| 2304 |  |  |  |
| 2305 |  |  |  |
| 2306 |  |  |  |
| 2307 |  |  |  |
| 2308 |  |  |  |
| 2309 |  |  |  |
| 2310 |  |  |  |
| 2311 |  |  |  |
| 2312 |  |  |  |
| 2313 |  |  |  |
| 2314 |  |  |  |
| 2315 |  |  |  |
| 2316 |  |  |  |
| 2317 |  |  |  |
| 2318 |  |  |  |

**Other**

| Item | Service code number | Value | Rating |
| --- | --- | --- | --- |
|  | 4822 122 32425 | 2.2 pF |  |
|  | 4822 124 22027 | 47 μF | 25 V |
|  | 5322 122 32839 | 100 nF |  |
|  | 5322 122 32839 | 100 nF |  |
|  | 5322 122 32839 | 100 nF |  |
|  | 5322 122 32839 | 100 nF |  |
|  | 5322 122 32839 | 100 nF |  |
|  | 5322 122 32839 | 100 nF |  |
|  | 5322 122 32839 | 100 nF |  |
|  | 5322 122 32839 | 100 nF |  |
|  | 5322 122 32839 | 100 nF |  |
|  | 5322 122 32839 | 100 nF |  |
|  | 5322 122 32839 | 100 nF |  |
|  | 4822 124 22027 | 47 μF | 25 V |
|  | 5322 122 32839 | 100 nF |  |
|  | 5322 122 32839 | 100 nF |  |
|  | 5322 122 32839 | 100 nF |  |
|  | 4822 121 41719 | 1 μF | 10% 100 V |

## Modification levels

[Chapter 8, module Y](../../service-information/modification-levels.md#mod-y).

## Related

- [Module circuit descriptions](../../circuit-description/modules.md)
- [VP400 series architecture](../../circuit-description/vp400-series.md)
- [Fault-finding charts](../../repair/fault-finding.md)
- [Fault symptoms](../../service-information/fault-symptoms.md)
- [Modification levels per module](../../service-information/modification-levels.md)
- [Module and connector lay-out](../../system/module-layout.md)
