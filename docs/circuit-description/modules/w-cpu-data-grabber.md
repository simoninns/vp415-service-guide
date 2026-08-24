---
title: Module W - Data grabber and CPU
description: >-
  How computer data is taken off the disc, the descrambler, the RAM shared
  with the CPU, the port map and the SCSI interface.
---

# Module W — Data grabber and CPU

*See also the [module W page](../../modules/w-cpu-data-grabber/index.md).*

## Function description

We may summarise the functions of the data grabber as :-

a) Collect serial data from the LV-ROM decoder.
b) Convert the two streams of serial data to parallel form.
c) Establish lock with the block structure.
d) Read the header.
e) When the desired header is seen, store that block and the two following blocks in RAM.
f) Signal to the CPU that the header and the following three blocks are ready.

During this sequence the data is unscrambled and if error flags are present the CPU enters a correction routine to recover corrupt data.

## Circuit description

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

## Bus linking

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

## Input circuit

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

## Sync detector

This circuit detects the sync pattern at the start of the data block. The pattern consists of a 12 byte sequence.

The detector comprises EPROM, IC 1 and D-Type flip flops IC's 6,7 and operates as a labyrinth in which, provided that the correct 96 bit pattern (8 x 12) is present an output pulse SNC will be developed. This pulse initiates the byte counter.

## Sync signal SYN

This signal is used to produce a byte count in sync with the incoming data.

When SYN=1 the count is set to 000h. The count commences when SYN=0. From this point on the byte counter generates addresses for the descrambler EPROM and the RAM. Owing to the fact that SYN is produced a little early it is delayed in IC 8 to correspond with the leading edge of ST1. Error window pulse ERWD.

If ERCF or ELCF are present indicating errors uncorrected in ERCO then by ORing these signals ERWD is produced. ERWD signifies that the error correction routine must be entered by the CPU.

ERWD is stored in flip flop IC 30. IC 30 is reset by HDR when a new header is recieved.

## Descrambler

The data in each block has a superimposed scrambling pattern which must be descrambled. This is achieved by EXORing byte by byte with a descrambling pattern from EPROM IC 24. Addresses for the EPROM are given by the byte counter (C bus). The byte counter forms part of a synchronous loop which ensures that the correct descrambler byte is output by the EPROM.

## In lock indication LCK

