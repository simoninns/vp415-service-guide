---
title: Introduction
description: >-
  Section 1 of the user manual: what the LaserVision system is, the three disc
  types, interactive use, and the features that make the VP415 what it is.
---

# Introduction

Section 1 of the operating instructions, pages 4 to 6. What LaserVision is,
what the three kinds of disc do, what interactive use means — and the nine
features Philips thought worth listing.

## Introduction

The VP415 LaserVision player (ROM disc drive) is primarily designed for use in
interactive computer-controlled systems that exploit the capabilities of
LaserVision as a versatile, high-quality storage and retrieval medium.
Communication between the VP415 and a controlling computer is via standard
RS232-C or SCSI interfaces, **both of which are fitted to the player**. The
player can be used with ordinary LaserVision discs containing audiovisual
information, or LV-ROM discs, which contain data as well as audiovisual
information. This data takes the place of the audio channel on some or all
sections of the disc.

The VP415 can of course be used for direct playback of LaserVision CAV (active
play) or CLV (long play) discs. In this respect it has extensive program
control, with search and memory facilities, conveniently operated from the
remote control handset.

## The LaserVision system

LaserVision is the only audiovisual playback system using optical (laser beam)
readout. The laser beam, concentrated to an almost inconceivably fine point —
*60 times finer than a gramophone stylus* — reads very densely-packed
information under the transparent surface of the LaserVision disc.

The picture reproduced is of high quality with 2-channel mono or stereo sound.
There is no wear to the disc or 'pick-up', and the discs are extremely
resistant to scratches, dust and fingerprints.

### Types of LaserVision disc

Three types of disc are available and the player will operate with any of them:

| Type | Speed | Capacity | Plays |
| --- | --- | --- | --- |
| **CAV** (active play) | Constant 1500 r.p.m. | 54 000 pictures per side — 36 minutes at 25 pictures per second | Still, slow motion, reverse, fast forward, fast reverse, goto picture or chapter number |
| **CLV** (long play) | Decreases gradually as the disc plays | 1 hour per side | Continuous forward play only, with time and chapter search |
| **LV-ROM** | A CAV disc | 324 Mbytes of user data **and** 54 000 pictures | As CAV, with data replacing some or all of the audio track |

### Interactive use

The VP415 allows all the facilities of the LaserVision system to be controlled
by a computer: the picture, the sound and the LV-ROM data. Play is controlled
by picture numbers, chapter numbers, autostops or a computer program, and the
program can be activated from the VP415 remote control handset, the computer
keyboard, or another computer peripheral.

Communication with the VP415 is achieved using either a special code known as
**F-code**, or **LV-DOS commands** via the SCSI interface.

- The [F-code](f-code-commands.md) instruction set enables commands to be sent
  as ASCII characters to the player, some of them causing responses to be
  returned to the computer. Using F-code commands, a VP415 can participate in
  an interactive program with any computer system loaded with the necessary
  program.
- [LV-DOS commands](scsi-operation.md) allow the VP415 to be used as an LV-ROM
  memory device in a computer system. Both data retrieval from disc and player
  control are possible.

## Features of the VP415

### RGB output / PAL-RGB decoder

The VP415 allows the best possible picture quality to be obtained from a
LaserVision disc, by employing a built-in PAL-RGB decoder. Within the
LaserVision format, video information is stored on the disc in PAL encoded
form. This can cause problems when the disc is played in still frame or slow
motion, or any other non-standard playing mode, because the PAL 8-field
sequence becomes destroyed. In order to correct this sequence such that a
monitor can understand it and reproduce correct colour, many players
incorporate a *PAL modifier*. This piece of circuitry corrects the PAL
sequence, but in doing so reduces the video bandwidth and introduces other
unwanted effects — echoes, for instance.

The VP415 tackles this problem by employing a fast-locking PAL-RGB decoder.
Having this device built in allows its characteristics to be fully optimised to
give the highest possible picture quality from the disc, even in non-standard
playing modes.

The result is an RGB output giving the **full 5 MHz video bandwidth in all
playing modes**. The benefit is particularly valuable when viewing video
material such as maps with fine text. RGB output also lends itself to simpler
mixing with computer graphic output — also RGB — in external equipment if
required.

!!! info "That decoder is module B"

    The fast-locking PAL-RGB decoder described here is
    [module B](../modules/b-rgb/index.md) in the service manual; the RGB-PAL
    encoder below is on [analog I/O module Ub](../modules/u-analog-io/index.md),
    and the mixer is [module Y](../modules/y-video-mixer/index.md).

### Sync pulse generator

The VP415 contains an internal sync pulse generator (SPG) which may either
free-run, or in the presence of a suitable reference signal, lock itself to the
external reference — genlock.

The SPG provides freshly-generated line and field sync pulses at the player's
video output at all times. Following the decoding process from PAL to RGB, fresh
sync pulses are inserted into the RGB signal, which is available at the
Euroconnector socket. A stable output from the player is therefore guaranteed
at all times.

### Genlock

Genlock allows the field and line sync pulses from the player output to be
synchronised with an external reference signal. It ensures correct overlay of
video signals and can also prevent picture jump or roll. The reference signal,
comprising line and field syncs (negative-going), should be applied to either
of the two `SYNC IN` sockets, or to pin 4 of the `RGB (TTL) IN` socket. A
horizontal shift of the overlay picture is achieved by adjusting the `H-SHIFT`
control at the rear of the player.

