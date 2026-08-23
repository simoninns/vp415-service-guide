# PLAY FORWARD AND JUMP REVERSE (CAV only)

Syntax: Nxxxxx-yy

Codes: N (78D = 4EH)

-(45D = 2DH)

Response: None

Function: After normal play forward of xxxxx pictures, a jump back of yy pictures is performed.

This is repeated until a Clear command or another mode command is received, or lead-in or lead-out is reached.

The following limits apply:

xxxxx > 0

yy = 1...50

yy <= 20 X xxxxx

This command is not applicable to CLV discs.

# PLAY REVERSE (CAV only)

Syntax: O

Code: O (79D = 4FH)

Response: None

Function: Normal play reverse.

This command is not applicable to CLV discs.

# PLAY REVERSE AND JUMP FORWARD (CAV only)

Syntax: Oxxxxx+yy

Codes: O (79D = 4FH)

+ (43D = 2BH)

Response: None

Function: After normal play reverse of xxxxx pictures, a jump forward of yy pictures is performed.

This is repeated until a Clear command or another mode command is received, or lead-in/lead-out is reached.

The following limits apply:

xxxxx > 0

yy = 1...50

yy <= 20 X xxxxx

This command is not applicable to CLV discs.

# PLAY REVERSE AND JUMP REVERSE (CAV only)

Syntax: Oxxxxx-yy

Codes: O (79D = 4FH)

-(45D = 2DH)

Response: None

Function: After normal play reverse of xxxxx pictures, a jump back of yy pictures is performed.

This is repeated until a Clear command or another mode command is received, or lead-in is reached.

The following limits apply:

xxxxx > 0

yy = 1...50

yy <= 20 X xxxxx

This command is not applicable to CLV discs.

# GOTO CHAPTER AND HALT

Syntax: QxxR

Codes: Q (81D = 51H)

R (82D = 52H)

Response: Positive ack: A6

Negative ack: AN if Goto fails

O if disc-tray is open

Function: Search for start of specified chapter and display first picture.

When found, the first picture of the chapter is displayed and the positive acknowledge signal is given.

Note: With CLV discs, play starts at that chapter.

# GOTO CHAPTER AND PLAY

Syntax: QxxN

Codes: Q (81D = 51H)

N (78D = 4EH)

Response: Positive ack: A6

Negative ack: AN if Goto fails

O if disc-tray is open

Function: Search for start of specified chapter and commence play.

Following a successful search, normal play forward starts from the first picture of the chapter and the positive acknowledge signal is given. If the search fails, the negative response (AN) is given. Video and audio are muted during the Goto.

# PLAY CHAPTER (SEQUENCE)

Syntax: QxxyyzzS

Codes: Q (81D = 51H)

S (83D = 53H)

Response: Positive ack: A7

Negative ack: AN if Goto fails

O if disc-tray is open

Function: Play the specified chapter or sequence of chapters.

The start of the first specified chapter is searched for. When found, this chapter is played (normal play forward). When the end of the chapter is reached, the next specified chapter is searched for, and played, etc., until the last specified chapter has been played. The positive ack. signal is then given and the player either halts (CAV) or enters pause mode (CLV).

A maximum of 7 chapters is allowed in a sequence. If more than one chapter is specified, two digits per chapter must be specified.

e.g. Q3S plays chapter 3

Q0312S plays chapter 3 then 12

If a chapter search fails, a negative ack. signal is given and the chapter sequence is terminated.

During a Goto, the video and audio are muted.

# SET FAST SPEED (CAV only)

Syntax: SxxxF

Codes: S (83D = 53H)

F (70D = 46H)

Response: None

Function: Fast speed is set to the specified value.

Limits: xxx = 2...40

where 2 is normal speed

3 is 3/2 times normal speed

40 is 40/2 (i.e. 20) times normal speed.

The default value is 6, i.e. 3 times normal speed.

Fast play action is initiated with command W for forward, or command Z for reverse.

This command is not applicable to CLV discs.

33