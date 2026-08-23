# COMMUNICATION PROBLEMS

Number : E 1

Problem : Disc drive does not accept any commands from ext.
computer after printer command <LF><CR> or
<CR><LF>.
For instance : LPRINT "F500R"

Solution : -Change mentioned command in :
LPRINT "F500R" ; CHR$(13) ;
-Adaptation of CONTROL software.
(will be released in later stage).

Introduced : -

CS 8 294