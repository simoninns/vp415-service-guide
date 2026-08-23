---
title: Alphabetical signal listing
description: >-
  All 243 signal mnemonics used in the VP415 circuit diagrams, with their
  meanings and active levels.
---

# Alphabetical signal listing

Every signal name that appears in a VP415 circuit diagram, in the manual's own
order. This is the page to search when a diagram hands you a three-letter name
and no explanation.

!!! tip "Searching"

    Use the site search — it indexes this table, so typing a mnemonic finds it
    here and on any module page that mentions it. Signal names are printed on
    the circuit diagrams in the same form as the first column below.

!!! note "Overbars"

    The manual prints an overbar on active-low signals — `TI`, `ATN`, `CS 1-8`
    and many others. The bar is not reproduced in the table below, because it
    would make the names harder to search for; the polarity it conveys is in
    the **active / level** column instead.

| Signal | Meaning | Active / level |
| --- | --- | --- |
| `-(B-Y)` | Colour difference B-Y |  |
| `-(R-Y)` | Colour difference R-Y |  |
| `+12` | Switched +12V |  |
| `+12SB` | +12V standby supply |  |
| `+5` | Switched +5V |  |
| `+5SB` | +5V standby supply |  |
| `0-RPM` | 0 RPM status | 0V = 0 RPM |
| `-12` | Switched -12V |  |
| `-12SB` | -12V standby supply |  |
| `2-PPR` | 2 pulses per revolution | pos.pulses |
| `400Hz PAL` | PAL switching signal |  |
| `-5SB` | -5V standby supply |  |
| `80-FH` | 80 times horizontal freq. |  |
| `A1-E/I` | Audio 1 internal/external | +12V = ext |
| `A2-E/I` | Audio 2 internal/external | +12V = ext |
| `ALE` | Address latch enable |  |
| `A-SYNT` | Synthesised audio on/off | +12V = on |
| `ATN` | Attention | 0V = active |
| `AUD1` | Audio 1 |  |
| `AUD1+2` | Audio 1 + audio 2 |  |
| `AUD1ON` | Audio 1 on/off | +12V = on |
| `AUD2` | Audio 2 |  |
| `AUD2ON` | Audio 2 on/off | +12V = on |
| `B` | Blue video signal |  |
| `BF` | Burst flag | pos.pulses |
| `B-MIX` | Blue video signal from mixer |  |
| `BP-CLP` | Bypass clamp | pos.pulses |
| `BRA` | Baudrate select A | 0V / +5V |
| `BRB` | Baudrate select B | 0V / +5V |
| `B-TTL` | Blue video signal TTL level |  |
| `BURST-ER` | Burst error signal |  |
| `CBL` | Composite blanking | pos.pulses |
| `CLCF` | Bit clock CIM to FIL |  |
| `CLDE` | Bit clock DEMOD to ERCO |  |
| `CLEC` | Bit clock ERCO to CIM |  |
| `CLOX` | LV-ROM decoder master clock |  |
| `CLP` | Clamp pulse | pos.pulses |
| `CL-RAD` | Clipped radial | -12V / +12V |
| `CL-VID` | Clipped video | 0V / +12V |
| `CLV-TC` | CLV trackcross | +5V = active |
| `COMM1` | Commutation coil 1 | +5V = on |
| `COMM2` | Commutation coil 2 | +5V = on |
| `COMM3` | Commutation coil 3 | +5V = on |
| `COMM4` | Commutation coil 4 | +5V = on |
| `CP-1` | Course pulse 1 | 0V = active |
| `CP-2` | Course pulse 2 | 0V = active |
| `CS` | Composite sync |  |
| `CS 1-8` | Chip select 1 up to 8 |  |
| `CS-EXT` | External comp. sync input |  |
| `CS-REF` | Composite sync reference | pos.pulses |
| `CS-S/NS` | Standard/non standard CS select | +5V = standard |
| `CS-TTL` | Comp. sync TTL level |  |
| `CTS` | Clear to send (RS232) |  |
| `CTS1` | CTS |  |
| `CTS2` | CTS |  |
| `CTS3` | CTS |  |
| `CV/CS` | CVBS/Comp. Sync select | +12V = CVBS |
| `CVBS IN` | External CVBS input signal |  |
| `CVBS` | Composite video/burst/sync |  |
| `CVBS OUT` | CVBS output signal |  |
| `CVBS2` | Disc CVBS without special burst |  |
| `CVBS-INT` | Internal CVBS |  |
| `CV-DEM` | CVBS demodulated |  |
| `CV-DOC` | CVBS dropout corrected |  |
| `CV-E/J` | CVBS external/internal select | +12V = external |
| `CV-EXT` | External CVBS |  |
| `CV-TBC` | CVBS time base corrected |  |
| `CV-TBM` | CVBS time base measurement |  |
| `CX-OFF` | CX on/off | +12V = off |
| `DADE` | Data DEMOD to ERCO |  |
| `DA-DUMP` | Data disc dump |  |
| `DAEC` | Data ERCO to CIM |  |
| `DAK` | S-bus data acknowledge |  |
| `DAV` | S-bus data available |  |
| `DB/STAT` | Databit/status text insert | 0V = busy |
| `DEM-BK` | Demodulator burst key | pos.pulses |
| `DEMV` | Demodulated vert. pulse |  |
| `DLCF` | Data left CIM to FIL |  |
| `DLEN` | P-bus data line enable | +5V = active |
| `DO-INH` | Dropout protection inhibit | +12V = active |
| `DR` | Disc reflection | +5V = refl |
| `DRCF` | Data right CIM to FIL |  |
| `DTR` | Data terminal ready (RS232) |  |
| `DTR 3` | DTR |  |
| `DTR 1` | DTR |  |
| `DTR 2` | DTR |  |
| `DUMP` | Dump on/off switch | 0V = dump on |
| `DUMP-ON` | Data dump on/off | +12V = on |
| `EJECT` | Eject button | 0V = active |
| `ELCF` | Error flag left |  |
| `ERCF` | Error flag right |  |
| `ER-DIS` | Error display | 0V = active |
| `EXT AUD 1` | External audio 1 |  |
| `EXT AUD 2` | External audio 2 |  |
| `FAS-REL` | Phase relation |  |
| `FI` | Field identification |  |
| `FOCACT` | Focus actuator drive signal |  |
| `FOC-EN` | Focus enable | +12V = enable |
| `FOC-ER` | Focus error |  |
| `FOC-IND` | In focus indication | 0V = in focus |
| `FPI` | Focus position indication | -12V = in position |
| `FRLOCK` | Frame lock | +5V = in lock |
| `FSDE` | Frame sync DEMOD to ERCO |  |
| `FSEC` | Frame sync ERCO to CIM |  |
| `G` | Green video signal |  |
| `GLC` | Genlock clock (4.5MHz) |  |
| `GL-CL` | Genlock clock (4.5MHz) |  |
| `G-MIX` | Green video signal from mixer |  |
| `G-TTL` | Green video signal TTL level |  |
| `H/2` | PAL 8kHz pulse |  |
| `HALL C-` | Signals from HALL elements |  |
| `HALL B-` | Signals from HALL elements |  |
| `HALL C+` | Signals from HALL elements |  |
| `HALL B+` | Signals from HALL elements |  |
| `HALL AV+` | Signals from HALL elements |  |
| `HALL A-` | Signals from HALL elements |  |
| `HALL A+` | Signals from HALL elements |  |
| `HALL CV-` | Signals from HALL elements |  |
| `HFATBC` | HF audio timebase corrected |  |
| `HF-AUD` | HF audio |  |
| `HF-OUT 1` | HF signal disc drive |  |
| `HF-OUT 2` | HF signal sandwich |  |
| `HMANCH` | Horizontal sync | neg.pulses |
| `HOR. BL` | Horizontal blanking adjustment |  |
| `HW-TEST` | Hardware test |  |
| `INS-TXT` | TXT signal for insert |  |
| `IRQ` | Interrupt request |  |
| `IR-REC` | ROS from IR receiver |  |
| `LA` | Laser on/off | 0V = off |
| `LA-STA` | Laser status | 0V = on |
| `LDI` | Load index |  |
| `LED1` | LED drive |  |
| `LED2` | LED drive |  |
| `LMOT-L` | Load motor left | +5V = on |
| `LMOT-R` | Load motor right | +5V = on |
| `LPO` | Line pulse out |  |
| `LPWM` | Line pulse width modulated |  |
| `LUM` | Luminance |  |
| `MCES` | Motor control error signal |  |
| `MCO` | Motor control output |  |
| `MCO-EN` | MCO enable | +12V = active |
| `MEM-SU` | Memory start up | +5V = active |
| `M-LOCK` | Motor lock |  |
| `MOT C` | Motor drive signals |  |
| `MOT B` | Motor drive signals |  |
| `MOT A` | Motor drive signals |  |
| `MTF` | Motional transfer function |  |
| `NPL` | Normal play forward | +5V = active |
| `NS-CS` | Non standard composite sync |  |
| `NS-VID` | Non standard video indication | +12V = NSV |
| `OBF` | Output buffer full |  |
| `OBS` | Output burst switch NTSC | +12V = active |
| `PWM` | Pulse width modulated |  |
| `Q1` | Stepping motor coil 1 (Yellow) |  |
| `Q1,2` | Common 1,2 (Red) |  |
| `Q2` | Stepping motor coil 2 (Grey) |  |
| `Q3` | Stepping motor coil 3 (Yellow) |  |
| `Q3,4` | Common 3,4 (Red) |  |
| `Q4` | Stepping motor coil 4 (Grey) |  |
| `R` | Red video signal |  |
| `RADACT` | Radial actuator drive signal |  |
| `RAD-ER` | Radial error |  |
| `RAD-FS` | Radial filter select | 0V = low pass |
| `RAMP-EN` | Ramp enable | pos.pulses |
| `RC5 IN(B)` | RC5 input SCART |  |
| `RC5` | RC5 commands |  |
| `RC5-INT` | RC5 from IR receiver |  |
| `RC5-SCART` | RC5 commands SCART |  |
| `RC5-OUT` | RC5 output control |  |
| `RCIR` | RC input IR/SCART | +5V = IR |
| `RD` | Read |  |
| `RDEN` | S-bus read enable |  |
| `RD-STRT` | Read start pulse text insert | +5V = inactive |
| `REF-CLP` | Clamp |  |
| `REFH` | Horizontal reference | pos.pulses |
| `REFV` | Vertical reference | pos.pulses |
| `REPLAY` | Replay switch on/off | 0V = replay |
| `RESI` | Reserved input dipswitch |  |
| `RESI 1` | Reserved input drive |  |
| `RESO 1` | Reserved output drive |  |
| `RESUPI` | Reset UPI |  |
| `RGB-STA` | RGB status signal SCART |  |
| `RLS` | Radial loop switch | +0V = closed |
| `R-MIX` | Red video signal from mixer |  |
| `R-TTL` | Red video signal TTL level |  |
| `RXD` | Received data (RS232) |  |
| `RXD1` | RXD |  |
| `RXD2` | RXD |  |
| `RXD3` | RXD |  |
| `SC` | Sandcastle pulse | pos.pulses |
| `SCANLS` | Scan loop switch | 0V = active |
| `SCL` | I²C bus clock |  |
| `SCLT` | P-bus clock |  |
| `SCSI` | Small computer system interface |  |
| `SD 0-7` | S-bus data |  |
| `SDA` | I²C bus data |  |
| `SDAT` | P-bus data |  |
| `SEL` | Selection |  |
| `SL-PWR` | Slide power low/high | +5V = low |
| `SMF` | Switch mode frequency | 17,6 kHz |
| `SPI` | Slide position indication | 0V = inwards |
| `SP-POS` | Spot position |  |
| `SSDE` | Symbol sync DEMOD to ERCO |  |
| `ST-ST` | Start-stop switch | 0V = start |
| `STB` | Strobe | 0V = active |
| `STBY` | Standby command | 0V = standby |
| `STBY-BUT` | Standby button command |  |
| `STR1` | Strobe 1 (16 bit word) |  |
| `STR2` | Strobe 2 (8 bit word) |  |
| `SYNC IN` | External sync input signal |  |
| `SYNC OUT` | Sync output signal |  |
| `TANG-ER` | Tangential error |  |
| `TI` | Tray inside | 0V = inside |
| `TILTOK` | Tilt in position | 0V = in position |
| `TLS` | Tilt loop switch | +5V = closed |
| `TPI` | Track position indication (+6 / −6 V) | −6V = on track |
| `TSP` | Terminal speed |  |
| `TTM` | Turntable motor on/off | +5V = on |
| `TX/RX` | Transmit/receive data | 0V = receive |
| `TXD` | Transmit data (RS232) |  |
| `TXD1` | TXD |  |
| `TXD2` | TXD |  |
| `TXD3` | TXD |  |
| `TXT-IW` | Teletext insertion window |  |
| `TXT-WH` | Teletext window horizontal | pos.pulses |
| `TXT-WV` | Teletext window vertical | pos.pulses |
| `UNEC` | Unreliable data ERCO to CIM (Error flag) |  |
| `V/C-TXT` | Video/control text insert | +5V = video text |
| `VBL` | Vertical blanking | neg.pulses |
| `VI-A/D` | Video analogue/digital | +12V = analogue |
| `VI-DOP` | Video dropout pulse |  |
| `VMANCH` | Vertical sync | neg.pulses |
| `VOBN` | Video background insertion | 0V = active |
| `VOW` | Video character insertion | +5V= active |
| `VP0` | Video mixer control 0 |  |
| `VP1` | Video mixer control 1 |  |
| `VP2` | Video mixer control 2 |  |
| `VR` | Vertical reference |  |
| `WDOGRS` | Watchdog reset | +5V = reset |
| `WINDOW` | S-bus window |  |
| `WR` | Write |  |
| `WR-CLK` | Write clock text insert | +5V = inactive |
| `WREN` | S-bus write enable |  |

<figure class="sheet sheet--fold" markdown>
[![Alphabetical signal listing: four columns of signal mnemonics with their meanings and active levels](assets/web/cs-7-830-table-p020-preview.webp)](assets/web/cs-7-830-table-p020-zoom.webp)
<figcaption>
  Alphabetical signal listing.
  <span class="cs">CS 7 830</span>
  <span class="src">service manual page 020</span>
</figcaption>
</figure>

!!! info "Corrections to the transcription"

    Twenty-two mnemonics came out of the OCR wrong and have been corrected
    against the 300 dpi scan: `+12SB`, `+5SB`, `−12SB`, `−5SB`, `0-RPM`,
    `A1-E/I`, `A2-E/I`, `AUD1ON`, `AUD2ON`, `CLOX`, `DAEC`, `FSDE`, `FPI`,
    `MCO`, `MCO-EN`, `Q1,2`, `RC5 IN(B)`, `RLS`, `STBY-BUT`, `TILTOK`, `TPI`
    and `TX/RX`. The eight `HALL` and three `MOT` entries share a brace on the
    sheet; each row carries the shared meaning here. Click the scan above if
    anything looks wrong.
