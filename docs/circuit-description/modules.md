---
title: Module circuit descriptions
description: >-
  Chapter 3 of the manual's circuit description: how each of the twenty-five
  modules works, module A through module Z.
---

# Module circuit descriptions

Chapter 3 of the manual's circuit description, in full: what each module does
and how its circuit does it, module by module. It is the text that the
[module pages](../modules/index.md) draw on.

The block diagrams the text refers to — Fig. A1, Fig. B1 and so on — are
printed on the manual sheets, which are reproduced after each description.

| | | | | |
| --- | --- | --- | --- | --- |
| [A](#module-a) audio processor | [B](#module-b) RGB | [C](#module-c) video processing | [D](#module-d) reference source | [E](#module-e) slide drive |
| [F](#module-f) motor + sequence | [G](#module-g) genlock | [H](#module-h) ETBC B | [I](#module-i) ETBC C | [J](#module-j) focus |
| [K](#module-k) HF processing | [L](#module-l) video drop-out | [M](#module-m) radial drive | [N](#module-n) display + keyboard | [P](#module-p) frontloader |
| [R](#module-r) drive processor | [S](#module-s) control | [T](#module-t) supply | [Ua](#module-ua) CVBS + audio | [Ub](#module-ub) video |
| [Uc](#module-uc) TXT | [W](#module-w) data grabber + CPU | [X](#module-x) LV-ROM decoder | [Y](#module-y) video mixing | [Z](#module-z) deck electronics |

!!! note "Modules the manual does not describe here"

    Chapter 7 has no circuit description for **Q (RC5 receiver)** or **V (module
    carrier)**, and none for the remote control handset. Those modules have
    circuit diagrams and parts lists in chapter 4 but no prose. The manual's own
    contents page lists 25 descriptions, and 25 is what follows.

    Module **T (supply)** is described here even though the contents page places
    it between S and Ua — the sheet carries both.

warning: Git tree '/home/sdi/Coding/vp415-service-guide' is dirty
## Module A — Audio processor { #module-a }

*See also the [module A page](../modules/a-audio-processor/index.md).*

On this module the hf audio signal (time base corrected) will be split up and demodulated into the 2 possible If audio signals. See block diagram in Fig.A1. Drop out correction takes place for both channels. On/off switching of one or both of the audio signals is possible on this module. The hf audio signal, time base corrected, (HFATBC) comes from the ETBC B module (H). This signal is fed through 2 identical circuits for both audio channels. Only some values of the applied components differ because of the different subcarrier frequencies (audio-1:683kHz, audio-2:1066kHz). Only the circuit for audio 1 will be discussed.

### Circuit description

The HFATBC signal(plug 1A2) goes, via bandpass filter L5007, to the demodulator IC6201-2A and is available, as demodulated audio, at the output, pin 16, of IC6201-2A. The audio signal goes, via a lowpass filter (50kHz) and emitter follower T6101, to the source of FET 6102. Normally this FET is conducting, so the audio signal goes, via amplifier circuit T6103, T6104 and T6105, to pin 9 of switch IC6201-2B. If audio 1 is wanted as output signal, pins 9 and 8 will be "connected" and the If audio 1 signal is available at plug 3A1 (AUD1) which will lead to the analog I/O module (U).

### Drop-out correction

If a drop-out occurs in the hf audio signal FET 6102 will be switched off by a drop-out pulse on the gate of this FET. The voltage level on C2003 will be used as audio signal during that drop-out, thus avoiding "plops" (track and hold principle).

Drop-out detection takes place by monitoring the hf components remaining in the demodulated audio signal on output pin 16 of IC6201-2A. That signal will be fed through a bandpass filter (200kHz), realised with the RC components around T6115.

Detection is done with T6116, T6117 and T6118 and will create positive pulses in the case of drop-outs on the collector of T6118. The pulses are inverted by T6123 and will then drive the gate of FET 6102. If a drop-out is measured in the audio 1 channel, the track and hold circuit in the audio 2 channel is driven too.

### Switching

Selection of the required audio channel is made with AUD-1ON and AUD2ON. When only one channel is selected, both outputs are fed with that channel by means of cross coupling 2007, 3017 and 2021, 3041.

*FIG.A1 AUDIO PROC. MODULE — see the sheet below.*

<figure class="sheet" markdown>
[![Module A - audio processor](assets/web/cs-7-885-text-p139-preview.webp)](assets/web/cs-7-885-text-p139-zoom.webp)
<figcaption>
  Module A - audio processor.
  <span class="cs">CS 7 885</span>
  <span class="src">service manual page 139</span>
</figcaption>
</figure>

## Module B — RGB { #module-b }

*See also the [module B page](../modules/b-rgb/index.md).*

See the block diagram in Fig.B1. The drop-out – and time-base corrected video, obtained from the VIDEO PROCESSING MODULE (C), is the input signal (CVBS) of this module. The CVBS signal will be split into a luminance and a chrominance signal and decoded into the R, G and B signals which are fed to the VIDEO MIXER MODULE (Y), via the ANALOG I/O MODULE (Ua). At the same time the luminance signal Y and the colour difference signals R–Y and B–Y are made available for creating the encoded CVBS signal on the ANALOG I/O MODULE (Ub).

### Circuit description

First the incoming CVBS signal (plug 1B1) will be split into a luminance and a chrominance signal. By filtering the CVBS signal on the emitter of T7001, the luminance signal Y is present on the emitter of T7002 with an amplitude adjustable by potentiometer R3080. Via bandpass filtering with L5004 + C2005 the chrominance signal is present on pin 15 of IC7201.

### Chroma decoding

The chroma signal will be decoded by IC7201, multistandard decoder, in an R–Y and a B–Y signal. The IC needs a crystal oscillator with a frequency of 8.86MHz (Cristal 5005) for chroma subcarrier generation. Capacitor C2010 is made switchable with T7012, driven by the CV/CS signal. The capacitor is connected to the +12V via the diode and resistor so that the AGC voltage remains at a fixed level if T7012 is out of conduction. The CV/CS signal will be low if the comp.sync signal is chosen instead of the video signal (mute function). In that case there will be no video content in the CVBS signal. The input signal, comp.sync, has no burst so the gain control in IC7201 will give more amplification and can cause some problems. Therefore the AGC voltage will be kept of a high level.

### Colour transient improver

The colour difference signals R–Y and B–Y are present at pin 1 and pin 2 of IC7202 resp. This IC functions as colour transient improver. This means that the slope of the colour signal will be improved, thus giving a better visual impression.

The amplitudes of the (R–Y) and (B–Y) signals can be adjusted by potentiometers R3082 and R3084. The improved (R–Y) and (B–Y) signals are the output signals on pins 8 and 7 of IC7202.

Because of the processing time required to improve the colour transient, some time delay will occur in these output signals. The Y signal must have the same delay, which will be realised in IC7202. The output signals of IC7202 the luminance signal Y and the colour difference signals (R–Y) and (B–Y), will go to the ANALOG I/O MODULE Ub via plugs 10B3, 9B2 and 10B2 resp.

### PAL decoder

At the same time the luminance and chrominance signals are going to IC7203, which takes care of decoding of these signals. The signals R, G and B go from pins 1, 3 and 5 of this IC7203, via output stages T7006, T7008 and T7010 to plugs 2B3, 3B3 and 4B3.

The dc-level of the output signals is adjustable by potentiometer R3045. The black level of the video signal is the reference point.

<figure class="sheet" markdown>
[![Module B - RGB](assets/web/cs-7-886-text-p140-preview.webp)](assets/web/cs-7-886-text-p140-zoom.webp)
<figcaption>
  Module B - RGB.
  <span class="cs">CS 7 886</span>
  <span class="src">service manual page 140</span>
</figcaption>
</figure>

## Module C — Video processing { #module-c }

*See also the [module C page](../modules/c-video-processor/index.md).*

See block diagram in Fig.C1. On the video processing module switching is made possible between internal video (CV–TBC), external video (CV–EXT) and composite sync depending on the demands. Composite sync can only be used in the case of internal video selection (video from the disc). Composite sync is necessary if the player is in "pause" or during "goto" actions. The index frame and index characters can be inserted in the video signal, if wanted. Sandcastle pulse generation takes place for RGB handling and clamp pulses are created for black–level clamping. Clamping of the video is necessary to enable insertion of the index information.

### Circuit description

### Switching

The CV–TBC signal (timebase corrected video) arrives on this module at plug 3C1 (from ETBC–B module H) and goes via C2001 to switch IC7201–3A. This switch is controlled by the CV/CS signal of the DRIVE PROCESSOR MODULE (R). This signal can turn over the switch between video and comp.sync. This comp.sync signal is the output signal of switch IC7201–3C which is controlled by the CSREF signal, obtained from the REF SOURCE MODULE (D). That signal takes care of the switch–over at the right time between 2 dc voltages, 4V at pin 5 of IC7201–3C (video level) and 3.3V at pin 3 of this IC (top sync level). So a comp.sync signal is created for a.o.th. the sandcastle generator.

The output signal of switch IC7201–3A (pin 14) goes to pin 2 of switch IC7201–3B. This switch is controlled by the CV–E/i signal from the DRIVE PROCESSOR MODULE (R) to select internal or external video.

The external video comes from the ANALOG I/O MODULE (U) and is available on plug 9C2 and goes via a 2x amplifier circuit (T7001 and T7002), to pin 1 of switch IC7201–3B. The output signal of this switch goes via emitter follower T7003 to the base of T7008. The black level of this video signal is clamped at 4V via T7004, of which the gate is driven by clamp pulses, created in IC7202 with the aid of some external components.

### Index insert

The video signal will obtain insertion of a grey level in the following circuit to get the index frame. This background level is realised by the VOBN signal at plug 5C1, coming from the DRIVE PROCESSOR MODULE (R). This TTL signal switches between 0V and 5V and goes, via T7005, to

the base of T7007. The insert is via the collector of T7007, on the emitter of T7008. Via emitter follower T7009, the video signal including the background is present on the emitter of T7009. At this point the index characters will be inserted. The index characters arrive at plug 6C1 as VOW signal from the DRIVE PROCESSOR MODULE (R). This signal is also switching between 0V and 5V and goes, via T7010 and T7011 to the base of T7012. In this circuit the character information will be made to the right voltage level, suitable to be inserted on the emitter of T7009 (characters at white level).

So on the emitter of T7009 the video signal, including index background and characters, is available.

### Video output

The CVBS signal on the emitter of T7009 goes, via T7016 and plug 1C2, to the RGB MODULE (B). This signal still contains the special burst signal, situated in the sync pulses. The ANALOG I/O MODULE needs the video signal too, but without the special burst signal. That signal is filtered out via T7017 and C2026, so via emitter follower T7018 the CVBS–2 signal (without special burst) is available at plug 6C2. FET T7017 is driven by the comp.sync pulse from IC7202.

### Sync separator + sandcastle generator

The composite sync signal is separated from the video signal in IC7202. The comp.sync signal suppresses via an OR circuit, realised by a few diodes and via nand gate 7203–4D the clamp pulses during vertical sync. The signal for creating the clamp pulses is the burstkey pulse which is separated from the sandcastle signal of pin 6 of IC7202, via T7014. The clamp pulses are needed for clamping of the black level of the video signal.

The sandcastle signal contains line frequency parts and frame frequency parts. The line frequency part is created in IC7202, output signal of pin 6. The frame frequency part (VBL signal) is added to it via T7015. The sandcastle signal can be adjusted to the correct horizontal frequency (15625Hz) with potmeter R3035.

In IC7202 a square waveform signal (15625Hz) is generated, duty–cycle 50%, and is available on pin 4. With the aid of circuit IC7203–4A,–4B and –4C a duty–cycle control of the block signal is made possible. See the timing diagram in Fig.C2. The output signal of this circuit is fed back to IC7202 (pin 2) and takes care of the horizontal blanking duration in the sandcastle signal. The width of the horizontal blanking is adjustable with potmeter R3045.

*FIG.C1 VIDEO PROC. MODULE — see the sheet below.*

<figure class="sheet" markdown>
[![Module C - video processing](assets/web/cs-7-887-text-p141-preview.webp)](assets/web/cs-7-887-text-p141-zoom.webp)
<figcaption>
  Module C - video processing.
  <span class="cs">CS 7 887</span>
  <span class="src">service manual page 141</span>
</figcaption>
</figure>

## Module D — Reference source { #module-d }

*See also the [module D page](../modules/d-reference-source/index.md).*

The circuit on this module takes care of the generation of video timing signals necessary in the player. See block diagram in Fig.D1. These reference signals have to be very accurate in frequency and timing. There are three modes of operation:

1) Stand alone.

In this mode the 5MHz crystal is locked to the 10MHz crystal oscillator.

2) Composite sync external (CS-EXT).

In this mode the 5MHz crystal is locked to the signal CS-EXT.

3) Non standard composite sync (NS-CS).

In this mode the 5MHz crystal is locked to the signal NS-CS, coming out of the sandwich part via the analog I/O module U.

If no sync signals are provided in modes 2 or 3, the stand alone mode will function automatically.

### Circuit description

ad 1) The 5MHz crystal 5001 is locked to the 10MHz crystal 5002. Inputs 8D2 and 4D2 are high impedance. In this mode the devices in use are: 5002, 7059-2A, 7060-4A, 7061-2B, 7062-3A, 7061-2A.
ad 2) The 5MHz crystal 5001 is locked to CS-EXT (8D2). For this mode the select signal CS-S/NS is at +5V. In this mode the devices in use are: 7050,51,52,53,54,55,56,57 and 7068.
ad 3) The 5MHz crystal 5001 is locked to NS-CS (10D1), coming out of the sandwich part. This mode is selected if CS-S/NS is pulled to ground. In this case 7068 is in use.

The NS-CS signal comes via the analog I/O module (Ua) from the vid mix module (Y). The CS-EXT signal can be applied directly to the analog I/O module (Ua). The control signal CS-S/NS can drive a switch circuit to pass the NS-CS signal or the CS-EXT signal. This control signal comes from the VID MIX MODULE (Y) and will be available on this module via the analog I/O module (Ua). The switch circuit is realized with the aid of 3 NAND gates in IC7068.

If neither comp. sync signal is available, it will be detected by the sync generator IC7063 which creates the "no sync" signal at output pin 13 in that case. The no sync signal takes care of the functioning of the reference oscillator of 10MHz by driving switch IC7062-3A.

