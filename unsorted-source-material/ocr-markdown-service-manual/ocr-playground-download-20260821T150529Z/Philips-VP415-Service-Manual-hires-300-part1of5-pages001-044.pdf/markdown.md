LaserVision ROM disc drive VP415/00/05/35

# Service
Service
Service

![img-0.jpeg](img-0.jpeg)

![img-1.jpeg](img-1.jpeg)

# Service Manual

![img-2.jpeg](img-2.jpeg)

The VP415 is a professional Video Disc Drive for use in computerized audiovisual systems, involving a high degree of interactivity.

The Drive is suitable for playback of pre-recorded optical video discs, according to the LaserVision system (PAL standard) and it has the capacity to handle LV-ROM (LaserVision Read Only Memory) interactive discs.

# Contents:

Chapter 1 Technical data

Controls, indicators, connections

Connector pinning

Chapter 2 Remarks

Warnings

Modification levels

Adjustments

Demounting instructions

Service hints

Service tools

List of used symbols

Connections of semiconductors

# Caution

"Use of controls or adjustments or performance of procedures other than those specified here in may result in hazardous radiation exposure".

Safety regulations require that the set be restored to its original condition and that parts which are identical with those specified be used.

The differences between /00, /05 and/35 are only related to the ornamental plate on the front panel and to the mainscord.

Version /00 = LV-ROM Disc Drive with Euro mainscord.

/05 = BBC Domesday version with GB

mainscord

/35 = /00 with GB mainscord

Chapter 3 Module- and connector lay-out

Signal listing

Wiring diagram

Blockdiagram Control routes

Blockdiagram AUDIO/VIDEO signal path

Blockdiagram Servo

Chapter 4 Survey of modules

Modules A to Z

- Circuit diagram

- PCB lay-out

- Adjustments

- Electrical parts

Remote control

Chapter 5 Exploded view drawings

List of mechanical parts

List of electrical parts

Chapter 6 Repair method

Chapter 7 Circuit description

Chapter 8 Service Information

![img-3.jpeg](img-3.jpeg)

Documentation Technique Service Dokumentation Documentazione di Servizio Huolte-Ohje Manual de Servicio Manual de Servicio

Subject to modification

4822 726 14282

Printed in The Netherlands

© Copyright reserved

Published by

Service Consumer Electronics

CS 7 814

Technical data

Controls, indicators, connections

Connector pinning

Remarks

Warnings

Modification levels

Adjustments

Demounting instructions

Service hints

Service tools

List of used symbols

Connections of semiconductors

Module- and connector lay-out

Signal listing

Wiring diagram

Blockdiagram Control routes

Blockdiagram AUDIO/VIDEO signal path

Blockdiagram Servo

Survey of modules

Modules A to Z

- Circuit diagram

- PCB lay-out

- Adjustments

- Electrical parts

Remote control

Exploded view drawings

List of mechanical parts

List of electrical parts

Repair method

Circuit description

Service Information

# Chapter 1

# Chapter 2

# Chapter 3

# Chapter 4

# Chapter 5

# Chapter 6

# Chapter 7

# Chapter 8

Technical data

Controls, indicators, connections

Connector pinning

Chapter 1

# TECHNICAL DATA

# LASERVISION DISC

|  Disc diameter | 30 cm (12") or 20 cm (8")  |
| --- | --- |
|  Disc thickness | 2.7 mm (0.1")  |
|  Disc speed | CAV disc: 1500 r.p.m. CLV disc: 1500-570 r.p.m.  |
|  Maximum capacity (30 cm - 12" disc) | CAV disc: 54000 pictures per side LV-ROM disc (CAV): 324 Mbyte (max.) user data per side (in place of audio)  |
|  Max. playingtime | CAV disc: 36 minutes per side CLV disc: 1 hour per side  |
|  Average track pitch | 1.6-1.8 μm  |

# LASERVISION DISC DRIVE VP415

# General

|  Front loading motor-powered disc-tray  |   |
| --- | --- |
|  startup time | <13s  |
|  unload time (time between Eject command and disc out of player) | <15s  |
|  SSL (solid state laser)  |   |
|  Laser type | AIGaAs semiconductor  |
|  Wavelength | 780 nm  |
|  Aperture | 0.5  |
|  Output of laser | 3 - 5 mW  |
|  Random access time | CAV: max. 3s (≤1 s average) CLV: max. 15s (≤5 s average)  |
|  Instant jump | up to 50 frames (forward or reverse) within vertical interval time  |
|  On-board programming | Up to 16 picture number/chapter number segments  |

|  Program retention with no mains supply | at least 1 week  |
| --- | --- |
|  Mains voltage | 220-240 V (±10%) a.c.  |
|  Mains frequency | 50 to 60 Hz  |
|  Power consumption | 60 W approx.  |
|  Electrical safety | acc. to IEC 65  |
|  operational conditions | 10 to 35 °C  |
|  Rel. humidity | 20-80%  |
|  storage conditions | -40 to 70 °C  |
|  Rel. humidity | 10-95%  |

|  Dimensions | 420x160x400mm  |
| --- | --- |
|  disc-tray open | 420x160x740mm  |
|  Weight | 15 kg (approx.)  |

|  TV system | 625/50 PAL  |
| --- | --- |
|  Video |   |
|  CVBS input (BNC) | 1 V into 75 Ω, loop-through  |
|  CVBS output (BNC) | 1 V into 75 Ω  |
|  CVBS output (Euroconnector pin 19) | 1 V into 75 Ω  |
|  RGB output (Euroconnector) |   |

|  R (pin 15) | 0.7 V into 75 Ω  |
| --- | --- |
|  G (pin 11) | 0.7 V into 75 Ω  |
|  B (pin 7) | 0.7 V into 75 Ω  |
|  Video bandwidth | RGB: 5 MHz (-3dB) CVBS: 3 MHz (-3 dB), encoded  |

# Video

|  CVBS input (BNC) | 1 V into 75 Ω, loop-through  |
| --- | --- |
|  CVBS output (BNC) | 1 V into 75 Ω  |
|  CVBS output (Euroconnector pin 19) | 1 V into 75 Ω  |
|  RGB output (Euroconnector) |   |
|  R (pin 15) | 0.7 V into 75 Ω  |
|  G (pin 11) | 0.7 V into 75 Ω  |
|  B (pin 7) | 0.7 V into 75 Ω  |
|  Video bandwidth | RGB: 5 MHz (-3dB) CVBS: 3 MHz (-3 dB), encoded  |

|  Signal-to-noise ratio | 40 dB typ. unweighted (disc dependent)  |
| --- | --- |
|   | 50 dB typ. weighted (disc dependent)  |
|  Timebase instability | less than 10ns (normal play)  |

# Audio

|  Audio input (cinch) | 3 Vpp (load 47 k)  |
| --- | --- |
|  Audio output (cinch) | 650 mV r.m.s. into 1k (max. deviation)  |
|  Audio output (Euroconnector pins 1 & 3) | 650 mV r.m.s. into 1 k  |
|  Audio bandwidth | 40-20 000 Hz  |
|  Signal-to noise ratio | ≥ 50 dB typ. weighted (disc dependent)  |
|  Channel separation | better than 55 dB  |

# Genlock

|  Sync input (BNC) | 0.3-2.0 Vpp 75Ω, loop-though (wavefrom acc. to CCIR standards)  |
| --- | --- |
|  Sync input (DIN pin 4) | line freq. 15 625 Hz ± 100 ppm field freq. 50 Hz locked to line freq., interlaced, with or without equalising pulses, negative-going, logic 0:0-1 V, logic 1:2.2-4.2 V  |
|  Sync output (BNC) | 2.0 Vpp 75 Ω, negative-going  |
|  Genlock lock-in time | 5s  |

# Video mixer

|  RGB mixing/keying modes:  |
| --- |
|  Player RGB only  |
|  Computer output RGB only  |
|  Mixed mode: player 62%, computer 38%  |
|  Key mode: player 100%, computer 100%  |
|  Enhanced mode: Player 57%/100%  |

# LV-ROM

|  User data capacity | Max. 324 Mbyte per disc side  |
| --- | --- |
|  User data per frame | 6 kbyte  |
|  User data transfer rate from disc | 150 kbyte/s (depending on computer)  |
|  Data integrity (error rate) | ≤10⁻¹⁶  |
|  Internal C.P.U. | 4X6 kbyte cache memory for user data  |
|  System | compatible with floppy disc and hard disc systems  |

CS 7 816

# CONTROLS, INDICATORS AND CONNECTIONS

![img-4.jpeg](img-4.jpeg)

![img-5.jpeg](img-5.jpeg)

# Front

EJECT button

STANDBY indicator

ON/STANDBY button

EJECT indicator

PAUSE indicator

REPLAY indicator

REPEAT indicator

AUDIO 1 indicator

AUDIO 2 indicator

CAV indicator

CLV indicator

REMOTE CONTROL indicator

# Rear

1 ON/OFF switch
2 MAINS lead socket
3 REPLAY on/of switch
4 RC IR/EURO switch
5 WIRED RC socket
6 RS232C socket
7 BAUD RATE dip switches
8 AUDIO IN (1&2) sockets
9 AUDIO OUT (1&2) sockets
10 A/V EUROCONNECTOR
11 H-SHIFT control [for Genlock]
12 CVBS OUT socket
13 SYNC OUT socket
14 CVBS IN socket
15 SYNC IN sockets
16 RGB (TTL) IN socket
17 SCSI address dip switches
18 SCSI socket

# Remote control functions

- Play forward/reverse
- Still frame/step forward/reverse
Audio 1/2 on/off
Picture number/time display on/off
Chapter number display on/off
Programme display on/off
Search forward/reverse (20 times normal speed)
- Goto (Picture or Chapter number)
Input correction
- Digits 0-9 entry
- Fast forward/reverse (3,10,20 x normal speed)
- Slow forward/reverse (1/100 to normal speed)
- Fast/slow rate \(+ / -\)
- Clear memory
- Enter
- Standby
- Pause
- Start/Repeat
- Next

CS 7 817

# A/V Euroconnector

# Pin signal

1 audio out (right) 650 mV rms/1k
2 not connected
3 audio out (left) 650 mV rms/1k
4 audio earth
5 blue earth
6 not connected
7 blue out \(700\mathrm{mV} / 75\Omega\)
8 player status (player in standby: 2 V, player on : 12 V)
9 green earth
10 not connected
11 green out \(700\mathrm{mV} / 75\Omega\)
12 not connected
13 red earth
14 earth
15 red out \(700\mathrm{mV} / 75\Omega\)
16 fast blanking: 2.5 V into 75 Ω (RGB status)
17 CVBS earth
18 RGB status earth
19 CVBS out 1 V/75 Ω (also ects as sync out when using RGB)
20 not connected
21 socket earth

# RGB (TTL) IN socket (DIN)

6-pole female connector, 270 degrees

# pin

1 Red signal
2 Green signal
3 Blue signal
4 Composite sync
5 Ground
6 Not connected

(logic 0:0 -1 V, logic 1:2.2. -4.2 V. Sync instability better than +/- 100 pm, interlaced, with or without equalising pulses, negative going.)

# RS232-C interface

Serial computer interface, in accordance with international communication standards.

Full duplex

8 data bits, 1 stop bit, no parity

Data transmission speed may be set to 1200/2400/4800/9600 baud according to the positions of the two baud rate dip switches (numbers 1 and 2) at the rear of the player.

|  Baud rate | switch 1 | switch 2  |
| --- | --- | --- |
|  1200 | UP | UP  |
|  2400 | UP | DOWN  |
|  4800 | DOWN | UP  |
|  9600 | DOWN | DOWN  |

The player is fitted with a 25-pole female D-connector with the following pin connections:

# pin signal

2 (TxD) transmitted data from player to computer
3 (RxD) received data from computer to player
5 (CTS) clear to send: a signal from computer to player indicating the computer is ready to receive data \((\geqslant +3\) V means O.K. to transmit)
7 (GND) logic ground
9 +12 V/100 mA
10 -12 V/10 mA
20 (DTR) data terminal ready: a signal from player to computer indicating that player is ready to receive data \((\geqslant +3\) V means O.K. for data)

# SCSI interface

A computer interface in accordance with SCSI standards. The player is fitted with a 50-pole unshielded connector consisting of two rows of 25 male pins on 100 mil centres.

Single-ended cable pin assignments:

# pin signal

2 -DB(0)
4 -DB(1)
6 -DB(2)
8 -DB(3)
10 -DB(4)
12 -DB(5)
14 -DB(6)
16 -DB(7)
18 -DB(P)
20 GROUND
22 GROUND
24 GROUND
26 *TERMPWR (not connected to internal power supply)
28 GROUND
30 GROUND
32 -ATN
34 GROUND
36 -BSY
38 -ACK
40 -RST
42 -MSG
44 -SEL
46 -C/D
48 -REQ
50 -I/O

# Notes

All odd pins except pin 25 are connected to ground. Pin 25 should be left open, but may be connected to ground.

A minus sign indicates active low.

Maximum cable length is 6 m.

Address dip switches at rear of player. Dip switch in up position = OFF. Switches 1-4 and switch 8 should be OFF. Switches 5-7 determine the SCSI bus address of the player as follows:

|  address | switch 5 | switch 6 | switch 7  |
| --- | --- | --- | --- |
|  0 | OFF | OFF | OFF  |
|  1 | OFF | OFF | ON  |
|  2 | OFF | ON | OFF  |
|  3 | OFF | ON | ON  |
|  4 | ON | OFF | OFF  |
|  5 | ON | OFF | ON  |
|  6 | ON | ON | OFF  |
|  7 | ON | ON | ON  |

(Factory setting: address 0)

Termination according to SCSI: 330 Ω TO +5 V
220 Ω to 0 V

If you have more than one device connected to the host computer via the SCSI bus, the SCSI bus termination in the player has to be altered.

For details see* note in diagram of LV-ROM Interface Module Wb.

CS 7 828

Remarks

Warnings

Modification levels

Adjustments

Demounting instructions

Service hints

Service tools

List of used symbols

Connections of semiconductors

Chapter 2

# REMARKS

# 1. Care of the disc drive

The disc drive requires no special maintenance.
It is, however, recommended to clean the objective
lens from time to time with a piece of wadding, dipped
in alcohol.

# 2. Set-up of the Service Manual

The set is composed of various modules (A through
Z). The circuit diagrams, PCB layouts and parts lists
have also been classified per module.

# a) Circuit diagrams

Of each module a functional circuit diagram has been
given, with the incoming signals drawn as much as
possible at the left-hand side and the outgoing
signals at the right-hand side. Each incoming and
outgoing signal has a unique name, the meaning of
which can be read in the Signal listing.

If a signal enters or leaves the module, this takes
place via a connector (e.g. 6B2 = pin 6 of connector
B2) and via a letter indication in the line. This
indication mentions to which module the line is
connected.

If the letter indication in the line is the same as the
module on which the signal is present, the signal
remains on the module mentioned and, naturally, no
connector is drawn.

# b) Oscillograms and voltages in the circuit diagrams

- The oscillograms in the diagrams have been
measured with a dual-beam scope with Delayed
Timebase PM3214. The set has been connected to
a monitor by means of a SCART cable

Video : still picture, picture number 5530
(EBU colour bar, 75% saturation)

Audio 1: normal play, picture numbers 6200 - 6500,
1 kHz modulation

Audio 2: normal play, picture numbers 6500 - 6900,
1 kHz modulation

- The DC voltages have been measured with a
Digital Multimeter PM2524, still picture, picture
number 5530, unless stated otherwise.

# c) PCB layouts

Most modules in the set have been equipped with
doublesided copper pattern and plated-through holes.
For each module a PCB layout is drawn, consisting of
a drawing of the component side and of the soldering
side (chip side) with corresponding copper pattern.

# d) Parts lists

For each module an electrical parts list is given,
stating the service code numbers of the specific
electrical components that have been applied on
the module.

The code numbers of the standard components
(ICs, transistors, diodes, standard resistors, etc.)
have been placed on a collective list in Chapter 5.

# e) Service code numbers of the modules

In this Service Manual service code numbers for
the modules have not been mentioned. Please
consult you parts supplier.

# 3. Repair on modules

To enable repair/adjustment on modules use can be
made of extension PCBs or extension cables. A
survey can be found sub Service Tools in this chapter.

# 4. Hidden switches

On Analog I/O module U two switches have been
applied, hidden for the user.

The function of these switches is :

SK1 : +11V or RC5 signal at pin 8 of the Euro
connector.
Factory adjustment is RC5 at pin 8 (switch
pressed out).

SK2 : ENCODED CVBS or NOT ENCODED CVBS
signal on CVBS OUT connector BNC3. The
factory adjustment is ENCODED (switch
pressed out).

Please consult the circuit diagram of Analog I/O
module U for more details on these switches.

# 5. The optical deck

The optical deck in the disc drive is composed of
various critical components and at the production
department adjusted by complicated alignment
equipment.

For the time being repair of the Deck Electronics and
of the Laser Detection Unit by a service technician is
not allowed.

If a failure analysis reveals that the Deck Electronics
or LDU are defective, the entire deck should be
submitted for repair to the production centre via the
Central Repair Procedure of the Concern Service
Centre. Please inquire at your parts supplier's for this
procedure.

Repairs on the slide drive assy and the Automatic Tilt
Control (ATC) assy are possible. See the List of
mechanical parts for the correct code numbers.

# 6. Coding of items

The coding of component items in the service printing
of the PCB's can differ from the coding of the items in
the circuit diagrams (except supply module T). On the
PCB's, a letter/number coding has been used (e.g. R1,
C1) and in the diagram a 4 number coding (e.g.
3001,2001). The table below shows the conversion
between both coding systems.

Circuit diagram

4 number coding

Service printing on PCB

letter/number coding

![img-6.jpeg](img-6.jpeg)

![img-7.jpeg](img-7.jpeg)

1 = Unit, battery

2 = capacitor

3 = resistor

5 = coil, trafo, cristal

6 = diode

7 = transistor, IC

= U

= C

= R

= S,L,K

= D

= T,TS,I,IC

CS 7 818

# WARNINGS

# 1. Laser radiation

The Laser Detection Unit (LDU) in the optical deck has been equipped with a semiconductor laser. This laser emits invisible light which is focussed on the disc by the objective.

If the objective would be removed in case of repair, the laser light exits from the objective aperture. Avoid looking directly into the laser beam, as this might cause permanent injury to the eye.

# 2. Replacement of modules

Before replacing a module upon repair, first the mains switch should be switched off. This should be done to prevent damage to the circuits on the modules.

# 3. Service position of the set

If measurements or repair require that the set is placed on its side (90° position), this may only be done when a 6" test disc is played on the optical deck and the front loader has been removed. If a disc with a larger diameter is used (8" or 12"), the risk that the disc will come loose from the turntable (motor) and cause injury to people in the vicinity will be too great. Also ensure that the disc is always locked on the turntable by the magnetic disc clamping piece (see service tools).

In the above-mentioned 90° position of the set not all signals will be present according to specification. Adjustments and checks for correct functioning are therefore only allowed in the horizontal position of the set.

# 4. The 6" test disc

The 6" test disc may only be played when the front loader has been removed. With mounted front loader playback of 8" and 12" discs is possible.

CS 7.819

# MODIFICATION LEVELS

In the entire set various modification levels have been indicated.

# 1. Modification level of the set

The modification level of the set can be found at the rear of the cabinet.

a) Change code on the type number plate

