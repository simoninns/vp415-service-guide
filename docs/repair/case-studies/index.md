---
title: Repair case studies
description: >-
  Worked diagnostic examples: a real fault, traced from the error code to the
  component, with the scope traces taken along the way.
---

# Repair case studies

Two faults on a real VP415, traced from the error code the diagnostic software
printed to the part of the circuit that was not doing its job. Both are
**original work, not from the service manual**: the measurements were taken on
a bench in 2017 with a Keysight MSO-X 3104T, and the traces are reproduced here
as they came off the scope.

| Case | Code | Where it got to |
| --- | --- | --- |
| [Not in focus](error-7-focus.md) | [007](../error-codes.md#error-7) | Nothing reaching the objective coil; the focus amplifier on [module J](../../modules/j-focus/index.md) is idle. Turned up the **6210 / 6211 pinout erratum** |
| [Frame lock](error-9-frame-lock.md) | [009](../error-codes.md#error-9) | `LPO` and `LPO'` missing at IC7206-2A on [module G](../../modules/g-genlock/index.md), with every input to the module good |

!!! warning "Neither case ends with a working player"

    Both write-ups stop where the notes stop: a fault localised to a board and
    a stage, and the next measurement identified but not taken. They are
    published as worked examples of *method* — how to get from a two-digit
    code to a named component — rather than as repair recipes, and each says
    plainly what was ruled out, what was found, and what is still open.

## What they are good for

- **They show what the manual's own numbers are for.** Both investigations
  lean on the red waveform sketches printed beside the connector pins on the
  circuit diagrams — amplitude and period, drawn at the pin. Half of
  diagnosing either fault is knowing what the pin should look like.
- **They show where the fault-finding charts stop being useful.** An error 9
  sends you to [module F](../../modules/f-motor-sequence/index.md); the fault
  was on module G, two boards upstream, and module F was doing as it was told.
- **One of them corrected the manual.** The
  [6210 / 6211 pinout](../../modules/j-focus/index.md) is printed BCE and
  should be ECB. That erratum came out of the error 7 investigation and is now
  carried on the module J page, where someone about to replace those
  transistors will see it.

## Related

- [Meaning of the error codes](../error-codes.md) — the full table, every code
  anchored so a case study can link straight at it
- [The diagnostic software](../diagnostic-mode.md) — how to get a code out of
  the player in the first place
- [Fault-finding charts](../fault-finding.md) — the manual's own route from a
  code to a module
