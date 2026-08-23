---
title: The LaserVision system
description: >-
  How information is stored on a LaserVision disc and read off it: pits,
  encoding, CAV and CLV, focusing, radial tracking, time base correction and
  genlock.
---

# The LaserVision system

Chapter 1 of the manual's circuit description: the physics and the format,
before any circuit. If you are trying to work out *why* the player does
something, this is where the answer usually is.

The figures — Fig. 1 to Fig. 9 — are drawings on the manual sheets, which are
reproduced in full at the foot of each section.

## Introduction

In the LaserVision system the video and audio information are stored on a disc
in encoded form. The information on the disc is scanned optically on a
LaserVision disc drive and then converted into a CVBS signal as well as RGB
signals suitable for a standard colour television receiver with Euroconnector.

The information is stored on the disc along a spiral track in the form of pits;
the disc is scanned from the centre to the outside. The length of the pits and
their spacing are determined by the stored information.

The pits are **0.4 μm wide and approximately 0.1 μm deep**. The track-to-track
spacing is **1.6 to 1.8 μm** (Fig. 1). The overall length of the track on a
30 cm disc is about **34 kilometres**.

The disc is made of a transparent plastic into which the pits are pressed. An
extremely thin reflective layer of aluminium is added on top, followed by a
protective coating that covers the whole. Two of these discs are glued together
to form a double-sided disc (Fig. 2).

A great advantage of the optical system is the contactless readout of the
information on the disc, as a result of which wear of disc and read-out device
is non-existent. A second advantage is the effective protection of the
information on the disc against dust, fingerprints and so on. Looking closely
at the beam path from the objective to the disc (Fig. 3), at the place where
the light cone enters the transparent base section the cone's diameter is still
fairly large. Dust particles at this place exert very little influence; the
light passes, as it were, around the dust particle. This highly effective
protection of the information enables normal handling of the disc.

### Optical read-out

The light beam from an AlGaAs semiconductor laser is focused on the disc by a
lens — the objective. In the absence of a pit practically the full amount of
light is reflected. The reflected light passes through the objective and is
then separated from the light beam going to the disc. The reflected light now
falls on a photodiode; the amount of current that starts flowing through the
diode is proportional to the amount of light falling on it.

When the light beam hits a pit, practically no light will be reflected — the
consequence of the properties of the laser light and the depth of the pit — so
the current passing through the photodiode is reduced.

In this way it is possible to convert the information on the disc into an
electrical signal suitable for further processing into a standard video signal
in the disc drive.

## Encoding of the signals on the disc

The video signal is frequency modulated on a carrier (Fig. 4a):

| Level | Frequency |
| --- | --- |
| Top sync | 6.76 MHz |
| Black | 7.1 MHz |
| White | 7.9 MHz |

giving a total frequency swing of 7.9 − 6.76 = **1.14 MHz**. Including its side
bands the video FM signal encompasses a frequency range down to approximately
2.5 MHz at the lower side.

The two audio signals are equally frequency modulated, on carriers of **683 kHz
and 1066 kHz**. The frequency swing of the two channels is **±100 kHz**
(Fig. 4b).

Summing these three signals and then limiting them results in a pulse-width
modulated signal (Fig. 4c). The negative half periods of this signal determine
the length of the pits; the positive half periods determine the spacing of the
pits (Fig. 4d). Fig. 5 shows the entire frequency spectrum with the associated
recording levels of the video and audio RF signals.

### CAV and CLV

The encoded RF signals may be stored on the disc in two different ways.

=== "CAV — constant angular velocity"

    The disc rotates at a constant speed, 1500 rpm = 25 rps. At each revolution
    a complete TV picture is reproduced, so the length of track corresponding to
    one picture gradually increases from the centre of the disc to the outside.
    **The frame sync pulses are situated on a diagonal.**

    Special playing modes — still picture, slow motion, fast forward and reverse
    — are feasible with this type of disc only, precisely because the frame sync
    pulses and therefore the frame blanking lie on a diagonal. That allows
    jumping from one track to the next or to the preceding one during the frame
    blanking period.

    Maximum playing time: **36 minutes per side**.

=== "CLV — constant linear velocity"

    The track length of each frame on the disc is constant, so the rotational
    speed decreases as the disc is scanned from the inside to the outside —
    from 1500 rpm at the inside to 565 rpm at the outside.

    No special playing modes can be realised with this type of disc, because the
    frame sync pulses and frame blanking are no longer on a diagonal, which
    puts jumping from one track to another out of the question.

    Maximum playing time: **54 minutes per side**.

