# INSTANT JUMP REVERSE

Syntax: -yy

First code: -(45D = 2DH)

Response: None

Function: Jump back over yy pictures.

The jump is performed at the end of the first video field. Small jumps are invisible, as they can be performed within the video blanking.

After this command, the player continues its previous operation.

The following limits apply:

yy = 1...50

# STANDBY

Syntax: ,0

First code: ,(44D = 2CH)

Response: None

Function: Enter standby condition.

The spinning motor is decelerated and the optical readout unit goes to 'lead-in' (home position). The player is then switched to standby. All defaults are reloaded except for communication protocol, and the STOP and INFO registers are cleared.

# ON

Syntax: ,1

First code: ,(44D = 2CH)

Response: Positive ack: S

Negative ack: O (if disc-tray is open)

Function: CAV - Display first picture

CLV - Start play

CAV discs: The player is started and goes to the first picture after lead-in (still mode). The positive acknowledge signal is then given.

CLV discs: The player is started and goes to the first time code after lead-in. The positive acknowledge signal is then given and normal play forward commences.

If the player is already on, this command performs a Goto the first picture, the positive acknowledge signal is given and then still (CAV) or play (CLV) occurs.

# PAUSE

Syntax: /

Code: /(47D = 2FH)

Response: None

Function: CAV - Enter still mode with audio and video muted

CLV - Pause, audio and video muted

(optical readout unit stays in current position)

# RESET TO DEFAULT

Syntax: :

Code: : (58D = 3AH)

Response: None

Function: Reset to initial conditions.

The player is reset to initial power-on conditions, except that the communication protocol remains unchanged. The STOP and INFO registers are not affected.

# PICTURE NUMBER REQUEST (CAV only)

Syntax: ?F

Codes: ? (63D = 3FH)

F (70D = 46H)

Response: Positive ack: F xxxxx

Negative ack:

X if picture no. is not available

O if disc-tray is open

Function: To return the current picture number as five ASCII digits (00001...59999).

If this command is attempted when a CLV disc is loaded, a negative acknowledge signal (X) is returned.

# CHAPTER NUMBER REQUEST

Syntax: ?C

Codes: ? (63D = 3FH)

C (67D = 43H)

Response: Positive ack: C xx

Negative ack:

X if chapter no. is not available

O if disc-tray is open

Function: To return the current chapter number as two

ASCII digits (00...79).

# DISC PROGRAM STATUS REQUEST

Syntax: ?D

Codes: ? (63D = 3FH)

D (68D = 44H)

Response: Positive ack: D x1 x2 x3 x4 x5

Negative ack:

X if disc status not available

O if disc-tray is open

Function: To return the disc program status

(as recorded on the disc).

Each status byte (x1 to x5) is in the form 0011yyyy.

These bytes are specified below:

# Response specification

# First status byte (x1)

bit 7: 0

bit 6: 0

bit 5: 1

bit 4: 1

bits 3-0: 1101 = D (Hex)

or

bits 3-0: 1011 = B (Hex)

# Second status byte (x2)

bit 7: 0

bit 6: 0

bit 5: 1

bit 4: 1

bits 3-0: 1100 = C (Hex)

or

bits 3-0: 1010 = A (Hex)

From x1 and x2:

DC = CX noise reduction present

BA = No CX noise reduction

# Third status byte (x3)

bit 7: 0

bit 6: 0

bit 5: 1

bit 4: 1

bit 3: 0 = 12" disc 1 = 8" disc

bit 2: 0 = side 1 1 = side 2

bit 1: 0 = no TXT present 1 = TXT present

bit 0: 0 = FM-FM mpx. off 1 = FM-FM mpx. on

# Fourth status byte (x4)

bit 7: 0

bit 6: 0

bit 5: 1

bit 4: 1

29