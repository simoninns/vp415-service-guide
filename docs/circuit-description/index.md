---
title: Circuit description
description: >-
  Chapter 7 of the service manual: how the LaserVision system works, how the
  optical deck works, how the player is architected, and how each module works.
---

# Circuit description

Chapter 7 is the *why*. Everywhere else in the manual tells you what to
measure; this chapter tells you what the circuit is trying to do. It is a
separate publication bound into the manual, titled *Circuit Description* and
published by Service Consumer Electronics for the **LaserVision ROM disc drive
VP415/00/05/35**.

| Page | Manual | What it covers |
| --- | --- | --- |
| [The LaserVision system](laservision-system.md) | 126–128 | Pits, encoding, CAV and CLV, the codes in the frame blanking, focusing, radial tracking, time base correction, genlock |
| [The optical deck](optical-deck.md) | 129–131 | What is on the deck, the Laser Detection Unit, Active Tilt Control |
| [VP400 series architecture](vp400-series.md) | 132–138 | The audio/video signal path, the control routes, the start-up sequence, the S-bus, the servo block diagram |
| [Module circuit descriptions](modules.md) | 139–163 | Twenty-five module descriptions, A through Z |

## The manual's own contents

The chapter's contents page gives page numbers within the circuit description
booklet, not the service manual. They are reproduced here because circuit
diagrams cross-reference them.

=== "1. The LaserVision system"

    | Section | Booklet page |
    | --- | --- |
    | Introduction | 1 |
    | Encoding of the signals on the disc | 1 |
    | Focusing | 2 |
    | Radial tracking | 3 |
    | Time base correction | 3 |
    | Genlock | 3 |
    | The optical deck | 5 |

=== "2. VP400 series"

    | Section | Booklet page |
    | --- | --- |
    | Introduction | 7 |
    | Block diagram audio/video signal path | 7 |
    | Control routes + start-up sequence | 9 |
    | S-bus | 9 |
    | Block diagram servo | 11 |

=== "3. Module description"

    | Module | Booklet page |
    | --- | --- |
    | A : Audio processing | 13 |
    | B : RGB processing | 14 |
    | C : Video processing | 15 |
    | D : Reference source | 16 |
    | E : Slide drive | 17 |
    | F : Motor + sequence | 17 |
    | G : Genlock | 18 |
    | H : Electronic time base correction B | 19 |
    | I : Electronic time base correction C | 20 |
    | J : Focus drive | 22 |
    | K : H.F. processing | 22 |
    | L : Video drop-out correction | 23 |
    | M : Radial drive | 24 |
    | N : Display + keyboard | 24 |
    | P : Front loader | 25 |
    | R : Drive processor | 25 |
    | S : Control processor | 26 |
    | T : Supply | 26 |
    | Ua : Analog I/O, CVBS + audio part | 27 |
    | Ub : Analog I/O, video part | 28 |
    | Uc : Analog I/O, TXT part | 29 |
    | W : Data grabber and CPU | 30 |
    | X : LV-ROM decoder | 34 |
    | Y : Video mixing | 36 |
    | Z : Deck electronics | 37 |

<figure class="sheet" markdown>
[![Circuit description title page for the LaserVision ROM disc drive VP415/00/05/35, with the three-chapter contents listing the LaserVision system, the VP400 series, and the module descriptions](assets/web/cs-7-874-text-p125-preview.webp)](assets/web/cs-7-874-text-p125-zoom.webp)
<figcaption>
  Circuit description — title page and contents.
  <span class="cs">CS 7 874</span>
  <span class="src">service manual page 125</span>
</figcaption>
</figure>

??? note "Chapter divider — service manual page 118"

    <figure class="sheet" markdown>
    [![Chapter 7 divider: circuit description](assets/web/divider-p118-preview.webp)](assets/web/divider-p118-zoom.webp)
    <figcaption>
      Chapter 7 divider.
      <span class="src">service manual page 118</span>
    </figcaption>
    </figure>
