---
title: Connections of semiconductors
description: >-
  Package pinouts for every transistor and FET type used in the VP415, with a
  type-to-package cross-reference.
---

# Connections of semiconductors

Which way round a transistor goes. The sheet gives the pin arrangement of every
package used in the set, then cross-references each type number to its package.

!!! info "Where this sheet sits in the manual"

    The manual's own contents page files *connections of semiconductors* under
    chapter 2, general service information — which is where this site puts it.
    In the binder the sheet is printed at the end of chapter 3, after the block
    diagrams, as service manual page 027.

## Package pinouts

**Read the view.** A TO-92 seen from below has its pins in the reverse order to
the same part seen from above, and the manual gives both. The right-hand block
of the figure is the top view — the one you want when the part is still on the
board.

| Package | Bottom view | Top view |
| --- | --- | --- |
| SOT-143 (SMD) | — | G1 G2 above, S D below |
| SOT-23 VAR.1 (SMD) | — | C above, B E below |
| SOT-23 VAR.2 (SMD) | — | C above, E B below |
| SOT-23 VAR.3 (SMD) | — | G above, D S below |
| TO-92 VAR.1 | B C E | E C B |
| TO-92 VAR.2 | E B C | C B E |
| TO-92 VAR.3 | B E C | C E B |
| TO-92 VAR.4 | D S G | G S D |
| TO-18, TO-72 | S D G, read from the tab | D S G, read from the tab |
| TO-39 | E B C, read from the tab | E B C, read from the tab |
| SOT-32 (TO-126), SOT-82, SOT-93, SOT-186 | B, C, E from the top down | B, C, E from the top down |

For the round metal cans — TO-18, TO-72 and TO-39 — the order depends on where
you start relative to the tab, so read them off the figure rather than the
table.

## Type to package

| Type | Package | | Type | Package |
| --- | --- | --- | --- | --- |
| BC264 | TO-92 VAR.4 | | BC849 | SOT-23 VAR.1 |
| BC327 | TO-92 VAR.2 | | BC858 | SOT-23 VAR.1 |
| BC337 | TO-92 VAR.2 | | BC859 | SOT-23 VAR.1 |
| BC368 | TO-92 VAR.1 | | BD135 | SOT-32 (TO-126) |
| BC369 | TO-92 VAR.1 | | BD434 | SOT-32 (TO-126) |
| BC375 | TO-92 VAR.2 | | BD435 | SOT-32 (TO-126) |
| BC376 | TO-92 VAR.2 | | BD436 | SOT-32 (TO-126) |
| BC546 | TO-92 VAR.2 | | BD437 | SOT-32 (TO-126) |
| BC547 | TO-92 VAR.2 | | BD438 | SOT-32 (TO-126) |
| BC548 | TO-92 VAR.2 | | BF256 | TO-92 VAR.4 |
| BC549 | TO-92 VAR.2 | | BF450 | TO-92 VAR.3 |
| BC556 | TO-92 VAR.2 | | BF494 | TO-92 VAR.3 |
| BC557 | TO-92 VAR.2 | | BF992 | SOT-143 |
| BC558 | TO-92 VAR.2 | | BFR30 | SOT-23 VAR.3 |
| BC639 | TO-92 VAR.1 | | BFR54 | TO-92 VAR.2 |
| BC640 | TO-92 VAR.1 | | BFS19 | SOT-23 VAR.1 |
| BC807 | SOT-23 VAR.1 | | BSD213 | TO-72 |
| BC817 | SOT-23 VAR.1 | | BSV78 | TO-18 |
| BC847 | SOT-23 VAR.1 | | BSV80 | TO-18 |
| BC848 | SOT-23 VAR.1 | | BSW68 | TO-39 |
| BUT11F | SOT-186 | | BUW85 | SOT-82 |
| BUW12 | SOT-93 | | BUX86 | SOT-32 (TO-126) |
| PH2369 | TO-92 VAR.2 | | | |

Service code numbers for these types are in the
[list of electrical parts](../parts/electrical-parts.md).

!!! note "BSV78"

    BSV78 appears in the manual's package-to-type column, under TO-18, but is
    missing from the type-to-package column. It is listed above as TO-18 on the
    strength of the first column.

<figure class="sheet" markdown>
[![Connections of semiconductors: package pinout diagrams for SOT-143, SOT-23, TO-92, TO-18, TO-72, TO-39, SOT-32, SOT-82, SOT-93 and SOT-186 in bottom and top views, followed by package-to-type and type-to-package cross-reference lists](assets/web/cs-8-121-figure-p027-preview.webp)](assets/web/cs-8-121-figure-p027-zoom.webp)
<figcaption>
  Connections of semiconductors.
  <span class="cs">CS 8 121</span>
  <span class="src">service manual page 027</span>
</figcaption>
</figure>