The disc drive is suited for both types of disc.

!!! note "CLV playing time"

    Chapter 1 of this circuit description gives the maximum CLV playing time as
    54 minutes per side; the
    [technical data](../overview/technical-data.md) sheet gives 1 hour per side,
    and the CLV outer speed as 570 rpm against the 565 rpm here. Both figures
    are as printed in the manual.

<figure class="sheet" markdown>
[![The LaserVision system: introduction and encoding of the signals on the disc, with figures showing the pit geometry and track pitch, a cross section of the disc, the beam path through the transparent base, the FM carriers and pulse-width modulated signal, and the frequency spectrum](assets/web/cs-7-875-text-p126-preview.webp)](assets/web/cs-7-875-text-p126-zoom.webp)
<figcaption>
  The LaserVision system — introduction, encoding. Figures 1 to 5.
  <span class="cs">CS 7 875</span>
  <span class="src">service manual page 126</span>
</figcaption>
</figure>

## Codes in the frame blanking

In addition to the video and audio information, the disc contains a number of
special codes inserted in the frame blanking periods:

- **Test signals** on lines 19, 20, 332 and 333.
- **Digital codes** for various purposes on lines 16, 17, 18, 329, 330 and 331.

### Lead-in tracks

A minimum of **900 tracks** prior to the start of the actual programme contain a
start code which sends the read-out objective to the beginning of the programme
at **nine times** normal speed.

### Lead-out tracks

A minimum of **600 tracks** immediately after the end of the programme contain
an end code which sends the read-out objective back to the beginning at **75
times** normal speed. Video and audio signals are muted during the return
period.

### Programme area

=== "CAV discs"

    1. **Picture code** — a picture number by which each individual picture of a
       programme can be identified. It may be displayed on the monitor screen if
       desired. The picture number code is always present in the first field of
       each complete television frame; the second field may contain a **stop
       code** to switch the disc drive to STILL PICTURE mode.
    2. **Chapter code** — a chapter number by which a search action can be
       automatically stopped as soon as the start of the relevant chapter is
       reached. It may also be displayed if desired.

    The presence of stop code and chapter code is optional and depends on the
    programme content.

=== "CLV discs"

    1. A **normal play code** is always present. This code disables the special
       modes of operation of the disc drive.
    2. Instead of a picture number code, a **time code** is present, containing
       hour and minute indication showing the time elapsed since the start of
       the programme. It may be displayed if desired.

## Focusing

The objective used to read the information on the disc has a very small depth
of focus — **maximum 1.5 μm**. Given the tolerances in disc and disc drive
construction, this accuracy can only be realised by a servo control system that
continuously verifies and corrects the focusing of the objective.

For this purpose the objective is mounted in a magnet so as to allow vertical
motion. Around the objective, and firmly attached to it, a coil is mounted.
Feeding a current through the coil moves the objective more or less upwards,
depending on the current intensity (Fig. 6). The system is very much similar to
a loudspeaker.

### How the error signal is derived

The light reflected by the disc is focused on the photodiodes by the objective.
On its way to the diodes the reflected beam passes an **astigmatic lens
system** — a cylinder lens.

Unlike a spherical lens, an astigmatic lens does not have one single focal
point, but two focal lines at some distance from each other and at right angles
to each other. Between the focal lines is a plane where a circular picture is
formed. When the disc is out of focus with respect to the objective — too far
from or too close to it — the astigmatism modifies the shape of the picture
from circular to elliptical, and the direction of the ellipse's axes tells you
*which way* the error goes.

The photodiode that converts the light variations into an RF signal is composed
of **four quadrants A, B, C and D** (Fig. 7). When the objective is in focus,
all four quadrants receive equal amounts of light. When it is out of focus,
either A and B or C and D receive more light. The quadrants are interconnected
crosswise:

| Combination | Is |
| --- | --- |
| A + B + C + D | the RF signal |
| (A + B) − (C + D) | the drive signal for the objective |

That difference signal is `FOC-ER` in the
[signal listing](../system/signal-listing.md), and it is what
[module J](../modules/j-focus/index.md) closes the loop around.

