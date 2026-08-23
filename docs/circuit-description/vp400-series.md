---
title: VP400 series architecture
description: >-
  How the player is put together: the audio/video signal path, the control
  routes, the start-up sequence, the S-bus, and the servo block diagram.
---

# VP400 series

Chapter 2 of the manual's circuit description: the player as a system. Three
block diagrams and the prose that goes with them.

The same three diagrams are reproduced without commentary in chapter 3, as
[block diagrams](../system/block-diagrams.md); this page is where they are
explained.

## Introduction

The VP400 series is a generation of LaserVision disc drives with all the
LaserVision facilities — picture or chapter search, moving pictures, still
frames, forward, reverse and variable speed — programmable through a separate
computer for interactive applications.

Characteristic of these disc drives:

- Front loading
- Solid-state laser
- Computer control via RS232C interface
- RGB output for full-bandwidth moving or still pictures
- Functional modular design
- Average random access time ≤ 1 s
- Instant jump of up to 50 frames in either direction
- Electronic timebase correction
- Genlock external video synchronisation
- Infra-red / wired or SCART RC-5 remote control
- Programmable with the remote control handset
- Auto replay via replay switch

Depending on the specific type in the VP400 generation, further features are
added — the LV-ROM decoding and SCSI interface of the VP415 among them.

## Audio / video signal path

Follow it module by module. The corresponding diagram is Fig. SP1.

**Off the disc.** The audio and video information is fixed on the disc as pits
and read by a 780 nm laser beam. The modulated light falls on the photodiode and
is converted into a high-frequency electrical signal, amplified on
[module Z](../modules/z-deck-electronics/index.md). Its output, `HF-OUT 1`,
goes to [module K](../modules/k-hf-processor/index.md).

**Splitting HF.** Module K first splits the signal into an HF audio and an HF
video signal. `HF-AUD` goes to [module H](../modules/h-etbc-b/index.md) for
timebase correction. The HF video is demodulated on module K and gets amplitude
correction from the `MTF` signal; the demodulated composite video, `CV-DEM`,
goes to [module L](../modules/l-video-dropout-correction/index.md).

**Drop-out correction.** Module L fills a video line containing a drop-out with
the contents of the preceding line: the video signal is delayed one line time
(64 μs) and, when the drop-out detector fires, a switch selects the delayed
video instead of the direct video. Module L also creates the `MTF` signal, by
measuring the amplitude of the colour burst in the video signal and producing a
DC voltage proportional to it. Its output, `CV-DOC`, goes to module H.

**Timebase correction.** On module H both `HF-AUD` and `CV-DOC` pass through a
CCD memory IC, which delays them by an amount set by the clock frequency
supplied. That clock comes from a VCO controlled by `TANG-ER`, the tangential
or timebase error signal — **the coarse correction**. Both signals then pass
through a variable LC delay line whose delay depends on `BURST-ER` — **the fine
correction**. `BURST-ER` is the result of comparing the phase of the disc video
signal `CV-TBM` against a reference derived from
[reference source module D](../modules/d-reference-source/index.md). The
corrected signals `HFATBC` and `CV-TBC` go on to modules A and C.

**Audio.** On [module A](../modules/a-audio-processor/index.md) `HFATBC` is
split into two paths and the two audio channels demodulated. Drop-out detection
happens here too: on a drop-out the LF audio is held at the level it had just
before the drop-out — the track-and-hold principle. Outputs `AUD1` and `AUD2`
go to [analog I/O module U](../modules/u-analog-io/index.md).

On module U, `AUD1` and `AUD2` are selected against the external audio inputs
`EXT AUD1` and `EXT AUD2`, and can be switched off with `AUD1ON` and `AUD2ON`.
A beep can be added depending on the `A-SYNT` command from
[drive processor module R](../modules/r-drive-processor/index.md). Both audio
signals appear on the rear-panel cinch connectors and on the Euroconnector.

**Video.** `CV-TBC` goes from module H to
[module C](../modules/c-video-processor/index.md). There:

1. Selection between the internal video and the composite sync `CS-REF` from
   reference source module D — among other things for sync during mute.
2. Selection between that and the externally supplied composite video `CV-EXT`
   coming from module U.
