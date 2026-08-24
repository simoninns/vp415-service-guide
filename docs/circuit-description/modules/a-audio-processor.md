---
title: Module A - Audio processor
description: >-
  The hf audio split into its two sub-carriers, demodulated, drop-out
  corrected and switched.
---

# Module A — Audio processor

*See also the [module A page](../../modules/a-audio-processor/index.md).*

On this module the hf audio signal (time base corrected) will be split up and demodulated into the 2 possible If audio signals. See block diagram in Fig.A1. Drop out correction takes place for both channels. On/off switching of one or both of the audio signals is possible on this module. The hf audio signal, time base corrected, (HFATBC) comes from the ETBC B module (H). This signal is fed through 2 identical circuits for both audio channels. Only some values of the applied components differ because of the different subcarrier frequencies (audio-1:683kHz, audio-2:1066kHz). Only the circuit for audio 1 will be discussed.

## Circuit description

The HFATBC signal(plug 1A2) goes, via bandpass filter L5007, to the demodulator IC6201-2A and is available, as demodulated audio, at the output, pin 16, of IC6201-2A. The audio signal goes, via a lowpass filter (50kHz) and emitter follower T6101, to the source of FET 6102. Normally this FET is conducting, so the audio signal goes, via amplifier circuit T6103, T6104 and T6105, to pin 9 of switch IC6201-2B. If audio 1 is wanted as output signal, pins 9 and 8 will be "connected" and the If audio 1 signal is available at plug 3A1 (AUD1) which will lead to the analog I/O module (U).

## Drop-out correction

If a drop-out occurs in the hf audio signal FET 6102 will be switched off by a drop-out pulse on the gate of this FET. The voltage level on C2003 will be used as audio signal during that drop-out, thus avoiding "plops" (track and hold principle).

Drop-out detection takes place by monitoring the hf components remaining in the demodulated audio signal on output pin 16 of IC6201-2A. That signal will be fed through a bandpass filter (200kHz), realised with the RC components around T6115.

Detection is done with T6116, T6117 and T6118 and will create positive pulses in the case of drop-outs on the collector of T6118. The pulses are inverted by T6123 and will then drive the gate of FET 6102. If a drop-out is measured in the audio 1 channel, the track and hold circuit in the audio 2 channel is driven too.

## Switching

Selection of the required audio channel is made with AUD-1ON and AUD2ON. When only one channel is selected, both outputs are fed with that channel by means of cross coupling 2007, 3017 and 2021, 3041.

*FIG.A1 AUDIO PROC. MODULE — see the sheet below.*

## The manual sheet

<figure class="sheet" markdown>
[![Module A - audio processor](../assets/web/cs-7-885-text-p139-preview.webp)](../assets/web/cs-7-885-text-p139-zoom.webp)
<figcaption>
  Module A - audio processor.
  <span class="cs">CS 7 885</span>
  <span class="src">service manual page 139</span>
</figcaption>
</figure>