<figure class="sheet" markdown>
[![CLV discs, lead-in and lead-out tracks, the programme area codes, and focusing — with figures showing the CLV track geometry, the objective in its magnet and coil, and the four-quadrant photodiode](assets/web/cs-7-876-text-p127-preview.webp)](assets/web/cs-7-876-text-p127-zoom.webp)
<figcaption>
  Lead-in / lead-out tracks, programme area, focusing. Figures 6 and 7.
  <span class="cs">CS 7 876</span>
  <span class="src">service manual page 127</span>
</figcaption>
</figure>

## Radial tracking

The information on the disc is contained in a spiral track read from the inside
to the outside, so the objective must also move from the centre of the disc to
the outside. The objective and all associated components of the optical system
are mounted on a **slide**, driven by a motor and moving radially under the
disc.

The light has to follow the track with an accuracy of approximately **0.1 μm**.
Tolerances in player and disc may cause a **track wobble of 130 μm** — the
slide cannot possibly follow that at 25 rps.

To obtain the required accuracy, a **movable mirror** is inserted in the light
path under the objective, allowing the light spot to be moved radially over the
disc. A magnet is attached to the mirror and a coil mounted around it; the
intensity and direction of the current through the coil determine how far the
mirror pivots left or right (Fig. 8).

### How the radial error signal is derived

Apart from the main beam for track scanning, the optical system forms **two
auxiliary light beams** whose impact is slightly displaced with respect to the
track's centre line, in opposite directions.

The light spots formed on the disc by the two auxiliary beams fall partly on
the track and partly outside its left or right edge. The objective focuses
these spots onto two separate photodiodes at either side of the signal diodes —
**E and F** in Fig. 7. When the track is followed correctly, the signals from
each diode are equal; when tracking is less than optimal, which diode output
exceeds the other depends on the direction of the deviation (Fig. 9).

The difference between the two signals is, after amplification, used to drive
the mirror. **When the average voltage across the mirror coil is positive or
negative, the slide motor is controlled until the average voltage is zero
again** — that is how the slow slide and the fast mirror share the work.

## Time base correction

A TV picture consists of lines written in an accurately laid down time —
64 μs for PAL. Deviations from this cause a distorted picture and phase errors
in the colour signal, which may lead to the colour dropping out. The video
signal of the disc drive must meet the same requirement.

Tolerances in disc, centring and motor result in variations in the line time.
The **maximum permissible deviation to give a stable picture with every TV
receiver is 5 ns**, and the correction is done in three stages:

1. **Motor speed.** The phase of the line sync pulses is compared with the phase
   of line-frequency pulses from a crystal oscillator, and the resulting control
   voltage drives the turntable motor. This cannot correct variations at 25 Hz
   and above.
2. **Coarse: a CCD** — a charge coupled device acting as a variable delay line,
   correcting the large time errors, **±17 μs**.
3. **Fine: a variable LC delay line**, **±50 ns**.

The CCD is driven by a signal obtained by comparing the phase of a
crystal-controlled reference with the line-frequency pulses of the disc video
signal.

The line sync pulses themselves are not suited to a measurement of this
accuracy, so use is made of a **3.75 MHz signal — 240 × the line frequency —
laid down on the disc at the level of the peak sync pulses**. If the same zero
crossing of the 3.75 MHz signal is used for every line sync pulse, the actual
line time can be measured accurately enough.

Time base correction is what makes it possible to connect the disc drive to any
TV set. In the player it is done by
[module H (ETBC B)](../modules/h-etbc-b/index.md) and
[module I (ETBC C)](../modules/i-etbc-c/index.md).

## Genlock

Genlock synchronises the video signal of the disc drive with the video signal of
another source — that is, the line and frame pulses of both signals are in
phase (sync lock). This is necessary to enable interference-free switching
between the two video signals. **Locking is done by controlling the revolution
speed of the disc**, and hence the phase of the line and frame pulses. See
[module G](../modules/g-genlock/index.md).

<figure class="sheet" markdown>
[![Radial tracking, time base correction and genlock — with figures showing the pivoting mirror in its coil and magnet, and the auxiliary beam spots straddling the track with their photodiode outputs](assets/web/cs-7-877-text-p128-preview.webp)](assets/web/cs-7-877-text-p128-zoom.webp)
<figcaption>
  Radial tracking, time base correction, genlock. Figures 8 and 9.
  <span class="cs">CS 7 877</span>
  <span class="src">service manual page 128</span>
</figcaption>
</figure>
