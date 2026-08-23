---
title: Firmware
description: >-
  Every ROM and microcontroller dump in the collection: 28 files, 11 distinct
  images, with sizes, Philips 16-bit sums, SHA-256 hashes and downloads.
---

# Firmware

Every ROM and microcontroller dump the collection holds, published with enough
identity to be useful: the size, the address range, the **Philips 16-bit sum**
that the manual's own survey uses, the **SHA-256** of the image, and a link to
the file.

**There are 28 files and 11 distinct images.** The duplication is not an
accident of tidying — the same ROM was read more than once, years apart, and
saved under different names each time. Hashing them is the only way to see
that, so this page is organised by *image*: eleven pieces of firmware, with the
files that carry each one listed as aliases underneath.

!!! info "The checksum in the filename is a Philips sum, and it checks out"

    Fourteen of the files carry a checksum in their name — `…0x68FF.BIN`. It is
    a **16-bit sum of every byte in the image**, the same number the manual
    prints in its [survey of software releases](../service-information/software-releases.md).
    All fourteen match the sum computed here, 0 mismatches, which means anyone
    who dumps their own EPROM can identify it the same way:

    ```
    sum16 = sum(bytes) & 0xFFFF
    ```

## The eleven images

| # | Module | Device | Name | Program | SW rev. | Size | Philips sum16 | SHA-256 of the image | Files |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | [R](../modules/r-drive-processor/index.md) | IC7204 EPROM | DRIVE | 3104 103 6803.6 | 1.7 | 16 KB | `0x68FF` | `6ec09eeb8d4751b5…` | 4 |
| 2 | [S](../modules/s-control/index.md) | IC7202 EPROM | CONTROL | 3104 103 6804.9 | 1.8 | 64 KB | `0x6728` | `e372542baa52e57f…` | 2 |
| 3 | [S](../modules/s-control/index.md) / [W](../modules/w-cpu-data-grabber/index.md) | 8041 slave CPU | — | not given by the manual | — | 1 KB | `0xFC62` | `35d258eb1ee0bfab…` | 8 |
| 4 | [W](../modules/w-cpu-data-grabber/index.md) | IC7201 EPROM | SYNC | 3104 103 6808.0 | 1.0 | 16 KB | `0xD120` | `bc7eb8ca0f1e5d50…` | 3 |
| 5 | [W](../modules/w-cpu-data-grabber/index.md) | IC7224 EPROM | DESCR. | 3104 103 6807.0 | 1.0 | 16 KB | `0x1FBE` | `850498330a6d4920…` | 3 |
| 6 | [W](../modules/w-cpu-data-grabber/index.md) | IC7247 EPROM | LVDOS#1 | 3104 103 6805.2 | 1.3 | 16 KB | `0xB42D` | `d929bc98adcd200c…` | 2 |
| 7 | [W](../modules/w-cpu-data-grabber/index.md) | IC7247 EPROM | LVDOS#1 | 3104 103 6805.3 | 1.4 | 16 KB | `0x8F90` | `ecdd68a65ebe45ae…` | 1 |
| 8 | [W](../modules/w-cpu-data-grabber/index.md) | IC7248 EPROM | LVDOS#2 | 3104 103 6806.2 | 1.3 | 16 KB | `0x1A1C` | `e230f04b178c2533…` | 2 |
| 9 | [W](../modules/w-cpu-data-grabber/index.md) | IC7248 EPROM | LVDOS#2 | 3104 103 6806.3 | 1.4 | 16 KB | `0x56D7` | `d87e81e193f38593…` | 1 |
| 10 | VP410 S | EPROM | CONTROL A | 3104 103 6811.4 | — | 64 KB | `0xFC6F` | `9dee7647ab7480a4…` | 1 |
| 11 | VP410 S | 8041 slave CPU | — | not given by the manual | — | 1 KB | `0xC014` | `b061c815822c0e35…` | 1 |

