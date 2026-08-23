---
title: Error 7 - not in focus
description: >-
  Tracing an error 7 through the focus start-up handshake on module J, and the
  mis-printed transistor pinout the investigation turned up on the way.
---

# Error 7 — not in focus

An error 7 on a real player, followed from the code back through the focus
handshake to the amplifier that drives the objective coil. It is also where the
**6210 / 6211 pinout erratum** on
[module J](../../modules/j-focus/index.md) was found — which is the most useful
thing to come out of it, and the reason a half-finished investigation is worth
publishing.

!!! info "What error 7 means"

    [Error 007](../error-codes.md#error-7) is fatal: *not in focus after 5x (no
    rotation of disc)*. The drive processor gives the focus servo five attempts
    to pull the objective into focus before the disc is allowed to spin. Five
    failures and it stops here — the disc never turns, which is exactly what a
    dead focus loop looks like from the outside.

    [Fault-finding chart 2](../fault-finding.md) sends an error 7 to: clean the
    objective, then [R](../../modules/r-drive-processor/index.md),
    [J](../../modules/j-focus/index.md), [Z](../../modules/z-deck-electronics/index.md).

## The handshake, and what to probe

Four signals do the whole job, and all four are on the module J connector, so a
single probe on `J1` sees the entire sequence:

| Pin | Signal | Direction | Meaning |
| --- | --- | --- | --- |
| `7J1` | `FOC-EN` | [R](../../modules/r-drive-processor/index.md) → J | Focus enable; +12 V enables the loop |
| `2J1` | `FPI` | [deck](../../modules/z-deck-electronics/index.md) → J | Focus position indication; −12 V = in position |
| `1J1` | `FOC-ER` | [deck](../../modules/z-deck-electronics/index.md) → J | Focus error, from the four-quadrant detector |
| `5J1` / `4J1` | `FOCACT` | J → objective coil | The drive to the coil itself |
| `6J1` | `FOC-IND` | J → [R](../../modules/r-drive-processor/index.md) | In-focus indication; 0 V = in focus |
| `9J1` | | | Ground, for all of the above |

The sequence the drive processor runs, and what each step should look like:

1. At start-up `FOC-EN` is **low** and `FPI` is **high**.
2. The laser comes on. The drive checks `FOC-IND` = 1 — out of focus, as it
   should be before a search — and takes `FOC-EN` **high** to enable the loop.
3. Module J sweeps the objective. When focus is found, `FPI` goes **low**.
4. `FOC-IND` should then go **low** too, and the disc is allowed to spin.

**If `FOC-IND` never goes low, the attempt has failed.** Five of those and the
drive raises error 7.

## Test 1 — is the player asking for focus at all?

With module J out of the rack, so that only the drive processor's own outputs
are on the connector:

| Measurement | Result |
| --- | --- |
| `FOC-EN` and `FPI` at power-up | `FOC-EN` low, `FPI` high — **correct** |
| `FOC-EN` through a diagnostic start-up | Goes **low → high five times** — the five attempts, exactly as specified |
| `FPI` through the same | **High throughout, never goes low** |

So the drive processor is behaving perfectly: it asks for focus five times and
is never told focus was found. The fault is downstream of `FOC-EN` — in module
J, in the objective coil, or in the deck electronics that generate `FOC-ER` and
`FPI`.

<figure class="sheet sheet--photo" markdown>
[![Three-channel scope trace from power-up through diagnostic mode: FOC-EN pulsing high five times, !FPI going high and staying high, FOC-ER showing bursts of activity during each attempt](assets/web/error-7-focus-module-j-test-from-startup-to-fail-in-diagnostic-mode-preview.webp)](assets/web/error-7-focus-module-j-test-from-startup-to-fail-in-diagnostic-mode-zoom.webp)
<figcaption>
  The whole failure in one capture, 2 s per division: <code>FOC-EN</code>
  (top) pulsing five times, <code>!FPI</code> (middle) high and staying high,
  <code>FOC-ER</code> (bottom) alive with activity while the five attempts
  run, and flat either side of them.
  <span class="src">error 7 investigation, 1 April 2017</span>
</figcaption>
</figure>

## Test 2 — is anything reaching the objective coil?

`FOCACT` leaves module J on `5J1`, returns on `4J1`, and the objective coil
sits between them. Two things were checked: the coil, and the amplifier.

**The coil is fine.** Continuity from `5J1` and from `4J1` to the coil in the
laser detection unit is good on both sides — **under 0.5 Ω** — and the coil
itself measures **10 Ω**.

**The amplifier is not doing anything.** With the player running its diagnostic
start-up:

| Test point | Expected | Measured |
| --- | --- | --- |
| Collectors of the output pair 6210 / 6211 | Drive, either polarity, on each attempt | **0 V, no activity** |
| Pin 7 of 7001-2B — the op-amp feeding them | Swinging with the search | **7 V, no variation** |
| D of 6206, the focus loop switch JFET | Following the loop | **No variation at 500 mV/div** |
| S of 6206 | | Variation in the 1–2 V range |
| G of 6206 | | Variation in the 1–2 V range |

There is signal at the JFET's gate and source and nothing at its drain, and the
op-amp behind it sits at a fixed 7 V.

