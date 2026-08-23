---
title: F-codes
description: >-
  The complete F-code command set for the VP415, the acknowledgements the
  player sends back, and the responses a real player gives for each Domesday
  disc side.
---

# F-codes

**F-codes are how a computer drives a VP415.** Send a few ASCII characters and
a carriage return down the RS232-C line — or the same string through the SCSI
interface — and the player plays, jumps, freezes, or tells you where it is.
The whole command set is on this page, in one searchable table.

This is the *reference*: what to send and what comes back. The manual's own
account of how the interface works — the connector, DTR and CTS handshaking,
baud rates, and a page of explanation per command — is in the operating
instructions, under
[F-code programming](../operating-instructions/f-code-programming.md) and
[F-code commands](../operating-instructions/f-code-commands.md).

!!! info "The three rules"

    1. **Every command ends with a carriage return (CR).** Nothing happens
       until the player sees it.
    2. **Digits are ASCII, and leading zeros are optional** on the way in. On
       the way out the player always sends them.
    3. **The player answers only some commands.** Which ones, and with what, is
       the acknowledgement table below.

## The command set

Where a row has no decimal and hex code of its own, it is a variant of the
command above it — `A0` and `A1` are both decimal 65.

!!! note "Where this table comes from"

    It is Table 1 of the operating instructions, page 22, transcribed from the
    vendor OCR and then checked cell by cell against the page photographed at
    native resolution — which corrected four characters the OCR could not see:
    the eject command is `'` and not `:`, halt is `*` and not a bullet, and the
    three source-select commands are `[`, `\\` and `]`, which came through as
    bare pipes.

    The collection also holds `vp415Fcode.xlsx`, somebody's typed copy of the
    same table. It agrees with the manual **row for row, all 72 of them**, and
    differs only in six typing slips — *AN EUROCONNECTOR* for A/V, *Audio-I*
    for Audio-1, a missing space in *routed toicomputer*, `_O` for `_0`, a
    stray `1`, and `2-251)` for the slow speed range `2-250`. The manual is
    what is published here.

