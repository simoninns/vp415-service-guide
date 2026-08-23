{
  description = "VP415 service guide - MkDocs site for the Philips VP415 LaserVision ROM drive";

  inputs = {
    # Pinned to the same channel as the development host's system flake.
    nixpkgs.url = "github:NixOS/nixpkgs/nixos-26.05";
    flake-utils.url = "github:numtide/flake-utils";
  };

  outputs = { self, nixpkgs, flake-utils }:
    flake-utils.lib.eachDefaultSystem (system:
      let
        pkgs = import nixpkgs { inherit system; };

        # MkDocs and its plugins, plus the libraries the tools/ scripts import.
        pythonEnv = pkgs.python3.withPackages (ps: with ps; [
          mkdocs                  # site generator
          mkdocs-material         # theme
          mkdocs-glightbox        # click-to-zoom lightbox for schematics
          mkdocs-minify-plugin    # HTML/CSS/JS minification
          mkdocs-redirects        # stable URLs if pages move
          pymdown-extensions      # tabs, admonitions, tables, footnotes
          pillow                  # image inspection in scripts
        ]);

        # Everything the derivation and import scripts shell out to.
        imageTools = with pkgs; [
          vips                    # fast WebP derivation, deep-zoom tiles
          imagemagick             # ad-hoc image work, contact sheets, montages
          poppler-utils           # PDF page extraction and inspection
          tesseract               # fallback OCR for anything the vendor OCR missed
          libwebp                 # cwebp / webpinfo for spot checks
          exiftool                # strip EXIF from published photographs
        ];

        shellTools = with pkgs; [
          just                    # task runner
          ripgrep
          fd
          jq
          yq-go
          lychee                  # external and internal link checking
        ];

        buildInputs = [ pythonEnv ] ++ imageTools ++ shellTools;
      in
      {
        devShells.default = pkgs.mkShell {
          inherit buildInputs;

          # Interactive greeting only - `nix develop -c <cmd>` stays quiet so
          # scripts and CI get clean output.
          shellHook = ''
            if [[ $- == *i* ]]; then
              echo "VP415 service guide - $(mkdocs --version)"
              echo "run 'just' for the available tasks"
            fi
          '';
        };

        # Reproducible site build: derive the web assets, then render.
        #
        # NOTE: this output does not build until phase 2 lands tools/derive_assets.py
        # and phase 3 lands mkdocs.yml. The dev shell above is phase 0's deliverable.
        packages.site = pkgs.stdenv.mkDerivation {
          pname = "vp415-service-guide";
          version = "0.1.0";
          src = self;

          nativeBuildInputs = buildInputs;

          buildPhase = ''
            runHook preBuild
            python3 tools/derive_assets.py
            mkdocs build --strict --site-dir site
            runHook postBuild
          '';

          installPhase = ''
            runHook preInstall
            cp -r site $out
            runHook postInstall
          '';
        };

        packages.default = self.packages.${system}.site;
      });
}
