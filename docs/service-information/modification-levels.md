---
title: Modification levels per module
description: >-
  Which modification level each module carried in each production batch, and
  what changed at every level.
---

# Modification levels

Two things: a survey of which modification level every module carried in each
production batch, and then, module by module, what actually changed at each
level and why.

Where to read the level off a player, a module or an EPROM is on
[general service → modification levels](../general-service/modification-levels.md).

!!! important "Check the level before you compare a circuit diagram"

    Several modules changed substantially between levels — module B went from 5
    to 7, module S from 3 to 8. A circuit diagram printed for one level will not
    match a board built to another.

## Survey of modification levels

Dated 1987-04-15. Columns are production batches, identified by week number and
production number; the assembly change code and set modification level are on
the second row.

| Module | 640–648<br>1–281 | 649-702<br>281-350 | 703-705<br>351-462 | 706-706<br>463-514 | 707-707<br>515-560 | 707-709<br>561-700 | 710-713<br>701-990 | 713-...<br>991-... |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| **Assembly change code / mod. level** | AH02 — 3 | AH02 — 5 | AH02 — 6 | AH02 — 7 | AH02 — 9 | AH02 — 10 | AH02 — 11 | AH03 — 13 |
| **A** [Audio processor](../modules/a-audio-processor/index.md) | 2 | 2 | 2 | 2 | 2 | 3 | 3 | 3 |
| **B** [RGB](../modules/b-rgb/index.md) | 5 | 5 | 6 | 6 | 6 | 6 | 6 | 7 |
| **C** [Video processor](../modules/c-video-processor/index.md) | 3 | 3 | 4 | 4 | 4 | 4 | 4 | 4 |
| **D** [Reference source](../modules/d-reference-source/index.md) | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 |
| **E** [Slide drive](../modules/e-slide-drive/index.md) | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 |
| **F** [Motor + sequence](../modules/f-motor-sequence/index.md) | 5 | 5 | 5 | 6 | 6 | 6 | 6 | 6 |
| **G** [Gen lock](../modules/g-genlock/index.md) | 3 | 3 | 4 | 4 | 4 | 4 | 4 | 4 |
| **H** [ETBC B](../modules/h-etbc-b/index.md) | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 |
| **I** [ETBC C](../modules/i-etbc-c/index.md) | 6 | 7 | 7 | 7 | 7 | 7 | 7 | 7 |
| **J** [Focus](../modules/j-focus/index.md) | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 4 |
| **K** [HF processor](../modules/k-hf-processor/index.md) | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| **L** [Video D.O.](../modules/l-video-dropout-correction/index.md) | 0 | 1 | 1 | 1 | 1 | 1 | 1 | 1 |
| **M** [Radial](../modules/m-radial/index.md) | 0 | 1 | 1 | 1 | 1 | 1 | 2 | 3 |
| **N** [Display + keyboard](../modules/n-display-keyboard/index.md) | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 |
| **P** [Front loader](../modules/p-frontloader/index.md) | 4 | 4 | 4 | 4 | 4 | 4 | 4 | 4 |
| **Q** [RC5 receiver](../modules/q-rc5-receiver/index.md) | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| **R** [Drive processor](../modules/r-drive-processor/index.md) | 3 | 4 | 5 | 5 | 5 | 5 | 6 | 7 |
| **S** [Control](../modules/s-control/index.md) | 3 | 4 | 4 | 4 | 5 | 5 | 6 | 8 |
| **T** [Supply](../modules/t-supply/index.md) | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 |
| **U** [Analog I/O](../modules/u-analog-io/index.md) | 3 | 4 | 4 | 4 | 4 | 4 | 4 | 4 |
| **V** [Module carrier](../modules/v-module-carrier/index.md) | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 3 |
| **W** [CPU + data grabber](../modules/w-cpu-data-grabber/index.md) | 2 | 3 | 3 | 3 | 3 | 3 | 3 | 3 |
| **X** [LV-ROM decoder](../modules/x-lv-rom-decoder/index.md) | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 |
| **Y** [Video mixer](../modules/y-video-mixer/index.md) | 4 | 5 | 6 | 6 | 6 | 6 | 6 | 6 |
| **Z** [Deck electronics](../modules/z-deck-electronics/index.md) | 2 | 2 | 2 | 2 | 3 | 3 | 3 | 3 |

