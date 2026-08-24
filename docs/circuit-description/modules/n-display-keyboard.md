---
title: Module N - Display and keyboard
description: >-
  The front panel display and the keyboard scan.
---

# Module N — Display and keyboard

*See also the [module N page](../../modules/n-display-keyboard/index.md).*

The display and keyboard module is built around a 16 bit LED driver IC 7201, driving the indication LEDs and a buzzer. See the block diagram in Fig.N1. Two control buttons are fitted : STANDBY and EJECT.

## Circuit description

Input to IC 7201 takes place via the P-bus (SDAT, SCLT, DLEN) from control module S (IC 7211) as an 18 bit word, i.e. 0 + 16 data bits + terminating bit.

Outputs Q1 to Q10 are used to drive LEDs, Q11 provides an audio bleep via IC 7202 and transistor 7001.

If Q11 is "high", generator circuit IC 7202-4B, resistor 3012 and capacitor 2001 will be switched off via NAND IC 7202-4A. Pin 6 will remain "high" thus preventing transistor 7001 from starting to conduct. If Q11 is "low" and thus pin 3 of IC 7202-4A "high", IC 7202-4B will alternately give a high and a low level to output pin 6, dependent on the RC time (3012/2001).

The connections for the local switches are returned to the drive processor module (R).

## The manual sheet

<figure class="sheet" markdown>
[![Module M - radial drive / Module N - display and keyboard](../assets/web/cs-7-896-text-p150-preview.webp)](../assets/web/cs-7-896-text-p150-zoom.webp)
<figcaption>
  Module M - radial drive / Module N - display and keyboard.
  <span class="cs">CS 7 896</span>
  <span class="src">service manual page 150</span>
</figcaption>
</figure>