The CS-EXT signal can be a clean comp. sync signal or a complete CVBS signal. In case of a CVBS signal a sync slicer circuit (IC7054-7057) will derive a comp. sync signal from that signal. Fixing of the dc level of the external sync signal is also necessary. Therefore the signal goes via a "HUM remover" circuit (IC7050,7051) to remove the video content of the complete signal. The result is a clean comp. sync signal which takes care of triggering of a clamp pulse generator circuit (IC7053). This circuit creates pulses for clamping of the signal offered to the sync slicer, by switching FET T7021.

The sync signal input of the sync generator IC7063 can be seen as a "master" input to have the outputs related in phase. Phase comparison takes place in IC7063 and depending on the result an output signal PHASE is realised controlling the varicap (6013) voltage of the 5MHz oscillator.

An FAS-REL signal is provided to this module. This signal is created on the analog I/O module (Ua) and is a dc voltage adjustable between 0V and 8V with potmeter R3149 on module Ua. This signal can influence the horizontal shift of the outgoing video signal. So the video signal of the player can be related to a possible computer video signal. The control range is from +4us (0V) to -4us (8V).

See for greater detail of the timing the data sheet for the SAA1043.

Because of the necessary processing time of the video signal in the sandwich part, an equal delay time has to be realised in the player part. This is done with the variable length shift registers IC7066 and IC7069. The delay time created in IC7069 is determined by the address offered to this IC. The required address in case of the PAL system is mentioned in the table on the circuit diagram.

<figure class="sheet" markdown>
[![Module D - reference source](assets/web/cs-7-888-text-p142-preview.webp)](assets/web/cs-7-888-text-p142-zoom.webp)
<figcaption>
  Module D - reference source.
  <span class="cs">CS 7 888</span>
  <span class="src">service manual page 142</span>
</figcaption>
</figure>

### Output signals

| Signal | Goes to, and does |
| --- | --- |
| `FI` | Field identification for genlock |
| `RAMP-EN` | Ramp enable signal to ETBC-C module, for phase measurement in the tangential error circuit |
| `80-FH` | 80-FH = 1.25 MHz signal to analog I/O module; **not used in the VP415** |
| `TXT-WH` | Teletext window horizontal, to analog I/O module for TXT insertion in the correct line |
| `400HZPAL` | To analog I/O module (Ub); **not used in the VP415** |
| `TXT-WV` | Teletext window vertical, to analog I/O module for TXT insertion in the correct line. Identical with `REFV` |
| `REFH` | Horizontal reference signal, to drive processor module R for horizontal sync character insert, to genlock module G, and to analog I/O module Ua for loop-through to video mixer module Y |
| `REFV` | Vertical reference signal, to drive processor module R for vertical sync character insert and VBL generation. Identical with `TXT-WV` |
| `CBL` | Composite blanking signal, to analog I/O module U for loop-through to video mixer module Y, and used for blanking |
| `CS-REF` | Composite sync reference signal, to analog I/O module Ua and video processor module C |
| `CLP` | Clamp pulse, to analog I/O module |
| `H/2` | PAL 8 kHz pulse, to analog I/O module Ub for 0°–180° phase switching of the chroma subcarrier for R−Y |
| `BF` | Burst flag signal, to the analog I/O module |


## Module E — Slide drive { #module-e }

*See also the [module E page](../modules/e-slide-drive/index.md).*

The slide drive module, see the block diagram in Fig.E1, controls the slide drive motor. The function of the slide drive motor is to move the LDU under the disc in such a way that the tracks can be read out in an optimal way.

### Circuit description

The slide is driven by a stepping motor. Each step moves the slide by about 50 track spaces. The motor is driven by means of pulses on COMM 1-4 and SL-PWR which switches the motor coils between holding and moving power levels via an astable multivibrator with transistors 7002, 7003.

The drive signals are provided by the drive processor, module R.

*Fig.E1 SLIDE DRIVE MODULE — see the sheet below.*

## Module F — Motor + sequence { #module-f }

*See also the [module F page](../modules/f-motor-sequence/index.md).*

The circuits in this module take care of the drive of the turntable motor. See servo block diagram and block diagram in Fig.F1.

The turntable motor is of the brushless type provided with Hall elements. The main groups on the board are:

-The MDS-IC 7202. This IC takes care of the communication between the motor and other circuits and delivers the required drive voltages to the output amplifiers of the motor.

-The Hall elements which are continuously passing the position of the motor via comparators to the MDS-IC.

-The logic circuits around transistors 7020-7022 which are controlling the motor with regard to the several conditions like start, brake, motor control and current limiting.

-The pulsewidth modulator IC 7230 which is converting the drive voltages into a duty cycle controlled input pulse for the MDS-IC

-The output stages which are supplying the required drive currents to the motor coils. This currents are derived from the commutating voltages supplied by the MDS-IC.

### Circuit description

For a proper functioning of the turntable motor, several input signals are required:

-TTM, the turntable motor on signal which is "H" during start and play conditions and delivered by the drive processor.

-MCO, a duty cycle controlled pulse which is originating from the GenLock Module and only active in the locked position.

-CLV-TC, a logic "H" signal, present during track crossing at CLV discs.

-MEM-SU, Memory start up, a logic "H" signal in case of focus loss on CLV disc in search mode. The last tacho information is then stored in a memory.

### Start condition

In start condition the TTM signal is "H" and is via the buffer amplifiers 7001-7002 fed to the MDS-IC. As long as the motorspeed is below 1500 RPM, the output signal TSP of the tacho circuit in the MDS-IC is "L" which causes switch 7201-4C to be open. The TSP signal is also fed to the sequence circuit and causes that 7021 is blocked. The collector voltage is then "H" and switch 7201-4C is closed. The "H" voltage from TTM is fed via 7201-4C to pulse-width modulator 7230-2A. This results in a low duty cycle and causes speeding up of the motor. The charge current of 2031 is limited by the diodes 6001-6002. The pulse-width modulator 7230-2A compares the control voltage with a sawtooth signal derived from the clock circuit in IC 7202. The frequency is about 17.6 kHz. The sawtooth shaped voltage is obtained by the generator consisting of transistor 7023, capacitor 2030 and the resistors 3029-3031. It will be clear, that the duty cycle decreases when the d.c. control voltage increases.

*Fig.F1 MOTOR+SEQUENCE MODULE — see the sheet below.*

<figure class="sheet sheet--fold" markdown>
[![Module E - slide drive](assets/web/cs-7-889-text-p143-preview.webp)](assets/web/cs-7-889-text-p143-zoom.webp)
<figcaption>
  Module E - slide drive.
  <span class="cs">CS 7 889</span>
  <span class="src">service manual page 143</span>
</figcaption>
</figure>

### Running condition

As soon as the motor is running, 12 p/rev. pulses are applied from 30IC-7202 to the base of transistor 7050. This causes the input voltage on 5-IC7230 to increase from about 2.7V up to 3.2V. After the opamp and the diodes 6061-6066 a small part of the output voltage is fed to switch 7201-4D. As soon as 1500 RPM is reached, the TSP-signal becomes "H" and switch 7201-4D will close. At the same time transistor 7021 starts conducting and switch 7201-4C will open. This means a lower input voltage at the pulse width modulator and the motor will not accelerate anymore.

### Frequency control

When the motor has reached a speed of 1500 RPM and TSP is "H", switch 7201-4B is closed via resistor 3021 and diode 6022. Now the motor control will take place with the aid of the LWPM signal and the phase compensation network IC 7260-2B. The output will be combined with the running current limiter signal.

### Phase control

In running condition TSP has become "H", capacitor 2020 is charged and after about 0.5 sec transistor 7020 starts conducting and the collector voltage will drop. Switch 7201-4B opens and there is no frequency control anymore. At the same time transistor 7022 is blocked and due to the high collector voltage, switch 7201-4A is closed. From this moment on MCO-EN becomes also "H" and the motor control is taken over by the MCO-signal.

In case of CLV-track crossing, which occurs in CLV-search mode, the CLV-TC-signal becomes "H", which means that there is only frequency control by the LPWM-signal.

### Active braking

When TTM becomes "L", TSP is "L" too. Switch 7201-4A will open and 7201-4C will close. A lower voltage is now given to the pulsewidth modulator input. Upon motor stop, all driver inputs are disabled.

## Module G — Genlock { #module-g }

*See also the [module G page](../modules/g-genlock/index.md).*

The purpose of this module is to establish lock in both frame and line between the disc and the sync generator on the reference source module (D). Thanks to the fact that the player is equipped with RGB, synchronization of the colour subcarrier is not required. Locking is possible at the internal sync generator which is highly accurate. In this way it is possible to place, before the disc is turning, text on the screen which is coupled to a sync to which the disc will also be synchronized later. Moreover, the video signal of the disc can be synchronized to an external video or sync signal. See the block diagram in Fig. G1. Locking is done by adapting the rotational speed of the disc or the motor control via module F. In this way the phase of the read-out video (CV-DOC) is controlled.

The time required by the player for synchronization can be divided into two parts. First the internal sync generator should synchronize to the external signal. This can take maximum 7 s. However, this action can already be started when the disc is still standing still. Next the disc should synchronize to the internal sync generator. This may take 3 s. When the phase of the external sync is reset arbitrarily during the program, the internal sync generator should fall into step and the disc should again lock to the internal sync. This may take a total of 7 s because both actions take place simultaneously.

### Circuit description

For the blockdiagram of the genlock module, see Fig.G2. Sync separator IC 7205 runs on a VCO with a centre frequency of 4.5MHz and control element varicap diode 6014.

IC 7205 outputs:

20 LPO Line pulse out, a line sync pulse obtained from input signal CV-DOC (Composite video dropout corrected).
19 M-LOCK CV-DOC/VCO locked.
15 MCO Motor control out, duty cycle proportional to speed error.
4 DEM-BK Burst key pulse from demodulated video (CV-DOC).
8 Frame pulse.
3 4.5MHz clock.
6 Composite syncs derived from CV-DOC.

In IC 7205 the phase comparison between the line pulses of the disc (derived from CV-DOC) and the line frequency pulses of the reference (4.5 MHz divided by 288) takes place. The phase difference will cause a change in the duty cycle of the MCO signal. The MCO signal is the input signal for the motor control. The line pulses of the disc are thus phase-coupled to the reference.

The signals from pins 4,6 and 8 are combined (IC 7206-2B, T 7018) to give DEM-BK. The pulses are suppressed around the vertical sync pulse.

The signal from pin 8 is stretched in one shots 7207-2A, 7207-2B to give DO-INH (dropout inhibit during the lines occupied by the Manchester codes).

### Establishing lock

Lock is established in speed and phase by adjusting the voltage applied to varicap diode 6014. This occurs in defined stages. During lock-in (crash lock) the phase control (outputs 13,14 IC 7201) is disabled by:

a) MCO-EN until 1500 rpm is reached, and

b) Line and frame lock has been achieved (INL2, pin 1,IC7201).

When this stage is reached MCO-EN and INL2 indicate "OK" and via ICs 7203-4B, 7203-4C and transistors 7004, 7005 the clamp voltage is removed from the phase correction network consisting of transistors 7006, 7007 and IC 7204-2A. Phase control outputs 13 and 14 of IC 7201 are now effective. Dependent on the required phase correction the charge on capacitor 2008 will be changed by charging more via transistor 7006 or discharging more via transistor 7007. The charging charge on capacitor 2008 will via OPAMP ICs 7204-2A and 7204-2B adapt the varicap voltage on diode 6014 and thus the reference frequency of IC 7205.

IC 7201 operates by comparing FI (field identification) and RSFH from the reference module (D) with LPO and DEMV (obtained from CV-DOC in IC 7205).

The comparison is obtained by counting GLC pulses. Speed corrections are made in a decreasing series of steps, from +/- 1.8% to +/- 0.1%. The dividend of the variable divider is dependent on the number of line pulses which is counted between the leading edges of the field identification of the disc (DEMV) and the field identification of the reference (FI). When the phase difference is maximum the disc goes with a speed of 1.8% relative to the nominal to the reference. As the phase difference decreases, the relative speed decreases too. In this way frame lock is realized. The next action is the synchronization of the line pulse. If genlock IC 7201 establishes that there no longer are line pulses between the field identification pulses of the disc video and the reference, the FRLOCK signal becomes active (high level, 5V). This is followed by permanent comparison between the line pulses of the disc and the line pulses of the reference.

*Fig.G2 GENLOCK MODULE G — see the sheet below.*

<figure class="sheet sheet--fold" markdown>
[![Module F - motor + sequence (running condition / frequency / phase control)](assets/web/cs-7-890-text-p144-preview.webp)](assets/web/cs-7-890-text-p144-zoom.webp)
<figcaption>
  Module F - motor + sequence (running condition / frequency / phase control).
  <span class="cs">CS 7 890</span>
  <span class="src">service manual page 144</span>
</figcaption>
</figure>

## Module H — ETBC B { #module-h }

*See also the [module H page](../modules/h-etbc-b/index.md).*

This module is part of the electronic timebase correction system (see block diagram overall timebase correction, fig.H1).

It is comprised of two CCD (charge coupled devices) delay lines to effect coarse correction (+/- 17 micro secs) and two variable LC delay lines to effect fine correction (+/- 50 nano secs).

Video and audio signals are treated separately, in parallel. IC 7201 is the CCD for the video channel and IC 7203 the CCD for the audio channel (see fig.H2).

On this module the timebase of the drop-out corrected composite video (CV-DOC) is corrected. This is necessary because of the presence of several tolerances (disc, centring, motor) which cause variations on the line phase of the video signal read. The variations can be about +/- 17us compared with the reference. This is unacceptable for video processing, so correction is needed. In the previous players the correction was realised in a mechanical way, the tangential mirror. In the new-generation disc drives the tangential mirror is not applied anymore. The timebase is corrected electronically. The ETBC B module will have the timebase corrected comp. video signal (CV-TBC) as output signal for further processing on the vid proc module (C).

Also it is necessary to have timebase correction of the audio signal (HFAUD), which is realised too on this module. As result the output signal is the timebase corrected hf audio signal (HFATBC).

Control of the time delay is by means of TANG-ER and BURST-ER both from the ETBC C module (I).

### Circuit description

### Video timebase correction

The CV-DOC signal from the video do corr module (L) arrives at this module on plug 2H2 and goes, via emitter follower T7013 and a lowpass filter (≤6.6MHz), to the input of the CCD memory IC 7201. Lowpass filtering is necessary to prevent aliasing effects in the CCD. The video signal will get a time delay in the CCD depending on the frequency of the clock signal offered. The clock oscillator is connected to pin 14 of IC 7201 and functions as a voltage controlled oscillator (VCO), IC 7206. The voltage offered is the measured error signal (TANG-ER) created on the ETBC C module (I). The TANG-ER signal is present on plug 4H1 of this module. As the clock rate is determined by TANG-ER, so the time the signal is delayed in the CCD's is also determined by TANG-ER. This shows that as TANG-ER is a measure of the time error, a loop is set up which will compensate for timebase errors within the measuring accuracy of TANG-ER.

