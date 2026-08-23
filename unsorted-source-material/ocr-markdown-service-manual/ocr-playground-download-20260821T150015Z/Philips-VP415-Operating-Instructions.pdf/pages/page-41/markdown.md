mixed type i.e. a disc with a mixture of data and analogue audio or other non-data signals. When the initiator tries to read from the non-data areas the media error sense key will be returned.

# 4 Hardware error

Hardware error detected in the system.

# 5 Illegal request

This is returned when an illegal or non-existing command is given, and also applies to the specific bits in the command.

# B Command aborted

This means that the target has aborted the command.

# D Volume exceeded

This means that an attempt has been made to read outside the volume associated with the specified logic unit or the logical block number exceeds the number of blocks associated with that volume.

# GROUP 6 (VENDOR-UNIQUE) COMMANDS

The format of a Group 6 command descriptor block is as follows:

|   | (MS bit) |   | (LS bit)  |
| --- | --- | --- | --- |
|   | 7 | 6 | 5  |
|  Byte |  |  |   |
|  0 | Group code (0) | Command code  |   |
|  1 | Logic unit number | not used (0)  |   |
|  2 | not used (0)  |   |   |
|  3 | not used (0)  |   |   |
|  4 | No. of data blocks to transfer (1)  |   |   |
|  5 | Control byte (0)  |   |   |

The group code + the command code together form the operation code.

The vendor-unique bits, reserved bits, flag bit and link bit are not supported and should be set to zero.

The Group 6 (vendor-unique) commands supported by LV-DOS are as follows:

|  Byte 0 (operation code) | Command name  |
| --- | --- |
|  CA | Write F-code command  |
|  C8 | Read F-code reply  |

F-code commands allow the initiator to control the LaserVision player. Some of these commands return an acknowledgement or reply code. Some return the reply code almost immediately while others return it up to several seconds later. The F-code commands and the reply codes are sent through the SCSI bus using vendor-unique read/write commands.

# CAH Write F-code command

This command allows the initiator to write an F-code to a specific logic unit. A data out phase is required, in which the F-code command is sent and terminated by a 'CR' character and null padded until the end of the block.

If there are picture numbers in the F-code command, then these picture numbers are considered to be logical picture numbers. They are numbered from zero at the beginning of the picture volume until the end of the volume, regardless of the physical location of the volume on the disc. LV-DOS adds the offset between the logical picture 0 and the physical picture address of that volume. This allows volumes with a specific LV-ROM application to be placed anywhere on a new disc without having to change the application and retrieval programs running on the initiator.

The allocation of logical pictures to a volume applies only to picture numbers, not to chapter numbers. This means that goto picture commands will be executed with a modified picture number, chapter commands are not modified. The F-code command ?F returns the physical picture number and not the logical picture number in order to avoid the problems of negative picture numbers or exceeding volume boundaries.

If a logic unit is open, then logical picture 0 is the first physical picture of the corresponding volume.

Access to a logic unit that has no volume associated with it, as defined by 'unit not ready', is not considered as an error. This allows the initiator to control video discs without LV-ROM data recorded on them. In this case LV-DOS is fully transparent and will not modify the picture numbers.

Note: If an F-code reply is needed, it must be read before another F-code command is issued to the same logic unit. Otherwise the reply will be lost.

# CBH Read F-code reply

This command allows the initiator to read the reply code from the reply code buffer for the specified logic unit in LV-DOS. If there is a reply code from the player then the reply code is sent; it is terminated by a 'CR' character and null padded until the end of the block. If there is no reply code the first character of the block is a 'CR' character. A data in phase is necessary.

If the reply code is read from the reply buffer in LV-DOS then the buffer for that logic unit is cleared. If a new F-code command is sent to the player without reading the reply code of the previous command, it will be erased and the new reply code made available. LV-DOS keeps a reply code buffer and reserves the reply code for each logic unit.

Note: This command is similar to the Group 0 Read command; the difference is only that the operation code is vendor-unique, the transfer length is one block and the logical address of the block is zero.

# Search modes

In addition to the F-code command list, there are 2 commands that control the way digital data is accessed from disc. The Fast read command will read data from disc and will stop at the position on the disc where the previous data was read. The Slow read command will return to the picture that was displayed immediately before the read command was issued. LV-DOS first reads the current picture number, performs the data read and transfer, and will then return to that picture again. While the first results in a higher performance, the latter may be more convenient in a multi-initiator environment. LV-DOS may be in either of these two modes; the Fast read and Slow read commands being a toggle between the two modes. The default mode at start-up is R1.

# SLOW READ

Syntax: R0

First code: R (82D = 52H)

Response: None

Function: Slow read mode, with picture restore after search.

Video switched on after search.

40