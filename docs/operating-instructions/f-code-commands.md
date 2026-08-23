---
title: F-code commands
description: >-
  Section 6 of the user manual: every F-code command in detail — syntax, codes,
  responses, limits, and the status-byte specifications.
---

# F-code commands

Section 6 of the operating instructions, pages 28 to 35. The functional
explanation of every command: what it does, what it answers, what it refuses,
and the exact meaning of every bit in the status responses.

!!! info "Looking for the list rather than the detail?"

    The command list, the acknowledgements and the handset codes are on
    [F-codes](../reference/f-codes.md) as one searchable set of tables. This
    page is the manual's own account of each command, in the manual's order.

**Conventions used throughout:** `x`, `y` and `z` are ASCII digits; a command is
actioned when the player receives a carriage return; `D` and `H` after a number
mean decimal and hexadecimal. Where a command is marked **CAV only** or
**CLV only**, sending it to the wrong disc type gets a negative acknowledgement.

## Sound and RC-5

#### `!xy` — sound insert (beep)

`!` = 33D = 21H · **Response:** none

Inserts a beep tone in both audio channels. `x` is the pitch — **fixed in the
VP415** — and `y` the duration, roughly 0.3 to 3 s; both range 0 to 9. The beep
is not influenced by the audio channels being switched on or off, or by the
audio controls.

#### `#xy` — RC-5 output via Euroconnector

`#` = 35D = 23H · **Response:** none

Transmits the specified RC-5 command on **pin 8 of the Euroconnector**, to
control certain types of monitor. `x` (40H–5FH) is the RC-5 system number —
40H = system 0 — and `y` (40H–7FH) the RC-5 command number.

## The tray, standby and reset

#### `'` — eject

`'` = 39D = 27H · **Response:** `O` when the tray is opened

Stops the current action and opens the disc-tray; the response is then given
and the player goes to standby. **All defaults are reloaded** — except the
communication protocol — and the `STOP` and `INFO` registers are cleared.

#### `,0` — standby

`,` = 44D = 2CH · **Response:** none

Enters the standby condition. The spinning motor is decelerated and the optical
readout unit goes to lead-in, the home position. All defaults are reloaded
except the communication protocol, and the `STOP` and `INFO` registers are
cleared.

#### `,1` — on

`,` = 44D = 2CH · **Response:** `S` · **Negative:** `O` if the tray is open

**CAV** — the player starts and goes to the first picture after lead-in, in
still mode; the positive acknowledgement is then given.
**CLV** — the player starts and goes to the first time code after lead-in, gives
the acknowledgement, and normal play forward commences.

If the player is already on, this performs a goto the first picture, gives the
acknowledgement, and then stills (CAV) or plays (CLV).

#### `/` — pause

`/` = 47D = 2FH · **Response:** none

**CAV** — still mode with audio and video muted. **CLV** — pause with audio and
video muted. The optical readout unit stays in its current position.

#### `:` — reset to default

`:` = 58D = 3AH · **Response:** none

Resets the player to initial power-on conditions, **except that the
communication protocol remains unchanged**. The `STOP` and `INFO` registers are
not affected.

## The replay switch

#### `$0` — replay switch disable · `$1` — replay switch enable

`$` = 36D = 24H · **Response:** none

`$1` is the power-on default. **The replay function is only active if the
`REPLAY` switch is on *and* it is enabled** — which is how a computer keeps
control of a player whose rear-panel switch has been left on.

## Transmission delay

#### `)0` — transmission delay off · `)1` — transmission delay on

`)` = 41D = 29H · **Response:** none

`)0` is the default. **This delay only affects the RS232-C bus.** With the delay
on, response characters are sent at 20 ms intervals — 50 characters per second
— which may prevent loss of data if a host cannot control the `CTS` handshake
from the player, which must then be kept active continuously.

## Halt and jump — CAV only

#### `*` — halt

`*` = 42D = 2AH · **Response:** none

The player enters still mode. Not applicable to CLV discs.

#### `*xxxxx+yy` — halt and jump forward · `*xxxxx-yy` — halt and jump reverse

`*` = 42D = 2AH, `+` = 43D = 2BH, `-` = 45D = 2DH · **Response:** none

