---
title: F-code programming
description: >-
  Section 5 of the user manual: the RS232-C interface, DTR and CTS handshaking,
  data format, baud rate setting and the player's registers.
---

# F-code programming

Section 5 of the operating instructions, pages 21 to 24. How the serial
interface works, what the wires do, and what the player remembers.

!!! info "The three tables from this section are on the F-code reference"

    Pages 22, 23 and 24 are Table 1 (the command list), Table 2 (handset keys
    routed to the computer) and Table 3 (acknowledgements). Rather than print
    them twice, they are reproduced — checked against these scans — on
    **[F-codes](../reference/f-codes.md)**, which also carries the responses a
    real player gives. The pages themselves are at the foot of this one.

## General introduction

The VP415 player is designed to allow control of all functions from an external
computer. Connection is via the RS232-C serial interface or the SCSI interface
on the rear of the player.

The interface allows **two-way communication**: some commands sent to the
player are followed by corresponding acknowledgements back to the computer.

## RS232-C interface connection

This is a serial computer interface in accordance with international
communication standards. Communication is **full duplex**, with a selectable
baud rate.

The player is fitted with a **25-pole female D-connector**:

| Pin | Signal | |
| --- | --- | --- |
| 2 | `TxD` | Transmitted data, player to computer |
| 3 | `RxD` | Received data, computer to player |
| 5 | `CTS` | Clear to send — computer to player, indicating the computer is ready to receive |
| 7 | `GND` | Logic ground |
| 9 | | +12 V / 100 mA |
| 10 | | −12 V / 10 mA |
| 20 | `DTR` | Data terminal ready — player to computer, indicating the player is ready to receive |

### DTR — data terminal ready, pin 20

Whenever the player is in a condition to receive data from the computer it
signals this by setting `DTR` **high, above +3 V**. When it is busy processing
data and cannot receive, it sets `DTR` **negative, below −3 V**.

!!! warning "Honour DTR or lose data"

    It is important to ensure that the data output of the computer is
    accurately controlled by the `DTR` line, so as to prevent partial loss of
    data.

### CTS — clear to send, pin 5

Many computers have a control line that can tell the player when the computer
is ready to receive. Whenever the player wishes to transmit it first checks
`CTS`: above +3 V it assumes the computer is ready and transmits; below −3 V it
**delays transmission indefinitely** until the correct status is seen.

If the computer cannot control `CTS`, it is recommended that the *transmission
delay on* command `)1` is sent to the player. This results in a transmission
rate of **50 characters per second**, giving the computer more time to handle
the characters. In this case the `CTS` line, pin 5, should be kept active — for
instance by leaving the connection open.

### Data format

**8 data bits and 1 stop bit, parity ignored.** Data sent to the player should
comprise a string of characters plus a carriage return, and the player actions
the command only after receiving the `CR`.

Each byte sent to the player is checked for validity. ASCII codes lower than 32
are rejected, and so is the rest of that string. ASCII codes higher than 127
are accepted: the most-significant bit is always read as zero, so the player
effectively subtracts 128. A computer which transmits only seven data bits per
ASCII code may therefore be used — in that case **at least two stop bits must
be sent**.

### Baud rate setting — RS232-C only