The frequency of the clock oscillator output signal is inversely proportional to TANG-ER and has a centre frequency of about 19MHz.

Referring to the anti aliasing phenomenon mentioned above it will be seen that low pass filtering of the input signal is required to eliminate any frequencies greater than half the clock rate.

In the CCD IC 7201 a flipflop is situated which acts as a :2 divider. The 2 output signals of this flipflop go to the 2 x 680 stages shift register, so the complete delay is 1360 stages for the video signal (see fig.H2). Reading by the CCD memory happens every positive going edge of the flipflop output signals Q and Q. For the timing of the internal flipflop, see Fig.H3.

*FIG.H1 BLOCK DIAGRAM - OVERALL TIMEBASE CORRECTION — see the sheet below.*

*FIG.H2 ETBC B MODULE — see the sheet below.*

<figure class="sheet" markdown>
[![Module H - ETBC B](assets/web/cs-7-891-text-p145-preview.webp)](assets/web/cs-7-891-text-p145-zoom.webp)
<figcaption>
  Module H - ETBC B.
  <span class="cs">CS 7 891</span>
  <span class="src">service manual page 145</span>
</figcaption>
</figure>

The timebase corrected output signal of IC 7201 goes, via T7018, to T7020 to have a 3x amplification. The signal continues from the collector of T7020, via emitter follower T7021, to plug 7H1 as CV-TBM signal. For the system this signal is the measuring signal to create the error signals on the ETBC C module (I). On that module a comparison takes place of the measure signal and the reference signals. So this is the feedback loop of the timebase correction mechanism.

At the same time the signal of the emitter of T7018 goes, via T7017, to a steep lowpass filter (≤7MHz). This filter is realised by coils L5002...L5008 and the varicap diodes D6005...D6010. The filter circuit provides the video signal with a delay time of 200ns and depending on the voltage on the varicap diodes another +/- 50ns. This depends on the BURST-ER signal. Lowpass filtering is also necessary to prevent switching noise of the CCD.

In the video path there is some high frequency loss in the CCD. This is compensated for with a high pass network in the emitter of T7022 giving a rising response of about 6dB between 2 and 4MHz. From this network the video signal will be available on plug 2H1 as CV-TBC signal, via amplifier T7023 and emitter follower T7024.

The BURST-ER signal is present on plug 5H1 and goes, via potentiometer R3134, to the + input of opamp IC 7202-2A. From the output of this opamp the signal goes, via voltage follower IC7202-2B, to the varicap diodes of the variable LC delay line.

Dependent on the voltage offered the delay time will change, and this with a maximum of the above-mentioned +/- 50ns. The functioning of this circuit can be seen as a fine correction of the timebase errors.

### Audio timebase correction

The HF-AUD (high frequency audio) signal from the HF PROC module (K) arrives this module (H) on plug 1H2. The audio signal goes, just like the video signal, via a lowpass filter to a CCD memory IC (IC7203). The audio signal needs timebase correction too.

The clock drive for the shift register is driven by the clock signal coming from flipflop IC7204-2A. The input signal of the flipflop is realised by the same VCO as used for the video path.

The flipflop IC7204-2A is used as :2 divider. The clock frequency can be half the value because of the lower number of stages used (680 instead of 1360). The time delay will be the same as for video, but the passband of the audio signal is lower.

The output signal of CCD IC7203 goes, via emitter follower T7026, to a lowpass filter (≤2.3MHz) to filter the switching noise.

This LC filter functions also as variable delay line with the aid of the varicap diodes 6013. The varicap diodes are controlled by the BURST-ER signal. The output signal of IC7202-2A, derived from the BURST-ER signal, goes, via C2059, potentiometer R3122 and emitter follower T7029, to the varicap diodes. The controlled time delay differences will have the same value as for the video signal. Via amplifier stage T7030 and emitter follower T7031 the timebase corrected hf audio signal is available on plug 9H1 as HFATBC signal.

## Module I — ETBC C { #module-i }

*See also the [module I page](../modules/i-etbc-c/index.md).*

This module is part of the electronic time base correction system (see block diagram overall timebase correction, fig.H1). Its primary function is to measure the timebase error and provide coarse (TANG-ER) and fine (BURST-ER) correction control signals to module H. To give the required accuracy, error measurement is made at two levels of precision.

The CV-TBM signal is coming from the ETBC-B module (H) and is the composite video signal for measuring the timebase error.

See Fig.I1 for the block diagram of this module.

Coarse measurement is obtained from comparison of syncs in CV-TBM and the RAMP-EN signal. The RAMP-EN signal is the reference timing signal from the REF SOURCE module (D). Fine error measurement is obtained from the special burst, a 3.75MHz signal during sync pulses. This inserted signal can only be found in the video signal from the disc.

### Circuit description

### Tangential error detector

For the circuit diagram of the tangential error detector, see Fig.I2.

CV-TBM applied to pin 9, IC 7203 (synchronization IC) is passed through an internal low pass filter and the syncs are separated. From these a line sync signal is obtained (HMANCH, pin 20 of IC 7203). From this signal a constant length pulse is obtained by one shot IC 7201-2A. In a similar way a pulse of the same duration is obtained from RAMP-EN (from module D). See the timing diagram in Fig. I3 (pulse width T1=33μs).

Comparison of the relative timing of these signals in 7202-2A, 7202-2B, gives a current in one of the collectors of 7004, 7005 which is proportional to the time error. See the timing diagram in Fig.I4 (pulse width T2=4.7μs), assuming that the disc video and hence the HMANCH signal derived from it has a longer timebase than the reference (also see fig. I3). This may e.g. occur when the disc turns too slowly.

<figure class="sheet" markdown>
[![Module I - ETBC C](assets/web/cs-7-892-text-p146-preview.webp)](assets/web/cs-7-892-text-p146-zoom.webp)
<figcaption>
  Module I - ETBC C.
  <span class="cs">CS 7 892</span>
  <span class="src">service manual page 146</span>
</figcaption>
</figure>

In Fig.14 output pulses P1 and P2 are drawn with dotted lines because these signals are only present when clear input pins 3 and 13 resp. are "high" (C1 and C2). These inputs are not constantly high but dependent on the outputs of one shots IC 7201-2A and -2B. See Fig.15 for the actual timing.

The timing figures show that a positive pulse remains (P2). Via T7005 it will see to a discharge of C2015. As a result the dc level of the TANG-ER signal will rise via buffering by IC 72072B. In this way adaptation of the timebase correction takes place, in the sense that the throughput time of the video signal is reduced.

*FIG.11 ETBC C MODULE — see the sheet below.*

C2015 will be charged for too short a period time of the disc video relative to the reference. Charging will take place by the negative pulses (P1) and T7004. The dc-level of the TANG-ER signal will drop. As a result the throughput time of the video on module H will be lengthened.

### Special burst separator + gate

From CV-TBM the special burst is extracted by T7001, L5001, C2005, and is, via emitter follower T7002, available at the source of FET 7003. The special burst signal is gated by the syncs from pin 6, IC 7203 at T7003.

T7011, T7012 act as a 'special burst presence' detector, the collector of T7012 going high if a special burst is present.

The special burst is applied via T7029, T7014 to input 4, IC 7206-2A.

### Sample detector

The sample detector, see Fig.16, sees to delivery of a sample pulse signal which is an accurate measure for the frequency of the disc video. This is realized by looking to exactly the same zero crossing of the special burst signal each line time.

The special burst signal is tied to one shot IC 7206-2A, pin 4. Pin 6 of this IC will change over to a high level as soon as pins 4 and 5 are high and pin 3, reset input, is high too. The latter will be realized via one shot IC 7206-2B and T7015. The input signal of this IC is the comp. sync signal derived from the disc video. This comp.sync signal thus triggers one shot IC 7206-2B, which delivers in its turn a defined pulse at pin 10. Via T6215 this pulse sets one shot IC 7206-2A free. Dependent on the pulse time at pin 3, which is determined by C2042 and R3081, one shot IC 7206-2A will be reset (low level at pin 3). One shot IC 7206-2A will be active after release at pin 3 and will give a pulse at pins 6 and 7 at the next zero crossing of the special burst signal. T7016 ensures the selection of the correct zero crossing with respect to the line sync.

### Tangential phase detector

The RAMP-EN signal of REF SOURCE module D is tapped by means of resistors R3127 and R3128 and goes to the tangential phase detector circuit, see Fig.17. The RAMP-EN pulse goes to the base of T7027 which is incorporated in a one shot circuit, formed by T7027 and T7028. The output pulse of this one shot goes to the base of T7019 and will let this T7019 conduct at high level thus discharging C2052. The output signal of IC 7206-2A, pin 7, is via C2049 present on the collector of T7017 as sample pulse signal.

The sample pulse signal indicates exactly where a fixed zero crossing of the special burst signal is situated. The frequency of the sample pulse signal can be seen as an accurate measurement of the line frequency of the disc video signal. Via R3094 this pulse is present at the base of T7018 and will let this T7018 conduct in case of a low level. As a result C2052 will be charged via R3097. This causes a certain sawtooth signal on C2052. The total picture of charging and discharging can be seen in Fig.18.

This sawtooth signal goes via T7020, T7021 to the source of FET T7023. This FET T7023 sees to sampling out of the platform level in the sawtooth voltage. This voltage level will be present at C2053 then. When the zero crossing of the special burst takes place, T7023 is turned on loading a new voltage into C2053. The value across C2053 is proportional to the timebase error as measured from the special burst. Should the phase relation between the RAMP-EN signal and the sample pulse be disturbed, the result will be a level change of the platform in the sawtooth signal. Thus a dc-change at C2053 and thus, via opamp IC 7027-2A, a change in the BURST-ER signal.

<figure class="sheet sheet--fold" markdown>
[![Module I - ETBC C (continued)](assets/web/cs-7-893-text-p147-preview.webp)](assets/web/cs-7-893-text-p147-zoom.webp)
<figcaption>
  Module I - ETBC C (continued).
  <span class="cs">CS 7 893</span>
  <span class="src">service manual page 147</span>
</figcaption>
</figure>

It is important that timebase correction is disabled during the start-up sequence until motor lock (M-LOCK) and frame lock (FRLOCK) has been reached. D6018/6019,T7024/7025 are used to clamp TANG-ER to a mean value until this moment. This mean value is realized with the aid of R3118/3119/3120 and T7026.

IC 7203 also provides the CL-VID, HMANCH and VMANCH signals. These signals are necessary for decoding the manchester codes present in the video signal from the disc. CL-VID (clipped video) is only present during a few lines in the vertical blanking. The CL-VID signal is suppressed during most of the video lines by the DO-INH signal (drop-out inhibit from the genlock module G) via T7009 and T7010.

## Module J — Focus { #module-j }

*See also the [module J page](../modules/j-focus/index.md).*

The function of the focus module is to move the objective in starting condition up to such a position that the laser beam is focussed on the disc and to keep the spot focussed under all play conditions.

### Circuit description

The block diagram of the focus circuit is shown in fig.J1. The objective is driven by amplifier transistors 6208-6211, which supply a positive or negative voltage FOCACT. Negative means that the objective is driven upwards to the disc and positive means that the objective is pulled downwards. The range of the objective movement is approximately 5mm.

When the player is started up (motor not yet turning), the focus enable signal FOC-EN is low and the focus position indication signal FPI from the deck electronics is high, resulting in 0 V on the objective (see timing diagram Fig. J2). As soon as the driving module detects a disc reflection (DR), a correct slide position SPI and a laser on LA-STIA the FOC-EN will go high. When FPI is still high, the drive voltage for the objective becomes negative causing the objective to go upwards. This movement is slowed down because of the feedback through filters 2006, 2007, 3015, 3016, 3017. Switch 6205 is still open, which means that there is maximum gain (low negative feedback).

When the objective focusses the laser beam onto the disc, the FPI signal will go low, causing the focus loop switch (transistor 6206) to close and after that the focus indication signal FOC-IND to go low. FOC-EN remains high. At the same time switch 6205 will be closed, which causes more negative feedback and as a consequence less gain. The FOC-IND low signal is applied to the drive module as a command that the turntable can be started. The objective is then driven by the focus error signal FOC-ER and is kept in focus by a negative voltage of average -1V on amplifier output 6208-6211.

When focus is found, the FPI will stay high and the drive module switches the FOC-EN to low after 0.5 sec. The drive voltage becomes 0V and the objective will move downwards. After 0.2 sec the FOC-EN will become high again and will move the objective upwards. This sequence is repeated 5 times. If no focus is found, the player is switched to stand by.

If there is a minor disturbance in the reflection, FPI and consequently also FOC-IND will become high for a short moment.

The positive pulse on FPI causes a negative drive voltage on the objective and without protection the objective should move upwards. The function of one shot transistors 6214-6215 is to prevent this. The positive FPI pulse triggers the one shot and keeps via collector of 6214 the FOC-EN signal low and via 6217/6010 the drive voltage at 0V during 40 ms. During this time the objective will not move.

The FOC-ER signal is fed through a low pass filter with transistor 6201 to an AC/DC converter with transistor 6204 and diode 6001. The DC voltage drives the gain switch in the feedback circuit of the output stage. As soon as the FOC-ER signal increases up to a certain AC level, the AC/DC converter switches the gain switch to high gain of the objective drive. The increasing error current through the objective then causes an audible noise in the LDU. When a low FOC-ER signal occurs, the circuit switches to low gain, resulting in a smooth objective drive.

## Module K — HF processing { #module-k }

*See also the [module K page](../modules/k-hf-processor/index.md).*

The h.f. signal of the disc will be splitted up into a video and an audio signal in this module. See block diagram in Fig.K1. The h.f. signal goes to the h.f. video processor section. After a highpass filter an adaptation of the frequency response will take place there by means of the MTF voltage. This is necessary dependent on the read-out diameter of the disc. The corrected h.f. video signal will be demodulated in IC 7201. After filtering and amplification output signal CV-DEM will be available for further processing at module L (drop-out correction).

The h.f. signal also goes to the h.f. audio processor where the audio is filtered out by means of a lowpass filter. Output signal HF-AUD will be timebase corrected at module H.

### Circuit description

The h.f. signal is first filtered by LC circuit 5003, 2014 and 2015. The h.f. signal will be used for the video part from the collector of transistor 7005. Therefore filtering is necessary by highpass filter (>2 MHz) 2004, 2005, 2006 and 5001. Via amplifier stage 7002, 7003 and 7004 the h.f. video signal is available on the collector of transistor 7004. In the collector circuit of 7002 an LC circuit is situated, tuned to a frequency of 8 MHz.

