---
title: Connector pinning
description: >-
  Pin assignments for the A/V Euroconnector, the RGB (TTL) DIN input, the
  RS232-C port and the SCSI connector.
---

# Connector pinning

Pin assignments for the four connectors on the rear panel that carry signals
rather than mains: the A/V Euroconnector (10), the RGB (TTL) DIN input (16),
the RS232-C port (6) and the SCSI connector (18). The numbers in brackets are
the manual's rear-panel numbering — see
[controls, indicators and connections](controls-and-connections.md).

## A/V Euroconnector

21-pin SCART.

| Pin | Signal |
| --- | --- |
| 1 | audio out (right), 650 mV rms / 1 k |
| 2 | not connected |
| 3 | audio out (left), 650 mV rms / 1 k |
| 4 | audio earth |
| 5 | blue earth |
| 6 | not connected |
| 7 | blue out, 700 mV / 75 Ω |
| 8 | player status (player in standby: 2 V; player on: 12 V) |
| 9 | green earth |
| 10 | not connected |
| 11 | green out, 700 mV / 75 Ω |
| 12 | not connected |
| 13 | red earth |
| 14 | earth |
| 15 | red out, 700 mV / 75 Ω |
| 16 | fast blanking: 2.5 V into 75 Ω (RGB status) |
| 17 | CVBS earth |
| 18 | RGB status earth |
| 19 | CVBS out, 1 V / 75 Ω — also acts as sync out when using RGB |
| 20 | not connected |
| 21 | socket earth |

## RGB (TTL) IN socket

6-pole female DIN connector, 270°.

| Pin | Signal |
| --- | --- |
| 1 | red signal |
| 2 | green signal |
| 3 | blue signal |
| 4 | composite sync |
| 5 | ground |
| 6 | not connected |

Logic 0: 0–1 V; logic 1: 2.2–4.2 V. Sync instability better than ±100 ppm;
interlaced, with or without equalising pulses, negative-going.

## RS232-C interface

A serial computer interface in accordance with international communication
standards. Full duplex, 8 data bits, 1 stop bit, no parity.

Transmission speed is set to 1200, 2400, 4800 or 9600 baud by the two baud-rate
dip switches — numbers 1 and 2 of switch bank 7 at the rear of the player:

| Baud rate | Switch 1 | Switch 2 |
| --- | --- | --- |
| 1200 | UP | UP |
| 2400 | UP | DOWN |
| 4800 | DOWN | UP |
| 9600 | DOWN | DOWN |

The player is fitted with a 25-pole female D-connector:

| Pin | Signal |
| --- | --- |
| 2 | (TxD) transmitted data, player to computer |
| 3 | (RxD) received data, computer to player |
| 5 | (CTS) clear to send: computer to player, indicating the computer is ready to receive data (≥ +3 V means OK to transmit) |
| 7 | (GND) logic ground |
| 9 | +12 V / 100 mA |
| 10 | −12 V / 10 mA |
| 20 | (DTR) data terminal ready: player to computer, indicating the player is ready to receive data (≥ +3 V means OK for data) |

## SCSI interface

A computer interface in accordance with SCSI standards. The player is fitted
with a 50-pole unshielded connector: two rows of 25 male pins on 100 mil
centres.

Single-ended cable pin assignments:

| Pin | Signal |
| --- | --- |
| 2 | −DB(0) |
| 4 | −DB(1) |
| 6 | −DB(2) |
| 8 | −DB(3) |
| 10 | −DB(4) |
| 12 | −DB(5) |
| 14 | −DB(6) |
| 16 | −DB(7) |
| 18 | −DB(P) |
| 20 | ground |
| 22 | ground |
| 24 | ground |
| 26 | TERMPWR (not connected to the internal power supply) |
| 28 | ground |
| 30 | ground |
| 32 | −ATN |
| 34 | ground |
| 36 | −BSY |
| 38 | −ACK |
| 40 | −RST |
| 42 | −MSG |
| 44 | −SEL |
| 46 | −C/D |
| 48 | −REQ |
| 50 | −I/O |

**Notes.** All odd pins except pin 25 are connected to ground; pin 25 should be
left open, but may be connected to ground. A minus sign indicates active low.
Maximum cable length is 6 m.

The player's SCSI target address is set by dip switch bank 17, and the SCSI
interface itself lives on [module W](../modules/w-cpu-data-grabber/index.md).

<figure class="sheet" markdown>
[![Connector pinning tables for the A/V Euroconnector, RGB TTL DIN socket, RS232-C interface and SCSI interface](assets/web/cs-7-828-text-p006-preview.webp)](assets/web/cs-7-828-text-p006-zoom.webp)
<figcaption>
  Connector pinning.
  <span class="cs">CS 7 828</span>
  <span class="src">service manual page 006</span>
</figcaption>
</figure>
