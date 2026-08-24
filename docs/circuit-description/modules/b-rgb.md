---
title: Module B - RGB
description: >-
  CVBS split into luminance and chrominance, PAL decoded to R, G and B, with
  the colour transient improver.
---

# Module B — RGB

*See also the [module B page](../../modules/b-rgb/index.md).*

See the block diagram in Fig.B1. The drop-out – and time-base corrected video, obtained from the VIDEO PROCESSING MODULE (C), is the input signal (CVBS) of this module. The CVBS signal will be split into a luminance and a chrominance signal and decoded into the R, G and B signals which are fed to the VIDEO MIXER MODULE (Y), via the ANALOG I/O MODULE (Ua). At the same time the luminance signal Y and the colour difference signals R–Y and B–Y are made available for creating the encoded CVBS signal on the ANALOG I/O MODULE (Ub).

## Circuit description

First the incoming CVBS signal (plug 1B1) will be split into a luminance and a chrominance signal. By filtering the CVBS signal on the emitter of T7001, the luminance signal Y is present on the emitter of T7002 with an amplitude adjustable by potentiometer R3080. Via bandpass filtering with L5004 + C2005 the chrominance signal is present on pin 15 of IC7201.

## Chroma decoding

The chroma signal will be decoded by IC7201, multistandard decoder, in an R–Y and a B–Y signal. The IC needs a crystal oscillator with a frequency of 8.86MHz (Cristal 5005) for chroma subcarrier generation. Capacitor C2010 is made switchable with T7012, driven by the CV/CS signal. The capacitor is connected to the +12V via the diode and resistor so that the AGC voltage remains at a fixed level if T7012 is out of conduction. The CV/CS signal will be low if the comp.sync signal is chosen instead of the video signal (mute function). In that case there will be no video content in the CVBS signal. The input signal, comp.sync, has no burst so the gain control in IC7201 will give more amplification and can cause some problems. Therefore the AGC voltage will be kept of a high level.

## Colour transient improver

The colour difference signals R–Y and B–Y are present at pin 1 and pin 2 of IC7202 resp. This IC functions as colour transient improver. This means that the slope of the colour signal will be improved, thus giving a better visual impression.

The amplitudes of the (R–Y) and (B–Y) signals can be adjusted by potentiometers R3082 and R3084. The improved (R–Y) and (B–Y) signals are the output signals on pins 8 and 7 of IC7202.

Because of the processing time required to improve the colour transient, some time delay will occur in these output signals. The Y signal must have the same delay, which will be realised in IC7202. The output signals of IC7202 the luminance signal Y and the colour difference signals (R–Y) and (B–Y), will go to the ANALOG I/O MODULE Ub via plugs 10B3, 9B2 and 10B2 resp.

## PAL decoder

At the same time the luminance and chrominance signals are going to IC7203, which takes care of decoding of these signals. The signals R, G and B go from pins 1, 3 and 5 of this IC7203, via output stages T7006, T7008 and T7010 to plugs 2B3, 3B3 and 4B3.

The dc-level of the output signals is adjustable by potentiometer R3045. The black level of the video signal is the reference point.

## The manual sheet

<figure class="sheet" markdown>
[![Module B - RGB](../assets/web/cs-7-886-text-p140-preview.webp)](../assets/web/cs-7-886-text-p140-zoom.webp)
<figcaption>
  Module B - RGB.
  <span class="cs">CS 7 886</span>
  <span class="src">service manual page 140</span>
</figcaption>
</figure>
