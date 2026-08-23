# TABLE 1 - F-CODE COMMAND LIST

This table lists the necessary codes to be sent by the computer to the player in order to perform each function.

|  dec | = | decimal code  |
| --- | --- | --- |
|  hex | = | hexadecimal code  |
|  char | = | character  |

|  dec | hex | char | function required  |
| --- | --- | --- | --- |
|  33 | 21 | !xy | Sound insert (beep)  |
|  35 | 23 | #xy | RC-5 command out via A/V EUROCONNECTOR  |
|  36 | 24 | $0 | Replay switch disable  |
|   |  | $1 | Replay switch enable (default)  |
|  39 | 27 | : | Eject (open the frontloader tray)  |
|  41 | 29 | )0 | Transmission delay off (default)  |
|   |  | )1 | Transmission delay on  |
|  42 | 2A | • | Halt (still mode)  |
|   |  | •xxxxx+yy | Repetitive halt and jump forward  |
|   |  | •xxxxx-yy | Repetitive halt and jump backward  |
|  43 | 2B | +yy | Instant jump forward yy tracks (max 50)  |
|  44 | 2C | ,0 | Standby (unload)  |
|   |  | ,1 | On (load)  |
|  45 | 2D | -yy | Instant jump backward yy tracks (max 50)  |
|  47 | 2F | / | Pause (halt + all muted)  |
|  58 | 3A | : | Reset to default values  |
|  63 | 3F | ?F | Picture number request  |
|   |  | ?C | Chapter number request  |
|   |  | ?D | Disc program status request  |
|   |  | ?P | Player status request  |
|   |  | ?U | User code request  |
|   |  | ?= | Revision level request  |
|  65 | 41 | A0 | Audio-1 off  |
|   |  | A1 | Audio-1 on (default)  |
|  66 | 42 | B0 | Audio-2 off  |
|   |  | B1 | Audio-2 on (default)  |
|  67 | 43 | C0 | Chapter number display off (default)  |
|   |  | C1 | Chapter number display on  |
|  68 | 44 | D0 | Picture number/time code display off (default)  |
|   |  | D1 | Picture number/time code display on  |
|  69 | 45 | E0 | Video off  |
|   |  | E1 | Video on (default)  |
|  70 | 46 | FxxxxxI | Load picture number information register  |
|   |  | FxxxxxS | Load picture number stop register  |
|   |  | FxxxxxR | Goto picture number then Still mode  |
|   |  | FxxxxxN | Goto picture number then normal play forward  |
|   |  | FxxxxxQ | Goto picture number and continue previous play mode  |
|  72 | 48 | H0 | Remote control not routed to computer (default)  |
|   |  | H1 | Remote control routed to computer  |
|  73 | 49 | I0 | Local front-panel buttons disabled  |
|   |  | I1 | Local front-panel buttons enabled (default)  |
|  74 | 4A | J0 | Remote control disabled for player control  |
|   |  | J1 | Remote control enabled for player control (default)  |
|  76 | 4C | L | Still forward  |
|  77 | 4D | M | Still reverse  |
|  78 | 4E | N | Normal play forward  |
|   |  | Nxxxxx+yy | Repetitive play forward and jump forward  |
|   |  | Nxxxxx-yy | Repetitive play forward and jump backward  |
|  79 | 4F | O | Play reverse  |
|   |  | Oxxxxx+yy | Play reverse and jump forward  |
|   |  | Oxxxxx-yy | Play reverse and jump reverse  |
|  81 | 51 | QxxR | Goto chapter and halt  |
|   |  | QxxN | Goto chapter and play  |
|   |  | QxxyyzzS | Goto chapter (sequence) and halt  |
|  83 | 53 | SxxxF | Set fast speed value, 2-40  |
|   |  | SxxxS | Set slow speed value, 2-250  |
|  84 | 54 | TxxyyN | Goto time code xx=min, yy=sec (yy=opt)  |
|   |  | TxxyyI | Load time code info register (yy=opt)  |
|  85 | 55 | U | Slow motion forward  |
|  86 | 56 | V | Slow motion reverse  |
|   |  | VPy | Video overlay (VP1 is default)  |
|  87 | 57 | W | Fast forward  |
|  88 | 58 | X | Clear  |
|  90 | 5A | Z | Fast reverse  |
|  91 | 5B | |0 | Audio-1 from internal (default)  |
|   |  | |1 | Audio-1 from external  |
|  92 | 5C | |0 | Video from internal (default)  |
|   |  | |1 | Video from external  |
|  93 | 5D | |0 | Audio-2 from internal (default)  |
|   |  | |1 | Audio-2 from external  |
|  95 | 5F | _0 | Teletext from disc off  |
|   |  | _1 | Teletext from disc on (default)  |

Notes:

1. Each command must be terminated by a carriage return (CR).

2. Digits (x,y,z) must be in ASCII; leading zeros are optional.

22