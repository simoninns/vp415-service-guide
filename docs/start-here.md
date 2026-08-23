---
title: Where do I start?
description: >-
  A symptom-first route into the service manual: what the player is doing
  wrong, and which page of this site answers it.
search:
  boost: 3
---

# Where do I start?

This site is the service manual, and the service manual is arranged the way
Philips wrote it — by chapter, not by symptom. This page is the other way in:
find what the player is doing, and go straight to the page that deals with it.

!!! danger "Before anything else"

    Read the [warnings](general-service/warnings.md). The VP415 exposes an
    invisible laser beam when the cabinet is open, and
    [supply module T](modules/t-supply/index.md) stays live and charged after
    the mains is pulled. [Service hints](general-service/service-hints.md)
    covers ESD, which will quietly kill several of the boards.

## Make the player tell you first

The VP415 diagnoses itself, and it is nearly always faster to let it. Hold
**STANDBY** and **EJECT** as you switch the mains on, and it starts in
[self-test mode](repair/diagnostic-mode.md) and puts a three-digit code in the
corner of the picture. That code is the fastest route into everything below.

<div class="grid cards" markdown>

-   :material-play-box-outline: **Start the diagnostics**

    ---

    Both modes, the key combinations, and how to read what appears.

    [:octicons-arrow-right-24: Diagnostic mode](repair/diagnostic-mode.md)

-   :material-format-list-numbered: **Look a code up**

    ---

    Every code from 1 to 171, its severity, and which module to look at.

    [:octicons-arrow-right-24: Error codes](repair/error-codes.md)

-   :material-sitemap-outline: **Follow the chart**

    ---

    The manual's own test procedure, from the mains switch to frame lock.

    [:octicons-arrow-right-24: Fault-finding charts](repair/fault-finding.md)

</div>

## Symptom to page

| The player is… | Start with | Then |
| --- | --- | --- |
| **Completely dead** — no stand-by indication, no fan | [Test procedure, step 2](repair/fault-finding.md#the-test-procedure) | [Supply module T](modules/t-supply/index.md) |
| **Dead but the fan runs** | [Test procedure, step 2](repair/fault-finding.md#the-test-procedure) | [Module N](modules/n-display-keyboard/index.md) and [module S](modules/s-control/index.md) |
| **Not opening the tray** on EJECT | [Test procedure, step 3](repair/fault-finding.md#the-test-procedure) | [Front loader P](modules/p-frontloader/index.md), [drive processor R](modules/r-drive-processor/index.md) |
| **Opening the tray on its own at start-up** | [Fault symptom A 1](service-information/fault-symptoms.md#a-start-up-problems) | [Modification levels](service-information/modification-levels.md#mod-r) — a level-7 change to module R |
| **Showing nothing on the monitor**, or no `DIAGNOSTICS` in self-test | [Chart ① — no display](repair/fault-finding.md#chart-1-no-display) | [D](modules/d-reference-source/index.md), [B](modules/b-rgb/index.md), [C](modules/c-video-processor/index.md), [Y](modules/y-video-mixer/index.md) |
| **Loading a disc but never spinning it** | [Self-test](repair/diagnostic-mode.md), then the code | [Error codes 1–9](repair/error-codes.md#the-codes) |
| **Showing a number in the corner of the picture** | [Meaning of the error codes](repair/error-codes.md) | The *where to look* column on that page |
| **Failing to focus** — error 6, 7, 12, 17, 60 or 61 | [Error 7 case study](repair/case-studies/error-7-focus.md) | [Focus module J](modules/j-focus/index.md), [deck electronics Z](modules/z-deck-electronics/index.md) |
| **Failing to lock** — error 9, or a picture that will not hold still | [Error 9 case study](repair/case-studies/error-9-frame-lock.md) | [G](modules/g-genlock/index.md), [D](modules/d-reference-source/index.md), [F](modules/f-motor-sequence/index.md), [L](modules/l-video-dropout-correction/index.md) |
| **Playing, but with white dots or dropouts in the picture** | [Fault symptom D 1](service-information/fault-symptoms.md#d-video-problems) | [HF processor K](modules/k-hf-processor/index.md), [drop-out correction L](modules/l-video-dropout-correction/index.md) |
| **Playing, but with no sound** | [Audio processor A](modules/a-audio-processor/index.md) | [Analog I/O U](modules/u-analog-io/index.md), [audio adjustments](general-service/adjustments.md) |
| **Jumping or missing frames** — instant jump, goto | [Fault symptoms B 1 and B 2](service-information/fault-symptoms.md#b-playability-problems) | [Radial module M](modules/m-radial/index.md), [slide drive E](modules/e-slide-drive/index.md) |
| **Distorting or jittering the computer overlay** | [Fault symptoms D 3 and D 4](service-information/fault-symptoms.md#d-video-problems) | [Video mixer Y](modules/y-video-mixer/index.md) |
| **Playing video, but the computer cannot read data** | [SCSI operation](operating-instructions/scsi-operation.md) | [LV-ROM decoder X](modules/x-lv-rom-decoder/index.md), [CPU + data grabber W](modules/w-cpu-data-grabber/index.md) |
| **Ignoring commands over RS232** | [Fault symptom E 1](service-information/fault-symptoms.md#e-communication-problems) | [F-codes](reference/f-codes.md) — and check the host is not sending a line feed |
| **Ignoring the handset** | [RC5 receiver Q](modules/q-rc5-receiver/index.md) | [Remote control](modules/remote-control/index.md) |
| **Working, but out of adjustment** | [Adjustments](general-service/adjustments.md) | The *adjustments* section of the [module page](modules/index.md) |

## When the code does not tell the whole story

A code names the test that failed, not the part that caused it. Frame lock is
tested last, so an [error 9](repair/error-codes.md#error-9) is reported against
the motor module — and in the
[worked case study](repair/case-studies/error-9-frame-lock.md) the motor module
was innocent, because the loop that feeds it runs through three other boards
first. Read the [circuit description](circuit-description/index.md) of the
function that failed before condemning the board the chart names.

Two other things worth checking before reaching for a scope:

- **The modification level of the board.** Several known faults are
  [fixed by a modification](service-information/fault-symptoms.md), and a board
  below that level will show the fault however healthy it is. How to read the
  level off a board is in
  [general service](general-service/modification-levels.md).
- **The software release.** The drive and control ROMs went through eight
  releases; [software releases](service-information/software-releases.md)
  lists what each one changed.

## What to have on the bench

| | |
| --- | --- |
| A **12-inch CAV disc** | The self-test needs one. The manual's start-up chart assumes it |
| A **monitor** | The error codes are displayed on the picture, not on the front panel |
| An **oscilloscope** | Most of the manual's measurements are pulse trains and levels |
| The **service tools** | Extender boards and the deck jigs — [service tools](general-service/service-tools.md) |
| The **demounting order** | Which panels come off in which order — [demounting](general-service/demounting.md) |

## Once you have found it

If this site sent you the wrong way, or you found something the manual does not
say, the [contributing](contributing.md) page has the templates: a repair
report, a correction, and the worked example of adding a repair guide of your
own to a module page.
