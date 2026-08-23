TABLE 2 - RESPONSES TO COMPUTER ON COMMANDS FROM REMOTE CONTROL HANDSET

Player commands from remote control handset when routed to host computer, after H1 command (RC to computer on), are of the form:

|  dec | hex | syntax  |
| --- | --- | --- |
|  76 | 4C | L x  |

Where x is given by the following codes:

|  STANDBY | ;  |
| --- | --- |
|  DISPLAY | !  |
|  NEXT | *  |
|  CLEAR | X  |
|  ENTER | P  |
|  START/REPEAT | F  |
|  AUDIO1 | A  |
|  AUDIO2 | B  |
|  CNR | R  |
|  PNR | D  |
|  CORR | C  |
|  GOTO | K  |
|  FAST▶ | W  |
|  FAST◀ | Z  |
|  SLOW▶ | T  |
|  SLOW◀ | U  |
|  SPEED + | H  |
|  SPEED - | G  |
|  TXT | Y  |
|  PAUSE | V  |
|  SEARCH▶ | >  |
|  SEARCH◀ | <  |
|  STILL▶ | L  |
|  STILL◀ | M  |
|  PLAY▶ | N  |
|  PLAY◀ | O  |

Similarly, when an H1 command routes RC commands to the host computer, the numeric keys of the remote control handset, will give a response of the form:

|  dec | hex | syntax  |
| --- | --- | --- |
|  86 | 56 | V x  |

Where x is the key value in ASCII:

|  DIGIT0 | 0  |
| --- | --- |
|  DIGIT1 | 1  |
|  DIGIT2 | 2  |
|  DIGIT3 | 3  |
|  DIGIT4 | 4  |
|  DIGIT5 | 5  |
|  DIGIT6 | 6  |
|  DIGIT7 | 7  |
|  DIGIT8 | 8  |
|  DIGIT9 | 9  |

Note: Each response is terminated by a carriage return(CR).

23