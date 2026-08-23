---
title: Controls and connections
description: >-
  Section 1 of the user manual: every control, indicator and socket on the
  VP415, front and rear, keyed to Fig. 1.
---

# Controls, indicators and connections

Page 9 of the operating instructions, and Fig. 1 on pages 2 and 3 that it
refers to throughout. Everything you can press, switch or plug into a VP415.

## Front of the player

| Control | What it does |
| --- | --- |
| `EJECT` button | Opens the disc-tray, ejecting a disc if one is loaded |
| `ON/STANDBY` button | Switches between standby and on. **It also effects a CPU reset** |

Ten indicators sit beside them:

| Indicator | Colour | Lights when |
| --- | --- | --- |
| `STANDBY` | Red | In standby mode — and **flashes during start-up** |
| `EJECT` | Green | Flashes during eject |
| `PAUSE` | Green | In pause |
| `REPLAY` | Green | The replay function is active |
| `REPEAT` | Green | The repeat function is active |
| `AUDIO 1` | Green | Audio channel 1 is enabled |
| `AUDIO 2` | Green | Audio channel 2 is enabled |
| `CAV` | Green | Playing a CAV disc |
| `CLV` | Green | Playing a CLV disc |
| `REMOTE CONTROL` | Green | Flashes to confirm the player is receiving a remote control command |

!!! tip "Those indicators are a diagnostic tool"

    A `STANDBY` light that flashes and never goes out is a start-up that never
    finished, which is the symptom the whole of
    [fault-finding chart 2](../repair/fault-finding.md) exists for. The
    lamps themselves are driven from
    [module N](../modules/n-display-keyboard/index.md).

## Rear of the player

The numbers are the callouts on Fig. 1.

| № | Control or socket | What it is for |
| --- | --- | --- |
| 1 | `ON/OFF` switch | Primary mains power switch |
| 2 | `MAINS` lead socket | Connection of the mains lead |
| 3 | `REPLAY` on/off switch | Switches the replay function on or off — see [replay](special-play-functions.md#replay) |
| 4 | `RC IR/EURO` switch | Whether remote control commands are received directly by the VP415 (`IR`) or through the monitor (`EURO`) |
| 5 | `WIRED RC` socket | Wired connection of the remote handset, for when the player is hidden from view |
| 6 | `RS232C` socket | Serial connection for an external computer |
| 7 | `BAUD RATE` dip switches | Baud rate for RS232-C — see [F-code programming](f-code-programming.md) |
| 8 | `AUDIO IN` (1 and 2) | External stereo or 2-channel sound source. **Audio L = audio 1, audio R = audio 2** |
| 9 | `AUDIO OUT` (1 and 2) | Output to an amplifier or monitor, same channel convention |
| 10 | `A/V EUROCONNECTOR` | The full set of monitor inputs and outputs — pinning in [technical data](technical-data.md) |
| 11 | `H-SHIFT` control | Shifts the horizontal position of the picture when an external sync signal is used — see [genlock](introduction.md#genlock) |
| 12 | `CVBS OUT` socket | Composite video output for a monitor |
| 13 | `SYNC OUT` socket | Synchronising signal for the host computer or a second VP415 in parallel |
| 14 | `CVBS IN` sockets | External video input, two sockets internally connected |
| 15 | `SYNC IN` sockets | External sync input, two sockets internally connected |
| 16 | `RGB (TTL) IN` socket | DIN socket for video and sync from an external computer |
| 17 | `SCSI address` dip switches | The player's address on the SCSI bus — see [SCSI operation](scsi-operation.md) |
| 18 | `SCSI` socket | Connection to an external computer to SCSI standards |

### The looped-through pairs

`CVBS IN` and `SYNC IN` are each **two sockets wired together inside the
player**, so a signal can be looped on to other equipment through the second
socket.

!!! important "Terminate the second socket"

    If no loop-through is used, the second socket of the pair **must be
    properly terminated with a 75 Ω plug**. This applies to both pairs.

    To lock the CVBS signal to an external RGB signal for mixing, loop `CVBS IN`
    through to one of the `SYNC IN` sockets.

    The reference signal must conform to broadcast standards in pulse shape and
    timing; a standard CVBS signal is suitable.

## The printed pages

<figure class="sheet" markdown>
[![Fig. 1: line drawings of the VP415 front panel, rear panel with eighteen numbered callouts, and the remote control handset](assets/web/operating-instructions-scan-02-a-preview.webp)](assets/web/operating-instructions-scan-02-a-zoom.webp)
<figcaption>
  Fig. 1 — the player, front and rear, and the handset, with the callout
  numbers used throughout the manual.
  <span class="src">operating instructions page 2</span>
</figcaption>
</figure>

<figure class="sheet" markdown>
[![Key to Fig. 1: the front panel button and indicator names, and the eighteen numbered rear panel items from the ON/OFF switch to the SCSI socket](assets/web/operating-instructions-scan-02-b-preview.webp)](assets/web/operating-instructions-scan-02-b-zoom.webp)
<figcaption>
  The key to Fig. 1.
  <span class="src">operating instructions page 3</span>
</figcaption>
</figure>

<figure class="sheet" markdown>
[![Page describing the controls on the front and rear of the player, the ten front-panel indicators, and every rear-panel connection](assets/web/operating-instructions-scan-06-b-preview.webp)](assets/web/operating-instructions-scan-06-b-zoom.webp)
<figcaption>
  Controls, indicators and connections.
  <span class="src">operating instructions page 9</span>
</figcaption>
</figure>

## Related

- [Technical data](technical-data.md) — the pinning of the Euroconnector, the
  RGB (TTL) IN socket, the RS232-C interface and the SCSI interface
- [Controls and connections](../overview/controls-and-connections.md) — the
  service manual's own version, with the same panels photographed
- [Connector pinning](../overview/connector-pinning.md) — every internal and
  external connector in the player
- [Module U — Analog I/O](../modules/u-analog-io/index.md) — the board most of
  these sockets land on