The Intel HEX files are decoded before hashing, so a HEX dump and a raw binary
of the same ROM hash alike and land in the same row. The address range is
`0x0000` to the top of the image in every case: 16 KB for the 27128 EPROMs,
64 KB for the two 27512s, and 1 KB for the 8041s.

!!! warning "Open question: the module S and module W 8041 dumps are the same image"

    Image 3 is **eight files** — every VP415 8041 slave-CPU dump in the
    collection, saved under both *module S Control* and *module W CPU* names —
    and all eight decode to one 1 KB image, sum16 `0xFC62`,
    SHA-256 `35d258eb…`.

    Either [module S](../modules/s-control/index.md) and
    [module W](../modules/w-cpu-data-grabber/index.md) genuinely run the same
    UPI-41 bus-interface firmware, or one dump was saved under both names and
    the other device was never read. **The files cannot settle it** and neither
    reading is presented here as fact.

    Two details worth having: the larger 8,848-byte files are the same 1 KB
    image repeated three times, which is what reading a 1 K device in a larger
    socket produces; and the VP410 8041 (image 11, `0xC014`) *is* a different
    image, so the two machines at least do not share one.

    **If you have a VP415 to hand, reading the 8041 on module W and comparing
    it against `0xFC62` would close this.**

!!! danger "The manual prints `BF90` where the dump computes `8F90`"

    The [survey of software releases](../service-information/software-releases.md)
    gives the checksum of `LVDOS#1` 6805.3 (SW rev. 1.4) as **`BF90`**. Checked
    against the 300 dpi scan of `CS 8 284`, that is what the sheet says.

    The dump of that program in the collection computes **`0x8F90`**, and the
    person who made it put `0x8F90` in the filename — so the file agrees with
    itself, and it is the only one of the fourteen name-checksums that the
    manual contradicts.

    A typewriter `B` for an `8` in 1987 is the obvious explanation, but the
    other possibility — that the dumped image is not the 6805.3 the survey
    describes — cannot be ruled out from here. Compare against a known-good
    6805.3 EPROM if you have one.

## Every file

| Image | File | In the collection as | Size on disk | Checksum in the name |
| --- | --- | --- | --- | --- |
| 1 | [R](../modules/r-drive-processor/index.md) | IC7204 EPROM | DRIVE | 3104 103 6803.6 | 1.7 | 16 KB | `0x68FF` | `6ec09eeb8d4751b5…` | 4 |
| 2 | [S](../modules/s-control/index.md) | IC7202 EPROM | CONTROL | 3104 103 6804.9 | 1.8 | 64 KB | `0x6728` | `e372542baa52e57f…` | 2 |
| 3 | [S](../modules/s-control/index.md) / [W](../modules/w-cpu-data-grabber/index.md) | 8041 slave CPU | — | not given by the manual | — | 1 KB | `0xFC62` | `35d258eb1ee0bfab…` | 8 |
| 4 | [W](../modules/w-cpu-data-grabber/index.md) | IC7201 EPROM | SYNC | 3104 103 6808.0 | 1.0 | 16 KB | `0xD120` | `bc7eb8ca0f1e5d50…` | 3 |
| 5 | [W](../modules/w-cpu-data-grabber/index.md) | IC7224 EPROM | DESCR. | 3104 103 6807.0 | 1.0 | 16 KB | `0x1FBE` | `850498330a6d4920…` | 3 |
| 6 | [W](../modules/w-cpu-data-grabber/index.md) | IC7247 EPROM | LVDOS#1 | 3104 103 6805.2 | 1.3 | 16 KB | `0xB42D` | `d929bc98adcd200c…` | 2 |
| 7 | [W](../modules/w-cpu-data-grabber/index.md) | IC7247 EPROM | LVDOS#1 | 3104 103 6805.3 | 1.4 | 16 KB | `0x8F90` | `ecdd68a65ebe45ae…` | 1 |
| 8 | [W](../modules/w-cpu-data-grabber/index.md) | IC7248 EPROM | LVDOS#2 | 3104 103 6806.2 | 1.3 | 16 KB | `0x1A1C` | `e230f04b178c2533…` | 2 |
| 9 | [W](../modules/w-cpu-data-grabber/index.md) | IC7248 EPROM | LVDOS#2 | 3104 103 6806.3 | 1.4 | 16 KB | `0x56D7` | `d87e81e193f38593…` | 1 |
| 10 | VP410 S | EPROM | CONTROL A | 3104 103 6811.4 | — | 64 KB | `0xFC6F` | `9dee7647ab7480a4…` | 1 |
| 11 | VP410 S | 8041 slave CPU | — | not given by the manual | — | 1 KB | `0xC014` | `b061c815822c0e35…` | 1 |

