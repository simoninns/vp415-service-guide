During the Goto action, the audio and video are muted. However, the video is not muted if the Goto can be performed within the instant jump region of 50 tracks.

If a CLV disc is loaded, the negative acknowledge signal (AN) is returned.

# GOTO PICTURE NUMBER AND PLAY (CAV only)

Syntax: FxxxxxN

Codes: F(70D = 46H)

N(78D = 4EH)

Response: Positive ack: A1

Negative ack: AN if Goto fails

O if disc-tray is open

Function: Search for picture number and commence play from that picture number.

The specified picture is searched for. When found, normal play forward commences from that picture and the positive acknowledge signal is given. If the picture number is not found, the negative response (AN) is given. During the Goto action, the audio and video are muted. However, the video is not muted if the Goto can be performed within the instant jump region of 50 tracks.

If a CLV disc is loaded, the negative acknowledge signal (AN) is returned.

# GOTO PICTURE NUMBER AND CONTINUE (CAV only)

Syntax: FxxxxxQ

Codes: F(70D = 46H)

Q(81D = 51H)

Response: Positive ack: A0

Negative ack: AN if Goto fails

O if disc-tray is open

Function: Search for picture number and continue with previous play mode from that picture number.

The specified picture is searched for. When found, the previous play mode continues from that picture and the positive acknowledge signal is given. If the picture number is not found, the negative response (AN) is given. During the Goto action, the audio and video are muted. However, the video is not muted if the Goto can be performed within the instant jump region of 50 tracks.

If a CLV disc is loaded, the negative acknowledge signal (AN) is returned.

# RC TO COMPUTER OFF

Syntax: H0

First code: H(72D = 48H)

Response: None

Function: Remote control commands NOT routed to host computer.

This is the power-on default state.

# RC TO COMPUTER ON

Syntax: H1

First code: H(72D = 48H)

Response: None

Function: Remote control commands routed to host computer.

Only one response is given for each RC command.

# LOCAL CONTROL OFF

Syntax: I0

First code: I(73D = 49H)

Response: None

Function: Disable player front-panel controls.

# LOCAL CONTROL ON

Syntax: I1

First code: I(73D = 49H)

Response: None

Function: Enable player front-panel controls.

This is the power-on default state.

# REMOTE CONTROL OFF

Syntax: J0

First code: J(74D = 4AH)

Response: None

Function: RC commands NOT executed by player.

# REMOTE CONTROL ON

Syntax: J1

First code: J(74D = 4AH)

Response: None

Function: RC commands executed by player.

This is the power-on default state.

# STILL FORWARD (CAV only)

Syntax: L

Code: L(76D = 4CH)

Response: None

Function: Halt and display next picture.

The time between two subsequent still commands (forward or reverse) must be at least 40 ms to be sure of execution. This command is not applicable to CLV discs.

# STILL REVERSE (CAV only)

Syntax: M

Code: M(77D = 4DH)

Response: None

Function: Halt and display previous picture.

The time between two subsequent still commands (forward or reverse) must be at least 40 ms to be sure of execution. This command is not applicable to CLV discs.

# PLAY FORWARD

Syntax: N

Code: N(78D = 4EH)

Response: None

Function: Normal play forward.

# PLAY FORWARD AND JUMP FORWARD (CAV only)

Syntax: Nxxxxx+yy

Codes: N(78D = 4EH)

+(43D = 2BH)

Response: None

Function: After normal play forward of xxxxx pictures, a jump forward of yy pictures is performed.

This is repeated until a Clear command or another mode command is received, or lead-out is reached.

The following limits apply:

xxxxx > 0

yy = 1...50

yy <= 20 X xxxxx

This command is not applicable to CLV discs.

32