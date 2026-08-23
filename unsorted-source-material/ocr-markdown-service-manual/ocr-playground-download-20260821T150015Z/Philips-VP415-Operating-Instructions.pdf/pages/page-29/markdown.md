# F-CODE COMMANDS

SOUND INSERT (beep)

Syntax: !xy

First code: !(33D = 21H)

Response: None

Function: To insert a beep tone in both audio channels

The values x and y range from 0 to 9 (in ASCII). x represents the pitch (although this is fixed in the VP415) and y represents the duration of the beep (approx. 0.3-3 s).

The beep is not influenced by on/off switching of Audio channels 1 or 2, or the audio controls.

RC-5 OUTPUT VIA EUROCONNECTOR

Syntax: #xy

First code: # (35D = 23H)

Response: None

Function: The specified RC-5 command is transmitted via pin 8 of the Euroconnector, to control certain types of monitor.

The value x (40H - 5FH) defines the RC-5 system number (40H = system 0, 41H = system 1, etc.) and the value y (40H - 7FH) defines the RC-5 command number (40H = command 0, 41H = command 1, etc.)

REPLAY SWITCH DISABLE

Syntax: $0

First code: $(36D = 24H)

Response: None

Function: To disable the REPLAY switch.

REPLAY SWITCH ENABLE

Syntax: $1

First code: $(36D = 24H)

Response: None

Function: To enable the REPLAY switch.

This is the power-on default state. The replay function is only active if the REPLAY switch is ON AND it is ENABLED.

EJECT

Syntax:

Code: '(39D = 27H)

Response: O when tray is opened

Function: To stop the current action and open the disc-tray.
The response is then given and the player goes to standby.

All defaults are reloaded (except for communication protocol) and the stop and info registers are cleared.

TRANSMISSION DELAY OFF

Syntax: )0

First code: )(41D = 29H)

Response: None

Function: To switch the transmission delay off (default) when sending response characters from player.

This delay only affects the RS232-C bus.

TRANSMISSION DELAY ON

Syntax: )1

First code: )(41D = 29H)

Response: None

Function: To switch the transmission delay on when sending response characters from player.

This delay only affects the RS232-C bus. When the delay is on, response characters are sent at 20 ms intervals, resulting in a transmission rate of 50 characters per second. Such a delay may prevent loss of data if a host cannot control the handshake signal CTS (from the player) which must then be kept active continuously.

HALT (CAV only)

Syntax: •

Code: • (42D = 2AH)

Response: None

Function: Player enters still mode.

This command is not applicable to CLV discs.

HALT & JUMP FORWARD (CAV only)

Syntax: •xxxxx+yy

Codes: • (42D = 2AH)

+ (43D = 2BH)

Response: None

Function: Still picture mode for duration xxxxx times 40 ms, followed by a jump forward over yy pictures.

The function is repeated until: another mode command is received, a clear command is received, or lead-out is entered.

The following limits apply:

xxxxx > 0

yy = 1 ... 50 AND yy <= 20 X xxxxx

This command is not applicable to CLV discs.

HALT & JUMP REVERSE (CAV only)

Syntax: •xxxxx-yy

Codes: • (42D = 2AH)

-(45D = 2DH)

Response: None

Function: Still picture mode for duration xxxxx times 40 ms, followed by a jump back over yy pictures.

The function is repeated until: another mode command is received, a clear command is received, or lead-in is entered.

The following limits apply:

xxxxx > 0

yy = 1 ... 50 AND yy <= 20 X xxxxx

This command is not applicable to CLV discs.

INSTANT JUMP FORWARD

Syntax: +yy

First code: + (43D = 2BH)

Response: None

Function: Jump forward over yy pictures.

The jump is performed at the end of the first video field. Small jumps are invisible, as they can be performed within the video blanking.

After this command, the player continues its previous operation.

The following limits apply:

yy = 1...50

28