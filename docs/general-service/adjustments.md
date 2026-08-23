---
title: Adjustments
description: >-
  Which modules need adjusting after replacement, the equipment required, and
  the video adjustments survey (Fig. 2.1).
---

# Adjustments

The per-module adjustment procedures live on the
[module pages](../modules/index.md). This page carries the general rules that
apply to all of them: what has to be adjusted after a module is swapped, and
what equipment you need on the bench.

## 1. General

For each module an adjustment procedure is given for components that are
replaced during repair.

!!! important "If an entire module is replaced"

    In principle adjustment should **not** take place — with four exceptions:

    | Module replaced | Adjust |
    | --- | --- |
    | [K — HF processor](../modules/k-hf-processor/index.md) | R3043 (video amplitude) |
    | [L — Video drop-out correction](../modules/l-video-dropout-correction/index.md) | R3050 (MTF) |
    | [U — Analog I/O](../modules/u-analog-io/index.md) | R3305 (R−Y gain) and R3315 (B−Y gain) |
    | [B — RGB](../modules/b-rgb/index.md) | R3305 and R3315 **on Analog I/O module U** |

When module H, K, L or Z is replaced, it is advisable to check the CVBS OUT
signal (NOT ENCODED) on BNC3 for correct amplitude and for correct VITS signals
MBI and MBIV. The CVBS OUT signal is described in adjustment 1 of Analog I/O
module U; the VITS signals in adjustment 2 of Video D.O. Corr. module L.

For amplitude adjustments see the video adjustments survey — Fig. 2.1, below.

The adjustments take place without connection of a computer (video overlay) or
external video source, unless stated otherwise.

## 2. Equipment required

- Test disc, 6" or 8"
- Dual-beam scope with delayed timebase

If available:

- Vector scope, **or** a dual-beam scope with X-deflection via the B channel
  (e.g. PM3226P)

Also:

- Scope probes with 1:10 attenuator, preferably FET probes or probes with a
  capacitance < 3 pF
- BNC 75 Ω terminator (4822 263 60037)

The test discs and the extender hardware are listed under
[service tools](service-tools.md).

## Fig. 2.1 — video adjustments survey

The survey traces the video signal from the deck through HF processing, drop-out
correction, timebase correction, video processing, RGB decoding and analog I/O
to the SCART and BNC outputs, and marks where each of the four
replacement-critical presets sits: **R3043** (CVBS gain, module K), **R3050**
(MTF, module L), and **R3305 / R3315** (R−Y and B−Y gain, module U). The
waveforms across the top give the amplitude each stage should produce.

<figure class="sheet sheet--fold" markdown>
[![Video adjustments survey: a block diagram of the video signal path from the deck to the outputs, marked with the four replacement-critical presets and the expected waveform amplitudes](assets/web/cs-7-822-figure-p012-preview.webp)](assets/web/cs-7-822-figure-p012-zoom.webp)
<figcaption>
  Fig. 2.1 — video adjustments survey.
  <span class="cs">CS 7 822</span>
  <span class="src">service manual page 012</span>
</figcaption>
</figure>

<figure class="sheet" markdown>
[![Adjustments: general rules and required equipment](assets/web/cs-7-821-text-p011-preview.webp)](assets/web/cs-7-821-text-p011-zoom.webp)
<figcaption>
  Adjustments — general and required.
  <span class="cs">CS 7 821</span>
  <span class="src">service manual page 011</span>
</figcaption>
</figure>