| Dec | Hex | Command | Function |
| --- | --- | --- | --- |
| **33** | `21` | `!xy` | Sound insert (beep) |
| **35** | `23` | `#xy` | RC-5 command out via A/V EUROCONNECTOR |
| **36** | `24` | `$0` | Replay switch disable |
|  |  | `$1` | Replay switch enable (default) |
| **39** | `27` | `'` | Eject (open the frontloader tray) |
| **41** | `29` | `)0` | Transmission delay off (default) |
|  |  | `)1` | Transmission delay on |
| **42** | `2A` | `*` | Halt (still mode) |
|  |  | `*xxxxx+yy` | Repetitive halt and jump forward |
|  |  | `*xxxxx-yy` | Repetitive halt and jump backward |
| **43** | `2B` | `+yy` | Instant jump forward yy tracks (max 50) |
| **44** | `2C` | `,0` | Standby (unload) |
|  |  | `,1` | On (load) |
| **45** | `2D` | `-yy` | Instant jump backward yy tracks (max 50) |
| **47** | `2F` | `/` | Pause (halt + all muted) |
| **58** | `3A` | `:` | Reset to default values |
| **63** | `3F` | `?F` | Picture number request |
|  |  | `?C` | Chapter number request |
|  |  | `?D` | Disc program status request |
|  |  | `?P` | Player status request |
|  |  | `?U` | User code request |
|  |  | `?=` | Revision level request |
| **65** | `41` | `A0` | Audio-1 off |
|  |  | `A1` | Audio-1 on (default) |
| **66** | `42` | `B0` | Audio-2 off |
|  |  | `B1` | Audio-2 on (default) |
| **67** | `43` | `C0` | Chapter number display off (default) |
|  |  | `C1` | Chapter number display on |
| **68** | `44` | `D0` | Picture number/time code display off (default) |
|  |  | `D1` | Picture number/time code display on |
| **69** | `45` | `E0` | Video off |
|  |  | `E1` | Video on (default) |
| **70** | `46` | `FxxxxxI` | Load picture number information register |
|  |  | `FxxxxxS` | Load picture number stop register |
|  |  | `FxxxxxR` | Goto picture number then Still mode |
|  |  | `FxxxxxN` | Goto picture number then normal play forward |
|  |  | `FxxxxxQ` | Goto picture number and continue previous play mode |
| **72** | `48` | `H0` | Remote control not routed to computer (default) |
|  |  | `H1` | Remote control routed to computer |
| **73** | `49` | `I0` | Local front-panel buttons disabled |
|  |  | `I1` | Local front-panel buttons enabled (default) |
| **74** | `4A` | `J0` | Remote control disabled for player control |
|  |  | `J1` | Remote control enabled for player control (default) |
| **76** | `4C` | `L` | Still forward |
| **77** | `4D` | `M` | Still reverse |
| **78** | `4E` | `N` | Normal play forward |
|  |  | `Nxxxxx+yy` | Repetitive play forward and jump forward |
|  |  | `Nxxxxx-yy` | Repetitive play forward and jump backward |
| **79** | `4F` | `O` | Play reverse |
|  |  | `Oxxxxx+yy` | Play reverse and jump forward |
|  |  | `Oxxxxx-yy` | Play reverse and jump reverse |
| **81** | `51` | `QxxR` | Goto chapter and halt |
|  |  | `QxxN` | Goto chapter and play |
|  |  | `QxxyyzzS` | Goto chapter (sequence) and halt |
| **83** | `53` | `SxxxF` | Set fast speed value, 2-40 |
|  |  | `SxxxS` | Set slow speed value, 2-250 |
| **84** | `54` | `TxxyyN` | Goto time code xx=min, yy=sec (yy=opt) |
|  |  | `TxxyyI` | Load time code info register (yy=opt) |
| **85** | `55` | `U` | Slow motion forward |
| **86** | `56` | `V` | Slow motion reverse |
|  |  | `VPy` | Video overlay (VP1 is default) |
| **87** | `57` | `W` | Fast forward |
| **88** | `58` | `X` | Clear |
| **90** | `5A` | `Z` | Fast reverse |
| **91** | `5B` | `[0` | Audio-1 from internal (default) |
|  |  | `[1` | Audio-1 from external |
| **92** | `5C` | `\0` | Video from internal (default) |
|  |  | `\1` | Video from external |
| **93** | `5D` | `]0` | Audio-2 from internal (default) |
|  |  | `]1` | Audio-2 from external |
| **95** | `5F` | `_0` | Teletext from disc off |
|  |  | `_1` | Teletext from disc on (default) |

## What the player sends back

Most commands are silent. These are the ones that answer:

| Dec | Hex | Response | Sent when |
| --- | --- | --- | --- |
| **79** | `4F` | `O` | Returned when disc-tray is opened on `'` (eject) command, or when disc-tray is open and a command which expects a response is received. |
| **83** | `53` | `S` | Ackn. on ON command when disc reaches correct speed. |
| **61** | `3D` | `= x1 x2 x3 x4 x5` | Returned after revision level request (?=). |
| **70** | `46` | `F x1 x2 x3 x4 x5` | Returned after frame number request command (?F). |
| **67** | `43` | `C x1 x2` | Returned after chapter number request command (?C). |
| **68** | `44` | `D x1 x2 x3 x4 x5` | Returned after disc status request command (?D). |
| **80** | `50` | `P x1 x2 x3 x4 x5` | Returned after player status request command (?P). |
| **85** | `55` | `U x1 x2 x3 x4 x5` | Returned after user code request command (?U). |
| **86** | `56` | `VP1...VP5` | Returned after video mode request command (VPX). |
| **88** | `58` | `X` | Returned after ?F,?C,?D or ?U when the information is not available. |
| **65** | `41` | `A 0` | Acknowledgement on FxxxxR or FxxxxQ when completed. |
|  |  | `A 1` | Acknowledgement on FxxxxN when completed. |
|  |  | `A 2` | Acknowledgement on FxxxxS when stopped. |
|  |  | `A 3` | Acknowledgement on FxxxxI when passed. |
|  |  | `A 6` | Acknowledgement on QxxN or QxxR when completed. |
|  |  | `A 7` | Acknowledgement on QxxS when completed. |
|  |  | `A 8` | Acknowledgement on TxxN when completed. |
|  |  | `A 9` | Acknowledgement on TxxI when passed |
|  |  | `A N` | Negative acknowledgement: picture number, chapter number or time code in error. |

