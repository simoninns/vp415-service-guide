33

### System clock

The 8MHz crystal clock is built around IC 63. This is divided by 2 to give a 4MHz symmetrical clock for the Z80A, DMA and SCSI and a 4MHz two phase clock for the UPI-41.

### UPI-41

The UPI-41 is a slave processor based on the 8041 providing a half duplex UART for communications with the player part.

LV-DOS (LV-ROM, Data grabber, CPU) communicates with the player via the UPI-41 RS232 interface using F-Codes. The connector for this local UART interface is W4. The UPI-41 operates via 4 internal registers, input, output, control and status. The registers are addressed by A0 with -IORD or -IORW.

Table W12

|  AO | -IORD | -IORW  |
| --- | --- | --- |
|  0 | output | input  |
|  1 | status | control  |

### SCSI interface (Small Computer System Interface)

All communications with the SCSI bus are under the control of the SCSI controller (NCR-5385/6). The controller has 16 on-board registers and behaves as a dedicated microprocessor. The controller can operate in target or initiator mode but for the Domesday project only target mode is used.

The SCSI registers

Table W13

|  port(h) | R/W | Function  |
| --- | --- | --- |
|  00 | R/W | Data  |
|  01 | R/W | Command  |
|  02 | R/W | Control  |
|  03 | R/W | Destination ID  |
|  04 | R/W | Auxiliary status  |
|  05 | R | ID. register  |
|  06 | R | Interrupt register  |
|  07 | R | Source ID  |
|  09 | R | Diagnostic status  |
|  0C | R/W | Transfer count (MSB)  |
|  0D | R/W | ... (2nd byte)  |
|  0E | R/W | ... (LSB)  |
|  0F | R/W | Reserved  |

### There are a number of connections with the CPU circuit

Table W14

|  Signal | Pin | Function  |
| --- | --- | --- |
|   | 16 | 4MHz clock  |
|  RST | 4 | RST=1 resets the SCSI controller  |
|  D0-D7 | 1-3,43-47 | Data bus to Z80A  |
|  INT0 | 19 | Interrupt to Z80A as a result of various SCSI conditions  |
|  -IOWR | 30 | Active low write signal to place a byte in the SCSI  |
|  -IORD | 31 | Active low read pulse to read a byte from the SCSI  |
|  A0-A3 | 22-24,26 | Addresses for the 16 registers  |
|  RDY | 29 | Used when a DMA controller is fitted  |
|  -SEL0 | 21 | Chip select  |
|  -SEL30 | 27 | Data register enable used by DMA SEL30=0 resets RDY  |

### SCSI bus interface

Since the SCSI controller can operate in initiator as well as target mode we must consider how this selection is made.

Two control lines are used for this :-

TGS (Target group select)

IGS (Initiator group select)

The effect of these signals can be seen from the following table.

Table W15

|  TGS | IGS | MSG | C/D | I/O | ATN | ACK | REQ  |
| --- | --- | --- | --- | --- | --- | --- | --- |
|  0 | 0 | IN | IN | IN | IN | IN | IN  |
|  0 | 1 | IN | IN | IN | OUT | OUT | OUT  |
|  1 | 0 | OUT | OUT | OUT | IN | IN | OUT  |
|  1 | 1 | This is a forbidden condition  |   |   |   |   |   |

All inputs/outputs of the SCSI bus are terminated with 220 Ohm to +5V and 330 Ohm to ground.

### SCSI bus pin assignments

Table W16

|  Signal | Pin | Signal | Pin  |
| --- | --- | --- | --- |
|  -DB0 | 2 | Ground | 28  |
|  -DB1 | 4 | Ground | 30  |
|  -DB2 | 6 | -ATN | 32  |
|  -DB3 | 8 | Ground | 34  |
|  -DB4 | 10 | -BSY | 36  |
|  -DB5 | 12 | -ACK | 38  |
|  -DB6 | 14 | -RST | 40  |
|  -DB7 | 16 | -MSG | 42  |
|  -DBP | 18 | -SEL | 44  |
|  Ground | 20 | -C/D | 46  |
|  Ground | 22 | -REQ | 48  |
|  Ground | 24 | -I/O | 50  |
|  +5V | 26 |  |   |

In addition all odd pins numbered below 25 are connected to ground.

### Indication of SCSI bus phase

#### .Table W17

MSG, C/D and I/O determine the bus phase

MSG Message byte waiting

C/D Control / Data byte

I/O Input or output

In target mode these signals are all outputs (TGS=1). In this condition IC 71 is enabled for output and IC 70 is disabled for input.

### SCSI handshake lines in target mode

#### Table W18

REQ informs the host computer that communications are required. ACK is the response from the host when it sees REQ. ATN informs the host that a message byte is required. BSY indicates that the device is busy.

### SCSI data bus buffers

The data bus of the SCSI controller is buffered between the controller and the in/out connector. Output buffer - IC's 75,76. Input buffer IC 77. The buffers are under the control of SBEN (pin20,SCSI). SBEN=0 - output, SBEN=1 - input.

CS 7 905