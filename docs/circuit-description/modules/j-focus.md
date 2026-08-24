---
title: Module J - Focus
description: >-
  The focus servo drive.
---

# Module J — Focus

*See also the [module J page](../../modules/j-focus/index.md).*

The function of the focus module is to move the objective in starting condition up to such a position that the laser beam is focussed on the disc and to keep the spot focussed under all play conditions.

## Circuit description

The block diagram of the focus circuit is shown in fig.J1. The objective is driven by amplifier transistors 6208-6211, which supply a positive or negative voltage FOCACT. Negative means that the objective is driven upwards to the disc and positive means that the objective is pulled downwards. The range of the objective movement is approximately 5mm.

When the player is started up (motor not yet turning), the focus enable signal FOC-EN is low and the focus position indication signal FPI from the deck electronics is high, resulting in 0 V on the objective (see timing diagram Fig. J2). As soon as the driving module detects a disc reflection (DR), a correct slide position SPI and a laser on LA-STIA the FOC-EN will go high. When FPI is still high, the drive voltage for the objective becomes negative causing the objective to go upwards. This movement is slowed down because of the feedback through filters 2006, 2007, 3015, 3016, 3017. Switch 6205 is still open, which means that there is maximum gain (low negative feedback).

When the objective focusses the laser beam onto the disc, the FPI signal will go low, causing the focus loop switch (transistor 6206) to close and after that the focus indication signal FOC-IND to go low. FOC-EN remains high. At the same time switch 6205 will be closed, which causes more negative feedback and as a consequence less gain. The FOC-IND low signal is applied to the drive module as a command that the turntable can be started. The objective is then driven by the focus error signal FOC-ER and is kept in focus by a negative voltage of average -1V on amplifier output 6208-6211.

When focus is found, the FPI will stay high and the drive module switches the FOC-EN to low after 0.5 sec. The drive voltage becomes 0V and the objective will move downwards. After 0.2 sec the FOC-EN will become high again and will move the objective upwards. This sequence is repeated 5 times. If no focus is found, the player is switched to stand by.

If there is a minor disturbance in the reflection, FPI and consequently also FOC-IND will become high for a short moment.

The positive pulse on FPI causes a negative drive voltage on the objective and without protection the objective should move upwards. The function of one shot transistors 6214-6215 is to prevent this. The positive FPI pulse triggers the one shot and keeps via collector of 6214 the FOC-EN signal low and via 6217/6010 the drive voltage at 0V during 40 ms. During this time the objective will not move.

The FOC-ER signal is fed through a low pass filter with transistor 6201 to an AC/DC converter with transistor 6204 and diode 6001. The DC voltage drives the gain switch in the feedback circuit of the output stage. As soon as the FOC-ER signal increases up to a certain AC level, the AC/DC converter switches the gain switch to high gain of the objective drive. The increasing error current through the objective then causes an audible noise in the LDU. When a low FOC-ER signal occurs, the circuit switches to low gain, resulting in a smooth objective drive.

## The manual sheet

<figure class="sheet sheet--fold" markdown>
[![Module I - ETBC C (tangential phase detector) / Module J - focus / Module K - HF processing](../assets/web/cs-7-894-text-p148-preview.webp)](../assets/web/cs-7-894-text-p148-zoom.webp)
<figcaption>
  Module I - ETBC C (tangential phase detector) / Module J - focus / Module K - HF processing.
  <span class="cs">CS 7 894</span>
  <span class="src">service manual page 148</span>
</figcaption>
</figure>