Under the type number a letter and digit code is given which looks as follows :

![img-8.jpeg](img-8.jpeg)

The change code is preceded by the production centre.

b) Modification level on yellow sticker

On a yellow sticker a TM code is marked, indicating the modification level, in this case TM3.

![img-9.jpeg](img-9.jpeg)

# 2. Modification level of the module

In the circuit diagram: top right, under the name of the module (e.g. MOD LEVEL 3).

On the PCB: in the service printing at the component side

( e.g. X2345678901).

The modification level is marked then.

# 3. Modification level of the software in the EPROMs

On various modules EPROMs have been applied, that have been programmed (see survey below).

|  module | item number | name | program number  |
| --- | --- | --- | --- |
|  Drive Proc (R) | 7204 | DRIVE | 3104 103 6803.4  |
|  Control (S) | 7202 | CONTROL | 3104 103 6804.4  |
|  *CPU (W) | 7201 | SYNC | 3104 103 6808.0  |
|  *CPU (W) | 7224 | DESCR. | 3104 103 6807.0  |
|  *CPU (W) | 7247 | LV DOS #1 | 3104 103 6805.2  |
|  *CPU (W) | 7248 | LV DOS #2 | 3104 103 6806.2  |

*= only for VP415

The program number of the software has been applied on a sticker on the EPROM.

The modification level of the software is the last digit of the program number (behind the dot).

The modification level of the software in the Drive and Control EPROMs can also be retrieved by means of an external computer. To achieve this an F-code command "?=" should be sent to the disc drive (see the directions for use, chapter F-CODE COMMANDS : Revision level request).

The feedback of the disc drive is a 5-digit code of the software revision.

Digit 1 = 0

Digit 2 = major level drive

Digit 3 = minor level drive

Digit 4 = major level control

Digit 5 = minor level control

The modification level of the Drive software will then e.g. be 1.5 (digit 2 . digit 3) and of the Control software e.g. 1.4 (digit 4 . digit 5).

The relation with the modification level in the program number is as follows:

|   | mod. level progr. number | mod. level software revision  |
| --- | --- | --- |
|  Drive | 3104 103 6803.4 | 1.5  |
|  Control | 3104 103 6804.4 | 1.4  |

Each time a change takes place in the software, the modification level will by raised by one.

A survey of the modification levels of the set, the modules and the software can be found in the Service Information, chapter 8.

CS 7.820

# ADJUSTMENTS

# 1. General

For each module an adjustment procedure is given for components that are replaced during repair.

If an entire module is replaced, in principle adjustment should not take place, with the exception of HF PROC module K, VIDEO DO CORR module L and ANALOG I/O module U.

Module K : in case of replacement, adjust R3043 (video ampl.)

Module L : in case of replacement, adjust R3050 (MTF)

Module U : in case of replacement, adjust R3305 (R-Y gain) and R3315 (B-Y gain).

Module B : in case of replacement, adjust R3305 and R3315 on Analog I/O module U.

When module H, K, L or Z is replaced, it is advisable to check the CVBS OUT signal (NOT ENCODED) on BNC3 for correct amplitude and correct VITS signals MBI and MBIV. The CVBS OUT signal is described in adjustment 1 of Ananlog I/O module U.

The VITS signals are described in adjustment 2 of Video D.O. Corr. module L.

For amplitude adjustments see Fig 2.1

The adjustments take place without connection of a computer (video overlay) or external video source, unless stated otherwise.

# 2. Required

To perform the adjustments the following equipment is required:

Test disc 6" or 8"
- Dual-beam scope with Delayed Timebase If available: - vector scope or

- dual-beam scope with X-deflection via B-channel (e.g. PM3226P)

- Scope probes with 1:10 attenuator, preferable FET probes or probes with a capacitance \(< 3\mathrm{pF}\)
- BNC 75Ω terminator (4822 263 60037).

CS 7 821

# VIDEO ADJUSTMENTS

![img-10.jpeg](img-10.jpeg)

Fig. 21

CS 7 822

DEMOUNTING INSTRUCTIONS

![img-11.jpeg](img-11.jpeg)

PUSHING OUT THE DISC TRAY

![img-12.jpeg](img-12.jpeg)

DEMOUNTING UPPERCASET AND FRONTLOADER

Xcrews dot marked

![img-13.jpeg](img-13.jpeg)

DEMOUNTING OPTICAL DECK

![img-14.jpeg](img-14.jpeg)

DEMOUNTING DISC TRAY ASSY

![img-15.jpeg](img-15.jpeg)

MOUNTING DISC TRAY ASSY

![img-16.jpeg](img-16.jpeg)

DEMOUNTING ANALOG I/O MODULE U

![img-17.jpeg](img-17.jpeg)

REMOVING SPEEDNUT

![img-18.jpeg](img-18.jpeg)

ONLY FOR VP415:

DEMOUNTING SANDWICH PART

EVA.00317

T28/710

CS 7 823

# SERVICE HINTS

# WARNING

# ESD

All ICs and many other semi-conductors are susceptible to electrostatic discharges (ESD).

Careless handling during repair can reduce life drastically.

When repairing, make sure that you are connected with the same potential as the mass of the set via a wrist wrap with resistance.

Keep components and tools also at this potential.

The photodiodes and the laser are more sensitive to electrostatic discharges than MOS IC's.

Careless handling during servicing may reduce life expectancy drastically.

For this reason care should be taken that during servicing the potentials of the tools and yourself are equal to that of the screening of the set

# Chip components (SMD)

Chip components have been applied in the set. For the insertion and removal of chip components see the figure below.

![img-19.jpeg](img-19.jpeg)

![img-20.jpeg](img-20.jpeg)

![img-21.jpeg](img-21.jpeg)

27 012C12

CS 7 824

SERVICE TOOLS

![img-22.jpeg](img-22.jpeg)

CS 7 825

APPLICATION OF SERVICE TOOLS

![img-23.jpeg](img-23.jpeg)

![img-24.jpeg](img-24.jpeg)

CS 7 826

# LIST OF USED SYMBOLS

Safety resistor

Veiligheidsweerstand

Sicherheitswiderstand

Résistance de sécurité

0.2 W ≤ 220 kΩ - 5%

(CR16) > 270 kΩ - 10%

0.33 W < 1 MΩ - 5%

(SFR25) > 1 MΩ - 10%

0.5 W ≤ 1 MΩ - 5%

(CR37) > 1 MΩ - 10%

0.33 W - MR25 - 1%

0.5 W ≤ 1 MΩ - 5%

(CR32) > 1 MΩ - 10%

1 W ≤ 1.6 MΩ - 5%

(CR68) > 1.6 MΩ - 10%

0.5 W High voltage resistor

(VR37) Hoogspanningsweerstand

Hochspannungswiderstand

Résistance haute tension

Safety capacitor

Veiligheidscondensator

Sicherheitskondensator

Condensateur de sécurité

Ceramic plate capacitor

Keramische plasticonductor

Keramischer Platten-Kondensator

Condensateur céramique plaquette

Metalized polyester flat film capacitor

Gametalliseerde polyester condensator

Metalliserter Polyester-Flachkondensator

Condensateur plat à feuille de polyester

métallisée

Miniature électrolytic capacitor

Miniatuur electrolytische condensator

Miniatur-Elektrolytkondensator

Condensateur électrolytique miniature

|  a = 2.5 V | g = 40 V | r = 250 V  |
| --- | --- | --- |
|  b = 4 V | h = 63 V | s = 350 V  |
|  c = 6.3 V | j = 100 V | u = 400 V  |
|  d = 10 V | l = 125 V | v = 500 V  |
|  e = 16 V | m = 150 V | w = 630 V  |
|  f = 25 V | q = 200 V | x = 1000 V  |
|   |  | y = 1600 V  |

Sewtooth pulse converter

Zaagtend-puls omzetter

Sägezahn Impulsumformer

Convertisseur d'impulsions en dents de scie

Pulse-code modulation (6-unit binary code)

Puls code modulatie (6 bits code)

Impulscode-Modulation (6 Bits-code)

Modulation code d'impulsions (code 6 bits)

Puls-duration modulation

Pulsiengte modulatie

Impulslänge-Modulation

Modulation de durée d'impulsion

Sync separator

Sync scheider

Sync-Trenner

Séparateur sync

FM detector

FM detector

FM-Detektor

Détecteur FM

Phase discriminator

Fasediscriminator

Phasenvergleich

Discriminateur de phase

Detector

Detector

Detektor

Détecteur

Level detector

Niveau detector

Niveau-Detektor

Détecteur de niveau

Phase-changing network

Faseverschuiver

Phasenverschiebung

Circuit de déphasage

Rejection filter

Bandspelfilter

Bandsperefilter

Filtre de suppression

Bandpass filter

Band-doorlatend filter

Bandpassfilter

Filtre passe-bande

Low-pass filter

Laag-doorlatend filter

Tierpassfilter

Filtre passe-bas

Mixer stage

Mengtrap

Mischstufe

Etage mélangeur

High-pass filter

Hoog-doorlatend filter

Hochpassfilter

Filtre passe-haut

HF generator

HF generator

HF-Generator

Générateur HF

Sewtooth generator

Zaagtendgenerator

Sägezahngenerator

Générateur en dents de scie

Square wave generator

Putagenerator

Rechteckgenerator

Générateur d'impulsions

rectangulaires

Delay element

Vertragingselement

Verzögerungselement

Élément à retard

Limiter

Begrenzer

Begrenzer

Limiteur

Positive-going step function

Positive flank

Übergang von tief zu hoch

Fonction de palier en sens positif

Négative-going step function

Negatieve flank

Übergang von hoch zu tief

Fonction de palier en sens négatif

Emitter follower

Emitter volger

Emitter folger

Ematteur suiveur

Automatically controlled amplifier

Automatisch gestuurde versterker

Automatisch gesteuerter Verstärker

Amplificateur à commande automatique

Mixer stage

Mengtrap

Mischstufe

Etage mélangeur

Amplifier

Versterker

Verstärker

Ampli

Differential amplifier

Verschilversterker

Differentialverstärker

Ampli différentiel

Amplifier with open output

Versterker met open uitgang

Verstärker mit offenem ausgang

Ampli a sortie ouverte

Electronic switch

Electronische schakelaar

Elektronische Schalter

Commutateur électronique

Electronic switch

Electronische schakelaar

Elektronischer Schalter

Commutateur électronique

Common control block

Gemeenschappelijk controleblok

Gemeinschaftlicher Kontrollablock

Bloc de contrôle commun

SRG

Shift register

Schult register

Schieberegister

Registre à décalage

Q

Output

Uitgang

Ausgang

Sortie

◇

Open collector output

Open kollektor uitgang

Offenen Kollektor ausgang

Sortie collecteur ouvert

G

Command input

Kommando ingang

Kommando eingang

Entrée ordres

CE

Chip enable input

Chip enable ingang

Chip enable singing

Entrée chip validation

00

Bidirectional

Tweezijdig gevoelig

Doppeteelig empfindlich

Bidirectional

Inverter

Inverter

Inverter

Invertisseur

Cir gate

Cli-poort

Oder

Porte ou

Nor gate

"Nor"

"Nor"

Porte Non-ou

And gate

En-poort

Und Gatter

Porte El

Nand gate

"Nand"

"Nand"

Porte "Non-El"

Buffer

Buffer

Puffer

Tampon

Inverting buffer

Inverterende buffer

Inverterender puffer

Tampon invertisseur

Buffer with open output

Buffer met open uitgang

Puffer mit offenem ausgang

Tampon à sortie ouverte

CS 7 827

Module- and connector lay-out

Signal listing

Wiring diagram

Blockdiagram Control routes

Blockdiagram AUDIO/VIDEO signal path

Blockdiagram Servo

Chapter 3

MODULE AND CONNECTOR LAY OUT

![img-25.jpeg](img-25.jpeg)

![img-26.jpeg](img-26.jpeg)

PMS 8/77/1
TBR 1911

CS 7 829

# ALPHABETICAL SIGNAL LISTING

|  -(B-Y) | Colour difference B-Y |  | DLCF | Data left CIM to FIL |   |
| --- | --- | --- | --- | --- | --- |
|  -(R-Y) | Colour difference R-Y |  | DLEN | P-bus data line enable | +5V = active  |
|  +12 | Switched +12V |  | DO-INH | Dropout protection inhibit | +12V = active  |
|  +125B | +12V standby supply |  | DR | Disc reflection | +5V = refi  |
|  +5 | Switched +5V |  | DRCF | Data right CIM to FIL |   |
|  +55B | +5V standby supply |  | DTR | Data terminal ready (RS232) |   |
|  D-RPM | 5 RPM status | 0V = 0 RPM | DTR 3 | DTR |   |
|  -12 | Switched -12V |  | DTR 1 | DTR |   |
|  -125B | -12V standby supply |  | DTR 2 | DTR |   |
|  2-PPR | 2 pulses per revolution | pos.pulses | DUMP | Dump on/off switch | 0V = dump on  |
|  400Hz PAL | PAL switching signal |  | DUMP-ON | Data dump on/off | +12V = on  |
|  -55B | -5V standby supply |  | EJECT | Eject button | 0V = active  |
|  80-FH | 80 times horizontal freq. |  | ELCF | Error flag left |   |
|  A1-E/J | Audio 1 internal/external | +12V = ext | ERCF | Error flag right |   |
|  A2-E/J | Audio 2 internal/external | +12V = ext | ER-DIS | Error display | 0V = active  |
|  ALE | Address latch enable |  | EXT AUD 1 | External audio 1 |   |
|  A-SYNT | Synthesised audio on/off | +12V = on | EXT AUD 2 | External audio 2 |   |
|  ATN | Attention | 0V = active | FAS-REL | Phase relation |   |
|  AUD1 | Audio 1 |  | FI | Field identification |   |
|  AUD1+2 | Audio 1 + audio 2 |  | FOCACT | Focus actuator drive signal |   |
|  AUD1CN | Audio 1 on/off | +12V = on | FOC-EN | Focus enable | +12V = enable  |
|  AUD2 | Audio 2 |  | FOC-ER | Focus error |   |
|  AUD2DN | Audio 2 on/off | +12V = on | FOC-IND | In focus indication | 0V = in focus  |
|  B | Blue video signal |  | FR | Focus position indication | -12V = in position  |
|  BF | Burst flag | pos.pulses | FRLOCK | Frame lock | +5V = in lock  |
|  B-MIX | Blue video signal from mixer |  | FGDE | Frame sync DEMOD to ERCO |   |
|  BP-CLP | Bypass clamp | pos.pulses | FSEC | Frame sync ERCO to CIM |   |
|  BRA | Baudrale select A | 0V / +5V | G | Green video signal |   |
|  BRB | Baudrale select B | 0V / +5V | GLC | Genlock clock (4.5MHz) |   |
|  B-TTL | Blue video signal TTL level |  | GL-CL | Genlock clock (4.5MHz) |   |
|  BURST-ER | Burst error signal |  | G-MIX | Green video signal from mixer |   |
|  CBL | Composite blanking | pos.pulses | G-TTL | Green video signal TTL level |   |
|  CLCF | Bit clock CIM to FIL |  | H/2 | PAL 8kHz pulse |   |
|  CLDE | Bit clock DEMOD to ERCO |  | HALL C- | x |   |
|  CLEC | Bit clock ERCO to CIM |  | HALL B- | x |   |
|  CLDX | LV-ROM decoder master clock |  | HALL C+ | x |   |
|  CLP | Clamp pulse | pos.pulses | HALL B+ | x |   |
|  CL-RAD | Clipped radial | -12V / +12V | HALL AV+ | x signals from HALL elements |   |
|  CL-VID | Clipped video | 0V / +12V | HALL A- | x |   |
|  CLV-TC | CLV trackcross | +5V = active | HALL A+ | x |   |
|  COMM1 | Commutation coil 1 | +5V = on | HALL CV- | x |   |
|  COMM2 | Commutation coil 2 | +5V = on | HFATBC | HF audio timebase corrected |   |
|  COMM3 | Commutation coil 3 | +5V = on | HF-AUD | HF audio |   |
|  COMM4 | Commutation coil 4 | +5V = on | HF-OUT 1 | HF signal disc drive |   |
|  CP-1 | Course pulse 1 | 0V = active | HF-OUT 2 | HF signal sandwich |   |
|  CP-2 | Course pulse 2 | 0V = active | HMANCH | Horizontal sync | neg.pulses  |
|  CS | Composite sync |  | HOR. BL | Horizontal blanking adjustment |   |
|  CS 1-8 | Chip select 1 up to 8 |  | HW-TEST | Hardware test |   |
|  CS-EXT | External comp. sync input |  | INS-TXT | TXT signal for insert |   |
|  CS-REF | Composite sync reference | pos.pulses | IRQ | Interrupt request |   |
|  CS-S/NS | Standard/non standard CS select | +5V = standard | IR-REC | ROS from IR receiver |   |
|  CS-TTL | Comp. sync TTL level |  | LA | Laser on/off | 0V = off  |
|  CTS | Clear to send (RS232) |  | LA-STA | Laser status | 0V = on  |
|  CTS1 | CTS |  | LDI | Load index |   |
|  CTS2 | CTS |  | LED1 | LED drive |   |
|  CTS3 | CTS |  | LED2 | LED drive |   |
|  CV/CS | CVBS/Comp. Sync select | +12V = CVBS | LMOT-L | Load motor left | +5V = on  |
|  CVBS IN | External CVBS input signal |  | LMOT-R | Load motor right | +5V = on  |
|  CVBS | Composite video/burst/sync |  | LPO | Line pulse out |   |
|  CVBS OUT | CVBS output signal |  | LPWM | Line pulse width modulated |   |
|  CVBS2 | Disc CVBS without special burst |  | LUM | Luminance |   |
|  CVBS-INT | Internal CVBS |  | MCES | Motor control error signal |   |
|  CV-DEM | CVBS demodulated |  | MCD | Motor control output |   |
|  CV-DOC | CVBS dropout corrected |  | MCD-EN | MCD enable | +12V = active  |
|  CV-E/J | CVBS external/internal select | +12V = external | MEM-SU | Memory start up | +5V = active  |
|  CV-EXT | External CVBS |  | M-LOCK | Motor lock |   |
|  CV-TBC | CVBS time base corrected |  | MOT C | x |   |
|  CV-TBM | CVBS time base measurement |  | MOT B | x Motor drive signals |   |
|  CX-OFF | CX on/off | +12V = off | MOT A | x |   |
|  DADE | Data DEMOD to ERCO |  | MTF | Motional transfer function |   |
|  DA-DUMP | Data disc dump |  | NPL | Normal play forward | +5V = active  |
|  DABC | Data ERCO to CIM |  | NS-CS | Non standard composite sync |   |
|  DAK | S-bus data acknowledge |  | NS-VID | Non standard video indication | +12V = NSV  |
|  DAV | S-bus data available |  | OBF | Output buffer full |   |
|  DB/STAT | Databl/status text insert | 0V = busy | OBS | Output burst switch NTSC | +12V = active  |
|  DEM-BK | Demodulator burst key | pos.pulses | PWM | Pulse width modulated |   |
|  DEMV | Demodulated vert. pulse |  | Q1 | Stepping motor coil 1 (Yellow) |   |
|   |  |  | Q1.2 | Common 1.2 (Red) |   |
|   |  |  | Q2 | Stepping motor coil 2 (Grey) |   |

