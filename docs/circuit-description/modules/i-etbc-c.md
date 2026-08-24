---
title: Module I - ETBC C
description: >-
  Tangential error detection from the special burst, and the phase detector
  that drives the correction.
---

# Module I — ETBC C

*See also the [module I page](../../modules/i-etbc-c/index.md).*

This module is part of the electronic time base correction system (see block diagram overall timebase correction, fig.H1). Its primary function is to measure the timebase error and provide coarse (TANG-ER) and fine (BURST-ER) correction control signals to module H. To give the required accuracy, error measurement is made at two levels of precision.

The CV-TBM signal is coming from the ETBC-B module (H) and is the composite video signal for measuring the timebase error.

See Fig.I1 for the block diagram of this module.

Coarse measurement is obtained from comparison of syncs in CV-TBM and the RAMP-EN signal. The RAMP-EN signal is the reference timing signal from the REF SOURCE module (D). Fine error measurement is obtained from the special burst, a 3.75MHz signal during sync pulses. This inserted signal can only be found in the video signal from the disc.

## Circuit description

## Tangential error detector

For the circuit diagram of the tangential error detector, see Fig.I2.

CV-TBM applied to pin 9, IC 7203 (synchronization IC) is passed through an internal low pass filter and the syncs are separated. From these a line sync signal is obtained (HMANCH, pin 20 of IC 7203). From this signal a constant length pulse is obtained by one shot IC 7201-2A. In a similar way a pulse of the same duration is obtained from RAMP-EN (from module D). See the timing diagram in Fig. I3 (pulse width T1=33μs).

Comparison of the relative timing of these signals in 7202-2A, 7202-2B, gives a current in one of the collectors of 7004, 7005 which is proportional to the time error. See the timing diagram in Fig.I4 (pulse width T2=4.7μs), assuming that the disc video and hence the HMANCH signal derived from it has a longer timebase than the reference (also see fig. I3). This may e.g. occur when the disc turns too slowly.


In Fig.14 output pulses P1 and P2 are drawn with dotted lines because these signals are only present when clear input pins 3 and 13 resp. are "high" (C1 and C2). These inputs are not constantly high but dependent on the outputs of one shots IC 7201-2A and -2B. See Fig.15 for the actual timing.

The timing figures show that a positive pulse remains (P2). Via T7005 it will see to a discharge of C2015. As a result the dc level of the TANG-ER signal will rise via buffering by IC 72072B. In this way adaptation of the timebase correction takes place, in the sense that the throughput time of the video signal is reduced.

*FIG.11 ETBC C MODULE — see the sheet below.*

C2015 will be charged for too short a period time of the disc video relative to the reference. Charging will take place by the negative pulses (P1) and T7004. The dc-level of the TANG-ER signal will drop. As a result the throughput time of the video on module H will be lengthened.

## Special burst separator + gate

From CV-TBM the special burst is extracted by T7001, L5001, C2005, and is, via emitter follower T7002, available at the source of FET 7003. The special burst signal is gated by the syncs from pin 6, IC 7203 at T7003.

T7011, T7012 act as a 'special burst presence' detector, the collector of T7012 going high if a special burst is present.

The special burst is applied via T7029, T7014 to input 4, IC 7206-2A.

## Sample detector

The sample detector, see Fig.16, sees to delivery of a sample pulse signal which is an accurate measure for the frequency of the disc video. This is realized by looking to exactly the same zero crossing of the special burst signal each line time.

The special burst signal is tied to one shot IC 7206-2A, pin 4. Pin 6 of this IC will change over to a high level as soon as pins 4 and 5 are high and pin 3, reset input, is high too. The latter will be realized via one shot IC 7206-2B and T7015. The input signal of this IC is the comp. sync signal derived from the disc video. This comp.sync signal thus triggers one shot IC 7206-2B, which delivers in its turn a defined pulse at pin 10. Via T6215 this pulse sets one shot IC 7206-2A free. Dependent on the pulse time at pin 3, which is determined by C2042 and R3081, one shot IC 7206-2A will be reset (low level at pin 3). One shot IC 7206-2A will be active after release at pin 3 and will give a pulse at pins 6 and 7 at the next zero crossing of the special burst signal. T7016 ensures the selection of the correct zero crossing with respect to the line sync.

