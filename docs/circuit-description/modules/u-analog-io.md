---
title: Module U - Analogue I/O
description: >-
  All three parts of module U: Ua the CVBS and audio switching, Ub the
  luminance and chroma encoder, Uc the teletext source selection.
---

# Module U — Analogue I/O

*See also the [module U page](../../modules/u-analog-io/index.md).*

## Module Ua — Analogue I/O, CVBS + audio part { #module-ua }

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


*Fig. Ua2 ANALOG I/O MODULE Ub — see the sheet below.*

(AUDIO PART)

## Module Ub — Analogue I/O, video part { #module-ub }

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

## The manual sheets

<figure class="sheet" markdown>
[![Module Ua - analogue I/O CVBS + audio part](../assets/web/cs-7-899-text-p153-preview.webp)](../assets/web/cs-7-899-text-p153-zoom.webp)
<figcaption>
  Module Ua - analogue I/O CVBS + audio part.
  <span class="cs">CS 7 899</span>
  <span class="src">service manual page 153</span>
</figcaption>
</figure>

<figure class="sheet" markdown>
[![Module Ua - beep generator / Module Ub - analogue I/O video part](../assets/web/cs-7-900-text-p154-preview.webp)](../assets/web/cs-7-900-text-p154-zoom.webp)
<figcaption>
  Module Ua - beep generator / Module Ub - analogue I/O video part.
  <span class="cs">CS 7 900</span>
  <span class="src">service manual page 154</span>
</figcaption>
</figure>

<figure class="sheet" markdown>
[![Module Ub - chroma encoding / Module Uc - analogue I/O TXT part](../assets/web/cs-7-901-text-p155-preview.webp)](../assets/web/cs-7-901-text-p155-zoom.webp)
<figcaption>
  Module Ub - chroma encoding / Module Uc - analogue I/O TXT part.
  <span class="cs">CS 7 901</span>
  <span class="src">service manual page 155</span>
</figcaption>
</figure>