Each response is terminated by a carriage return, all characters including
leading zeros are sent, and the digits `x1`…`x5` are ASCII.

## Handset keys routed to the computer

After `H1` — *remote control routed to computer* — the handset stops driving
the player and its keypresses arrive at the computer instead, as `L x` for the
function keys and `V x` for the numeric keys:

| Handset key | `L` code |
| --- | --- |
| STANDBY | `;` |
| DISPLAY | `!` |
| NEXT | `*` |
| CLEAR | `X` |
| ENTER | `P` |
| START/REPEAT | `F` |
| AUDIO1 | `A` |
| AUDIO2 | `B` |
| CNR | `R` |
| PNR | `D` |
| CORR | `C` |
| GOTO | `K` |
| FAST▶ | `W` |
| FAST◀ | `Z` |
| SLOW▶ | `T` |
| SLOW◀ | `U` |
| SPEED + | `H` |
| SPEED - | `G` |
| TXT | `Y` |
| PAUSE | `V` |
| SEARCH▶ | `>` |
| SEARCH◀ | `<` |
| STILL▶ | `L` |
| STILL◀ | `M` |
| PLAY▶ | `N` |
| PLAY◀ | `O` |

| Numeric key | `V` code |
| --- | --- |
| DIGIT0 | `0` |
| DIGIT1 | `1` |
| DIGIT2 | `2` |
| DIGIT3 | `3` |
| DIGIT4 | `4` |
| DIGIT5 | `5` |
| DIGIT6 | `6` |
| DIGIT7 | `7` |
| DIGIT8 | `8` |
| DIGIT9 | `9` |

## Responses from a real player

Original data, not from any manual: the four status commands issued to a real
VP415 with each side of a set of BBC Domesday and related LV-ROM discs in it,
and the exact response the player gave.

