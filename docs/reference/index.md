---
title: Reference
description: >-
  Material with no service manual equivalent: firmware dumps with checksums,
  the F-code command set, and the files worth downloading.
---

# Reference

The service manual describes a player Philips was still building. This section
holds what has been learned about it since, and what only exists because
somebody dumped a ROM, drove the player from a computer, or wrote down what a
real disc answered.

<div class="grid cards" markdown>

-   :material-memory: **Firmware**

    ---

    Every ROM and microcontroller dump in the collection: **28 files, 11
    distinct images**, with sizes, Philips 16-bit sums, SHA-256 hashes and
    downloads. Including two things the files themselves make plain and the
    manual does not.

    [:octicons-arrow-right-24: Firmware](firmware.md)

-   :material-console: **F-codes**

    ---

    The complete command set for driving a VP415 from a computer, what the
    player sends back, and the status responses a real player gave for each
    Domesday disc side.

    [:octicons-arrow-right-24: F-codes](f-codes.md)

-   :material-download: **Downloads**

    ---

    The eleven firmware images, one file each, with the checksum to verify
    them against.

    [:octicons-arrow-right-24: Downloads](downloads.md)

</div>

## Elsewhere on the site

Two more pieces of original work live with the material they belong to rather
than here:

- **[Repair case studies](../repair/case-studies/index.md)** — an error 7 and
  an error 9 traced on a real player, with the scope traces. They sit with the
  [repair method](../repair/index.md) chapter, beside the error codes they
  start from.
- **The module J erratum** — the service manual prints the 6210 / 6211 pinout
  as BCE when it should be ECB. It is on the
  [module J page](../modules/j-focus/index.md), where somebody about to replace
  those transistors will meet it.

## What is not published

- **PDF files.** The site serves no PDFs. The operating instructions are
  published as [their own section](../operating-instructions/index.md),
  transcribed with the page scans as figures; the NEC, Intel and Fujitsu
  datasheets are named by part number on the [firmware](firmware.md) page.
- **The archival originals.** Every scan is served as a web derivative that
  zooms to full resolution; the lossless 300 dpi files behind them stay in the
  repository.
