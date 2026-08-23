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

# Strict build plus an offline link check of the rendered site
check: build
    lychee --offline --include-fragments --no-progress site

# As `check`, but also resolves external URLs - needs network, slower
check-external: build
    lychee --include-fragments --no-progress site

# Remove generated output: site/ and every assets/web/ directory
clean:
    rm -rf site
    @test -d docs && find docs -type d -path '*/assets/web' -prune -exec rm -rf {} + || true
