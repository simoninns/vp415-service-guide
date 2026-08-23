# SET SLOW SPEED (CAV only)

Syntax: SxxxS

Codes: S (83D = 53H)

Response: None

Function: Slow speed is set to the specified value.

Limits: xxx = 2...250

where 2 is normal speed

3 is 2/3 times normal speed

250 is 2/250 times normal speed (i.e. 5 sec per picture)

The default value is 6, i.e. 1/3 normal speed.

Slow play action is initiated with command U for forward, or command V for reverse.

For compatibility reasons, the command Sxxx is equivalent to SxxxS.

This command is not applicable to CLV discs.

# GOTO TIME CODE (CLV only)

Syntax: TxxyyN

Codes: T (84D = 54H)

N (78D = 4EH)

Response: Positive ack: A8

Negative ack: AN if Goto fails

O if disc-tray is open

Function: The specified time code is searched for and when found, normal play forward is performed.

When the specified time code is found, the positive acknowledge signal is given. If the time code is not found then the negative response is given. xx defines the minutes, and yy the seconds. Minutes are mandatory, and the seconds are optional. If the seconds are specified, the minutes must be given as a two digit number e.g. 07.

If the seconds are not specified, or a disc without line 16 manchester code is played, a search to the start of the specified minute is performed.

If performed with CAV discs, the negative response (AN) is given.

# LOAD TIME CODE INFO REGISTER (CLV only)

Syntax: xxyyl

Codes: T (84D = 54H)

I (73D = 49H)

Response: Positive ack: A9

Negative ack: AN if CAV disc

O if disc-tray is open

Function: The positive acknowledge signal is given when the specified time code is passed during normal play forward.

xx defines the minutes, yy the seconds. The minutes are mandatory, the seconds are optional. If the seconds are specified, the minutes must be given as a two digit number e.g. 07.

If the seconds are not specified or a disc without line 16 manchester code is played, the acknowledge signal appears on the first second of the specified minute.

If performed with CAV discs, the negative ack. signal (AN) will be returned immediately.

# SLOW MOTION FORWARD (CAV only)

Syntax: U

Code: U (85D = 55H)

Response: None

Function: Play forward at slow speed is started, conforming to the SxxxS setting.

This command is not applicable to CLV discs.

# SLOW MOTION REVERSE (CAV only)

Syntax: V

Code: V (86D = 56H)

Response: None

Function: Play reverse at slow speed is started conforming to the SxxxS setting.

This command is not applicable to CLV discs.

# FAST FORWARD (CAV only)

Syntax: W

Code: W (87D = 57H)

Response: None

Function: Play forward at fast speed is started conforming to the SxxxS setting.

This command is not applicable to CLV discs.

# FAST REVERSE (CAV only)

Syntax: Z

Code: Z (90H = 5AH)

Response: None

Function: Play reverse at fast speed is started conforming to the SxxxS setting.

This command is not applicable to CLV discs.

# CLEAR

Syntax: X

Code: X (88D = 58H)

Response: None

Function: CAV: Any play action is stopped and the player is put into still mode. A chapter play (sequence) is cancelled. The picture number INFO and STOP registers will be cleared. CLV: Any chapter play (sequence) is cancelled. The timecode INFO and STOP registers will be cleared.

The cancelled chapter play (sequence) does not send a response to the host computer.

# VIDEO OVERLAY

Syntax: VPy

Codes: V (86D = 56H)

P (80D = 50H)

Response: None on commands VP1 - VP5

VP1 - VP5 on command VPX

Function: To control the mode of the video processor.

y = 1...5 or X

VP1 = LaserVision video only.

This is the power-on default state.

VP2 = External (computer) RGB only.

VP3 = Hard-keyed.

External RGB overlayed on LaserVision video.

At screen positions where external RGB is

suppressed (black), LV video only is displayed.

Where the external RGB is not suppressed, only

the external RGB is displayed.

VP4 = Mixed.

Transparent overlay of external RGB and LV video.

Both images are simultaneously displayed, each at reduced intensity.

VP5 = Enhanced.

LV video is highlighted by external RGB.

At screen positions where external RGB is

black, the LV video is displayed at

reduced intensity. Where the external RGB is

not black, the LV video is displayed at normal intensity.

34