Still picture for a duration of `xxxxx` × 40 ms, followed by a jump forward (or
back) over `yy` pictures. **The function repeats** until another mode command
or a clear command is received, or lead-out (lead-in, for the reverse form) is
entered.

Limits: `xxxxx` > 0, `yy` = 1…50, and **`yy` ≤ 20 × `xxxxx`** — the optical
slide cannot be asked to average more than 20 times normal speed.

#### `+yy` — instant jump forward · `-yy` — instant jump reverse

`+` = 43D = 2BH, `-` = 45D = 2DH · **Response:** none

Jump forward or back over `yy` pictures, `yy` = 1…50. **The jump is performed at
the end of the first video field**, and small jumps are invisible because they
fit inside the video blanking. After the command the player continues its
previous operation.

## Status requests

#### `?F` — picture number request — CAV only

`?` = 63D = 3FH, `F` = 70D = 46H · **Response:** `F xxxxx` ·
**Negative:** `X` if the picture number is not available, `O` if the tray is open

Returns the current picture number as five ASCII digits, `00001`…`59999`. On a
CLV disc the negative acknowledgement `X` is returned.

#### `?C` — chapter number request

`?` = 63D = 3FH, `C` = 67D = 43H · **Response:** `C xx` ·
**Negative:** `X` if not available, `O` if the tray is open

Returns the current chapter number as two ASCII digits, `00`…`79`.

#### `?D` — disc program status request

`?` = 63D = 3FH, `D` = 68D = 44H · **Response:** `D x1 x2 x3 x4 x5` ·
**Negative:** `X` if the disc status is not available, `O` if the tray is open

Returns the disc program status **as recorded on the disc**. Each status byte is
of the form `0011yyyy`.

| Byte | Bits | Meaning |
| --- | --- | --- |
| **x1** | 7–4 | `0011` |
| | 3–0 | `1101` = `D`, or `1011` = `B` |
| **x2** | 7–4 | `0011` |
| | 3–0 | `1100` = `C`, or `1010` = `A` |
| **x3** | 7–4 | `0011` |
| | 3 | 0 = 12-inch disc · 1 = 8-inch disc |
| | 2 | 0 = side 1 · 1 = side 2 |
| | 1 | 0 = no teletext · 1 = teletext present |
| | 0 | 0 = FM-FM multiplex off · 1 = on |
| **x4** | 7–4 | `0011` |
| | 3 | 0 = no program dump · 1 = program dump in audio channel 2 |
| | 2 | 0 = normal video · 1 = video contains digital information |
| | 1, 0 | See the audio table below |
| **x5** | 7–4 | `0011` |
| | 3 | Even parity check with bits 3, 2 and 0 of x4 |
| | 2 | Even parity check with bits 3, 1 and 0 of x4 |
| | 1 | Even parity check with bits 2, 1 and 0 of x4 |
| | 0 | 0 |

Taken together, **x1 and x2 spell `DC` for *CX noise reduction present* and `BA`
for *no CX noise reduction***.

The four bits x4·3, x3·0, x4·1 and x4·0 — in that order — give the state of the
analogue audio channels:

| Bits | Program dump | FM multiplex | Channel 1 | Channel 2 |
| --- | --- | --- | --- | --- |
| `0000` | off | off | stereo | |
| `0001` | off | off | mono | |
| `0010` | off | off | no sound carriers | |
| `0011` | off | off | bilingual | |
| `0100` | off | on | stereo | stereo |
| `0101` | off | on | stereo | bilingual |
| `0110` | off | on | cross-channel stereo | |
| `0111` | off | on | bilingual | bilingual |
| `1000` | on | off | mono | dump |
| `1001` | on | off | mono | dump |
| `1010` | on | off | *(for future use)* | |
| `1011` | on | off | mono | dump |
| `1100` | on | on | stereo | dump |
| `1101` | on | on | stereo | dump |
| `1110` | on | on | bilingual | dump |
| `1111` | on | on | bilingual | dump |

#### `?P` — player status request

`?` = 63D = 3FH, `P` = 80D = 50H · **Response:** `P x1 x2 x3 x4 x5` ·
**Negative:** `O` if the tray is open

Returns the player status. Each byte is of the form `01yyyyyy`. **Zero status
bits are reserved for future use.**

