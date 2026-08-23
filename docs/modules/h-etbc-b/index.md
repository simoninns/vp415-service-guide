---
title: Module H - ETBC-B
description: >-
  ETBC-B, the first half of the electronic timebase corrector.
---

<!-- drafted by tools/import_modules.py - hand-edited afterwards -->

# Module H - ETBC-B

ETBC-B, the first half of the electronic timebase corrector.

## Overview

| | |
| --- | --- |
| Designation | **H** |
| Modification levels | 5 |
| Circuit diagram | `CS 6 874`, page 048 |
| Data sheet | `CS 7 844`, page 049 |

## The board

<div class="sheet-pair" markdown>
<figure class="sheet sheet--photo" markdown>
[![Module H, component side of the board](assets/web/h-etbc-b-top-preview.webp)](assets/web/h-etbc-b-top-zoom.webp)
<figcaption>
  Module H, component side.
</figcaption>
</figure>
<figure class="sheet sheet--photo" markdown>
[![Module H, solder side of the board](assets/web/h-etbc-b-bottom-preview.webp)](assets/web/h-etbc-b-bottom-zoom.webp)
<figcaption>
  Module H, solder side.
</figcaption>
</figure>
</div>

## Where it sits in the player

See the [module and connector lay-out](../../system/module-layout.md).

## Circuit description

[Chapter 7, module H](../../circuit-description/modules.md#module-h).

## Adjustments

# Required

Test disc

Scope

DC supply

# Adjustment conditions

Load test disc.

Still picture, colour bar (picture no. 6200).

# Adjustments

1) R3012, R3013 (CCD pass-through, limiter freq. sweep)

- Using the scope, measure signal CV-DOC on 2H2 (A channel) and CV-TBC on 2H1 (B channel).
- Short-circuit C2003 (9-IC7206 to ground).
- Display the first lines of the video signal on the scope by means of the DTB.
- Adjust R3012 for a delay of 70 μsec ± 1 μsec between the two signals.
- Remove the short-circuit of C2003.
- Connect with the DC supply a variable voltage to junction R3001, R3002, C2001 (TANG-ER).
- Measure the delay of the CV-DOC and CV-TBC signals as a function of the DC voltage presented:

0V : 46 μsec ± 1.5 μsec

+3V : 70 μsec ± 1 μsec

+6V : 91 μsec ± 1.5 μsec

Correct deviations by adjusting R3013.

2) R3063 (CCD adjust)

- Search for pict. no. 470 (white).
- Measure the CV-TBM signal on p.1-IC7201 with the scope.
- Adjust R3063 for a black level amplitude of 3.2Vpp.
- The CV-TBM signal on 7H1 is shown in fig. H1.

3) R3087 (Video adjust)

- Measure the CVBS OUT-signal on BNC3 (rear) with the scope (75 Ω terminated).
- Press switch SK2 on analog I/O module U (pos. NOT ENCODED).
- Adjust R3087 for a CVBS amplitude (top white-sync bottom) of 1 Vpp.
- Switch SK2 back into the earlier position.

4) R3134 (video time errors)

- Search picture no. 1000 (blue picture) and adjust R3134 for minimum dark bars.
- Search picture no 1800 (yellow picture) and adjust R3134 for minimum red stripes.
- Repeat these two adjustments if necessary.

5) R3122 (audio time errors)

- Switch the player into the normal play mode with sound modulation.
- Measure the AC signal on E-TS7029 and adjust R3122 for minimum AC.

# Adjustment when item replaced

replaced

IC7201

IC7206

adjust

R3063, R3087

R3012, R3013

| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

## Circuit diagram

<figure class="sheet sheet--fold" markdown>
[![ETBC-B module H - circuit diagram](assets/web/cs-6-874-circuit-p048-preview.webp)](assets/web/cs-6-874-circuit-p048-zoom.webp)
<figcaption>
  ETBC-B module H - circuit diagram.
  <span class="cs">CS 6 874</span>
  <span class="src">service manual page 048</span>
</figcaption>
</figure>

## PCB lay-out

<figure class="sheet sheet--fold" markdown>
[![ETBC-B module H (mod level 5) - adjustments / PCB / parts](assets/web/cs-7-844-module-sheet-p049-preview.webp)](assets/web/cs-7-844-module-sheet-p049-zoom.webp)
<figcaption>
  ETBC-B module H (mod level 5) - adjustments / PCB / parts.
  <span class="cs">CS 7 844</span>
  <span class="src">service manual page 049</span>
</figcaption>
</figure>

## List of electrical parts

**Coils**

| Item | Service code number | Value | Rating |
| --- | --- | --- | --- |
| 5001 | 4822 156 11002 | 7.7 μH |  |
| 5002 | 4822 156 10998 | 3 μH |  |
| 5003 | 4822 156 11001 | 6 μH |  |
| 5004 | 4822 156 11001 | 6 μH |  |
| 5005 | 4822 156 11001 | 6 μH |  |
| 5006 | 4822 156 11001 | 6 μH |  |
| 5007 | 4822 156 11001 | 6 μH |  |
| 5008 | 4822 156 10998 | 3 μH |  |
| 5009 | 4822 156 11004 | 26.5 μH |  |
| 5010 | 4822 156 11006 | 54 μH |  |
| 5011 | 4822 156 11004 | 26.5 μH |  |