|  Q3 | Stepping motor coil 3 (Yellow) |  | SPI | Slide position indication | 0V = inwards  |
| --- | --- | --- | --- | --- | --- |
|  Q3,4 | Common 3,4 (Red) |  | SP-POS | Spot position |   |
|  Q4 | Stepping motor coil 4 (Grey) |  | SSDE | Symbol sync DEMOD to ERCO |   |
|  R | Red video signal |  | ST-ST | Start-stop switch | 0V = start  |
|  RADACT | Radial actuator drive signal |  | STB | Strobe | 0V = active  |
|  RAD-ER | Radial error |  | STBY | Standby command | 0V = standby  |
|  RAD-FS | Radial filter select | 0V = low pass | STBY-OUT | Standby button command |   |
|  RAMP-EN | Ramp enable | pos.pulses | STR1 | Strobe 1 (16 bit word) |   |
|  RC5 (NIB) | RC5 input SCART |  | STR2 | Strobe 2 (8 bit word) |   |
|  RC5 | RC5 commands |  | SYNC IN | External sync input signal |   |
|  RC5-INT | RC5 from IR receiver |  | SYNC OUT | Sync output signal |   |
|  RC5-SCART | RC5 commands SCART |  | TANG-ER | Tangential error |   |
|  RC5-OUT | RC5 output control |  | TI | Tray inside | 0V = inside  |
|  RCIR | RC input IR/SCART | +5V = IR | TLYOK | Tilt in position | 0V = in position  |
|  RD | Read |  | TLS | Tilt loop switch | +5V = closed  |
|  RDEN | S-bus read enable |  | TR | Track position |   |
|  RD-STRT | Read start pulse text insert | +5V = inactive |  | Indication(+6/-8V) | -6V = on track  |
|  REF-CLP | Clamp |  | TSP | Terminal speed |   |
|  REFH | Horizontal reference | pos.pulses | TTM | Turntable motor on/off | +5V = on  |
|  REFV | Vertical reference | pos.pulses | TK/RE | Transmit/receive data | 0V = receive  |
|  REPLAY | Replay switch on/off | 0V = replay | TXD | Transmit data (RS232) |   |
|  RESI | Reserved input dipswitch |  | TXD1 | TXD |   |
|  RESI 1 | Reserved input drive |  | TXD2 | TXD |   |
|  RESO 1 | Reserved output drive |  | TXD3 | TXD |   |
|  RESUPI | Reset UPI |  | TXT-IW | Teletext insertion window |   |
|  RGB-STA | RGB status signal SCART |  | TXT-WH | Teletext window horizontal | pos.pulses  |
|  RLE | Radial loop switch | +0V = closed | TXT-WV | Teletext window vertical | pos.pulses  |
|  R-MIX | Red video signal from mixer |  | UNEC | Unreliable data ERCO to CIM (Error flag) |   |
|  R-TTL | Red video signal TTL level |  | V/C-TXT | Video/control text insert | +5V = video text  |
|  RXD | Received data (RS232) |  | VBL | Vertical blanking | neg.pulses  |
|  RXD1 | RXD |  | VI-A/D | Video analogue/digital | +12V = analogue  |
|  RXD2 | RXD |  | VI-DOP | Video dropout pulse |   |
|  RXD3 | RXD |  | VMANCH | Vertical sync | neg.pulses  |
|  SC | Sandcastle pulse | pos.pulses | VOBN | Video background insertion | 0V = active  |
|  SCANLS | Scan loop switch | 0V = active | VOW | Video character insertion | +5V= active  |
|  SCL | IC bus clock |  | VP0 | Video mixer control 0 |   |
|  SCLT | P-bus clock |  | VP1 | Video mixer control 1 |   |
|  SCSI | Small computer system interface |  | VP2 | Video mixer control 2 |   |
|  SD 0-7 | S-bus data |  | VR | Vertical reference |   |
|  SDA | IC bus data | pos.pulses | WDOGRS | Watchdog reset | +5V = reset  |
|  SDAT | P-bus data | 0V = closed | WINDOW | S-bus window |   |
|  SEL | Selection |  | WR | Write |   |
|  SL-PWR | Slide power low/high | +5V = low | WR-CLK | Write clock text insert | +5V = inactive  |
|  SMF | Switch mode frequency | 17,6 kHz | WREN | S-bus write enable |   |

CS 7.020

![img-27.jpeg](img-27.jpeg)

C

C

C

C

![img-28.jpeg](img-28.jpeg)

CS 7 831

WIRING DIAGRAM SANDWICH

WDS

![img-29.jpeg](img-29.jpeg)

CS 7 832

# BLOCKDIAGRAM CONTROL ROUTES

![img-30.jpeg](img-30.jpeg)

CS 7 833

BLOCKDIAGRAM AUDIO/VIDEO PATH

![img-31.jpeg](img-31.jpeg)

CS 7 834

# BLOCKDIAGRAM SERVO

![img-32.jpeg](img-32.jpeg)

CS 7 835

CONNECTIONS OF SEMICONDUCTORS

|  SMD TOPVIEW SOT-143 | 01 02 3 D  |   |   |   |
| --- | --- | --- | --- | --- |
|  SMD TOPVIEW SOT-23 VAR | VAR 1 2 3 E | VAR 2 2 E 6 | VAR 3 2 D 5 |   |
|   | BOTTOM VIEW |   |   | TOP VIEW  |
|   | VAR 1 | VAR 2 | VAR 3 | VAR 4  |
|  TO-92 VAR | B C 1 | F B C | B E C | G S 0  |
|  TO-18 TO-72 | 5 0 |  |  | 6 0  |
|  TO-39 | 5 0 |  |  | 6 0  |
|  SOT-32(TO-126) SOT-82 SOT-93 SOT-186 | B C E |  |  | B C E  |

MDA 00636
T10 T16

|  SOT-143 | BF992 | BC264 | TO-92 VAR.4  |
| --- | --- | --- | --- |
|  SOT-186 | BUT11F | BC327 | TO-92 VAR.2  |
|  SOT-23 VAR.1 | BC807 | BC337 | TO-92 VAR.2  |
|   | BC817 | BC368 | TO-92 VAR.1  |
|   | BC847 | BC369 | TO-92 VAR.1  |
|   | BC848 | BC375 | TO-92 VAR.2  |
|   | BC849 | BC376 | TO-92 VAR.2  |
|   | BC858 | BC546 | TO-92 VAR.2  |
|   | BC859 | BC547 | TO-92 VAR.2  |
|   | BFS19 | BC548 | TO-92 VAR.2  |
|  SOT-23 VAR.3 | BFR30 | BC549 | TO-92 VAR.2  |
|  SOT-32 (TO-126) | BD135 | BC556 | TO-92 VAR.2  |
|   | BD434 | BC557 | TO-92 VAR.2  |
|   | BD435 | BC558 | TO-92 VAR.2  |
|   | BD436 | BC639 | TO-92 VAR.1  |
|   | BD437 | BC640 | TO-92 VAR.1  |
|   | BD438 | BC807 | SOT-23 VAR.1  |
|   | BUX86 | BC817 | SOT-23 VAR.1  |
|   |  | BC847 | SOT-23 VAR.1  |
|   |  | BC848 | SOT-23 VAR.1  |
|  SOT-82 | BUW85 | BC849 | SOT-23 VAR.1  |
|  SOT-93 | BUW12 | BC858 | SOT-23 VAR.1  |
|  TO-18 | BSV78 | BC859 | SOT-23 VAR.1  |
|   | BSV80 | BD135 | SOT-32 (TO-126)  |
|  TO-39 | BSW68 | BD434 | SOT-32 (TO-126)  |
|  TO-72 | BSD213 | BD435 | SOT-32 (TO-126)  |
|  TO-92 VAR.1 | BC368 | BD436 | SOT-32 (TO-126)  |
|   | BC369 | BD437 | SOT-32 (TO-126)  |
|   | BC639 | BD438 | SOT-32 (TO-126)  |
|   | BC640 | BFR30 | SOT-23 VAR.3  |
|  TO-92 VAR.2 | BC327 | BFR54 | TO-92 VAR.2  |
|   | BC337 | BFS19 | SOT-23 VAR.1  |
|   | BC375 | BF256 | TO-92 VAR.4  |
|   | BC376 | BF450 | TO-92 VAR.3  |
|   | BC546 | BF494 | TO-92 VAR.3  |
|   | BC547 | BF992 | SOT-143  |
|   | BC548 | BSD213 | TO-72  |
|   | BC549 | BSV80 | TO-18  |
|   | BC556 | BSW68 | TO-39  |
|   | BC557 | BUT11F | SOT-186  |
|   | BC558 | BUW12 | SOT-93  |
|   | BFR54 | BUW85 | SOT-82  |
|   | PH2369 | BUX86 | SOT-32 (TO-126)  |
|  TO-92 VAR.3 | BF450 | PH2369 | TO-92 VAR.2  |
|   | BF494 |  |   |
|  TO-92 VAR.4 | BC264 |  |   |
|   | BF256 |  |   |

CS 8 121

Survey of modules

Modules A to Z

- Circuit diagram
- PCB lay-out
- Adjustments
- Electrical parts

Remote control

Chapter 4

# SURVEY OF MODULES VP415

|  MOD | DESCRIPTION  |
| --- | --- |
|  A | AUDIO PROCESSOR  |
|  B | RGB  |
|  C | VIDEO PROCESSOR  |
|  D | REF SOURCE  |
|  E | SLIDE DRIVE  |
|  F | MOTOR+SEQUENCE  |
|  G | GEN LOCK  |
|  H | ETBC B  |
|  I | ETBC C  |
|  J | FOCUS  |
|  K | HF PROCESSOR  |
|  L | VIDEO D.O.  |
|  M | RADIAL  |
|  N | DISPLAY KEYBOARD  |
|  P | FRONT LOADER  |
|  Q | RC5 MIRROR  |
|  R | DRIVE PROCESSOR  |
|  S | CONTROL  |
|  T | SUPPLY  |
|  U | ANALOG I/O  |
|  V | MODULE CARRIER  |
|  W | CPU DATAGR.  |
|  X | LV ROM  |
|  Y | VID MIX  |
|  Z | DECK ELECTRONICS  |

CS 7 855

![img-33.jpeg](img-33.jpeg)

![img-34.jpeg](img-34.jpeg)

COMPONENT 3/DE

![img-35.jpeg](img-35.jpeg)

ENT SIDE

![img-36.jpeg](img-36.jpeg)

SOLDER SIDE

CS 7 836

CS 7 836

AUDIO PROC. MODULE

A

(MOD LEVEL 2)

# ADJUSTMENTS

Required

Test disc

Scope

Adjustment conditions

Load test disc

Normal play, picture no. 6200-6500 Audio 1,

6600-6900 Audio 2 (replay)

Audio modulation 1 kHz

# Adjustments

1) R3003, R3005 (Audio demo)

- Measure the output voltage on 1A1 and 3A1 (AUD2 and AUD1) with the scope.
- Adjust R3003 and R3005 until the output voltage is 1.6 Vpp.

Adjustment when item replaced:

replaced adjust

IC6201

IC6202

R3005

R3003

LIST OF ELECTRICAL PARTS MODULE A

|  Filters  |   |   |   |
| --- | --- | --- | --- |
|  5007 | 4822 242 71658 | SLC3251 |   |
|  5008 | 4822 242 71659 | SLC3252 |   |
|  Coils  |   |   |   |
|  5001 | 4822 156 20928 | 8 mH | 2008  |
|  5002 | 4822 156 11009 | 130 μH | 2009  |
|  5003 | 4822 156 11009 | 130 μH | 2010  |
|  5004 | 4822 156 20928 | 8 mH | 2011  |
|  5005 | 4822 156 11008 | 110 μH | 2012  |
|  5006 | 4822 156 11008 | 110 μH | 2013  |
|  Potentiometers  |   |   |   |
|  3003 | 4822 100 11087 | 2.2 kΩ | 2016  |
|  3005 | 4822 100 11087 | 2.2 kΩ | 2017  |
|   |  |  | 2018  |
|   |  |  | 2019  |
|   |  |  | 2020  |
|   |  |  | 2021  |
|   |  |  | 2022  |

![img-37.jpeg](img-37.jpeg)

|  4822 122 32808 | 1.2 nF |  | 2023 | 4822 122 32442 | 10 nF |  | 2057 | 5322 122 31647 | 1 nF |   |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
|  4822 122 32808 | 1.2 nF |  | 2024 | 4822 122 31759 | 22 nF |  | 2058 | 4822 122 31783 | 2.7 nF |   |
|  4822 122 32856 | 8.2 nF |  | 2025 | 4822 122 32482 | 22 pF |  | 2059 | 4822 122 31965 | 220 pF |   |
|  5322 124 21711 | 100 μF | 25 V | 2026 | 4822 122 31766 | 120 pF |  | 2060 | 4822 122 31774 | 56 pF |   |
|  4822 122 32597 | 6.8 nF |  | 2027 | 4822 122 31759 | 22 nF |  | 2061 | 4822 122 31767 | 150 pF |   |
|  4822 124 22189 | 6.8 μF | 63 V | 2028 | 4822 122 32442 | 10 nF |  | 2062 | 4822 122 32442 | 10 nF |   |
|  5322 124 21749 | 10 μF | 63 V | 2030 | 4822 122 31759 | 22 nF |  | 2064 | 4822 122 31783 | 2.7 nF |   |
|  5322 122 32839 | 100 nF |  | 2034 | 5322 124 21711 | 100 μF | 25 V | 2065 | 5322 124 10512 | 68 μF | 20% 16 V  |
|  4822 122 32442 | 10 nF |  | 2036 | 4822 122 31759 | 22 nF |  | 2066 | 5322 124 21749 | 10 μF | 63 V  |
|  4822 122 31759 | 22 nF |  | 2037 | 4822 122 33007 | 330 nF | 25 V | 2069 | 5322 124 21749 | 10 μF | 63 V  |
|  4822 122 31768 | 180 pF |  | 2039 | 4822 122 33007 | 330 nF | 25 V |  |  |  |   |
|  4822 122 32975 | 33 pF |  | 2046 | 4822 122 32927 | 220 nF |  |  |  |  |   |
|  4822 122 31759 | 22 nF |  | 2047 | 4822 122 32927 | 220 nF |  |  |  |  |   |
|  4822 122 32442 | 10 nF |  | 2048 | 5322 124 21711 | 100 μF | 25 V |  |  |  |   |
|  4822 122 32808 | 1.2 nF |  | 2049 | 5322 124 10512 | 68 μF | 20% 16 V |  |  |  |   |
|  4822 122 32808 | 1.2 nF |  | 2050 | 4822 122 32972 | 1 nF |  |  |  |  |   |
|  4822 122 32856 | 8.2 nF |  | 2051 | 4822 122 31783 | 2.7 nF |  |  |  |  |   |
|  5322 124 21711 | 100 μF | 25 V | 2052 | 4822 122 31965 | 220 pF |  |  |  |  |   |
|  4822 122 32597 | 6.8 nF |  | 2053 | 4822 122 31774 | 56 pF |  |  |  |  |   |
|  4822 124 22189 | 6.8 μF | 63 V | 2054 | 4822 122 31767 | 150 pF |  |  |  |  |   |
|  5322 124 21749 | 10 μF | 63 V | 2055 | 4822 122 32442 | 10 nF |  |  |  |  |   |
|  5322 122 32839 | 100 nF |  | 2056 | 4822 122 31783 | 2.7 nF |  |  |  |  |   |

