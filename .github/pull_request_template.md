## What this changes

<!-- One or two sentences. If it fixes an issue, say "Fixes #123". -->

## Which source page it is based on

<!--
The question that matters most. A change to transcribed content can be checked
against the scan in a minute if it names the sheet it came from:

  CS 7 846, service manual page 053

For a repair guide or anything measured on a real player, say so here instead -
"measured on a VP415/00, module R mod level 5" - and give the error code if
there was one.
-->

## Checklist

- [ ] `nix develop -c just check` passes — strict build, figure checks, and the link check
- [ ] New images are the **full-resolution originals**, committed under `docs/**/assets/originals/`, not resized or re-saved first
- [ ] `just derive` was run, and figures reference the `-preview` derivative with the `-zoom` one as the link target
- [ ] Every image has alt text describing what is in it, and every figure has a caption
- [ ] A figure from the manual carries its CS code and page number in the caption
- [ ] A new page is listed in the `nav:` block of `mkdocs.yml`; a moved page has a `redirect_maps` entry
- [ ] Nothing is committed twice — files move with `git mv`

<!--
The house rules and a worked example of adding a repair guide to a module page:
https://domesday86.github.io/vp415-service-guide/contributing/
-->