<figure class="sheet" markdown>
[![Survey of modification levels VP415, page 1 of 2: a table of production batches by week and production number against the modification level of each module A to Z](assets/web/cs-8-264-table-p167-preview.webp)](assets/web/cs-8-264-table-p167-zoom.webp)
<figcaption>
  Survey of modification levels VP415, page 1/2.
  <span class="cs">CS 8 264</span>
  <span class="src">service manual page 167</span>
</figcaption>
</figure>

<figure class="sheet" markdown>
[![Survey of modification levels VP415, page 2 of 2: the later production batches, with four columns left blank for batches not yet built](assets/web/cs-8-265-table-p168-preview.webp)](assets/web/cs-8-265-table-p168-zoom.webp)
<figcaption>
  Survey of modification levels VP415, page 2/2. The last four columns are
  blank on the sheet — batches that had not been built when it was printed.
  <span class="cs">CS 8 265</span>
  <span class="src">service manual page 168</span>
</figcaption>
</figure>

## What changed at each level

Eighteen sheets, one or two per module, dated 1987-04-15. Modules D, E, N, P,
Q, V, W and X have no mod-level sheet: nothing changed on them that needed
documenting.

Component references use the four-number diagram coding — see
[remarks](../general-service/remarks.md), section 6.

## Module A — Audio processor { #mod-a }

*See also the [module A page](../modules/a-audio-processor/index.md).*

| Mod. level | Description | Reason | Mod. documents |
| --- | --- | --- | --- |
| 3 | **Deleted :**<br>-IC6203<br>-R3112 47k<br>-R3113 3k9<br>-R3114 2k<br>**Added :**<br>-TS6112 BC 817-25 4822 130 42804<br>-TS6113 BC 817-25 4822 130 42804<br>-R3075 820 E 4822 111 90171<br>-R3053 820 E 4822 111 90171 | Availability IC, better S/R and cheaper circuit added | FA 2961 |

<figure class="sheet" markdown>
[![Modification levels per module](assets/web/cs-8-266-table-p169-preview.webp)](assets/web/cs-8-266-table-p169-zoom.webp)
<figcaption>
  Modification levels per module.
  <span class="cs">CS 8 266</span>
  <span class="src">service manual page 169</span>
</figcaption>
</figure>

## Module B — RGB { #mod-b }

*See also the [module B page](../modules/b-rgb/index.md).*

| Mod. level | Description | Reason | Mod. documents |
| --- | --- | --- | --- |
| 6 | **Changed :**<br>-R3031 was 3k6 becomes 3k3 4822 111 90157<br>-L5003 was 66μH becomes 31μH 4822 157 53155 | To make the arrange level (R-Y)-(B-Y) Symmetrical | AHT 9196 |
| 7 | **Changed :**<br>-IC7202 was TDA4560 becomes TDA4565/V4 4822 209 71512<br>-R3021 was 10E becomes 1k 5322 111 90092<br>-R3022 was 1k becomes 10E 5322 111 90095<br>-Correction circuit diagram: .pin13-IC7202 becomes pin14 .pin24-IC7202 becomes pin13 .pin15-IC7202 to+11 supply<br>-R3031 wasw 3k3 becomes 3k6 5322 116 53738 | Improved specification | AHT9453 |
| 8 | **Changed :**<br>-Short circuit pins 27 and 28 of IC7203 | White stripes at switch on and prevent neg.pulses in vert.blanking below black level | FA2989 |
| 8 | **Added :**<br>-R 22k(SFR25)between base TS7012 and 7B3(CVE/I) (Also add connection between 9C1 and 7B3 on module V ) | Colour loss when 2 disc-drives operate synchronous and slave drive is in still-mode | FA2978 |

<figure class="sheet" markdown>
[![Mod levels - RGB module B](assets/web/cs-8-267-table-p170-preview.webp)](assets/web/cs-8-267-table-p170-zoom.webp)
<figcaption>
  Mod levels - RGB module B.
  <span class="cs">CS 8 267</span>
  <span class="src">service manual page 170</span>
</figcaption>
</figure>

## Module C — Video processor { #mod-c }

*See also the [module C page](../modules/c-video-processor/index.md).*

| Mod. level | Description | Reason | Mod. documents |
| --- | --- | --- | --- |
| 4 | **Changed :**<br>-R3007 was 130E becomes 120E 4822 111 90339<br>**Added :**<br>-C2006 22N 4822 122 31797<br>-R3014 Fus car Flm rst 22E 4822 111 40847<br>-R3077 Chip rst 22K 4822 111 90251<br>-R3078 Chip rst 22k 4822 111 90251 | Amplification extern CVBS signal is to small | AHT 9198 |