LCK indicates that the system is in lock with the block structure. LCK is derived from SYN and CNT, when the byte counter is counting 2351 bytes between sync patterns (IC's 13,14).

## Header pulse HDR

HDR=1 indicates that the 4 header bytes are being loaded in the header register IC 19,20 and in RAM IC 22. ERD (Enable Read Data) =1 inhibits the refreshing of the header when the header is found.


- DATA GRABBER DATA PROCESSING MODULE
- Wa

## Header register

Header bytes are loaded into the header register IC's 19,20 when HWE=0 (Header write enable). Header reading by the CPU is accomplished with HRE=0, IORD=0 and SEL4=0. The CPU can then determine if the header is from the desired data block.

## Byte counter

The byte counter uses 4 counters, IC's 31,32,36,38. It generates addresses for the descrambler EPROM and the RAM. The byte counter must be synchronised with the blocks. At the end of each sync pattern the counter is reset by SYN and so is rapidly pulled into lock. RDY indicates to the CPU that 3 blocks (3 x 2352) blocks are in the RAM.

## RDY (ready signal)

RDY informs the CPU that 3 blocks are in the RAM. RDY is generated when TCNT(Terminate count ) occurs ( 3 x 2352-1) from IC 35. The RDY circuit is built around IC's14,13 it is reset by RES.

## Read/write of header register and RAM

The read signal comes from the CPU. The write signal is DST2=0 for the ram, HDR for the header register.

## Status register

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

## Processor control lines to data grabber

Table W5

| -MEMRD | Read RAM |
| --- | --- |
| -MEMWR | Write to RAM |
| -IORD | Read I/O ports |
| -ENA | Enable status register |
| -PRO4 | Chip select RAM 8000h - 9FFFh |
| -SEL4 | Chip select I/O ports 40h - 4Fh |

## I/O ports

Table W6

| -34h | Status register input |
| --- | --- |
| 34h | Control register output |
| 40h | Header register (Mins) |
| 41h | Header register (Secs) |
| 42h | Header register (Block) |
| 43h | Header register (Mode) |

## RAM (8k shared with CPU)

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

## Control register

Table W8

| Bit | Function |
| --- | --- |
| 1 | INTR=0 Reset interupt flip flops |
| 0 - 4 | Not used |
| 5 | RES=1 Reset LCK and RDY |
| 6 | ERD=1 Read header of first data block |
| 7 | ENW=1 CPU can write to RAM |

## Sequence to get data from the disc

Table W9

| 1 | Make RES=1 to reset |
| --- | --- |
| 2 | Wait for lock (LCK) |
| 3 | Wait for header |
| 4 | Make ERD=1 to read header when HDR arrives |
| 5 | Wait for ready signal (RDY) |
| 6 | Make ENW=1 |


## CPU

The CPU section operates as the intelligent communications interface between the player and the host computer. It is built around a Z80A microprocessor and has 32k/bytes of ROM and 32k/bytes of RAM of which one 8k block is shared with the data grabber.

- Communication with the host computer is via a SCSI interface (Small Computer System Interface).
- Communication with the player is via a UART.
- Communications with the data grabber have been described.

An optional DMA controller for faster data transfer is catered for but this is not used in the VP415.

## Inputs to CPU

Commands in F-Code from host computer via SCSI.
Disc data from LV-ROM decoder via data grabber.
Acknowledgements from player via UART.

## Outputs of CPU

Disc dump data to host computer via SCSI.
F-Code commands to player via UART.

All three busses of the Z80A are buffered.
Address bus in IC's 44,45.
Data bus in IC 41.
Control bus in IC 40.

The RAM is arranged as 8kbyte blocks which are addressed by A0-A12. Selection of the desired block is by chip select lines -PR4 - -PR7 decoded from A13 - A15 in the 3 to 8 decoder IC56. The 3 to 8 decoder is enabled by -MREQ and gives active low outputs.

Chip enable of the ROM is by means of -PRO0 AND -PRO1 (IC 67).

## In/out port arrangement

The I/O ports are arranged in 8 blocks. Each block or device is allocated a chip select signal (-SEL0 - -SEL7) which is derived from 3 to 8 line decoder IC 57 using address lines A4 to A6. The decoder is enabled when the CPU is carrying out a machine port access (IOREQ=0) and A7=0.

The block identified by SEL3 is further divided into single bit I/O ports by decoding A0 - A3 in 3 to 8 line decoder IC 58 to give -SEL30 - -SEL37. This decoder is enabled by -SEL3.

## Read/write of I/O ports

When the Z80A accesses a machine port (I/O port) it does this by use of IOREQ with RD or WR. This separates I/O port access from memory access which uses MEMREQ and RD or WR.

## Single bit I/O ports

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

## Interrupt handling

The requirement is for two interrupt systems, one from the SCSI controller (INT0) and one from the DMA controller (-INT1). These two interrupts are combined in IC 67 and stored in J-K flip flop IC 59 to give an interrupt to the Z80A (-INT). IC 59 is reset when the interrupt has been serviced by -INTR from the output port IC 53.


## System clock

The 8MHz crystal clock is built around IC 63. This is divided by 2 to give a 4MHz symmetrical clock for the Z80A, DMA and SCSI and a 4MHz two phase clock for the UPI-41.

## UPI-41

The UPI-41 is a slave processor based on the 8041 providing a half duplex UART for communications with the player part.

LV-DOS (LV-ROM, Data grabber, CPU) communicates with the player via the UPI-41 RS232 interface using F-Codes. The connector for this local UART interface is W4. The UPI-41 operates via 4 internal registers, input, output, control and status. The registers are addressed by A0 with -IORD or -IORW.

Table W12

| AO | -IORD | -IORW |
| --- | --- | --- |
| 0 | output | input |
| 1 | status | control |

## SCSI interface (Small Computer System Interface)

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

## There are a number of connections with the CPU circuit

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

## SCSI bus interface

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

## SCSI bus pin assignments

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

## Indication of SCSI bus phase

## .Table W17

- MSG, C/D and I/O determine the bus phase
- MSG Message byte waiting
- C/D Control / Data byte
- I/O Input or output

In target mode these signals are all outputs (TGS=1). In this condition IC 71 is enabled for output and IC 70 is disabled for input.

## SCSI handshake lines in target mode

## Table W18

REQ informs the host computer that communications are required. ACK is the response from the host when it sees REQ. ATN informs the host that a message byte is required. BSY indicates that the device is busy.

## SCSI data bus buffers

The data bus of the SCSI controller is buffered between the controller and the in/out connector. Output buffer - IC's 75,76. Input buffer IC 77. The buffers are under the control of SBEN (pin20,SCSI). SBEN=0 - output, SBEN=1 - input.


## Installation of target ID

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

## CPU memory map

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

## CPU port map

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

## Dip switches on the CPU panel

- Dip switch S1.
- Table W22

| Switch | Purpose | |
| --- | --- | --- |
| 1 | Baudrate selection | Not used |
| 2 | Monitor test | Not used |
| 3-4 | Not used | |
| 5-7 | Target ID installation. | |

## The manual sheets

<figure class="sheet" markdown>
[![Module W - data grabber and CPU](../assets/web/cs-7-902-text-p156-preview.webp)](../assets/web/cs-7-902-text-p156-zoom.webp)
<figcaption>
  Module W - data grabber and CPU.
  <span class="cs">CS 7 902</span>
  <span class="src">service manual page 156</span>
</figcaption>
</figure>

<figure class="sheet" markdown>
[![Module W - header register / byte counter / RDY](../assets/web/cs-7-903-text-p157-preview.webp)](../assets/web/cs-7-903-text-p157-zoom.webp)
<figcaption>
  Module W - header register / byte counter / RDY.
  <span class="cs">CS 7 903</span>
  <span class="src">service manual page 157</span>
</figcaption>
</figure>

<figure class="sheet" markdown>
[![Module W - CPU inputs and outputs](../assets/web/cs-7-904-text-p158-preview.webp)](../assets/web/cs-7-904-text-p158-zoom.webp)
<figcaption>
  Module W - CPU inputs and outputs.
  <span class="cs">CS 7 904</span>
  <span class="src">service manual page 158</span>
</figcaption>
</figure>

<figure class="sheet" markdown>
[![Module W - system clock / UPI-41 / SCSI interface](../assets/web/cs-7-905-text-p159-preview.webp)](../assets/web/cs-7-905-text-p159-zoom.webp)
<figcaption>
  Module W - system clock / UPI-41 / SCSI interface.
  <span class="cs">CS 7 905</span>
  <span class="src">service manual page 159</span>
</figcaption>
</figure>

<figure class="sheet" markdown>
[![Module W - target ID, CPU memory map and port map / Module X - LV-ROM decoder](../assets/web/cs-7-906-text-p160-preview.webp)](../assets/web/cs-7-906-text-p160-zoom.webp)
<figcaption>
  Module W - target ID, CPU memory map and port map / Module X - LV-ROM decoder.
  <span class="cs">CS 7 906</span>
  <span class="src">service manual page 160</span>
</figcaption>
</figure>
