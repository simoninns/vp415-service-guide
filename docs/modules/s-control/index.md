---
title: Module S - Control
description: >-
  Control: the player's main microcontroller and watchdog.
search:
  boost: 2
---

# Module S - Control

Control: the player's main microcontroller and watchdog.

## Overview

Control module S is the player's outward-facing processor. It does two things:

1. **An RS232 interface** between the player and an external computer.
2. **A local bus interface** to the CPU board — the UART link to
   [module W](../w-cpu-data-grabber/index.md).

Everything on it runs under processor IC7201, which is wired to address 64 K of
ROM and 64 K of RAM — though only **8 K of RAM** is fitted in the VP415 and
VP410. The RAM (IC7203) is non-volatile, kept alive by a **2.4 V Ni-Cd
battery**, item 1002.

| | |
| --- | --- |
| Designation | **S** — control |
| Modification levels | 3 → 8 |
| Data sheet | `CS 7 852`, pages 069–070 (mod level 3) |
| Circuit diagram | `CS 6 884`, pages 067–068 |
| Connectors | `S1`, `S2` |
| Processor | IC7201 with crystal 5101, **11.059 MHz** |
| Slave processor | IC7211 with crystal 5102, **4 MHz** — one RS232 and two RC5 I/Os |
| Firmware | IC7202 — `CONTROL`, TMS 27512, program 3104 103 6804.4 → 6804.9 |
| Battery | 1002, 2.4 V Ni-Cd — **check it before you diagnose lost settings** |

## The board

<div class="sheet-pair" markdown>
<figure class="sheet sheet--photo" markdown>
[![Module S, component side of the board](assets/web/s-control-top-preview.webp)](assets/web/s-control-top-zoom.webp)
<figcaption>
  Module S, component side.
</figcaption>
</figure>
<figure class="sheet sheet--photo" markdown>
[![Module S, solder side of the board](assets/web/s-control-bottom-preview.webp)](assets/web/s-control-bottom-zoom.webp)
<figcaption>
  Module S, solder side.
</figcaption>
</figure>
</div>

## Where it sits in the player

One of the two large boards at the right of the chassis, beside
[drive processor module R](../r-drive-processor/index.md) — see the
[module and connector lay-out](../../system/module-layout.md).

## Circuit description

ROM (IC7202) and RAM (IC7203) overlay the same address field; no conflict
arises because the control bus is fully decoded. The processor's data bus pins
double as the low address byte, so IC7204 latches the address under `ALE`, and
the ROM is read-enabled by `PSEN`. Address decoding is done by the 3-to-8 line
decoder IC7205, giving chip selects `CS1`–`CS8`; `CS1` enables the RAM.

The I/O ports live in the top 8 K of memory space, `E000h`–`FFFFh`. `CS8` is
decoded further with A10, A11, `WR` and `RD` into `RD1`–`RD3`, `RDEN`, `WR1`,
`WR3` and `WREN`. The ports themselves:

| Device | Function |
| --- | --- |
| IC7209 | Output latch strobed by `WR1`, providing `VP0`–`VP2` — controls for [video mixer module Y](../y-video-mixer/index.md), by way of module Uc |
| IC7207 | Bidirectional buffer between the data bus and the S-bus; enabled by `RDEN` or `WREN`, direction set by `WREN` |
| IC7208 | Input buffer reading the **DIP switches** `DS1`–`DS8`; enabled by `RD1` |
| IC7211 | Slave processor: one RS232 and two RC5 I/Os, addressed with A9 and `WR3` or `RD3`, signalling with `OBF` |
| IC7201 | The main processor — S-bus handshakes, and one RS232 port to the external connector through line transmitter 7214 and line receiver 7213 |