## Tangential phase detector

The RAMP-EN signal of REF SOURCE module D is tapped by means of resistors R3127 and R3128 and goes to the tangential phase detector circuit, see Fig.17. The RAMP-EN pulse goes to the base of T7027 which is incorporated in a one shot circuit, formed by T7027 and T7028. The output pulse of this one shot goes to the base of T7019 and will let this T7019 conduct at high level thus discharging C2052. The output signal of IC 7206-2A, pin 7, is via C2049 present on the collector of T7017 as sample pulse signal.

The sample pulse signal indicates exactly where a fixed zero crossing of the special burst signal is situated. The frequency of the sample pulse signal can be seen as an accurate measurement of the line frequency of the disc video signal. Via R3094 this pulse is present at the base of T7018 and will let this T7018 conduct in case of a low level. As a result C2052 will be charged via R3097. This causes a certain sawtooth signal on C2052. The total picture of charging and discharging can be seen in Fig.18.

This sawtooth signal goes via T7020, T7021 to the source of FET T7023. This FET T7023 sees to sampling out of the platform level in the sawtooth voltage. This voltage level will be present at C2053 then. When the zero crossing of the special burst takes place, T7023 is turned on loading a new voltage into C2053. The value across C2053 is proportional to the timebase error as measured from the special burst. Should the phase relation between the RAMP-EN signal and the sample pulse be disturbed, the result will be a level change of the platform in the sawtooth signal. Thus a dc-change at C2053 and thus, via opamp IC 7027-2A, a change in the BURST-ER signal.


It is important that timebase correction is disabled during the start-up sequence until motor lock (M-LOCK) and frame lock (FRLOCK) has been reached. D6018/6019,T7024/7025 are used to clamp TANG-ER to a mean value until this moment. This mean value is realized with the aid of R3118/3119/3120 and T7026.

IC 7203 also provides the CL-VID, HMANCH and VMANCH signals. These signals are necessary for decoding the manchester codes present in the video signal from the disc. CL-VID (clipped video) is only present during a few lines in the vertical blanking. The CL-VID signal is suppressed during most of the video lines by the DO-INH signal (drop-out inhibit from the genlock module G) via T7009 and T7010.

## The manual sheets

<figure class="sheet" markdown>
[![Module H - ETBC B (audio timebase correction) / Module I - ETBC C](../assets/web/cs-7-892-text-p146-preview.webp)](../assets/web/cs-7-892-text-p146-zoom.webp)
<figcaption>
  Module H - ETBC B (audio timebase correction) / Module I - ETBC C.
  <span class="cs">CS 7 892</span>
  <span class="src">service manual page 146</span>
</figcaption>
</figure>

<figure class="sheet sheet--fold" markdown>
[![Module I - ETBC C (continued)](../assets/web/cs-7-893-text-p147-preview.webp)](../assets/web/cs-7-893-text-p147-zoom.webp)
<figcaption>
  Module I - ETBC C (continued).
  <span class="cs">CS 7 893</span>
  <span class="src">service manual page 147</span>
</figcaption>
</figure>

<figure class="sheet sheet--fold" markdown>
[![Module I - ETBC C (tangential phase detector) / Module J - focus / Module K - HF processing](../assets/web/cs-7-894-text-p148-preview.webp)](../assets/web/cs-7-894-text-p148-zoom.webp)
<figcaption>
  Module I - ETBC C (tangential phase detector) / Module J - focus / Module K - HF processing.
  <span class="cs">CS 7 894</span>
  <span class="src">service manual page 148</span>
</figcaption>
</figure>