<figure class="sheet" markdown>
[![Mod levels - video processor module C](assets/web/cs-8-268-table-p171-preview.webp)](assets/web/cs-8-268-table-p171-zoom.webp)
<figcaption>
  Mod levels - video processor module C.
  <span class="cs">CS 8 268</span>
  <span class="src">service manual page 171</span>
</figcaption>
</figure>

## Module F — Motor + sequence { #mod-f }

*See also the [module F page](../modules/f-motor-sequence/index.md).*

MOTOR + SEQUENCE MODULE F

| Mod. level | Description | Reason | Mod. documents |
| --- | --- | --- | --- |
| 6 | **Deleted :**<br>-C2010/2011/2012/2013/2014 2015<br>**Added :**<br>-C2901/2902/2903-1n2 4822 122 10185 | White dots on screen | FA2960 FA2968 |
| 6 | **Changed :**<br>-C2020 was 4μF becomes 1μF 4822 124 22028 | Improved lock in of 6"-and 8"- disc | FA2976 |
| 6 | **Changed :**<br>-C2002 was chip 330nF becomes Pol.cond. 330nF 4822 121 42779<br>-R3015 was 1k5 becomes MET FLM RST 1k5 | Unallowed tolerance and instability of motor control-loop. | FA2981 |
| 6 | **Changed :**<br>-IC7260 was MC1458P1 becomes MC34002BP 4822 209 71382 | Improved GOTO at CLV | AHT9921 |

<figure class="sheet" markdown>
[![Mod levels - motor + sequence module F](assets/web/cs-8-269-table-p172-preview.webp)](assets/web/cs-8-269-table-p172-zoom.webp)
<figcaption>
  Mod levels - motor + sequence module F.
  <span class="cs">CS 8 269</span>
  <span class="src">service manual page 172</span>
</figcaption>
</figure>

## Module G — Gen lock { #mod-g }

*See also the [module G page](../modules/g-genlock/index.md).*

| Mod. level | Description | Reason | Mod. documents |
| --- | --- | --- | --- |
| 4 | Changed :<br>-R3077 was 100k becomes 91k 5322 111 90277 | Shift of DO-INH window | FA2955 |
| | | | |

<figure class="sheet" markdown>
[![Mod levels - gen lock module G](assets/web/cs-8-270-table-p173-preview.webp)](assets/web/cs-8-270-table-p173-zoom.webp)
<figcaption>
  Mod levels - gen lock module G.
  <span class="cs">CS 8 270</span>
  <span class="src">service manual page 173</span>
</figcaption>
</figure>

## Module H — ETBC B { #mod-h }

*See also the [module H page](../modules/h-etbc-b/index.md).*

| Mod. level | Description | Reason | Mod. documents |
| --- | --- | --- | --- |
| 5 | Changed :<br>-R3072 was 3K4 becomes 2K4 4822 111 90286<br>-2070 was 47PF becomes 39PF 4822 122 31069 | Fault in diagram | FA2894 AHT9064 AHT8790 |
| 5 | Changed :<br>-R3013 was 22k potmeter, becomes 2k2 potmeter 5322 101 14008 | Improved adjustment of VCO at CLV disc | FA2947 AHT9095 |
| 5 | Deleted :<br>-C2059/2061/2064<br>-R3115/3116/3120/3121/3122 3123/3124/3125<br>-L5009/5010/5011<br>-D6013<br>-TS7026/7029 Changed :<br>-R3127 was 620E becomes 22k 4822 111 90251<br>-R3130 was 470E becomes 1k 5322 111 90092 | Audio correction is not necessary | AHT9069 |
| 5 | Changed :<br>-C2001 was 270nF becomes 220nF 4822 121 41876 | Fault in diagram | AHT9349 |

<figure class="sheet" markdown>
[![Mod levels - ETBC B module H](assets/web/cs-8-271-table-p174-preview.webp)](assets/web/cs-8-271-table-p174-zoom.webp)
<figcaption>
  Mod levels - ETBC B module H.
  <span class="cs">CS 8 271</span>
  <span class="src">service manual page 174</span>
</figcaption>
</figure>

## Module I — ETBC C { #mod-i }

*See also the [module I page](../modules/i-etbc-c/index.md).*

