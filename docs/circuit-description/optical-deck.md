---
title: The optical deck
description: >-
  What is on the deck, how the Laser Detection Unit works, and how Active Tilt
  Control keeps the LDU perpendicular to a bent disc.
---

# The optical deck

The deck reads the information from the video disc with a laser beam and turns
the modulated light into an electrical signal, which the player's electronics
then process.

The corresponding circuitry is
[module Z, deck electronics](../modules/z-deck-electronics/index.md); the
mechanical parts are itemised on the
[optical deck exploded view](../parts/exploded-views.md#optical-deck).

## What is on the deck

The deck consists of a main chassis carrying (Fig. OD1):

| Part | Function |
| --- | --- |
| Laser Detection Unit (LDU) | Reads the information from the video disc |
| Slide drive mechanism | Moves the LDU under the disc — [module E](../modules/e-slide-drive/index.md) |
| Turntable motor | Spins the disc — [module F](../modules/f-motor-sequence/index.md) |
| Tilt compartment | Gives the LDU an angular (and vertical) movement under the disc |
| Tilt mechanism | Drives the tilt compartment |
| Slide position indicator | Indicates the starting position of the slide — the `SPI` signal |
| Deck electronics | Processes the signals from the LDU and the tilt control — [module Z](../modules/z-deck-electronics/index.md) |

<figure class="sheet" markdown>
[![Fig. OD1, the optical deck: a labelled drawing of the deck chassis showing the Laser Detection Unit, slide drive mechanism, turntable motor, tilt compartment and mechanism, slide position indicator and the deck electronics board](assets/web/cs-7-878-figure-p129-preview.webp)](assets/web/cs-7-878-figure-p129-zoom.webp)
<figcaption>
  Fig. OD1 — optical deck.
  <span class="cs">CS 7 878</span>
  <span class="src">service manual page 129</span>
</figcaption>
</figure>

## The Laser Detection Unit

The LDU reads the information from the video disc and delivers electrical
signals for further processing. Its principle is drawn in Fig. OD2, and its
detailed construction in Fig. OD3.

!!! danger "The LDU is the laser"

    This is the part that emits. With the objective removed, the beam leaves the
    aperture directly — see [warnings](../general-service/warnings.md).

### The outgoing beam

1. A **solid state laser** emits a diverging beam. Power **3 mW**, wavelength
   **780 nm**, of the aluminium gallium arsenide (AlGaAs) type.
2. Just in front of the laser a **grating plate** splits the beam into a main
   beam and two auxiliary beams — the auxiliary beams are what
   [radial tracking](laservision-system.md#radial-tracking) uses.
3. The beam reflects partly off the surface of a **semi-transparent mirror**.
4. Still diverging, it passes through a **collimator lens** which makes it
   exactly parallel.
5. A **folding mirror** projects it onto the **radial mirror**, which is
   activated by the radial correction signal.
6. The **objective** focuses it on the surface of the video disc. The objective
   is driven vertically by the focus correction signal.

### The returning beam

The laser light reflected by the disc, carrying the disc information, returns by
the same path — objective, radial mirror, folding mirror, collimator lens — to
the semi-transparent mirror. There it is partly reflected back into the laser,
but enough passes through to be detected on the photodiodes.

The photodiodes are a **quadrant diode** plus **two auxiliary diodes, R1 and
R2**:

| Diodes | Deliver |
| --- | --- |
| Quadrant diode, segments A B C D | The HF signal and the focus error signal |
| R1 and R2 | The radial tracking signals |

<figure class="sheet" markdown>
[![The optical deck: what the deck consists of, and the Laser Detection Unit — with Fig. OD2 showing the beam path from the solid state laser through the grating, semi-transparent mirror, collimator, folding mirror, radial mirror and objective to the disc and back to the photodiodes, and Fig. OD3 showing the detailed construction of the LDU](assets/web/cs-7-879-text-p130-preview.webp)](assets/web/cs-7-879-text-p130-zoom.webp)
<figcaption>
  The optical deck. Figures OD2 and OD3.
  <span class="cs">CS 7 879</span>
  <span class="src">service manual page 130</span>
</figcaption>
</figure>

## Active Tilt Control (ATC)

### Why it exists

When a video disc is put on the turntable it bends under its own weight, into
an umbrella shape.

The LDU moves in a horizontal plane under the disc, so its distance to the disc
surface differs between the beginning of the disc and the outer side. At the
outer side the optical axis of the LDU is no longer perpendicular to the disc
surface. In that region the focused laser spot is distorted, causing **optical
cross-talk between the tracks**.

Active Tilt Control moves the LDU in an angular direction so that it is always
perpendicular to the disc surface, minimising the cross-talk. To do that, the
distance between LDU and disc has to be measured (Fig. OD4).

### How the distance is measured

An **infrared LED** is mounted on the LDU. The light it reflects off the disc
surface hits receiving diodes **D1 and D2** (Fig. OD5):

- **D1 = D2** — the position of the LED, and so of the LDU, relative to the disc
  is correct.
- **D1 ≠ D2** — a positive or negative error signal is generated, driving a DC
  **tilt motor** that corrects the position of the LDU until D1 equals D2 again.

The `TILTOK` signal reports the result, and a tilt loop that never settles is
what raises [error code 4, time-out tilt](../repair/error-codes.md#error-4).
The manual's fault-finding chart for that code sends you to the ATC circuit in
the optical deck.

<figure class="sheet" markdown>
[![Active Tilt Control: the principle, with Fig. OD4 showing a disc bending into an umbrella shape over the horizontally-moving LDU, and Fig. OD5 showing the infrared LED on the LDU with its reflected light falling on receiving diodes D1 and D2](assets/web/cs-7-880-text-p131-preview.webp)](assets/web/cs-7-880-text-p131-zoom.webp)
<figcaption>
  Active tilt control (ATC). Figures OD4 and OD5.
  <span class="cs">CS 7 880</span>
  <span class="src">service manual page 131</span>
</figcaption>
</figure>
