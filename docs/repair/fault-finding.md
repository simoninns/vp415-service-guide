---
title: Fault-finding charts
description: >-
  The manual's test procedure and fault-finding trees, transcribed as tables:
  which signal fails, which error code it raises, and which module to check.
search:
  boost: 2
---

# Fault-finding

Two flow charts and the procedure that leads into them, printed across five
sheets: a top-level test procedure, chart ① for a player that shows nothing,
and chart ② — three sheets of it — for a start-up that stops with a code below
60. Each chart ends by naming a module: that is the answer it is trying to give
you.

Everything here assumes the player is in
[self-test mode](diagnostic-mode.md) with a monitor connected, and that you
have the [error code](error-codes.md) it is displaying.

## Meaning of the symbols used

| Symbol on the chart | Meaning |
| --- | --- |
| Rectangle | An action or operation to be carried out |
| Diamond | A decision — follow the `Y` or `N` branch |
| Boxed letter, e.g. `T` | Check that module, or the circuits on it |
| Circled number, e.g. ① | Go on to that block in the fault-finding tree |
| Three-cell box, e.g. `0 0 7` | The error code on the picture screen; no error is `- - -` |
| Mains + STANDBY + EJECT symbol | Switch on the drive by pressing STANDBY and EJECT together with the mains switch; release when `DIAGNOSTICS` is displayed |

<figure class="sheet" markdown>
[![Fault finding: the meaning of the symbols used in the test procedure and the fault-finding tree](assets/web/cs-8-115-text-p112-preview.webp)](assets/web/cs-8-115-text-p112-zoom.webp)
<figcaption>
  Fault finding — meaning of the symbols used.
  <span class="cs">CS 8 115</span>
  <span class="src">service manual page 112</span>
</figcaption>
</figure>

## The test procedure

Start here.

1. **Switch on the drive with the mains switch.**
2. **Does the STAND-BY indication light?**
    - **No** → is the fan operating? If not, check
      [module T](../modules/t-supply/index.md). If it is, press EJECT: if the
      disc tray does not open, check [module T](../modules/t-supply/index.md);
      if it does, check [module N](../modules/n-display-keyboard/index.md) and
      [module S](../modules/s-control/index.md).
    - **Yes** → continue.
3. **Press EJECT. Does the disc tray open?**
    - **No** → check [module P](../modules/p-frontloader/index.md) and
      [module R](../modules/r-drive-processor/index.md).
    - **Yes** → continue.
4. **Switch the mains switch off, then switch on in
   [self-test mode](diagnostic-mode.md).**