**Potentiometers**

| Item | Service code number | Value | Rating |
| --- | --- | --- | --- |
| 3012 | 5322 101 10627 | 10 kΩ |  |
| 3013 | 5322 101 10628 | 22 kΩ |  |
| 3063 | 4822 100 20151 | 1 kΩ |  |
| 3087 | 4822 100 10254 | 1 kΩ |  |
| 3122 | 5322 101 10628 | 22 kΩ |  |
| 3134 | 5322 101 10628 | 22 kΩ |  |

**Fuse Resistors**

| Item | Service code number | Value | Rating |
| --- | --- | --- | --- |
| 3137 | 4822 111 10165 | 10Ω |  |
| 3138 | 4822 111 10165 | 10Ω |  |

**Capacitors**

| Item | Service code number | Value | Rating |
| --- | --- | --- | --- |
| 2001 | 4822 121 41874 | 270 nF | 63 V |
| 2002 | 4822 122 32541 | 27 nF |  |
| 2003 | 4822 122 31916 | 5.6 nF |  |
| 2004 | 4822 122 31971 | 10 pF |  |
| 2005 | 4822 122 31758 | 22 nF |  |
| 2006 | 5322 124 21643 | 22 μF | 40 V |
| 2007 | 4822 124 22027 | 47 μF | 25 V |
| 2008 | 4822 122 31758 | 22 nF |  |
| 2009 | 4822 122 31767 | 150 pF |  |
| 2010 | 4822 122 31767 | 150 pF |  |
| 2011 | 4822 124 22027 | 47 μF | 25 V |
| 2012 | 5322 122 32839 | 100 nF |  |
| 2013 | 4822 121 41719 | 1 μF | 10% 100 V |
| 2014 | 5322 122 32839 | 100 nF |  |
| 2015 | 5322 124 21749 | 10 μF | 63 V |
| 2016 | 4822 122 32442 | 10 nF |  |
| 2017 | 4822 124 22188 | 3.3 μF | 63 V |
| 2018 | 4822 122 32442 | 10 nF |  |
| 2019 | 5322 122 32839 | 100 nF |  |
| 2020 | 5322 122 32839 | 100 nF |  |
| 2021 | 5322 124 21643 | 22 μF | 40 V |
| 2022 | 5322 124 21643 | 22 μF | 40 V |
| 2023 | 4822 124 22188 | 3.3 μF | 63 V |
| 2024 | 5322 124 21749 | 10 μF | 63 V |
| 2025 | 4822 122 32442 | 10 nF |  |
| 2026 | 5322 124 21749 | 10 μF | 63 V |
| 2027 | 5322 124 21749 | 10 μF | 63 V |
| 2028 | 4822 122 32442 | 10 nF | PCB 3/1/64 |
| 2029 | 4822 124 22027 | 47 μF | 25 V |
| 2030 | 5322 122 31647 | 1 nF |  |
| 2031 | 5322 124 21643 | 22 μF | 40 V |
| 2032 | 4822 124 22027 | 47 μF | 25 V |
| 2033 | 4822 124 22027 | 47 μF | 25 V |
| 2034 | 5322 124 21643 | 22 μF | 40 V |
| 2035 | 4822 122 31759 | 22 nF |  |
| 2036 | 5322 124 21643 | 22 μF | 40 V |
| 2037 | 4822 124 22027 | 47 μF | 25 V |
| 2038 | 4822 124 22027 | 47 μF | 25 V |
| 2040 | 4822 124 22027 | 47 μF | 25 V |
| 2042 | 4822 124 22027 | 47 μF | 25 V |
| 2043 | 4822 124 22027 | 47 μF | 25 V |
| 2044 | 4822 122 31759 | 22 nF |  |
| 2045 | 5322 124 21749 | 10 μF | 63 V |
| 2046 | 4822 122 31759 | 22 nF |  |
| 2047 | 4822 122 31759 | 22 nF |  |
| 2050 | 4822 122 32142 | 270 pF |  |
| 2051 | 4822 122 31759 | 22 nF |  |
| 2052 | 4822 122 31759 | 22 nF |  |
| 2053 | 4822 124 22028 | 1 μF | 63 V |
| 2054 | 5322 122 32839 | 130 nF |  |
| 2055 | 5322 124 21643 | 22 μF | 40 V |
| 2057 | 4822 122 31759 | 22 nF |  |
| 2057 | 5322 124 21643 | 22 μF | 40 V |
| 2058 | 4822 122 31759 | 22 nF |  |

## Modification levels

[Chapter 8, module H](../../service-information/modification-levels.md#mod-h).

## Related

- [The LaserVision system](../../circuit-description/laservision-system.md)
- [Module circuit descriptions](../../circuit-description/modules.md)
- [VP400 series architecture](../../circuit-description/vp400-series.md)
- [Modification levels per module](../../service-information/modification-levels.md)
- [Module and connector lay-out](../../system/module-layout.md)
