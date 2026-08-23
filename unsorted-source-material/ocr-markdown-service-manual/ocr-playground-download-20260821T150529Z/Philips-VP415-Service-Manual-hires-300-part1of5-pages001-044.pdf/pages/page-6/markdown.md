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