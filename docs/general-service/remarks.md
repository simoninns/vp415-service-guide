---
title: Remarks
description: >-
  How the service manual is put together, how the circuit diagrams and PCB
  lay-outs are drawn, the hidden switches on module U, and what may not be
  repaired.
---

# Remarks

The opening sheet of chapter 2 explains how to read the rest of the manual —
and it carries two things a repairer needs early: the item-numbering conversion
between the circuit diagrams and the PCB silkscreen, and the two switches on
module U that are hidden from the user.

## 1. Care of the disc drive

The disc drive requires no special maintenance. It is, however, recommended to
clean the objective lens from time to time with a piece of wadding, dipped in
alcohol.

## 2. Set-up of the service manual

The set is composed of various modules, A through Z. The circuit diagrams, PCB
lay-outs and parts lists have also been classified per module — on this site,
that is [one page per module](../modules/index.md).

### a) Circuit diagrams

Of each module a functional circuit diagram has been given, with the incoming
signals drawn as much as possible at the left-hand side and the outgoing
signals at the right-hand side. Each incoming and outgoing signal has a unique
name, the meaning of which can be read in the
[signal listing](../system/signal-listing.md).

If a signal enters or leaves the module, this takes place via a connector — for
example `6B2` is pin 6 of connector B2 — and via a letter indication in the
line. This indication mentions to which module the line is connected.

If the letter indication in the line is the same as the module on which the
signal is present, the signal remains on the module mentioned and, naturally,
no connector is drawn.

### b) Oscillograms and voltages in the circuit diagrams

The oscillograms in the diagrams have been measured with a dual-beam scope with
delayed timebase, a PM3214. The set has been connected to a monitor by means of
a SCART cable.

| Trace | Conditions |
| --- | --- |
| Video | Still picture, picture number 5530 (EBU colour bar, 75% saturation) |
| Audio 1 | Normal play, picture numbers 6200–6500, 1 kHz modulation |
| Audio 2 | Normal play, picture numbers 6500–6900, 1 kHz modulation |

The DC voltages have been measured with a digital multimeter PM2524, still
picture, picture number 5530, unless stated otherwise.

### c) PCB lay-outs

Most modules in the set have been equipped with double-sided copper pattern and
plated-through holes. For each module a PCB lay-out is drawn, consisting of a
drawing of the component side and of the soldering side (chip side) with
corresponding copper pattern.

### d) Parts lists

For each module an electrical parts list is given, stating the service code
numbers of the specific electrical components that have been applied on the
module. The code numbers of the standard components — ICs, transistors, diodes,
standard resistors and so on — have been placed on a collective list in
[chapter 5](../parts/electrical-parts.md).

### e) Service code numbers of the modules

In this service manual service code numbers for the modules have not been
mentioned. Please consult your parts supplier.

## 3. Repair on modules

To enable repair and adjustment on modules, use can be made of extension PCBs
or extension cables. A survey can be found under
[service tools](service-tools.md) in this chapter.

## 4. Hidden switches

!!! info "Two switches on module U that are not on any panel"

    On [Analog I/O module U](../modules/u-analog-io/index.md) two switches have
    been applied, hidden for the user:

    | Switch | Function | Factory setting |
    | --- | --- | --- |
    | SK1 | +11 V **or** RC5 signal at pin 8 of the Euroconnector | RC5 at pin 8 (switch pressed out) |
    | SK2 | ENCODED **or** NOT ENCODED CVBS signal on CVBS OUT connector BNC3 | ENCODED (switch pressed out) |

    Consult the circuit diagram of Analog I/O module U for more detail.

## 5. The optical deck

The optical deck in the disc drive is composed of various critical components
and, at the production department, adjusted by complicated alignment equipment.

!!! warning "Not repairable by the service technician"

    For the time being repair of the Deck Electronics and of the Laser
    Detection Unit by a service technician is not allowed.

    If a failure analysis reveals that the Deck Electronics or LDU are
    defective, the entire deck should be submitted for repair to the production
    centre via the Central Repair Procedure of the Concern Service Centre.
    Please inquire at your parts supplier's for this procedure.

    This is a 1986 instruction and the Concern Service Centre is long gone. It
    is recorded here because it explains why the manual gives no component-level
    procedure for the deck — not because a deck can be sent anywhere today. The
    [module Z](../modules/z-deck-electronics/index.md) page lists the six
    potentiometers the deck electronics board carries and what each one sets.

Repairs on the slide drive assembly and the Automatic Tilt Control (ATC)
assembly are possible. See the
[list of mechanical parts](../parts/mechanical-parts.md) for the correct code
numbers.

## 6. Coding of items

The coding of component items in the service printing of the PCBs can differ
from the coding of the items in the circuit diagrams — except on
[supply module T](../modules/t-supply/index.md). On the PCBs a letter/number
coding has been used, `R1`, `C1`; in the diagram a four-number coding, `3001`,
`2001`.

In both systems the trailing digits are the item number and the leading
character identifies the kind of component:

| Circuit diagram<br>(4-number coding) | Component | Service printing on PCB<br>(letter/number coding) |
| --- | --- | --- |
| 1 | unit, battery | U |
| 2 | capacitor | C |
| 3 | resistor | R |
| 5 | coil, transformer, crystal | S, L, K |
| 6 | diode | D |
| 7 | transistor, IC | T, TS, I, IC |

So diagram item `2001` is the first capacitor, `C1` on the board; `3305` is
resistor `R305`.

<figure class="sheet" markdown>
[![Remarks: care of the disc drive, set-up of the service manual, repair on modules, hidden switches, the optical deck, coding of items](assets/web/cs-7-818-text-p008-preview.webp)](assets/web/cs-7-818-text-p008-zoom.webp)
<figcaption>
  Remarks.
  <span class="cs">CS 7 818</span>
  <span class="src">service manual page 008</span>
</figcaption>
</figure>
