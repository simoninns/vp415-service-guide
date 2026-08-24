---
title: Module H - ETBC B
description: >-
  The CCD coarse and LC fine delay lines that correct the video and audio
  time base.
---

# Module H — ETBC B

*See also the [module H page](../../modules/h-etbc-b/index.md).*

This module is part of the electronic timebase correction system (see block diagram overall timebase correction, fig.H1).

It is comprised of two CCD (charge coupled devices) delay lines to effect coarse correction (+/- 17 micro secs) and two variable LC delay lines to effect fine correction (+/- 50 nano secs).

Video and audio signals are treated separately, in parallel. IC 7201 is the CCD for the video channel and IC 7203 the CCD for the audio channel (see fig.H2).

On this module the timebase of the drop-out corrected composite video (CV-DOC) is corrected. This is necessary because of the presence of several tolerances (disc, centring, motor) which cause variations on the line phase of the video signal read. The variations can be about +/- 17us compared with the reference. This is unacceptable for video processing, so correction is needed. In the previous players the correction was realised in a mechanical way, the tangential mirror. In the new-generation disc drives the tangential mirror is not applied anymore. The timebase is corrected electronically. The ETBC B module will have the timebase corrected comp. video signal (CV-TBC) as output signal for further processing on the vid proc module (C).

Also it is necessary to have timebase correction of the audio signal (HFAUD), which is realised too on this module. As result the output signal is the timebase corrected hf audio signal (HFATBC).

Control of the time delay is by means of TANG-ER and BURST-ER both from the ETBC C module (I).

## Circuit description

## Video timebase correction

The CV-DOC signal from the video do corr module (L) arrives at this module on plug 2H2 and goes, via emitter follower T7013 and a lowpass filter (≤6.6MHz), to the input of the CCD memory IC 7201. Lowpass filtering is necessary to prevent aliasing effects in the CCD. The video signal will get a time delay in the CCD depending on the frequency of the clock signal offered. The clock oscillator is connected to pin 14 of IC 7201 and functions as a voltage controlled oscillator (VCO), IC 7206. The voltage offered is the measured error signal (TANG-ER) created on the ETBC C module (I). The TANG-ER signal is present on plug 4H1 of this module. As the clock rate is determined by TANG-ER, so the time the signal is delayed in the CCD's is also determined by TANG-ER. This shows that as TANG-ER is a measure of the time error, a loop is set up which will compensate for timebase errors within the measuring accuracy of TANG-ER.

The frequency of the clock oscillator output signal is inversely proportional to TANG-ER and has a centre frequency of about 19MHz.

Referring to the anti aliasing phenomenon mentioned above it will be seen that low pass filtering of the input signal is required to eliminate any frequencies greater than half the clock rate.

In the CCD IC 7201 a flipflop is situated which acts as a :2 divider. The 2 output signals of this flipflop go to the 2 x 680 stages shift register, so the complete delay is 1360 stages for the video signal (see fig.H2). Reading by the CCD memory happens every positive going edge of the flipflop output signals Q and Q. For the timing of the internal flipflop, see Fig.H3.

*FIG.H1 BLOCK DIAGRAM - OVERALL TIMEBASE CORRECTION — see the sheet below.*

*FIG.H2 ETBC B MODULE — see the sheet below.*


The timebase corrected output signal of IC 7201 goes, via T7018, to T7020 to have a 3x amplification. The signal continues from the collector of T7020, via emitter follower T7021, to plug 7H1 as CV-TBM signal. For the system this signal is the measuring signal to create the error signals on the ETBC C module (I). On that module a comparison takes place of the measure signal and the reference signals. So this is the feedback loop of the timebase correction mechanism.

At the same time the signal of the emitter of T7018 goes, via T7017, to a steep lowpass filter (≤7MHz). This filter is realised by coils L5002...L5008 and the varicap diodes D6005...D6010. The filter circuit provides the video signal with a delay time of 200ns and depending on the voltage on the varicap diodes another +/- 50ns. This depends on the BURST-ER signal. Lowpass filtering is also necessary to prevent switching noise of the CCD.

In the video path there is some high frequency loss in the CCD. This is compensated for with a high pass network in the emitter of T7022 giving a rising response of about 6dB between 2 and 4MHz. From this network the video signal will be available on plug 2H1 as CV-TBC signal, via amplifier T7023 and emitter follower T7024.

The BURST-ER signal is present on plug 5H1 and goes, via potentiometer R3134, to the + input of opamp IC 7202-2A. From the output of this opamp the signal goes, via voltage follower IC7202-2B, to the varicap diodes of the variable LC delay line.

Dependent on the voltage offered the delay time will change, and this with a maximum of the above-mentioned +/- 50ns. The functioning of this circuit can be seen as a fine correction of the timebase errors.

## Audio timebase correction

The HF-AUD (high frequency audio) signal from the HF PROC module (K) arrives this module (H) on plug 1H2. The audio signal goes, just like the video signal, via a lowpass filter to a CCD memory IC (IC7203). The audio signal needs timebase correction too.

The clock drive for the shift register is driven by the clock signal coming from flipflop IC7204-2A. The input signal of the flipflop is realised by the same VCO as used for the video path.

The flipflop IC7204-2A is used as :2 divider. The clock frequency can be half the value because of the lower number of stages used (680 instead of 1360). The time delay will be the same as for video, but the passband of the audio signal is lower.

The output signal of CCD IC7203 goes, via emitter follower T7026, to a lowpass filter (≤2.3MHz) to filter the switching noise.

This LC filter functions also as variable delay line with the aid of the varicap diodes 6013. The varicap diodes are controlled by the BURST-ER signal. The output signal of IC7202-2A, derived from the BURST-ER signal, goes, via C2059, potentiometer R3122 and emitter follower T7029, to the varicap diodes. The controlled time delay differences will have the same value as for the video signal. Via amplifier stage T7030 and emitter follower T7031 the timebase corrected hf audio signal is available on plug 9H1 as HFATBC signal.

## The manual sheets

<figure class="sheet" markdown>
[![Module H - ETBC B](../assets/web/cs-7-891-text-p145-preview.webp)](../assets/web/cs-7-891-text-p145-zoom.webp)
<figcaption>
  Module H - ETBC B.
  <span class="cs">CS 7 891</span>
  <span class="src">service manual page 145</span>
</figcaption>
</figure>

<figure class="sheet" markdown>
[![Module H - ETBC B (audio timebase correction) / Module I - ETBC C](../assets/web/cs-7-892-text-p146-preview.webp)](../assets/web/cs-7-892-text-p146-zoom.webp)
<figcaption>
  Module H - ETBC B (audio timebase correction) / Module I - ETBC C.
  <span class="cs">CS 7 892</span>
  <span class="src">service manual page 146</span>
</figcaption>
</figure>
