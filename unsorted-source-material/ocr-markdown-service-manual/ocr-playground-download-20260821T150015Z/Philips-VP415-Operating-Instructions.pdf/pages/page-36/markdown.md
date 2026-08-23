VPX = This command interrogates the system for its current video mode. The reply code is identical to the appropriate video command i.e. VP1 to VP5.

# AUDIO 1 FROM INTERNAL

Syntax: 0

First code: (91D = 5BH)

Response: None

Function: The internal audio 1 signal is selected.

This is the power-on default state.

# AUDIO 1 FROM EXTERNAL

Syntax: 1

First code: (91D = 5BH)

Response: None

Function: The internal audio 1 signal is inhibited in favour of the audio source on the audio 1 input connector.

The audio 1 on/off switch and the audio 1 mute do not have a function in this mode.

# VIDEO FROM INTERNAL

Syntax: 0

First code: (92D = 5CH)

Response: None

Function: The internal video signal is selected.

This is the power-on default state.

# VIDEO FROM EXTERNAL

Syntax: 1

First code: (92D = 5CH)

Response: None

Function: The internal video signal is inhibited in favour of the external video source on the CVBS video input connector.

The video on/off switch and the video mute do not have a function in this mode.

# AUDIO 2 FROM INTERNAL

Syntax: 0

First code: (93D = 5DH)

Response: None

Function: The internal audio 2 signal is selected.

This is the power-on default state.

# AUDIO 2 FROM EXTERNAL

Syntax: 1

First code: (93D = 5DH)

Response: None

Function: The internal audio 2 signal is inhibited in favour of the audio source on the audio 2 input connector.

The audio 2 on/off switch and the audio 2 mute do not have a function in this mode.

# TXT FROM DISC OFF

Syntax: _0

First code: _ (95D = 5FH)

Response: None

Function: The video lines that may contain teletext information are muted (internal video signal from LV disc).

# TXT FROM DISC ON

Syntax: _1

First code: _ (95D = 5FH)

Response: None

Function: The teletext information in the raster blanking lines of the internal video signal (LV disc) is enabled.

This is the power-on default state.

35