| Mod. level | Description | Reason | Mod. documents |
| --- | --- | --- | --- |
| 7 | **Changed :**<br>-C2046 was 56PF becomes 47PF 4822 122 31772 | Decrease of disturbation on time fault measuring | AHT9061 FA2945 |
| 7 | **Changed :**<br>-C2015 was Pol 100nF becomes Cr chip 100nF 5322 122 32839<br>-C2023 was Pol 33nF becomes Cr chip 33nF 5322 122 31848<br>-C2024 was Pol 270nF becomes Cr chip 270nF 5322 122 32839 | Improvement of HF filtering in sync sepa- rator | AHT9348 |

<figure class="sheet" markdown>
[![Mod levels - ETBC-C module I](assets/web/cs-8-272-table-p175-preview.webp)](assets/web/cs-8-272-table-p175-zoom.webp)
<figcaption>
  Mod levels - ETBC-C module I.
  <span class="cs">CS 8 272</span>
  <span class="src">service manual page 175</span>
</figcaption>
</figure>

## Module J — Focus { #mod-j }

*See also the [module J page](../modules/j-focus/index.md).*

| Mod. level | Description | Reason | Mod. documents |
| --- | --- | --- | --- |
| 3 | **Changed :**<br>-R3025 was 4k7 becomes 2k7 4822 111 90569 | Improvement of playability | FA2974 |
| 4 | **Added :**<br>-R3055 10k SFR25 on connector 7J1 to mass 4822 116 52973 | Prevent FOC-EN to go active when drive is in "tri-state" | FA2988 |

<figure class="sheet" markdown>
[![Mod levels - focus module J](assets/web/cs-8-273-table-p176-preview.webp)](assets/web/cs-8-273-table-p176-zoom.webp)
<figcaption>
  Mod levels - focus module J.
  <span class="cs">CS 8 273</span>
  <span class="src">service manual page 176</span>
</figcaption>
</figure>

## Module K — HF processor { #mod-k }

*See also the [module K page](../modules/k-hf-processor/index.md).*

| Mod. level | Description | Reason | Mod. documents |
| --- | --- | --- | --- |
| 1 | **Changed :**<br>-R3015 was 470E becomes 120E 4822 111 90339 | Avoid limiting of HF ampli- fier at max. resonant rise | AHT9286 |
| | | | |

<figure class="sheet" markdown>
[![Mod levels - HF processor module K](assets/web/cs-8-274-table-p177-preview.webp)](assets/web/cs-8-274-table-p177-zoom.webp)
<figcaption>
  Mod levels - HF processor module K.
  <span class="cs">CS 8 274</span>
  <span class="src">service manual page 177</span>
</figcaption>
</figure>

## Module L — Video D.O. { #mod-l }

*See also the [module L page](../modules/l-video-dropout-correction/index.md).*

| Mod. level | Description | Reason | Mod. documents |
| --- | --- | --- | --- |
| 1 | **Changed :**<br>-R3096 was 470E becomes 560E 5322 111 90113 | Adaption of video amplitudes | AHT9062 |
| 1 | **Changed :**<br>-R3046 was 3k3 becomes 2k7 4822 111 90157 | MTF-regulation is not good | AHT9287 |
| | | | |

<figure class="sheet" markdown>
[![Mod levels - video correction module L](assets/web/cs-8-275-table-p178-preview.webp)](assets/web/cs-8-275-table-p178-zoom.webp)
<figcaption>
  Mod levels - video correction module L.
  <span class="cs">CS 8 275</span>
  <span class="src">service manual page 178</span>
</figcaption>
</figure>

## Module M — Radial { #mod-m }

*See also the [module M page](../modules/m-radial/index.md).*

RADIAL MODULE M

| Mod. level | Description | Reason | Mod. documents |
| --- | --- | --- | --- |
| 1 | Added :<br>-TS7023 BC558B 4822 130 44197<br>-TS7024 BC558B 4822 130 44197<br>-R3085 47K 4822 116 52472<br>-R3086 47K 4822 116 52472 | Avoid DC offset on radial mirror unload | FA2946 |
| 2 | Deleted :<br>-TS7023 BC558B<br>-TS7024 BC558B<br>-R3085 47K<br>-R3086 47K | New drive software 6803.5 on Drive Proc. Mod.R | FA2946 |
| 2 | Deleted :<br>-R3001/3002/3003/3004/3005<br>-R3006/3007/3008/3009/3010<br>-C2002/2004<br>-TS7001-Short circuit S en D of TS7001 | Improvement jump behaviour | AHT9350 |
| 2 | Deleted :<br>-TS7004 | Idem | FA2958 |
| 3 | Added :<br>-C2024 10pF 4822 122 32185 | Avoid oscillation on TS IC7100 | FA2983 |

