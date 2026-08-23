---
title: Fault symptoms
description: >-
  Known fault symptoms in the VP415, the modification that fixes each, and the
  modification level at which it was introduced.
---

# Fault symptoms and solutions

Dated 1987-05-20. A survey of known fault symptoms and problems that can occur
in the disc drive, with a possible solution for each and the modification level
at which that solution was introduced.

This is the most directly useful sheet in chapter 8: if a player misbehaves in
one of these specific ways, it is probably a board below the level at which the
fix landed. Check the level against
[modification levels](modification-levels.md) before you go looking for a
component fault.

The manual divides the problems into five categories:

| Category | |
| --- | --- |
| **A** | [Start-up problems](#a-start-up-problems) |
| **B** | [Playability problems](#b-playability-problems) |
| **C** | Audio problems — *no entries in this issue* |
| **D** | [Video problems](#d-video-problems) |
| **E** | [Communication problems](#e-communication-problems) |

<figure class="sheet" markdown>
[![Fault symptoms and solutions: the introduction to the survey, listing the five problem categories A to E](assets/web/cs-8-290-table-p193-preview.webp)](assets/web/cs-8-290-table-p193-zoom.webp)
<figcaption>
  Fault symptoms and solutions.
  <span class="cs">CS 8 290</span>
  <span class="src">service manual page 193</span>
</figcaption>
</figure>

## A — Start-up problems

| No. | Problem | Solution | Introduced |
| --- | --- | --- | --- |
| **A 1** | Disc tray opens when starting up | Change C2018 on [drive processor module R](../modules/r-drive-processor/index.md) from 15 μF to 68 μF | Module R, mod level 7 |
| **A 2** | No eject of disc tray when no disc has been inserted | Update in drive software on drive processor module R (6803.5) | Module R, mod level 4 |
| **A 3** | Start-up problem when loading a 6" or 8" disc | Change C2020 from 4 μF to 1 μF on [motor module F](../modules/f-motor-sequence/index.md) | Module F, mod level 6 |
| **A 4** | White stripes on screen when the disc drive is switched on | Short-circuit pins 27 and 28 of IC 7203 on [RGB module B](../modules/b-rgb/index.md) | Module B, mod level 8 |
| **A 5** | Horizontal stripes in the picture at start-up — **VP410 only** | Add a resistor 0.15 E / 1 W in series with fuse F913 on [supply module T](../modules/t-supply/index.md) | Module T, mod level 1 |

<figure class="sheet" markdown>
[![Start-up problems A1 to A5, each with its problem, solution and the modification level at which the solution was introduced](assets/web/cs-8-291-table-p194-preview.webp)](assets/web/cs-8-291-table-p194-zoom.webp)
<figcaption>
  Start-up problems.
  <span class="cs">CS 8 291</span>
  <span class="src">service manual page 194</span>
</figcaption>
</figure>

## B — Playability problems

| No. | Problem | Solution | Introduced |
| --- | --- | --- | --- |
| **B 1** | Instant jump failures | Delete R3001 to R3010, C2002, C2004, TS7001 and TS7004 on [radial module M](../modules/m-radial/index.md); several updates in drive software on drive processor module R (6803.5 and .6) | Module M, mod level 2<br>Module R, mod levels 4 and 6 |
| **B 2** | Goto failures at CLV | Change IC7260 on [motor + sequence module F](../modules/f-motor-sequence/index.md) from MC1458P1 to MC34002BP | Module F, mod level 6 |

<figure class="sheet" markdown>
[![Playability problems B1 and B2, each with its problem, solution and the modification level at which the solution was introduced](assets/web/cs-8-292-table-p195-preview.webp)](assets/web/cs-8-292-table-p195-zoom.webp)
<figcaption>
  Playability problems.
  <span class="cs">CS 8 292</span>
  <span class="src">service manual page 195</span>
</figcaption>
</figure>

## D — Video problems

| No. | Problem | Solution | Introduced |
| --- | --- | --- | --- |
| **D 1** | White dots on monitor screen — motor disturbance in the video signal | Mount metal screening around coils L5001 and L5002 on [HF processor module K](../modules/k-hf-processor/index.md), and around delay line L5001 on [video D.O. correction module L](../modules/l-video-dropout-correction/index.md). Screening assembly, service code number **4822 462 41173**.<br><br>Add 3 capacitors 1n2 and delete 6 capacitors 47p, as described under mod level 6 of [motor + sequence module F](modification-levels.md#mod-f) | Module K, mod level 0<br>Module L, mod level 1 |
| **D 2** | Colour loss when two disc drives operate synchronously and the slave drive is in still mode | Add a resistor 22 k between B-TS7012 and 7B3 on [module B](../modules/b-rgb/index.md); connect 9C1 and 7B3 on [module carrier V](../modules/v-module-carrier/index.md) | Module B, mod level 8 |
| **D 3** | Horizontal distortion of computer overlay — VP415 | Change C2416 on [video mixer module Y](../modules/y-video-mixer/index.md) from 8n2 to 100p | Module Y, mod level 5 |
| **D 4** | Jitter of computer overlay — VP415 | Add a resistor 10 M in parallel with C2415 on [video mixer module Y](../modules/y-video-mixer/index.md) | Module Y, mod level 6 |

<figure class="sheet" markdown>
[![Video problems D1 to D4, each with its problem, solution and the modification level at which the solution was introduced](assets/web/cs-8-293-table-p196-preview.webp)](assets/web/cs-8-293-table-p196-zoom.webp)
<figcaption>
  Video problems.
  <span class="cs">CS 8 293</span>
  <span class="src">service manual page 196</span>
</figcaption>
</figure>

## E — Communication problems

| No. | Problem | Solution | Introduced |
| --- | --- | --- | --- |
| **E 1** | The disc drive does not accept any commands from an external computer after a printer command `<LF><CR>` or `<CR><LF>` — for instance `LPRINT "F500R"` | Change the command to `LPRINT "F500R"; CHR$(13);`<br>An adaptation of the CONTROL software was to follow at a later stage | — |

!!! tip "Still relevant"

    E 1 is a software problem in the host, not the player: the player is left
    waiting because the trailing line feed is never consumed. Anything driving a
    VP415 over RS232 today needs to send a bare carriage return, not the
    platform's usual line ending. The F-code command set is on the
    [F-codes](../reference/f-codes.md) page.

<figure class="sheet" markdown>
[![Communication problem E1: the disc drive not accepting commands after a printer command with a line feed, and the BASIC LPRINT workaround](assets/web/cs-8-294-table-p197-preview.webp)](assets/web/cs-8-294-table-p197-zoom.webp)
<figcaption>
  Communication problems.
  <span class="cs">CS 8 294</span>
  <span class="src">service manual page 197</span>
</figcaption>
</figure>
