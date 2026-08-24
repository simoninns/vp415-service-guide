---
title: Module S - Control
description: >-
  The control processor, its RS232 and S-bus interfaces, its memory map and
  its watchdog.
---

# Module S — Control

*See also the [module S page](../../modules/s-control/index.md).*

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

## Operation

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

## Watchdog

IC7210 is a watchdog circuit which provides power on reset and also gives a reset if the program hangs up or if the local standby key is pressed. In this latter case a software reset is performed.

It consists of a retriggerable monostable which when the processor is running is continuously retriggered. At power on or if the program crashes the circuit is no longer triggered and generates a reset.

## The manual sheet

<figure class="sheet sheet--fold" markdown>
[![Module S - control (operation / watchdog) / Module T - supply](../assets/web/cs-7-898-text-p152-preview.webp)](../assets/web/cs-7-898-text-p152-zoom.webp)
<figcaption>
  Module S - control (operation / watchdog) / Module T - supply.
  <span class="cs">CS 7 898</span>
  <span class="src">service manual page 152</span>
</figcaption>
</figure>
