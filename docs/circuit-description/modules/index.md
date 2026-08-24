---
title: Module circuit descriptions
description: >-
  Chapter 3 of the manual's circuit description: how each of the twenty-five
  modules works, module A through module Z, one page per module.
---

# Module circuit descriptions

Chapter 3 of the manual's circuit description, in full: what each module does
and how its circuit does it. There is a page here for every module the manual
describes, and it carries that module's text and the manual sheets the text was
set on. It is the text that the [module pages](../../modules/index.md) draw on —
those cover the board itself, its connectors, its parts and its modification
levels.

The block diagrams the text refers to — Fig. A1, Fig. B1 and so on — are printed
on the manual sheets, which are reproduced at the foot of each page. A sheet
often carries the end of one module's description and the start of the next, so
a sheet that spans two modules appears on both of their pages.

| Module | Manual | What the description covers |
| --- | --- | --- |
| [A](a-audio-processor.md){ #module-a } — audio processor | 139 | The hf audio split into its two sub-carriers, demodulated, drop-out corrected and switched |
| [B](b-rgb.md){ #module-b } — RGB | 140 | CVBS split into luminance and chrominance, PAL decoded to R, G and B, with the colour transient improver |
| [C](c-video-processor.md){ #module-c } — video processing | 141 | Switching between internal video, external video and composite sync; the index insert; the sandcastle generator |
| [D](d-reference-source.md){ #module-d } — reference source | 142–143 | The internal sync generator and the reference signals it feeds to the rest of the player |
| [E](e-slide-drive.md){ #module-e } — slide drive | 143 | The stepping motor that moves the LDU under the disc |
| [F](f-motor-sequence.md){ #module-f } — motor + sequence | 143–144 | The brushless turntable motor: start condition, frequency control, phase control and active braking |
| [G](g-genlock.md){ #module-g } — genlock | 144 | Locking the disc to the internal sync generator in frame and line, and how that lock is established |
| [H](h-etbc-b.md){ #module-h } — ETBC B | 145–146 | The CCD coarse and LC fine delay lines that correct the video and audio time base |
| [I](i-etbc-c.md){ #module-i } — ETBC C | 146–148 | Tangential error detection from the special burst, and the phase detector that drives the correction |
| [J](j-focus.md){ #module-j } — focus | 148 | The focus servo drive |
| [K](k-hf-processor.md){ #module-k } — HF processing | 148 | Processing of the hf signal from the LDU before it reaches the demodulators |
| [L](l-video-dropout-correction.md){ #module-l } — video drop-out correction | 149 | Drop-out detection, the delayed-video substitution that hides it, and the MTF circuit |
| [M](m-radial.md){ #module-m } — radial drive | 150 | The radial servo drive |
| [N](n-display-keyboard.md){ #module-n } — display and keyboard | 150 | The front panel display and the keyboard scan |
| [P](p-frontloader.md){ #module-p } — frontloader | 151 | The front loader mechanism, its motor drive and its sensors |
| [R](r-drive-processor.md){ #module-r } — drive processor | 151 | Command input, slide control, Manchester code reading, display on screen, start-up, local control, A/V switching and service diagnostics |
| [S](s-control.md){ #module-s } — control | 152 | The control processor, its RS232 and S-bus interfaces, its memory map and its watchdog |
| [T](t-supply.md){ #module-t } — supply | 152 | The parallel switched-mode supply, its overload protection, the auxiliary supply and the output circuits |
| [Ua](u-analog-io.md#module-ua){ #module-ua } — analogue I/O, CVBS + audio | 153–154 | The sync and CVBS buffers, dc restoration, the internal/external audio switches and the beep generator |
| [Ub](u-analog-io.md#module-ub){ #module-ub } — analogue I/O, video | 154–155 | Luminance processing and chroma encoding, to make the composite output |
| [Uc](u-analog-io.md#module-uc){ #module-uc } — analogue I/O, TXT | 155 | Selection of the text source for insertion into the picture |
| [W](w-cpu-data-grabber.md){ #module-w } — data grabber and CPU | 156–160 | How computer data is taken off the disc, the descrambler, the RAM shared with the CPU, the port map and the SCSI interface |
| [X](x-lv-rom-decoder.md){ #module-x } — LV-ROM decoder | 160–161 | Computer data on the disc, the block and frame formats, data scrambling, and the decoder circuit |
| [Y](y-video-mixer.md){ #module-y } — video mixing | 162 | The five mixing modes and how the TCA240 mixer arrays combine disc video with computer text and graphics |
| [Z](z-deck-electronics.md){ #module-z } — deck electronics | 163 | The laser supply, the LDU signal processing, the ATC circuit and the focus signals |

!!! note "Modules the manual does not describe here"

    Chapter 7 has no circuit description for **Q (RC5 receiver)** or **V (module
    carrier)**, and none for the remote control handset. Those modules have
    circuit diagrams and parts lists in chapter 4 but no prose. The manual's own
    contents page lists 25 descriptions, and 25 is what is above — module U
    counts as three, Ua, Ub and Uc, and all three are on
    [one page](u-analog-io.md).

    Module **T (supply)** is described here even though the contents page places
    it between S and Ua — the sheet carries both.