<figure class="sheet" markdown>
[![Mod levels - radial module M](assets/web/cs-8-276-table-p179-preview.webp)](assets/web/cs-8-276-table-p179-zoom.webp)
<figcaption>
  Mod levels - radial module M.
  <span class="cs">CS 8 276</span>
  <span class="src">service manual page 179</span>
</figcaption>
</figure>

## Module R — Drive processor { #mod-r }

*See also the [module R page](../modules/r-drive-processor/index.md).*

DRIVE PROC MODULE R

| Mod. level | Description | Reason | Mod. documents |
| --- | --- | --- | --- |
| - | Changed :<br>-R3064 becomes R3069<br>-R3064 becomes R3080<br>-C2019 was 10μF becomes 22μF 5322 124 21643 | Correction Service manual | AHT9285 |
| 4 | Changed :<br>-EPROM IC7204 software was 3104 103 6803.4 becomes 3104 103 6803.5 | See survey of software rel- eases in this service infor- mation | WV14748 |
| 5 | Added :<br>-R3070 100k 4822 116 52453<br>-R3071 100k 4822 116 52453 | Improvement of DR-signal | AHT9285 |
| 5 | Changed :<br>-C2004 was 2μF becomes 10μF 5322 124 21749 | A temporary solution to avoid "reset" of the drive | FA2889 AHT9457 |
| 6 | Changed :<br>-EPROM IC7204 software was 3104 103 6803.5 becomes 3104 103 6803.6 | See survey of S.W releases in this Ser- vice Informat- ion | WV14750 |
| 7 | Changed :<br>-C2018 was 15μF becomes 68μF 5322 124 10512 | Prevent eject of disc tray at start up | FA2990 |

<figure class="sheet" markdown>
[![Mod levels - drive processor module R](assets/web/cs-8-277-table-p180-preview.webp)](assets/web/cs-8-277-table-p180-zoom.webp)
<figcaption>
  Mod levels - drive processor module R.
  <span class="cs">CS 8 277</span>
  <span class="src">service manual page 180</span>
</figcaption>
</figure>

| Mod. level | Description | Reason | Mod. documents |
| --- | --- | --- | --- |
| 7 | Added :<br>-R3064 1E5 4822 111 30487<br>-R3065 220k 4822 111 90197<br>-R3066 100k 4822 111 90214<br>-R3067 100k 4822 111 90214<br>-C2019 10μF 5322 124 21749<br>-TS7007 BC858B 5322 130 41983<br>-TS7008 BC848B 5322 130 41982 | Finger protection circuit front loader | AHT9030 |

<figure class="sheet" markdown>
[![Mod levels - drive processor module R (continued)](assets/web/cs-8-278-table-p181-preview.webp)](assets/web/cs-8-278-table-p181-zoom.webp)
<figcaption>
  Mod levels - drive processor module R (continued).
  <span class="cs">CS 8 278</span>
  <span class="src">service manual page 181</span>
</figcaption>
</figure>

## Module S — Control { #mod-s }

*See also the [module S page](../modules/s-control/index.md).*

| Mod. level | Description | Reason | Mod. documents |
| --- | --- | --- | --- |
| - | **Changed :**<br>-R3005 was 10K becomes 8K2 5322 111 90118<br>-R3006 was 47K becomes 10K 4822 111 40249<br>-R3012 was 10K becomes 2K7 4822 111 90569 | Correction of Service manual | |
| 6 | **Changed :**<br>-EPROM IC7202 software was 3104 103 6804.4 becomes 3104 103 6804.5 | See survey of S.W releases in this Service infor- mation | WV14748 |
| 7 | **Changed :**<br>-EPROM IC7202 software was 3104 103 6804.5 becomes 3104 103 6804.6 | See survey of S.W releases in this Service infor- mation | WV14749 |

<figure class="sheet" markdown>
[![Mod levels - control module S](assets/web/cs-8-279-table-p182-preview.webp)](assets/web/cs-8-279-table-p182-zoom.webp)
<figcaption>
  Mod levels - control module S.
  <span class="cs">CS 8 279</span>
  <span class="src">service manual page 182</span>
</figcaption>
</figure>