The LC circuit will be damped more or less depending on the value of the MTF signal. So the MTF signal will via transistor 7001 take care of adaptation of the frequency responses.

Demodulation of the h.f. video signal takes place in IC 7201-2A with an adjustable output amplitude with the aid of potentiometer 3043. At point 16 of IC 7201-2A the demodulated video is available which will give a composite video signal (CV-DEM) after lowpass filtering (<5MHz) and amplification by IC 7201-2B at point 6k2 of the module.

The h.f. audio signal will be obtained from the emitter of transistor 7005. This is realised with the amplifier stage in feedback mode, 7006, 7007 and 7008 and the lowpass filter (<2MHz) in the collector circuit of transistor 7006. This filter consists of 5004 and 2019, 2020 and 2021. The h.f. audio signal is available at point 1k1 of the module.

<figure class="sheet sheet--fold" markdown>
[![Module J - focus / Module K - HF processing](assets/web/cs-7-894-text-p148-preview.webp)](assets/web/cs-7-894-text-p148-zoom.webp)
<figcaption>
  Module J - focus / Module K - HF processing.
  <span class="cs">CS 7 894</span>
  <span class="src">service manual page 148</span>
</figcaption>
</figure>

## Module L — Video drop-out correction { #module-l }

*See also the [module L page](../modules/l-video-dropout-correction/index.md).*

The circuit on this module takes care of drop-out compensation of the demodulated video signal and of generation of the MTF signal. See the block diagram in Fig.L1. The drop-out detector circuit measures a negative going drop-out and in case of a drop-out it will give a pulse to switch over the DO switch to have the delayed video as output signal. This will be the case as long as there is drop-out. The drop-out pulses can be blocked by the DO-INH signal. This is necessary to prevent drop-out correction during the data part of the video signal. Drop-out correction is only done with the luminance signal. The luminance signal is fed to the CCD memory part, which takes care of the 64µs delay (one linetime).

The DC RESTORER will take care of clamping of the dc level of the delayed video to the dc level of the direct video with the aid of the burst key pulses. The MTF signal is also created on this module. This MTF signal is a dc voltage which will vary in value depending on the read-out diameter of the disc. This voltage is used to adapt the frequency response of the hf signal on the HF PROC module (K).

### Circuit description

### Direct video

The demodulated video signal is obtained from the HF PROC MODULE and arrives, via plug 1L1, on the base of transistor 7001. Via the emitter of 7001 the signal goes via a delay line of 470ns (5001) to the amplifier stage 7002,7003. The signal goes via emitter follower 7004 to the drop-out switch IC 7201-2A. If there is no drop-out, the video signal will, via emitter follower 7005, be available at plug 1L2.

### Drop-out detection

Drop-out detection will be realised in the drop-out detector formed by IC 7202. The demodulated video goes via emitter follower 7006 to the pos.input of the opamp IC 7202, which is applied as comparator. Under normal conditions the output of the opamp is high (+12V). As soon as the pos. input will come under the switch level as a result of a drop-out, the output will become low (0V). If the video signal has no drop-out, the video level will be normal, the pos. input of the opamp will be high again. In that way a pulse is created which goes, via transistor 7007 in order to obtain the right amplitude (6V) and polarity, to pin 10 of switch IC 7201-2A.

The drop-out pulses can be blocked by the DO-INH signal. The DO-INH signal, generated on the genlock module, is present at plug 5L2. The signal is active high and will, via transistor 7008, give a low level on pin 10 of the DO switch IC 7201-2A. At that moment the switch cannot be controlled by the drop-out detector.

### Delayed video

Realisation of the delayed video is done in the following way. The drop-out corrected video signal (CV-DOC) is also fed to the base of transistor 7014. In the emitter circuit a lowpass filter (≤2MHz) is provided to separate the luminance signal. The luminance signal is fed to the CCD memory IC 7203, which takes care of the 64µs delay. The output signal will be made proper again with a lowpass filter (≤2MHz) in the collector circuit of transistor 7017 and will, via transistors 7018 and 7019, be available on the emitter of transistor 7021 as video in case of a drop-out. The CCD memory needs a clock signal, which is realised with the 13.4MHz clock generator circuit (7022,7023). The frequency can be adjusted with coil 5007 to have a delay of exactly 64µs.

The DC RESTORER mainly consists of switch FET 7020 which brings the dc decoupled delayed video from the base of transistor 7021 via filter 5006 at the dc level of the direct video. This is done during the DEM-BK pulses (burst key) that are connected with the gate of FET 7020.

### MTF circuit

The drop-out corrected video signal (CV-DOC) goes, via resistor 3043 and capacitor 2010, to the base of transistor 7009. In the collector circuit of this transistor a circuit (5003/2012) which is tuned to 4.43MHz is situated.

The 4.43MHz signal will, via emitter follower 7010, go to the source of FET 7011. The gate is driven by the burstkey pulses from the genlock module (G). Transistor 7011 is only conducting during the burstkey pulses, so on the drain of this FET only the colour burst is available. The burst signal will via capacitor 2014 go to the base of transistor 7012. The burst voltage is clamped to 0.7V by the base-emittor junction of transistor 7012, so in case of a small burst the average base emitter voltage is higher than with a large burst amplitude. Consequently a large burst causes less collector current. So the collector voltage will increase and the dc-voltage across capacitor 2016 is a measure for the amplitude of the burst signal. This voltage is via transistor 7013 available at plug 6L1, it will vary between 2V and about 10V and goes to the h.f. proc module (K). This circuit is incorporated in a closed loop thus causing continuous adaptation.

*FIG.L1 VIDEO DO CORR MODULE — see the sheet below.*

<figure class="sheet" markdown>
[![Module L - video drop-out correction](assets/web/cs-7-895-text-p149-preview.webp)](assets/web/cs-7-895-text-p149-zoom.webp)
<figcaption>
  Module L - video drop-out correction.
  <span class="cs">CS 7 895</span>
  <span class="src">service manual page 149</span>
</figcaption>
</figure>

## Module M — Radial drive { #module-m }

*See also the [module M page](../modules/m-radial/index.md).*

The function of the radial module is, to supply the required current to drive the radial mirror in such a way that the laser beam is kept on the required track, depending on the various play modes. See the block diagram in Fig. M1.

### Circuit description

In the normal play mode the radial error signal RAD-ER, originating from the deck electronics and proportional to the deviation of the laser beam relative to the track, is applied to the radial loop switch RLS transistor 7002 via a phase compensation network and a limiter IC 7100-2B. The radial loop switch, which is driven by a signal from the microprocessor 7201 on the drive processor module, is only closed when a track is followed. The radial error signal is then amplified in IC 7100-2A and via the output stage transistors 7010-7013 fed to the radial mirror. As the range of the deviation of the mirror is limited, the drive signal of the mirror is also applied via a level shifter IC 7101-2A to the drive processor. In this way too high a deviation will be compensated for by a displacement of the slide. The level shifter converts the signal, which may vary both to a positive and to a negative value, into a positive signal with the same variations.

In special play modes, the laserbeam jumps across one or more tracks. This is realised by giving the laser beam, with the aid of the radial mirror, a fast forward or reverse deviation. For this fast deviation use is made of the course pulse CP1 for a forward jump and CP2 for a reverse jump. The course pulses are also fed to the radial amplifier in IC 7100-2A. During a jump, the radial loop switch is opened by the RLS signal. The number of tracks that will be crossed in this way depends on the duration of CP1 and CP2 respectively. Both CP1 and CP2 are delivered by the drive processor module. As an indication of how many tracks are crossed, the RAD-ER signal is fed via a switchable lowpass filter in IC 7101-2B to a clipper circuit in IC 7102-2B and converted into a square wave clipped radial signal CL-RAD. The number of pulses of the CL-RAD signal, which indicates how many tracks are crossed, is fed as "count pulses" to the microprocessor on the drive processor module. In case of a jump across more than 15 tracks the radial mirror will get a high speed and about every 25 microseconds a track will be crossed. The CL-RAD signal has a frequency of about 40 kHz then with a small amplitude. In this case the switchable lowpass filter is switched to the maximum amplification of 40 kHz by the radial filter select signal RAD-FS, as a result of which sufficient signal is available again now.

During scan, a SCANLS scan loop switch "L" signal is fed to transistors 7015-7004. As a result scan loopswitch 7004 is closed and the amplification of the radial amplifier is reduced.

The TPI signal "L" on track causes switch 7003 to be closed when the beam is on track. The input voltage of the radial amplifier is present across capacitor 2014. When the beam loses track, the switch will be opened and the voltage remains on capacitor 2014. As soon as the beam is on track again, the initial input voltage for the radial amplifier is equal to the last voltage before the beam lost the track.

## Module N — Display and keyboard { #module-n }

*See also the [module N page](../modules/n-display-keyboard/index.md).*

The display and keyboard module is built around a 16 bit LED driver IC 7201, driving the indication LEDs and a buzzer. See the block diagram in Fig.N1. Two control buttons are fitted : STANDBY and EJECT.

### Circuit description

Input to IC 7201 takes place via the P-bus (SDAT, SCLT, DLEN) from control module S (IC 7211) as an 18 bit word, i.e. 0 + 16 data bits + terminating bit.

Outputs Q1 to Q10 are used to drive LEDs, Q11 provides an audio bleep via IC 7202 and transistor 7001.

If Q11 is "high", generator circuit IC 7202-4B, resistor 3012 and capacitor 2001 will be switched off via NAND IC 7202-4A. Pin 6 will remain "high" thus preventing transistor 7001 from starting to conduct. If Q11 is "low" and thus pin 3 of IC 7202-4A "high", IC 7202-4B will alternately give a high and a low level to output pin 6, dependent on the RC time (3012/2001).

The connections for the local switches are returned to the drive processor module (R).

<figure class="sheet" markdown>
[![Module M - radial drive / Module N - display and keyboard](assets/web/cs-7-896-text-p150-preview.webp)](assets/web/cs-7-896-text-p150-zoom.webp)
<figcaption>
  Module M - radial drive / Module N - display and keyboard.
  <span class="cs">CS 7 896</span>
  <span class="src">service manual page 150</span>
</figcaption>
</figure>

## Module P — Frontloader { #module-p }

*See also the [module P page](../modules/p-frontloader/index.md).*

The purpose of this module is to provide the required drive current to the motor of the front loading mechanism, which takes care, that the disc is positioned at the correct place in the player. Control signals are fed in from the drive processor module R and status signals are fed back to the drive processor. See Fig.P1.

### Circuit description

The front loader motor is a d.c. motor, which can be driven in two ways, for loading and unloading respectively. Therefore the motor is connected to a bridge circuit. See Fig. P2.

Loading: When the tray is partly pushed in, the start stop switch is connected to ground and ST-ST signal "L" is fed to drive processor R. At this moment the LMOT-L signal from drive processor R becomes "H" and transistors 7001, 7006 and 7004 will conduct. This causes current I1 to drive the motor and the tray will move further inside. When the tray is fully inside, the "tray inside" switch is closed and "I" becomes "L". LMOT-L becomes "L" again and all transistors are cut off. The motor will stop.

Unloading: When "EJECT" is pressed, the drive processor delivers an LMOT-R signal "H". Now transistors 7003, 7005 and 7007 will conduct and the motor is driven by current I2. As I2 is in direction opposite to I1, the tray will now move outwards. This continues until the ST-ST switch is open again and ST-ST signal "H" is fed to the drive processor. LMOT-R becomes low and all transistors are blocked again.

Protection device: When the tray is blocked during loading as well as during unloading, the LMOT-L and LMOT-R signals become "L" and the motor is not energized anymore.

*Fig.P1 FRONT LOADER CIRCUIT — see the sheet below.*

## Module R — Drive processor { #module-r }

*See also the [module R page](../modules/r-drive-processor/index.md).*

The main tasks of the drive processor module are :

a) To accept and interpret commands from control module S
b) Radial tracking and access
c) Manchester code reading
d) Display on screen drive
e) Start-up sequence of the disc drive
f) Local control: 'standby' and 'eject'
g) Audio and video switching
h) Service diagnostics

All the functions of module R run under control of microprocessor IC 7201. See the block diagram in Fig.R1. A 16k ROM is present on this module (IC 7204). The communication with control processor module S goes via the S-bus. The disc drive communication takes place via two I/O port expanders, ICs 7202 and 7203. Various drive and switching signals are given by the drive processor via the three 8-bit shift registers ICs 7213, 7214 and 7215. The drive processor reads the manchester codes of the video signal (clipped video) and also sees to insertion of the index signal.

### sub a) Command input

Command inputs from and responses to module S go via the S-bus. The S-bus interface comprises ICs 7203, 7216, 7206, 7207. IC 7203 is a port expander by which processor IC 7201 accesses S-bus handshake signals DAV and DAK.

IC 7207 is the data input buffer latch. IC 7206 is the data output buffer latch.

DAV and DAK are serviced via D-type flip flops 7216-2A and 2B.

For detailed information on the operation of the S-bus please refer to the S-bus section.

### sub b) Control of the slide motor

Control of the slide motor takes place via software.

The slide motor is a stepping motor driven by the 4 phase signals COMM-1 - COMM-4 and SL-PWR which are output by port expander IC 7202.

During normal play functions the slide motor is driven when the deflection of the radial mirror is approaching its limit. This is determined by measuring the mirror offset by comparison of SP-POS (Radial error from mirror drive) with the output of DAC 7218 in IC 7210-2A. The result of this comparison (RAD-MIR) is applied to input pin 31 of port expander IC 7203.

### sub c) Reading Manchester codes

IC 7211 is a dedicated device which reads Manchester codes from the clipped video signal CL-VID. The code data is stored on-board to be read by the processor via the data bus.

Signals required by IC 7211 are :

Handshake from processor IC 7201:

- ATN
- TX/RX
- STB
- IRQ
- Horizontal sync
- Vertical sync
- Clipped video
- HMANCH
- VMANCH
- CL-VID

### sub d) Display on screen

Status information from the manchester codes for display on screen is read from IC 7211 by processor IC 7201 and loaded into display driver IC 7212.

IC 7212 contains the character generator for on screen display.

Inputs to IC 7212:

- Databus Pins 14-21
- Reset 1
- HSTNC 8
- VSTNC 7
- LDI (Load index) 12

Outputs from IC 7212:

- VOBN (Background for insertion) pin 6
- VOW (Character for insertion) pin 5

To have correct timing vertical and horizontal syncs for IC 7212 are provided via IC 7219. When playing a CLV disc in the visible scan mode (internal video) the sync source is changed by NS-VID.