!!! note "Locking takes a moment"

    The player may take up to **2 seconds** initially to lock to a reference
    signal. The service manual is more precise, and less optimistic: the
    internal generator takes up to 7 s to lock to the external signal and the
    disc up to 3 s to lock to the generator — see
    [module G](../modules/g-genlock/index.md).

### CVBS output / RGB-PAL encoder

The VP415 contains an RGB-PAL encoder. This takes the RGB output from the
player, prior to the video mixing stage, and encodes it into a CVBS signal
using fresh sync pulses from the internal SPG. The signal available at the CVBS
output is thus totally stable. It does however have a reduced bandwidth in all
playing modes — approximately **3 MHz**.

### Electronic timebase corrector

A CCD (charge coupled device) timebase corrector is employed to provide
correction of timing errors always present in the signal read from the video
disc. This replaces the more traditional tangential mirror — a mechanical
method — allowing for a smaller, lighter optical system. This reduction in mass
allows the optical readout unit to track the disc faster and thus reduces
picture access time.

!!! info "The timebase corrector is three modules"

    `ETBC` is split across [module H](../modules/h-etbc-b/index.md),
    [module I](../modules/i-etbc-c/index.md) and the CCD delay line, and the
    optical system it made lighter is the
    [optical deck](../circuit-description/optical-deck.md).

### Video mixing

The VP415 has a built-in video mixer which is able to mix either the RGB signal
derived from the video disc — via the PAL-RGB decoder — or an RGB signal
derived from an external video signal connected to one of the `CVBS IN`
sockets, with an external TTL RGB signal from the `RGB (TTL) IN` socket.

This facility allows the TTL RGB graphics output of an external computer to be
mixed with the off-disc video, or external video, in a number of ways. The
mixed video is available at the Euroconnector socket:

| Mode | What it does | Player | Computer |
| --- | --- | --- | --- |
| **1** | Player RGB only | — | — |
| **2** | Computer RGB only | — | — |
| **3** | Key mode | 100% intensity | 100% intensity |
| **4** | Mixed mode — transparent graphics | 62% intensity | 38% intensity |
| **5** | Enhanced video — 'highlighting'. The presence of graphics produces 100% intensity video at that point; elsewhere video is reduced | 100% where there are graphics, 57% where there are none | — |

When mixing in this manner, the VP415 genlocks to the composite sync signal
from the external computer. The mode is selected with the
[`VPy` F-code](../reference/f-codes.md).

### Instant jump

The VP415 also incorporates an *instant jump* feature. Essentially this means
that the radial mirror which points the laser beam at the required disc track
can be made to 'twitch' and therefore jump a predetermined number of tracks —
**maximum 50** — in either direction during the vertical interval, the field
flyback time. Small jumps are invisible, as they can be performed within the
video blanking. This gives the effect of an instant search to the required
picture, almost as if it were immediately adjacent to the current picture.

This feature is valuable in, for example, map-walking, where each picture
contains a map of an area and each successive picture shows adjacent areas. The
user can scan across map boundaries with no black picture between maps while
the player searches for the next picture.

It is also possible to interleave programmes on the disc such that by playing
the disc and missing out — jumping over — every alternate picture, one
particular storyline is followed; and then by offsetting this process by one
picture, another storyline is immediately accessed and followed.

It must be realised that following a jump, the optical slide requires a finite
time to catch up and centralise the radial mirror. A limit is therefore imposed
on how many jumps may be made in a given time. **The limit occurs when the
effective playing speed of the disc exceeds 20 times normal speed** — that is,
it is possible to jump 20 tracks, display for a period of 1 picture, then jump
another 20 tracks and so on continuously, without the optical slide falling
behind.

Details of the types of jump possible, and their associated commands, are in
the [F-code command list](../reference/f-codes.md).

### Fast random access

The VP415 features a very fast random access time: the time needed for the
optical readout unit to move from one point on the disc to another, which may
be anywhere on the disc. Figures are typically **1 s for a CAV disc and 5 s for
a CLV disc**.

### Wired remote control

In some applications it may be required to hide the VP415. In such cases the
infra-red beam of the remote control handset may not be able to operate. For
reliable working under such conditions, the wired connection should be used
between the remote control handset and the `WIRED RC` socket at the rear of the
player.

## The printed pages

<figure class="sheet" markdown>
[![Section 1 divider page listing the contents of the introduction, features, installation, and controls and connections sections with their page numbers](assets/web/operating-instructions-scan-03-b-preview.webp)](assets/web/operating-instructions-scan-03-b-zoom.webp)
<figcaption>
  Section 1 divider and contents.
  <span class="src">operating instructions page 4</span>
</figcaption>
</figure>

<figure class="sheet" markdown>
[![Page of the introduction covering the LaserVision system, the three disc types, interactive use, and the first five features of the VP415](assets/web/operating-instructions-scan-04-b-preview.webp)](assets/web/operating-instructions-scan-04-b-zoom.webp)
<figcaption>
  Introduction, the LaserVision system and the first features.
  <span class="src">operating instructions page 5</span>
</figcaption>
</figure>

<figure class="sheet" markdown>
[![Page covering video mixing with its five modes, instant jump, fast random access and wired remote control](assets/web/operating-instructions-scan-04-a-preview.webp)](assets/web/operating-instructions-scan-04-a-zoom.webp)
<figcaption>
  Video mixing, instant jump, fast random access, wired remote control.
  <span class="src">operating instructions page 6</span>
</figcaption>
</figure>

## Related

- [Installation](installation.md) — the rest of section 1
- [Technical data](technical-data.md) — the numbers behind these features
- [Circuit description](../circuit-description/index.md) — the service
  manual's account of how the same features are built
