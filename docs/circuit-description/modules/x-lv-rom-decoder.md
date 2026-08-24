---
title: Module X - LV-ROM decoder
description: >-
  Computer data on the disc, the block and frame formats, data scrambling,
  and the decoder circuit.
---

# Module X — LV-ROM decoder

*See also the [module X page](../../modules/x-lv-rom-decoder/index.md).*

## Computer data on disc

LV-ROM data storage has a similar format to that used on the Compact Disc in that the basic word size is sixteen bits with a sample rate of 44,100 per second alternating left and right to give 176.4 kBytes/Sec.

The data is organised in blocks. Each block consists of 98 frames. Each frame contains 12 pairs of byte values (6 x DLCF, 6 x DRCF) ie. 24 bytes.

To allow synchronisation and identification each block commences with a sync pattern and header.

We can summarise a block as :

- Table X1
- 12 bytes sync
- 4 bytes header
- 2048 bytes data
- 8 bytes unused

280 bytes CRC (error detection and correction)

Total 2352 bytes

A block is read from the disc in 1/75th sec.

As the disc revolves at TV frame rate (25Hz) we may deduce that three blocks will be read during one revolution of the disc. Thus the position of any block on the disc can be obtained by dividing the block number by three to obtain the frame or picture number. The player accesses the disc in terms of frame number.

The encoding format on the disc uses a cross interleaved Reed Solomon code to give protection against reading errors caused by dust or scratches on the disc and each byte is represented by a 14 bit word. This process of modulation is termed EFM - Eight to Fourteen bit Modulation. An EFM word obeys the rule that there must be at least two and not more than ten '0's' between adjacent '1's'. Since this rule might be broken at the junction of two words three 'merging bits' are inserted between each pair of EFM words to ensure that the 2 - 10 rule is adhered to.

A 'Control and Display' word (and a synchronising pattern precede the data bytes in each frame. Two groups of parity bits each of 4 bytes complete the frame.

Over a block of 98 frames the C and D words are accumulated to provide a block label in terms of time.(Mins, Secs, 1/75 Secs)

Each frame therefore consists of

| Sync pattern | 24 bits |
| --- | --- |
| Control and display | 14 bits |
| Data (24 x 14) | 336 bits |
| Parity (8 x 14) | 112 bits |
| Merging (34 x 3) | 102 bits |
| Total bits | 588 bits |

In addition to the protection given by the CIRC (Cross interleaved Reed Solomon) coding further protection is provided by the 280 CRC bytes of each block.

The bit rate as read from the disc is 4.3218 Mbits/Sec. giving a decoded data rate of 153.6 kbytes/Sec.

## Data scrambling

There may be sections of data where a number of bytes have a similar value. This would have the effect of causing a DC offset (non-zero DSV) which could upset servo operation. To avoid this the data is modified by having a scrambling pattern superimposed. This scrambling must be unpicked in the player.


## LV-ROM decoder

The LV-ROM decoder accepts the signal from module Z (HFOUT2). This signal is of sinusoidal form and carries digital data for the host computer.

The data rate is 4.3218 mbits/sec but owing to the protection overhead carried the useable data rate is 153.6 kbytes/sec.

The family of IC's used in the LV-ROM decoder is common to the Compact Disc system and so is organised to output data in 16 bit words on two channels.

Data is output in serial form as - left (DLCF) and right (DRCF) with appropriate timing signals - Bit clock (CLCF), Byte clock (STR2) and word clock (STR1). This latter references 16 bit values which are the basic units in Compact Disc.

In addition LV-ROM outputs error flags (ELCF, ERCF) to indicate if uncorrected errors remain in the data.

LV-ROM DECODER MODULE

## Circuit description

The incoming signal from the deck is amplified (Ts6701, 6702, 6703, 6706) to give the required input level (1vpp.) then applied to the input of DEMOD (DEMODulator) IC6501. The signal is also applied to the HF level detector (Ts6530, 6531, IC6508).

When the signal is of adequate amplitude HFL, from 6508.14 enables DEMOD. This occurs when the signal is greater than 0.65Vpp.

The functions of DEMOD are as follows :

- a) To regenerate a bit clock in synchronism with the bit rate from the disc.
- b) To demodulate the data. (On the disc each byte is represented as a 14 bit word.)
- c) To output the data with corresponding timing signals.