3. Black level clamping, and the index insert if wanted: `VOBN` provides an
   index background and `VOW` inserts the index information at white level.
4. A sync separator generates the line-frequency sandcastle signal `SC`, which
   with `VBL` also acquires its frame-frequency component.
5. The video is buffered along two paths: one CVBS signal to
   [module B](../modules/b-rgb/index.md), and one stripped of the special burst
   — `CVBS2` — to module U.

**Out of module U.** The DC level of `CVBS2` is restored and it goes as
`TXT CVBS` to the TXT section. A selection is possible between the external
`CVBS IN` and `TXT CVBS`, made by the switching signal `CV-E/I`. The output of
that switch reaches manual switch **SK2** and leaves as `CVBS OUT` on a
rear-panel BNC.

!!! info "What switch SK2 actually chooses"

    SK2 selects **not encoded** or **encoded** video.

    The internal composite signal `CVBS2` comes straight off the disc, and as
    such is *not* suitable for a monitor when the special playing modes are
    used. The encoded CVBS *is* suitable for a monitor, but has a limited
    bandwidth of 3 MHz.

    SK2 is hidden inside the player, on module U — see
    [remarks](../general-service/remarks.md), section 4. Chart ① of
    [fault-finding](../repair/fault-finding.md#chart-1-no-display) has you
    operate it.

**RGB.** The CVBS signal from module C — the one that still has the special
burst — is decoded on module B into RGB at full bandwidth. The CVBS is split
into luminance and chrominance; the chroma is decoded into the colour
difference signals R−Y and B−Y, and together with the luminance `LUM` is
encoded into CVBS on module U. The R, G and B signals come from the RGB matrix
on module B and go, via module U, to
[video mixer module Y](../modules/y-video-mixer/index.md) in the sandwich
section of the VP415.

On module Y they may be mixed with the RGB signals of an externally connected
computer, the mode of mixing set by `VP0`, `VP1` and `VP2`. The outgoing RGB
goes to the Euroconnector via module U — **full bandwidth, 5 MHz**, against the
3 MHz of the encoded CVBS.

<figure class="sheet" markdown>
[![VP400 series: introduction, the characteristics of the disc drive generation, and the audio/video signal path described module by module](assets/web/text-p132-preview.webp)](assets/web/text-p132-zoom.webp)
<figcaption>
  VP400 series — introduction, audio/video signal path.
  <span class="src">service manual page 132</span>
</figcaption>
</figure>

<figure class="sheet sheet--fold" markdown>
[![Fig. SP1, block diagram of the audio and video signal path: the deck electronics HF output through HF processing, video drop-out correction, electronic timebase correction, audio and video processing, RGB decoding, the video mixer and analog I/O to the outputs](assets/web/cs-7-581-figure-p133-preview.webp)](assets/web/cs-7-581-figure-p133-zoom.webp)
<figcaption>
  Fig. SP1 — audio/video signal path.
  <span class="cs">CS 7 581</span>
  <span class="src">service manual page 133</span>
</figcaption>
</figure>

## Control routes

The control and drive section is determined by two modules:
[control processor module S](../modules/s-control/index.md) and
[drive processor module R](../modules/r-drive-processor/index.md). They
communicate over the **S-bus**. See Fig. CR1.

### The control processor

Module S is the one that talks to the outside world:

- A communication similar to the RS232 bus — the **RS232-2 bus** — with the
  sandwich part of the drive,
  [CPU and data grabber module W](../modules/w-cpu-data-grabber/index.md), and
  so through the SCSI connector to an external computer.
- The **RS232-1 bus**: the rear-panel RS232 connector is connected directly to
  module S.
- Remote control communication (RC5): infrared, wired, and SCART RC5 commands.
- The LEDs on [display + keyboard module N](../modules/n-display-keyboard/index.md),
  driven over `DLEN`, `SDAT` and `SCLT`.
- Signals `VP0`, `VP1` and `VP2` for the video mixing modes realised on
  [video mixer module Y](../modules/y-video-mixer/index.md) in the sandwich.

The `NPL` signal is not used.

### The drive processor

Module R has eight main tasks:

| | Task | Notes |
| --- | --- | --- |
| a | Accept and interpret commands from module S | Over the S-bus |
| b | Radial tracking and access | Uses `SP-POS` and `CL-RAD` from [radial module M](../modules/m-radial/index.md). During start-up the voltage on the radial mirror is studied, and the slide displaced from the actual mirror position if conditions require |
| c | Manchester code reading | Picture numbers, chapter code, stop code and CLV code, read from the video. Uses `VMANCH`, `HMANCH` and `CL-VID` from [ETBC-C module I](../modules/i-etbc-c/index.md) |
| d | Display on screen drive | A character generator on module R, synchronised to the video, inserts the index background `VOBN` and index information `VOW` on module C |
| e | Start-up sequence of the disc drive | See below |
| f | Local control: stand-by and eject | The two front-panel keys pass their commands directly to module R via module N |
| g | Audio and video switching | Including muting the signals during search actions |
| h | Service diagnostics | The [diagnostic software](../repair/diagnostic-mode.md), integrated into the drive software |

### Start-up sequence

Module R runs and checks the start-up procedure. Once a disc is on the tray and
the tray pushed in, and provided the drive is in stand-by, the sequence is
triggered. It is drawn as timing diagrams in **Fig. CR2**, and the numbered
steps appear again on the control-routes block diagram Fig. CR1, so that you can
see the order in which module R energises each module.

| # | Step | Command signal | Confirmed by |
| --- | --- | --- | --- |
| 1 | Tray pushed in | `ST-ST` (start-stop) | — |
| 2 | Pull in the front loader | `LMOT-L` (2a) | `TI`, tray inside (2b) |
| 3 | Bring the slide to its initial position | `SL-PWR` (3a), `COMM-1.2.3.4` (3b) | `SPI`, slide position indication (3c) |
| 4 | Detect a disc, by photo-sensor | — | `DR`, disc reflection (4) |
| 5 | Activate the tilt control | `TLS` (5a) | `TILTOK` (5b) |
| 6 | Switch the laser on | `LA` (6a) | `LA-STA`, laser status (6b) |
| 7 | Activate the focus control | `FOC-EN` (7a) | The deck electronics, module Z, give `FPI` — focus position indication (7b) — to [focus module J](../modules/j-focus/index.md); `FPI` together with the zero crossing of `FOC-ER` (7c) produces `FOC-IND`, focus indication (7d), for module R |
| 8 | Bring the turntable motor to speed | `TTM` (8a) | `0-RPM` (8b) |
| 9 | Close the radial tracking loop | `RLS`, radial loop switch (9) | — |
| 10 | Lock the motor to the read-out video | — | `M-LOCK` (10), to timebase correction module I |
| 11 | Lock the disc video sync to reference source module D | — | `FRLOCK`, frame lock (11) |
| 12 | Timebase correction becomes active | — | `TANGER`, tangential error (12), from module I to module H |
| 13 | Read the lead-in code, and give course pulses to radial module M up to picture 1 | `HMANCH`, `VMANCH`, `CL-VID` | `RAD-ER`, radial error (13) |
| 14 | Put the disc video on the outputs — until now a sync signal derived from module D has been present on every video and sync output | `CV/CS` (14) | A locked picture with colour on a connected monitor |
| 15 | Switch the audio lines over | `AUD1ON`, `AUD2ON` (15) | The audio LEDs light, as does the CAV or CLV LED |

**This sequence is the same one the [fault-finding
charts](../repair/fault-finding.md#chart-2-error-code-60-self-test-mode) walk
through**, and the confirmations in the right-hand column are exactly the tests
whose failure raises error codes 1 to 9.

<figure class="sheet sheet--fold" markdown>
[![Fig. CR1, block diagram of the control routes: the control processor and drive processor linked by the S-bus, with the RS232 interfaces, the remote control paths, the display and keyboard, the sandwich CPU and SCSI, and the numbered start-up steps marked against each module](assets/web/cs-7-882-figure-p134-preview.webp)](assets/web/cs-7-882-figure-p134-zoom.webp)
<figcaption>
  Fig. CR1 — block diagram, control routes.
  <span class="cs">CS 7 882</span>
  <span class="src">service manual page 134</span>
</figcaption>
</figure>

<figure class="sheet" markdown>
[![Fig. CR2, start-up sequence: timing diagrams showing the fifteen numbered steps of the start-up procedure and the command and confirmation signal for each](assets/web/figure-p135-preview.webp)](assets/web/figure-p135-zoom.webp)
<figcaption>
  Fig. CR2 — start-up sequence.
  <span class="src">service manual page 135</span>
</figcaption>
</figure>

## The S-bus

In the VP415, communication between control module S and drive processor module
R is over the **S-bus**: a synchronous communication link intended for use
between a LaserVision drive and a host controller. The bus is bi-directional
with handshake, and byte serial.

### The window

Bus activity is not continuous. It is confined to a **window occurring in each
video field: 8 ms out of each 20 ms field period.** Communications may not
extend beyond the limits of the window, and execution of commands commences
after the window terminates.

Commands are allocated a priority order:

| Priority | Rule |
| --- | --- |
| 1 | More than one command may be sent during a window, but only the last one accepted will be executed |
| 2 | As priority 1, but if a priority 1 command is included, the priority 2 command is ignored |
| 3 | These commands will always be executed |

### Constraints on operation

For the S-bus to operate, **the video from the disc must be locked to either the
internal or an external reference in both line and field, and the Manchester
codes must be readable.** A player that cannot lock cannot be talked to.

### Command and response structure

Data is organised as packets, each a three-byte string. A command from the
controller to the drive processor module is **one packet**. Responses may be 0
to 5 packets; the length is set by a command from the controller of the form
`- 05 00 0x`, where x is the number of packets required. In the VP415 the
initialising sequence calls for **4 packets**.

By way of example, the contents of the packets are:

| Packet | Byte | Contents |
| --- | --- | --- |
| 1 | — | Manchester code from line 18 |
| 2 | 1 | Disc loaded — CAV/CLV |
| 2 | 2 | Player mode |
| 2 | 3 | Error status |
| 3 | — | Manchester code from line 16 |
| 4 | 1 | LaserVision deck status |
| 4 | 2 | Audio/video status |
| 4 | 3 | Miscellaneous status |
| 5 | — | Manchester code from line 17, if requested |

For the packets containing Manchester code information, **all zeros are returned
if the Manchester codes are not readable**.

### S-bus signals

| Signal | Direction | Meaning |
| --- | --- | --- |
| `SD0-7` | Bidirectional | Databus; `SD7` is MSB |
| `WREN` | To the drive | Write enable — write data to drive |
| `RDEN` | To the drive | Read enable — read data from drive |
| `DAK` | From the drive | Data acknowledge — data has been read by the drive |
| `DAV` | From the drive | Data available |
| `WINDOW` | From the drive | Drive can communicate |

`WREN`, `RDEN` and `DAV` are printed with an overbar in the manual: they are
active low.

<figure class="sheet sheet--fold" markdown>
[![Control routes, the S-bus and constraints on operation: the tasks of the control and drive processors, the fifteen-step start-up sequence, the S-bus window and priorities, the packet structure and the S-bus signal list](assets/web/cs-7-883-text-p136-preview.webp)](assets/web/cs-7-883-text-p136-zoom.webp)
<figcaption>
  Control routes / S-bus / constraints on operation.
  <span class="cs">CS 7 883</span>
  <span class="src">service manual page 136</span>
</figcaption>
</figure>

## The servo block diagram

Fig. SE1 surveys every module needed for correct functioning of the optical
deck:

- [Deck electronics Z](../modules/z-deck-electronics/index.md)
- [Focus module J](../modules/j-focus/index.md)
- [Radial drive module M](../modules/m-radial/index.md)
- [Drive processor R](../modules/r-drive-processor/index.md)
- [Slide motor drive E](../modules/e-slide-drive/index.md)
- [Motor + sequence module F](../modules/f-motor-sequence/index.md)
- [Genlock module G](../modules/g-genlock/index.md)

### Focus

From the laser source a beam is projected onto photodiodes A–D and R1–R2 in the
optical unit, converted to electrical signals, and applied to the servo
preamplifier and the radial amplifier.

From the servo preamplifier, `FPI` (objective focussed) and the focus error
signal are fed to focus drive module J via **8Z4–2J1** and **9Z4–1J1**. Module J
generates the focus drive signal `FOC-ACT` and feeds it back to the objective
via **5J1–3Z4**. The module only operates when the focus enable signal
`FOC-EN`, arriving via **22aR2–7J1** from the drive processor, is high. When the
objective is focussed, `FOC-IND` goes low and is fed via **6J1–21aR2** back to
the drive processor.

### Radial

From the radial part of the servo preamplifier, `RAD-ER` is applied to radial
drive module M via **7Z4–2M2**, and the tracking position indication `TPI` via
**6Z4–3M2**. The radial drive output `RAD-ACT`, fed via **6M2–2Z4** to the deck,
controls the radial mirror. The radial module only operates when the radial
loop switch `RLS` from the drive processor is low.

For jumps over one or more tracks, `CP1` or `CP2` goes low from the drive
processor via **26aR2–7M1** or **27aR2–8M1**, and at the same time the clipped
radial signal `CL-RAD` is fed back to the drive processor.

### Turntable motor and slide

The drive processor starts the turntable motor with `TTM`, fed via **22cR1–1F1**
to motor and sequence module F; when the motor runs, a `2PPR` — two pulses per
revolution — signal comes back via **4F1–23cR1**.

The drive processor also controls the slide position. Its output expander feeds
four commutating signals via **12aR1–15aR1** to **5E1–2E1**, and a slide power
signal `SL-PWR` via **16aR1–1E1**, to slide motor drive module E. Module E
converts the commutating signals into drive signals for the slide motor and
supplies them to the deck via plugs **1E2–6E2**.

### Motor control: three regimes

Module F drives the turntable motor, and which control regime it uses depends on
the conditions.

1. **Acceleration.** `TTM` is high and goes to the start/stop sequence block,
   which also takes information from the Hall elements in the motor via plugs
   **2–11F3** and the comparator block. Only `TTM` operates; via the motor
   control block it is converted into a pulse-width modulated signal `PWM` with
   a minimum duty cycle. `PWM` controls the commutation block, which supplies
   six drive voltages to the three output stages in the motor drive block; those
   connect to the motor via plug **5–7F1**.
2. **Frequency control.** At 1500 rpm the acceleration is stopped by the D/A
   converter and control is taken over by `LPWM`, a frequency control signal
   from the line speed measurement block. That block measures the line frequency
   of the video on the disc using `LPO` pulses supplied by the genlock module
   via **9G1–4F2**.
3. **Phase control.** Shortly after, once the speed is within 5% of correct, the
   sequence circuit switches to phase control: it delivers the motor control
   enable signal `MCO-EN`, and the 15 625 Hz duty-cycle-controlled `MCO` signal
   is supplied to the motor control block via the genlock module and plug
   **8G1–5F2**.

Control switches **back** to frequency control for search mode on a CLV disc:
the `CLV-TC` signal from the drive processor, via **22aR1–2F1** to the sequence
circuit, goes high.

If focus is lost during a search, the drive processor delivers `MEM-SU` via
**22cR1–5F1**, which activates a memory in the tacho circuit so that the last
motor speed is stored. As soon as focus is correct again the motor speeds back
up to the original velocity.

<figure class="sheet sheet--fold" markdown>
[![Fig. SE1, block diagram of the servo system: the optical unit photodiodes feeding the servo preamplifier and radial amplifier, the focus and radial drive modules, the slide motor drive, the motor and sequence module with its commutation and motor control blocks, and the genlock module, with every interconnecting plug and pin marked](assets/web/cs-8-123-figure-p137-preview.webp)](assets/web/cs-8-123-figure-p137-zoom.webp)
<figcaption>
  Fig. SE1 — block diagram, servo.
  <span class="cs">CS 8 123</span>
  <span class="src">service manual page 137</span>
</figcaption>
</figure>

<figure class="sheet" markdown>
[![The servo block diagram: a short description naming every module involved and tracing the focus, radial, slide and motor control paths with their connector references](assets/web/cs-7-884-text-p138-preview.webp)](assets/web/cs-7-884-text-p138-zoom.webp)
<figcaption>
  The servo block diagram — short description.
  <span class="cs">CS 7 884</span>
  <span class="src">service manual page 138</span>
</figcaption>
</figure>
