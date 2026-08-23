TABLE 3 - ACKNOWLEDGEMENTS BACK TO EXTERNAL COMPUTER

On some F-code commands, the player will return a response code to the host computer. These are summarised below.

|  dec | hex | response syntax (ASCII) | description  |
| --- | --- | --- | --- |
|  79 | 4F | O | Returned when disc-tray is opened on '(Eject) command, or when disc-tray is open and a command which expects a response is received.  |
|  83 | 53 | S | Ackn. on ON command when disc reaches correct speed.  |
|  61 | 3D | = x1 x2 x3 x4 x5 | Returned after revision level request (?=).  |
|  70 | 46 | F x1 x2 x3 x4 x5 | Returned after frame number request command (?F).  |
|  67 | 43 | C x1 x2 | Returned after chapter number request command (?C).  |
|  68 | 44 | D x1 x2 x3 x4 x5 | Returned after disc status request command (?D).  |
|  80 | 50 | P x1 x2 x3 x4 x5 | Returned after player status request command (?P).  |
|  85 | 55 | U x1 x2 x3 x4 x5 | Returned after user code request command (?U).  |
|  86 | 56 | VP1...VP5 | Returned after video mode request command (VPX).  |
|  88 | 58 | X | Returned after ?F,?C,?D or ?U when the information is not available.  |
|  65 | 41 | A 0 | Acknowledgement on FxxxxR or FxxxxQ when completed.  |
|   |  | A 1 | Acknowledgement on FxxxxN when completed.  |
|   |  | A 2 | Acknowledgement on FxxxxS when stopped.  |
|   |  | A 3 | Acknowledgement on FxxxxI when passed.  |
|   |  | A 6 | Acknowledgement on QxxN or QxxR when completed.  |
|   |  | A 7 | Acknowledgement on QxxS when completed.  |
|   |  | A 8 | Acknowledgement on TxxN when completed.  |
|   |  | A 9 | Acknowledgement on TxxI when passed  |
|   |  | A N | Negative acknowledgement: picture number, chapter number or time code in error.  |

# Notes:

1. Each response is terminated by a carriage return (CR).
2. All response characters, including leading zeros, are sent.
3. Digits (x1...x5) are in ASCII.

24