## Module T — Supply { #mod-t }

*See also the [module T page](../modules/t-supply/index.md).*

| Mod. level | Description | Reason | Mod. documents |
| --- | --- | --- | --- |
| 1 | **Added :**<br>-Res. 0.15E/1W 5322 113 41136 in series with fuse F913. Only for VP410. | Stripes in picture at start up of disc drive | FA2954 |
| | | | |

<figure class="sheet" markdown>
[![Mod levels - supply module T](assets/web/cs-8-280-table-p183-preview.webp)](assets/web/cs-8-280-table-p183-zoom.webp)
<figcaption>
  Mod levels - supply module T.
  <span class="cs">CS 8 280</span>
  <span class="src">service manual page 183</span>
</figcaption>
</figure>

## Module U — Analog I/O { #mod-u }

*See also the [module U page](../modules/u-analog-io/index.md).*

| Mod. level | Description | Reason | Mod. documents |
| --- | --- | --- | --- |
| 4 | **Changed :**<br>-R3304 was 470E becomes 330E 5322 111 90106 | Arrange level too small | FA2934 AH18876 |
| 4 | **Added :**<br>-R3350 100E in series with C2302 5322 111 90091<br>-R3351 100E in series with C2305 5322 111 90091 | Improvement CBL to encoder Analog I/O | FA2948 |
| 4 | **Changed :**<br>-IC7651 was IC SAA5230/V3 becomes IC SAA5231/V3 4822 209 71491 | Availability of IC | AHT9548 |

<figure class="sheet" markdown>
[![Mod levels - analog I/O module U](assets/web/cs-8-281-table-p184-preview.webp)](assets/web/cs-8-281-table-p184-zoom.webp)
<figcaption>
  Mod levels - analog I/O module U.
  <span class="cs">CS 8 281</span>
  <span class="src">service manual page 184</span>
</figcaption>
</figure>

## Module Y — Video mixer { #mod-y }

*See also the [module Y page](../modules/y-video-mixer/index.md).*

| Mod. level | Description | Reason | Mod. documents |
| --- | --- | --- | --- |
| 5 | **Changed :**<br>-D6404 was BB112 becomes BB809 5322 130 31684 | Correction Ser.manual | AHT9032 FA2908 |
| 5 | **Changed :**<br>-C2416 was 8nF2 becomes 100pF 4822 122 32942 | Improvement horizontal distortion computer text | FA2943 AHT9352 |
| 6 | **Added :**<br>-R3429 Chip rest 10M 4822 111 90807 | Jitter of com- puter overlay | FA2949 AHT9197 |

<figure class="sheet" markdown>
[![Mod levels - video mix module Y](assets/web/cs-8-282-table-p185-preview.webp)](assets/web/cs-8-282-table-p185-zoom.webp)
<figcaption>
  Mod levels - video mix module Y.
  <span class="cs">CS 8 282</span>
  <span class="src">service manual page 185</span>
</figcaption>
</figure>

## Module Z — Deck electronics { #mod-z }

*See also the [module Z page](../modules/z-deck-electronics/index.md).*

| Mod. level | Description | Reason | Mod. documents |
| --- | --- | --- | --- |
| - | **Changed :**<br>-R3104 was 22K becomes 10K 4822 111 90249<br>-R3086 was 6K8 becomes 33K 5322 111 90267<br>-R3087 was 4K7 becomes 22K 4822 111 90251<br>-R3088 was 4K7 becomes 22K 4822 100 11155<br>-R3089 was 1M becomes 4M7 4822 111 90806 | Fault in diagram Introducing new corner sensor with another specification | FA2950 |
| - | **Added :**<br>-D6021 HZA92 8V2 4822 130 33294<br>**Changed :**<br>-R3109 was 10E becomes 0E 4822 111 90163<br>-R3110 was 10E becomes 0E 4822 111 90163 | Tiltmotor does not work correct | FA2880 AHT9134 |
| - | **Changed :**<br>-D6021 was HZA92 becomes BC548B 4822 130 40937. | Cheaper | AHT9863 |

<figure class="sheet" markdown>
[![Mod levels - deck electronics module Z](assets/web/cs-8-283-table-p186-preview.webp)](assets/web/cs-8-283-table-p186-zoom.webp)
<figcaption>
  Mod levels - deck electronics module Z.
  <span class="cs">CS 8 283</span>
  <span class="src">service manual page 186</span>
</figcaption>
</figure>
