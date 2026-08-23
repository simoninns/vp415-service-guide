---
title: Maintenance
description: >-
  Section 8 of the user manual: care of the player and of discs, and the
  trouble-symptom table with its possible causes.
---

# Maintenance

Section 8 of the operating instructions, page 43. Two paragraphs of care, and a
symptom table that is the user manual's equivalent of the service manual's
fault-finding charts — and a sensible thing to run through before opening
anything.

## Care of the player

The player requires no special maintenance. It is, however, advisable to
**clean the objective lens from time to time with a piece of wadding dipped in
alcohol**.

!!! danger "Cleaning the objective means opening the deck"

    Reaching the objective lens is not a front-panel operation, and the deck
    carries a **class 1 laser** whose supply must be treated with respect. Read
    [warnings](../general-service/warnings.md) and
    [demounting](../general-service/demounting.md) first, and note that the
    manual's own fault-finding for an
    [error 7](../repair/case-studies/error-7-focus.md) starts with *clean the
    objective* for exactly this reason.

## Care of discs

No special care is needed in handling discs. For best results, keep the playing
surface clean and free from dust and grease. When cleaning is required, gently
wipe the disc surface with a **soft, dry cloth. Use no solvents.**

Always remove discs after playing and replace them in their protective jackets.
Store them **vertically**, in their original jackets, away from extreme heat or
moisture, and out of direct sunlight.

## Trouble symptoms and possible causes

=== "Nothing works"

    **Disc does not rotate, no indicators light up**

    - The **automatic overload protection circuit** is in operation. Switch the
      player off at the rear, wait approximately **30 seconds**, then switch on
      again.

    **Disc does not rotate**

    - Check that the player is receiving power — the `STANDBY` indicator should
      be lit.
    - Check that the disc-tray is properly closed.

=== "Picture"

    **Disc rotates but the picture is weak or absent**

    - Check the connection between monitor and player.
    - Check that the disc is loaded correctly, **label up**. Some discs have
      programme content on one side only.
    - Press the `SEARCH ▶` button.
    - The player may be in pause: press `PLAY ▶`.

    **Player sticks at a particular point on the disc**

    - Press `SEARCH ▶` momentarily to skip over the affected part.
    - Remove the disc and wipe both surfaces clean with a soft, dry cloth to
      remove possible opaque surface marks.

    **Unstable still picture**

    - If still pictures taken from a fast-moving scene sometimes flicker,
      **this is not a fault of the player**: it results from the programme
      material the disc was made from.

=== "Sound and special effects"

    **Special effects — still, slow, reverse, fast — do not function**

    - Check that a **CAV** disc is being played. On CLV discs the special-effects
      buttons do not function.

    **Good picture but no sound**

    - Make sure the player is in **forward play**; in every other mode there is
      no sound.
    - Check that `AUDIO 1` and/or `AUDIO 2` are switched on — the indicators
      should be lit.
    - On an **LV-ROM disc there may be data, and therefore no sound**, on the
      disc. Try a non-LV-ROM disc.

=== "Controls"

    **Digit buttons are inoperative**

    - Check whether the picture number or chapter number is displayed on the
      monitor. If not, press `PNR` or `CNR` — the digits only mean something
      when a number is on screen.

    **Remote control does not function correctly**

    - Check that the `RC IR/EURO` switch on the rear is set to `IR`.
    - Keep the distance between player and handset to **no more than 10 m**.
    - Aim the handset at the front of the player with no obstacle in the way.
    - Check the batteries.
    - **If the player is in replay mode, most controls are disabled** — see
      [replay](special-play-functions.md#replay).

=== "Under computer control"

    **The player fails to respond when under computer control**

    - Check the connections to the relevant interface.
    - Ensure that **data in and data out are the right way round** (RS232-C).
    - Check that the `DTR` signal from the player is being received by the
      computer (RS232-C).
    - To reset, press the `ON/STANDBY` button on the front of the player.

    It is sometimes possible for the microprocessor in the player to *lock up*
    if it receives spurious or corrupted data. **Switch the player off for a few
    seconds**; this resets the microcomputer to its correct state.

!!! tip "When the symptom table runs out"

    Everything above is what an owner can do without a screwdriver. Past that
    point the player will tell you what is wrong itself: hold `STAND-BY` while
    switching on at the rear and it reports a two-digit
    [error code](../repair/error-codes.md) — see
    [the diagnostic software](../repair/diagnostic-mode.md).

## The printed pages

<figure class="sheet" markdown>
[![Section 8 divider listing maintenance, care of the player, care of discs, trouble symptoms, and the technical data subsections with their page numbers](assets/web/operating-instructions-scan-24-a-preview.webp)](assets/web/operating-instructions-scan-24-a-zoom.webp)
<figcaption>
  Section 8 divider and contents.
  <span class="src">operating instructions page 42</span>
</figcaption>
</figure>

<figure class="sheet" markdown>
[![Page covering care of the player, care of discs, and the full trouble symptoms table from a disc that will not rotate to a player that will not respond to a computer](assets/web/operating-instructions-scan-23-a-preview.webp)](assets/web/operating-instructions-scan-23-a-zoom.webp)
<figcaption>
  Maintenance and the trouble-symptom table.
  <span class="src">operating instructions page 43</span>
</figcaption>
</figure>

## Related

- [Technical data](technical-data.md) — the rest of section 8
- [Fault symptoms](../service-information/fault-symptoms.md) — the service
  manual's own symptom table, at component level
- [The diagnostic software](../repair/diagnostic-mode.md) — how to get an error
  code out of the player
- [General service → service hints](../general-service/service-hints.md) — what
  a service engineer is told to check