| Byte | Bit | 1 means |
| --- | --- | --- |
| **x1** | 5 | Normal mode (loaded) |
| | 2 | Chapter play |
| | 1, 0 | Goto action |
| **x2** | 2 | Chapter numbers exist on the disc |
| | 1 | CLV detected |
| | 0 | CAV detected |
| **x3** | 2 | Replay function active — switch on *and* enabled |
| | 0 | Frame lock |
| **x4** | 4 | RS232-C transmission delay (50 char/s) |
| | 3 | Remote control handset enabled for player control |
| | 2 | Remote control commands routed to the computer |
| | 1 | Local front-panel controls enabled |
| **x5** | 5 | Audio channel 2 enabled |
| | 4 | Audio channel 1 enabled |
| | 3 | Teletext from disc enabled |

In every byte bit 7 is 0 and bit 6 is 1; the bits not listed are 0.

#### `?U` — user code request

`?` = 63D = 3FH, `U` = 85D = 55H · **Response:** `U x1 x2 x3 x4 x5` ·
**Negative:** `X` if the user code is not available, `O` if the tray is open

Returns the user code as recorded on the disc. **One line of user code is read
during lead-in at player start-up** and saved for subsequent requests. Each byte
is of the form `0011yyyy`, and the status nibbles in hex are: x1 = 0…7,
x2 = `D`, x3, x4, x5 = 0…F.

#### `?=` — revision level request

`?` = 63D = 3FH, `=` = 61D = 3DH · **Response:** `= x1 x2 x3 x4 x5`

Returns the player's firmware revision level as ASCII digits:

| Byte | Meaning |
| --- | --- |
| x1 | 0 |
| x2 | Major revision level of the **drive** software |
| x3 | Minor revision level of the drive software |
| x4 | Major revision level of the **control** software |
| x5 | Minor revision level of the control software |

