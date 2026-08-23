---
title: Module and connector lay-out
description: >-
  Where every module sits in the player, and where its connectors are — the
  manual's lay-out drawing beside an annotated photograph of a real chassis.
---

# Module and connector lay-out

The map of the machine. The manual's drawing gives the position of every module
and every connector on the module carrier, the deck and the front loader; the
photograph beside it is the same layout in a real player, so you can match the
two before you pull a board.

## In a real player

<figure class="sheet sheet--photo sheet--fold" markdown>
[![Overhead photograph of an opened VP415 with each module labelled: A audio processor, B RGB, C video processor, D reference source, E slide drive, F motor and sequence, G genlock, H ETBC B, I ETBC C, J focus, K HF processor, L video drop-out, M radial, R drive processor, S control, T supply, U analog I/O and Z deck electronics](assets/web/module-layout-annotated-preview.webp)](assets/web/module-layout-annotated-zoom.webp)
<figcaption>
  A VP415 with the upper case and front loader removed, seen from above, each
  plug-in module labelled. The optical deck is in the centre; the supply is the
  perforated screen at the right.
</figcaption>
</figure>

Reading the photograph:

- **Left-hand cage, front to back:** [A audio processor](../modules/a-audio-processor/index.md),
  [B RGB](../modules/b-rgb/index.md),
  [C video processor](../modules/c-video-processor/index.md),
  [D reference source](../modules/d-reference-source/index.md).
- **Front row, lying flat:** [E slide drive](../modules/e-slide-drive/index.md),
  [F motor + sequence](../modules/f-motor-sequence/index.md),
  [G genlock](../modules/g-genlock/index.md),
  [H ETBC B](../modules/h-etbc-b/index.md),
  [I ETBC C](../modules/i-etbc-c/index.md).
- **Right-hand cage, front to back:** [J focus](../modules/j-focus/index.md),
  [K HF processor](../modules/k-hf-processor/index.md),
  [L video drop-out correction](../modules/l-video-dropout-correction/index.md),
  [M radial](../modules/m-radial/index.md).
- **Far right, the two large boards:**
  [R drive processor](../modules/r-drive-processor/index.md) and
  [S control](../modules/s-control/index.md), with
  [T supply](../modules/t-supply/index.md) behind its perforated screen.
- **Top left, lying flat over the chassis:**
  [U analog I/O](../modules/u-analog-io/index.md), which carries the rear panel.
- **On the deck itself:** [Z deck electronics](../modules/z-deck-electronics/index.md),
  under the yellow laser warning label.

Not visible from above: [N display + keyboard](../modules/n-display-keyboard/index.md)
and [Q RC5 receiver](../modules/q-rc5-receiver/index.md) behind the front
panel, [P frontloader](../modules/p-frontloader/index.md) in the loader
assembly, [V module carrier](../modules/v-module-carrier/index.md) — the
backplane the cages plug into — and the sandwich boards
([W](../modules/w-cpu-data-grabber/index.md),
[X](../modules/x-lv-rom-decoder/index.md),
[Y](../modules/y-video-mixer/index.md)) which sit in a second cage beneath.

## The manual's lay-out drawing

The drawing is in three parts: the player itself at the left, the optical deck
at the top right, and the front loader at the far right. Every connector is
drawn where it physically is, with its designation — `A1`, `B2`, `Z4` — and its
pin count and pin-1 end marked. When a circuit diagram says a signal leaves on
`6B2`, this drawing is where you find pin 6 of connector B2.

The connector designations follow the module letter: module A has `A1` and
`A2`, module B has `B1` to `B3`, and so on. Deck connectors are `Z0` to `Z6`,
and the front loader has `P1` and `P2`.

<figure class="sheet sheet--fold" markdown>
[![Module and connector lay-out: a plan drawing of the player showing every module in position with its connectors and pin numbering, plus separate drawings of the optical deck and the front loader](assets/web/cs-7-829-figure-p019-preview.webp)](assets/web/cs-7-829-figure-p019-zoom.webp)
<figcaption>
  Module and connector lay-out.
  <span class="cs">CS 7 829</span>
  <span class="src">service manual page 019</span>
</figcaption>
</figure>

What runs between those connectors is on the
[wiring diagrams](wiring-diagrams.md) page.
