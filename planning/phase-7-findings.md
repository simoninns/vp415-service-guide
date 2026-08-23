# Phase 7 — Cross-linking and polish: verification record

The phase that makes the pages reach each other: an error code that names the modules to look at, a
signal mnemonic that names the modules that carry it, a module page that reaches its circuit
description, its modification levels and its parts. Plus the machinery that keeps those links from
rotting — a figure checker, a generated index checked in CI, and a pull-request workflow.

---

## 1. What landed

| File | What |
| --- | --- |
| `tools/build_signal_index.py` | The *modules* column of the alphabetical signal listing, generated from the module pages and the chapter 7 circuit description. `--check` fails CI when it drifts |
| `tools/check_figures.py` | Alt text, captions, CS code and page number, and the preview → zoom pairing, on every figure on the site |
| `docs/start-here.md` | **Where do I start?** — a symptom-first router into the manual, second in the nav after Home |
| `docs/contributing.md` | What is wanted, how to build locally, and a worked example of adding a repair guide to a module page |
| `docs/system/signal-listing.md` | 243 rows gained a *modules* column; **135 mnemonics** credited to at least one module |
| `docs/repair/error-codes.md` | 77 rows gained a *where to look* column, with the basis for each stated |
| 26 module pages | Every **Related** list now reaches chapter 7, chapter 8 and the parts lists |
| `.github/workflows/check.yml` | `just check` on every pull request; a weekly external-link sweep |
| `.github/ISSUE_TEMPLATE/` · `pull_request_template.md` | Repair report, correction, and a PR template that asks which source page a change is based on |
| `justfile` | New `lint` recipe; `check` now depends on it |
| `mkdocs.yml` | Search separator tuned for punctuated mnemonics; `search.boost` on the pages that answer one |

`just check` — **14 823 links, 0 errors** (13 735 at the end of phase 6), `mkdocs build --strict`
clean, 295 images pass the figure checks.

## 2. The signal listing cannot be turned into a netlist

The phase's first bullet — *signal listing entries link to the modules that produce and consume
them* — assumes a machine-readable interconnection list. There is not one anywhere in the source
material:

- `CS 7 830`, the alphabetical signal listing, gives the mnemonic, the meaning and the active level.
  It never names a module.
- The two wiring diagrams, `CS 7 831` (player) and `CS 7 832` (sandwich), **do** name every module
  and pin — but they are fold-out scans. Their vendor OCR is three characters long: the page number
  and the sheet code.
- The module data sheets carry connector pin-outs, in the same form: printed on the drawing.

So the column is built the only way the material allows, and the page says so in as many words: **a
module is credited with a signal when that module's page, or that module's section of the chapter 7
circuit description, names the mnemonic.** It is an index of where a signal is *described*, not of
where it is wired.

Direction is carried where the material states it. Ten module pages have an `Out` or `Outputs to`
row in their summary table, written in phase 5 from the manual; the signals in those rows are marked
in bold as the source. That is **28 signals** with a direction, out of 135 credited.

### How the matching works, and what it deliberately misses

Normalisation drops everything but letters, digits, `/` and `+`, so `HF-OUT 1` on the listing finds
`HF-OUT1` in the prose and `COMM1` finds `COMM-1`. Beyond that:

- **Module pages** are this site's own prose and code-quote every mnemonic, so only backticked text
  is matched.
- **Chapter 7** is a transcription of the manual, which prints signal names as bare capitals in
  running text — *"the FRLOCK signal becomes active"*. Bare all-caps tokens of three characters or
  more are matched there as well. This is what took coverage from 105 signals to 135: `FRLOCK`,
  `TILTOK`, `SPI`, `MCES`, `RAD-FS` and 113 other mnemonics appear in the manual's prose and nowhere
  in a code span.
