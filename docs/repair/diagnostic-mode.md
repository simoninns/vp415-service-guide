---
title: Diagnostic mode
description: >-
  How to start the VP415's built-in diagnostic software in check mode or
  self-test mode, and how to read what it puts on the screen.
---

# The diagnostic software

The VP415 tests itself. The diagnostic software is not a separate program: it
is built into the drive software on
[drive processor module R](../modules/r-drive-processor/index.md), and it
checks the drive's own tasks as they run. When a task fails, an error code
appears on the picture as a video overlay.

This is the single most useful thing in the manual, and everything in
[fault-finding](fault-finding.md) starts from a code it produced.

!!! important "You need a monitor"

    The codes appear as **video overlay on the picture screen** — not on the
    front panel. Connect a monitor to the CVBS or SCART output before you start.

## Starting it

There are two modes, and each is entered by holding front-panel keys while the
**mains switch at the rear** is switched on.

=== "Check mode"

    **Hold STAND-BY while switching the mains on.** Do not release the STAND-BY
    key until three horizontal stripes are visible in the bottom right corner of
    the picture.

    The player then works normally — manually or under computer control — and
    shows the error code of the last detected fault in the bottom right corner.

=== "Self-test mode"

    **Hold both EJECT and STAND-BY while switching the mains on.** Do not
    release either key until the word `DIAGNOSTICS` appears on the screen.

    The drive now runs a programme loop of its own and the normal operating
    functions are inoperative. The screen shows the drive mode, the diagnostic
    mode, the loop counter, the number of faults registered, and two error
    codes.

Both modes are cleared by switching the mains off. **Switch the set off only
when it is in STAND-BY.**

## Reading the screen

### Check mode

Three numbers appear. Only the one in the bottom right corner is the error
code; the others are not relevant. `- - -` means no fault — the initial value,
255.

### Self-test mode

| Line | Meaning |
| --- | --- |
| `PLAY FWD` | Drive mode |
| `PNR5542` | Picture number |
| Arrow symbol at the left of `DIAGNOSTICS` | Diagnostic mode — see below |
| `DIAGNOSTICS` | Confirms the set is in self-test mode |
| `LOOP COUNTER 001` | Number of completed test loops |
| `NR OF FAULTS 000` | Number of registered faults |
| `MAJOR FAULT 081` | Error code of the most serious fault so far |
| `ACTUAL FAULT 096` | Error code of the last detected fault |

The diagnostic-mode symbol beside `DIAGNOSTICS` is one of five:

| Symbol | Meaning |
| --- | --- |
| ↑ | Stand by |
| → | Start up |
| ↓ | Normal operation |
| ← | Unload |
| ✳ | Error detected (error code < 60) |

**Major fault against actual fault.** The major-fault code is overwritten only
by a code with *higher priority* — that is, a *lower* number. So `MAJOR FAULT`
is the worst thing that has happened since the mode was entered, and
`ACTUAL FAULT` is the most recent. Look up both in
[meaning of the error codes](error-codes.md).

<figure class="sheet" markdown>
[![Reproducing the error codes on the screen: a drawing of the check-mode display with the error code in the bottom right corner, and of the self-test display showing drive mode, picture number, DIAGNOSTICS, loop counter, number of faults, major fault and actual fault, with the five diagnostic-mode symbols](assets/web/cs-8-112-text-p109-preview.webp)](assets/web/cs-8-112-text-p109-zoom.webp)
<figcaption>
  Reproducing the error codes on the screen.
  <span class="cs">CS 8 112</span>
  <span class="src">service manual page 109</span>
</figcaption>
</figure>

## What the self-test loop does

One pass of the programme loop, from the flow chart:

1. Stand by
2. Load 12" disc
3. Start up
4. Play forward
5. Move slide for 2 seconds
6. Play forward
7. Search until lead-out
8. Unload
9. Stand by — then increase the loop counter, update the fault display, and go
   back to **start up** (step 3), not to the load step

Any step can raise an error. A fault with a code **below 60** breaks out of the
loop and puts the drive into STAND-BY, keeping the last LDU slide position; a
code of 60 or above is recorded and the loop carries on.

<figure class="sheet" markdown>
[![Flow chart of the self-test programme loop: press mains plus eject plus standby, then stand by, load 12-inch disc, start up, play forward, move slide 2 seconds, play forward, search until lead out, unload, stand by, with every step branching out to an error-below-60 exit that returns the drive to stand by](assets/web/cs-8-113-text-p110-preview.webp)](assets/web/cs-8-113-text-p110-zoom.webp)
<figcaption>
  Programme loop in the self-test mode.
  <span class="cs">CS 8 113</span>
  <span class="src">service manual page 110</span>
</figcaption>
</figure>

## Introduction and set-up, as the manual has it

The object of the repair method is to facilitate fault-finding in a defective
set. Fault diagnosis is made via a test procedure in which operations are
carried out in sequence and yes/no decisions taken at various points, leading
the technician to a defective module or a part of it. A central role is played
by the diagnostic software implemented in the drive processor.

Because drive processor module R controls the various functions in the set, the
diagnostic software forms an integral part of the drive software of that
module, and many of the drive's tasks are checked for proper performance as
they run.

<figure class="sheet" markdown>
[![Repair method: introduction and the diagnostic software — set-up, the error code priority rule, and switching on check mode and self-test mode](assets/web/cs-8-111-text-p108-preview.webp)](assets/web/cs-8-111-text-p108-zoom.webp)
<figcaption>
  Introduction / diagnostic software.
  <span class="cs">CS 8 111</span>
  <span class="src">service manual page 108</span>
</figcaption>
</figure>
