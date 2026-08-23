---
title: SCSI operation
description: >-
  Section 7 of the user manual: LV-DOS, volumes and logic units, the SCSI
  command set, sense codes, F-codes over SCSI, and the address switches.
---

# SCSI operation

Section 7 of the operating instructions, pages 37 to 41. **This is the section
that made the BBC Domesday system possible**: the VP415 is not only a video
player but a 324 Mbyte read-only disc drive that answers on a SCSI bus, and
this is its programming interface.

## Introduction

The VP415 contains a microprocessor to access the data on a LaserVision disc
and make it available to an industry standard **SCSI** (Small Computer System
Interface). The interface connects the player — the **target** — to a host
computer — the **initiator** — allowing the host to read data from the disc as
well as providing the usual player control functions. The software running in
the player's microprocessor is called **LV-DOS**, and it is with LV-DOS that
the host communicates.

A LaserVision disc has a storage capacity of 324 Mbytes, subdivided into a
number of **volumes** managed by LV-DOS:

```
 ┌─────────────────────────────┐
 │ System table for LV-DOS     │   internal to LV-DOS
 ├─────────────────────────────┤
 │ Volume directory            │   one entry per volume
 ├─────────────────────────────┤
 │ Volume 'JIM'                │
 ├─────────────────────────────┤
 │ Volume 'HENRY'              │   300 Mbytes
 └─────────────────────────────┘
```

The system table holds information for LV-DOS's own use; the volume directory
holds an entry per volume giving its name, its whereabouts on the disc and some
control information. The volumes themselves hold whatever an application
developer put in them — **LV-DOS does not manipulate that data and does not
care what format it is in**.

Blocks are not interleaved: consecutive logical blocks are in consecutive
physical order, interleave value 1. Detection and correction of errors is
carried out entirely by the LV-DOS firmware, so **data transferred to the
initiator is error free**. The pre-mastering system must supply all the data to
be mastered onto the disc, including the system table and volume directory.

## Volumes

Each disc side holds 54 000 pictures and 324 Mbytes of data. To divide that
capacity — and to allow more than one independent interactive application on a
side — the concept of volumes was adopted. **It is entirely transparent to the
host**, which talks in logical pictures and logical blocks; LV-DOS translates
those to physical ones.

After the initiator sends a **start-unit** command, LV-DOS reads the physical
location of each volume's data and pictures from the disc, and the volumes are
automatically opened, provided the relevant digital data can be read.

Volumes are accessible as **logic units**. The SCSI command format allows 8
logic units, and LV-DOS supports up to **7 volumes** (excluding the directory
volume):

| Logic unit | What it is |
| --- | --- |
| 0 – 6 | The volumes, in the order they appear in the volume directory. Unused units are closed by definition |
| 7 | Absolute F-code read/write, and access to the volume directory |

## The SCSI interface

The SCSI interface is usually used to connect a microcomputer to floppy or
Winchester disc drives. It is a bussed system of a very general nature that
makes few assumptions about the equipment connected, which suits LV-DOS: it
allows player control commands and disc data to travel over the same physical
link.

Only what is needed to use the interface with a VP415 is covered here; the full
standard is **ANSI X3T9.2**.

A transaction between one initiator and the player runs through these phases:

| Phase | What happens |
| --- | --- |
| **Arbitration** | The host gains control of the bus. Only necessary to allow for multiple initiators; if it fails, another device has the bus and the host must wait and retry |
| **Selection** | The host outputs the player's SCSI address — each device has a unique address 0 to 7 — and waits for a response. If it fails, *no response from player* must go back to the higher-level software |
| **Command** | The host sends a command descriptor block: the command, plus any additional information such as the block number to read |
| **Data in / data out** | Where appropriate, the requested data is transferred. **On a read there may be a delay of several seconds** before data is available, and both parties must usually know in advance how much is to be transferred |
| **Status** | The player returns a single byte saying whether the command succeeded |
| **Message** | The player sends *command complete* before releasing the bus. Required by the standard, but of no use to LV-DOS, since all its operations are synchronous |