![img-38.jpeg](img-38.jpeg)[{"box_2d": [918, 74, 945, 899], "label": "header_footer", "caption": "1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18\nAUDIO PROC MODULE\nA\n1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18\nAUDIO PROC MODULE\nA\n1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18\nAUDIO PROC MODULE\nA\n1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18\nAUDIO PROC MODULE\nA\n1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18\nAUDIO PROC MODULE\nA\n1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18\nAUDIO PROC MODULE\nA\n1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18\nAUDIO PROC MODULE\nA\n1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18\nAUDIO PROC MODULE\nA\n1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18\nAUDIO PROC MODULE\nA\n1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18\nAUDIO PROC MODULE\nA\n1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18\nAUDIO PROC MODULE\nA\n1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18\nAUDIO PROC MODULE\nA\n1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18\nAUDIO PROC MODULE\nA\n1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18\nAUDIO PROC MODULE\nA\n1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18\nAUDIO PROC MODULE\nA\n1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18\nAUDIO PROC MODULE\nA\n1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18\nAUDIO PROC MODULE\nA\n1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18\nAUDIO PROC MODULE\nA\n1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18\nAUDIO PROC MODULE\nA\n1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18\nAUDIO PROC MODULE\nA\n1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18\nAUDIO PROC MODULE\nA\n1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18\nAUDIO PROC MODULE\nA\n1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18\nAUDIO PROC MODULE\nA\n1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18\nAUDIO PROC MODULE\nA\n1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18\nAUDIO PROC MODULE\nA\n1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18\nAUDIO PROC MODULE\nA\n1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18\nAUDIO PROC MODULE\nA\n1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18\nAUDIO PROC MODULE\nA\n1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18\nAUDIO PROC MODULE\nA\n1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18\nAUDIO PROC MODULE\nA\n1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18\nAUDIO PROC MODULE\nA\n1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18\nAUDIO PROC MODULE\nA\n1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18\nAUDIO PROC MODULE\nA\n1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18\nAUDIO PROC MODULE\nA\n1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18\nAUDIO PROC MODULE\nA\n1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18\nAUDIO PROC MODULE\nA\n1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18\nAUDIO PROC MODULE\nA\n1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18\nAUDIO PROC MODULE\nA\n1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18\nAUDIO PROC MODULE\nA\n1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18\nAUDIO PROC MODULE\nA\n1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18\nAUDIO PROC MODULE\nA\n1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18\nAUDIO PROC MODULE\nA\n1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18\nAUDIO PROC MODULE\nA\n1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18\nAUDIO PROC MODULE\nA\n1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18\nAUDIO PROC MODULE\nA\n1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18\nAUDIO PROC MODULE\nA\n1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18\nAUDIO PROC MODULE\nA\n1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18\nAUDIO PROC MODULE\nA\n1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18\nAUDIO PROC MODULE\nA\n1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18\nAUDIO PROC MODULE\nA\n1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18\nAUDIO PROC MODULE\nA\n1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18\nAUDIO PROC MODULE\nA\n1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18\nAUDIO PROC MODULE\nA\n1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18\nAUDIO PROC MODULE\nA\n1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18\nAUDIO PROC MODULE\nA\n1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18\nAUDIO PROC MODULE\nA\n1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18\nAUDIO PROC MODULE\nA\n1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18\nAUDIO PROC MODULE\nA\n1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18\nAUDIO PROC MODULE\nA\n1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18\nAUDIO PROC MODULE\nA\n1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18\nAUDIO PROC MODULE\nA\n1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18\nAUDIO PROC MODULE\nA\n1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18\nAUDIO PROC MODULE\nA\n1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18\nAUDIO PROC MODULE\nA\n1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18\nAUDIO PROC MODULE\nA\n1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18\nAUDIO PROC MODULE\nA\n1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18\nAUDIO PROC MODULE\nA\n1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18\nAUDIO PROC MODULE\nA\n1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18\nAUDIO PROC MODULE\nA\n1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18\nAUDIO PROC MODULE\nA\n1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18\nAUDIO PROC MODULE\nA\n1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18\nAUDIO PROC MODULE\nA\n1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18\nAUDIO PROC MODULE\nA\n1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18\nAUDIO PROC MODULE\nA\n1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18\nAUDIO PROC MODULE\nA\n1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18\nAUDIO PROC MODULE\nA\n1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18\nAUDIO PROC MODULE\nA\n1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18\nAUDIO PROC MODULE\nA\n1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18\nAUDIO PROC MODULE\nA\n1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18\nAUDIO PROC MODULE\nA\n1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18\nAUDIO PROC MODULE\nA\n1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18\nAUDIO PROC MODULE\nA\n1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18\nAUDIO PROC MODULE\nA\n1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18\nAUDIO PROC MODULE\nA\n1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18\nAUDIO PROC MODULE\nA\n1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18\nAUDIO PROC MODULE\nA\n1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18\nAUDIO PROC MODULE\nA\n1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18\nAUDIO PROC MODULE\nA\n1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18\nAUDIO PROC MODULE\nA\n1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18\nAUDIO PROC MODULE\nA\n1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18\nAUDIO PROC MODULE\nA\n1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18\nAUDIO PROC MODULE\nA\n1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18\nAUDIO PROC MODULE\nA\n1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18\nAUDIO PROC MODULE\nA\n1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18\nAUDIO PROC MODULE\nA\n1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18\nAUDIO PROC MODULE\nA\n1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18\nAUDIO PROC MODULE\nA\n1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18\nAUDIO PROC MODULE\nA\n1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18\nAUDIO PROC MODULE\nA\n1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18\nAUDIO PROC MODULE\nA\n1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18\nAUDIO PROC MODULE\nA\n1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18\nAUDIO PROC MODULE\nA\n1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18\nAUDIO PROC MODULE\nA\n1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18\nAUDIO PROC MODULE\nA\n1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18\nAUDIO PROC MODULE\nA\n1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18\nAUDIO PROC MODULE\nA\n1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18\nAUDIO PROC MODULE\nA\n1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18\nAUDIO PROC MODULE\nA\n1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18\nAUDIO PROC MODULE\nA\n1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18\nAUDIO PROC MODULE\nA\n1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18\nAUDIO PROC MODULE\nA\n1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18\nAUDIO PROC MODULE\nA\n1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18\nAUDIO PROC MODULE\nA\n1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18\nAUDIO PROC MODULE\nA\n1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18\nAUDIO PROC MODULE\nA\n1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18\nAUDIO PROC MODULE\nA\n1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18\nAUDIO PROC MODULE\nA\n1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18\nAUDIO PROC MODULE\nA\n1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18\nAUDIO PROC MODULE\nA\n1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18\nAUDIO PROC MODULE\nA\n1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18\nAUDIO PROC MODULE\nA\n1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18\nAUDIO PROC MODULE\nA\n1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18\nAUDIO PROC MODULE\nA\n1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18\nAUDIO PROC MODULE\nA\n1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18\nAUDIO PROC MODULE\nA\n1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18\nAUDIO PROC MODULE\nA\n1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18\nAUDIO PROC MODULE\nA\n1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18\nAUDIO PROC MODULE\nA\n1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18\nAUDIO PROC MODULE\nA\n1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18\nAUDIO PROC MODULE\nA\n1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18\nAUDIO PROC MODULE\nA\n1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18\nAUDIO PROC MODULE\nA\n1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18\nAUDIO PROC MODULE\nA\n1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18\nAUDIO PROC MODULE\nA\n1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18\nAUDIO PROC MODULE\nA\n1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18\nAUDIO PROC MODULE\nA\n1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18\nAUDIO PROC MODULE\nA\n1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18\nAUDIO PROC MODULE\nA\n1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18\nAUDIO PROC MODULE\nA\n1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18\nAUDIO PROC MODULE\nA\n1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18\nAUDIO PROC MODULE\nA\n1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18\nAUDIO PROC MODULE\nA\n1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18\nAUDIO PROC MODULE\nA\n1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18\nAUDIO PROC MODULE\nA\n1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18\nAUDIO PROC MODULE\nA\n1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18\nAUDIO PROC MODULE\nA\n1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18\nAUDIO PROC MODULE\nA\n1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18\nAUDIO PROC MODULE\nA\n1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18\nAUDIO PROC MODULE\nA\n1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18\nAUDIO PROC MODULE\nA\n1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18\nAUDIO PROC MODULE\nA\n1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18\nAUDIO PROC MODULE\nA\n1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18\nAUDIO PROC MODULE\nA\n1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18\nAUDIO PROC MODULE\nA\n1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18\nAUDIO PROC MODULE\nA\n1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18\nAUDIO PROC MODULE\nA\n1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18\nAUDIO PROC MODULE\nA\n1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18\nAUDIO PROC MODULE\nA\n1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18\nAUDIO PROC MODULE\nA\n1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18\nAUDIO PROC MODULE\nA\n1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18\nAUDIO PROC MODULE\nA\n1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18\nAUDIO PROC MODULE\nA\n1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18\nAUDIO PROC MODULE\nA\n1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18\nAUDIO PROC MODULE\nA\n1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18\nAUDIO PROC MODULE\nA\n1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18\nAUDIO PROC MODULE\nA\n1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18\nAUDIO PROC MODULE\nA\n1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18\nAUDIO PROC MODULE\nA\n1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18\nAUDIO PROC MODULE\nA\n1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18\nAUDIO PROC MODULE\nA\n1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18\nAUDIO PROC MODULE\nA\n1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18\nAUDIO PROC MODULE\nA\n1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18\nAUDIO PROC MODULE\nA\n1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18\nAUDIO PROC MODULE\nA\n1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18\nAUDIO PROC MODULE\nA\n1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18\nAUDIO PROC MODULE\nA\n1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18\nAUDIO PROC MODULE\nA\n1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18\nAUDIO PROC MODULE\nA\n1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18\nAUDIO PROC MODULE\nA\n1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18\nAUDIO PROC MODULE\nA\n1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18\nAUDIO PROC MODULE\nA\n1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18\nAUDIO PROC MODULE\nA\n1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18\nAUDIO PROC MODULE\nA\n1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18\nAUDIO PROC MODULE\nA\n1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18\nAUDIO PROC MODULE\nA\n1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18\nAUDIO PROC MODULE\nA\n1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18\nAUDIO PROC MODULE\nA\n1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18\nAUDIO PROC MODULE\nA\n1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18\nAUDIO PROC MODULE\nA\n1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18\nAUDIO PROC MODULE\nA\n1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18\nAUDIO PROC MODULE\nA\n1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18\nAUDIO PROC MODULE\nA\n1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18\nAUDIO PROC MODULE\nA\n1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18\nAUDIO PROC MODULE\nA\n1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18\nAUDIO PROC MODULE\nA\n1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18\nAUDIO PROC MODULE\nA\n1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18\nAUDIO PROC MODULE\nA\n1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18\nAUDIO PROC MODULE\nA\n1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18\nAUDIO PROC MODULE\nA\n1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18\nAUDIO PROC MODULE\nA\n1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18\nAUDIO PROC MODULE\nA\n1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18\nAUDIO PROC MODULE\nA\n1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18\nAUDIO PROC MODULE\nA\n1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18\nAUDIO PROC MODULE\nA\n1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18\nAUDIO PROC MODULE\nA\n1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18\nAUDIO PROC MODULE\nA\n1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18\nAUDIO PROC MODULE\nA\n1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18\nAUDIO PROC MODULE\nA\n1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18\nAUDIO PROC MODULE\nA\n1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18\nAUDIO PROC MODULE\nA\n1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18\nAUDIO PROC MODULE\nA\n1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18\nAUDIO PROC MODULE\nA\n1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18\nAUDIO PROC MODULE\nA\n1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18\nAUDIO PROC MODULE\nA\n1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18\nAUDIO PROC MODULE\nA\n1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18\nAUDIO PROC MODULE\nA\n1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18\nAUDIO PROC MODULE\nA\n1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18\nAUDIO PROC MODULE\nA\n1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18\nAUDIO PROC MODULE\nA\n1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18\nAUDIO PROC MODULE\nA\n1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18\nAUDIO PROC MODULE\nA\n1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18\nAUDIO PROC MODULE\nA\n1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18\nAUDIO PROC MODULE\nA\n1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18\nAUDIO PROC MODULE\nA\n1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18\nAUDIO PROC MODULE\nA\n1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18\nAUDIO PROC MODULE\nA\n1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18\nAUDIO PROC MODULE\nA\n1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18\nAUDIO PROC MODULE\nA\n1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18\nAUDIO PROC MODULE\nA\n1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18\nAUDIO PROC MODULE\nA\n1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18\nAUDIO PROC MODULE\nA\n1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18\nAUDIO PROC MODULE\nA\n1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18\nAUDIO PROC MODULE\nA\n1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18\nAUDIO PROC MODULE\nA\n1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18\nAUDIO PROC MODULE\nA\n1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18\nAUDIO PROC MODULE\nA\n1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18\nAUDIO PROC MODULE\nA\n1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18\nAUDIO PROC MODULE\nA\n1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18\nAUDIO PROC MODULE\nA\n1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18\nAUDIO PROC MODULE\nA\n1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18\nAUDIO PROC MODULE\nA\n1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18\nAUDIO PROC MODULE\nA\n1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18\nAUDIO PROC MODULE\nA\n1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18\nAUDIO PROC MODULE\nA\n1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18\nAUDIO PROC MODULE\nA\n1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18\nAUDIO PROC MODULE\nA\n1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18\nAUDIO PROC MODULE\nA\n1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18\nAUDIO PROC MODULE\nA\n1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18\nAUDIO PROC MODULE\nA\n1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18\nAUDIO PROC MODULE\nA\n1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18\nAUDIO PROC MODULE\nA\n1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18\nAUDIO PROC MODULE\nA\n1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18\nAUDIO PROC MODULE\nA\n1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18\nAUDIO PROC MODULE\nA\n1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18\nAUDIO PROC MODULE\nA\n1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18\nAUDIO PROC MODULE\nA\n1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18\nAUDIO PROC MODULE\nA\n1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18\nAUDIO PROC MODULE\nA\n1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18\nAUDIO PROC MODULE\nA\n1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18\nAUDIO PROC MODULE\nA\n1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18\nAUDIO PROC MODULE\nA\n1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18\nAUDIO PROC MODULE\nA\n1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18\nAUDIO PROC MODULE\nA\n1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18\nAUDIO PROC MODULE\nA\n1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18\nAUDIO PROC MODULE\nA\n1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18\nAUDIO PROC MODULE\nA\n1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18\nAUDIO PROC MODULE\nA\n1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18\nAUDIO PROC MODULE\nA\n1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18\nAUDIO PROC MODULE\nA\n1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18\nAUDIO PROC MODULE\nA\n1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18\nAUDIO PROC MODULE\nA\n1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18\nAUDIO PROC MODULE\nA\n1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18\nAUDIO PROC MODULE\nA\n1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18\nAUDIO PROC MODULE\nA\n1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18\nAUDIO PROC MODULE\nA\n1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18\nAUDIO PROC MODULE\nA\n1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18\nAUDIO PROC MODULE\nA\n1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18\nAUDIO PROC MODULE\nA\n1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18\nAUDIO PROC MODULE\nA\n1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18\nAUDIO PROC MODULE\nA\n1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18\nAUDIO PROC MODULE\nA\n1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18\nAUDIO PROC MODULE\nA\n1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18\nAUDIO PROC MODULE\nA\n1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18\nAUDIO PROC MODULE\nA\n1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18\nAUDIO PROC MODULE\nA\n1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18\nAUDIO PROC MODULE\nA\n1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18\nAUDIO PROC MODULE\nA\n1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18\nAUDIO PROC MODULE\nA\n1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18\nAUDIO PROC MODULE\nA\n1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18\nAUDIO PROC MODULE\nA\n1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18\nAUDIO PROC MODULE\nA\n1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18\nAUDIO PROC MODULE\nA\n1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18\nAUDIO PROC MODULE\nA\n1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18\nAUDIO PROC MODULE\nA\n1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18\nAUDIO PROC MODULE\nA\n1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18\nAUDIO PROC MODULE\nA\n1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18\nAUDIO PROC MODULE\nA\n1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18\nAUDIO PROC MODULE\nA\n1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18\nAUDIO PROC MODULE\nA\n1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18\nAUDIO PROC MODULE\nA\n1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18\nAUDIO PROC MODULE\nA\n1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18\nAUDIO PROC MODULE\nA\n1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18\nAUDIO PROC MODULE\nA\n1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18\nAUDIO PROC MODULE\nA\n1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18\nAUDIO PROC MODULE\nA\n1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18\nAUDIO PROC MODULE\nA\n1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18\nAUDIO PROC MODULE\nA\n1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18\nAUDIO PROC MODULE\nA\n1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18\nAUDIO PROC MODULE\nA\n1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18\nAUDIO PROC MODULE\nA\n1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18\nAUDIO PROC MODULE\nA\n1 2 3 4 5 6 7 8 9 10 11 12 13 14

1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31 32 33 34 35 36 37 38 39 40 41 42 43 44 45 46 47 48 49 50 51 52 53 54 55 56 57 58 59 60 61 62 63 64 65 66 67 68 69 70 71 72 73 74 75 76 77 78 79 80 81 82 83 84 85 86 87 88 89 90 91 92 93 94 95 96 97 98 99 100

![img-39.jpeg](img-39.jpeg)

CS 6 868

RGB MODULE

B

(MOD LEVEL 5)

# ADJUSTMENTS

# Required

Test disc

Scope (dual beam) with X-deflection via B-channel

Or vector scope, if available

# Adjustment conditions

Load test disc.

Still picture, colour pattern (picture no. 6200).

# Adjustments

1) L5002 and L5003 (notch filter)

- Using the scope, measure the luminance signal on 10B3, line triggered (see fig. B1)

![img-40.jpeg](img-40.jpeg)

LUMINANCE SIGNAL

MDA-30595
T28/711

Fig. B1

- Adjust L5002 until the chroma rests in the luminance signal have disappeared.
- Adjust L5003 until overshoot a and undershoot b have the same amplitude.

2) L5004 (Bandpass)

