---
title: Modules
description: >-
  Chapter 4 and the heart of this site: one page per plug-in module, A to Z, plus the remote control.
---

# Modules

Chapter 4 of the service manual, and the heart of this site. Every module in
the player has a page here carrying, in one place: what the module does, both
sides of the board photographed, where it sits, the circuit description from
chapter 7, the adjustment procedure, the circuit diagram, the PCB lay-out, the
list of electrical parts, and what changed at each modification level.

## Survey of modules

| | | | | |
| --- | --- | --- | --- | --- |
| **A** [Audio processor](a-audio-processor/index.md) | **B** [RGB](b-rgb/index.md) | **C** [Video processor](c-video-processor/index.md) | **D** [Ref. source](d-reference-source/index.md) | **E** [Slide drive](e-slide-drive/index.md) |
| **F** [Motor + sequence](f-motor-sequence/index.md) | **G** [Gen lock](g-genlock/index.md) | **H** [ETBC B](h-etbc-b/index.md) | **I** [ETBC C](i-etbc-c/index.md) | **J** [Focus](j-focus/index.md) |
| **K** [HF processor](k-hf-processor/index.md) | **L** [Video D.O.](l-video-dropout-correction/index.md) | **M** [Radial](m-radial/index.md) | **N** [Display + keyboard](n-display-keyboard/index.md) | **P** [Front loader](p-frontloader/index.md) |
| **Q** [RC5 mirror](q-rc5-receiver/index.md) | **R** [Drive processor](r-drive-processor/index.md) | **S** [Control](s-control/index.md) | **T** [Supply](t-supply/index.md) | **U** [Analog I/O](u-analog-io/index.md) |
| **V** [Module carrier](v-module-carrier/index.md) | **W** [CPU + data grabber](w-cpu-data-grabber/index.md) | **X** [LV-ROM decoder](x-lv-rom-decoder/index.md) | **Y** [Video mixer](y-video-mixer/index.md) | **Z** [Deck electronics](z-deck-electronics/index.md) |
| [Remote control](remote-control/index.md) | | | | |

There is no module O: the manual's survey goes straight from N to P, and so do
the connector designations on the carrier.

<figure class="sheet" markdown>
[![Survey of modules VP415: a table of the twenty-five module letters A to Z against their descriptions, from audio processor to deck electronics](assets/web/cs-7-855-table-p029-preview.webp)](assets/web/cs-7-855-table-p029-zoom.webp)
<figcaption>
  Survey of modules VP415.
  <span class="cs">CS 7 855</span>
  <span class="src">service manual page 029</span>
</figcaption>
</figure>

## Which modules a VP410 does not have

The sandwich — [W](w-cpu-data-grabber/index.md),
[X](x-lv-rom-decoder/index.md) and [Y](y-video-mixer/index.md) — is what makes
a VP415 rather than a VP410: the LV-ROM data path and the computer-video mixer.
A VP410 has the same A to V.

## Where each module sits

The [module and connector lay-out](../system/module-layout.md) page has the
manual's drawing beside a photograph of a real chassis with every board
labelled. In short:

- **Left-hand cage, front to back** — A, B, C, D
- **Front row, lying flat** — E, F, G, H, I
- **Right-hand cage, front to back** — J, K, L, M
- **Far right** — R and S, with T behind its perforated screen
- **Lying flat over the chassis at the back** — U, carrying the rear panel
- **On the deck** — Z
- **Behind the front panel** — N and Q
- **In the loader** — P
- **The sandwich, underneath** — W, X, Y
- **The backplane everything plugs into** — [V](v-module-carrier/index.md)

## Which modules have adjustments

Eleven of the twenty-six. The rest carry a PCB lay-out and a parts list only.

| Module | Adjustments |
| --- | --- |
| [A](a-audio-processor/index.md) | 1 — audio demodulator level |
| [B](b-rgb/index.md) | 7 — notch, bandpass, delay line, oscillator, luminance, colour difference, black level |
| [C](c-video-processor/index.md) | 2 — frequency, horizontal blanking |
| [F](f-motor-sequence/index.md) | 2 — sawtooth, current limiter |
| [G](g-genlock/index.md) | 1 — VCO |
| [H](h-etbc-b/index.md) | 5 — CCD delay and level, video amplitude, video and audio time errors |
| [I](i-etbc-c/index.md) | 1 — special burst separator |
| [K](k-hf-processor/index.md) | 2 — video amplitude, three filter dips |
| [L](l-video-dropout-correction/index.md) | 2 — 64 μs delay, MTF |
| [T](t-supply/index.md) | 1 — +5 V rail |
| [U](u-analog-io/index.md) | 7 — CVBS amplitudes, sub-carrier, chroma notch, burst, eye height, delay, beep |
| [X](x-lv-rom-decoder/index.md) | 1 — demodulator frequency |

[Deck electronics module Z](z-deck-electronics/index.md) carries six
potentiometers and **no procedure in the manual**; its page tabulates what each
one sets. The general rules — what to adjust after replacing a whole module,
and what equipment you need — are on
[general service → adjustments](../general-service/adjustments.md).

## A note on the parts lists

Every module page carries the list of electrical parts from its own sheet.
Where the vendor OCR of a sheet was reliable the list is its output, corrected
against the scan; where it was not — several sheets lost an item-number column,
and one lost the values — the rows were re-read off the 300 dpi scan, and the
page says so. **The scan on each page is the authority**: it is reproduced at
native resolution and zooms in the lightbox.

Components are numbered in the manual's four-number diagram coding — 2xxx
capacitors, 3xxx resistors, 5xxx coils and crystals, 6xxx diodes, 7xxx
transistors and ICs — except on [supply module T](t-supply/index.md), which
uses the board's own letter coding. See
[remarks, section 6](../general-service/remarks.md).

<figure class="sheet" markdown>
[![Chapter 4 divider: Survey of modules, modules A to Z — circuit diagram, PCB lay-out, adjustments, electrical parts — and remote control](assets/web/divider-p028-preview.webp)](assets/web/divider-p028-zoom.webp)
<figcaption>
  Chapter 4 divider.
  <span class="src">service manual page 028</span>
</figcaption>
</figure>
