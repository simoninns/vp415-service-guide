---
description: >-
  A working repair and servicing reference for the Philips VP415 LaserVision
  ROM disc drive, built around the original Philips service manual.
hide:
  - navigation
---

# Philips VP415 service guide

<figure class="sheet sheet--photo hero" markdown>
[![A LaserVision disc spinning on the optical deck of an opened VP415](assets/web/title-picture-preview.webp)](assets/web/title-picture-zoom.webp)
<figcaption>
  A LaserVision ROM disc on the deck of an opened VP415, sandwich removed.
</figcaption>
</figure>

The **Philips VP415** is a LaserVision ROM disc drive: a 12-inch videodisc player
with a SCSI interface, built in 1986 so that a computer could drive it. It is the
player at the heart of the **BBC Domesday Project** — the machine that read the
two Domesday discs under the control of a BBC Master AIV. It plays video like any
LaserVision player, and it also reads data tracks off the same disc and returns
them over SCSI.

This site is a servicing reference for that player. It is built around the
**Philips VP415 service manual** — 197 sheets covering technical data, the
twenty-six plug-in modules A to Z, circuit descriptions, parts lists, the
diagnostic software and its error codes — with the scans, the transcribed text
and the original Philips `CS` sheet codes kept together on every page.

!!! danger "Read this before you open the player"

    **Laser radiation.** The VP415 is a Class 1 laser product, and that
    classification holds only while the cabinet is closed. With the cabinet open
    and the interlocks defeated, the objective emits an invisible beam that can
    damage your eyesight. Never look into the objective lens or at the disc
    surface while the laser is on, and never defeat an interlock unless the
    procedure you are following requires it.

    **Mains.** The supply module (module T) is a switched-mode supply that runs
    directly off the mains. Its primary side and its reservoir capacitors stay
    live and charged after the player is unplugged. Treat the whole of module T
    as live.

    **Static.** Several modules carry MOS devices that ESD will destroy silently.
    Work earthed. See [service hints](general-service/service-hints.md).

## Where to start

If you know what the player is doing wrong but not which chapter deals with it,
start at **[where do I start?](start-here.md)** — a symptom-by-symptom router
into the rest of the site.

<div class="grid cards" markdown>

-   :material-alert-circle-outline: **The player reports an error code**

    ---

    Read the code out of the diagnostic software, look up what it means, then
    follow the fault-finding chart for it.

    [:octicons-arrow-right-24: Repair method](repair/index.md)

-   :material-chip: **You know which module is at fault**

    ---

    One page per module: photographs, circuit description, adjustments, circuit
    diagram, PCB lay-out, parts and modification levels.

    [:octicons-arrow-right-24: Modules A to Z](modules/index.md)

-   :material-screwdriver: **You need to take it apart**

    ---

    Demounting order, the service tools, the exploded views and the part
    numbers that go with them.

    [:octicons-arrow-right-24: General service](general-service/index.md)

-   :material-tune: **You need to set it up**

    ---

    The manual's adjustment procedures, module by module, and the general rules
    for what to re-adjust after replacing a board.

    [:octicons-arrow-right-24: Adjustments](general-service/adjustments.md)

-   :material-console: **You want to drive it from a computer**

    ---

    The F-code command set over RS232-C, or LV-DOS over SCSI — the interface
    the Domesday system was built on, with the responses a real player gives.

    [:octicons-arrow-right-24: F-codes](reference/f-codes.md)

</div>

## What is here

The eight chapters of the service manual, each as its own section:

| Section | Manual | What it covers |
| --- | --- | --- |
| [Overview](overview/index.md) | chapter 1 | Technical data, controls, connector pinning |
| [General service](general-service/index.md) | chapter 2 | Warnings, adjustments, demounting, tools, symbols |
| [System lay-out](system/index.md) | chapter 3 | Module lay-out, signal listing, wiring and block diagrams |
| [Modules](modules/index.md) | chapter 4 | The twenty-six modules, A to Z, and the remote control |
| [Parts](parts/index.md) | chapter 5 | Exploded views, mechanical and electrical parts lists |
| [Repair method](repair/index.md) | chapter 6 | Diagnostic software, error codes, fault-finding charts |
| [Circuit description](circuit-description/index.md) | chapter 7 | How the system, the deck and each module work |
| [Service information](service-information/index.md) | chapter 8 | Modification levels, software releases, fault symptoms |

And two sections the service manual does not have:

- **[Operating instructions](operating-instructions/index.md)** — the *user*
  manual, kept deliberately separate so the two are never confused. F-code
  programming and SCSI operation live here.
- **[Reference](reference/index.md)** — firmware dumps with checksums, the
  F-code command set, and the files worth downloading. The
  [repair case studies](repair/case-studies/index.md) sit with the repair
  method chapter, beside the error codes they start from.

## How the pages are put together

Every page that comes from the service manual carries three things: the
transcribed text, the scan it was transcribed from, and the identity of the
original sheet. Philips gave each drawing a code in its bottom-right corner —
`CS 6 876` is the module J circuit diagram, `CS 7 846` its data sheet — and
those codes are printed under every figure alongside the page number in the
manual, so a reader with the paper manual can find the same sheet in seconds.

Click any scan to open it full size. Circuit diagrams, PCB lay-outs and
photographs open at the resolution they were captured at, so a fold-out
schematic is readable down to the component reference. The lossless 300 dpi
originals are not served by the site, but they are in the repository, one file
per sheet, for anyone who wants them.

!!! success "Every page is written"

    The whole service manual — the seven non-module chapters and all twenty-six
    [module pages](modules/index.md) — the
    [operating instructions](operating-instructions/index.md) in full, and the
    [reference](reference/index.md) section: firmware with checksums, the
    F-code command set, and two
    [repair case studies](repair/case-studies/index.md) traced on a real player.

    The pages are cross-linked in both directions: every
    [error code](repair/error-codes.md) names the modules to look at, every
    [signal mnemonic](system/signal-listing.md) names the modules that carry
    it, and every module page reaches its circuit description, its modification
    levels and its parts.

    What remains is the corrections that come from people using it at a bench,
    and the repairs they write up. Both are welcome —
    [contributing](contributing.md) has the templates and a worked example.
