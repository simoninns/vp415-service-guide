|  bit 3: | 0 = no program dump | 1 = program dump in audio channel 2  |
| --- | --- | --- |
|  bit 2: | 0 = normal video | 1 = video contains digital information  |
|  bit 1: | (see table below) |   |
|  bit 0: | (see table below) |   |

Fifth status byte (x5)

|  bit 7: | 0  |
| --- | --- |
|  bit 6: | 0  |
|  bit 5: | 1  |
|  bit 4: | 1  |
|  bit 3: | even parity check with bits 3, 2 & 0 of x4  |
|  bit 2: | even parity check with bits 3, 1 & 0 of x4  |
|  bit 1: | even parity check with bits 2, 1 & 0 of x4  |
|  bit 0: | 0  |

x4 bit 3, x3 bit 0, x4 bit 1 and x4 bit 0 (respectively in the table below) indicate the status of the analogue audio channels:

|   | program dump | FM multiplex | channel 1 | channel 2  |
| --- | --- | --- | --- | --- |
|  0000 | off | off | stereo  |   |
|  0001 | off | off | mono  |   |
|  0010 | off | off | no sound carriers  |   |
|  0011 | off | off | bilingual  |   |
|  0100 | off | on | stereo | stereo  |
|  0101 | off | on | stereo | bilingual  |
|  0110 | off | on | cross-channel stereo  |   |
|  0111 | off | on | bilingual | bilingual  |
|  1000 | on | off | mono | dump  |
|  1001 | on | off | mono | dump  |
|  1010 | on | off | (for future use)  |   |
|  1011 | on | off | mono | dump  |
|  1100 | on | on | stereo | dump  |
|  1101 | on | on | stereo | dump  |
|  1110 | on | on | bilingual | dump  |
|  1111 | on | on | bilingual | dump  |

### PLAYER STATUS REQUEST

Syntax: ?P

Codes: ? (63D = 3FH)

P(80D = 50H)

Response: Positive ack: P x1 x2 x3 x4 x5

Negative ack: O if disc-tray is open

Function: To return the player status.

Each status byte (x1 to x5) is in the form 01yyyyyy, where y represents a status bit. The status bytes are specified below. Zero status bits are reserved for future use.

#### Response specification

First status byte (x1)

|  bit 7: | 0  |
| --- | --- |
|  bit 6: | 1  |
|  bit 5: | 1 = normal mode (loaded)  |
|  bit 4: | 0  |
|  bit 3: | 0  |
|  bit 2: | 1 = chapter play  |
|  bit 1: | 1 = Goto action  |
|  bit 0: | 1 = Goto action  |

Second status byte (x2)

|  bit 7: | 0  |
| --- | --- |
|  bit 6: | 1  |
|  bit 5: | 0  |
|  bit 4: | 0  |
|  bit 3: | 0  |
|  bit 2: | 1 = chapter numbers exist on disc  |
|  bit 1: | 1 = CLV detected  |
|  bit 0: | 1 = CAV detected  |

Third status byte (x3)

|  bit 7: | 0  |
| --- | --- |
|  bit 6: | 1  |
|  bit 5: | 0  |
|  bit 4: | 0  |
|  bit 3: | 0  |
|  bit 2: | 1 = replay function active (switch is on and enabled)  |
|  bit 1: | 0  |
|  bit 0: | 1 = frame lock  |

Fourth status byte (x4)

|  bit 7: | 0  |
| --- | --- |
|  bit 6: | 1  |
|  bit 5: | 0  |
|  bit 4: | 1 = RS232-C transmission delay (50 char/s)  |
|  bit 3: | 1 = Remote control handset enabled for player control  |
|  bit 2: | 1 = Remote control commands routed to computer  |
|  bit 1: | 1 = Local front-panel controls enabled  |
|  bit 0: | 0  |

Fifth status byte (x5)

|  bit 7: | 0  |
| --- | --- |
|  bit 6: | 1  |
|  bit 5: | 1 = audio channel 2 enabled  |
|  bit 4: | 1 = audio channel 1 enabled  |
|  bit 3: | 1 = TXT from disc enabled  |
|  bit 2: | 0  |
|  bit 1: | 0  |
|  bit 0: | 0  |

#### USER CODE REQUEST

Syntax: ?U

Codes: ? (63D = 3FH)
U (85D = 55H)

Response: Positive ack: U x1 x2 x3 x4 x5
Negative ack: X if user code not available
O if disc-tray open

Function: To return the user code, as recorded on the disc.

One line of user code is read during lead-in at player start-up. This is saved for subsequent requests.

Each status byte (x1 to x5) has the following form: 0011yyyy (y = status bit).

The status bits (in Hex) are:

x1: 0...7
x2: D
x3,x4,x5: 0...F

#### REVISION LEVEL REQUEST

Syntax: ?=

Codes: ? (63D = 3FH)
= (61D = 3DH)

Response: Positive ack: x1 x2 x3 x4 x5

Function: To return the player firmware revision level.

30