### sub e) Start up and control

The start-up procedure has by means of a block diagram with command signals (Fig.CR1) and timing diagrams (Fig.CR2) been dealt with in chapter 2 sub 'Control routes + start-up sequence'. Here the interaction with the various modules is discussed.

The start-up sequence operates under control of processor IC 7201 via output buffers ICs 7213, 7214, 7215 and I/O port expanders 7202 and 7203. Buffers 7213 and 7214 operate with +12V supply so the input signals are first converted by level converter IC 7208. Buffer 7215 works directly with +5V supply. The start-up consists of the sequence : Close tray, move slide to start position, detect disc, activate the tilt control, put laser on, find focus, spin disc, close radial tracking loop, find picture no. 1.

During start-up it is determined which type of player we are dealing with (PAL or NTSC). This is done by determining the distance between successive VR pulses over a number of periods.

These VR pulses are the derivatives of the REFV pulses of ref. source module D. The measured period time is studied within certain limits (windows) and next the system is evaluated. If the VR signal is missing the player will not start up.

### sub f) Local control

The 'stand-by' and 'eject' keys on the front of the player give, if activated, a low level signal directly to I/O port expander IC 7203. The drive processor will respond to this.

### sub g) A/V switching

The drive processor sees to switching on and off of the audio and video signals, not only during start-up but also during normal play procedures. It is e.g. necessary to mute audio and video during search actions, realized with the AUDION, AUD2ON and CV/CS signals respectively. Or e.g. to switch over from internal source to external source if this is requested via control processor module S, realized with the A1-E/I, A2-E/I and CV-E/I signals, etc.

### sub h) Service diagnostics

The diagnostic software has been integrated in the drive software in such a way that many of the tasks of the drive are checked for proper performance. If a fault is detected in the execution of a task, an error code is shown on the screen as video overlay (like the index information). The software program is very useful on behalf of service diagnosis. The working and the use of this diagnosis software is dealt with extensively in the REPAIR METHOD description.

IC 7209 is a watchdog circuit which provides a reset for the processor on power up and also monitors the operation of the processor giving a reset if the program crashes.

<figure class="sheet sheet--fold" markdown>
[![Module P - frontloader / Module R - drive processor](assets/web/cs-7-897-text-p151-preview.webp)](assets/web/cs-7-897-text-p151-zoom.webp)
<figcaption>
  Module P - frontloader / Module R - drive processor.
  <span class="cs">CS 7 897</span>
  <span class="src">service manual page 151</span>
</figcaption>
</figure>

## Module S — Control { #module-s }

*See also the [module S page](../modules/s-control/index.md).*

The functions of the control module are :

a) To provide an RS232 interface between the player and an external computer.
b) To provide a local bus interface with the CPU board (UART).

Control module S is driven by processor 7201.

7201 is organised to access 64k of ROM and 64k of RAM although only 8k of RAM is fitted in the VP415/VP410.

IC 7202 is the ROM. IC 7203 is the RAM. The RAM is non volatile being supported by a 2.4V Ni-CAD battery 1002.

ROM and RAM overlay the same address field, however no conflict occurs as the control bus is fully decoded. Also the data bus pins of processor 7201 are shared with the low address byte. IC7204 functioning as an address latch under control of ALE (Address latch enable). The ROM is read enabled when PSEN (Program store enable) is low. The address bus is decoded in 3 to 8 line decoder 7205 to give 6 chip select lines (CS1 to CS8). CS1 enables RAM 7203.

The I/O ports are configured to use the top 8KBytes of memory space (E000h-FFFFh). CS8 is further decoded with A10, A11, WR, and RD to give RD1-3, RDEN, WR1, WR3 and WREN.

There are a number of I/O ports.

IC7209 - Output latch strobed by WR1 providing VP0-2. These signals are controls to the mixing board Y (via diagram Uc), in the VP415.

IC7207 - Bi-directional buffer from data bus to S-bus. Enabled by RDEN or WREN with the direction set by WREN.

IC7208 - Input buffer reading the dip switches DS1-8. Enabled by RD1.

IC7211 - A slave processor providing one RS232 I/O and two RC5 I/O's. It is addressed with A9 and WR3 or RD3 and behaves as a true slave signalling via OBF (Output buffer full) when data is ready.

IC7201 - This is the main processor which provides direct handshakes for the S-bus and a single RS232 port to service the external connector via line transmitter 7214 and line receiver 7213.

### Operation

Communication with the CPU board (Module W) in the VP415 is by F-codes at 9600 baud, 1/2 duplex 5 volt logic. Communications via the external RS232 are also by F-codes but the baud rate is selectable and normal RS232 levels are used. For more information on F-codes please refer to the separate section in the operating instructions.

The default condition of module S uses the external RS232 port. The use of the internal port is selected by the CPU board module W. In this condition all F-codes presented to the external connector are ignored with the exception of mode change commands.

Memory map

| Address. | | |
| --- | --- | --- |
| ROM (PSEN) | 0000h - | FFFh |
| RAM (CS1) | 0000h - | 1FFFh |
| I/O ports (CS8) | E000h - | FFFFh |
| Address | IC. | Comment. |
| E000h | 7207 | Write to S-bus if WREN=0 else read. |
| E400h | 7211 | Slave read/write. |
| E600h | 7211 | Slave read/write. |
| E800h | not used. | |
| EC00h | 7208 | Read dip switches. |
| EC00h | 7209 | Write to mixer board. |

### Watchdog

IC7210 is a watchdog circuit which provides power on reset and also gives a reset if the program hangs up or if the local standby key is pressed. In this latter case a software reset is performed.

It consists of a retriggerable monostable which when the processor is running is continuously retriggered. At power on or if the program crashes the circuit is no longer triggered and generates a reset.

## Module T — Supply { #module-t }

*See also the [module T page](../modules/t-supply/index.md).*

The supply module of which the block diagram is given in Fig. T1 has as function to feed the stabilized voltages +12V, -12V, -5V and +5V to the various circuits in the disc drive. These voltages are obtained in a parallel switched mode power supply. The supply circuit is protected against overload by a current monitor. An auxiliary supply is used to generate the starting voltage for the driver stage of the switched mode power supply and the supply voltage of the command circuit.

### Circuit description

The mains voltage is rectified by bridge rectifier V001. The output voltage of the bridge rectifier, which is not stabilized against mains variations, is used as supply voltage for the parallel switched mode circuit with transformer T901 and transistor V203. The switching pulses on the primary side of transformer T901 are transformed to the secondary windings 12-1, 11-2, 10-3, and x921-x922. The typical forward rectifier circuit (series and fre-wheel diode, coil and smoothing capacitor) is connected to the secondary windings and the stabilized supply voltages +12V, -12V, +5V and -5V are generated. The switching transistor V203 is controlled by the output pulses on point 5 of the command circuit D501, via a driver stage with transistor V303 and driver transformer T201. The supply voltage for the driver stage is obtained by rectifying pulses from winding 10-3 of transformer T901, by diode V301 and capacitor C301. As starting voltage for the driver stage, +15V is also generated by an auxiliary supply circuit with transistor V104 and transformer T101 (self oscillating flyback converter). This auxiliary supply voltage is also used as supply voltage for the command circuit (DS01). The command circuit generates a 50 kHz duty cycle controlled voltage, which is used as drive voltage for the driver stage. The command circuit uses the +5V input signal at pin 9 as a reference for the output voltages of the switched mode power supply. In the command circuit the voltage on pin 9 is compared with an internal reference voltage and the duty cycle of the pulses at pin 5 depends on the difference between the external voltage and the internal reference voltage. With potentiometer R503 the output voltages of the switched mode power supply can be adjusted.

### Overload protection

The current in the primary of transformer T901 is proportional to the total load current. The current through transistor V203 and the primary of transformer T901 flows also through the primary of T401. This causes a voltage on the secondary side of transformer T401, across resistor R401, which is also proportional to the total load current. With the input voltage on pin 1 of command circuit D501 the duty cycle is reduced and as a consequence the output power can be limited. The level by which the current limiter starts can be adjusted by potentiometer R402. A small part of the pulses on pin 1 of D501 is applied via a voltage divider consisting of zener diode D954 and resistors R917-R918 to the base of transistor V996. During the positive pulses capacitor C506 will be discharged and the voltage on pin 12 of D501 will decrease. By this voltage level the maximum duty cycle is adjusted. This circuit is used as fast current limiter (the current limiter via pin 1 of D501 is not fast enough for transient current variations during e.g. switching on the power supply).

### The auxiliary supply

This circuit with transistor V104 and transformer T101 consists of an oscillator and a rectifier circuit. The oscillator is of the blocking type. The current through transistor V104 is increasing until transformer T101 is saturated. From that moment on there is no voltage induced anymore in winding 1-8 and the transistor V104 will be cut off. At this moment the voltages across the windings reverse. After some time the base of transistor V104 becomes positive again and a new cycle starts. The oscillating frequency is about 30 kHz. The pulse voltage induced in secondary winding 4-5 of transformer T101 is rectified by diode V106 and capacitor C104 and forms the auxiliary supply voltage of +15V.

### Output circuits

All the outputs have a common zero.

- The output +5V: winding x921-x922 of T901, rectified by series and parallel diode V701, smoothed by L701, C703. This output is also protected by fuse F913.

- The output +12V: winding 1-12 of T901, rectified by series and parallel diode V705, smoothed by L701, C707.

- The output -12V (and -5V): winding 2-11 of T901, rectified by series and parallel diode V703, smoothed by L701, C704. An additional voltage of -5V is derived from the -12V by a series regulator N801.

<figure class="sheet sheet--fold" markdown>
[![Module S - control (operation / watchdog)](assets/web/cs-7-898-text-p152-preview.webp)](assets/web/cs-7-898-text-p152-zoom.webp)
<figcaption>
  Module S - control (operation / watchdog).
  <span class="cs">CS 7 898</span>
  <span class="src">service manual page 152</span>
</figcaption>
</figure>

## Module Ua — Analogue I/O, CVBS + audio part { #module-ua }

*See also the [module Ua page](../modules/u-analog-io/index.md).*

This part of module U provides selection of the various audio and video I/O configurations of the player including DC restoration of the external video input. See the block diagram in Fig.Ua1 for the CVBS circuitry and Fig.Ua2 for the audio part.

### Circuit description

### Sync out buffer