## Every file

14 of the 28 files carry a checksum in the filename, and every one of them matches the sum computed here.

| Image | File | In the collection as | Size on disk | Checksum in the name |

Files are linked in the repository rather than served by the site: the archival
originals are deliberately kept out of the published build, and a ROM image is
something to fetch, not something to read in a browser. Everything on this page
is also in [firmware-checksums.csv](https://github.com/simoninns/vp415-service-guide/blob/main/planning/firmware-checksums.csv),
which carries the SHA-256 of both the file and the decoded image for all 28.

!!! note "Where the VP410 program number comes from"

    Image 10 is a VP410 board and its program number, **3104 103 6811.4**, is
    read off the filename of the dump. `CS 8 284` covers the VP410 as well as
    the VP415, but it does not list a 6811 anywhere, so treat that number as
    the dumper's, not Philips'.

## What the EPROMs do

| Image | Device | What it is |
| --- | --- | --- |
| `0x68FF` | [Module R](../modules/r-drive-processor/index.md) IC7204 | `DRIVE` — the drive processor's program, and the software the diagnostic mode is part of |
| `0x6728` | [Module S](../modules/s-control/index.md) IC7202 | `CONTROL` — the system controller, front panel, RS232 and RC5 |
| `0xFC62` | [S](../modules/s-control/index.md) / [W](../modules/w-cpu-data-grabber/index.md) 8041 | The UPI-41 slave that handles the serial and remote-control I/O |
| `0xD120` | [Module W](../modules/w-cpu-data-grabber/index.md) IC7201 | `SYNC` — the sequencer, called the sync detector on the board |
| `0x1FBE` | [Module W](../modules/w-cpu-data-grabber/index.md) IC7224 | `DESCR.` — the descrambler |
| `0xB42D`, `0x8F90` | [Module W](../modules/w-cpu-data-grabber/index.md) IC7247 | `LVDOS#1` — half of the LV-DOS program, rev 1.3 and 1.4 |
| `0x1A1C`, `0x56D7` | [Module W](../modules/w-cpu-data-grabber/index.md) IC7248 | `LVDOS#2` — the other half, rev 1.3 and 1.4 |

!!! important "The two LV-DOS EPROMs are a matched pair"

    `CS 8 284`'s own footnote: when the program number of the EPROMs in a set
    deviates from the latest, **order both service code numbers of LV-DOS** —
    4822 209 51261 and 4822 209 51262. Do not mix a 1.3 with a 1.4.

!!! quote "Provenance of the 6807 and 6808 images"

    The two module W images that are not LV-DOS came with a note from their
    dumper, kept in the collection as `Rom descriptions.txt`:

    > Here's the two ROM images you were after. "6807" is the descrambler
    > (marked as 7224 in your parts list) and "6808" is the sequencer (marked
    > as 7201 in your list).
    >
    > Hopefully they do what you need — I know there were a few releases of the
    > VP415 with various changes, so I'm not sure if there were tweaks done that
    > mean the firmware has to match up with the board!
    >
    > — Jules

    That identification agrees with the manual: `CS 8 284` puts `DESCR.` at item
    7224 and `SYNC` at item 7201. The caution in the second paragraph is fair —
    see the modification levels on the
    [module W page](../modules/w-cpu-data-grabber/index.md) for what changed
    around these devices.

## Which release is in a player

Two ways, neither needing a screwdriver on the EPROM itself:

- **Ask the player.** The `?=` F-code returns the software revision level —
  see [modification levels](../general-service/modification-levels.md) and the
  [F-code reference](f-codes.md).
- **Read the sum off the sticker** and look it up in the
  [survey of software releases](../service-information/software-releases.md),
  which lists every release Philips shipped, its date and its service code
  number. The survey lists **14 releases**; the collection holds dumps of
  **8 of them** — the last `DRIVE` and `CONTROL`, and all six module W EPROMs.
  The six missing images are the earlier `DRIVE` 6803.4 and 6803.5 and the
  earlier `CONTROL` 6804.4, .5, .6 and .7.

<figure class="sheet" markdown>
[![Survey of software releases VP410/415, upright: a table of every EPROM release with module, item number, name, program number 3104 103, software revision level, introduction date, checksum and service code number 4822 209](assets/web/cs-8-284-software-release-survey-upright-preview.webp)](assets/web/cs-8-284-software-release-survey-upright-zoom.webp)
<figcaption>
  Survey of software releases VP410/415 — every release Philips shipped, with
  the checksum of each. The manual binds this sheet sideways at page 187; this
  is the same sheet scanned upright, because a reader comparing checksums wants
  the table the right way up. The sheet in its place in the manual is on
  <a href="../../service-information/software-releases/">software releases</a>.
  <span class="cs">CS 8 284</span>
  <span class="src">service manual page 187</span>
</figcaption>
</figure>

## The processors

The devices themselves, for anyone reading a dump rather than replacing a chip:

| Device | Where | Notes |
| --- | --- | --- |
| **NEC D8041AHC** | [Module S](../modules/s-control/index.md) IC7211, and [module W](../modules/w-cpu-data-grabber/index.md) | UPI-41 slave microcontroller, 1 K masked-ROM program, 64 bytes of RAM. The Intel **D8741A** is the EPROM version of the same part |
| **TMS 27128** | [Module R](../modules/r-drive-processor/index.md) IC7204, [module W](../modules/w-cpu-data-grabber/index.md) IC7201, IC7224, IC7247, IC7248 | 16 KB EPROM — `DRIVE`, `SYNC`, `DESCR.` and the two LV-DOS devices. Service code 4822 209 71312, supplied **unprogrammed** |
| **TMS 27512** | [Module S](../modules/s-control/index.md) IC7202 | 64 KB EPROM — `CONTROL`. Service code 4822 209 71317, also supplied unprogrammed |
| **Fujitsu MB88303** | Not tied to a board by the manual | In the [electrical parts list](../parts/electrical-parts.md) as 4822 209 71278; the third datasheet in the collection |

!!! note "The datasheets are in the repository, not on the site"

    The collection holds the NEC D8041AHC, Intel D8741A and Fujitsu MB88303
    datasheets as PDFs. **The site does not serve PDF files**, so they are named
    here by part number rather than republished; the files are under
    `docs/reference/assets/originals/datasheets/` in the repository, and all
    three are common parts whose datasheets are widely mirrored.

## Related

- [Software releases](../service-information/software-releases.md) — chapter 8's
  survey and what changed at each revision
- [Module R](../modules/r-drive-processor/index.md) ·
  [Module S](../modules/s-control/index.md) ·
  [Module W](../modules/w-cpu-data-grabber/index.md) — the three boards with
  programmed devices
- [Modification levels](../general-service/modification-levels.md) — reading a
  set's software revision with `?=`
- [Downloads](downloads.md) — every downloadable original in one place
