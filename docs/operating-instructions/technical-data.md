---
title: Technical data
description: >-
  Section 8 of the user manual: the disc, the player, video, audio, genlock,
  the video mixer, LV-ROM, and the pinning of every external connector.
---

# Technical data

Section 8 of the operating instructions, pages 44 and 45. The specification of
the disc and the player, and — the part worth bookmarking — **the pinning of
every socket on the back panel**.

## LaserVision disc

| | |
| --- | --- |
| Disc diameter | 30 cm (12″) or 20 cm (8″) |
| Disc thickness | 2.7 mm (0.1″) |
| Disc speed | CAV: 1500 r.p.m. · CLV: 1500 – 570 r.p.m. |
| Maximum capacity, 30 cm disc | CAV: **54 000 pictures per side**. LV-ROM (CAV): **324 Mbyte** max. user data per side, in place of audio |
| Maximum playing time, 30 cm disc | CAV: 36 minutes per side · CLV: 1 hour per side |
| Average track pitch | 1.6 – 1.8 μm |

## Professional LaserVision player VP415

### General

| | |
| --- | --- |
| Disc-tray | Front loading, motor-powered |
| Start-up time | < 13 s |
| Unload time | < 15 s, from the eject command to the disc out of the player |
| Laser | **SSL — solid state, AlGaAs semiconductor** |
| Wavelength | 780 nm |
| Aperture | 0.5 |
| Output of laser | 3 – 5 mW |
| Random access time | CAV: max. 3 s, ≤ 1 s average · CLV: max. 15 s, ≤ 5 s average |
| Instant jump | Up to 50 frames forward or reverse, within the vertical interval |
| On-board programming | Up to 16 picture number / chapter number segments |
| Program retention with no mains supply | **> 1 week** |
| Mains voltage | 220 – 240 V ± 10% a.c. |
| Mains frequency | 50 to 60 Hz |
| Power consumption | 60 W approximately |
| Electrical safety | To IEC 65 |
| Operating conditions | 10 to 35 °C, 20 – 80% relative humidity |
| Storage conditions | −40 to 70 °C, 10 – 95% relative humidity |
| Dimensions | 420 × 160 × 400 mm · **740 mm deep with the disc-tray open** |
| Weight | 15 kg approximately |
| TV system | 625/50 PAL |

### Video

| | |
| --- | --- |
| CVBS input (BNC) | 1 V into 75 Ω, loop-through |
| CVBS output (BNC) | 1 V into 75 Ω |
| CVBS output (Euroconnector pin 19) | 1 V into 75 Ω |
| RGB output (Euroconnector) | R pin 15, G pin 11, B pin 7 — **0.7 V into 75 Ω** each |
| Video bandwidth | **RGB: 5 MHz (−3 dB)** · CVBS: 3 MHz (−3 dB), encoded |
| Signal-to-noise ratio | 40 dB typical unweighted, 50 dB typical weighted — disc dependent |
| Timebase instability | **Less than 10 ns** in normal play |

### Audio

| | |
| --- | --- |
| Audio input (cinch) | 3 Vpp, load 47 kΩ |
| Audio output (cinch) | 650 mV r.m.s. into 1 kΩ at maximum deviation |
| Audio output (Euroconnector pins 1 and 3) | 650 mV r.m.s. into 1 kΩ |
| Audio bandwidth | 40 – 20 000 Hz |
| Signal-to-noise ratio | ≥ 50 dB typical weighted, disc dependent |
| Channel separation | Better than 55 dB |

### Genlock

| | |
| --- | --- |
| Sync input (BNC) | 0.3 – 2.0 Vpp, 75 Ω, loop-through; waveform to CCIR standards |
| Sync input (DIN pin 4) | Line 15 625 Hz ± 100 ppm; field 50 Hz locked to line, interlaced, with or without equalising pulses, negative-going. Logic 0: 0 – 1 V, logic 1: 2.2 – 4.2 V |
| Sync output (BNC) | 2.0 Vpp, 75 Ω, negative-going |
| Genlock lock-in time | **5 s** |

### Video mixer