The bit clock is formed as a phase locked loop with varicap diode 6540 as the control element.

## Signals from DEMOD are

Table X2

| DADE | Data DEMOD to ERCO |
| --- | --- |
| FSDE | Frame sync DEMOD to ERCO |
| SSDE | Symbol (8 bit) sync DEMOD to ERCO |
| CLDE | Bit clock DEMOD to ERCO |
| CRI | Mutes ERCO if no data present |

ERCO provides de-interleaving of the data, error detection, and error correction of up to two error bits in any word.

De-interleaving is achieved by storing the data as recieved from DEMOD in buffer RAM 6502 then picking out in the correct order.

Uncorrected errors are flagged on pin 36 of ERCO as UNEC (UNcorrected errors ERCO to CIM).

The parity bits are discarded in ERCO.

## The signals from ERCO are

Table X3

| DAEC | Data ERCO to CIM |
| --- | --- |
| UNEC | Unreliable data ERCO to CIM |
| CLEC | Bit clock ERCO to CIM |
| FSEC | Frame sync ERCO to CIM |

CLOX is the master clock from CIM to ERCO which determines the rate at which data is read from RAM 6502.

CIM (Concealment, Interpolation and Muting) separates the data into left and right streams (DLCF, DRCF) and again provides the necessary timing signals STR1, STR2, CLCF (Bit clock).

There are other functions built into CIM for the Compact Disc system which are not used in this application.

## UNEC descrambler

The error flags from ERCO do not correspond in time with the data leaving CIM. To restore the correct time relationship a further SAA7000 (CIM) is used, IC6604.

IC6604 provides error flags for both data streams.

- Data- DLCF error flags ELCF.
- Data- DRCF error flags ERCF.

## Frequency of CLOX

In the Compact Disc application of this chip set the bit clock (DEMOD) runs in lock with the data from the disc which itself runs at a continually varying speed. CLOX determines the sample play rate and operates as a fixed frequency master clock. The disc is driven at a rate to maintain the contents of RAM 6512.

In this Laservision application the disc (CAV) is driven at a constant controlled speed which may be locked to an outside reference by Genlock.

CIOX therefore must run in sync with the data rate from the disc.

Provision is made to pull CLOX to the precise frequency by varicap diode 6606. The control voltage for 6606 is developed from MCES (motor control error signal from ERCO). MCES is a variable mark/space ratio signal. The mark/space ratio is determined in ERCO by the difference between the bit clock (CLDE) and CLOX. MCES is integrated by IC6602-2a and controls 6606 via 6602-2b. D6605 limits the excursions to protect 6606.

## The manual sheets

<figure class="sheet" markdown>
[![Module W - target ID, CPU memory map and port map / Module X - LV-ROM decoder](../assets/web/cs-7-906-text-p160-preview.webp)](../assets/web/cs-7-906-text-p160-zoom.webp)
<figcaption>
  Module W - target ID, CPU memory map and port map / Module X - LV-ROM decoder.
  <span class="cs">CS 7 906</span>
  <span class="src">service manual page 160</span>
</figcaption>
</figure>

<figure class="sheet" markdown>
[![Module X - LV-ROM decoder (continued)](../assets/web/cs-7-907-text-p161-preview.webp)](../assets/web/cs-7-907-text-p161-zoom.webp)
<figcaption>
  Module X - LV-ROM decoder (continued).
  <span class="cs">CS 7 907</span>
  <span class="src">service manual page 161</span>
</figcaption>
</figure>
