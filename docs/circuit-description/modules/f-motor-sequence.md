---
title: Module F - Motor + sequence
description: >-
  The brushless turntable motor: start condition, frequency control, phase
  control and active braking.
---

# Module F — Motor + sequence

*See also the [module F page](../../modules/f-motor-sequence/index.md).*

The circuits in this module take care of the drive of the turntable motor. See servo block diagram and block diagram in Fig.F1.

The turntable motor is of the brushless type provided with Hall elements. The main groups on the board are:

-The MDS-IC 7202. This IC takes care of the communication between the motor and other circuits and delivers the required drive voltages to the output amplifiers of the motor.

-The Hall elements which are continuously passing the position of the motor via comparators to the MDS-IC.

-The logic circuits around transistors 7020-7022 which are controlling the motor with regard to the several conditions like start, brake, motor control and current limiting.

-The pulsewidth modulator IC 7230 which is converting the drive voltages into a duty cycle controlled input pulse for the MDS-IC

-The output stages which are supplying the required drive currents to the motor coils. This currents are derived from the commutating voltages supplied by the MDS-IC.

## Circuit description

For a proper functioning of the turntable motor, several input signals are required:

-TTM, the turntable motor on signal which is "H" during start and play conditions and delivered by the drive processor.

-MCO, a duty cycle controlled pulse which is originating from the GenLock Module and only active in the locked position.

-CLV-TC, a logic "H" signal, present during track crossing at CLV discs.

-MEM-SU, Memory start up, a logic "H" signal in case of focus loss on CLV disc in search mode. The last tacho information is then stored in a memory.

## Start condition

In start condition the TTM signal is "H" and is via the buffer amplifiers 7001-7002 fed to the MDS-IC. As long as the motorspeed is below 1500 RPM, the output signal TSP of the tacho circuit in the MDS-IC is "L" which causes switch 7201-4C to be open. The TSP signal is also fed to the sequence circuit and causes that 7021 is blocked. The collector voltage is then "H" and switch 7201-4C is closed. The "H" voltage from TTM is fed via 7201-4C to pulse-width modulator 7230-2A. This results in a low duty cycle and causes speeding up of the motor. The charge current of 2031 is limited by the diodes 6001-6002. The pulse-width modulator 7230-2A compares the control voltage with a sawtooth signal derived from the clock circuit in IC 7202. The frequency is about 17.6 kHz. The sawtooth shaped voltage is obtained by the generator consisting of transistor 7023, capacitor 2030 and the resistors 3029-3031. It will be clear, that the duty cycle decreases when the d.c. control voltage increases.

*Fig.F1 MOTOR+SEQUENCE MODULE — see the sheet below.*


## Running condition

As soon as the motor is running, 12 p/rev. pulses are applied from 30IC-7202 to the base of transistor 7050. This causes the input voltage on 5-IC7230 to increase from about 2.7V up to 3.2V. After the opamp and the diodes 6061-6066 a small part of the output voltage is fed to switch 7201-4D. As soon as 1500 RPM is reached, the TSP-signal becomes "H" and switch 7201-4D will close. At the same time transistor 7021 starts conducting and switch 7201-4C will open. This means a lower input voltage at the pulse width modulator and the motor will not accelerate anymore.

## Frequency control

When the motor has reached a speed of 1500 RPM and TSP is "H", switch 7201-4B is closed via resistor 3021 and diode 6022. Now the motor control will take place with the aid of the LWPM signal and the phase compensation network IC 7260-2B. The output will be combined with the running current limiter signal.

## Phase control

In running condition TSP has become "H", capacitor 2020 is charged and after about 0.5 sec transistor 7020 starts conducting and the collector voltage will drop. Switch 7201-4B opens and there is no frequency control anymore. At the same time transistor 7022 is blocked and due to the high collector voltage, switch 7201-4A is closed. From this moment on MCO-EN becomes also "H" and the motor control is taken over by the MCO-signal.

In case of CLV-track crossing, which occurs in CLV-search mode, the CLV-TC-signal becomes "H", which means that there is only frequency control by the LPWM-signal.

## Active braking

When TTM becomes "L", TSP is "L" too. Switch 7201-4A will open and 7201-4C will close. A lower voltage is now given to the pulsewidth modulator input. Upon motor stop, all driver inputs are disabled.

## The manual sheets

<figure class="sheet sheet--fold" markdown>
[![Module D - output signals / Module E - slide drive / Module F - start condition](../assets/web/cs-7-889-text-p143-preview.webp)](../assets/web/cs-7-889-text-p143-zoom.webp)
<figcaption>
  Module D - output signals / Module E - slide drive / Module F - start condition.
  <span class="cs">CS 7 889</span>
  <span class="src">service manual page 143</span>
</figcaption>
</figure>

<figure class="sheet sheet--fold" markdown>
[![Module F - motor + sequence (running condition / frequency / phase control) / Module G - genlock](../assets/web/cs-7-890-text-p144-preview.webp)](../assets/web/cs-7-890-text-p144-zoom.webp)
<figcaption>
  Module F - motor + sequence (running condition / frequency / phase control) / Module G - genlock.
  <span class="cs">CS 7 890</span>
  <span class="src">service manual page 144</span>
</figcaption>
</figure>
