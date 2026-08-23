---
title: Module Z - Deck electronics
description: >-
  Deck electronics: laser supply and the laser detection unit.
search:
  boost: 2
---

# Module Z - Deck electronics

Deck electronics: laser supply and the laser detection unit.

## Overview

Deck electronics is the board **under the optical deck chassis**, connected to
the laser detection unit by a flex-foil. It does two things: it runs the
**laser supply**, and it turns the photodiode signals from the LDU into the
signals the rest of the player works with — HF, radial, focus and tilt.

It is also the board with **six adjustment potentiometers on it** and no
adjustment procedure in the manual — see below.

| | |
| --- | --- |
| Designation | **Z** — deck electronics |
| Modification levels | 2 → 3 |
| Data sheet | `CS 7 861`, page 098 — parts and PCB lay-out |
| Circuit diagram | `CS 6 893`, page 099 — laser detection unit |
| Connectors | `Z0` to `Z6` on the deck |
| Out | `HF-OUT1`, `HF-OUT2` · `RAD-ER` · `FOC-ER`, `FPI` · `LA-STA` |

## Where it sits in the player

On the optical deck itself, underneath the deck chassis — the yellow laser
warning label in the overhead photograph on the
[module and connector lay-out](../../system/module-layout.md) page is directly
above it. There are no photographs of this board in the collection's plug-in
module set, because it is not a plug-in module.

!!! danger "Class 1 laser"

    Working on this board means working with the laser supply live and the
    deck open. Read [warnings](../../general-service/warnings.md) first.

## Circuit description

**The laser supply.** The solid-state laser runs from +5 V through a
controllable DC amplifier. Part of the light goes to the optics and part to an
internal monitor diode, whose output is fed back through T7002 and T7003 to
amplifier T7005 — a constant-current loop. The monitor signal also drives
switch T7004, taking `LA-STA` low once the laser is on, which
[drive processor module R](../r-drive-processor/index.md) watches. `LA`
switches the amplifier, and so the laser, on and off through T7001 — **`LA`
low = laser off**.

**HF.** Photodiodes A, B, C and D carry the pit pattern. The sum A+B+C+D goes
through a > 50 kHz high-pass filter to the HF preamplifier, which produces
`HF-OUT1` and `HF-OUT2`, both FM modulated by the disc information.

**Radial.** Photodiodes R1 and R2 produce a radial error when the laser spots
are not exactly on track; the servo preamplifier turns that into `RAD-ER` for
[radial module M](../m-radial/index.md).