The comp. sync reference signal (CS-REF') will be used as sync out signal. This is realised via buffer circuit T 7109/7110 which will take care of the correct amplitude of the output signal (2Vpp) and the required output impedance. The sync out signal is available at BNC socket 6.

### Sync in buffer

External sync or CVBS signals can be connected to the input BNC sockets 4 and 5. Via the buffer circuit T 7111/7112 that sync signal will be used in the disc drive as CS-EXT, which will be applied to the reference source module (D). The input is high impedance in contrast to the output. The output is made low impedance because of a wanted insensitivity to disturbances.

### Fas-rel

A simple adjustable dc voltage (0V-8V) is used as FAS-REL signal, which will go to the ref. source module (D). This is done for adjustment of the phase relation between the incoming sync signal and the outgoing sync signal (horizontal shift). The range is from +4μs to -4μs and can be adjusted at the rear of the player.

### CVBS2 via dc restorer

The CVBS signal, CVBS2, from the video processor module (C) obtains a dc restoration during the black level on the backporch of the video signal. Via the CVBS switch circuit (IC 7152) the CVBS2 is available at the BNC 3 socket, if selected. Also the CVBS2 signal is, after the DC restoration, available as TXT CVBS signal which will be fed to the TXT part of module U (Uc).

DC restoration is driven by the BP-CLP signal from the video proc. module (C). This signal goes, via buffer T 7104, to the gate of FET 7108. This FET will conduct then, so at the moment of the pulse the dc level of the CVBS signal on the collector of T 7107 will be fed to the opamp IC 7151-2A. The opamp will create an output signal which makes the dc level of the CVBS signal on the collector of T 7107 zero (pin 3 of IC 7151-2A is connected to ground).

### CVBS IN via dc restorer

The 2 possible input sockets for CVBS IN (BNC 1 and BNC 2) are connected to each other. One of the 2 sockets can be applied as CVBS input for the disc drive itself and the other socket can be used to connect another disc drive in parallel. DC restoration takes place in exactly the same way as described in the previous section. The CVBS IN signal after DC restoration is available in the disc drive as CV-EXT signal and will be fed to the video proc. module (C) and to the CVBS switch. Then it is possible to have the external video signal directly available at the BNC3 socket depending on the control signal CV-E/I and the switch SK2.

### CVBS switch

The CVBS switch is realised with IC 7152 which consists of 2 identical circuits: a switchable differential amplifier with current source. The 2 input video signals are the internal and external video signal with dc restoration. Selection of one of these signals can be done with the CV-E/I signal at plug 29cU1.

If this signal is high, the current source in IC 7152-2B will function and the CV-EXT signal will be provided to the base of T 7105 and via SK2 be available on BNC3. If the CV-E/I signal is low the switch transistor in IC 7152-2B will be cut off. In that case the circuit in IC 7152-2A will function and connect the CVBS2 signal to the base of T 7105. The signal on the emitter of T 7105 is, after division of the signal by 2, used as feedback signal to have an amplification of 2. Switch SK2 under the backplate on the rear of the disc drive can select "encoded CVBS" or "non-encoded CVBS". Non-encoded means that the video signal will not be according the standard during special playing modes.

### Audio int/ext switches

Via cinch socket "EXT AUD1" (audio left channel) the audio signal arrives at pin 11 of switch IC 7551-4A which can be driven by the A1-E/I signal at pin 12. If the A1-E/I signal is high, the switch will be closed and the external audio 1 signal will via opamp IC 7552-2A be available at the AUD-1OUT cinch bus and SCART 3 output. The A1-E/I signal closes switch IC 7551-4A if the external audio signal is asked for but will at the same time, via inverter IC 7553-4A and D 6504, open switch IC 7551-4B. So the internal AUD1 signal is switched off.

If internal audio is asked for, the A1-E/I signal will be low, so switch IC 7551-4A is open and output pin 4 of inverter IC 7553-4A is high. So this high level is blocked by D 6504 and whether switch IC 7551-4B is closed or open depends on the AUD1ON and AUD2ON signal (high level results in closed switch).

Audio switching is arranged so that if either AUD1ON = 1 or AUD2ON = 1 then both channels are active but either may be internal or external depending on the status of A1-E/I and A2E/I.

For the audio 2 channel the same procedure is valid.

### Beep generator

A beep generator is realised with the aid of a simple nand gate (IC 7553-4C) and can be switched on via the A-SYNT signal from the drive processor module (R). If the A-SYNT signal is low, output pin 11 of IC 7553-4C will be high and no oscillation will arise. If A-SYNT is of high level output pin 11 depends on the other input level of the nand gate (pin 13). If this level is high too, pin 11 will become low. Then C 2511 will be discharged, so pin 13 becomes low and causes output pin 11 to be high. C 2511 will be charged then via R 3528 and input pin 13 becomes high, etc. This process continues until A-SYNT becomes of a low level.

The "beep" of adjustable amplitude (R 3530) may be injected to both channels.

<figure class="sheet" markdown>
[![Module Ua - analogue I/O CVBS + audio part](assets/web/cs-7-899-text-p153-preview.webp)](assets/web/cs-7-899-text-p153-zoom.webp)
<figcaption>
  Module Ua - analogue I/O CVBS + audio part.
  <span class="cs">CS 7 899</span>
  <span class="src">service manual page 153</span>
</figcaption>
</figure>

*Fig. Ua2 ANALOG I/O MODULE Ub — see the sheet below.*

(AUDIO PART)

## Module Ub — Analogue I/O, video part { #module-ub }

*See also the [module Ub page](../modules/u-analog-io/index.md).*

This part of module U re-encodes -(R-Y) and -(B-Y) as a PAL chroma signal, mixes luminance and chroma and re-inserts text from disc if it is present. New syncs are inserted then and the resulting signal output goes as CVBS to SCART and encoded CVBS to the BNC outlet socket. See the block diagram in Fig. Ub1.

### Circuit description

### Luminance processing

On plug 9aU1 the luminance signal LUM arrives from the RGB demodulator module (B). The LUM signal will go via an adjustable gain buffer amplifier T 7201/7202/7203 to C 2204. The luminance signal will be clamped by the BPCLP signal. This signal is available on the gate of FET 7204 and will clamp the black level of the luminance signal to about OV.

The clamped luminance signal is present on the base of T 7205. Because the base of T 7206 is at GND level T 7205 will not pass on signals of negative level. In this way the syncs are removed and the luminance signal without syncs is available on the emitters of T 7205/7206. This removing of the syncs is blocked if the NS-VID signal (plug 6cU1) is high. Because this signal can let T 7217 conduct and pull the base of T7206 to a negative voltage level. The original syncs will remain in the luminance signal. The luminance signal will be buffered by T 7207 and is then present on the base of T 7209.

The signal at the base of T 7209 will be shorted to GND if FET 7208 is conducting. This is only possible via a high level of the CBL (composite blanking) signal, which only arises in the signal parts without luminance information (line syncs, frame syncs, burst period).

This blanking is blocked again by the NS-VID signal via T 7221.

The processed luminance signal will via emitter follower T 7209 go to the base of T 7211. In the meanwhile the luminance signal will be mixed with the encoded chroma signal via L 5202. Unwanted chroma in the luminance signal will be filtered out via C 2206, L 5202 and T 7223. The encoded chroma will be added to the luminance signal via T 7210 and T 7223.

To the signal at the base of T 7211 TXT information will be added via the T 7211/7212 circuit. The amplitude of the INS-TXT signal can be adjusted by potmeter R 3240. The insertion of TXT signals can be blocked too. If wanted, the NS-VID signal will make T 7222 conducting. In that case the INS-TXT is shorted to GND, so the video signal will pass T 7211 without TXT insert. The video signal will be available at the base of T 7213.

New syncs are now added to the signal at the base of T 7213 from the CS-REF signal (generated on the REFsource module (D)), via T 7216/7219. The amplitude of the offered sync signal can be adjusted with potmeter R 3263, via T 7220. Also, the insertion of CS-REF can be blocked by the NS-VID signal via T 7218.

<figure class="sheet" markdown>
[![Module Ub - analogue I/O video part](assets/web/cs-7-900-text-p154-preview.webp)](assets/web/cs-7-900-text-p154-zoom.webp)
<figcaption>
  Module Ub - analogue I/O video part.
  <span class="cs">CS 7 900</span>
  <span class="src">service manual page 154</span>
</figcaption>
</figure>

The complete video signal (CVBS) will go via T 7213 and the 2 emitter followers T 7214 and T 7215 to the outlet sockets SCART (pin 19) and BNC3 (CVBS out) resp.

At the moment there is non-standard video (during visible scan CLV) and the internal video is selected, the NS-VID signal (plug 6cU1, coming from the drive proc. module R) is high. If NS-VID is high the insertion of CBL, sync removing, sync insert and TXT insert will be blocked. The original luminance signal will be kept complete and is, with added chroma, directly available on the outputs.

### Chroma encoding

Encoding of the chroma signal is taken care of by IC 7351. The -(B-Y) signal and the -(R-Y) signal are coming from the RGB module (B). The -(B-Y) signal is available on pin 8cU1 and will go, via inverting and buffering stage T 7305/7311 with an adjustable amplitude (R 3315), to pin 12 of IC 7351.

The -(R-Y) signal will have the same process via T 7301/7310 and is present on pin 5 of IC 7351. A crystal oscillator (5302) is connected to IC 7351 to generate the chroma subcarrier frequency of 4.43MHz.

In IC 7351 itself generation of 2 carrier signals with a relative phase difference of 90° (pin 2 and 14) takes place.

A signal with half the line frequency (H/2, from the REF SOURCE module D) is provided to pin 8 of the IC (square-wave form). This signal will take care of a 0° or 180° phase shift of the subcarrier signal to have the (R-Y) signal phase shifted 180° every second line.

Via plug 10aU1 the CBL (Composite BLanking) signal is applied to MOSFETS 7302 and 7306. These fets can be made conducting by the CBL signal, which causes the (R-Y) and (B-Y) signals to be clamped to the voltage level of pin 10 of IC 7351 offered to the sources of the MOSFETS.

This is done to prevent chroma signals during the blanking period. In that period the dc-levels on pin 12 and 5 of the IC have the same level as the reference voltage of pin 10.

Because the colour burst also has to be generated, the BF (burst flag) signal will take care of pulse creation at the right moment. The amplitude of the pulse to be added is adjustable by potmeter R 3309 for the (R-Y) signal and by R 3319 for the (B-Y) signal. The dc levels will be added to the chroma difference signals via MOSFETS 7303 and 7307. The dc level is derived from the reference voltage of pin 10 (via T 7304 and T 7308).

The signals of the (R-Y) modulator and (B-Y) modulator will be added, clamped to the reference voltage of pin 10 by the CS-REF signal on pin 7, and made available as encoded chroma signal on pin 9 of the IC. This encoded chroma signal will be inserted in the original luminance signal.

## Module Uc — Analogue I/O, TXT part { #module-uc }

*See also the [module Uc page](../modules/u-analog-io/index.md).*

In the VP415, to allow text or graphics from an external computer to be mixed with the video from the LV disc, the CVBS signal from the disc is demodulated to RGB. Text or graphics from the external source are added and the resulting signal output as RGB.

Because there is no way to pass the teletext signal from the disc by an RGB link, Module Uc provides an alternative path to the CVBS encoder. See the block diagram for the TXT bypass in Fig.Uc1.

Timing of the teletext signal is extremely important and so we find that Module Uc is built around a teletext video input processor, the so-called eye-height restorer, and a number of devices to ensure correct timing.

### Circuit description

CVBS from the disc enters IC 7651, pin 27. In IC 7651 the text data is separated from the CVBS signal and output at pin 15. Also the bit clock (6.9375MHz) is regenerated and output at pin 14.

The text data passes via IC 7657-8C, 7658, 7661, then is inserted (INS-TXT) into the CVBS, see diagram Ub.

IC 7658 is a variable length shift register, the length (number of stages) being determined by the setting of the dip switches and the time difference between reference sync (CS-REF) and the sync signal from pin 25 of IC 7651.

The setting of the switches is pre-loaded into ICs 7655 and 7656 at the commencement of each TV line by means of CS-REF and the sync signal from pin 25 of IC 7651.

### Selection of text source

In the general application of this board to the VP400 series of disc drives it is necessary to select text from CVBS or text from external (computer insertion) source as the presence of text from more than one source would confuse the decoder in the monitor.

The option of text insertion by either F-code or V-code is not available in the VP415. However, the components to allow this selection are still fitted. IC 7661 a multiplexer is present to effect this selection. Text from disc is selected when inputs 14 and 2 are both high. Input 14 is high when signal V/C-TXT, plug 20cU1, is high (text from disc allowed). When input 2 is high, is determined by line counter IC 7659, 7660. Text on disc may be present during lines 20, 21, 333 and 334 of the video signal.

<figure class="sheet" markdown>
[![Module Uc - analogue I/O TXT part](assets/web/cs-7-901-text-p155-preview.webp)](assets/web/cs-7-901-text-p155-zoom.webp)
<figcaption>
  Module Uc - analogue I/O TXT part.
  <span class="cs">CS 7 901</span>
  <span class="src">service manual page 155</span>
</figcaption>
</figure>

## Module W — Data grabber and CPU { #module-w }

*See also the [module W page](../modules/w-cpu-data-grabber/index.md).*

### Function description

We may summarise the functions of the data grabber as :-

a) Collect serial data from the LV-ROM decoder.
b) Convert the two streams of serial data to parallel form.
c) Establish lock with the block structure.
d) Read the header.
e) When the desired header is seen, store that block and the two following blocks in RAM.
f) Signal to the CPU that the header and the following three blocks are ready.

During this sequence the data is unscrambled and if error flags are present the CPU enters a correction routine to recover corrupt data.

### Circuit description

The bus structure of the data grabber is as follows:

- Table W1
- Bus Function

| A | Address from CPU. |
| --- | --- |
| B | Address from byte counter. |
| C | Ram and eprom address. |
| D | Data to/from CPU. |
| E | Data to/from RAM. |
| F | Data, descrambler byte from EPROM. |
| G | Data, descrambled data. |
| H | Data from shift registers (S/P). |

### Bus linking

Certain of these buses can be interconnected as follows :

Table W2

| Address bus C | ENW=0, to B bus | ENW=1, to A bus |
| --- | --- | --- |
| Data bus E | ENW=0, to G bus | ENW=1, to D bus |

Serial data from the LV-ROM decoder (DLCF,DRCF) is placed in shift registers IC9,10,11,12 to appear as 4 parallel bytes (Hbus).

These 4 bytes are strobed out under control of signals SA0-SA3

which are decoded from B0,B1 of the byte counter. Each byte from the shift registers is EXORed with a byte from the descrambler EPROM (F bus) in IC's 16,17 to appear on the G bus.

From the G bus the bytes are transferred via buffer IC21 to the RAM IC 22.

The 4 header bytes are collected in the header register IC's

19,20 the remainder of the batch of three blocks are placed in the RAM. The CPU can now read the header information to determine if this is the start of the wanted sequence of blocks.

### Input circuit

Inputs from the LV-ROM decoder are via connector W1.

Table W3

| DRCF | Data right | Pin 8 |
| --- | --- | --- |
| DLCF | Data left | Pin 4 |
| STR1 | Word strobe | Pin 5 |
| STR2 | Byte strobe | Pin 7 |
| CLCF | Bit clock | Pin 6 |
| ERCF | Error flag right | Pin 3 |
| ELCF | Error flag left | Pin 2 |
| GND | Ground | Pin 1 |

The incoming signals are buffered in IC's 2,3.

### Sync detector

This circuit detects the sync pattern at the start of the data block. The pattern consists of a 12 byte sequence.

The detector comprises EPROM, IC 1 and D-Type flip flops IC's 6,7 and operates as a labyrinth in which, provided that the correct 96 bit pattern (8 x 12) is present an output pulse SNC will be developed. This pulse initiates the byte counter.

### Sync signal SYN

This signal is used to produce a byte count in sync with the incoming data.

When SYN=1 the count is set to 000h. The count commences when SYN=0. From this point on the byte counter generates addresses for the descrambler EPROM and the RAM. Owing to the fact that SYN is produced a little early it is delayed in IC 8 to correspond with the leading edge of ST1. Error window pulse ERWD.

If ERCF or ELCF are present indicating errors uncorrected in ERCO then by ORing these signals ERWD is produced. ERWD signifies that the error correction routine must be entered by the CPU.

ERWD is stored in flip flop IC 30. IC 30 is reset by HDR when a new header is recieved.

### Descrambler

The data in each block has a superimposed scrambling pattern which must be descrambled. This is achieved by EXORing byte by byte with a descrambling pattern from EPROM IC 24. Addresses for the EPROM are given by the byte counter (C bus). The byte counter forms part of a synchronous loop which ensures that the correct descrambler byte is output by the EPROM.

### In lock indication LCK