The full text, including the S-bus operation and the link to the CPU board, is
in [chapter 7, module S](../../circuit-description/modules.md#module-s).

## Adjustments

The manual gives **no adjustment procedure** for this module.

## Circuit diagram

<figure class="sheet sheet--fold" markdown>
[![Control module S - circuit diagram](assets/web/cs-6-884-circuit-p067-068-preview.webp)](assets/web/cs-6-884-circuit-p067-068-zoom.webp)
<figcaption>
  Control module S - circuit diagram.
  <span class="cs">CS 6 884</span>
  <span class="src">service manual pages 067, 068</span>
</figcaption>
</figure>

## PCB lay-out

<figure class="sheet sheet--fold" markdown>
[![Control module S (mod level 3) - parts](assets/web/cs-7-852-module-sheet-p069-070-preview.webp)](assets/web/cs-7-852-module-sheet-p069-070-zoom.webp)
<figcaption>
  Control module S (mod level 3) - parts.
  <span class="cs">CS 7 852</span>
  <span class="src">service manual pages 069, 070</span>
</figcaption>
</figure>

## List of electrical parts

**Eproms (programmed)**

| Item | Service code number | Value | Rating |
| --- | --- | --- | --- |
| 7202 | 4822 209 51256 | TMS 27512 — `CONTROL` |  |

**Batteries**

| Item | Service code number | Value | Rating |
| --- | --- | --- | --- |
| 1002 | 4822 138 10032 | Battery 2.4 V |  |

**Crystals**

| Item | Service code number | Value | Rating |
| --- | --- | --- | --- |
| 5101 | 4822 242 70917 | 11.059 MHz |  |
| 5102 | 4822 242 70668 | 4 MHz |  |

**Coils**

| Item | Service code number | Value | Rating |
| --- | --- | --- | --- |
| 5001 | 4822 158 10101 | 5.3 μH |  |
| 5002 | 4822 158 10101 | 5.3 μH |  |
| 5003 | 4822 158 10101 | 5.3 μH |  |

**NFR25 Resistors**

| Item | Service code number | Value | Rating |
| --- | --- | --- | --- |
| 3028 | 4822 111 30483 | 1 Ω |  |

**Capacitors**

| Item | Service code number | Value | Rating |
| --- | --- | --- | --- |
| 2001 | 4822 124 22027 | 47 μF | 25 V |
| 2002 | 5322 124 21749 | 10 μF | 63 V |
| 2003 | 5322 124 21749 | 10 μF | 63 V |
| 2004 | 4822 122 31759 | 22 nF |  |
| 2005 | 4822 122 31759 | 22 nF |  |
| 2006 | 4822 122 31759 | 22 nF |  |
| 2007 | 4822 124 22027 | 47 μF | 25 V |
| 2008 | 4822 124 22029 | 2.2 μF | 63 V |
| 2009 | 4822 124 22027 | 47 μF | 25 V |
| 2010 | 4822 122 31759 | 22 nF |  |
| 2011 | 4822 122 31644 | 2.2 nF |  |
| 2012 | 4822 122 31966 | 27 pF |  |
| 2013 | 4822 122 31966 | 27 pF |  |
| 2014 | 4822 122 32976 | 470 pF |  |
| 2015 | 4822 122 32976 | 470 pF |  |
| 2016 | 4822 122 32975 | 33 pF |  |
| 2017 | 4822 122 32975 | 33 pF |  |
| 2018 | 4822 122 33009 | 270 nF | 25 V |
| 2019 | 4822 122 31644 | 2.2 nF |  |
| 2020 | 4822 122 32482 | 22 pF |  |
| 2021 | 4822 122 32482 | 22 pF |  |
| 2023 | 4822 124 22028 | 1 μF | 63 V |
| 2101 | 4822 122 31759 | 22 nF |  |
| 2102 | 4822 122 31759 | 22 nF |  |
| 2103 | 4822 122 31759 | 22 nF |  |
| 2104 | 4822 122 31759 | 22 nF |  |
| 2105 | 4822 122 31759 | 22 nF |  |
| 2106 | 4822 122 31759 | 22 nF |  |
| 2107 | 4822 122 31759 | 22 nF |  |
| 2108 | 4822 122 31759 | 22 nF |  |
| 2109 | 4822 122 31759 | 22 nF |  |
| 2110 | 4822 122 31759 | 22 nF |  |
| 2111 | 4822 122 31759 | 22 nF |  |
| 2112 | 4822 122 31759 | 22 nF |  |
| 2113 | 4822 122 31759 | 22 nF |  |
| 2114 | 4822 122 31759 | 22 nF |  |
| 2115 | 4822 122 31759 | 22 nF |  |
| 2116 | 4822 122 31759 | 22 nF |  |
| 2117 | 4822 122 31759 | 22 nF |  |

## Firmware

Two programmable devices sit on this board: the `CONTROL` EPROM at IC7202 and
the 8041 slave processor at IC7211.

| Program | SW rev. | Introduced | Philips sum16 | Service code number |
| --- | --- | --- | --- | --- |
| 3104 103 6804.4 | 1.4 | 1986-10-30 | `1F53` | 4822 209 51256 |
| 3104 103 6804.5 | 1.5 | 1986-11-24 | `2B55` | 4822 209 51256 |
| 3104 103 6804.6 | 1.6 | 1987-02-09 | `5D44` | 4822 209 51256 |
| 3104 103 6804.7 | 1.7 | 1987-02-23 | `C699` | 4822 209 51256 |
| 3104 103 6804.9 | 1.8 | 1987-03-19 | `6728` | 4822 209 51256 |

IC7211 is a **NEC D8041AHC** UPI-41 slave, carrying one RS232 and two RC5
I/Os. The manual gives it no program number.

What changed at each `CONTROL` release is on
[software releases](../../service-information/software-releases.md). **Of the
five releases, only 6804.9 is in the collection** — sum16 `0x6728`, held twice
over — and it is on the [firmware](../../reference/firmware.md) page with its
size and SHA-256.

!!! warning "Open question: the module S and module W 8041 dumps are the same image"

    Every VP415 8041 slave-CPU dump in the collection this site is built from —
    eight files, saved under both **module S Control** and **module W CPU**
    names — decodes to the **same 1 KB image**: Philips sum16 `0xFC62`,
    SHA-256 `35d258eb…`.

    That has two possible explanations, and the files cannot settle which:

    - modules S and W genuinely share the same UPI-41 firmware, or
    - one dump was saved under both names at some point, and the other
      device's image was never captured.

    Neither is presented here as fact. **If you have a VP415 to hand, reading
    the 8041 on module W and comparing it against `0xFC62` would settle it.**
    The same note is on [module W](../w-cpu-data-grabber/index.md) and on the
    [firmware](../../reference/firmware.md) page. A separate VP410 module S
    dump *is* a different image (sum16 `0xC014`), which at least shows the two
    machines do not share one.

## Modification levels

The module shipped at level 3 and reached **level 8** in the last production
batch — the widest span of any module, and almost all of it firmware.

- **Correction to the service manual**, applying at every level — R3005
  10 k → 8k2, R3006 47 k → 10 k, R3012 10 k → 2k7.
- **Level 6** — EPROM IC7202 `CONTROL` 6804.4 → **6804.5**.
- **Level 7** — EPROM IC7202 `CONTROL` 6804.5 → **6804.6**.

The mod-level sheet stops at level 7; the survey shows level 8 in the last
batch, and the software survey shows `CONTROL` reaching 6804.9. Read the
EPROM label, not the board revision, if it matters.

Full tables, with service code numbers:
[chapter 8, module S](../../service-information/modification-levels.md#mod-s).

## Related

- [Software releases](../../service-information/software-releases.md) — what changed in `CONTROL` 6804.4 through 6804.9
- [Firmware](../../reference/firmware.md) — dumps with sizes, Philips sums and SHA-256
- [Module circuit descriptions](../../circuit-description/modules.md#module-s) — the chapter 7 text in full
- [Module W — CPU + data grabber](../w-cpu-data-grabber/index.md) — the other end of the local bus, and the other 8041
- [Modification levels per module](../../service-information/modification-levels.md#mod-s) — the firmware steps
- [SCSI operation](../../operating-instructions/scsi-operation.md) — what the host end of this interface looks like
- [Fault-finding charts](../../repair/fault-finding.md) — communication faults start here
- [Electrical parts](../../parts/electrical-parts.md) — the collective list of standard components by service code number; the connectors are in [mechanical parts](../../parts/mechanical-parts.md#module-connectors)
