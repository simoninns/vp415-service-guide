# VP415 service guide - task runner
#
# Everything here assumes the nix dev shell:  nix develop -c just <task>

# List the available tasks
default:
    @just --list

# Build the web derivatives from docs/**/assets/originals/ (gitignored output)
derive:
    python3 tools/derive_assets.py

# Serve the site locally with live reload
serve: derive
    mkdocs serve

# Build the site into site/
build: derive
    mkdocs build --strict

# Page checks that do not need a build: figures, and the generated signal index
lint:
    python3 tools/check_figures.py
    python3 tools/build_signal_index.py --check

# Everything CI runs on a pull request: the page checks, a strict build, and an
# offline link check of the rendered site
check: lint build
    @just _lychee --offline

# As `check`, but also resolves external URLs - needs network, slower
check-external: build
    @just _lychee

# Link-check site/ under the Pages base path.
#
# mkdocs writes root-relative links (/vp415-service-guide/...) because site_url
# is set, so lychee needs a root directory in which that path exists. A symlink
# gives it one without moving the build output.
#
# mkdocs also writes directory-style URLs (.../error-codes/#error-7). Without
# --index-files, lychee resolves those to a directory and reports every
# cross-page anchor as a missing fragment.
_lychee *ARGS:
    #!/usr/bin/env bash
    set -euo pipefail
    root=$(mktemp -d)
    trap 'rm -rf "$root"' EXIT
    ln -s "$PWD/site" "$root/vp415-service-guide"
    lychee {{ARGS}} --include-fragments --index-files index.html --no-progress \
        --root-dir "$root" "$root/vp415-service-guide"

# Remove generated output: site/ and every assets/web/ directory
clean:
    rm -rf site
    @test -d docs && find docs -type d -path '*/assets/web' -prune -exec rm -rf {} + || true