LCK indicates that the system is in lock with the block structure. LCK is derived from SYN and CNT, when the byte counter is counting 2351 bytes between sync patterns (IC's 13,14).

### Header pulse HDR

HDR=1 indicates that the 4 header bytes are being loaded in the header register IC 19,20 and in RAM IC 22. ERD (Enable Read Data) =1 inhibits the refreshing of the header when the header is found.

<figure class="sheet" markdown>
[![Module W - data grabber and CPU](assets/web/cs-7-902-text-p156-preview.webp)](assets/web/cs-7-902-text-p156-zoom.webp)
<figcaption>
  Module W - data grabber and CPU.
  <span class="cs">CS 7 902</span>
  <span class="src">service manual page 156</span>
</figcaption>
</figure>

- DATA GRABBER DATA PROCESSING MODULE
- Wa

### Header register

Header bytes are loaded into the header register IC's 19,20 when HWE=0 (Header write enable). Header reading by the CPU is accomplished with HRE=0, IORD=0 and SEL4=0. The CPU can then determine if the header is from the desired data block.

### Byte counter

The byte counter uses 4 counters, IC's 31,32,36,38. It generates addresses for the descrambler EPROM and the RAM. The byte counter must be synchronised with the blocks. At the end of each sync pattern the counter is reset by SYN and so is rapidly pulled into lock. RDY indicates to the CPU that 3 blocks (3 x 2352) blocks are in the RAM.

### RDY (ready signal)

RDY informs the CPU that 3 blocks are in the RAM. RDY is generated when TCNT(Terminate count ) occurs ( 3 x 2352-1) from IC 35. The RDY circuit is built around IC's14,13 it is reset by RES.

### Read/write of header register and RAM

The read signal comes from the CPU. The write signal is DST2=0 for the ram, HDR for the header register.

### Status register

The CPU can read the status of the data grabber- port 34.

Table W4

| Bit | Signal | |
| --- | --- | --- |
| 0 | LCK | =1, Data grabber in lock |
| 1 | RDY | =1, Three blocks in RAM |
| 2 | HDR | =1, Header in register |
| 3 | ERR | =0, Error is present |
| 4-7 | Not used | |

The status register is a tri-state octal buffer IC 18. It is enabled when ENA=0. ENA is derived from SEL4 and IORD in IC 66.

### Processor control lines to data grabber

Table W5

| -MEMRD | Read RAM |
| --- | --- |
| -MEMWR | Write to RAM |
| -IORD | Read I/O ports |
| -ENA | Enable status register |
| -PRO4 | Chip select RAM 8000h - 9FFFh |
| -SEL4 | Chip select I/O ports 40h - 4Fh |

### I/O ports

Table W6

| -34h | Status register input |
| --- | --- |
| 34h | Control register output |
| 40h | Header register (Mins) |
| 41h | Header register (Secs) |
| 42h | Header register (Block) |
| 43h | Header register (Mode) |

### RAM (8k shared with CPU)

Table W7

| 8000h-8003h | Header block 1 |
| --- | --- |
| 8004h-8803h | Data block 1 |
| 8804h-8923h | CRC block 1 |
| 8924h-892Fh | Sync pattern block 2 |
| 8930h-8933h | Header block 2 |
| 8934h-9133h | Data block 2 |
| 9134h-9253h | CRC block 2 |
| 9254h-925Fh | Sync pattern block 3 |
| 9260h-9263h | Header block 3 |
| 9264h-9A63h | Data block 3 |
| 9A64h-9B83h | CRC block 3 |
| 9B84h-9B8Fh | Sync block 4 |

### Control register

Table W8

| Bit | Function |
| --- | --- |
| 1 | INTR=0 Reset interupt flip flops |
| 0 - 4 | Not used |
| 5 | RES=1 Reset LCK and RDY |
| 6 | ERD=1 Read header of first data block |
| 7 | ENW=1 CPU can write to RAM |

### Sequence to get data from the disc

Table W9

| 1 | Make RES=1 to reset |
| --- | --- |
| 2 | Wait for lock (LCK) |
| 3 | Wait for header |
| 4 | Make ERD=1 to read header when HDR arrives |
| 5 | Wait for ready signal (RDY) |
| 6 | Make ENW=1 |

<figure class="sheet" markdown>
[![Module W - header register / byte counter / RDY](assets/web/cs-7-903-text-p157-preview.webp)](assets/web/cs-7-903-text-p157-zoom.webp)
<figcaption>
  Module W - header register / byte counter / RDY.
  <span class="cs">CS 7 903</span>
  <span class="src">service manual page 157</span>
</figcaption>
</figure>

### CPU

The CPU section operates as the intelligent communications interface between the player and the host computer. It is built around a Z80A microprocessor and has 32k/bytes of ROM and 32k/bytes of RAM of which one 8k block is shared with the data grabber.

- Communication with the host computer is via a SCSI interface (Small Computer System Interface).
- Communication with the player is via a UART.
- Communications with the data grabber have been described.

An optional DMA controller for faster data transfer is catered for but this is not used in the VP415.

### Inputs to CPU

Commands in F-Code from host computer via SCSI.
Disc data from LV-ROM decoder via data grabber.
Acknowledgements from player via UART.

### Outputs of CPU

Disc dump data to host computer via SCSI.
F-Code commands to player via UART.

All three busses of the Z80A are buffered.
Address bus in IC's 44,45.
Data bus in IC 41.
Control bus in IC 40.

The RAM is arranged as 8kbyte blocks which are addressed by A0-A12. Selection of the desired block is by chip select lines -PR4 - -PR7 decoded from A13 - A15 in the 3 to 8 decoder IC56. The 3 to 8 decoder is enabled by -MREQ and gives active low outputs.

Chip enable of the ROM is by means of -PRO0 AND -PRO1 (IC 67).

### In/out port arrangement

The I/O ports are arranged in 8 blocks. Each block or device is allocated a chip select signal (-SEL0 - -SEL7) which is derived from 3 to 8 line decoder IC 57 using address lines A4 to A6. The decoder is enabled when the CPU is carrying out a machine port access (IOREQ=0) and A7=0.

The block identified by SEL3 is further divided into single bit I/O ports by decoding A0 - A3 in 3 to 8 line decoder IC 58 to give -SEL30 - -SEL37. This decoder is enabled by -SEL3.

### Read/write of I/O ports

When the Z80A accesses a machine port (I/O port) it does this by use of IOREQ with RD or WR. This separates I/O port access from memory access which uses MEMREQ and RD or WR.

### Single bit I/O ports

The input port is built around IC 53 and consists of 8 - D-TYPE flip flops. A word is loaded from the flip flops on the rising edge of the signal derived by ORing -SEL37 and -IORD.

Table W10

| Bit | Signal |
| --- | --- |
| 0 | ID0=1 interrupt from SCSI controller. |
| 1 | ID1=1 interrupt from DMA controller. |
| 2 | - |
| 3 | - |
| 4 | Baudrate=9600. |
| 5 | MON=0 Monitor enabled. |
| 6-7 | - |

The output port is built around IC 53 and consists of 8 D-TYPE flip flops. A word is loaded to the flip flops from the data bus when the device is selected (-SEL34) and the write pulse (-IOWR) occurs.

Table W11

| Bit | Signal |
| --- | --- |
| 0 | INTR=0 Resets the interrupt flip flops.(IC 59). |
| 1-4 | - |
| 5 | RES=1 Reset data grabber. |
| 6 | ERD=1 Enable read data. |
| 7 | ENW=1 CPU access to RAM (8000h-9FFFh). |

### Interrupt handling

The requirement is for two interrupt systems, one from the SCSI controller (INT0) and one from the DMA controller (-INT1). These two interrupts are combined in IC 67 and stored in J-K flip flop IC 59 to give an interrupt to the Z80A (-INT). IC 59 is reset when the interrupt has been serviced by -INTR from the output port IC 53.

<figure class="sheet" markdown>
[![Module W - CPU inputs and outputs](assets/web/cs-7-904-text-p158-preview.webp)](assets/web/cs-7-904-text-p158-zoom.webp)
<figcaption>
  Module W - CPU inputs and outputs.
  <span class="cs">CS 7 904</span>
  <span class="src">service manual page 158</span>
</figcaption>
</figure>

### System clock

The 8MHz crystal clock is built around IC 63. This is divided by 2 to give a 4MHz symmetrical clock for the Z80A, DMA and SCSI and a 4MHz two phase clock for the UPI-41.

### UPI-41

The UPI-41 is a slave processor based on the 8041 providing a half duplex UART for communications with the player part.

LV-DOS (LV-ROM, Data grabber, CPU) communicates with the player via the UPI-41 RS232 interface using F-Codes. The connector for this local UART interface is W4. The UPI-41 operates via 4 internal registers, input, output, control and status. The registers are addressed by A0 with -IORD or -IORW.

Table W12

| AO | -IORD | -IORW |
| --- | --- | --- |
| 0 | output | input |
| 1 | status | control |

### SCSI interface (Small Computer System Interface)

All communications with the SCSI bus are under the control of the SCSI controller (NCR-5385/6). The controller has 16 on-board registers and behaves as a dedicated microprocessor. The controller can operate in target or initiator mode but for the Domesday project only target mode is used.

- The SCSI registers
- Table W13

| port(h) | R/W | Function |
| --- | --- | --- |
| 00 | R/W | Data |
| 01 | R/W | Command |
| 02 | R/W | Control |
| 03 | R/W | Destination ID |
| 04 | R/W | Auxiliary status |
| 05 | R | ID. register |
| 06 | R | Interrupt register |
| 07 | R | Source ID |
| 09 | R | Diagnostic status |
| 0C | R/W | Transfer count (MSB) |
| 0D | R/W | ... (2nd byte) |
| 0E | R/W | ... (LSB) |
| 0F | R/W | Reserved |

### There are a number of connections with the CPU circuit

Table W14

| Signal | Pin | Function |
| --- | --- | --- |
| | 16 | 4MHz clock |
| RST | 4 | RST=1 resets the SCSI controller |
| D0-D7 | 1-3,43-47 | Data bus to Z80A |
| INT0 | 19 | Interrupt to Z80A as a result of various SCSI conditions |
| -IOWR | 30 | Active low write signal to place a byte in the SCSI |
| -IORD | 31 | Active low read pulse to read a byte from the SCSI |
| A0-A3 | 22-24,26 | Addresses for the 16 registers |
| RDY | 29 | Used when a DMA controller is fitted |
| -SEL0 | 21 | Chip select |
| -SEL30 | 27 | Data register enable used by DMA SEL30=0 resets RDY |

### SCSI bus interface

Since the SCSI controller can operate in initiator as well as target mode we must consider how this selection is made.

- Two control lines are used for this :-
- TGS (Target group select)
- IGS (Initiator group select)

The effect of these signals can be seen from the following table.

Table W15

| TGS | IGS | MSG | C/D | I/O | ATN | ACK | REQ |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 0 | 0 | IN | IN | IN | IN | IN | IN |
| 0 | 1 | IN | IN | IN | OUT | OUT | OUT |
| 1 | 0 | OUT | OUT | OUT | IN | IN | OUT |
| 1 | 1 | This is a forbidden condition | | | | | |

All inputs/outputs of the SCSI bus are terminated with 220 Ohm to +5V and 330 Ohm to ground.

### SCSI bus pin assignments

Table W16

| Signal | Pin | Signal | Pin |
| --- | --- | --- | --- |
| -DB0 | 2 | Ground | 28 |
| -DB1 | 4 | Ground | 30 |
| -DB2 | 6 | -ATN | 32 |
| -DB3 | 8 | Ground | 34 |
| -DB4 | 10 | -BSY | 36 |
| -DB5 | 12 | -ACK | 38 |
| -DB6 | 14 | -RST | 40 |
| -DB7 | 16 | -MSG | 42 |
| -DBP | 18 | -SEL | 44 |
| Ground | 20 | -C/D | 46 |
| Ground | 22 | -REQ | 48 |
| Ground | 24 | -I/O | 50 |
| +5V | 26 | | |

In addition all odd pins numbered below 25 are connected to ground.

### Indication of SCSI bus phase

### .Table W17

- MSG, C/D and I/O determine the bus phase
- MSG Message byte waiting
- C/D Control / Data byte
- I/O Input or output

In target mode these signals are all outputs (TGS=1). In this condition IC 71 is enabled for output and IC 70 is disabled for input.

### SCSI handshake lines in target mode

### Table W18

REQ informs the host computer that communications are required. ACK is the response from the host when it sees REQ. ATN informs the host that a message byte is required. BSY indicates that the device is busy.

### SCSI data bus buffers

The data bus of the SCSI controller is buffered between the controller and the in/out connector. Output buffer - IC's 75,76. Input buffer IC 77. The buffers are under the control of SBEN (pin20,SCSI). SBEN=0 - output, SBEN=1 - input.

<figure class="sheet" markdown>
[![Module W - system clock / UPI-41 / SCSI interface](assets/web/cs-7-905-text-p159-preview.webp)](assets/web/cs-7-905-text-p159-zoom.webp)
<figcaption>
  Module W - system clock / UPI-41 / SCSI interface.
  <span class="cs">CS 7 905</span>
  <span class="src">service manual page 159</span>
</figcaption>
</figure>

### Installation of target ID

There are eight possible ID's that can be selected for the target:-

The ID is selected by means of dip switch S1 Nos 5,6 and 7.

Table W19

| Dip switch setting | | | ID No. |
| --- | --- | --- | --- |
| 5 | 6 | 7 | |
| off | off | off | 0 Default |
| off | off | on | 1 |
| off | on | off | 2 |
| off | on | on | 3 |
| on | off | off | 4 |
| on | off | on | 5 |
| on | on | off | 6 |
| on | on | on | 7 |

### CPU memory map

The CPU is organised to handle a maximum of 32kBytes of ROM plus 32kBytes of RAM.

Table W20

| IC No. | Address (h) | Chip select |
| --- | --- | --- |
| 47 16k EPROM | 0000 - 3FFF | -PRO x -PR1 |
| 48 16k EPROM | 4000 - 7FFF | -PR2 x -PR3 |
| 22 8k RAM | 8000 - 9FFF | -PR4 (shared) |
| 49 8k RAM | A000 - BFFF | -PR5 |
| 50 8k RAM | C000 - DFFF | -PR6 |
| 51 8k RAM | E000 - FFFF | -PR7 |

### CPU port map

Table W21

| Port No. | IC No. | Chip sel. | I/O | Function |
| --- | --- | --- | --- | --- |
| 00 | 39 | -SEL0 | I/O | SCSI data |
| 01 | .. | .. | I/O | SCSI command |
| 02 | .. | .. | I/O | SCSI control |
| 03 | .. | .. | I/O | SCSI destination |
| 04 | .. | .. | I/O | SCSI aux. |
| 05 | .. | .. | In | SCSI ID. |
| 06 | .. | .. | In | SCSI interrupt |
| 07 | .. | .. | In | Source ID. |
| 09 | .. | .. | In | Diag. status |
| 0C | .. | .. | I/O | Count MSB |
| 0D | .. | .. | I/O | Count 2nd byte |
| 0E | .. | .. | I/O | Count LSB |
| 0F | .. | .. | I/O | Reserved - test |
| 10 | 43 | -SEL1 | I/O | DMA data/control |
| 20 | 52 | -SEL2 | I/O | UPI-41 data |
| 21 | 52 | .. | In | UPI-41 status |
| 21 | 52 | .. | Out | UPI-41 control |
| 34 | 18 | -SEL34 | In | Data grab status |
| 34 | 54 | -SEL34 | Out | Data grab control and interrupt reset |
| 37 | 53 | -SEL37 | Out | Read dip sw. and interrupt f/f's. |
| 40 | 19,20 | -SEL4 | In | Header Mins. |
| 41 | .. .. | .. | In | Header Secs. |
| 42 | .. .. | .. | In | Header Blocks. |
| 43 | .. .. | .. | In | Header Mode. |

### Dip switches on the CPU panel

- Dip switch S1.
- Table W22

| Switch | Purpose | |
| --- | --- | --- |
| 1 | Baudrate selection | Not used |
| 2 | Monitor test | Not used |
| 3-4 | Not used | |
| 5-7 | Target ID installation. | |

## Module X — LV-ROM decoder { #module-x }

*See also the [module X page](../modules/x-lv-rom-decoder/index.md).*

### Computer data on disc

LV-ROM data storage has a similar format to that used on the Compact Disc in that the basic word size is sixteen bits with a sample rate of 44,100 per second alternating left and right to give 176.4 kBytes/Sec.

The data is organised in blocks. Each block consists of 98 frames. Each frame contains 12 pairs of byte values (6 x DLCF, 6 x DRCF) ie. 24 bytes.

To allow synchronisation and identification each block commences with a sync pattern and header.

We can summarise a block as :

- Table X1
- 12 bytes sync
- 4 bytes header
- 2048 bytes data
- 8 bytes unused

280 bytes CRC (error detection and correction)

Total 2352 bytes

A block is read from the disc in 1/75th sec.

As the disc revolves at TV frame rate (25Hz) we may deduce that three blocks will be read during one revolution of the disc. Thus the position of any block on the disc can be obtained by dividing the block number by three to obtain the frame or picture number. The player accesses the disc in terms of frame number.

The encoding format on the disc uses a cross interleaved Reed Solomon code to give protection against reading errors caused by dust or scratches on the disc and each byte is represented by a 14 bit word. This process of modulation is termed EFM - Eight to Fourteen bit Modulation. An EFM word obeys the rule that there must be at least two and not more than ten '0's' between adjacent '1's'. Since this rule might be broken at the junction of two words three 'merging bits' are inserted between each pair of EFM words to ensure that the 2 - 10 rule is adhered to.

A 'Control and Display' word (and a synchronising pattern precede the data bytes in each frame. Two groups of parity bits each of 4 bytes complete the frame.

Over a block of 98 frames the C and D words are accumulated to provide a block label in terms of time.(Mins, Secs, 1/75 Secs)

Each frame therefore consists of

| Sync pattern | 24 bits |
| --- | --- |
| Control and display | 14 bits |
| Data (24 x 14) | 336 bits |
| Parity (8 x 14) | 112 bits |
| Merging (34 x 3) | 102 bits |
| Total bits | 588 bits |

In addition to the protection given by the CIRC (Cross interleaved Reed Solomon) coding further protection is provided by the 280 CRC bytes of each block.

The bit rate as read from the disc is 4.3218 Mbits/Sec. giving a decoded data rate of 153.6 kbytes/Sec.

### Data scrambling

There may be sections of data where a number of bytes have a similar value. This would have the effect of causing a DC offset (non-zero DSV) which could upset servo operation. To avoid this the data is modified by having a scrambling pattern superimposed. This scrambling must be unpicked in the player.

<figure class="sheet" markdown>
[![Module W - target ID / CPU memory map / port map](assets/web/cs-7-906-text-p160-preview.webp)](assets/web/cs-7-906-text-p160-zoom.webp)
<figcaption>
  Module W - target ID / CPU memory map / port map.
  <span class="cs">CS 7 906</span>
  <span class="src">service manual page 160</span>
</figcaption>
</figure>

### LV-ROM decoder

The LV-ROM decoder accepts the signal from module Z (HFOUT2). This signal is of sinusoidal form and carries digital data for the host computer.

The data rate is 4.3218 mbits/sec but owing to the protection overhead carried the useable data rate is 153.6 kbytes/sec.

The family of IC's used in the LV-ROM decoder is common to the Compact Disc system and so is organised to output data in 16 bit words on two channels.

Data is output in serial form as - left (DLCF) and right (DRCF) with appropriate timing signals - Bit clock (CLCF), Byte clock (STR2) and word clock (STR1). This latter references 16 bit values which are the basic units in Compact Disc.

In addition LV-ROM outputs error flags (ELCF, ERCF) to indicate if uncorrected errors remain in the data.

LV-ROM DECODER MODULE

### Circuit description

The incoming signal from the deck is amplified (Ts6701, 6702, 6703, 6706) to give the required input level (1vpp.) then applied to the input of DEMOD (DEMODulator) IC6501. The signal is also applied to the HF level detector (Ts6530, 6531, IC6508).

When the signal is of adequate amplitude HFL, from 6508.14 enables DEMOD. This occurs when the signal is greater than 0.65Vpp.

The functions of DEMOD are as follows :

- a) To regenerate a bit clock in synchronism with the bit rate from the disc.
- b) To demodulate the data. (On the disc each byte is represented as a 14 bit word.)
- c) To output the data with corresponding timing signals.

