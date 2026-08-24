---
title: Module E - Slide drive
description: >-
  The stepping motor that moves the LDU under the disc.
---

# Module E — Slide drive

*See also the [module E page](../../modules/e-slide-drive/index.md).*

The slide drive module, see the block diagram in Fig.E1, controls the slide drive motor. The function of the slide drive motor is to move the LDU under the disc in such a way that the tracks can be read out in an optimal way.

## Circuit description

The slide is driven by a stepping motor. Each step moves the slide by about 50 track spaces. The motor is driven by means of pulses on COMM 1-4 and SL-PWR which switches the motor coils between holding and moving power levels via an astable multivibrator with transistors 7002, 7003.

The drive signals are provided by the drive processor, module R.

*Fig.E1 SLIDE DRIVE MODULE — see the sheet below.*

## The manual sheet

<figure class="sheet sheet--fold" markdown>
[![Module D - output signals / Module E - slide drive / Module F - start condition](../assets/web/cs-7-889-text-p143-preview.webp)](../assets/web/cs-7-889-text-p143-zoom.webp)
<figcaption>
  Module D - output signals / Module E - slide drive / Module F - start condition.
  <span class="cs">CS 7 889</span>
  <span class="src">service manual page 143</span>
</figcaption>
</figure>
