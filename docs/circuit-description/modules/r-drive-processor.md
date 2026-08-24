---
title: Module R - Drive processor
description: >-
  Command input, slide control, Manchester code reading, display on screen,
  start-up, local control, A/V switching and service diagnostics.
---

# Module R — Drive processor

*See also the [module R page](../../modules/r-drive-processor/index.md).*

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

## sub a) Command input

Command inputs from and responses to module S go via the S-bus. The S-bus interface comprises ICs 7203, 7216, 7206, 7207. IC 7203 is a port expander by which processor IC 7201 accesses S-bus handshake signals DAV and DAK.

IC 7207 is the data input buffer latch. IC 7206 is the data output buffer latch.

DAV and DAK are serviced via D-type flip flops 7216-2A and 2B.

For detailed information on the operation of the S-bus please refer to the S-bus section.

## sub b) Control of the slide motor

Control of the slide motor takes place via software.

The slide motor is a stepping motor driven by the 4 phase signals COMM-1 - COMM-4 and SL-PWR which are output by port expander IC 7202.

During normal play functions the slide motor is driven when the deflection of the radial mirror is approaching its limit. This is determined by measuring the mirror offset by comparison of SP-POS (Radial error from mirror drive) with the output of DAC 7218 in IC 7210-2A. The result of this comparison (RAD-MIR) is applied to input pin 31 of port expander IC 7203.

## sub c) Reading Manchester codes

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

## sub d) Display on screen

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

## sub e) Start up and control

The start-up procedure has by means of a block diagram with command signals (Fig.CR1) and timing diagrams (Fig.CR2) been dealt with in chapter 2 sub 'Control routes + start-up sequence'. Here the interaction with the various modules is discussed.

The start-up sequence operates under control of processor IC 7201 via output buffers ICs 7213, 7214, 7215 and I/O port expanders 7202 and 7203. Buffers 7213 and 7214 operate with +12V supply so the input signals are first converted by level converter IC 7208. Buffer 7215 works directly with +5V supply. The start-up consists of the sequence : Close tray, move slide to start position, detect disc, activate the tilt control, put laser on, find focus, spin disc, close radial tracking loop, find picture no. 1.

During start-up it is determined which type of player we are dealing with (PAL or NTSC). This is done by determining the distance between successive VR pulses over a number of periods.

These VR pulses are the derivatives of the REFV pulses of ref. source module D. The measured period time is studied within certain limits (windows) and next the system is evaluated. If the VR signal is missing the player will not start up.

## sub f) Local control

The 'stand-by' and 'eject' keys on the front of the player give, if activated, a low level signal directly to I/O port expander IC 7203. The drive processor will respond to this.

## sub g) A/V switching

The drive processor sees to switching on and off of the audio and video signals, not only during start-up but also during normal play procedures. It is e.g. necessary to mute audio and video during search actions, realized with the AUDION, AUD2ON and CV/CS signals respectively. Or e.g. to switch over from internal source to external source if this is requested via control processor module S, realized with the A1-E/I, A2-E/I and CV-E/I signals, etc.

## sub h) Service diagnostics

The diagnostic software has been integrated in the drive software in such a way that many of the tasks of the drive are checked for proper performance. If a fault is detected in the execution of a task, an error code is shown on the screen as video overlay (like the index information). The software program is very useful on behalf of service diagnosis. The working and the use of this diagnosis software is dealt with extensively in the REPAIR METHOD description.

IC 7209 is a watchdog circuit which provides a reset for the processor on power up and also monitors the operation of the processor giving a reset if the program crashes.

## The manual sheet

<figure class="sheet sheet--fold" markdown>
[![Module P - frontloader / Module R - drive processor](../assets/web/cs-7-897-text-p151-preview.webp)](../assets/web/cs-7-897-text-p151-zoom.webp)
<figcaption>
  Module P - frontloader / Module R - drive processor.
  <span class="cs">CS 7 897</span>
  <span class="src">service manual page 151</span>
</figcaption>
</figure>