Transmission speed may be set to **1200, 2400, 4800 or 9600 baud** by the two
baud rate dip switches, numbers 1 and 2, at the rear of the player. Section 5
gives the settings only as the pictogram of Fig. 9; the same four settings are
printed as a table in [technical data](technical-data.md#rs232-c-interface) on
page 45, and that is the one to work from:

| Baud | Switch 1 | Switch 2 |
| --- | --- | --- |
| 1200 | up | up |
| 2400 | up | down |
| 4800 | down | up |
| 9600 | down | down |

**Up is off**, as the manual says of the SCSI switches on the same panel — so
1200 is both switches off and 9600 is both on. Fig. 9 draws exactly this, with
a square high for up and low for down.

!!! tip "Let the player tell you which rate it is at"

    When altering these switches, first switch on the player and disc status
    display with the `DISPLAY` button on the handset. **The baud rate setting is
    then shown on the screen** — the bottom-left line of
    [Fig. 7](special-play-functions.md#player-and-disc-status). That is quicker
    than reading a pictogram, and it is proof rather than inference.

## Commands to the player

The F-code commands sent to the player to carry out particular functions are
listed in **Tables 1 and 2**, and functional explanations of them are in
[section 6, F-code commands](f-code-commands.md). **Table 3** lists the
acknowledgements sent from the player to the computer on receipt of certain
commands.

All three are on the [F-code reference](../reference/f-codes.md).

## Player registers

There are **two picture number registers**, each holding a five-digit number
from 1 to 79999. Normally a disc contains up to around 54 000 pictures, so
numbers beyond that are not used. There is also a **time code register** holding
a time code of the form `mm:ss` in the range `00:00` to `59:59`.

| Register | Loaded by | What happens |
| --- | --- | --- |
| **Picture number stop** | `FxxxxxS` | Automatically cleared to zero when the player reaches the stored picture number and enters still mode |
| **Picture number information** | `FxxxxxI` | When the player *passes* the stored number, an acknowledgement is sent to the computer and the register is cleared. **The playing mode does not change** |
| **Time code information** | `TxxyyI` | When the player passes the stored time code, an acknowledgement is sent and the register is cleared. The playing mode does not change |

## The printed pages

<figure class="sheet" markdown>
[![Section 5 divider listing F-code programming, table 1 the F-code command list, table 2 responses to computer on commands from the remote control handset, and table 3 acknowledgements](assets/web/operating-instructions-scan-13-b-preview.webp)](assets/web/operating-instructions-scan-13-b-zoom.webp)
<figcaption>
  Section 5 divider and contents.
  <span class="src">operating instructions page 20</span>
</figcaption>
</figure>

<figure class="sheet" markdown>
[![Page describing the RS232-C interface, its 25-pin connector, DTR and CTS handshaking, the data format, the baud rate dip switches as figure 9, and the player's picture number and time code registers](assets/web/operating-instructions-scan-14-b-preview.webp)](assets/web/operating-instructions-scan-14-b-zoom.webp)
<figcaption>
  The interface, the handshaking, Fig. 9 and the registers.
  <span class="src">operating instructions page 21</span>
</figcaption>
</figure>

<figure class="sheet" markdown>
[![Table 1, the F-code command list: about seventy commands with their decimal code, hexadecimal code, character and function](assets/web/operating-instructions-scan-13-a-preview.webp)](assets/web/operating-instructions-scan-13-a-zoom.webp)
<figcaption>
  Table 1 — the F-code command list. Transcribed on the
  <a href="../../reference/f-codes/">F-code reference</a>.
  <span class="src">operating instructions page 22</span>
</figcaption>
</figure>

<figure class="sheet" markdown>
[![Table 2: the codes returned to the computer for each remote control handset key when RC commands are routed to the computer, and the codes for the numeric keys](assets/web/operating-instructions-scan-14-a-preview.webp)](assets/web/operating-instructions-scan-14-a-zoom.webp)
<figcaption>
  Table 2 — handset keys routed to the computer.
  <span class="src">operating instructions page 23</span>
</figcaption>
</figure>

<figure class="sheet" markdown>
[![Table 3: the acknowledgements the player sends back to the computer, from the O returned on eject to the negative acknowledgement A N](assets/web/operating-instructions-scan-16-b-preview.webp)](assets/web/operating-instructions-scan-16-b-zoom.webp)
<figcaption>
  Table 3 — acknowledgements back to the external computer.
  <span class="src">operating instructions page 24</span>
</figcaption>
</figure>

## Related

- [F-codes](../reference/f-codes.md) — Tables 1, 2 and 3, plus real-player
  responses
- [F-code commands](f-code-commands.md) — section 6, a description of every
  command
- [SCSI operation](scsi-operation.md) — the other interface
- [Technical data](technical-data.md) — the RS232-C interface specification