- Measure the chroma signal on 15-IC7201 with the scope.
- Adjust L5004 for minimum overshoots in the chroma signal.

3) R3015 and L5007 (Delay line)

- Measure with the scope the (R-Y) signal at 9B2 with the A-channel and the (B-Y) signal on 10B2 with the B-channel, both AC coupled.
- Switch the scope to X-deflection and adjust it until the vector diagram below appears (see Fig. B2).

![img-41.jpeg](img-41.jpeg)

VECTOR DIAGRAM COLOUR BAR

Fig. B2

MDA-30585
T28/711

The colour spots visible on the scope screen are lying at a certain distance B from origin O.

- Short-circuit pins 1-2 or 3-4 of delay line L5008. The spots in the vector diagram will lie closer to the origin now, at distance A from the origin. When the short-circuit is removed, the spots move outwards again (B).
- Adjust L5007 until the dimensions of the spots (in B) are minimal.
- Adjust R3015 until distance OB is twice distance OA in case of alternate short-circuiting of the delay line.

4) C2015 (Oscillator frequency)

- Connect the scope as described sub 3).
- Short-circuit pins 1-2 or 3-4 of delay line L5008.
- Adjust C2015 until the dimensions of the colour spots of the vector diagram are minimal.

5) R3080 (Luminance signal amplitude)

- Measure the G-signal on 3B3 (line freq.) with the scope. See fig. B3.

![img-42.jpeg](img-42.jpeg)

Fig. B3

MDA-30580
T28/711

- Adjust R3080 for an average amplitude of 700 mV ± 7 mV.

6) R3082, R3084 (colour difference signal amplitude)

- Using the scope, measure the R-signal on 2B3 and adjust R3082 to the same amplitude of yellow, magenta and red.
- Using the scope, measure the B-signal on 4B3 and adjust R3084 to the same amplitude of cyan, magenta and blue (see Fig. B3).

7) R3045 (black level)

- Measure output B-signal on 4B3 with the scope.
- Adjust R3045 for a black level of 0V ± 50 mV (see Fig. B3).

# Adjustment when item replaced

replaced

adjust

IC7201

R3015, R3082, R3084, C2015, L5006, L5007

IC7202

R3080

IC7203

R3055, R3080, R3082, R3084

R3080

R3207 )

R3082

R3305 ) on analog I/O module U

R3084

R3315 )

|   | 2008 A 1 | 2018 A 4 | 2028 B 5 | 2039 A 5 | 3010 B 1 | 3080 A 3 | 5001  |
| --- | --- | --- | --- | --- | --- | --- | --- |
|  2001 B 2 | 2011 B 2 | 2021 A 4 | 2028 B 5 | 2040 A 5 | 3015 A 2 | 3082 A 3 | 5002  |
|  2002 B 4 | 2015 B 2 | 2022 A 4 | 2028 A 5 | 2039 B 1 | 3045 A 7 | 3084 A 3 | 5003  |

![img-43.jpeg](img-43.jpeg)

|  2001 B 2 | 2009 A 2 | 2015 A 2 | 2024 A 4 | 2031 A 5 | 3002 A 3 | 3007 B 4 | 3013  |
| --- | --- | --- | --- | --- | --- | --- | --- |
|  2004 B 2 | 2012 A 2 | 2017 A 1 | 2025 A 4 | 2032 A 5 | 3003 B 3 | 3008 A 3 | 3014  |
|  2005 A 3 | 2012 A 2 | 2019 A 4 | 2027 A 5 | 2032 A 5 | 3004 B 3 | 3011 A 2 | 3016  |
|  2006 B 4 | 2013 A 2 | 2020 A 4 | 2029 A 5 | 2034 A 5 | 3005 B 4 | 3012 A 2 | 3017  |
|  2007 B 2 | 2014 A 2 | 2023 A 4 | 2030 A 5 | 2051 B 3 | 3006 B 3 |  | 3018  |

![img-44.jpeg](img-44.jpeg)

LIST OF ELECTRICAL PARTS MODULE B

Trimcapaci
2015

Crystals

|  5005 | 4822 242 70304 | 8.867238 MHz  |
| --- | --- | --- |

2001

Delay lines

|  5008 | 4822 320 40051 | DL711  |
| --- | --- | --- |

2002

Coils

|  5001 | 4822 156 10993 | 150 μH  |
| --- | --- | --- |
|  5002 | 4822 157 52873 | 5.5 μH  |
|  5003 | 4822 157 52875 | 66 μH  |
|  5004 | 4822 157 52874 | 12.5 μH  |
|  5006 | 4822 156 10995 | 10 μH  |
|  5007 | 5322 156 21341 | 10 μH  |

2012

Potentiometers

|  3015 | 4822 100 10359 | 220 Ω  |
| --- | --- | --- |
|  3045 | 5322 101 14066 | 10 kΩ  |
|  3080 | 5322 100 10117 | 2.2 kΩ  |
|  3082 | 5322 100 10117 | 2.2 kΩ  |
|  3084 | 5322 100 10117 | 2.2 kΩ  |

2013

2014

2015

2016

2017

2018

MODULE

DD LEVEL 5)

B

1 the scope screen are from origin O.

-4 of delay line L5008.
ram will lie closer to the
om the origin. When the
e spots move outwards

sions of the spots (in B)

DB is twice distance OA
cruiting of the delay line.

ibed sub 3).

4 of delay line L5008.
sions of the colour
are minimal.

tude)

IB3 (line freq.) with the

![img-45.jpeg](img-45.jpeg)

![img-46.jpeg](img-46.jpeg)

![img-47.jpeg](img-47.jpeg)

![img-48.jpeg](img-48.jpeg)

INALS

MDX 0098
726711

amplitude of 700 mV ±

signal amplitude)

a R-signal on 2B3 and
mplitude of yellow, ma-

a B-signal on 4B3 and
plitude of cyan, magen-

7) R3045 (black level)

- Measure output B-signal on 4B3 with the scope.
- Adjust R3045 for a black level of 0V ± 50 mV (see Fig. B3).

Adjustment when item replaced

|  replaced | adjust  |
| --- | --- |
|  IC7201 | R3015, R3082, R3084, C2015, L5006, L5007  |
|  IC7202 | R3080  |
|  IC7203 | R3055, R3080, R3082, R3084  |
|  R3080 | R3207 )  |
|  R3082 | R3305 ) on analog I/O module U  |
|  R3084 | R3315 )  |

|  2001 B 3 | 2011 B 2 | 2021 A 4 | 2028 B 5 | 2040 A 5 | 2015 B 1 | 2080 A 3 | 5091 B 3 | 5054 B 4 | 5037 A 1 | 5002 A 1 | 6007 A 7 | 7008 A 7 | 7202 A 4  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
|  2002 B 4 | 2019 B 2 | 2022 A 4 | 2038 B 5 | 2040 B 5 | 2015 A 2 | 2082 A 3 | 5092 B 3 | 5035 B 2 | 5008 A 1 | 5003 A 7 | 5009 B 7 | 7010 B 7 | 7203 A 6  |
|  |   |   |   |   |   |   |   |   |   |   |   |   |   |

![img-49.jpeg](img-49.jpeg)

|  2003 B 3 | 2006 A 2 | 2010 A 2 | 2024 A 4 | 2031 A 5 | 2002 A 3 | 2007 B 4 | 2013 A 3 | 2019 A 4 | 2025 A 6 | 2030 A 8 | 2035 A 6 | 2047 B 6 | 2057 A 7 | 2067 A 7 | 2071 B 4 | 6010 B 3  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
|  2004 B 3 | 2010 A 2 | 2017 A 1 | 2025 A 4 | 2032 A 6 | 2002 B 3 | 2008 A 3 | 2014 A 2 | 2021 A 4 | 2025 B 5 | 2021 A 8 | 2028 A 6 | 2040 B 7 | 2050 B 7 | 2060 B 7 | 2070 B 3 | 7001 B 3  |
|  2005 A 2 | 2012 A 2 | 2019 A 4 | 2027 A 6 | 2033 A 6 | 2004 B 3 | 2011 A 2 | 2016 A 1 | 2022 A 5 | 2027 A 6 | 2032 A 5 | 2037 A 7 | 2040 B 7 | 2050 B 7 | 2060 B 7 | 2070 B 3 | 7002 A 3  |
|  2006 B 4 | 2013 A 2 | 2020 A 4 | 2035 A 5 | 2044 A 6 | 2005 B 4 | 2012 A 2 | 2017 A 2 | 2023 B 5 | 2028 A 6 | 2033 A 5 | 2043 A 7 | 2050 B 7 | 2060 A 7 | 2070 B 7 | 2081 A 4 | 7003 B 3  |
|  2007 B 2 | 2014 A 2 | 2023 A 4 | 2036 A 5 | 2051 B 3 | 2006 B 3 |  | 2018 A 4 | 2024 B 5 | 2029 A 6 | 2034 A 5 | 2044 A 7 | 2051 B 7 | 2061 A 7 | 2071 B 7 | 2083 A 3 | 7010 B 3  |

![img-50.jpeg](img-50.jpeg)

LIST OF ELECTRICAL PARTS MODULE B

Crystals

|  5005 | 4822 242 70304 | 8.867238 MHz  |
| --- | --- | --- |

Delay lines

|  5008 | 4822 320 40051 | DL711  |
| --- | --- | --- |

Coils

|  5001 | 4822 156 10993 | 150 μH  |
| --- | --- | --- |
|  5002 | 4822 157 52873 | 5.5 μH  |
|  5003 | 4822 157 52875 | 66 μH  |
|  5004 | 4822 157 52874 | 12.5 μH  |
|  5006 | 4822 156 10995 | 10 μH  |
|  5007 | 5322 156 21341 | 10 μH  |

Potentiometers

|  3015 | 4822 100 10359 | 220 Ω  |
| --- | --- | --- |
|  3045 | 5322 101 14066 | 10 kΩ  |
|  3080 | 5322 100 10117 | 2.2 kΩ  |
|  3082 | 5322 100 10117 | 2.2 kΩ  |
|  3084 | 5322 100 10117 | 2.2 kΩ  |

Trimcapacitors

|  2015 | 4822 125 50092 | 40 pF  |
| --- | --- | --- |

|  2001 | 4822 124 22027 | 47 μF | 25 V  |
| --- | --- | --- | --- |
|  2002 | 4822 124 22027 | 47 μF | 25 V  |
|  2003 | 4822 122 31974 | 820 pF |   |
|  2004 | 4822 122 31965 | 220 pF |   |
|  2005 | 4822 122 31966 | 27 pF |   |
|  2006 | 4822 122 31766 | 120 pF |   |
|  2007 | 4822 122 31783 | 2.7 nF |   |
|  2008 | 4822 124 22186 | 150 μF | 25 V  |
|  2009 | 4822 122 31759 | 22 nF |   |
|  2010 | 4822 122 31759 | 22 nF |   |
|  2011 | 4822 124 22188 | 3.3 μF | 63 V  |
|  2012 | 4822 122 31916 | 5.6 nF |   |
|  2013 | 4822 122 32183 | 56 nF |   |
|  2014 | 4822 121 42915 | 330 pF |   |
|  2015 | 4822 125 50092 | 40 pF | trimmer  |
|  2016 | 4822 122 32442 | 10 nF |   |
|  2017 | 4822 122 32442 | 10 nF |   |
|  2018 | 4822 121 41756 | 330 nF | 10% 63 V  |

|  2019 | 4822 122 33002 | 68 pF |   |
| --- | --- | --- | --- |
|  2020 | 4822 122 33002 | 68 pF |   |
|  2021 | 4822 121 41719 | 1 μF | 10% 100 V  |
|  2022 | 4822 121 41719 | 1 μF | 10% 100 V  |
|  2023 | 4822 121 42915 | 330 pF |   |
|  2024 | 4822 122 32974 | 100 pF |   |
|  2025 | 4822 122 32974 | 100 pF |   |
|  2026 | 4822 124 22186 | 150 μF | 25 V  |
|  2027 | 4822 122 31759 | 22 nF |   |
|  2028 | 5322 124 21643 | 22 μF | 40 V  |
|  2029 | 4822 122 33008 | 120 nF | 50 V  |
|  2030 | 4822 122 33008 | 120 nF | 50 V  |
|  2031 | 4822 122 33008 | 120 nF | 50 V  |
|  2032 | 4822 122 31759 | 22 nF |   |
|  2033 | 4822 122 31759 | 22 nF |   |
|  2034 | 4822 122 31759 | 22 nF |   |
|  2038 | 4822 121 41608 | 100 nF | 100 V  |
|  2039 | 4822 121 41608 | 100 nF | 100 V  |
|  2040 | 4822 121 41874 | 270 nF | 63 V  |

CS 7 838

VIDEO PROC. MODULE

(MOD LEVEL 3)

C

# ADJUSTMENTS

# Required

Test disc

Voltmeter

Scope

# Adjustment conditions

Load test disc

Still picture, colour bar (picture no. 6200).

# Adjustments

1) R3035 (frequency)

- Measure the DC voltage on 18-IC7202.
- Adjust R3035 for a DC voltage of 5.5V ± 0.5 V.

2) R3045 (horizontal blanking)

- Search for a white picture (e.g. picture no. 7500).
- Measure sandcastle pulse SC on 3C2 with the scope (A-channel).
- Measure the G-signal on 3B3 with the scope (B-channel) and trigger on this signal.
- Adjust R3045 for a difference of 0.5μs between the SC and the G-signal (see Fig. C1).

![img-51.jpeg](img-51.jpeg)

Fig. C1

# Adjustment when item replaced

replaced

IC7202

IC7203

adjust

R3035, R3045

R3045

|  2001 A 1 | 2005 A 2 | 2017 A 4 | 2022 A 3 | 2005 A 1 | 6002 A 2 | 7000 B 2 | 7011 B 2 | 7001 A 1 | 2015 A 3 | 1102 B 0 | 2105 A 6 | 6004 A 5 | 7101 B 5  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
|  2002 B 2 | 2010 A 3 | 2016 B 3 | 2026 A 3 | 6001 A 2 | 6003 B 4 | 7007 A 2 | 7012 B 3 | 7202 A 4 | 2101 B 6 | 3103 B 0 | 2106 B 6 | 6005 A 5 | 7102 A 6  |
|  2004 A 1 | 2011 A 3 | 2019 B 3 | 2045 A 4 | 6001 A 2 | 7004 A 2 | 7010 B 2 | 7017 B 3 | 7202 A 4 | 3101 B 5 | 3104 B 0 | 2107 B 6 | 6006 A 5 | 7103 B 6  |

![img-52.jpeg](img-52.jpeg)

|  2003 A 1 | 2014 B 4 | 2024 B 4 | 2032 A 1 | 2008 A 2 | 2015 B 3 | 2021 B 2 | 2027 A 2 | 2034 B 3 | 2041 A 4 | 2049 B 4 | 2057 A 3 | 2063 A 2 | 2077 A 1 | 7008 B 3 | 7104 A 1  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
|  2007 B 2 | 2018 A 3 | 2025 A 5 | 2033 A 2 | 2009 A 2 | 2016 A 2 | 2022 B 2 | 2028 A 2 | 2036 A 4 | 2042 A 4 | 2050 B 4 | 2056 A 3 | 2064 A 3 | 2066 A 2 | 7009 B 3 |   |
|  2008 B 3 | 2020 B 3 | 2026 A 3 | 2034 A 2 | 2010 B 1 | 2017 A 2 | 2023 B 2 | 2029 A 2 | 2037 B 4 | 2043 B 4 | 2051 B 4 | 2058 A 2 | 2066 B 1 | 7011 A 2 | 7014 B 4 |   |
|  2009 B 3 | 2021 A 4 | 2027 B 5 | 2035 A 2 | 2011 B 1 | 2018 A 2 | 2024 A 3 | 2030 A 3 | 2038 A 3 | 2044 B 4 | 2052 B 4 | 2060 A 3 | 2067 B 1 | 7002 A 2 | 7015 A 3 |   |
|  2012 B 4 | 2022 B 4 | 2028 A 2 | 2036 B 2 | 2012 B 3 | 2019 B 2 | 2025 A 2 | 2031 A 2 | 2039 A 3 | 2046 B 4 | 2053 B 4 | 2061 A 3 | 2068 B 2 | 7003 B 1 | 7016 A 3 |   |
|  2013 B 4 | 2023 B 4 | 2031 A 1 | 2037 A 2 | 2013 B 3 | 2020 B 2 | 2026 A 2 | 2032 A 3 | 2040 A 3 | 2047 B 4 | 2059 A 3 | 2062 B 5 | 2069 A 1 | 7006 B 2 | 7018 A 3 |   |

![img-53.jpeg](img-53.jpeg)

LIST OF ELECTRICAL PARTS MODULE C

Cells

5001 4822 156 10992 117 μH

Potentiometers

3035 5322 101 10666 47 kΩ

3045 5322 101 10666 47 kΩ

NTC Resistors

3105 4822 116 30251 150 kΩ 0.5W

Fuse Resistors

3065 4822 111 10165 10 Ω

3108 4822 111 90357 33 Ω

NFR25 Resistors

3033 4822 111 30508 10 Ω

3107 4822 111 30593 3.3 Ω

