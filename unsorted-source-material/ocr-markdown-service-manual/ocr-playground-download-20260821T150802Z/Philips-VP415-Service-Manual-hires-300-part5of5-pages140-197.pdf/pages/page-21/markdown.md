34

# Installation of target ID

There are eight possible ID's that can be selected for the target:-

The ID is selected by means of dip switch S1 Nos 5,6 and 7.

Table W19

|  Dip switch setting |   |   | ID No.  |
| --- | --- | --- | --- |
|  5 | 6 | 7 |   |
|  off | off | off | 0 Default  |
|  off | off | on | 1  |
|  off | on | off | 2  |
|  off | on | on | 3  |
|  on | off | off | 4  |
|  on | off | on | 5  |
|  on | on | off | 6  |
|  on | on | on | 7  |

# CPU memory map

The CPU is organised to handle a maximum of 32kBytes of ROM plus 32kBytes of RAM.

Table W20

|  IC No. | Address (h) | Chip select  |
| --- | --- | --- |
|  47 16k EPROM | 0000 - 3FFF | -PRO x -PR1  |
|  48 16k EPROM | 4000 - 7FFF | -PR2 x -PR3  |
|  22 8k RAM | 8000 - 9FFF | -PR4 (shared)  |
|  49 8k RAM | A000 - BFFF | -PR5  |
|  50 8k RAM | C000 - DFFF | -PR6  |
|  51 8k RAM | E000 - FFFF | -PR7  |

# CPU port map

Table W21

|  Port No. | IC No. | Chip sel. | I/O | Function  |
| --- | --- | --- | --- | --- |
|  00 | 39 | -SEL0 | I/O | SCSI data  |
|  01 | .. | .. | I/O | SCSI command  |
|  02 | .. | .. | I/O | SCSI control  |
|  03 | .. | .. | I/O | SCSI destination  |
|  04 | .. | .. | I/O | SCSI aux.  |
|  05 | .. | .. | In | SCSI ID.  |
|  06 | .. | .. | In | SCSI interrupt  |
|  07 | .. | .. | In | Source ID.  |
|  09 | .. | .. | In | Diag. status  |
|  0C | .. | .. | I/O | Count MSB  |
|  0D | .. | .. | I/O | Count 2nd byte  |
|  0E | .. | .. | I/O | Count LSB  |
|  0F | .. | .. | I/O | Reserved - test  |
|  10 | 43 | -SEL1 | I/O | DMA data/control  |
|  20 | 52 | -SEL2 | I/O | UPI-41 data  |
|  21 | 52 | .. | In | UPI-41 status  |
|  21 | 52 | .. | Out | UPI-41 control  |
|  34 | 18 | -SEL34 | In | Data grab status  |
|  34 | 54 | -SEL34 | Out | Data grab control and interrupt reset  |
|  37 | 53 | -SEL37 | Out | Read dip sw. and interrupt f/f's.  |
|  40 | 19,20 | -SEL4 | In | Header Mins.  |
|  41 | .. .. | .. | In | Header Secs.  |
|  42 | .. .. | .. | In | Header Blocks.  |
|  43 | .. .. | .. | In | Header Mode.  |

# Dip switches on the CPU panel

Dip switch S1.

Table W22

|  Switch | Purpose |   |
| --- | --- | --- |
|  1 | Baudrate selection | Not used  |
|  2 | Monitor test | Not used  |
|  3-4 | Not used |   |
|  5-7 | Target ID installation. |   |

# MODULE X - LV-ROM DECODER

# Computer data on disc

LV-ROM data storage has a similar format to that used on the Compact Disc in that the basic word size is sixteen bits with a sample rate of 44,100 per second alternating left and right to give 176.4 kBytes/Sec.

The data is organised in blocks. Each block consists of 98 frames. Each frame contains 12 pairs of byte values (6 x DLCF, 6 x DRCF) ie. 24 bytes.

To allow synchronisation and identification each block commences with a sync pattern and header.

We can summarise a block as :

Table X1

12 bytes sync

4 bytes header

2048 bytes data

8 bytes unused

280 bytes CRC (error detection and correction)

Total 2352 bytes

A block is read from the disc in 1/75th sec.

As the disc revolves at TV frame rate (25Hz) we may deduce that three blocks will be read during one revolution of the disc. Thus the position of any block on the disc can be obtained by dividing the block number by three to obtain the frame or picture number. The player accesses the disc in terms of frame number.

The encoding format on the disc uses a cross interleaved Reed Solomon code to give protection against reading errors caused by dust or scratches on the disc and each byte is represented by a 14 bit word. This process of modulation is termed EFM - Eight to Fourteen bit Modulation. An EFM word obeys the rule that there must be at least two and not more than ten '0's' between adjacent '1's'. Since this rule might be broken at the junction of two words three 'merging bits' are inserted between each pair of EFM words to ensure that the 2 - 10 rule is adhered to.

A 'Control and Display' word (and a synchronising pattern precede the data bytes in each frame. Two groups of parity bits each of 4 bytes complete the frame.

Over a block of 98 frames the C and D words are accumulated to provide a block label in terms of time.(Mins, Secs, 1/75 Secs)

Each frame therefore consists of

|  Sync pattern | 24 bits  |
| --- | --- |
|  Control and display | 14 bits  |
|  Data (24 x 14) | 336 bits  |
|  Parity (8 x 14) | 112 bits  |
|  Merging (34 x 3) | 102 bits  |
|  Total bits | 588 bits  |

In addition to the protection given by the CIRC (Cross interleaved Reed Solomon) coding further protection is provided by the 280 CRC bytes of each block.

The bit rate as read from the disc is 4.3218 Mbits/Sec. giving a decoded data rate of 153.6 kbytes/Sec.

# Data scrambling

There may be sections of data where a number of bytes have a similar value. This would have the effect of causing a DC offset (non-zero DSV) which could upset servo operation. To avoid this the data is modified by having a scrambling pattern superimposed. This scrambling must be unpicked in the player.

CS 7 906