The bit clock is formed as a phase locked loop with varicap diode 6540 as the control element.

### Signals from DEMOD are

Table X2

| DADE | Data DEMOD to ERCO |
| --- | --- |
| FSDE | Frame sync DEMOD to ERCO |
| SSDE | Symbol (8 bit) sync DEMOD to ERCO |
| CLDE | Bit clock DEMOD to ERCO |
| CRI | Mutes ERCO if no data present |

ERCO provides de-interleaving of the data, error detection, and error correction of up to two error bits in any word.

De-interleaving is achieved by storing the data as recieved from DEMOD in buffer RAM 6502 then picking out in the correct order.

Uncorrected errors are flagged on pin 36 of ERCO as UNEC (UNcorrected errors ERCO to CIM).

The parity bits are discarded in ERCO.

### The signals from ERCO are

Table X3

| DAEC | Data ERCO to CIM |
| --- | --- |
| UNEC | Unreliable data ERCO to CIM |
| CLEC | Bit clock ERCO to CIM |
| FSEC | Frame sync ERCO to CIM |

CLOX is the master clock from CIM to ERCO which determines the rate at which data is read from RAM 6502.

CIM (Concealment, Interpolation and Muting) separates the data into left and right streams (DLCF, DRCF) and again provides the necessary timing signals STR1, STR2, CLCF (Bit clock).

There are other functions built into CIM for the Compact Disc system which are not used in this application.

### UNEC descrambler

The error flags from ERCO do not correspond in time with the data leaving CIM. To restore the correct time relationship a further SAA7000 (CIM) is used, IC6604.

IC6604 provides error flags for both data streams.

- Data- DLCF error flags ELCF.
- Data- DRCF error flags ERCF.

### Frequency of CLOX

In the Compact Disc application of this chip set the bit clock (DEMOD) runs in lock with the data from the disc which itself runs at a continually varying speed. CLOX determines the sample play rate and operates as a fixed frequency master clock. The disc is driven at a rate to maintain the contents of RAM 6512.

In this Laservision application the disc (CAV) is driven at a constant controlled speed which may be locked to an outside reference by Genlock.

CIOX therefore must run in sync with the data rate from the disc.

Provision is made to pull CLOX to the precise frequency by varicap diode 6606. The control voltage for 6606 is developed from MCES (motor control error signal from ERCO). MCES is a variable mark/space ratio signal. The mark/space ratio is determined in ERCO by the difference between the bit clock (CLDE) and CLOX. MCES is integrated by IC6602-2a and controls 6606 via 6602-2b. D6605 limits the excursions to protect 6606.

<figure class="sheet" markdown>
[![Module X - LV-ROM decoder](assets/web/cs-7-907-text-p161-preview.webp)](assets/web/cs-7-907-text-p161-zoom.webp)
<figcaption>
  Module X - LV-ROM decoder.
  <span class="cs">CS 7 907</span>
  <span class="src">service manual page 161</span>
</figcaption>
</figure>

## Module Y — Video mixing { #module-y }

*See also the [module Y page](../modules/y-video-mixer/index.md).*

The function of the mixer board is to allow selection of a variety of combinations of video from the disc and text/graphics from the host computer.

### The combinations available are

- Mode 1 Video from Laservision disc only.
- Mode 2 Signals from host computer only.

Mode 3 Enhanced mode - LV 100%, 57% in window.
(In mode 3 areas of the LV video may be highlighted by windows generated by a 'black' signal from the á computer. In a window the video will be displayed at REDUCED intensity.)

Mode 4 Mix mode - 62% LV + 38% computer.
(Transparent overlay.)

Mode 5 Hard key - 100% LV or 100% computer.
(Computer text/graphics inserted in LV video.)

Mode selection is performed by control signals VP0 - 2.
Video and computer signals are input as RGB drives.

### Description

As the board consists of three identical channels the following description will refer only to the red channel.
The board is built around a number of TCA240 transistor arrays, each termed a mixer. To simplify the description we will allocate each array a letter.

Consider the Red channel only.

| IC7151-2b | Mixer A |
| --- | --- |
| IC7152-2a | B |
| IC7152-2b | C |
| IC7153-2b | D |
| IC7153-2a | E |

VP0-2 are decoded in 7458

| Mode | VP2 | VP1 | VP0 | Q0 | Q1 | Q2 | Q3 | Q4 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | 0 | 0 | 0 | 1 | 0 | 0 | 0 | 0 |
| 2 | 0 | 0 | 1 | 0 | 1 | 0 | 0 | 0 |
| 3 | 0 | 1 | 0 | 0 | 0 | 1 | 0 | 0 |
| 4 | 0 | 1 | 1 | 0 | 0 | 0 | 1 | 0 |
| 5 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 1 |

The effects of the control signals on the mixers can be summarised as a table.

Mixer

| Output | Mode | A | B | C | D | E |
| --- | --- | --- | --- | --- | --- | --- |
| LV-disc | 1 | off | off | off | off | on |
| Computer | 2 | off | off | on | on | off |
| Enhanced | 3 | on | off | off | on | on |
| Mix | 4 | off | on | off | on | on |
| Hard key | 5 | off | off | on | on | on |

### From this table a number of assumptions can be made

a) Mixer A passes video from the LV-disc.
b) Mixer E passes video from the LV-disc.
c) Mixers B and C pass computer video.
d) Mixer D passes computer video.

By comparing this list with the list of modes we can also deduce that mixers B and C pass differing amounts of the computer signal.

- Mixer B - 38%
- Mixer C - 100%.

### Signal path - LV video modes 1, 3, 4 and 5

The video signal input at 9Y1 is applied to buffer/clamp 7151-2a.

During the line syncs (REFH, 1Y1) the level is clamped (7102, 7154). The signal exits 7151-2a at pin 12 to enter mixer 7151-2b pin 5. From this point the signal is also applied to mixer 71532a via R3134. The amplitude of the latter signal is determined by whether 7105 is on or off. 7105 is on in all modes except mode 3 (Reduced amplitude when 7105 is on). As mixer 7151-2b is off during modes 1, 4 and 5 the video signal will pass via 3134 and mixer 7153-2a. In mode 3 7151-2b is on to provide the signal path.

### Signal path - computer video

The computer video signal input at 1Y3 is buffered and inverted by 7451-3a and applied to input 1 of 7452-3a. Output 9 of 7454-2a is high when modes 1 or 3 are selected or the burst blanking signal CBL is high causing 7452-3a to block. 74523a therefore behaves as a switch. In mode 3, RGB drives from the computer are off. A window will be generated when NOT R or G or B is sent via 7455, 7456-4a, to control input 7 of mixer 7153-2b. Due to the cross coupling between mixers 7153-2a and 7153-2b the output level of 7153-2a will be reduced.

### Computer syncs

Owing to irregularities in the computer syncs these have to be restructured. Computer syncs (-CS) are applied to sync regenerator 7457 where they are regenerated and output as NS-CS (nonstandard composite syncs). When computer syncs are present the reference module (D) must be informed. The signal for this purpose is CS-S/NS. NS-CS and CS-S/NS are routed to module D via module U.

<figure class="sheet" markdown>
[![Module X - LV-ROM decoder (continued)](assets/web/cs-7-908-text-p162-preview.webp)](assets/web/cs-7-908-text-p162-zoom.webp)
<figcaption>
  Module X - LV-ROM decoder (continued).
  <span class="cs">CS 7 908</span>
  <span class="src">service manual page 162</span>
</figcaption>
</figure>

## Module Z — Deck electronics { #module-z }

*See also the [module Z page](../modules/z-deck-electronics/index.md).*

The Deck Electronics consist of the circuitry to process the signal from the LDU and the Active Tilt Control. The circuits are built on a PCB, situated under the optical deck chassis. The LDU is connected to this PCB by means of a flex-foil connection. For the block diagram of the LDU signal processing see Fig.Z1.

### Circuit description

### The laser supply

The Solid State laser is supplied by the +5V through a controllable DC amplifier. The laser emits part of the light to the optics and part to an internal monitor-diode. This diode measures the amount of light and feeds the monitor information back to amplifier T 7005 via T 7002, 7003. In this way, a constant current through the laser is realised. The monitor signal also drives switch T 7004, causing the LA-STA signal to go low when the laser has been switched on. This signal is fed to the drive processor module (R).

The signal LA switches, via T 7001, the controllable amplifier T 7005, thus the laser, on and off (LA low = off).

### The LDU signal processing

The LDU signal processing converts the signals from the photodiodes into drive signals to be processed further in the electronics of the player.

### - HF signal

The signals from photodiodes A, B, C and D contain the information of the pit pattern on the video disc, read out by the laser beam. The sum signal A + B + C + D is fed to the HF preamplifier via a highpass filter (>50kHz).

This amplifier delivers the HF-OUT1 and HF-OUT2 signals, both FM modulated by the disc info.

### - Radial signals

The radial fault signal on photodiodes R1 and R2 occurs when the laser spots are not exactly positioned on the tracks of the disc. In the servo preamplifier, the difference signal (R1-R2) represents the radial error signal RAD-ER. When the laser spot is exactly positioned on the track, a track position indication TPI is obtained from the servo preamp. The TPI signal is low when on track and high when the spot is off the track.

As soon as the TPI signal becomes high, the radial mirror in the LDU will be driven by the RAD-ER signal.

### The ATC circuit

The block diagram of the ATC circuit is shown in Fig.Z2. The signals of D1 and D2 are measured in IC 7204. Addition of the two signals gives a sign that a disc is present above the LDU. In this case DR (disc reflection) is high. Subtraction of the signals represents the error-signal (D1-D2), that is fed to the tilt loop switch T 7015. Signal TLS, coming from the Drive Module, is high when the ATC circuit has to become active (DR = high).

The tilt error signal is fed to amplifier IC 7206 which drives the tilt motor. As soon as the tilt motor voltage is within a range of + and - 0.5V, the TILTOK signal will be low, as a sign that the ATC is in a correct position.

### - Focus signals

The signals A, B, C and D are processed in the servo preamplifier to gain the focus error signal FOC-ER and the focus position indication FPI. Both signals drive the focus module (J) which focusses the objective onto the video disc.

The FOC-ER representing the deviation between objective and disc is composed by the difference signal (A+B) - (C+D).

The FPI signal is high when the objective is not focussed. As soon as focus is obtained, the FPI will go low and the objective is kept in focus by the FOC-ER signal.

<figure class="sheet" markdown>
[![Module Z - deck electronics / laser supply](assets/web/cs-7-873-text-p163-preview.webp)](assets/web/cs-7-873-text-p163-zoom.webp)
<figcaption>
  Module Z - deck electronics / laser supply.
  <span class="cs">CS 7 873</span>
  <span class="src">service manual page 163</span>
</figcaption>
</figure>
