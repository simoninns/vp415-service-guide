---
title: Block diagrams
description: >-
  The three system block diagrams: control routes, the audio/video signal path,
  and the servo loops.
---

# Block diagrams

Three fold-out sheets, one per subsystem. They are the fastest way to work out
which module a symptom implicates before you open a circuit diagram.

The prose that goes with them is in chapter 7 — see
[VP400 series architecture](../circuit-description/vp400-series.md), which
describes the same three diagrams as Fig. CR1, Fig. SP1 and Fig. SE1 and
explains what each block does.

## Control routes

Who commands what: the control module and drive processor, the S-bus and P-bus,
the front panel, the remote control and the external interfaces.

<figure class="sheet sheet--fold" markdown>
[![Block diagram of the control routes: the control and drive processor modules, the S-bus and P-bus, the display and keyboard, the RC5 receiver, and the RS232 and SCSI interfaces](assets/web/cs-7-833-figure-p024-preview.webp)](assets/web/cs-7-833-figure-p024-zoom.webp)
<figcaption>
  Block diagram — control routes.
  <span class="cs">CS 7 833</span>
  <span class="src">service manual page 024</span>
</figcaption>
</figure>

## Audio / video signal path

From the HF signal off the disc, through demodulation, drop-out correction and
timebase correction, to RGB decoding, the video mixer and the outputs.

<figure class="sheet sheet--fold" markdown>
[![Block diagram of the audio and video signal path: HF pre-amplifier, demodulation, drop-out correction, electronic timebase correction, video processing, RGB decoding, audio processing and the analog I/O outputs](assets/web/cs-7-834-figure-p025-preview.webp)](assets/web/cs-7-834-figure-p025-zoom.webp)
<figcaption>
  Block diagram — audio/video signal path.
  <span class="cs">CS 7 834</span>
  <span class="src">service manual page 025</span>
</figcaption>
</figure>

## Servo

The four loops that keep the spot on the track: focus, radial, tangential and
turntable-motor speed, plus the slide drive and tilt control.

<figure class="sheet sheet--fold" markdown>
[![Block diagram of the servo system: the focus, radial, tangential and motor loops, the slide drive and the active tilt control, with the error signals that drive each](assets/web/cs-7-835-figure-p026-preview.webp)](assets/web/cs-7-835-figure-p026-zoom.webp)
<figcaption>
  Block diagram — servo.
  <span class="cs">CS 7 835</span>
  <span class="src">service manual page 026</span>
</figcaption>
</figure>