RGB mixing and keying modes, selected with [`VPy`](f-code-commands.md#video-overlay):

| Mode | Player | Computer |
| --- | --- | --- |
| Player RGB only | 100% | — |
| Computer RGB only | — | 100% |
| Key mode | 100% | 100% |
| Mixed mode | 62% | 38% |
| Enhanced mode | 57% / 100% | — |

### LV-ROM

| | |
| --- | --- |
| User data capacity | Max. **324 Mbyte per disc side** |
| User data per frame | 6 kbyte |
| User data transfer rate from disc | 150 kbyte/s, depending on the computer |
| Data integrity | Error rate **≤ 10⁻¹⁶** |
| Internal CPU | 4 × 6 kbyte cache memory for user data |
| System | Compatible with floppy disc and hard disc systems |

## Connector pinning

### A/V Euroconnector

| Pin | Signal |
| --- | --- |
| 1 | Audio out, right — 650 mV r.m.s. / 1 kΩ |
| 2 | Not connected |
| 3 | Audio out, left — 650 mV r.m.s. / 1 kΩ |
| 4 | Audio earth |
| 5 | Blue earth |
| 6 | Not connected |
| 7 | **Blue out** — 700 mV / 75 Ω |
| 8 | **Player status** — 2 V in standby, 12 V when on |
| 9 | Green earth |
| 10 | Not connected |
| 11 | **Green out** — 700 mV / 75 Ω |
| 12 | Not connected |
| 13 | Red earth |
| 14 | Earth |
| 15 | **Red out** — 700 mV / 75 Ω |
| 16 | Fast blanking — 2.5 V into 75 Ω, RGB status |
| 17 | CVBS earth |
| 18 | RGB status earth |
| 19 | **CVBS out** — 1 V / 75 Ω. Also acts as sync out when using RGB |
| 20 | Not connected |
| 21 | Socket earth |

Pin 8 is also the pin the [`#xy` RC-5 command](f-code-commands.md#sound-and-rc-5)
is transmitted on.

### RGB (TTL) IN socket

6-pole female DIN connector, 270°.

| Pin | Signal |
| --- | --- |
| 1 | Red signal |
| 2 | Green signal |
| 3 | Blue signal |
| 4 | **Composite sync** |
| 5 | Ground |
| 6 | Not connected |

Logic 0 is 0 – 1 V and logic 1 is 2.2 – 4.2 V. Sync instability better than
± 100 ppm; interlaced, with or without equalising pulses, negative-going.

### RS232-C interface

A serial computer interface in accordance with international communication
standards. **Full duplex, 8 data bits, 1 stop bit, no parity.**

Transmission speed is set by the two baud rate dip switches, numbers 1 and 2,
at the rear of the player:

| Baud rate | Switch 1 | Switch 2 |
| --- | --- | --- |
| 1200 | up | up |
| 2400 | up | down |
| 4800 | down | up |
| 9600 | down | down |

The player is fitted with a **25-pole female D-connector**:

| Pin | Signal |
| --- | --- |
| 2 | `TxD` — transmitted data, player to computer |
| 3 | `RxD` — received data, computer to player |
| 5 | `CTS` — clear to send, computer to player. **≥ +3 V means OK to transmit** |
| 7 | `GND` — logic ground |
| 9 | +12 V / 100 mA |
| 10 | −12 V / 10 mA |
| 20 | `DTR` — data terminal ready, player to computer. **≥ +3 V means OK for data** |

### SCSI interface

A computer interface in accordance with SCSI standards. The player is fitted
with a **50-pole unshielded connector**, two rows of 25 male pins on 100 mil
centres. Single-ended cable pin assignments:

| Pin | Signal | Pin | Signal |
| --- | --- | --- | --- |
| 2 | `-DB(0)` | 30 | Ground |
| 4 | `-DB(1)` | 32 | `-ATN` |
| 6 | `-DB(2)` | 34 | Ground |
| 8 | `-DB(3)` | 36 | `-BSY` |
| 10 | `-DB(4)` | 38 | `-ACK` |
| 12 | `-DB(5)` | 40 | `-RST` |
| 14 | `-DB(6)` | 42 | `-MSG` |
| 16 | `-DB(7)` | 44 | `-SEL` |
| 18 | `-DB(P)` | 46 | `-C/D` |
| 20 | Ground | 48 | `-REQ` |
| 22 | Ground | 50 | `-I/O` |
| 24 | Ground | | |
| 26 | `TERMPWR` — **not connected to the internal power supply** | | |
| 28 | Ground | | |

!!! note "Reading that connector"

    - **All odd pins except pin 25 are connected to ground.** Pin 25 should be
      left open, but may be connected to ground.
    - A minus sign indicates **active low**.
    - **Maximum cable length is 6 m.**

The address dip switches are at the rear of the player. **A switch in the up
position is off.** Switches 1 to 4 and switch 8 should be off; switches 5 to 7
set the address:

| Address | Switch 5 | Switch 6 | Switch 7 |
| --- | --- | --- | --- |
| 0 | off | off | off |
| 1 | off | off | on |
| 2 | off | on | off |
| 3 | off | on | on |
| 4 | on | off | off |
| 5 | on | off | on |
| 6 | on | on | off |
| 7 | on | on | on |

**Factory setting: address 0.**

## The printed pages

<figure class="sheet" markdown>
[![Page of technical data covering the LaserVision disc, the player's general specification, video, audio, genlock, the video mixer, LV-ROM and the A/V Euroconnector pinning](assets/web/operating-instructions-scan-27-b-preview.webp)](assets/web/operating-instructions-scan-27-b-zoom.webp)
<figcaption>
  Technical data — disc, player, video, audio, genlock, mixer, LV-ROM and the
  Euroconnector.
  <span class="src">operating instructions page 44</span>
</figcaption>
</figure>

<figure class="sheet" markdown>
[![Page giving the RGB TTL input socket pinning, the RS232-C interface with its baud rate switch table and 25-pin connector, and the SCSI interface with its 50-pin assignments and address switches](assets/web/operating-instructions-scan-26-b-preview.webp)](assets/web/operating-instructions-scan-26-b-zoom.webp)
<figcaption>
  The RGB input, RS232-C and SCSI interfaces, and the address switches.
  <span class="src">operating instructions page 45</span>
</figcaption>
</figure>

## Related

- [Connector pinning](../overview/connector-pinning.md) — the service manual's
  own connector tables, internal as well as external
- [Technical data](../overview/technical-data.md) — the service manual's
  specification, which goes further in places
- [Controls and connections](controls-and-connections.md) — what each socket is
  for
- [SCSI operation](scsi-operation.md) · [F-code programming](f-code-programming.md)
  — the two interfaces in use
