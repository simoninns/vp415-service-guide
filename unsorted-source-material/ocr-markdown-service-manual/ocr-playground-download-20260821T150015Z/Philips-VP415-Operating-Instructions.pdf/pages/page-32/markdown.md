The response bytes x1 to x5 are made up of ASCII digits.

x1 = 0

x2 = major revision level of drive software

x3 = minor revision level of drive software

x4 = major revision level of control software

x5 = minor revision level of control software

# AUDIO 1 OFF

Syntax: A0

First code: A (65D = 41H)

Response: None

Function: Disable internal audio channel 1 (from disc)

If audio channel 2 is on, both audio outputs are supplied by audio channel 2.

# AUDIO 1 ON

Syntax: A1

First code: A (65D = 41H)

Response: None

Function: Enable internal audio channel 1 (from disc)

This is the power-on default state. Audio is on only during normal play forward.

# AUDIO 2 OFF

Syntax: B0

First code: B (66D = 42H)

Response: None

Function: Disable internal audio channel 2 (from disc)

If audio channel 1 is on, both audio outputs are supplied by audio channel 1.

# AUDIO 2 ON

Syntax: B1

First code: B (66D = 42H)

Response: None

Function: Enable internal audio channel 2 (from disc)

This is the power-on default state. Audio is on only during normal play forward.

# CHAPTER NUMBER DISPLAY OFF

Syntax: C0

First code: C (67D = 43H)

Response: None

Function: Cancel chapter number display.

This is the power-on default state.

# CHAPTER NUMBER DISPLAY ON

Syntax: C1

First code: C (67D = 43H)

Response: None

Function: Display chapter number on screen.

This is disabled during lead-in/lead-out and during Goto. The picture number/time code display (if on) is switched off.

# PICTURE NUMBER/TIME CODE DISPLAY OFF

Syntax: D0

First code: D (68D = 44H)

Response: None

Function: CAV - Cancel picture number display

CLV - Cancel time code display

This is the power-on default state.

# PICTURE NUMBER/TIME CODE DISPLAY ON

Syntax: D1

First code: D (68D = 44H)

Response: None

Function: CAV - Display picture number on screen

CLV - Display time code on screen

This is disabled during lead-in/lead-out and during Goto. The chapter number display (if on) is switched off.

# VIDEO OFF

Syntax: E0

First code: E (69D = 45H)

Response: None

Function: Switch off internal video (from disc)

# VIDEO ON

Syntax: E1

First code: E (69D = 45H)

Response: None

Function: Switch on internal video (from disc)

This is the power-on default state. The video is also switched off by the player when not in the active area of the disc, or when pause, ready or Goto are active.

# LOAD PICTURE NUMBER INFO REGISTER (CAV only)

Syntax: FxxxxxI

Codes: F (70D = 46H)

I (73D = 49H)

Response: Positive ack: A3

Negative ack: AN if CLV disc

O if disc-tray is open

Function: The positive acknowledge signal is given when the specified picture number is passed by any play or step action.

The INFO register is cleared after the response.

If a CLV disc is loaded, the negative acknowledge (AN) will be given.

# LOAD PICTURE NUMBER STOP REGISTER (CAV only)

Syntax: FxxxxxS

Codes: F (70D = 46H)

S (83D = 53H)

Response: Positive ack: A2

Negative ack: AN if CLV disc

O if disc-tray is open

Function: The player halts at the specified picture number when reached by any play or step action. The positive acknowledge signal is then given.

The STOP register is cleared after the response.

If a CLV disc is loaded, the negative acknowledge (AN) will be given.

# GOTO PICTURE NUMBER AND HALT (CAV only)

Syntax: FxxxxxR

Codes: F (70D = 46H)

R (82D = 52H)

Response: Positive ack: A0

Negative ack: AN if Goto fails

O if disc-tray is open

Function: Search for picture number and display in still mode.

The specified picture is searched for. When found, the picture is displayed in still mode and the positive acknowledge signal is given. If the picture number is not found, the negative response (AN) is given.

31