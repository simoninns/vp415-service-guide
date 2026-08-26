# Phase 8 — Deployment: verification record

The phase that publishes. Its workflow landed early, as the plan itself recommended — phase 3 gave
a buildable skeleton and every phase since has been published on push — so this phase is less about
writing a workflow than about proving the one already running does what the plan says, and closing
what it turned out not to cover.

---

## 1. What landed

| File | What |
| --- | --- |
| `.github/workflows/deploy.yml` | The build job now runs the **whole** pull-request gate — `just check` — before the artifact is uploaded, not just `derive` and a strict build |
| `.github/workflows/deploy.yml` | `cancel-in-progress: false`, so a deployment already under way is never cancelled half-published |
| `.github/workflows/deploy.yml` · `check.yml` | Actions off the deprecated Node 20 runtime: `checkout` v4 → **v7**, `cache` v4 → **v6**, `upload-pages-artifact` v3 → **v5**, `deploy-pages` v4 → **v5** |
| `.github/workflows/deploy.yml` · `check.yml` | `timeout-minutes` on every job, so a hung `nix develop` cannot sit on a runner for six hours |
| `.github/workflows/check.yml` | The redundant `just lint` step removed — `just check` already runs it first |
| `flake.nix` | The stale note on `packages.site` saying it does not build until phases 2 and 3 land |

Verified against the **published** site, not a local build — see §3.

## 2. The gate ran on pull requests. Nothing ever opened one.

Phase 7 built the machinery that keeps this site honest — `check_figures.py`, `build_signal_index.py
--check`, `lychee` over every rendered `#anchor` — and wired it into `.github/workflows/check.yml`,
which triggers `on: pull_request`.

**That workflow has never run.** `gh run list --workflow check.yml` returns nothing. Every phase in
this repository has landed as a direct push to `main`, and `deploy.yml` ran `just derive` and
`mkdocs build --strict` — and nothing else. So for the whole of phase 7 the figure checks and the
generated signal index guarded a code path that this project does not use, while the builds that
actually published the site skipped them.

`--strict` is not a substitute. It catches a broken *markdown* link and an unrecognised nav entry.
It does not know that a figure is missing its alt text, that the signal listing has drifted from the
module pages it indexes, or that a `#anchor` in rendered HTML points at a heading that no longer
exists — the three things phase 7 was for.

Closed by making the deploy build job run `just check` in place of the two commands it ran before.
The gate is now on the path work actually takes, the cost is seconds (§6), and a tree that fails it
is not published — the last good deployment stays live.

`check.yml` stays. It is the same command, on the path a contributor's pull request will take.

## 3. The deployment was already live — verified against the published site

Six deployments, all green, one per phase commit. The published site was probed directly rather
than inferred from a green tick:

| Probe | Result |
| --- | --- |
| `/`, `/start-here/`, `/contributing/`, `/modules/j-focus/`, `/repair/error-codes/` | `200`, and the two phase-7 pages are there — the deployment is current |
| `/sitemap.xml` | `200`, `application/xml`, 13 210 B |
| `/search/search_index.json` | `200`, 710 330 B — search is served, not just built |
| `/nonexistent-page/` | **`404`, serving the site's own `404.html`** — Material's, styled, with the nav |
| `.../assets/web/cs-6-876-circuit-p052-preview.webp` | `200`, `image/webp`, 142 722 B |
| `.../assets/web/cs-6-876-circuit-p052-zoom.webp` | `200`, `image/webp`, 298 658 B — the lightbox resolves |
| `.../assets/originals/cs-6-876-circuit-p052.webp` | **`404`** — `exclude_docs` holds; no original is published |
| GitHub Pages source | `build_type: workflow` — deploying from Actions, not from a branch, as the plan requires |
| `github-pages` deployment for `1cc35de` | `success`, environment URL live |

The custom 404 is worth naming because nothing in the plan asked for it: `mkdocs-material` emits
`404.html`, and because `site_url` is set every asset reference inside it is absolute, so it renders
correctly at any depth of missing path. Pages serves it for anything it cannot resolve. No
`.nojekyll` is needed — Pages-from-Actions publishes the artifact verbatim and never runs Jekyll —
and the build produces no dotfiles at all, which matters for §4.

## 4. Node 20, and what the version bumps actually change

Every run since the first carried the same annotation: `actions/checkout@v4`, `actions/cache@v4`,
`actions/upload-artifact@v4` (inside `upload-pages-artifact@v3`) and `actions/deploy-pages@v4`
target Node 20, which the runners now force onto Node 24. Forced today, removed later. The release
notes were read rather than the majors taken on trust:

- **`checkout` v5 → v7.** v5 is the Node 24 move. v6 persists credentials to a separate file. v7
  blocks checking out a fork's head for `pull_request_target` and `workflow_run` — neither of which
  this repository uses.
- **`cache` v5 → v6.** v5 is Node 24, v6 an ESM migration. The key and `restore-keys` behaviour is
  unchanged, which is what the derived-asset cache depends on.
- **`upload-pages-artifact` v4 → v5.** **v4 is the one with teeth: hidden files are no longer
  included in the artifact.** `find site -name '.*'` returns **0 files**, and Pages-from-Actions
  needs no `.nojekyll`, so nothing published depends on it. v5 adds an `include-hidden-files` input
  if that ever changes.
- **`deploy-pages` v5.** Node 24.

`cachix/install-nix-action` is a composite action, so it never appeared in the annotation; it stays
at `v31`.

## 5. `cancel-in-progress: true` was wrong for a deployment

The plan's workflow, and the one that has been running, set `concurrency: {group: pages,
cancel-in-progress: true}`. That is right for a *check* — a superseded pull-request build is wasted
work — and wrong for a *deployment*: two pushes a minute apart would cancel the first mid-publish.
Now `false`, matching GitHub's own Pages starter workflow: one deployment at a time, queued runs
superseded, a run already publishing left to finish. `check.yml` keeps `true`, where it belongs.

## 6. The size budget and the time budget, measured

| | |
| --- | --- |
| Archival originals, committed, **not** published | 389 files, 874 MiB |
| Web derivatives, gitignored, published | 658 files, 189 MB (the script's own budget is 350 MB) |
| Rendered site | 85 pages + `404.html`, 200 MiB |
| Uploaded Pages artifact | **189 MB**, against the **1 GB** ceiling Pages puts on a published site |

Publishing the originals would mean roughly 1.1 GB — past the ceiling — which is why `exclude_docs`
exists and why §3 probes an original expecting a 404.

Timings, from the six runs so far: a **cold** cache took 253 s, every **warm** run since 61–77 s,
and the deploy job 11–15 s. The cache is doing its job — `derive_assets.py` reports *0 to derive,
305 up to date* on a warm tree.

The gate added to the build job costs, locally: figure checks and the signal index in under a
second, `mkdocs build --strict` **4.36 s**, and `lychee` over the rendered site **237 ms** for
**14 823 links** (1 903 unique, 13 994 OK, 829 excluded, **0 errors**). Against a 61-second build
that is noise, and it is the difference between a published site that has been checked and one that
has not.

## 7. `nix build .#site`

The README says *`nix build .#site` produces the whole site as a reproducible derivation*, and
`flake.nix` carried a note saying that output would not build until phases 2 and 3 landed. Both
claims were three phases stale and neither had been tested. It was tested:

```
$ nix build .#site
/nix/store/zanwfyxq1lhqn771pc6af0vligh5jndq-vp415-service-guide-0.1.0
```

**793 files, 200 MiB, byte-for-byte identical to `just build`** — same file list, same SHA-256 of
the sorted per-file digest. So the sandboxed build derives the assets and renders the site with no
network and no writable source tree, and the flake is a real second path to the same output rather
than a decorative one. The stale note is gone from `flake.nix`.

One cost worth knowing before reaching for it: `src = self` copies the entire working tree —
including the 874 MiB of archival originals — into the store before the build starts, so a cold
`nix build .#site` takes minutes where `just build` takes seconds. It is the right tool for
reproducing a release, not for iterating. CI uses `nix develop -c just check` for exactly that
reason.

## 8. What must stay as it is, outside the repository

Two settings live in the GitHub UI, not in a file, and nothing in the tree will notice if they
change:

- **Pages source must stay *GitHub Actions***, not *Deploy from a branch*. Currently
  `build_type: workflow` — confirmed through the API. Switching it to a branch would make every
  green deploy job publish nothing.
- **The `github-pages` environment** is what `deploy-pages` targets and where the deployment URL
  comes from. It exists and is unprotected; adding a required reviewer to it would leave every
  push waiting for approval.

Neither is a problem today. Both are recorded here because the next person to wonder why a green
build did not change the site will look in the repository first.

## 9. Done when

> a push to `main` publishes to `https://domesday86.github.io/vp415-service-guide/` and the build is
> green.

Met before this phase opened, and now met on stronger terms: the build that publishes is the build
that runs the checks. Six deployments, all green; the seventh is this record.