5. **Is `DIAGNOSTICS` displayed?**
    - **No** → go to chart ① [no display](#chart-1-no-display).
    - **Yes** → continue.
6. **Insert a 12" CAV disc and close the disc tray.**
7. **Is the error code `- - -`?**
    - **Yes** → **end.** Nothing is wrong.
    - **No** → is the error code greater than 60? If **yes**, look it up in
      [meaning of the error codes](error-codes.md). If **no**, go to chart ②
      [error code < 60](#chart-2-error-code-60-self-test-mode).

<figure class="sheet" markdown>
[![Test procedure flow chart: switch on with the mains switch, check the stand-by indication and the fan, press eject, switch into self-test mode, check for the DIAGNOSTICS display, insert a 12-inch CAV disc and read the error code](assets/web/cs-8-116-figure-p113-preview.webp)](assets/web/cs-8-116-figure-p113-zoom.webp)
<figcaption>
  Test procedure flow chart.
  <span class="cs">CS 8 116</span>
  <span class="src">service manual page 113</span>
</figcaption>
</figure>

## Chart ① — no display

Reached when the player runs but nothing appears on the monitor.

1. **Measure VOW on [module R](../modules/r-drive-processor/index.md),
   connector 25aR1.** Are there positive pulses of 5 Vpp in the video field?
    - **No** → measure `REFH` and `REFV` on module R. If they are **not**
      correct, check [module D](../modules/d-reference-source/index.md); if
      they **are** correct, check
      [module R](../modules/r-drive-processor/index.md).
    - **Yes** → continue.
2. **Press SK2 on [Analog I/O module U](../modules/u-analog-io/index.md)** —
   position NOT ENCODED. Is there a video signal on CVBS OUT (BNC3)?
    - **No** → check [module C](../modules/c-video-processor/index.md).
    - **Yes** → continue.
3. **Release SK2** — position ENCODED. Is there a sync signal on CVBS OUT
   (BNC3)?
    - **No** → check [module B](../modules/b-rgb/index.md).
    - **Yes** → continue.
4. **Are there positive pulses on connector 1U2 of module U?**
    - **No** → check [module B](../modules/b-rgb/index.md).
    - **Yes** → check [module Y](../modules/y-video-mixer/index.md). **End.**

SK2 is one of the two switches hidden on module U — see
[remarks](../general-service/remarks.md), section 4.

<figure class="sheet" markdown>
[![Fault finding chart 1, no display: measure VOW on module R, check REFH and REFV, press SK2 on analog I/O module U and check for video and sync on CVBS OUT, ending at module B, C, D, R or Y](assets/web/cs-8-117-figure-p114-preview.webp)](assets/web/cs-8-117-figure-p114-zoom.webp)
<figcaption>
  Fault finding chart 1 — no display.
  <span class="cs">CS 8 117</span>
  <span class="src">service manual page 114</span>
</figcaption>
</figure>

## Chart ② — error code < 60 (self-test mode)

The start-up procedure, step by step. Each row is one test the drive makes as
it starts; the code in the third column is what it raises when the test fails.
This is the table to read a start-up error code against.

| Step | Test | Fails → | Meaning | Check |
| --- | --- | --- | --- | --- |
| Tray moving inside | `TI` = 0 | [001](error-codes.md#error-1) | Tray meets hindrance | The disc tray moving inwards; [P](../modules/p-frontloader/index.md), [R](../modules/r-drive-processor/index.md) |
| Measure disc reflection | `DR` = 1 | [002](error-codes.md#error-2) | No disc reflection | Whether a disc is in the tray; the ATC circuit in the optical deck, [Z](../modules/z-deck-electronics/index.md) |
| Position of LDU slide inwards | `SPI` = 0 | [003](error-codes.md#error-3) | SPI not found | Whether the LDU slide is in the inward position; [E](../modules/e-slide-drive/index.md), [R](../modules/r-drive-processor/index.md) |
| Active tilt control operative | `TILTOK` = 0 | [004](error-codes.md#error-4) | Time-out tilt | The ATC circuit in the optical deck |
| Laser is emitting light | `LA-STA` = 0 | [005](error-codes.md#error-5) | Laser not on | [R](../modules/r-drive-processor/index.md), [Z](../modules/z-deck-electronics/index.md) |
| Objective not in focus | `FOC-IND` = 1 | [006](error-codes.md#error-6) | Not out of focus | [R](../modules/r-drive-processor/index.md), [J](../modules/j-focus/index.md) |
| Objective in focus | `FOC-IND` = 0 | [007](error-codes.md#error-7) | Not in focus after 5 attempts (no rotation of disc) | Clean the objective; [R](../modules/r-drive-processor/index.md), [J](../modules/j-focus/index.md), [Z](../modules/z-deck-electronics/index.md) |
| Motor is starting until normal speed | `0-RPM` = 1 | [008](error-codes.md#error-8) | Motor speed error | Does the motor rotate? If **no**: [R](../modules/r-drive-processor/index.md), [G](../modules/g-genlock/index.md), [F](../modules/f-motor-sequence/index.md). If **yes**: [R](../modules/r-drive-processor/index.md) |
| Motor has reached nominal speed | `FRLOCK` = 1 | [009](error-codes.md#error-9) | Frame lock | [F](../modules/f-motor-sequence/index.md) |

Past `FRLOCK`, the chart hands you back to
[meaning of the error codes](error-codes.md).

The signal names in the second column are in the
[alphabetical signal listing](../system/signal-listing.md), which gives the
polarity of each: `TI` is 0 V when the tray is inside, `SPI` is 0 V when the
slide is inwards, and so on.

!!! tip "Worked examples"

    Errors 7 and 9 are the two most common start-up failures on a
    forty-year-old player, and both have been traced end to end on a real
    machine — see the [case studies](case-studies/index.md).

<figure class="sheet" markdown>
[![Fault finding chart 2, error code below 60 in self-test mode, part 1: tray moving inside with TI equals 0, measure disc reflection with DR equals 1, and LDU slide position with SPI equals 0, raising codes 001, 002 and 003](assets/web/cs-8-118-figure-p115-preview.webp)](assets/web/cs-8-118-figure-p115-zoom.webp)
<figcaption>
  Fault finding chart 2 — start-up procedure, tray to slide position.
  <span class="cs">CS 8 118</span>
  <span class="src">service manual page 115</span>
</figcaption>
</figure>

<figure class="sheet" markdown>
[![Fault finding chart 2 continued: active tilt control with TILTOK equals 0, laser emitting with LA-STA equals 0, and objective not in focus with FOC-IND equals 1, raising codes 004, 005 and 006](assets/web/cs-8-119-figure-p116-preview.webp)](assets/web/cs-8-119-figure-p116-zoom.webp)
<figcaption>
  Fault finding chart — time-out tilt, laser not on, not out of focus.
  <span class="cs">CS 8 119</span>
  <span class="src">service manual page 116</span>
</figcaption>
</figure>

<figure class="sheet" markdown>
[![Fault finding chart 2 continued: objective in focus with FOC-IND equals 0, motor starting with 0-RPM equals 1, and motor at nominal speed with FRLOCK equals 1, raising codes 007, 008 and 009](assets/web/cs-8-120-figure-p117-preview.webp)](assets/web/cs-8-120-figure-p117-zoom.webp)
<figcaption>
  Fault finding chart — not in focus after 5 attempts, motor speed error,
  frame lock.
  <span class="cs">CS 8 120</span>
  <span class="src">service manual page 117</span>
</figcaption>
</figure>