|  2001 | 4822 124 22027 | 47 μF | 25 V | 2023 | 4822 122 32974 | 100 pF  |
| --- | --- | --- | --- | --- | --- | --- |
|  2002 | 4822 124 22027 | 47 μF | 25 V | 2024 | 4822 122 32974 | 100 pF  |
|  2003 | 4822 122 31759 | 22 nF |  | 2025 | 4822 122 31759 | 22 nF  |
|  2004 | 4822 121 42688 | 68 nF | 100 V | 2026 | 5322 122 32839 | 100 nF  |
|  2005 | 4822 124 22027 | 47 μF | 25 V | 2027 | 4822 122 31965 | 220 pF  |
|  2007 | 4822 122 31759 | 22 nF |  | 2028 | 4822 122 31316 | 100 pF  |
|  2008 | 4822 122 31769 | 18 pF |  | 2101 | 4822 124 22027 | 47 μF  |
|  2009 | 4822 122 31759 | 22 nF |  |  |  |   |
|  2010 | 5322 124 21749 | 10 μF | 63 V |  |  |   |
|  2011 | 5322 124 21711 | 100 μF | 25 V |  |  |   |
|  2012 | 4822 122 31759 | 22 nF |  |  |  |   |
|  2013 | 4822 122 32442 | 10 nF |  |  |  |   |
|  2014 | 5322 122 32839 | 100 nF |  |  |  |   |
|  2015 | 4822 121 51051 | 4.7 nF | 63 V |  |  |   |
|  2016 | 4822 122 32442 | 10 nF |  |  |  |   |
|  2017 | 4822 121 41876 | 220 nF | 20% 63 V |  |  |   |
|  2018 | 4822 124 22031 | 4.7 μF | 63 V |  |  |   |
|  2019 | 4822 121 41837 | 560 nF | 20% 100 V |  |  |   |
|  2020 | 5322 122 32839 | 100 nF |  |  |  |   |
|  2021 | 4822 122 31971 | 10 pF |  |  |  |   |
|  2022 | 4822 122 31759 | 22 nF |  |  |  |   |

25 V

|  0001 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 1.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 1.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.1 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 1.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |   |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

|  1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 | 11 | 12 | 13 | 14 | 15 | 16 | 17 | 18 | 19 | 20 | 21 | 22  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

|  1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 | 11 | 12 | 13 | 14 | 15 | 16 | 17 | 18 | 19 | 20 | 21 | 22  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

|  VIDEO PROC. MODULE  |
| --- |

(mode level 3)

|  1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 | 11 | 12 | 13 | 14 | 15 | 16 | 17 | 18 | 19 | 20 | 21 | 22  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

|  1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 | 11 | 12 | 13 | 14 | 15 | 16 | 17 | 18 | 19 | 20 | 21 | 22  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

|  1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 | 11 | 12 | 13 | 14 | 15 | 16 | 17 | 18 | 19 | 20 | 21 | 22  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

|  1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 | 11 | 12 | 13 | 14 | 15 | 16 | 17 | 18 | 19 | 20 | 21 | 22  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

|  1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 | 11 | 12 | 13 | 14 | 15 | 16 | 17 | 18 | 19 | 20 | 21 | 22  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

|  1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 | 11 | 12 | 13 | 14 | 15 | 16 | 17 | 18 | 19 | 20 | 21 | 22  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

|  1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 | 11 | 12 | 13 | 14 | 15 | 16 | 17 | 18 | 19 | 20 | 21 | 22  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

|  1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 | 11 | 12 | 13 | 14 | 15 | 16 | 17 | 18 | 19 | 20 | 21 | 22  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

|  1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 | 11 | 12 | 13 | 14 | 15 | 16 | 17 | 18 | 19 | 20 | 21 | 22  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

|  1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 | 11 | 12 | 13 | 14 | 15 | 16 | 17 | 18 | 19 | 20 | 21 | 22  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

|  1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 | 11 | 12 | 13 | 14 | 15 | 16 | 17 | 18 | 19 | 20 | 21 | 22  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

|  1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 | 11 | 12 | 13 | 14 | 15 | 16 | 17 | 18 | 19 | 20 | 21 | 22  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

|  1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 | 11 | 12 | 13 | 14 | 15 | 16 | 17 | 18 | 19 | 20 | 21 | 22  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

|  1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 | 11 | 12 | 13 | 14 | 15 | 16 | 17 | 18 | 19 | 20 | 21 | 22  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

|  1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 | 11 | 12 | 13 | 14 | 15 | 16 | 17 | 18 | 19 | 20 | 21 | 22  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

|  1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 | 11 | 12 | 13 | 14 | 15 | 16 | 17 | 18 | 19 | 20 | 21 | 22  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

|  1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 | 11 | 12 | 13 | 14 | 15 | 16 | 17 | 18 | 19 | 20 | 21 | 22  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

|  1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 | 11 | 12 | 13 | 14 | 15 | 16 | 17 | 18 | 19 | 20 | 21 | 22  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

|  1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 | 11 | 12 | 13 | 14 | 15 | 16 | 17 | 18 | 19 | 20 | 21 | 22  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

|  1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 | 11 | 12 | 13 | 14 | 15 | 16 | 17 | 18 | 19 | 20 | 21 | 22  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

|  1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 | 11 | 12 | 13 | 14 | 15 | 16 | 17 | 18 | 19 | 20 | 21 | 22  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

|  1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 | 11 | 12 | 13 | 14 | 15 | 16 | 17 | 18 | 19 | 20 | 21 | 22  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

|  1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 | 11 | 12 | 13 | 14 | 15 | 16 | 17 | 18 | 19 | 20 | 21 | 22  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

|  1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 | 11 | 12 | 13 | 14 | 15 | 16 | 17 | 18 | 19 | 20 | 21 | 22  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

|  1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 | 11 | 12 | 13 | 14 | 15 | 16 | 17 | 18 | 19 | 20 | 21 | 22  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

|  1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 | 11 | 12 | 13 | 14 | 15 | 16 | 17 | 18 | 19 | 20 | 21 | 22  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

|  1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 | 11 | 12 | 13 | 14 | 15 | 16 | 17 | 18 | 19 | 20 | 21 | 22  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

|  1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 | 11 | 12 | 13 | 14 | 15 | 16 | 17 | 18 | 19 | 20 | 21 | 22  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

|  1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 | 11 | 12 | 13 | 14 | 15 | 16 | 17 | 18 | 19 | 20 | 21 | 22  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

|  1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 | 11 | 12 | 13 | 14 | 15 | 16 | 17 | 18 | 19 | 20 | 21 | 22  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

|  1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 | 11 | 12 | 13 | 14 | 15 | 16 | 17 | 18 | 19 | 20 | 21 | 22  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

|  1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 | 11 | 12 | 13 | 14 | 15 | 16 | 17 | 18 | 19 | 20 | 21 | 22  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

|  1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 | 11 | 12 | 13 | 14 | 15 | 16 | 17 | 18 | 19 | 20 | 21 | 22  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

|  1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 | 11 | 12 | 13 | 14 | 15 | 16 | 17 | 18 | 19 | 20 | 21 | 22  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

|  1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 | 11 | 12 | 13 | 14 | 15 | 16 | 17 | 18 | 19 | 20 | 21 | 22  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

|  1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 | 11 | 12 | 13 | 14 | 15 | 16 | 17 | 18 | 19 | 20 | 21 | 22  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

|  1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 | 11 | 12 | 13 | 14 | 15 | 16 | 17 | 18 | 19 | 20 | 21 | 22  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

|  1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 | 11 | 12 | 13 | 14 | 15 | 16 | 17 | 18 | 19 | 20 | 21 | 22  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

|  1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 | 11 | 12 | 13 | 14 | 15 | 16 | 17 | 18 | 19 | 20 | 21 | 22  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

|  1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 | 11 | 12 | 13 | 14 | 15 | 16 | 17 | 18 | 19 | 20 | 21 | 22  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

|  1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 | 11 | 12 | 13 | 14 | 15 | 16 | 17 | 18 | 19 | 20 | 21 | 22  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

|  1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 | 11 | 12 | 13 | 14 | 15 | 16 | 17 | 18 | 19 | 20 | 21 | 22  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

|  1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 | 11 | 12 | 13 | 14 | 15 | 16 | 17 | 18 | 19 | 20 | 21 | 22  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

|  1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 | 11 | 12 | 13 | 14 | 15 | 16 | 17 | 18 | 19 | 20 | 21 | 22  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

|  1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 | 11 | 12 | 13 | 14 | 15 | 16 | 17 | 18 | 19 | 20 | 21 | 22  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

|  1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 | 11 | 12 | 13 | 14 | 15 | 16 | 17 | 18 | 19 | 20 | 21 | 22  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

|  1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 | 11 | 12 | 13 | 14 | 15 | 16 | 17 | 18 | 19 | 20 | 21 | 22  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

|  1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 | 11 | 12 | 13 | 14 | 15 | 16 | 17 | 18 | 19 | 20 | 21 | 22  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

|  1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 | 11 | 12 | 13 | 14 | 15 | 16 | 17 | 18 | 19 | 20 | 21 | 22  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

|  1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 | 11 | 12 | 13 | 14 | 15 | 16 | 17 | 18 | 19 | 20 | 21 | 22  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

|  1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 | 11 | 12 | 13 | 14 | 15 | 16 | 17 | 18 | 19 | 20 | 21 | 22  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

|  1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 | 11 | 12 | 13 | 14 | 15 | 16 | 17 | 18 | 19 | 20 | 21 | 22  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

|  1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 | 11 | 12 | 13 | 14 | 15 | 16 | 17 | 18 | 19 | 20 | 21 | 22  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

|  1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 | 11 | 12 | 13 | 14 | 15 | 16 | 17 | 18 | 19 | 20 | 21 | 22  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

|  1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 | 11 | 12 | 13 | 14 | 15 | 16 | 17 | 18 | 19 | 20 | 21 | 22  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

|  1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 | 11 | 12 | 13 | 14 | 15 | 16 | 17 | 18 | 19 | 20 | 21 | 22  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

|  1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 | 11 | 12 | 13 | 14 | 15 | 16 | 17 | 18 | 19 | 20 | 21 | 22  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

|  1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 | 11 | 12 | 13 | 14 | 15 | 16 | 17 | 18 | 19 | 20 | 21 | 22  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

|  1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 | 11 | 12 | 13 | 14 | 15 | 16 | 17 | 18 | 19 | 20 | 21 | 22  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

|  1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 | 11 | 12 | 13 | 14 | 15 | 16 | 17 | 18 | 19 | 20 | 21 | 22  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

|  1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 | 11 | 12 | 13 | 14 | 15 | 16 | 17 | 18 | 19 | 20 | 21 | 22  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

|  1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 | 11 | 12 | 13 | 14 | 15 | 16 | 17 | 18 | 19 | 20 | 21 | 22  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

|  1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 | 11 | 12 | 13 | 14 | 15 | 16 | 17 | 18 | 19 | 20 | 21 | 22  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

|  1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 | 11 | 12 | 13 | 14 | 15 | 16 | 17 | 18 | 19 | 20 | 21 | 22  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

|  1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 | 11 | 12 | 13 | 14 | 15 | 16 | 17 | 18 | 19 | 20 | 21 | 22  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

|  1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 | 11 | 12 | 13 | 14 | 15 | 16 | 17 | 18 | 19 | 20 | 21 | 22  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