### VP415 issues

The VP415 SCSI interface adheres strictly to the SCSI specification in both
hardware and software.

- The bus cable is **daisy-chained in single-ended mode**; parity is ignored.
- **`TERMPWR` is not connected** to an internal supply.
- All bus phases are supported **except the optional reselection and message-out
  phases**, and arbitrary systems with multiple initiators are supported.
- The **hard reset** condition is supported.
- **Asynchronous transfer is the default**; optional synchronous transfer and
  linked commands are *not* supported.

The logic unit number in the command descriptor block selects which volume the
command applies to — rather like specifying one of several floppy drives on a
controller. **Logic unit 7 is used for all commands that do not pertain to a
particular volume**, including reading the volume directory. A logic unit number
is assigned to a volume when it is opened.

## Default conditions

### After start-up

At power-up or reset the system is in standby. To log the disc onto LV-DOS an
initial **start-unit** command should be issued before any other SCSI command —
though if the first command after a hard reset is a **read**, the start-unit
function is performed automatically first.

After a successful start-unit the player is in this default mode:

| | |
| --- | --- |
| Audio | **off** |
| Remote control handset | on |
| Index display | off |
| Normal video | on |
| Video mode | **VP3** — hard-keyed |
| Front panel controls | enabled |
| Search mode | **R1** — fast read |

F-code commands issued to logic unit 7 are executed fully transparently; those
issued to other logic units apply to the volume associated with that unit.

If the disc has no digital data — a CLV or a CAV disc without data — or the
automatic start-unit fails for any reason, the player is reset to the F-code
default conditions and fully transparent F-code control is possible through all
logic units.

!!! tip "VP3 even on failure, so you can say so on screen"

    If start-unit is given over SCSI **the video mode will be VP3 even if the
    command fails** — deliberately, so that the host computer can display an
    error message over whatever the player is showing.

### After stop-unit