!!! tip "This is how to read a player's software without opening it"

    A player answering `=01717` is running **drive software 1.7 and control
    software 1.7** — which the
    [survey of software releases](../service-information/software-releases.md)
    identifies as `DRIVE` 3104 103 6803.6 and `CONTROL` 3104 103 6804.7. Real
    responses from a real player are on
    [F-codes](../reference/f-codes.md#responses-from-a-real-player).

## Audio and video switching

#### `A0` / `A1` — audio 1 off / on · `B0` / `B1` — audio 2 off / on

`A` = 65D = 41H, `B` = 66D = 42H · **Response:** none

Disable or enable the internal audio channel from the disc. **On is the
power-on default for both**, and audio is only present during normal play
forward. If one channel is off and the other on, **both outputs are supplied by
the channel that is on**.

#### `E0` / `E1` — video off / on

`E` = 69D = 45H · **Response:** none

Switch off or on the internal video from the disc; on is the default. The video
is *also* switched off by the player when it is not in the active area of the
disc, or when pause, ready or goto are active.

#### `[0` / `[1` — audio 1 from internal / external

`[` = 91D = 5BH · **Response:** none

Internal is the default. With external selected, the internal audio 1 signal is
inhibited in favour of the source on the audio 1 input connector, and **the
audio 1 on/off switch and mute have no function**.

#### `\0` / `\1` — video from internal / external

`\` = 92D = 5CH · **Response:** none

Internal is the default. With external selected, the internal video is inhibited
in favour of the source on the `CVBS IN` connector, and the video on/off switch
and mute have no function.

#### `]0` / `]1` — audio 2 from internal / external

`]` = 93D = 5DH · **Response:** none

As audio 1, for channel 2.

#### `_0` / `_1` — teletext from disc off / on

`_` = 95D = 5FH · **Response:** none

`_1` is the default: the teletext information in the raster blanking lines of
the internal video signal is enabled. `_0` mutes the video lines that may
contain teletext.

## On-screen displays

#### `C0` / `C1` — chapter number display off / on

`C` = 67D = 43H · **Response:** none

Off is the default. Displaying the chapter number **switches the picture number
display off**, and the display is disabled during lead-in, lead-out and goto.

#### `D0` / `D1` — picture number / time code display off / on

`D` = 68D = 44H · **Response:** none

Off is the default. On a CAV disc this is the picture number, on a CLV disc the
time code. Turning it on **switches the chapter number display off**, and it is
disabled during lead-in, lead-out and goto.

## Picture number registers and goto — CAV only

#### `FxxxxxI` — load picture number info register

`F` = 70D = 46H, `I` = 73D = 49H · **Response:** `A3` ·
**Negative:** `AN` on a CLV disc, `O` if the tray is open

The acknowledgement is given when the specified picture number is **passed** by
any play or step action; the `INFO` register is cleared after the response. The
playing mode does not change.

#### `FxxxxxS` — load picture number stop register

`F` = 70D = 46H, `S` = 83D = 53H · **Response:** `A2` ·
**Negative:** `AN` on a CLV disc, `O` if the tray is open

The player **halts** at the specified picture number when it is reached by any
play or step action, and the acknowledgement is then given. The `STOP` register
is cleared after the response.

#### `FxxxxxR` — goto picture number and halt

`F` = 70D = 46H, `R` = 82D = 52H · **Response:** `A0` ·
**Negative:** `AN` if the goto fails, `O` if the tray is open

Searches for the picture and displays it in still mode.

#### `FxxxxxN` — goto picture number and play

`F` = 70D = 46H, `N` = 78D = 4EH · **Response:** `A1` ·
**Negative:** `AN` if the goto fails, `O` if the tray is open

Searches for the picture and commences normal play forward from it.

#### `FxxxxxQ` — goto picture number and continue

`F` = 70D = 46H, `Q` = 81D = 51H · **Response:** `A0` ·
**Negative:** `AN` if the goto fails, `O` if the tray is open

Searches for the picture and **continues the previous play mode** from it.

!!! note "All three gotos mute — unless the jump is short"

    During a goto action the audio and video are muted. **The video is not
    muted if the goto can be performed within the instant jump region of 50
    tracks**, which is what makes map-walking look seamless. On a CLV disc all
    three return `AN`.

## Control routing

#### `H0` / `H1` — RC to computer off / on

`H` = 72D = 48H · **Response:** none

Off is the default. With `H1`, remote control commands are routed to the host
computer instead of acting on the player — **only one response is given per RC
command**. The codes are in
[Table 2](../reference/f-codes.md#handset-keys-routed-to-the-computer).

#### `I0` / `I1` — local control off / on

`I` = 73D = 49H · **Response:** none

Disables or enables the player's own front-panel controls. On is the default.

#### `J0` / `J1` — remote control off / on

`J` = 74D = 4AH · **Response:** none

Whether RC commands are executed by the player at all. On is the default.

## Play modes

#### `L` — still forward · `M` — still reverse — CAV only

`L` = 76D = 4CH, `M` = 77D = 4DH · **Response:** none

Halt and display the next or previous picture. **At least 40 ms must separate
two still commands** for execution to be certain.

#### `N` — play forward

`N` = 78D = 4EH · **Response:** none

Normal play forward. The only play command that works on both disc types.

#### `Nxxxxx+yy` / `Nxxxxx-yy` — play forward and jump — CAV only

`N` = 78D = 4EH with `+` = 43D = 2BH or `-` = 45D = 2DH · **Response:** none

After normal play forward of `xxxxx` pictures, a jump forward (or back) of `yy`
pictures is performed, **repeating** until a clear or other mode command is
received or lead-in/lead-out is reached. Limits: `xxxxx` > 0, `yy` = 1…50,
`yy` ≤ 20 × `xxxxx`.

#### `O` — play reverse, and `Oxxxxx+yy` / `Oxxxxx-yy` — CAV only

`O` = 79D = 4FH · **Response:** none

Normal play reverse, and the same repeating play-and-jump pattern as the `N`
forms, with the same limits.

#### `U` — slow motion forward · `V` — slow motion reverse — CAV only

`U` = 85D = 55H, `V` = 86D = 56H · **Response:** none

Play at the slow speed set by `SxxxS`.

#### `W` — fast forward · `Z` — fast reverse — CAV only

`W` = 87D = 57H, `Z` = 90D = 5AH · **Response:** none

Play at the fast speed set by `SxxxF`.

#### `X` — clear

`X` = 88D = 58H · **Response:** none

**CAV** — any play action is stopped and the player put into still mode, a
chapter play sequence is cancelled, and the picture number `INFO` and `STOP`
registers are cleared.
**CLV** — any chapter play sequence is cancelled and the time code `INFO` and
`STOP` registers are cleared.

A cancelled chapter sequence **does not** send a response to the host.

## Chapters

#### `QxxR` — goto chapter and halt

`Q` = 81D = 51H, `R` = 82D = 52H · **Response:** `A6` ·
**Negative:** `AN` if the goto fails, `O` if the tray is open

Searches for the start of the chapter and displays its first picture. *On CLV
discs, play starts at that chapter.*

#### `QxxN` — goto chapter and play

`Q` = 81D = 51H, `N` = 78D = 4EH · **Response:** `A6` ·
**Negative:** `AN` if the goto fails, `O` if the tray is open

Searches and commences normal play forward from the first picture of the
chapter. Video and audio are muted during the goto.

#### `QxxyyzzS` — play chapter sequence

`Q` = 81D = 51H, `S` = 83D = 53H · **Response:** `A7` ·
**Negative:** `AN` if a search fails, `O` if the tray is open

Plays the specified chapters in turn: each is searched for, played to its end,
and the next searched for. When the last has played, the acknowledgement is
given and the player halts (CAV) or enters pause (CLV).

**A maximum of 7 chapters** may be given, and if more than one is specified,
**two digits per chapter are required**:

```
Q3S        plays chapter 3
Q0312S     plays chapter 3, then chapter 12
```

If a chapter search fails, a negative acknowledgement is given and the sequence
is terminated.

## Speeds — CAV only

#### `SxxxF` — set fast speed

`S` = 83D = 53H, `F` = 70D = 46H · **Response:** none

`xxx` = 2…40, where **2 is normal speed**, 3 is 3/2 × normal and 40 is 20 ×
normal. **The default is 6 — three times normal speed.** Fast play is then
started with `W` or `Z`.

#### `SxxxS` — set slow speed

`S` = 83D = 53H · **Response:** none

`xxx` = 2…250, where 2 is normal speed, 3 is 2/3 × normal and 250 is 2/250 ×
normal — **5 seconds per picture**. The default is 6, one third of normal speed.
Slow play is then started with `U` or `V`.

For compatibility, **`Sxxx` is equivalent to `SxxxS`**.

## Time code — CLV only

#### `TxxyyN` — goto time code

`T` = 84D = 54H, `N` = 78D = 4EH · **Response:** `A8` ·
**Negative:** `AN` if the goto fails, `O` if the tray is open

Searches for the time code and then plays forward normally. `xx` is minutes and
`yy` seconds; **minutes are mandatory, seconds optional**, and if seconds are
given the minutes must be two digits — `07`. Without seconds, or on a disc with
no line-16 Manchester code, the search goes to the start of the specified
minute.

#### `TxxyyI` — load time code info register

`T` = 84D = 54H, `I` = 73D = 49H · **Response:** `A9` ·
**Negative:** `AN` on a CAV disc, `O` if the tray is open

The acknowledgement is given when the time code is **passed** during normal play
forward. Same rules for minutes and seconds; without seconds the acknowledgement
appears on the first second of the specified minute.

## Video overlay

#### `VPy` — video overlay mode

`V` = 86D = 56H, `P` = 80D = 50H · **Response:** none on `VP1`–`VP5`;
`VP1`–`VP5` on `VPX`

Controls the mode of the video processor:

| Command | Mode | What appears |
| --- | --- | --- |
| `VP1` | LaserVision video only | **The power-on default** |
| `VP2` | External RGB only | The computer's picture, alone |
| `VP3` | Hard-keyed | External RGB overlaid on LV video: where the external RGB is black, LV video shows; where it is not, only the external RGB shows |
| `VP4` | Mixed | Transparent overlay — both images at reduced intensity |
| `VP5` | Enhanced | LV video highlighted by external RGB: reduced intensity where the RGB is black, normal intensity where it is not |
| `VPX` | *Interrogate* | Replies with the current mode, `VP1` to `VP5` |

The percentages behind modes 3 to 5 are in
[introduction](introduction.md#video-mixing), and the circuit that does it is
[module Y](../modules/y-video-mixer/index.md).

## The printed pages

<figure class="sheet" markdown>
[![Section 6 divider, first page: the contents of the F-code commands section from sound insert to goto chapter and play, with page numbers](assets/web/operating-instructions-scan-16-a-preview.webp)](assets/web/operating-instructions-scan-16-a-zoom.webp)
<figcaption>
  Section 6 divider and contents, first page.
  <span class="src">operating instructions page 26</span>
</figcaption>
</figure>

<figure class="sheet" markdown>
[![Section 6 contents continued, from play chapter sequence to teletext from disc on](assets/web/operating-instructions-scan-15-a-preview.webp)](assets/web/operating-instructions-scan-15-a-zoom.webp)
<figcaption>
  Section 6 contents, second page.
  <span class="src">operating instructions page 27</span>
</figcaption>
</figure>

<figure class="sheet" markdown>
[![Page describing sound insert, RC-5 output, the replay switch commands, eject, transmission delay, halt and jump, and instant jump forward](assets/web/operating-instructions-scan-18-b-preview.webp)](assets/web/operating-instructions-scan-18-b-zoom.webp)
<figcaption>
  Sound insert through instant jump forward.
  <span class="src">operating instructions page 28</span>
</figcaption>
</figure>

<figure class="sheet" markdown>
[![Page describing instant jump reverse, standby, on, pause, reset to default, and the picture number, chapter number and disc program status requests with their bit specifications](assets/web/operating-instructions-scan-17-b-preview.webp)](assets/web/operating-instructions-scan-17-b-zoom.webp)
<figcaption>
  Instant jump reverse through the disc program status request.
  <span class="src">operating instructions page 29</span>
</figcaption>
</figure>

<figure class="sheet" markdown>
[![Page with the analogue audio channel table, the player status request bit specifications, the user code request and the revision level request](assets/web/operating-instructions-scan-18-a-preview.webp)](assets/web/operating-instructions-scan-18-a-zoom.webp)
<figcaption>
  The audio status table, and the player status, user code and revision level
  requests.
  <span class="src">operating instructions page 30</span>
</figcaption>
</figure>

<figure class="sheet" markdown>
[![Page describing the audio and video on/off commands, the display commands, and the picture number register and goto commands](assets/web/operating-instructions-scan-17-a-preview.webp)](assets/web/operating-instructions-scan-17-a-zoom.webp)
<figcaption>
  Audio, video, displays and the picture number registers.
  <span class="src">operating instructions page 31</span>
</figcaption>
</figure>

<figure class="sheet" markdown>
[![Page describing goto picture number and play or continue, the control routing commands, still forward and reverse, and play forward with jump](assets/web/operating-instructions-scan-20-b-preview.webp)](assets/web/operating-instructions-scan-20-b-zoom.webp)
<figcaption>
  Goto and play, control routing, still and play forward.
  <span class="src">operating instructions page 32</span>
</figcaption>
</figure>

<figure class="sheet" markdown>
[![Page describing play forward and jump reverse, play reverse and its jump variants, the goto chapter commands, the chapter sequence command and set fast speed](assets/web/operating-instructions-scan-19-b-preview.webp)](assets/web/operating-instructions-scan-19-b-zoom.webp)
<figcaption>
  Play reverse, the chapter commands and fast speed.
  <span class="src">operating instructions page 33</span>
</figcaption>
</figure>

<figure class="sheet" markdown>
[![Page describing set slow speed, goto time code, load time code info register, slow motion, fast play, clear and the video overlay modes](assets/web/operating-instructions-scan-20-a-preview.webp)](assets/web/operating-instructions-scan-20-a-zoom.webp)
<figcaption>
  Slow speed, time code, clear and video overlay.
  <span class="src">operating instructions page 34</span>
</figcaption>
</figure>

<figure class="sheet" markdown>
[![Page describing the VPX interrogation and the internal-or-external source commands for audio 1, video, audio 2 and teletext from disc](assets/web/operating-instructions-scan-19-a-preview.webp)](assets/web/operating-instructions-scan-19-a-zoom.webp)
<figcaption>
  VPX, and the internal-or-external source commands.
  <span class="src">operating instructions page 35</span>
</figcaption>
</figure>

## Related

- [F-codes](../reference/f-codes.md) — the same command set as tables, with
  real-player responses
- [F-code programming](f-code-programming.md) — the interface these commands
  travel over
- [SCSI operation](scsi-operation.md) — sending F-codes as SCSI group 6
  commands
- [Special play functions](special-play-functions.md) — the same functions from
  the handset
