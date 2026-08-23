---
title: Modification levels
description: >-
  Where to read the modification level of the set, of a module and of the
  EPROM software, and how the ?= revision request maps onto the program number.
---

# Modification levels

Modification levels are indicated all over the set, in four different places
and in three different notations. Establish them before you order a part or
compare a circuit diagram: several modules changed substantially between
levels.

The surveys themselves — which level a given serial number carries, and what
changed at each — are in chapter 8:
[modification levels per module](../service-information/modification-levels.md).

## 1. Modification level of the set

At the rear of the cabinet, in two places.

**a) Change code on the type number plate.** Under the type number a letter and
digit code is given. The change code is preceded by the production centre.

**b) Modification level on a yellow sticker.** A TM code is marked on a yellow
sticker — `TM3`, for instance, meaning modification level 3.

Both markings are visible on the rear panel photograph on the
[controls and connections](../overview/controls-and-connections.md) page: the
type plate is the paper label in the centre, and the printed grid to its left
is the TM code.

## 2. Modification level of the module

- **In the circuit diagram:** top right, under the name of the module — e.g.
  `MOD LEVEL 3`.
- **On the PCB:** in the service printing at the component side, e.g.
  `X2345678901`, with the modification level marked.

## 3. Modification level of the software in the EPROMs

Various modules carry programmed EPROMs:

| Module | Item number | Name | Program number |
| --- | --- | --- | --- |
| [Drive processor (R)](../modules/r-drive-processor/index.md) | 7204 | DRIVE | 3104 103 6803.4 |
| [Control (S)](../modules/s-control/index.md) | 7202 | CONTROL | 3104 103 6804.4 |
| [CPU (W)](../modules/w-cpu-data-grabber/index.md) \* | 7201 | SYNC | 3104 103 6808.0 |
| [CPU (W)](../modules/w-cpu-data-grabber/index.md) \* | 7224 | DESCR. | 3104 103 6807.0 |
| [CPU (W)](../modules/w-cpu-data-grabber/index.md) \* | 7247 | LV DOS #1 | 3104 103 6805.2 |
| [CPU (W)](../modules/w-cpu-data-grabber/index.md) \* | 7248 | LV DOS #2 | 3104 103 6806.2 |

\* only for VP415.

The program number is on a sticker on the EPROM. **The modification level of
the software is the last digit of the program number**, the digit after the
dot.

Dumps of these EPROMs, with sizes and checksums, are on the
[firmware](../reference/firmware.md) page.

### Reading the level over the interface

The modification level of the software in the Drive and Control EPROMs can also
be retrieved by an external computer, by sending the F-code command `?=` to the
disc drive — see
[F-code commands](../operating-instructions/f-code-commands.md), revision level
request.

The player answers with a 5-digit code:

| Digit | Meaning |
| --- | --- |
| 1 | always 0 |
| 2 | major level, Drive |
| 3 | minor level, Drive |
| 4 | major level, Control |
| 5 | minor level, Control |

So a Drive software level reads as digit 2 . digit 3 — e.g. 1.5 — and Control
as digit 4 . digit 5 — e.g. 1.4.

The relation to the program number is:

| | Mod. level in program number | Mod. level in software revision |
| --- | --- | --- |
| Drive | 3104 103 6803**.4** | 1.5 |
| Control | 3104 103 6804**.4** | 1.4 |

Each time a change takes place in the software, the modification level is
raised by one.

<figure class="sheet" markdown>
[![Modification levels: of the set, of the module, and of the software in the EPROMs](assets/web/cs-7-820-text-p010-preview.webp)](assets/web/cs-7-820-text-p010-zoom.webp)
<figcaption>
  Modification levels. The two small figures show the change code under the
  type number and the TM code on the yellow sticker.
  <span class="cs">CS 7 820</span>
  <span class="src">service manual page 010</span>
</figcaption>
</figure>
