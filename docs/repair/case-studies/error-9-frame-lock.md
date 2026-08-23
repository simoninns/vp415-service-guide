---
title: Error 9 - frame lock
description: >-
  Tracing an error 9 through the reference source, genlock and timebase
  correction chain, with the scope traces measured at each pin of module G.
---

# Error 9 — frame lock

The last test in the start-up chart, and a worked example of how to use it: an
error 9 on a real player, traced signal by signal through
[gen lock module G](../../modules/g-genlock/index.md) until one output stopped
where it should not have.

!!! info "What error 9 means"

    [Error 009](../error-codes.md#error-9) is fatal, and it is raised by the
    last step of [fault-finding chart 2](../fault-finding.md): the motor has
    reached nominal speed, and the drive processor then looks for `FRLOCK` = 1.
    If the disc will not lock in frame to the reference, the player stops here.

    The chart sends you to [module F](../../modules/f-motor-sequence/index.md).
    That is where the motor is driven from, but it is not the only place the
    lock can fail, and it was not where this fault was.

## The player and the symptom

A VP415 in diagnostic self-test mode, disc up to speed, reporting **error 9**.
Nothing else in the chart had failed, so focus, laser, tilt and motor speed
were all good; only the frame lock was missing.

## Where to look first

Frame lock is not one module's job. The disc's own line and frame pulses are
recovered from the video, compared against the internal sync generator, and the
answer is used to pull the disc's speed about — so the loop runs through
several boards, and any of them can break it:

| Module | Part in the loop |
| --- | --- |
| [D — reference source](../../modules/d-reference-source/index.md) | The sync generator everything is locked to |
| [G — gen lock](../../modules/g-genlock/index.md) | Compares disc timing against the reference and produces `MCO` |
| [F — motor + sequence](../../modules/f-motor-sequence/index.md) | Turns `MCO` into motor drive |
| [L — video dropout correction](../../modules/l-video-dropout-correction/index.md) | Supplies `CV-DOC`, the corrected video the timing is recovered from |

The investigation started from the signals the drive processor itself watches,
because those are what set `FRLOCK`:

| Into [module R](../../modules/r-drive-processor/index.md) | What it should be |
| --- | --- |
| `FRLOCK` | Frame lock, +5 V when locked |
| `HMANCH` | Horizontal sync, negative pulses |
| `VMANCH` | Vertical sync, negative pulses |
| `CL-VID` | Clipped video, 0 V / +12 V |

and the signals either side of module G:

| Signal | Direction | What it is |
| --- | --- | --- |
| `REFH` | [D](../../modules/d-reference-source/index.md) → G | Horizontal reference, positive pulses |
| `FI` | [D](../../modules/d-reference-source/index.md) → G | Field identification |
| `DEM-BK` | G → [H](../../modules/h-etbc-b/index.md) | Demodulator burst key, positive pulses |
| `DO-INH` | G → [H](../../modules/h-etbc-b/index.md) | Drop-out protection inhibit, +12 V = active |
| `CV-DOC` | [L](../../modules/l-video-dropout-correction/index.md) → G | Video, drop-out corrected |

All of these are in the [alphabetical signal listing](../../system/signal-listing.md).

!!! tip "The circuit diagram tells you what to expect"

    `CS 6 873` — the [module G circuit diagram](../../modules/g-genlock/index.md)
    — carries a red waveform sketch beside each connector pin: amplitude and
    period, drawn at the pin. **That is what makes this fault findable**, and
    every "expected" figure in the tables below is read off it, not guessed:
    8 V / 40 ms at `1G1`, 8 V / 64 μs at `2G1`, 2.8 V on a 6 V pedestal at
    `3G2`, 4 V / 0.22 μs at `6G1`, 4 V / 64 μs at `8G1`, 12 V / 20 ms at `6G2`.

## Testing module G, pin by pin

Every measurement below is on the module in the player, disc running, taken
with a Keysight MSO-X 3104T.

### `1G1` — field identification

| | |
| --- | --- |
| Expected | 8 V square wave, 40 ms period |
| Measured | **9.2 V peak-to-peak, 40.001 ms, 24.999 Hz** |
| Verdict | Good — this is the 25 Hz field rate, so the reference source is alive |

<figure class="sheet sheet--photo" markdown>
[![Scope trace at pin 1G1: a clean square wave, 9.2 volts peak to peak, period 40.001 milliseconds, measured at 24.999 hertz](assets/web/error-9-frame-lock-module-g-1g1-preview.webp)](assets/web/error-9-frame-lock-module-g-1g1-zoom.webp)
<figcaption>
  <code>1G1</code>, field identification — 40 ms, the field rate.
  <span class="src">error 9 investigation, 1 April 2017</span>
</figcaption>
</figure>

### `2G1` — `REFH`, horizontal reference

| | |
| --- | --- |
| Expected | 8 V square wave, 64 μs period |
| Measured | **9.0 V peak-to-peak, 64.000 μs, 15.625 kHz** |
| Verdict | Good — the line reference is exactly on frequency |

<figure class="sheet sheet--photo" markdown>
[![Scope trace at pin 2G1: narrow positive pulses 9 volts peak to peak with a period of 64 microseconds, 15.625 kilohertz](assets/web/error-9-frame-lock-module-g-2g1-preview.webp)](assets/web/error-9-frame-lock-module-g-2g1-zoom.webp)
<figcaption>
  <code>2G1</code>, <code>REFH</code> — 64 μs, the line rate.
  <span class="src">error 9 investigation, 1 April 2017</span>
</figcaption>
</figure>

### `3G2` — `CV-DOC`, the video coming in

| | |
| --- | --- |
| Expected | 2.8 V peak-to-peak burst on a 6 V pedestal, 64 μs line |
| Measured | cursors 74.1 μs apart, **ΔY 3.35 V** — one line plus a little, burst and picture content both present |
| Verdict | Good — the video module L feeds in is there |

<figure class="sheet sheet--photo" markdown>
[![Scope trace at pin 3G2: a video line with colour burst and active picture content, cursors reading 3.345 volts between them](assets/web/error-9-frame-lock-module-g-3g2-preview.webp)](assets/web/error-9-frame-lock-module-g-3g2-zoom.webp)
<figcaption>
  <code>3G2</code>, <code>CV-DOC</code> — video off the disc, drop-out
  corrected, arriving at the gen lock module.
  <span class="src">error 9 investigation, 1 April 2017</span>
</figcaption>
</figure>

### `6G1` — `GL-CL`, the genlock clock

| | |
| --- | --- |
| Expected | 4 V, 0.22 μs pulses — the 4.5 MHz VCO |
| Measured | **3.5 V peak-to-peak, 229.4 ns, 4.359 MHz** |
| Verdict | Running, and close to the 4.5 MHz centre frequency L5001 sets |

<figure class="sheet sheet--photo" markdown>
[![Scope trace at pin 6G1: a 4.359 megahertz clock, 3.5 volts peak to peak, period 229.4 nanoseconds](assets/web/error-9-frame-lock-module-g-6g1-preview.webp)](assets/web/error-9-frame-lock-module-g-6g1-zoom.webp)
<figcaption>
  <code>6G1</code>, <code>GL-CL</code> — the 4.5 MHz genlock clock.
  <span class="src">error 9 investigation, 1 April 2017</span>
</figcaption>
</figure>

The same clock at the emitter of 7014 measured **4.554 MHz, 219.6 ns**, which
is the buffered `GLC` on its way to the counter chain.

<figure class="sheet sheet--photo" markdown>
[![Scope trace at the emitter of transistor 7014: the same clock at 4.554 megahertz, 3.5 volts peak to peak](assets/web/error-9-frame-lock-module-g-e-7014-preview.webp)](assets/web/error-9-frame-lock-module-g-e-7014-zoom.webp)
<figcaption>
  Emitter of 7014 — the buffered genlock clock.
  <span class="src">error 9 investigation, 1 April 2017</span>
</figcaption>
</figure>

### `8G1` — `MCO`, motor control out

| | |
| --- | --- |
| Expected | 4 V, 64 μs, duty cycle proportional to the speed error |
| Measured | **4.1 V**, and the duty cycle wandering — 34 μs high in the marked interval |
| Verdict | Present. A wandering duty cycle is what an unlocked loop looks like: the module is still asking the motor to hurry up and slow down |

<figure class="sheet sheet--photo" markdown>
[![Scope trace at pin 8G1: a 4.1 volt pulse train whose mark-space ratio changes from line to line, cursors 34 microseconds apart](assets/web/error-9-frame-lock-module-g-8g1-preview.webp)](assets/web/error-9-frame-lock-module-g-8g1-zoom.webp)
<figcaption>
  <code>8G1</code>, <code>MCO</code> — the motor control output, duty cycle
  unsettled.
  <span class="src">error 9 investigation, 1 April 2017</span>
</figcaption>
</figure>

### `6G2` — `DO-INH`, drop-out inhibit

| | |
| --- | --- |
| Expected | 12 V, 20 ms |
| Measured | Narrow pulses at the field rate on an otherwise flat line |
| Verdict | Present |

<figure class="sheet sheet--photo" markdown>
[![Scope trace at pin 6G2: narrow spikes at the field rate on a flat baseline, 5 volts per division, 20 milliseconds per division](assets/web/error-9-frame-lock-module-g-6g2-preview.webp)](assets/web/error-9-frame-lock-module-g-6g2-zoom.webp)
<figcaption>
  <code>6G2</code>, <code>DO-INH</code> — drop-out inhibit, at the field rate.
  <span class="src">error 9 investigation, 1 April 2017</span>
</figcaption>
</figure>

## Where it stopped: IC7206-2A

The pins that carry the line pulses out of the sync separator go through
IC7206-2A. The circuit diagram wants **12 V peak-to-peak at 64 μs on both**,
`LPO` positive on pin 6 and `LPO'` inverted on pin 7.

| Pin | Expected | Measured |
| --- | --- | --- |
| 6 | 12 V p-p, 64 μs, positive | **0 V, stable** |
| 7 | 12 V p-p, 64 μs, inverted | **11.15 V, no activity** |

Both with and without a disc. That is the fault: **no `LPO` or `LPO'` coming
out of module G**. Every input to the module is good and the clock is running,
but the line pulses that the phase comparison depends on never leave it, so the
disc can never be pulled into frame lock and `FRLOCK` never goes high.

## The supply rails

The module's supplies come in through NFR25 fuse resistors — the small values
in the bottom left corner of `CS 6 873` — and they were checked next:

| Fuse resistor | Value | Rail | Result |
| --- | --- | --- | --- |
| 3051 | 4Ω7 | +5 V → +5A | OK |
| 3001 | 6Ω8 | +12 V → +12A | **fail** |
| 3004 | 4Ω7 | +12 V → +12C | measured |
| 3081 | 470 Ω | +12 V → +12B | OK |
| 3056 | 15 Ω | +12 V → +12D | OK — **14.6 Ω** measured in circuit |
| 3002 | 4Ω7 | −12 V → −12A | OK |

!!! warning "Two facts that have to be reconciled"

    The rail check marks **3001, the 6Ω8 feeding +12A, as failing** — and pin 7
    of IC7206-2A was nevertheless sitting at 11.15 V, which is not what a dead
    supply rail looks like.

    Both measurements are recorded here as they were taken. Which is right
    decides the repair: an open fuse resistor is a five-minute job, a dead
    HEF4538 is a desolder. **Measure the voltage on both supply pins of
    IC7206-2A before ordering anything**, and check 3001 out of circuit —
    a 6Ω8 in parallel with the rest of the board reads low from either side.

## Where the investigation stopped

The written record ends with the rail measurements. The module was not
replaced, and no "after" trace was taken, so this case study proves a
diagnosis rather than a repair:

- **Ruled out** — the reference source (`1G1`, `2G1` both exact), the video
  path into the module (`3G2`), the VCO (`6G1`, 7014), the outputs that do
  work (`8G1`, `6G2`).
- **Found** — `LPO` / `LPO'` missing at IC7206-2A, which is inside module G and
  downstream of everything that measured good.
- **Left open** — whether IC7206-2A itself has failed or is starved of its
  supply through 3001.

The next two measurements, in order, are the supply pins of IC7206-2A and
3001 lifted at one end.

!!! note "Why the chart's answer was not the answer"

    Fault-finding chart 2 sends an error 9 to
    [module F](../../modules/f-motor-sequence/index.md), and module F was
    innocent: it was being asked to do the right thing by an `MCO` that could
    never settle. The chart is pointing at the *last* board in the loop, not
    the first place to look — which is worth remembering for every code in it.

## Related

- [Meaning of the error codes](../error-codes.md#error-9) — where the code comes from
- [Fault-finding charts](../fault-finding.md) — the start-up chart this ends
- [Module G — Gen lock](../../modules/g-genlock/index.md) — the board, its
  circuit description and `CS 6 873`
- [Module D — Reference source](../../modules/d-reference-source/index.md) —
  where `REFH` and `FI` come from
- [Module L — Video dropout correction](../../modules/l-video-dropout-correction/index.md) —
  where `CV-DOC` comes from
- [Signal listing](../../system/signal-listing.md) — every mnemonic above
- [Error 7 — not in focus](error-7-focus.md) — the other case study
