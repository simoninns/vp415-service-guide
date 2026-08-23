---
title: Interactive play
description: >-
  Section 4 of the user manual: the two ways a computer can drive the player,
  and how to switch between them.
---

# Interactive play operation

Section 4 of the operating instructions, page 19. Short, and the hinge of the
whole book: **the player will talk to a computer over RS232-C or over SCSI, but
never both at once**, and this page is where that is settled.

## Introduction

Interactive operation requires a computer program. Virtually any computer with
an RS232-C or SCSI interface can control the VP415 using a high-level language
such as BASIC or PASCAL. Connect the host computer to the relevant socket at
the rear of the player and load the program in the usual way.

!!! important "One interface at a time"

    **It is not possible to control the player over both RS232-C and the SCSI
    bus simultaneously.** Mode selection is made by the master — the host
    computer; the player cannot make the choice itself.

    From power-up the player is in **F-code communication mode over RS232-C,
    with the SCSI bus switched off**.

## F-code operation via RS232-C

This mode is selected automatically by the player unless a **start-unit**
command is issued, as described in [SCSI operation](scsi-operation.md). The
player is in slave mode: it executes the commands received from the computer
and sends back confirmatory responses.

An F-code consists of one or more 8-bit bytes, coded in ASCII, terminated by a
carriage return.

### Mode selection

Only necessary if SCSI operation was selected and you now want RS232-C. The
protocol is below; **carriage returns are not sent** during it. `ACK` is a
positive acknowledgement `A` and `NACK` a negative acknowledgement `N`.

1. The master sends **two spaces**.
2. The master awaits `ACK` from the player. If it does not arrive within
   **200 ms**, retry.
3. The master sends the mode select byte for F-code communication, which is
   **`F`**.
4. The master awaits `ACK` from the player. If it does not arrive within
   200 ms, retry the mode selection.

## SCSI operation

SCSI operation provides communication between the player and the host computer,
allowing the VP415 to be used as an **LV-ROM memory device**. Both data
retrieval from the disc and control of the player are possible — and F-codes
can be sent over SCSI as well, as group 6 vendor-unique commands.

### Mode selection

SCSI mode is selected by issuing a **start-unit** command to the player. See
[SCSI operation](scsi-operation.md).

!!! info "This is what made Domesday work"

    The BBC Domesday system drove the player over SCSI from a BBC Master's
    co-processor, reading pictures and data off the same disc. The data side of
    that is [LV-ROM](introduction.md#types-of-laservision-disc) and the
    decoding is [module X](../modules/x-lv-rom-decoder/index.md) and
    [module W](../modules/w-cpu-data-grabber/index.md) in the service manual.

## The printed pages

<figure class="sheet" markdown>
[![Section 4 divider listing interactive play operation, introduction, F-code operation via RS232-C, mode selection, SCSI operation and mode selection, all on page 19](assets/web/operating-instructions-scan-10-a-preview.webp)](assets/web/operating-instructions-scan-10-a-zoom.webp)
<figcaption>
  Section 4 divider and contents.
  <span class="src">operating instructions page 18</span>
</figcaption>
</figure>

<figure class="sheet" markdown>
[![Page describing interactive operation, F-code operation over RS232-C with its four-step mode selection protocol, and SCSI operation selected by a start-unit command](assets/web/operating-instructions-scan-11-a-preview.webp)](assets/web/operating-instructions-scan-11-a-zoom.webp)
<figcaption>
  Interactive play operation.
  <span class="src">operating instructions page 19</span>
</figcaption>
</figure>

## Related

- [F-code programming](f-code-programming.md) — section 5: the RS232-C
  interface in detail
- [SCSI operation](scsi-operation.md) — section 7: the SCSI command set
- [F-codes](../reference/f-codes.md) — the command list as a reference
