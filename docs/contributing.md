---
title: Contributing
description: >-
  How to report a fault, correct a transcription, and add your own repair
  guide to a module page — with a worked example.
---

# Contributing

This site is a working reference for people repairing forty-year-old players,
and the most valuable thing in it is what somebody learned at a bench. The
manual is fixed; what surrounds it is not.

## What is wanted

<div class="grid cards" markdown>

-   :material-wrench: **Repair reports**

    ---

    A fault you traced, with the error code, the measurements and what it
    turned out to be. Even an unfinished diagnosis is useful — both
    [case studies](repair/case-studies/index.md) started as one.

    [:octicons-arrow-right-24: Open a repair report](https://github.com/domesday86/vp415-service-guide/issues/new?template=repair-report.yml)

-   :material-text-search: **Corrections**

    ---

    A transcription that does not match the scan, a wrong component value, a
    dead link. Say which page and which sheet, and it can be checked against
    the 300 dpi original in the repository.

    [:octicons-arrow-right-24: Report a correction](https://github.com/domesday86/vp415-service-guide/issues/new?template=correction.yml)

-   :material-image-plus: **Better material**

    ---

    Sharper photographs of a board, a scan of a sheet this copy of the manual
    is missing, an oscillogram of a signal the manual only describes.

    [:octicons-arrow-right-24: Open an issue](https://github.com/domesday86/vp415-service-guide/issues/new)

</div>

Errata are welcome even when you are not sure. The manual is not always right —
[module J's data sheet prints the 6210 / 6211 pinout backwards](modules/j-focus/index.md),
and it took a real player to find it.

## The three ways in

1. **Open an issue.** Nothing to install. The templates ask for the things that
   turn out to matter — the error code, the modification level, what was
   measured where.
2. **Use the pencil.** Every page has an *edit this page* icon at the top right
   that opens it in the GitHub editor and raises a pull request for you. This is
   the right route for a typo or a wrong value.
3. **Clone it.** For anything with pictures, or more than a paragraph of prose.
   The rest of this page is about that.

## Building the site locally

Everything the site needs is in the flake, so there is nothing to install
beyond Nix:

```bash
git clone https://github.com/domesday86/vp415-service-guide
cd vp415-service-guide
nix develop -c just serve      # http://127.0.0.1:8000, live reload
```

Two more tasks matter before you push:

```bash
nix develop -c just build      # mkdocs build --strict: warnings are errors
nix develop -c just check      # the strict build, plus a link check of the result
```

`just check` is what CI runs on a pull request. It walks every link in the
rendered site — 13 000 of them — including the fragment of every `#anchor`, so
a link to a heading that has been renamed fails the build rather than rotting
quietly.

## A worked example: adding a repair guide to a module page

Say you have repaired the focus amplifier on
[module J](modules/j-focus/index.md) and want the next person to have it.

### 1. Put the photographs where they belong

Every section carries its own assets, beside its markdown. There is exactly one
copy of any file in this repository, and for images that copy is the **archival
original**:

```
docs/modules/j-focus/
  index.md
  assets/originals/          # committed: the one copy, full resolution
  assets/web/                # gitignored: derived by `just derive`
```

Drop the full-resolution files into `assets/originals/`, named for what they
are, in lower case with hyphens:

```
docs/modules/j-focus/assets/originals/j-focus-6210-6211-replaced.jpg
```

Do not resize, crop or re-save them first — the derivation does that, and the
original is what someone will want in ten years. Nothing under
`assets/originals/` is published: `exclude_docs` in `mkdocs.yml` keeps 918 MB of
scans out of the build, because a GitHub Pages site is capped at 1 GB.

### 2. Derive the web copies

```bash
nix develop -c just derive
```

This writes a `-preview` and a `-zoom` WebP beside each other under
`assets/web/`, sized by profile. A photograph gets the `photo` profile by
default: 1400 px preview, native-resolution zoom. To pick a different one —
`schematic` for a drawing, `scope-trace` for an oscillogram — add a row for the
file to `planning/migration-log.csv`. Re-running is cheap: files whose SHA-256
has not changed are skipped.

### 3. Write the section

Module pages have a fixed running order — Overview · The board · Circuit
description · Adjustments · Circuit diagram · PCB lay-out · Electrical parts ·
Modification levels · Related. A repair guide goes in after *Modification
levels* and before *Related*:

```markdown
## Repairing the focus amplifier

Symptom: [error 7](../../repair/error-codes.md#error-7) on every start-up, the
objective sweeping its full travel and never settling.

**What it was.** 6211 (BD437) had failed short collector-to-emitter, holding
`FOCACT` at −12 V. …

**Measurements**

| Point | Should be | Was |
| --- | --- | --- |
| `9J1` — `FOCACT` | about −1 V once in focus | −11.8 V, static |
| `7J1` — `FOC-EN` | +12 V while the drive is trying | correct |

!!! warning "Watch the pinout"

    The data sheet prints 6210 and 6211 as **BCE**; they are **ECB**. See the
    erratum at the top of this page.

<figure class="sheet sheet--photo" markdown>
[![Module J with 6210 and 6211 replaced, showing the two new BD436 and BD437 transistors](assets/web/j-focus-6210-6211-replaced-preview.webp)](assets/web/j-focus-6210-6211-replaced-zoom.webp)
<figcaption>
  6210 and 6211 replaced. The originals had failed short.
</figcaption>
</figure>
```

Then add a line to that page's **Related** list pointing at whatever else the
repair touches — the error code, the case study, the module at the other end of
the signal.

### 4. The house rules the build enforces

| Rule | Why |
| --- | --- |
| Every image has **alt text** that describes what is in it, not what it is called | The alt text is what a reader who cannot see the picture gets, and what a search engine reads |
| Every figure has a `<figcaption>` | A picture with no caption is an ornament |
| A figure that comes from the manual carries the **CS code** and the **page number** in its caption, in `<span class="cs">` and `<span class="src">` | So a reader with the paper manual can find the same sheet |
| The inline image is the `-preview`, the link target is the `-zoom` | glightbox opens the link in the lightbox |
| Links between pages are **relative** and end in `.md` | mkdocs rewrites them, and `--strict` catches the ones that do not resolve |
| Signal mnemonics are in `` `backticks` `` | The [signal index](system/signal-listing.md) is built by reading them |

`tools/check_figures.py` checks the first three on every page and runs as part
of `just check`, so a figure without alt text or a caption fails CI rather than
reaching the site.

### 5. Open the pull request

The pull-request template asks one question that matters more than the rest:
**which source page the change is based on**. A correction that names the sheet
it came from can be checked in a minute against the 300 dpi scan; one that does
not, cannot.

## Adding a whole page

Same as above, plus an entry in the `nav:` block of `mkdocs.yml` — the nav is
explicit, so a page that is not listed there is built but unreachable, and
`--strict` will say so. If a page moves, add a `redirect_maps` entry rather than
breaking the old URL.

## What is deliberately not here

- **No PDFs.** The operating instructions are transcribed as their own section,
  and the NEC and Intel datasheets are named by part number rather than served.
- **No archival originals on the site.** They are in the repository, which is
  where a lossless file belongs; the site carries the derivatives.
- **No second copy of anything.** If a file needs to be somewhere else, it is
  moved with `git mv`, not copied.