| Disc and side | `?D` disc status | `?P` player status | `?U` user code | `?=` revision |
| --- | --- | --- | --- | --- |
| National ++ (Side A) | `D;:026` | ``P`AAHp`` | `U1=986` | `=01717` |
| National ++ (Side B) | `D;:01?` | ``P`FAHp`` | `U1=987` | `=01717` |
| CommunityN (Side A) | `D;:41?` | ``P`AAHp`` | `U1=067` | `=01717` |
| CommunityS (Side B) | `D;:026` | ``P`AAHp`` | `U1=066` | `=01717` |
| National (Side A) | `D;:01?` | ``P`AAHp`` | `U1=986` | `=01717` |
| National (Side B) | `D;:01?` | ``P`FAHp`` | `U1=987` | `=01717` |
| CommunityN (Side A) (second copy) | `D;:41?` | ``P`AAHp`` | `U1=067` | `=01717` |
| CommunityS (Side B) (second copy) | `D;:01?` | ``P`AAHp`` | `U1=066` | `=01717` |
| Volcanoes (single sided disc) | `D;:000` | ``P`AAHp`` | `U1=986` | `=01717` |
| Countryside (Side A) | `D;:039` | ``P`AAHP`` | `U1=991` | `=01717` |
| Countryside (Side B) | `D;:439` | ``P`AAHP`` | `U1=992` | `=01717` |
| The Eco Disc (Side A) | `D;:026` | ``P`AAHp`` | `U1=988` | `=01717` |
| The Eco Disc (Side B) | `D;:41?` | ``P`AAHp`` | `X` | `=01717` |

Every byte of these responses is decodable against the specifications in
[F-code commands](../operating-instructions/f-code-commands.md). Worked
through for **National ++ side A**:

| Response | Byte | Value | Means |
| --- | --- | --- | --- |
| `D;:026` | x1 = `;` | `0011 1011` = B | With x2, `BA` — **no CX noise reduction** |
| | x2 = `:` | `0011 1010` = A | |
| | x3 = `0` | `0011 0000` | 12-inch disc · side 1 · no teletext · FM-FM multiplex off |
| | x4 = `2` | `0011 0010` | No program dump · normal video · audio bits `0010` |
| | x5 = `6` | `0011 0110` | Parity over x4 — and it checks out |
| ``P`AAHp`` | x1 = `` ` `` | `0110 0000` | **Normal mode, disc loaded** |
| | x2 = `A` | `0100 0001` | **CAV disc** |
| | x3 = `A` | `0100 0001` | **Frame lock** |
| | x4 = `H` | `0100 1000` | Handset enabled for player control |
| | x5 = `p` | `0111 0000` | Audio channels 1 and 2 both enabled |

Four things fall out of the table that are worth knowing:

- **`?=` is the same on every disc — `=01717`.** It is the *player's* software
  revision, not the disc's, which is why it does not move. The five bytes are
  `0`, then the major and minor revision of the **drive** software and the major
  and minor revision of the **control** software, so this player was running
  **drive 1.7 and control 1.7**: `DRIVE` 3104 103 6803.6 and `CONTROL`
  3104 103 6804.7 in the
  [survey of software releases](../service-information/software-releases.md) —
  the last drive release, and the second-to-last control release. Reading `?=`
  is the quickest way to identify a set's software without opening it; see
  [modification levels](../general-service/modification-levels.md).
- **The `?P` byte x2 distinguishes CAV from CLV.** ``P`AAHp`` is a CAV side;
  ``P`FAHp`` — x2 = `F`, `0100 0110` — is **CLV with chapter numbers on the
  disc**.
- **Countryside answers ``P`AAHP``,** with x5 = `P` rather than `p`: audio
  channel 1 enabled, channel 2 not.
- **The Eco Disc side B answers `?U` with `X`** — the *information not
  available* response from the acknowledgement table, rather than a user code.

!!! warning "The source disagrees with itself in three places"

    These readings were taken twice, and the record has three internal
    conflicts. They are reproduced above exactly as written, and none of them
    has been quietly corrected:

    - **CommunityS (side B)** is recorded as `D;:026` in the first pass and
      `D;:01?` in the second.
    - **National (side B)** is recorded as ``P`FAHp``, but the decimal bytes
      written beside it — 080 096 065 065 072 112 — spell ``P`AAHp``.
    - **Countryside (side B)** has the byte list of its own `?U` response
      copied into the `?D` row.

    Where the ASCII string and the decimal bytes disagree, the bytes are the
    safer record: they were read off the wire.

## Talking to a player today

The interface is a 25-pin D on the back panel, and it is plain RS232-C:

| Setting | Value |
| --- | --- |
| Baud | 1200 / 2400 / 4800 / 9600, set by dip switches 1 and 2 at the rear |
| Format | 8 data bits, 1 stop bit, parity ignored |
| Flow control | The player raises **DTR** (pin 20) when it can accept data, and waits for **CTS** (pin 5) before transmitting |

If the computer cannot drive CTS, leave pin 5 open and send `)1` —
*transmission delay on* — which slows the player to 50 characters per second.
The full pinning, and the connector's +12 V and −12 V pins, are on
[F-code programming](../operating-instructions/f-code-programming.md) and in
[connector pinning](../overview/connector-pinning.md).

## Related

- [F-code programming](../operating-instructions/f-code-programming.md) — the
  manual's section 5: interface, handshaking, baud rates, registers
- [F-code commands](../operating-instructions/f-code-commands.md) — the
  manual's section 6: a description of every command, with the status-byte
  specifications the responses above decode against
- [SCSI operation](../operating-instructions/scsi-operation.md) — the same
  F-codes, sent as SCSI group 6 commands
- [Modification levels](../general-service/modification-levels.md) — using `?=`
  to read a player's software revision
- [Firmware](firmware.md) — the software revisions themselves
