---
title: Error codes
description: >-
  The meaning of every diagnostic error code the VP415 can display, with its
  severity band.
---

# Meaning of the error codes

The drive processor shows a fault as a number in the bottom right corner of the
picture. This page is the lookup table. How to get the player to display them
at all is on the [diagnostic mode](diagnostic-mode.md) page; what to do about
one is on the [fault-finding charts](fault-finding.md) page.

## Severity bands

The code number itself carries the severity — **the lower the code, the more
serious the fault**:

| Range | Severity | Effect in self-test mode |
| --- | --- | --- |
| 1–30 | Fatal fault | Interrupts the programme loop; the drive goes to STAND-BY |
| 31–59 | Major fault | Interrupts the programme loop; the drive goes to STAND-BY |
| 60–80 | Behaviour fault | Programme loop continues |
| 81–99 | Minor fault | Programme loop continues |
| 100–254 | For development | — |
| 255 | Initial value | Displayed as `- - -`, meaning no fault |

In check mode the display shows the **last** detected fault. In self-test mode
a displayed major fault is overwritten only by a code with higher priority —
that is, a lower number.

## The codes

| Code | Severity | Description |
| --- | --- | --- |
| <a id="error-1"></a>**1** | Fatal | tray is impeded in getting in or out |
| <a id="error-2"></a>**2** | Fatal | no disc reflection |
| <a id="error-3"></a>**3** | Fatal | SPI not found |
| <a id="error-4"></a>**4** | Fatal | time-out tilt |
| <a id="error-5"></a>**5** | Fatal | laser not on |
| <a id="error-6"></a>**6** | Fatal | not out of focus |
| <a id="error-7"></a>**7** | Fatal | not in focus after 5x (no rotation of disc)<br>→ [worked case study](case-studies/error-7-focus.md) |
| <a id="error-8"></a>**8** | Fatal | motor speed error |
| <a id="error-9"></a>**9** | Fatal | framelock<br>→ [worked case study](case-studies/error-9-frame-lock.md) |
| <a id="error-10"></a>**10** | Fatal | motor slows down |
| <a id="error-11"></a>**11** | Fatal | laser not off |
| <a id="error-12"></a>**12** | Fatal | not out of focus after unloading |
| <a id="error-13"></a>**13** | Fatal | not switched into 'standby off' (time-out 2 sec.) |
| <a id="error-14"></a>**14** | Fatal | active 0-RPM without a LV disc at start up |
| <a id="error-15"></a>**15** | Fatal | laser out during MAIN 1 |
| <a id="error-16"></a>**16** | Fatal | motor error during MAIN 1 |
| <a id="error-17"></a>**17** | Fatal | no focus 20 steps after focus error |
| <a id="error-20"></a>**20** | Fatal | drive board inside LV player during hardware test |
| <a id="error-25"></a>**25** | Fatal | no REFV pulse at system start-up |
| <a id="error-26"></a>**26** | Fatal | REFV period > 64 msec |
| <a id="error-27"></a>**27** | Fatal | REFV pulse is not in conformity with NTSC/PAL standard |
| <a id="error-28"></a>**28** | Fatal | - |
| <a id="error-29"></a>**29** | Fatal | out of valid active video area, action:unload |
| <a id="error-30"></a>**30** | Fatal | no reference pulse |
| <a id="error-43"></a>**43** | Major | radial offset outside of window set to upper limit |
| <a id="error-44"></a>**44** | Major | radial offset outside of window set to lower limit |
| <a id="error-52"></a>**52** | Major | no 2ppr pulse |
| <a id="error-53"></a>**53** | Major | no lead-in code at start-up of player (diagnostics) |
| <a id="error-54"></a>**54** | Major | no active video area detected (diagnostics) |
| <a id="error-56"></a>**56** | Major | time-out (100 s) scan forward (diagnostics) |
| <a id="error-58"></a>**58** | Major | play forward error (diagnostics) |
| <a id="error-60"></a>**60** | Behaviour | out of focus during 'main1' |
| <a id="error-61"></a>**61** | Behaviour | out of focus at start-up (disc rotates) |
| <a id="error-62"></a>**62** | Behaviour | detection of radial mirror movements fails during instant jump |
| <a id="error-63"></a>**63** | Behaviour | goto time-out |
| <a id="error-64"></a>**64** | Behaviour | no valid command |
| <a id="error-65"></a>**65** | Behaviour | lead-in/lead-out |
| <a id="error-66"></a>**66** | Behaviour | no valid 24-bit code |
| <a id="error-67"></a>**67** | Behaviour | instant jump error in one of the previous jump(s) |
| <a id="error-68"></a>**68** | Behaviour | time-out during track crossing instant jump |
| <a id="error-70"></a>**70** | Behaviour | error 62 during 'scan'; corr. of slide with 1 fs. |
| <a id="error-71"></a>**71** | Behaviour | radial mirror sensitivity > 900 μ/V |
| <a id="error-72"></a>**72** | Behaviour | radial mirror sensitivity > 200 μ/V |
| <a id="error-73"></a>**73** | Behaviour | a/d converted mirror pos. min. (out of field of view) |
| <a id="error-74"></a>**74** | Behaviour | a/d converted mirror pos. max. (out of field of view) |
| <a id="error-75"></a>**75** | Behaviour | SPI detected during master mode & slide moves inward. The slide is stopped by 'timer0'. |
| <a id="error-76"></a>**76** | Behaviour | SPI protection is activated |
| <a id="error-79"></a>**79** | Behaviour | apply for update of comm. pattern over zero steps |
| <a id="error-80"></a>**80** | Behaviour | *no description printed* |
| <a id="error-81"></a>**81** | Minor | no 24 bits |
| <a id="error-82"></a>**82** | Minor | no 8 or F key |
| <a id="error-83"></a>**83** | Minor | no valid 8 key code |
| <a id="error-84"></a>**84** | Minor | no valid chapter code |
| <a id="error-85"></a>**85** | Minor | lead-in code |
| <a id="error-86"></a>**86** | Minor | lead-out code |
| <a id="error-87"></a>**87** | Minor | time code |
| <a id="error-88"></a>**88** | Minor | BCD error in picture no. X2X3 |
| <a id="error-89"></a>**89** | Minor | BCD error in picture no. X4X5 |
| <a id="error-95"></a>**95** | Minor | out of lock during main1 (only detec. for CAV discs) |
| <a id="error-96"></a>**96** | Minor | no datic interrupt (no 24-bit code ?) |
| <a id="error-99"></a>**99** | Minor | time-out during start-up 'diagnostics' |
| <a id="error-110"></a>**110** | Development | master mode: actual slide speed > limited speed |
| <a id="error-111"></a>**111** | Development | timer1 overflow / sw error |
| <a id="error-112"></a>**112** | Development | instant jump of > 51 tracks (limited to 51) |
| <a id="error-113"></a>**113** | Development | instant jump of 0 tracks |
| <a id="error-117"></a>**117** | Development | selection of 'slave mode' at high speed master mode |
| <a id="error-119"></a>**119** | Development | hwtest activated after detection of low level pin p3.5 |
| <a id="error-120"></a>**120** | Development | hardware test is active |
| <a id="error-121"></a>**121** | Development | command sequence in undefined mode (diagnostics) |
| <a id="error-124"></a>**124** | Development | synchronisation error timing single track crossing |
| <a id="error-126"></a>**126** | Development | instant jump at high speed master mode (not executed) |
| <a id="error-127"></a>**127** | Development | instant jump during master mode (not executed) |
| <a id="error-133"></a>**133** | Development | error during 'step procedure' |
| <a id="error-137"></a>**137** | Development | re-initialisation of delay counter stand-by |
| <a id="error-151"></a>**151** | Development | re-init. delay counter stand-by |
| <a id="error-170"></a>**170** | Development | precontrol instant jump > 1step |
| <a id="error-171"></a>**171** | Development | precontrol error instant jump |

Codes 18, 19, 21–24, 31–42, 45–51, 55, 57, 59, 69, 77, 78, 90–94, 97, 98 and
the gaps above 100 are not listed in the manual: they are unused, or reserved.
Code 28 is listed with a dash, and code 80 with no description at all.

<figure class="sheet" markdown>
[![Meaning of the error codes: a two-column list of diagnostic error codes from 1 to 171 with their descriptions](assets/web/cs-8-114-table-p111-preview.webp)](assets/web/cs-8-114-table-p111-zoom.webp)
<figcaption>
  Meaning of the error codes.
  <span class="cs">CS 8 114</span>
  <span class="src">service manual page 111</span>
</figcaption>
</figure>

!!! tip "Linking to a code"

    Every row above has an anchor of the form `#error-7`, so a page elsewhere on
    this site — or a bookmark, or a forum post — can link straight at one code.
