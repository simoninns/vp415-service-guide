---
title: Module K - HF processing
description: >-
  Processing of the hf signal from the LDU before it reaches the
  demodulators.
---

# Module K — HF processing

*See also the [module K page](../../modules/k-hf-processor/index.md).*

The h.f. signal of the disc will be splitted up into a video and an audio signal in this module. See block diagram in Fig.K1. The h.f. signal goes to the h.f. video processor section. After a highpass filter an adaptation of the frequency response will take place there by means of the MTF voltage. This is necessary dependent on the read-out diameter of the disc. The corrected h.f. video signal will be demodulated in IC 7201. After filtering and amplification output signal CV-DEM will be available for further processing at module L (drop-out correction).

The h.f. signal also goes to the h.f. audio processor where the audio is filtered out by means of a lowpass filter. Output signal HF-AUD will be timebase corrected at module H.

## Circuit description

The h.f. signal is first filtered by LC circuit 5003, 2014 and 2015. The h.f. signal will be used for the video part from the collector of transistor 7005. Therefore filtering is necessary by highpass filter (>2 MHz) 2004, 2005, 2006 and 5001. Via amplifier stage 7002, 7003 and 7004 the h.f. video signal is available on the collector of transistor 7004. In the collector circuit of 7002 an LC circuit is situated, tuned to a frequency of 8 MHz.

The LC circuit will be damped more or less depending on the value of the MTF signal. So the MTF signal will via transistor 7001 take care of adaptation of the frequency responses.

Demodulation of the h.f. video signal takes place in IC 7201-2A with an adjustable output amplitude with the aid of potentiometer 3043. At point 16 of IC 7201-2A the demodulated video is available which will give a composite video signal (CV-DEM) after lowpass filtering (<5MHz) and amplification by IC 7201-2B at point 6k2 of the module.

The h.f. audio signal will be obtained from the emitter of transistor 7005. This is realised with the amplifier stage in feedback mode, 7006, 7007 and 7008 and the lowpass filter (<2MHz) in the collector circuit of transistor 7006. This filter consists of 5004 and 2019, 2020 and 2021. The h.f. audio signal is available at point 1k1 of the module.

## The manual sheet

<figure class="sheet sheet--fold" markdown>
[![Module I - ETBC C (tangential phase detector) / Module J - focus / Module K - HF processing](../assets/web/cs-7-894-text-p148-preview.webp)](../assets/web/cs-7-894-text-p148-zoom.webp)
<figcaption>
  Module I - ETBC C (tangential phase detector) / Module J - focus / Module K - HF processing.
  <span class="cs">CS 7 894</span>
  <span class="src">service manual page 148</span>
</figcaption>
</figure>