- **Ten mnemonics are never matched.** `B`, `G` and `R` are the video signals and also ordinary
  prose; `CS` is composite sync and also the Philips sheet code, as in *"no `CS` code printed"`*;
  `Q1`–`Q4` are the stepping-motor coils and also module Q's two connectors and module Y's decoder
  outputs. Every hit each of them produced was read in context before it was excluded, and each of
  those hits was a false positive.

The remaining 108 uncredited mnemonics are genuinely undiscussed: the RS232 handshakes (`CTS1-3`,
`DTR 1-3`, `RXD1-3`, `TXD1-3`), the SCART lines, the LED drives, the TTL video outputs. They appear
on the diagrams and nowhere else, which is what an empty cell means.

**A bug worth recording.** The first version mapped chapter 7 sections to module directories by
first letter, over a sorted list. `remote-control` sorts after `r-drive-processor`, so it won the
letter `r` — and module R's entire chapter 7 section was credited to the remote control handset.
Caught by reading the output: `REFV` had no business pointing at a handset. The remote control is
now excluded from the letter map.

## 3. `LA-STA` is printed `LA-STIA` once, on page 148

Module J's page said the drive module takes `FOC-EN` high once it has seen a disc reflection, a
correct slide position and *laser on (`LA-STIA`)*. There is no such signal. Across the vendor OCR
of the whole manual the spelling is `LA-STA` six times and `LA-STIA` twice, both of the latter on
**service manual page 148** — the chapter 7 circuit description of module J.

The manual's own text on that page is transcribed faithfully and keeps `LA-STIA`. Module J's
summary prose, which is this site's writing, now says `LA-STA`, and the signal index credits the
signal to J and Z as it should.

## 4. Chapter 8 says nothing changed on modules V and W; its own survey disagrees

The chapter 8 page carried the manual's explanation that modules D, E, N, P, Q, V, W and X have no
mod-level sheet because "nothing changed on them that needed documenting". The survey table
directly above it, `CS 8 264` / `CS 8 265`, shows:

| Module | First batch | Last batch |
| --- | --- | --- |
| D, E, N, P, Q, X | one level throughout | — |
| **V** — module carrier | 1 | **3** |
| **W** — CPU + data grabber | 2 | **3** |

Two modules changed level twice over and no sheet in the chapter says what changed. Both the
chapter 8 text and the two module pages now state that as an open gap rather than asserting that
nothing happened. It is the same class of finding as the phase 6 checksum contradiction: the
manual disagreeing with itself, published as such.

## 5. What the error-code column can and cannot claim

Chapter 6 attributes a module to a code in exactly two places:

- **Fault-finding chart ②** walks the start-up sequence and names the module to check at each of its
  nine steps — codes 1 to 9.
- **Fault-finding chart ①** sends an incorrect `REFH` / `REFV` to the reference source, which covers
  codes 25, 26, 27 and 30.

That is 13 of the 77 codes. For the rest the manual gives the code, the severity and a line of
description, and stops. The column is filled for another 46 of them from the function the code
names, traced through the chapter 7 circuit description and the signal listing — error 14 to the
front loader because `0-RPM` is a front-loader output, error 52 to the motor module because the code
is about the turntable tacho, and so on. The page marks the distinction in an admonition rather than
letting a reader assume the manual said it.

The remaining 18 are left blank on purpose: they report on the drive processor's own software or on
the disc, and naming a second module would be an invention. Every code on the page is raised by
module R, which the admonition says once rather than repeating it in 77 rows.

**The case for reading it sceptically is on the site already.** Chart ② sends an error 9 to module
F; the [error 9 case study](../docs/repair/case-studies/error-9-frame-lock.md) traced a real one to
module G, because frame lock is a loop through four boards and the chart names the last of them.
The error 9 row now carries D, G and L alongside the chart's F for exactly that reason.

## 6. Chapter 6 has two fault-finding charts, not four

The fault-finding page opened with *"Four flow charts: a top-level test procedure, and three trees
it branches into."* The chapter is five sheets: the test procedure (`CS 8 116`), chart ① for a
player that shows nothing (`CS 8 117`), and chart ② spread across three sheets (`CS 8 118`–`CS 8
120`). Three sheets of one chart were read as three charts. Corrected on the fault-finding page and
on the chapter 6 index.

## 7. Alt text and captions were already right

The figure checker was written expecting to find work. It found none: **295 images across 85 pages,
every one with alt text of substance, every figure with a caption, and every figure derived from a
manual sheet carrying its page number and — where the sheet has one — its Philips CS code.** The
photographs correctly carry no `src` span, because a photograph of a board is not a page of the
manual.

The checker is worth having anyway: it is now the rule rather than the habit, it runs in `just lint`
and so on every pull request, and it also verifies the thing a hand-written figure gets wrong most
easily — that the inline image is the `-preview` derivative and the link around it points at the
matching `-zoom`.

## 8. Search tuning

Two changes, both aimed at someone typing a name off a circuit diagram:

- **Separator.** The index now splits on `-`, `+`, `/` and `:` as well as whitespace, so `CV-DOC`,
  `TX/RX` and `AUD1+2` are findable whole and by either half.
- **Boost.** `search.boost` in the front matter of the pages that answer a mnemonic or a module
  letter: 3 on the signal listing, the error codes and *where do I start?*, 2 on the 26 module pages
  and their index, the fault-finding charts and the fault symptoms. Nothing is demoted — the
  operating instructions and the reference section keep their default weight.

## 9. What phase 7 did not do

- **No per-signal netlist.** See §2. If someone traces the wiring diagrams into a CSV, the tool that
  builds the column can read it instead, and the *modules* column becomes what the phase asked for.
- **No deferred material published.** The RGB calibration guide and the deck electronics adjustment
  stay deferred, and nothing added in this phase links to them or promises them.
- **The `redirects` plugin is still empty.** No page moved, so nothing needed one; `start-here.md`
  and `contributing.md` are new URLs.
