The data phase is followed by the status phase in which the player returns a single byte to the host computer indicating the success or failure of the command. In the latter case, the host computer may be able to ask the player for further information with a request sense command to determine what has gone wrong.

Finally, the player sends a command complete message to the host computer before releasing the SCSI bus. This is required by the SCSI standard, but serves no purpose for LV-DOS as all operations are synchronous (i.e. complete before the status is returned).

# VP415 issues

The VP415 SCSI interface adheres strictly to SCSI specifications for both hardware and software. The bus cable is daisy-chained in single ended mode; parity is ignored. The connector pin TERMPWR is not connected to an internal power supply.

LV-DOS supports all SCSI bus phases except the optional Reselection phase and Message Out phase, and supports arbitrary systems with multiple initiators. The 'hard reset' condition is supported by LV-DOS. Asynchronous transfer mode is the default; optional synchronous transfer mode and linked commands are not supported.

One of the values specified in the command descriptor block is the Logic Unit Number (0 - 7). This is provided by the SCSI standard to address different logic units within the same device. In the case of LV-DOS, the logic unit number is used to specify which of the volumes is to be accessed by the current command (rather like specifying one of two or more floppy drives attached to the same controller). Logic unit 7 is used for all commands not pertaining to a particular volume, including reading the volume directory. A logic unit number is assigned to a volume when it is opened.

# DEFAULT CONDITIONS

# Default start-up conditions

At power-up or reset the system is in the standby condition. To log the disc onto LV-DOS, an initial Start-unit command should be issued to the player before any other SCSI command. If, however, the first command after a hard reset is a Read command, then the Start-unit function is automatically performed prior to the read action.

After a successful execution of the Start-unit command the player will have a start-up default mode as follows:

Audio off

Remote control handset on

Index display off

Normal video on

Video mode VP3

Front panel controls enabled

Search mode R1

In addition, F-code commands issued to logic unit 7 will be executed fully transparent and F-code commands issued to other logic units will apply to the volume associated to that logic unit.

If the disc has no digital data, such as a CLV or CAV but without data, or if the execution of the automatic Start-unit command fails for any reason, then the player will be reset to the default conditions (according to the F-code specifications) and fully transparent F-code control is possible via all logic units. It is the responsibility of the initiator to select the desired player mode for the particular application. See 'Mode selection' in Section 4.

If the Start-unit command is given via SCSI, the video mode will be VP3 even if the command fails. This enables the host computer to display an error message.

# Default stop-unit conditions

A Stop-unit command from the initiator is received as an 'unload' command at the VP415, and all switches are reset to their default values (see F-code command 'Reset to default'). It is the responsibility of the initiator to send an Eject command if necessary. After a Stop-unit command, all the volumes are closed; a subsequent Start-unit command is needed to open the volumes again.

# LV-DOS COMMANDS

LV-DOS supports: all mandatory commands for read-only direct-access devices, some extended commands, and some vendor-unique commands. It should be noted that the SCSI command and reply formats supported by LV-DOS are a subset of the general SCSI definition (ANSI standard X3T9.2).

The first field in the command descriptor block is a group code (value 0 - 7). The group code defines the format of the rest of the command. LV-DOS supports Group 0 commands for reading disc data and Group 6 (vendor-unique) commands for F-code read/write commands.

# The status byte

A single status byte is returned to the host computer on completion of a command. The SCSI standard assigns meanings to each bit in this byte, of which LV-DOS uses the following subset:

bit 0 reserved, 0

bit 1 command failed, check sense status

bit 2 - 7 reserved, 0

A return value of 0 indicates that the command was successful. If a non-zero value is returned, the host computer should use the Request sense command for more details of what went wrong.

# Group 0 (6-byte) commands

The format of a Group 0 command descriptor block is as follows:

|   | (MS bit) |   |   |   |   |   |   |   | (LS bit)  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
|   | 7 | 6 | 5 | 4 | 3 | 2 | 1 | 0 |   |
|  Byte 0 | Group code (0) |   |   | Command code  |   |   |   |   |   |
|  1 | Logic unit number |   |   | Logical block address (MSB)  |   |   |   |   |   |
|  2 | Logical block address  |   |   |   |   |   |   |   |   |
|  3 | Logical block address (LSB)  |   |   |   |   |   |   |   |   |
|  4 | No. of data blocks to transfer (transfer length)  |   |   |   |   |   |   |   |   |
|  5 | Control byte (0)  |   |   |   |   |   |   |   |   |

The group code + the command code together form the operation code.

The logical block address parameter bytes apply only to Read and Write block commands. For other commands they are in general meaningless and should be set to zero unless otherwise stated.

The vendor-unique bits, reserved bits, flag bit and link bit in the control byte are not supported and should be set to zero.

There is no data in or data out phase unless otherwise stated.

38