|  1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 | 11 | 12 | 13 | 14 | 15 | 16 | 17 | 18 | 19 | 20 | 21 | 22  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |[{"box_2d": [107, 831, 954, 841], "label": "table", "caption": "<table><tr><td>1</td><td>2</td><td>3</td><td>4</td><td>5</td><td>6</td><td>7</td><td>8</td><td>9</td><td>10</td><td>11</td><td>12</td><td>13</td><td>14</td><td>15</td><td>16</td><td>17</td><td>18</td><td>19</td><td>20</td><td>21</td><td>22</td

2023 0 7 2024 212 2026 0 5 2041 M18 2045 215 2049 116 2103 215 2127 0 5 2111 0 8 2105 0 8 2112 117 2124 M18 2128 625 2132 0 4 2136 625 2140 0 4 2050 0 4 2054 0 10 2058 714 2060 0 7 2058 0 8 2070 1016 2050 M23 2054 215 2058 418 2102 M13 2108 M11
2021 0 4 2024 212 2030 0 5 2042 M18 2045 216 2109 0 5 2104 0 7 2108 0 8 2110 0 8 2112 0 8 2115 0 8 2118 0 8 2120 0 8 2123 0 8 2125 0 8 2128 0 8 2130 0 8 2133 0 8 2134 0 8 2135 0 8 2136 0 8 2137 0 8 2138 0 8 2139 0 8 2140 0 8 2141 0 8 2142 0 8 2143 0 8 2144 0 8 2145 0 8 2146 0 8 2147 0 8 2148 0 8 2149 0 8 2150 0 8 2151 0 8 2152 0 8 2153 0 8 2154 0 8 2155 0 8 2156 0 8 2157 0 8 2158 0 8 2159 0 8 2160 0 8 2161 0 8 2162 0 8 2163 0 8 2164 0 8 2165 0 8 2166 0 8 2167 0 8 2168 0 8 2169 0 8 2170 0 8 2171 0 8 2172 0 8 2173 0 8 2174 0 8 2175 0 8 2176 0 8 2177 0 8 2178 0 8 2179 0 8 2180 0 8 2181 0 8 2182 0 8 2183 0 8 2184 0 8 2185 0 8 2186 0 8 2187 0 8 2188 0 8 2189 0 8 2190 0 8 2191 0 8 2192 0 8 2193 0 8 2194 0 8 2195 0 8 2196 0 8 2197 0 8 2198 0 8 2199 0 8 2200 0 8 2201 0 8 2202 0 8 2203 0 8 2204 0 8 2205 0 8 2206 0 8 2207 0 8 2208 0 8 2209 0 8 2210 0 8 2211 0 8 2212 0 8 2213 0 8 2214 0 8 2215 0 8 2216 0 8 2217 0 8 2218 0 8 2219 0 8 2220 0 8 2221 0 8 2222 0 8 2223 0 8 2224 0 8 2225 0 8 2226 0 8 2227 0 8 2228 0 8 2229 0 8 2230 0 8 2231 0 8 2232 0 8 2233 0 8 2234 0 8 2235 0 8 2236 0 8 2237 0 8 2238 0 8 2239 0 8 2240 0 8 2241 0 8 2242 0 8 2243 0 8 2244 0 8 2245 0 8 2246 0 8 2247 0 8 2248 0 8 2249 0 8 2250 0 8 2251 0 8 2252 0 8 2253 0 8 2254 0 8 2255 0 8 2256 0 8 2257 0 8 2258 0 8 2259 0 8 2260 0 8 2261 0 8 2262 0 8 2263 0 8 2264 0 8 2265 0 8 2266 0 8 2267 0 8 2268 0 8 2269 0 8 2270 0 8 2271 0 8 2272 0 8 2273 0 8 2274 0 8 2275 0 8 2276 0 8 2277 0 8 2278 0 8 2279 0 8 2280 0 8 2281 0 8 2282 0 8 2283 0 8 2284 0 8 2285 0 8 2286 0 8 2287 0 8 2288 0 8 2289 0 8 2290 0 8 2291 0 8 2292 0 8 2293 0 8 2294 0 8 2295 0 8 2296 0 8 2297 0 8 2298 0 8 2299 0 8 2300 0 8 2301 0 8 2302 0 8 2303 0 8 2304 0 8 2305 0 8 2306 0 8 2307 0 8 2308 0 8 2309 0 8 2310 0 8 2311 0 8 2312 0 8 2313 0 8 2314 0 8 2315 0 8 2316 0 8 2317 0 8 2318 0 8 2319 0 8 2320 0 8 2321 0 8 2322 0 8 2323 0 8 2324 0 8 2325 0 8 2326 0 8 2327 0 8 2328 0 8 2329 0 8 2330 0 8 2331 0 8 2332 0 8 2333 0 8 2334 0 8 2335 0 8 2336 0 8 2337 0 8 2338 0 8 2339 0 8 2340 0 8 2341 0 8 2342 0 8 2343 0 8 2344 0 8 2345 0 8 2346 0 8 2347 0 8 2348 0 8 2349 0 8 2350 0 8 2351 0 8 2352 0 8 2353 0 8 2354 0 8 2355 0 8 2356 0 8 2357 0 8 2358 0 8 2359 0 8 2360 0 8 2361 0 8 2362 0 8 2363 0 8 2364 0 8 2365 0 8 2366 0 8 2367 0 8 2368 0 8 2369 0 8 2370 0 8 2371 0 8 2372 0 8 2373 0 8 2374 0 8 2375 0 8 2376 0 8 2377 0 8 2378 0 8 2379 0 8 2380 0 8 2381 0 8 2382 0 8 2383 0 8 2384 0 8 2385 0 8 2386 0 8 2387 0 8 2388 0 8 2389 0 8 2390 0 8 2391 0 8 2392 0 8 2393 0 8 2394 0 8 2395 0 8 2396 0 8 2397 0 8 2398 0 8 2399 0 8 2400 0 8 2401 0 8 2402 0 8 2403 0 8 2404 0 8 2405 0 8 2406 0 8 2407 0 8 2408 0 8 2409 0 8 2410 0 8 2411 0 8 2412 0 8 2413 0 8 2414 0 8 2415 0 8 2416 0 8 2417 0 8 2418 0 8 2419 0 8 2420 0 8 2421 0 8 2422 0 8 2423 0 8 2424 0 8 2425 0 8 2426 0 8 2427 0 8 2428 0 8 2429 0 8 2430 0 8 2431 0 8 2432 0 8 2433 0 8 2434 0 8 2435 0 8 2436 0 8 2437 0 8 2438 0 8 2439 0 8 2440 0 8 2441 0 8 2442 0 8 2443 0 8 2444 0 8 2445 0 8 2446 0 8 2447 0 8 2448 0 8 2449 0 8 2450 0 8 2451 0 8 2452 0 8 2453 0 8 2454 0 8 2455 0 8 2456 0 8 2457 0 8 2458 0 8 2459 0 8 2460 0 8 2461 0 8 2462 0 8 2463 0 8 2464 0 8 2465 0 8 2466 0 8 2467 0 8 2468 0 8 2469 0 8 2470 0 8 2471 0 8 2472 0 8 2473 0 8 2474 0 8 2475 0 8 2476 0 8 2477 0 8 2478 0 8 2479 0 8 2480 0 8 2481 0 8 2482 0 8 2483 0 8 2484 0 8 2485 0 8 2486 0 8 2487 0 8 2488 0 8 2489 0 8 2490 0 8 2491 0 8 2492 0 8 2493 0 8 2494 0 8 2495 0 8 2496 0 8 2497 0 8 2498 0 8 2499 0 8 2500 0 8 2501 0 8 2502 0 8 2503 0 8 2504 0 8 2505 0 8 2506 0 8 2507 0 8 2508 0 8 2509 0 8 2510 0 8 2511 0 8 2512 0 8 2513 0 8 2514 0 8 2515 0 8 2516 0 8 2517 0 8 2518 0 8 2519 0 8 2520 0 8 2521 0 8 2522 0 8 2523 0 8 2524 0 8 2525 0 8 2526 0 8 2527 0 8 2528 0 8 2529 0 8 2530 0 8 2531 0 8 2532 0 8 2533 0 8 2534 0 8 2535 0 8 2536 0 8 2537 0 8 2538 0 8 2539 0 8 2540 0 8 2541 0 8 2542 0 8 2543 0 8 2544 0 8 2545 0 8 2546 0 8 2547 0 8 2548 0 8 2549 0 8 2550 0 8 2551 0 8 2552 0 8 2553 0 8 2554 0 8 2555 0 8 2556 0 8 2557 0 8 2558 0 8 2559 0 8 2560 0 8 2561 0 8 2562 0 8 2563 0 8 2564 0 8 2565 0 8 2566 0 8 2567 0 8 2568 0 8 2569 0 8 2570 0 8 2571 0 8 2572 0 8 2573 0 8 2574 0 8 2575 0 8 2576 0 8 2577 0 8 2578 0 8 2579 0 8 2580 0 8 2581 0 8 2582 0 8 2583 0 8 2584 0 8 2585 0 8 2586 0 8 2587 0 8 2588 0 8 2589 0 8 2590 0 8 2591 0 8 2592 0 8 2593 0 8 2594 0 8 2595 0 8 2596 0 8 2597 0 8 2598 0 8 2599 0 8 2600 0 8 2601 0 8 2602 0 8 2603 0 8 2604 0 8 2605 0 8 2606 0 8 2607 0 8 2608 0 8 2609 0 8 2610 0 8 2611 0 8 2612 0 8 2613 0 8 2614 0 8 2615 0 8 2616 0 8 2617 0 8 2618 0 8 2619 0 8 2620 0 8 2621 0 8 2622 0 8 2623 0 8 2624 0 8 2625 0 8 2626 0 8 2627 0 8 2628 0 8 2629 0 8 2630 0 8 2631 0 8 2632 0 8 2633 0 8 2634 0 8 2635 0 8 2636 0 8 2637 0 8 2638 0 8 2639 0 8 2640 0 8 2641 0 8 2642 0 8 2643 0 8 2644 0 8 2645 0 8 2646 0 8 2647 0 8 2648 0 8 2649 0 8 2650 0 8 2651 0 8 2652 0 8 2653 0 8 2654 0 8 2655 0 8 2656 0 8 2657 0 8 2658 0 8 2659 0 8 2660 0 8 2661 0 8 2662 0 8 2663 0 8 2664 0 8 2665 0 8 2666 0 8 2667 0 8 2668 0 8 2669 0 8 2670 0 8 2671 0 8 2672 0 8 2673 0 8 2674 0 8 2675 0 8 2676 0 8 2677 0 8 2678 0 8 2679 0 8 2680 0 8 2681 0 8 2682 0 8 2683 0 8 2684 0 8 2685 0 8 2686 0 8 2687 0 8 2688 0 8 2689 0 8 2690 0 8 2691 0 8 2692 0 8 2693 0 8 2694 0 8 2695 0 8 2696 0 8 2697 0 8 2698 0 8 2699 0 8 2700 0 8 2701 0 8 2702 0 8 2703 0 8 2704 0 8 2705 0 8 2706 0 8 2707 0 8 2708 0 8 2709 0 8 2710 0 8 2711 0 8 2712 0 8 2713 0 8 2714 0 8 2715 0 8 2716 0 8 2717 0 8 2718 0 8 2719 0 8 2720 0 8 2721 0 8 2722 0 8 2723 0 8 2724 0 8 2725 0 8 2726 0 8 2727 0 8 2728 0 8 2729 0 8 2730 0 8 2731 0 8 2732 0 8 2733 0 8 2734 0 8 2735 0 8 2736 0 8 2737 0 8 2738 0 8 2739 0 8 2740 0 8 2741 0 8 2742 0 8 2743 0 8 2744 0 8 2745 0 8 2746 0 8 2747 0 8 2748 0 8 2749 0 8 2750 0 8 2751 0 8 2752 0 8 2753 0 8 2754 0 8 2755 0 8 2756 0 8 2757 0 8 2758 0 8 2759 0 8 2760 0 8 2761 0 8 2762 0 8 2763 0 8 2764 0 8 2765 0 8 2766 0 8 2767 0 8 2768 0 8 2769 0 8 2770 0 8 2771 0 8 2772 0 8 2773 0 8 2774 0 8 2775 0 8 2776 0 8 2777 0 8 2778 0 8 2779 0 8 2780 0 8 2781 0 8 2782 0 8 2783 0 8 2784 0 8 2785 0 8 2786 0 8 2787 0 8 2788 0 8 2789 0 8 2790 0 8 2791 0 8 2792 0 8 2793 0 8 2794 0 8 2795 0 8 2796 0 8 2797 0 8 2798 0 8 2799 0 8 2800 0 8 2801 0 8 2802 0 8 2803 0 8 2804 0 8 2805 0 8 2806 0 8 2807 0 8 2808 0 8 2809 0 8 2810 0 8 2811 0 8 2812 0 8 2813 0 8 2814 0 8 2815 0 8 2816 0 8 2817 0 8 2818 0 8 2819 0 8 2820 0 8 2821 0 8 2822 0 8 2823 0 8 2824 0 8 2825 0 8 2826 0 8 2827 0 8 2828 0 8 2829 0 8 2830 0 8 2831 0 8 2832 0 8 2833 0 8 2834 0 8 2835 0 8 2836 0 8 2837 0 8 2838 0 8 2839 0 8 2840 0 8 2841 0 8 2842 0 8 2843 0 8 2844 0 8 2845 0 8 2846 0 8 2847 0 8 2848 0 8 2849 0 8 2850 0 8 2851 0 8 2852 0 8 2853 0 8 2854 0 8 2855 0 8 2856 0 8 2857 0 8 2858 0 8 2859 0 8 2860 0 8 2861 0 8 2862 0 8 2863 0 8 2864 0 8 2865 0 8 2866 0 8 2867 0 8 2868 0 8 2869 0 8 2870 0 8 2871 0 8 2872 0 8 2873 0 8 2874 0 8 2875 0 8 2876 0 8 2877 0 8 2878 0 8 2879 0 8 2880 0 8 2881 0 8 2882 0 8 2883 0 8 2884 0 8 2885 0 8 2886 0 8 2887 0 8 2888 0 8 2889 0 8 2890 0 8 2891 0 8 2892 0 8 2893 0 8 2894 0 8 2895 0 8 2896 0 8 2897 0 8 2898 0 8 2899 0 8 2900 0 8 2901 0 8 2902 0 8 2903 0 8 2904 0 8 2905 0 8 2906 0 8 2907 0 8 2908 0 8 2909 0 8 2910 0 8 2911 0 8 2912 0 8 2913 0 8 2914 0 8 2915 0 8 2916 0 8 2917 0 8 2918 0 8 2919 0 8 2920 0 8 2921 0 8 2922 0 8 2923 0 8 2924 0 8 2925 0 8 2926 0 8 2927 0 8 2928 0 8 2929 0 8 2930 0 8 2931 0 8 2932 0 8 2933 0 8 2934 0 8 2935 0 8 2936 0 8 2937 0 8 2938 0 8 2939 0 8 2940 0 8 2941 0 8 2942 0 8 2943 0 8 2944 0 8 2945 0 8 2946 0 8 2947 0 8 2948 0 8 2949 0 8 2950 0 8 2951 0 8 2952 0 8 2953 0 8 2954 0 8 2955 0 8 2956 0 8 2957 0 8 2958 0 8 2959 0 8 2960 0 8 2961 0 8 2962 0 8 2963 0 8 2964 0 8 2965 0 8 2966 0 8 2967 0 8 2968 0 8 2969 0 8 2970 0 8 2971 0 8 2972 0 8 2973 0 8 2974 0 8 2975 0 8 2976 0 8 2977 0 8 2978 0 8 2979 0 8 2980 0 8 2981 0 8 2982 0 8 2983 0 8 2984 0 8 2985 0 8 2986 0 8 2987 0 8 2988 0 8 2989 0 8 2990 0 8 2991 0 8 2992 0 8 2993 0 8 2994 0 8 2995 0 8 2996 0 8 2997 0 8 2998 0 8 2999 0 8 3000[{"}]

![img-54.jpeg](img-54.jpeg)

CS 6 870

2123 1428 2123 1000 2123 4 2123 1000 2123 4 2023 1 1 2023 2 1 2023 3 1 2023 4 1 2023 5 1 2023 6 1 2023 7 1 2023 8 1 2023 9 1 2023 10 1 2023 11 1 2023 12 1 2023 13 1 2023 14 1 2023 15 1 2023 16 1 2023 17 1 2023 18 1 2023 19 1 2023 20 1 2023 21 1 2023 22 1 2023 23 1 2023 24 1 2023 25 1 2023 26 1 2023 27 1 2023 28 1 2023 29 1 2023 30 1 2023 31 1 2023 32 1 2023 33 1 2023 34 1 2023 35 1 2023 36 1 2023 37 1 2023 38 1 2023 39 1 2023 40 1 2023 41 1 2023 42 1 2023 43 1 2023 44 1 2023 45 1 2023 46 1 2023 47 1 2023 48 1 2023 49 1 2023 50 1 2023 51 1 2023 52 1 2023 53 1 2023 54 1 2023 55 1 2023 56 1 2023 57 1 2023 58 1 2023 59 1 2023 60 1 2023 61 1 2023 62 1 2023 63 1 2023 64 1 2023 65 1 2023 66 1 2023 67 1 2023 68 1 2023 69 1 2023 70 1 2023 71 1 2023 72 1 2023 73 1 2023 74 1 2023 75 1 2023 76 1 2023 77 1 2023 78 1 2023 79 1 2023 80 1 2023 81 1 2023 82 1 2023 83 1 2023 84 1 2023 85 1 2023 86 1 2023 87 1 2023 88 1 2023 89 1 2023 90 1 2023 91 1 2023 92 1 2023 93 1 2023 94 1 2023 95 1 2023 96 1 2023 97 1 2023 98 1 2023 99 1 2023 100

![img-55.jpeg](img-55.jpeg)

0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31 32 33

D

A

B

C

D

E

F

G

H

I

J

K

L

M

N

O

P

Q

R

S

T

U

V

W

X

Y

Z

A

B

C

D

REF SOURCE MODULE

D

(MOD LEVEL 2)

2030 A 6 2130 A 4 2136 B 3 2033 A 4 6011 B 5 7018 B 6 7021 B 5 7051 A 7 7054 A 6 7057 B 6 7061 A 4 7064 A 2 7067 A 2
2101 B 5 2106 B 3 2001 B 5 5001 A 3 6010 B 5 7010 B 5 7022 B 1 7052 A 7 7054 A 5 7056 A 5 7062 A 3 7066 A 1
2102 B 5 2106 B 3 2002 B 4 5002 A 6 6015 A 3 7005 B 5 7009 B 1 7053 A 7 7056 B 7 7066 A 5 7060 A 3 7066 A 1 7068 B 1

![img-56.jpeg](img-56.jpeg)

2029 B 7 2028 A 7 2042 A 4 2048 B 4 2104 B 6 2110 B 7 2116 A 5 2122 B 3 2129 B 7 3030 B 5 3036 A 6 3062 A 7 3068 B 7 3078 B 4 3094 B 4 3106 A 4 3106 A 4 3130 A 3
2021 B 5 2027 A 7 2043 A 4 2046 A 4 2105 B 6 2111 A 7 2117 A 3 2124 A 2 2130 A 5 3051 B 5 3057 A 6 3063 B 7 3069 B 7 3079 B 4 3095 A 3 3101 A 4 3107 A 4 3123 B 3
2022 A 6 2028 B 7 2044 B 4 2100 A 5 2108 B 7 2112 A 7 2118 A 2 2125 A 5 3046 B 6 3052 A 7 3058 A 6 3064 A 7 3073 B 6 3090 A 5 3096 A 5 3102 A 4 3108 A 4
2023 B 6 2038 A 4 2045 B 4 2101 A 6 2107 B 7 2115 A 7 2119 A 4 2126 A 1 3047 A 6 3053 A 7 3059 B 6 3065 A 7 3075 A 5 3091 A 3 3097 A 3 3103 A 4 3130 B 3
2024 A 7 2046 A 4 2046 A 3 2102 A 6 2108 B 7 2114 A 6 2120 A 4 2127 A 1 3048 B 5 3054 A 6 3060 B 5 3066 A 7 3079 A 5 3092 B 4 3098 B 3 3104 A 5 3101 B 3
2025 A 7 2041 A 4 2047 A 3 2103 A 6 2109 A 7 2115 A 5 2121 B 7 2128 B 1 3049 B 5 3055 A 6 3061 B 7 3067 A 7 3077 A 3 3093 B 4 3099 A 3 3105 A 4 3132 B 3

![img-57.jpeg](img-57.jpeg)

LIST OF ELECTRICAL PARTS MODULE D

Crystals

|  5001 | 4822 242 70362 | 5 MHz  |
| --- | --- | --- |
|  5002 | 4822 242 71664 | 10 MHz  |

NFR25 Resistors

|  3001 | 4822 111 30483 | 1 Ω  |
| --- | --- | --- |
|  3002 | 4822 111 30483 | 1 Ω  |
|  3003 | 4822 111 30483 | 1 Ω  |

|  2020  |
| --- |
|  2021  |
|  2022  |
|  2023  |
|  2024  |
|  2025  |
|  2026  |
|  2027  |
|  2028  |
|  2030  |
|  2039  |
|  2040  |
|  2041  |
|  2042  |
|  2043  |
|  2044  |
|  2045  |
|  2046  |
|  2047  |
|  2048  |
|  2049  |

|  4822 121 42915 | 330 pF  |
| --- | --- |
|  4822 122 33012 | 150 nF  |
|  4822 122 31784 | 4.7 nF  |
|  4822 122 32542 | 47 nF  |
|  5322 122 32839 | 100 nF  |
|  4822 122 32976 | 470 pF  |
|  4822 122 32974 | 100 pF  |
|  4822 122 32972 | 1 nF  |
|  4822 122 32972 | 1 nF  |
|  4822 124 20942 | 1.5 μF  |
|  4822 122 33007 | 330 nF  |
|  4822 122 32972 | 1 nF  |
|  4822 122 32442 | 10 nF  |
|  5322 122 31848 | 33 nF  |
|  4822 122 32972 | 1 nF  |
|  4822 122 31644 | 2.2 nF  |
|  4822 122 33012 | 150 nF  |
|  4822 122 31766 | 120 pF  |
|  4822 122 32974 | 100 pF  |
|  4822 122 32442 | 10 nF  |
|  4822 122 33008 | 120 nF  |

|  50 V  |
| --- |
|  |
|  |
|  |
|  |
|  |
|  |
|  |
|  |
|  |
|  |
|  |
|  |
|  |
|  |
|  |
|  |
|  |
|  |
|  |
|  |
|  |
|  |
|  |
|  |
|  |
|  |
|  |
|  |
|  |
|  |
|  |
|  |
|  |
|  |

|  2100  |
| --- |
|  2101  |
|  2102  |
|  2103  |
|  2104  |
|  2105  |
|  2106  |
|  2107  |
|  2108  |
|  2109  |
|  2110  |
|  2111  |
|  2112  |
|  2113  |
|  2114  |
|  2115  |
|  2116  |
|  2117  |
|  2118  |
|  2119  |
|  2120  |

|  5322 122 32839 | 100 nF  |
| --- | --- |
|  5322 122 32839 | 100 nF  |
|  5322 122 32839 | 100 nF  |
|  5322 122 32839 | 100 nF  |
|  5322 122 32839 | 100 nF  |
|  5322 122 32839 | 100 nF  |

|  2121  |
| --- |
|  2122  |
|  2124  |
|  2125  |
|  2126  |
|  2127  |
|  2128  |
|  2129  |
|  2130  |
|  2131  |
|  2132  |
|  2133  |
|  2134  |
|  2135  |
|  2136  |

|  5322 122 32839 | 100 nF  |
| --- | --- |
|  5322 122 32839 | 100 nF  |
|  5322 122 32839 | 100 nF  |
|  5322 122 32839 | 100 nF  |
|  5322 122 32839 | 100 nF  |

|  6.3 V  |
| --- |
|  16 V  |
|  16 V  |
|  16 V  |
|  10 V  |
|  10 V  |

CS 7 840

SLIDE DRIVE MODULE

E

(MOD LEVEL 3)

![img-58.jpeg](img-58.jpeg)

![img-59.jpeg](img-59.jpeg)

LIST OF ELECTRICAL PARTS MODULE E

NFR25 Resistors

3026 4822 111 30483 1 Ω

3027 4822 111 30483 1 Ω

|  2001 | 4822 122 30053 | 680 pF | 100 V  |
| --- | --- | --- | --- |
|  2002 | 4822 121 50959 | 3.9 nF | 63 V  |
|  2007 | 4822 124 22027 | 47 μF | 25 V  |
|  2008 | 4822 124 22027 | 47 μF | 25 V  |

CS 7 841

|  1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 | 11 | 12 | 13 | 14 | 15 | 16 | 17 | 18 | 19 | 20 | 21 | 22 | 23 | 24 | 25 | 26 | 27 | 28 | 29 | 30 | 31 | 32 | 33 | 34 | 35 | 36 | 37 | 38 | 39 | 40 | 41 | 42 | 43 | 44 | 45 | 46 | 47 | 48 | 49 | 50 | 51 | 52 | 53 | 54 | 55 | 56 | 57 | 58 | 59 | 60 | 61 | 62 | 63 | 64 | 65 | 66 | 67 | 68 | 69 | 70 | 71 | 72 | 73 | 74 | 75 | 76 | 77 | 78 | 79 | 80 | 81 | 82 | 83 | 84 | 85 | 86 | 87 | 88 | 89 | 90 | 91 | 92 | 93 | 94 | 95 | 96 | 97 | 98 | 99 | 100 | 101 | 102 | 103 | 104 | 105 | 106 | 107 | 108 | 109 | 110 | 111 | 112 | 113 | 114 | 115 | 116 | 117 | 118 | 119 | 120 | 121 | 122 | 123 | 124 | 125 | 126 | 127 | 128 | 129 | 130 | 131 | 132 | 133 | 134 | 135 | 136 | 137 | 138 | 139 | 140 | 141 | 142 | 143 | 144 | 145 | 146 | 147 | 148 | 149 | 150 | 151 | 152 | 153 | 154 | 155 | 156 | 157 | 158 | 159 | 160 | 161 | 162 | 163 | 164 | 165 | 166 | 167 | 168 | 169 | 170 | 171 | 172 | 173 | 174 | 175 | 176 | 177 | 178 | 179 | 180 | 181 | 182 | 183 | 184 | 185 | 186 | 187 | 188 | 189 | 190 | 191 | 192 | 193 | 194 | 195 | 196 | 197 | 198 | 199 | 200 | 201 | 202 | 203 | 204 | 205 | 206 | 207 | 208 | 209 | 210 | 211 | 212 | 213 | 214 | 215 | 216 | 217 | 218 | 219 | 220 | 221 | 222 | 223 | 224 | 225 | 226 | 227 | 228 | 229 | 230 | 231 | 232 | 233 | 234 | 235 | 236 | 237 | 238 | 239 | 240 | 241 | 242 | 243 | 244 | 245 | 246 | 247 | 248 | 249 | 250 | 251 | 252 | 253 | 254 | 255 | 256 | 257 | 258 | 259 | 260 | 261 | 262 | 263 | 264 | 265 | 266 | 267 | 268 | 269 | 270 | 271 | 272 | 273 | 274 | 275 | 276 | 277 | 278 | 279 | 280 | 281 | 282 | 283 | 284 | 285 | 286 | 287 | 288 | 289 | 290 | 291 | 292 | 293 | 294 | 295 | 296 | 297 | 298 | 299 | 300 | 301 | 302 | 303 | 304 | 305 | 306 | 307 | 308 | 309 | 310 | 311 | 312 | 313 | 314 | 315 | 316 | 317 | 318 | 319 | 320 | 321 | 322 | 323 | 324 | 325 | 326 | 327 | 328 | 329 | 330 | 331 | 332 | 333 | 334 | 335 | 336 | 337 | 338 | 339 | 340 | 341 | 342 | 343 | 344 | 345 | 346 | 347 | 348 | 349 | 350 | 351 | 352 | 353 | 354 | 355 | 356 | 357 | 358 | 359 | 360 | 361 | 362 | 363 | 364 | 365 | 366 | 367 | 368 | 369 | 370 | 371 | 372 | 373 | 374 | 375 | 376 | 377 | 378 | 379 | 380 | 381 | 382 | 383 | 384 | 385 | 386 | 387 | 388 | 389 | 390 | 391 | 392 | 393 | 394 | 395 | 396 | 397 | 398 | 399 | 400 | 401 | 402 | 403 | 404 | 405 | 406 | 407 | 408 | 409 | 410 | 411 | 412 | 413 | 414 | 415 | 416 | 417 | 418 | 419 | 420 | 421 | 422 | 423 | 424 | 425 | 426 | 427 | 428 | 429 | 430 | 431 | 432 | 433 | 434 | 435 | 436 | 437 | 438 | 439 | 440 | 441 | 442 | 443 | 444 | 445 | 446 | 447 | 448 | 449 | 450 | 451 | 452 | 453 | 454 | 455 | 456 | 457 | 458 | 459 | 460 | 461 | 462 | 463 | 464 | 465 | 466 | 467 | 468 | 469 | 470 | 471 | 472 | 473 | 474 | 475 | 476 | 477 | 478 | 479 | 480 | 481 | 482 | 483 | 484 | 485 | 486 | 487 | 488 | 489 | 490 | 491 | 492 | 493 | 494 | 495 | 496 | 497 | 498 | 499 | 500 | 501 | 502 | 503 | 504 | 505 | 506 | 507 | 508 | 509 | 510 | 511 | 512 | 513 | 514 | 515 | 516 | 517 | 518 | 519 | 520 | 521 | 522 | 523 | 524 | 525 | 526 | 527 | 528 | 529 | 530 | 531 | 532 | 533 | 534 | 535 | 536 | 537 | 538 | 539 | 540 | 541 | 542 | 543 | 544 | 545 | 546 | 547 | 548 | 549 | 550 | 551 | 552 | 553 | 554 | 555 | 556 | 557 | 558 | 559 | 560 | 561 | 562 | 563 | 564 | 565 | 566 | 567 | 568 | 569 | 570 | 571 | 572 | 573 | 574 | 575 | 576 | 577 | 578 | 579 | 580 | 581 | 582 | 583 | 584 | 585 | 586 | 587 | 588 | 589 | 590 | 591 | 592 | 593 | 594 | 595 | 596 | 597 | 598 | 599 | 600 | 601 | 602 | 603 | 604 | 605 | 606 | 607 | 608 | 609 | 610 | 611 | 612 | 613 | 614 | 615 | 616 | 617 | 618 | 619 | 620 | 621 | 622 | 623 | 624 | 625 | 626 | 627 | 628 | 629 | 630 | 631 | 632 | 633 | 634 | 635 | 636 | 637 | 638 | 639 | 640 | 641 | 642 | 643 | 644 | 645 | 646 | 647 | 648 | 649 | 650 | 651 | 652 | 653 | 654 | 655 | 656 | 657 | 658 | 659 | 660 | 661 | 662 | 663 | 664 | 665 | 666 | 667 | 668 | 669 | 670 | 671 | 672 | 673 | 674 | 675 | 676 | 677 | 678 | 679 | 680 | 681 | 682 | 683 | 684 | 685 | 686 | 687 | 688 | 689 | 690 | 691 | 692 | 693 | 694 | 695 | 696 | 697 | 698 | 699 | 700 | 701 | 702 | 703 | 704 | 705 | 706 | 707 | 708 | 709 | 710 | 711 | 712 | 713 | 714 | 715 | 716 | 717 | 718 | 719 | 720 | 721 | 722 | 723 | 724 | 725 | 726 | 727 | 728 | 729 | 730 | 731 | 732 | 733 | 734 | 735 | 736 | 737 | 738 | 739 | 740 | 741 | 742 | 743 | 744 | 745 | 746 | 747 | 748 | 749 | 750 | 751 | 752 | 753 | 754 | 755 | 756 | 757 | 758 | 759 | 760 | 761 | 762 | 763 | 764 | 765 | 766 | 767 | 768 | 769 | 770 | 771 | 772 | 773 | 774 | 775 | 776 | 777 | 778 | 779 | 780 | 781 | 782 | 783 | 784 | 785 | 786 | 787 | 788 | 789 | 790 | 791 | 792 | 793 | 794 | 795 | 796 | 797 | 798 | 799 | 800 | 801 | 802 | 803 | 804 | 805 | 806 | 807 | 808 | 809 | 810 | 811 | 812 | 813 | 814 | 815 | 816 | 817 | 818 | 819 | 820 | 821 | 822 | 823 | 824 | 825 | 826 | 827 | 828 | 829 | 830 | 831 | 832 | 833 | 834 | 835 | 836 | 837 | 838 | 839 | 840 | 841 | 842 | 843 | 844 | 845 | 846 | 847 | 848 | 849 | 850 | 851 | 852 | 853 | 854 | 855 | 856 | 857 | 858 | 859 | 860 | 861 | 862 | 863 | 864 | 865 | 866 | 867 | 868 | 869 | 870 | 871 | 872 | 873 | 874 | 875 | 876 | 877 | 878 | 879 | 880 | 881 | 882 | 883 | 884 | 885 | 886 | 887 | 888 | 889 | 890 | 891 | 892 | 893 | 894 | 895 | 896 | 897 | 898 | 899 | 900 | 901 | 902 | 903 | 904 | 905 | 906 | 907 | 908 | 909 | 910 | 911 | 912 | 913 | 914 | 915 | 916 | 917 | 918 | 919 | 920 | 921 | 922 | 923 | 924 | 925 | 926 | 927 | 928 | 929 | 930 | 931 | 932 | 933 | 934 | 935 | 936 | 937 | 938 | 939 | 940 | 941 | 942 | 943 | 944 | 945 | 946 | 947 | 948 | 949 | 950 | 951 | 952 | 953 | 954 | 955 | 956 | 957 | 958 | 959 | 960 | 961 | 962 | 963 | 964 | 965 | 966 | 967 | 968 | 969 | 970 | 971 | 972 | 973 | 974 | 975 | 976 | 977 | 978 | 979 | 980 | 981 | 982 | 983 | 984 | 985 | 986 | 987 | 988 | 989 | 990 | 991 | 992 | 993 | 994 | 995 | 996 | 997 | 998 | 999 | 1000  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

![img-60.jpeg](img-60.jpeg)

CS 6 871

|  2001 | L | 4 | 2018 | MT | 2082 | Y | 2101 | Z | 2115 | Z | 2201 | L | 4 | 2019 | Z | 2102 | Y | 2104 | Z | 2106 | Z | 2202 | Y | 2204 | Z | 2206 | Z | 2208 | Z | 2210 | Z | 2212 | Z | 2214 | Z | 2216 | Z | 2218 | Z | 2220 | Z | 2222 | Z | 2224 | Z | 2226 | Z | 2228 | Z | 2230 | Z | 2232 | Z | 2234 | Z | 2236 | Z | 2238 | Z | 2240 | Z | 2242 | Z | 2244 | Z | 2246 | Z | 2248 | Z | 2250 | Z | 2252 | Z | 2254 | Z | 2256 | Z | 2258 | Z | 2260 | Z | 2262 | Z | 2264 | Z | 2266 | Z | 2268 | Z | 2270 | Z | 2272 | Z | 2274 | Z | 2276 | Z | 2278 | Z | 2280 | Z | 2282 | Z | 2284 | Z | 2286 | Z | 2288 | Z | 2290 | Z | 2292 | Z | 2294 | Z | 2296 | Z | 2298 | Z | 2300 | Z | 2302 | Z | 2304 | Z | 2306 | Z | 2308 | Z | 2310 | Z | 2312 | Z | 2314 | Z | 2316 | Z | 2318 | Z | 2320 | Z | 2322 | Z | 2324 | Z | 2326 | Z | 2328 | Z | 2330 | Z | 2332 | Z | 2334 | Z | 2336 | Z | 2338 | Z | 2340 | Z | 2342 | Z | 2344 | Z | 2346 | Z | 2348 | Z | 2350 | Z | 2352 | Z | 2354 | Z | 2356 | Z | 2358 | Z | 2360 | Z | 2362 | Z | 2364 | Z | 2366 | Z | 2368 | Z | 2370 | Z | 2372 | Z | 2374 | Z | 2376 | Z | 2378 | Z | 2380 | Z | 2382 | Z | 2384 | Z | 2386 | Z | 2388 | Z | 2390 | Z | 2392 | Z | 2394 | Z | 2396 | Z | 2398 | Z | 2400 | Z | 2402 | Z | 2404 | Z | 2406 | Z | 2408 | Z | 2410 | Z | 2412 | Z | 2414 | Z | 2416 | Z | 2418 | Z | 2420 | Z | 2422 | Z | 2424 | Z | 2426 | Z | 2428 | Z | 2430 | Z | 2432 | Z | 2434 | Z | 2436 | Z | 2438 | Z | 2440 | Z | 2442 | Z | 2444 | Z | 2446 | Z | 2448 | Z | 2450 | Z | 2452 | Z | 2454 | Z | 2456 | Z | 2458 | Z | 2460 | Z | 2462 | Z | 2464 | Z | 2466 | Z | 2468 | Z | 2470 | Z | 2472 | Z | 2474 | Z | 2476 | Z | 2478 | Z | 2480 | Z | 2482 | Z | 2484 | Z | 2486 | Z | 2488 | Z | 2490 | Z | 2492 | Z | 2494 | Z | 2496 | Z | 2498 | Z | 2500 | Z | 2502 | Z | 2504 | Z | 2506 | Z | 2508 | Z | 2510 | Z | 2512 | Z | 2514 | Z | 2516 | Z | 2518 | Z | 2520 | Z | 2522 | Z | 2524 | Z | 2526 | Z | 2528 | Z | 2530 | Z | 2532 | Z | 2534 | Z | 2536 | Z | 2538 | Z | 2540 | Z | 2542 | Z | 2544 | Z | 2546 | Z | 2548 | Z | 2550 | Z | 2552 | Z | 2554 | Z | 2556 | Z | 2558 | Z | 2560 | Z | 2562 | Z | 2564 | Z | 2566 | Z | 2568 | Z | 2570 | Z | 2572 | Z | 2574 | Z | 2576 | Z | 2578 | Z | 2580 | Z | 2582 | Z | 2584 | Z | 2586 | Z | 2588 | Z | 2590 | Z | 2592 | Z | 2594 | Z | 2596 | Z | 2598 | Z | 2600 | Z | 2602 | Z | 2604 | Z | 2606 | Z | 2608 | Z | 2610 | Z | 2612 | Z | 2614 | Z | 2616 | Z | 2618 | Z | 2620 | Z | 2622 | Z | 2624 | Z | 2626 | Z | 2628 | Z | 2630 | Z | 2632 | Z | 2634 | Z | 2636 | Z | 2638 | Z | 2640 | Z | 2642 | Z | 2644 | Z | 2646 | Z | 2648 | Z | 2650 | Z | 2652 | Z | 2654 | Z | 2656 | Z | 2658 | Z | 2660 | Z | 2662 | Z | 2664 | Z | 2666 | Z | 2668 | Z | 2670 | Z | 2672 | Z | 2674 | Z | 2676 | Z | 2678 | Z | 2680 | Z | 2682 | Z | 2684 | Z | 2686 | Z | 2688 | Z | 2690 | Z | 2692 | Z | 2694 | Z | 2696 | Z | 2698 | Z | 2700 | Z | 2702 | Z | 2704 | Z | 2706 | Z | 2708 | Z | 2710 | Z | 2712 | Z | 2714 | Z | 2716 | Z | 2718 | Z | 2720 | Z | 2722 | Z | 2724 | Z | 2726 | Z | 2728 | Z | 2730 | Z | 2732 | Z | 2734 | Z | 2736 | Z | 2738 | Z | 2740 | Z | 2742 | Z | 2744 | Z | 2746 | Z | 2748 | Z | 2750 | Z | 2752 | Z | 2754 | Z | 2756 | Z | 2758 | Z | 2760 | Z | 2762 | Z | 2764 | Z | 2766 | Z | 2768 | Z | 2770 | Z | 2772 | Z | 2774 | Z | 2776 | Z | 2778 | Z | 2780 | Z | 2782 | Z | 2784 | Z | 2786 | Z | 2788 | Z | 2790 | Z | 2792 | Z | 2794 | Z | 2796 | Z | 2798 | Z | 2800 | Z | 2802 | Z | 2804 | Z | 2806 | Z | 2808 | Z | 2810 | Z | 2812 | Z | 2814 | Z | 2816 | Z | 2818 | Z | 2820 | Z | 2822 | Z | 2824 | Z | 2826 | Z | 2828 | Z | 2830 | Z | 2832 | Z | 2834 | Z | 2836 | Z | 2838 | Z | 2840 | Z | 2842 | Z | 2844 | Z | 2846 | Z | 2848 | Z | 2850 | Z | 2852 | Z | 2854 | Z | 2856 | Z | 2858 | Z | 2860 | Z | 2862 | Z | 2864 | Z | 2866 | Z | 2868 | Z | 2870 | Z | 2872 | Z | 2874 | Z | 2876 | Z | 2878 | Z | 2880 | Z | 2882 | Z | 2884 | Z | 2886 | Z | 2888 | Z | 2890 | Z | 2892 | Z | 2894 | Z | 2896 | Z | 2898 | Z | 2900 | Z | 2902 | Z | 2904 | Z | 2906 | Z | 2908 | Z | 2910 | Z | 2912 | Z | 2914 | Z | 2916 | Z | 2918 | Z | 2920 | Z | 2922 | Z | 2924 | Z | 2926 | Z | 2928 | Z | 2930 | Z | 2932 | Z | 2934 | Z | 2936 | Z | 2938 | Z | 2940 | Z | 2942 | Z | 2944 | Z | 2946 | Z | 2948 | Z | 2950 | Z | 2952 | Z | 2954 | Z | 2956 | Z | 2958 | Z | 2960 | Z | 2962 | Z | 2964 | Z | 2966 | Z | 2968 | Z | 2970 | Z | 2972 | Z | 2974 | Z | 2976 | Z | 2978 | Z | 2980 | Z | 2982 | Z | 2984 | Z | 2986 | Z | 2988 | Z | 2990 | Z | 2992 | Z | 2994 | Z | 2996 | Z | 2998 | Z | 2000  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

![img-61.jpeg](img-61.jpeg)

CS 6 872