A **stop-unit** command is received as an *unload* at the VP415, and all
switches are reset to their default values, as with the F-code
[reset to default](f-code-commands.md#the-tray-standby-and-reset). It is the initiator's
job to send an eject command if one is needed. After stop-unit **all volumes
are closed**; a subsequent start-unit is needed to open them again.

## LV-DOS commands

LV-DOS supports all mandatory commands for read-only direct-access devices,
some extended commands, and some vendor-unique commands. **The command and
reply formats are a subset of the general SCSI definition.**

The first field in a command descriptor block is a **group code**, 0 to 7,
which defines the format of the rest of the command. LV-DOS supports **group 0**
for reading disc data and **group 6** (vendor-unique) for F-code read and write.

### The status byte

A single status byte comes back on completion of every command. LV-DOS uses
this subset of the standard's meanings:

| Bit | Meaning |
| --- | --- |
| 0 | Reserved, 0 |
| **1** | **Command failed — check sense status** |
| 2–7 | Reserved, 0 |

A return value of 0 means the command succeeded. Anything else, and the host
should issue **request sense** for the details.

### Group 0 — the 6-byte commands

| Byte | Bits 7–5 | Bits 4–0 |
| --- | --- | --- |
| 0 | Group code (0) | Command code |
| 1 | Logic unit number | Logical block address (MSB) |
| 2 | Logical block address | |
| 3 | Logical block address (LSB) | |
| 4 | Number of data blocks to transfer (transfer length) | |
| 5 | Control byte (0) | |

The group code and command code together form the **operation code**. The
logical block address applies only to read and write; for other commands it is
meaningless and should be zero. The vendor-unique bits, reserved bits, flag bit
and link bit in the control byte are not supported and should be zero. **There
is no data phase unless stated.**

| Operation code | Command |
| --- | --- |
| `00H` | Test unit ready |
| `01H` | Rezero unit |
| `08H` | Read |
| `0AH` | Write |
| `1BH` | Start/stop unit |
| `03H` | Request sense |

#### `00H` — test unit ready

Verifies that the player is running, the disc is logged in, and the player is
ready for commands through the selected logic unit. **Status 0** if the volume
associated with that logic unit is open; **`02H`** if the unit is not open or
the target is not ready.

#### `01H` — rezero unit

Displays **logical picture zero** of the volume accessed through the command's
logic unit. Status 0 on success, `02H` otherwise.

#### `08H` — read

Reads blocks of data from the disc. The block number of the first block is a
**logical** block address relative to the beginning of the selected volume's
data; LV-DOS adds the offset to the physical location, making it transparent to
the initiator. A data-in phase is required.

Status 0 on success, `02H` otherwise — a subsequent request sense reveals *unit
not ready*, *media error* and so on.

!!! note "Read moves the picture, and the search mode decides how"

    In search mode **R1** this command switches the video **off**, because after
    a search the system stops at a random picture — and also if the requested
    data was in cache. In search mode **R0** the video is only muted during data
    retrieval, after which the previously displayed picture returns. See
    [search modes](#search-modes).

#### `0AH` — write

Implemented as a **dummy**: nothing is written to the medium. It exists so that
operating systems which date-stamp files on access do not produce error
messages, and so that drivers written for read/write media work without
patching. A data-out phase is required unless the number of blocks is zero.

#### `1BH` — start/stop unit

Bit 0 of byte 1 = 1. **Bit 0 of byte 4 is 1 for start-unit and 0 for
stop-unit.**

**Stop-unit** logs the disc off, closes the volumes, and puts the player into
standby with all switches at their defaults. It is always executed without error
status, and an eject command is needed as well if the disc is to be changed.

**Start-unit** logs a disc on: the system table is read and the volumes opened.
Status 0 on success; `02H` otherwise, with sense key 2 (*unit not ready*) if the
drive is physically not ready, or 3 (*media error*) if the drive is spinning but
no data can be read.

**These commands are mandatory when the media is changed.** They can be issued
to any logic unit, open or closed.

#### `03H` — request sense

Returns more detailed information about the previous command to the specified
logic unit, successful or not. **Sense data is maintained separately for each
logic unit**, and this command can be issued to any unit and is always executed
without error status. A data-in phase is required. The fourth command byte —
the allocation length — should be set to zero, and non-extended sense data of
**4 bytes** is returned:

| Byte | Bits |
| --- | --- |
| 0 | Valid · error class (0) · error code |
| 1 | Logic unit number · logical block address (MSB) |
| 2 | Logical block address |
| 3 | Logical block address (LSB) |

The **valid** bit is 1 if the logical block address bytes are meaningful — that
is, they show the block where the error occurred.

| Code | Sense | Means |
| --- | --- | --- |
| `0` | No error | The previous command was carried out correctly |
| `2` | Unit not ready | No volume is associated with the specified logic unit after a test-unit-ready, read or write; or a start-unit failed because the drive is physically not ready — no disc, not spinning |
| `3` | Media error | Data cannot be read: after start-unit on a CLV or CAV disc without digital data, or on reading a **non-data area of a mixed disc** — one carrying data and analogue audio |
| `4` | Hardware error | A hardware error detected in the system |
| `5` | Illegal request | An illegal or non-existent command, including illegal bits within a command |
| `B` | Command aborted | The target aborted the command |
| `D` | Volume exceeded | An attempt to read outside the volume, or a block number beyond the volume's length |

### Group 6 — the vendor-unique commands

| Byte | Contents |
| --- | --- |
| 0 | Group code · command code |
| 1 | Logic unit number · not used (0) |
| 2 | Not used (0) |
| 3 | Not used (0) |
| 4 | Number of data blocks to transfer (1) |
| 5 | Control byte (0) |

!!! warning "The manual prints the group code as (0) in this table"

    Byte 0 of the group 6 table is labelled **`Group code (0)`** — copied from
    the group 0 table above it and not corrected. It cannot be 0: the operation
    codes given immediately below are `CAH` and `C8H`, and the top three bits of
    both are `110`, which is **group 6**. Build the descriptor block from the
    operation code, not from the table's label.

| Operation code | Command |
| --- | --- |
| `CAH` | Write F-code command |
| `C8H` | Read F-code reply |

F-code commands allow the initiator to control the player over the same bus.
Some return an acknowledgement or reply code, some almost immediately and some
up to several seconds later.

#### `CAH` — write F-code command

Writes an [F-code](../reference/f-codes.md) to a specific logic unit. A data-out
phase is required, in which the F-code is sent **terminated by `CR` and null
padded to the end of the block**.

**Picture numbers in the F-code are logical picture numbers**, numbered from
zero at the beginning of the picture volume; LV-DOS adds the offset to the
physical picture address. This is what allows an LV-ROM application to be placed
anywhere on a new disc without changing the retrieval programs on the initiator.

Three consequences worth having in front of you:

- **Chapter numbers are not translated** — only picture numbers are. Goto
  picture commands get a modified number; chapter commands do not.
- **`?F` returns the physical picture number**, not the logical one, to avoid
  negative picture numbers or numbers beyond the volume boundary.
- Access to a logic unit with **no volume** associated is *not* an error: it
  lets the initiator control ordinary video discs, with LV-DOS fully
  transparent and picture numbers unmodified.

!!! important "Read the reply before sending the next command"

    If an F-code reply is needed it must be read **before another F-code command
    is issued to the same logic unit**. Otherwise the reply is lost.

#### `C8H` — read F-code reply

Reads the reply code from the reply buffer for the specified logic unit. The
reply is terminated by `CR` and null padded to the end of the block; **if there
is no reply, the first character of the block is `CR`**. A data-in phase is
necessary.

Reading the buffer clears it, and LV-DOS keeps a separate reply buffer per logic
unit. This command is the group 0 read with a vendor-unique operation code, a
transfer length of one block and a logical address of zero.

### Search modes

Two commands control how digital data is fetched from the disc:

| Command | Mode | Behaviour |
| --- | --- | --- |
| `R0` | **Slow read** | Returns to the picture displayed immediately before the read: LV-DOS reads the current picture number, does the transfer, and searches back. Video is switched **on** after the search |
| `R1` | **Fast read** | Stops at the position where the data was read. Video is switched **off** after the search. **The power-on default** |

`R` = 82D = 52H, no response. The two commands toggle between the modes. Fast
read gives higher performance; slow read may be more convenient in a
multi-initiator environment.

## Special issues

### SCSI address setting

Every device on the bus needs a unique address, 0 to 7. **If the address is not
the one the host expects, the VP415 will not be recognised. The factory setting
is address 0.**

The address is set on the `SCSI ADDRESS` dip switches at the rear of the player.
**A switch in the up position is OFF.** Switches 1 to 4 and switch 8 should be
off; switches 5 to 7 set the address:

| Address | Switch 5 | Switch 6 | Switch 7 |
| --- | --- | --- | --- |
| 0 | off | off | off |
| 1 | off | off | on |
| 2 | off | on | off |
| 3 | off | on | on |
| 4 | on | off | off |
| 5 | on | off | on |
| 6 | on | on | off |
| 7 | on | on | on |

### Condition after start-unit

Successful execution of start-unit **always brings the system to the same
condition**, regardless of what went before.

### Initiator powered off

If an initiator connected to the bus is not powered up, it is possible that the
reset line will be pulled active low, leaving LV-DOS in its reset condition. It
will then not take control of the player, **which behaves as if there were no
controller at all**.

### Loss of sync

Anything that affects the sync signal the player is genlocked to — a change of
video mode, for instance — makes the player re-genlock by changing the disc
speed. **During a speed change the tolerances for reading digital data can be
exceeded**, so the system may retry, or register a media error.

### Retries

LV-DOS will make a number of retries itself where necessary. It is very unlikely
that an unsuccessful command will succeed on a retry from the host, so **the
initiator is advised not to retry** a failed command.

### Two computers trying to take control

The RS232-C interface can also control the player, and **the player can only
listen to one channel at a time**. If two systems try to control it at once, the
SCSI initiator may lose control, and any subsequent command except mode-select
F-codes is then ignored.

Initiator control is resumed by issuing a **start-unit** to LV-DOS. That command
may come back with *media error* or *unit not ready*, but either way the SCSI
initiator now has control.

### Changing a disc under initiator control

1. Issue **stop-unit**, then **eject**.
2. Poll the player status with the F-code `?P` and read the reply until it says
   the disc-tray is closed again.
3. Issue **start-unit** to log the disc on.
4. Optionally confirm with **test unit ready** — unnecessary if start-unit
   returned no error.
5. **Verify the identity of the disc** and set all the player modes your
   application needs.

## The printed pages

<figure class="sheet" markdown>
[![Section 7 divider listing the SCSI operation contents from introduction and volumes through the LV-DOS commands to the special issues](assets/web/operating-instructions-scan-22-b-preview.webp)](assets/web/operating-instructions-scan-22-b-zoom.webp)
<figcaption>
  Section 7 divider and contents.
  <span class="src">operating instructions page 36</span>
</figcaption>
</figure>

<figure class="sheet" markdown>
[![Page introducing LV-DOS, the disc structure diagram with system table, volume directory and volumes, the volume concept and logic units, and the SCSI bus phases](assets/web/operating-instructions-scan-21-b-preview.webp)](assets/web/operating-instructions-scan-21-b-zoom.webp)
<figcaption>
  Introduction, volumes and the SCSI interface.
  <span class="src">operating instructions page 37</span>
</figcaption>
</figure>

<figure class="sheet" markdown>
[![Page covering the VP415's SCSI implementation, default start-up and stop-unit conditions, the LV-DOS command set, the status byte and the group 0 command descriptor block](assets/web/operating-instructions-scan-22-a-preview.webp)](assets/web/operating-instructions-scan-22-a-zoom.webp)
<figcaption>
  VP415 issues, defaults and the group 0 command format.
  <span class="src">operating instructions page 38</span>
</figcaption>
</figure>

<figure class="sheet" markdown>
[![Page describing the six group 0 commands — test unit ready, rezero unit, read, write, start/stop unit and request sense — with the sense data format and error codes](assets/web/operating-instructions-scan-21-a-preview.webp)](assets/web/operating-instructions-scan-21-a-zoom.webp)
<figcaption>
  The group 0 commands and the sense data.
  <span class="src">operating instructions page 39</span>
</figcaption>
</figure>

<figure class="sheet" markdown>
[![Page with the remaining sense codes, the group 6 vendor-unique command format, the write F-code command and the read F-code reply command, and the search modes](assets/web/operating-instructions-scan-24-b-preview.webp)](assets/web/operating-instructions-scan-24-b-zoom.webp)
<figcaption>
  The group 6 vendor-unique commands and the search modes.
  <span class="src">operating instructions page 40</span>
</figcaption>
</figure>

<figure class="sheet" markdown>
[![Page covering fast read, the SCSI address dip switch settings as figure 10, and the special issues from initiator powered off to changing a disc under initiator control](assets/web/operating-instructions-scan-23-b-preview.webp)](assets/web/operating-instructions-scan-23-b-zoom.webp)
<figcaption>
  Fast read, the address switches and the special issues.
  <span class="src">operating instructions page 41</span>
</figcaption>
</figure>

## Related

- [F-codes](../reference/f-codes.md) — the commands carried by `CAH` and `C8H`
- [Interactive play](interactive-play.md) — choosing between SCSI and RS232-C
- [Module W — CPU and data grabber](../modules/w-cpu-data-grabber/index.md) —
  the board LV-DOS runs on
- [Module X — LV-ROM decoder](../modules/x-lv-rom-decoder/index.md) — where the
  digital data comes off the disc
- [Technical data](technical-data.md) — the SCSI interface specification and
  its termination