<figure class="sheet sheet--photo" markdown>
[![Scope trace of the drain, source and gate of JFET 6206 through a diagnostic start-up: all three step up together, the source and gate showing small variation, the drain flat](assets/web/error-7-focus-module-j-dsg-of-6206-preview.webp)](assets/web/error-7-focus-module-j-dsg-of-6206-zoom.webp)
<figcaption>
  D, S and G of 6206 — the focus loop switch — from power-on through
  diagnostics, 1 V per division.
  <span class="src">error 7 investigation, 1 April 2017</span>
</figcaption>
</figure>

<figure class="sheet sheet--photo" markdown>
[![Scope trace of pin 5 and pin 6 of op-amp 7001-2B with FOC-ER: pin 5 flat, pin 6 stepping up and holding, FOC-ER noisy during the search](assets/web/error-7-focus-module-j-test-foc-er-and-pins5-6-7001-preview.webp)](assets/web/error-7-focus-module-j-test-foc-er-and-pins5-6-7001-zoom.webp)
<figcaption>
  <code>FOC-ER</code> against pins 5 and 6 of 7001-2B (MC1458P1), the op-amp
  that drives the output stage.
  <span class="src">error 7 investigation, 1 April 2017</span>
</figcaption>
</figure>

## The focus error signal is small

`CS 6 876` sketches `FOC-ER` at `1J1` as a burst about **7 V** tall lasting
some **2 ms** — the objective being swept past the focal point. On this player
it measured **1.81 V peak-to-peak**.

<figure class="sheet sheet--photo" markdown>
[![Scope trace of FOC-ER at the module J input: a noisy signal measuring 1.81 volts peak to peak at 500 millivolts per division](assets/web/error-7-focus-foc-er-input-to-module-j-preview.webp)](assets/web/error-7-focus-foc-er-input-to-module-j-zoom.webp)
<figcaption>
  <code>FOC-ER</code> arriving at module J — 1.81 V peak-to-peak where the
  circuit diagram sketches about 7 V.
  <span class="src">error 7 investigation, 31 March 2017</span>
</figcaption>
</figure>

Whether that is a cause or a consequence is the open question of this
investigation. A focus error signal that small can be a deck problem — a dirty
objective, a weak laser, a mis-set focus gain on
[module Z](../../modules/z-deck-electronics/index.md) — or it can be what you
see when the objective is barely being moved, because the amplifier that should
move it is dead.

## The erratum

!!! danger "The service manual prints the 6210 / 6211 pinout wrong"

    The manual gives the pinout of 6210 and 6211 as **BCE**. It should be
    **ECB**. Both are power transistors in a plastic package — `CS 6 876` at
    300 dpi identifies them as a **BD436 / BD437** complementary pair — and
    they are the last stage before the objective coil. Fitted to the printed
    order the focus amplifier cannot work, and the parts may not survive being
    powered.

    Anyone who has replaced these transistors on the strength of the printed
    pinout has a focus amplifier that will never work and a player that reports
    error 7. That is worth checking before going any further.

    The erratum is carried on the [module J page](../../modules/j-focus/index.md)
    as well.

## What was replaced, and what it changed

| Done | Result |
| --- | --- |
| JFETs replaced with NTE312 — 6205, 6206 and one more (see below) | No change |
| Every BC848 and BC858 on the board replaced | No change |
| All capacitors checked | All good |
| 3003 checked | Good |

!!! note "The third JFET was 6011, not 6211"

    The notes list the replaced JFETs as *6205, 6206 and 6211*. Module J has
    exactly three JFETs, all BC264C: **6205** (the gain switch), **6206** (the
    focus loop switch) and **6011**. 6211 is the BD437 of the output pair — a
    power transistor, which an NTE312 could not stand in for. Read as **6011**,
    the list is the three JFETs on the board, so that is almost certainly what
    was meant.

## Where the investigation stopped

The record ends part-way through tracing pins 5, 6 and 7 of 7001, with the
heading written and no result under it. So this is a diagnosis in progress, not
a repair:

- **Confirmed working** — the drive processor's side of the handshake, the
  objective coil and its wiring, every capacitor on module J, and the small
  signal transistors.
- **Confirmed not working** — nothing reaching the objective coil: the output
  pair idle, 7001-2B stuck at 7 V, no variation at the drain of 6206.
- **Suspicious but unresolved** — `FOC-ER` at a quarter of the amplitude the
  circuit diagram sketches.

The next steps are the ones the notes were reaching for: measure pins 5, 6 and
7 of 7001 against the diagram's own DC conditions, check the ±12 V rails at
3057 and 3060 — both 2Ω2 fuse resistors — and **check the orientation of 6210
and 6211 before anything else**, because that is the one failure mode this
board is known to have.

## Related

- [Meaning of the error codes](../error-codes.md#error-7) — where the code comes from
- [Fault-finding charts](../fault-finding.md) — the start-up chart error 7 comes out of
- [Module J — Focus](../../modules/j-focus/index.md) — the board, the erratum,
  and `CS 6 876`
- [Module R — Drive processor](../../modules/r-drive-processor/index.md) —
  where `FOC-EN` comes from and `FOC-IND` goes
- [Module Z — Deck electronics](../../modules/z-deck-electronics/index.md) —
  where `FOC-ER` and `FPI` come from
- [Signal listing](../../system/signal-listing.md) — every mnemonic above
- [Error 9 — frame lock](error-9-frame-lock.md) — the other case study