The full text — focus, tilt and the active tilt control — is in
[chapter 7, module Z](../../circuit-description/modules.md#module-z).

## Adjustments

**The manual gives no adjustment procedure for this module**, which is
unhelpful, because the board carries six potentiometers and they all matter:

| Item | Value | What it sets |
| --- | --- | --- |
| 3040 | 1 kΩ | HF amplitude |
| 3058 | 1 kΩ | Focus / radial ratio |
| 3066 | 100 kΩ | Focus gain |
| 3076 | 10 kΩ | Radial balance |
| 3079 | 22 kΩ | Radial gain |
| 3088 | 4.7 kΩ | Tilt offset |

Note also that chapter 2 asks you to check `CVBS OUT` after replacing module H,
K, L **or Z** — see [adjustments](../../general-service/adjustments.md).

## Circuit diagram

<figure class="sheet sheet--fold" markdown>
[![Deck electronics module Z - circuit diagram (laser detection unit)](assets/web/cs-6-893-circuit-p099-preview.webp)](assets/web/cs-6-893-circuit-p099-zoom.webp)
<figcaption>
  Deck electronics module Z - circuit diagram (laser detection unit).
  <span class="cs">CS 6 893</span>
  <span class="src">service manual page 099</span>
</figcaption>
</figure>

## PCB lay-out

<figure class="sheet sheet--fold" markdown>
[![Deck electronics module Z - parts](assets/web/cs-7-861-module-sheet-p098-preview.webp)](assets/web/cs-7-861-module-sheet-p098-zoom.webp)
<figcaption>
  Deck electronics module Z - parts.
  <span class="cs">CS 7 861</span>
  <span class="src">service manual page 098</span>
</figcaption>
</figure>

## List of electrical parts

**Diodes**

| Item | Service code number | Type |
| --- | --- | --- |
| — | 4822 130 60493 | Detector diode |
| 6020 | 4822 130 32114 | GP1S04 photo interrupter |

The detector diode has no item number on the sheet; that is how the manual
prints it.

**Potentiometers**

| Item | Service code number | Value | Rating |
| --- | --- | --- | --- |
| 3040 | 4822 100 11152 | 1 kΩ |  |
| 3058 | 4822 100 11152 | 1 kΩ |  |
| 3066 | 4822 100 11156 | 100 kΩ |  |
| 3076 | 4822 100 11154 | 10 kΩ |  |
| 3079 | 4822 100 11155 | 22 kΩ |  |
| 3088 | 4822 100 11153 | 4.7 kΩ |  |

**Fuse Resistors**

| Item | Service code number | Value | Rating |
| --- | --- | --- | --- |
| 3120 | 4822 111 30892 | 27 Ω |  |
| 3121 | 4822 111 30892 | 27 Ω |  |

**Capacitors**

| Item | Service code number | Value | Rating |
| --- | --- | --- | --- |
| 2001 | 4822 122 31759 | 22 nF |  |
| 2002 | 4822 122 32974 | 100 pF |  |
| 2003 | 4822 122 31759 | 22 nF |  |
| 2004 | 4822 124 22194 | 33 μF | 10 V |
| 2005 | 4822 124 22194 | 33 μF | 10 V |
| 2006 | 4822 122 32974 | 100 pF |  |
| 2007 | 4822 122 32542 | 47 nF |  |
| 2023 | 4822 122 31759 | 22 nF |  |
| 2024 | 4822 124 22193 | 10 μF | 16 V |
| 2025 | 4822 124 22192 | 1 μF | 16 V |
| 2026 | 4822 124 22192 | 1 μF | 16 V |
| 2031 | 4822 122 31971 | 10 pF |  |
| 2032 | 4822 122 31971 | 10 pF |  |
| 2033 | 4822 122 32972 | 1 nF |  |
| 2034 | 4822 122 31759 | 22 nF |  |
| 2035 | 4822 122 32975 | 33 pF |  |
| 2036 | 4822 122 32975 | 33 pF |  |
| 2037 | 4822 122 31784 | 4.7 nF |  |
| 2038 | 4822 122 32975 | 33 pF |  |
| 2039 | 4822 122 32975 | 33 pF |  |
| 2042 | 4822 122 31759 | 22 nF |  |
| 2043 | 4822 122 31759 | 22 nF |  |
| 2044 | 4822 122 31966 | 27 pF |  |
| 2045 | 4822 122 31966 | 27 pF |  |
| 2048 | 4822 122 33007 | 330 nF | 25 V |
| 2049 | 4822 122 33007 | 330 nF | 25 V |
| 2051 | 4822 121 51107 | 4.7 μF | 16 V |
| 2052 | 4822 122 31759 | 22 nF |  |
| 2053 | 4822 121 51107 | 4.7 μF | 16 V |
| 2054 | 4822 122 32891 | 68 nF |  |
| 2055 | 4822 124 22192 | 1 μF | 16 V |
| 2056 | 4822 124 22192 | 1 μF | 16 V |

## Modification levels

The module shipped at level 2 and went to level 3 in the fifth production
batch. The chapter 8 sheet records three changes, none of them tied to a level
number on the sheet itself:

- R3104 22 k → 10 k, R3086 6k8 → 33 k, R3087 4k7 → 22 k, R3088 4k7 → 22 k and
  R3089 1 M → 4M7 — a fault in the diagram, and the introduction of a **new
  corner sensor** with a different specification.
- D6021 (HZA92, 8.2 V) added with R3109 and R3110 changed from 10 Ω to 0 Ω,
  because the **tilt motor did not work correctly**.
- D6021 HZA92 → BC548B, "cheaper".

Note that R3088 appears in the parts list above as a 4.7 kΩ potentiometer and
in the mod list as a fixed resistor changing 4k7 → 22 k; the sheets use the
same item number for both, so **check the board**.

Full tables, with service code numbers:
[chapter 8, module Z](../../service-information/modification-levels.md#mod-z).

## Related

- [The optical deck](../../circuit-description/optical-deck.md) — the LDU this board reads
- [Module circuit descriptions](../../circuit-description/modules.md#module-z) — the chapter 7 text in full
- [Warnings](../../general-service/warnings.md) — laser safety
- [Modification levels per module](../../service-information/modification-levels.md#mod-z) — the corner sensor and tilt motor changes
- [Module J — Focus](../j-focus/index.md) — takes `FOC-ER` and `FPI` from here
- [Module M — Radial](../m-radial/index.md) — takes `RAD-ER` from here
- [Module K — HF processor](../k-hf-processor/index.md) — takes the HF signal from here
- [Electrical parts](../../parts/electrical-parts.md) — the collective list of standard components by service code number; the connectors are in [mechanical parts](../../parts/mechanical-parts.md#module-connectors)
