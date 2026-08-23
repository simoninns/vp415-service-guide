The following Group 0 commands are supported:

|  Byte 0 (operation code) | Command name  |
| --- | --- |
|  00H | Test unit ready  |
|  01H | Rezero unit  |
|  08H | Read  |
|  0AH | Write  |
|  1BH | Start/Stop unit  |
|  03H | Request sense  |

# 00H Test unit ready

Allows the initiator to verify that the player is running, the disc is logged in, and that the player is ready for commands from the initiator through the logic unit selected by the host.

If the volume associated to that logic unit is open then the status byte returned will be 0. If the logic unit is not open, or the target is not ready, the status byte will be 02H. More detailed information can be obtained using a Request sense command (03H).

# 01H Rezero unit

Displays the logical picture zero of the volume that is accessed through the logic unit number of the command. If successful, the status returned is 0; otherwise the status returned is 02H.

# 08H Read

Allows the initiator to read blocks of data from the disc. The block number of the first block to be read is a logical block address, and is relative to the beginning of the data of the selected volume. There is an offset between the logical blocks within a volume and the physical blocks on the disc. This offset is added by LV-DOS to the logical block address, thus making the physical location of a volume on a disc transparent to the initiator.

If successful, a status of 0 is returned; otherwise 02H is returned. A subsequent Request sense data command reveals more information such as 'unit not ready' or 'media error'. A data in phase is required to read the logical block(s).

In search mode R1 (see later in this section) this command causes the video to switch off, since after a search the system will stop at a random picture. The video will also be switched off if the requested data is in cache. In search mode R0 the video is only muted during data retrieval, after which the previous displayed picture is shown.

# 0AH Write

The Write command is implemented so that the system may be used with operating systems that perform, for example, time and date stamping on file level when a file has been accessed. To prevent error messages from the operating system, write commands are implemented as dummy write commands without data being written to a medium. Consequently communication is enabled with operating systems with drivers for read/write media without patching of the operating system. If successful, a status of 0 is returned; otherwise 02H is returned. A data out phase is required unless the number of data blocks specified in the command is zero.

# 1BH Start/Stop-unit

Bit 0 of byte 1 = 1. Bit 0 of byte 4 = 1 for Start-unit and 0 for Stop-unit.

In response to the Stop-unit command, the disc is logged off, volumes close down, and the player goes into the standby mode. All switches are reset to their default conditions e.g. front panel controls enabled, etc. The Stop-unit command is always executed without error status. An additional 'Eject' command is required if the disc has to be changed.

The Start-unit command logs a disc on to LV-DOS and as such gives a means to perform a disc reset to default. Logging on means that the system table will be read from the disc and that volumes are opened. If the Start-unit command is successful, the status byte is 0; otherwise the status byte is 02H (sense key = 2 for 'unit not ready').

If the disc has been replaced, or a Stop-unit command issued, then a Start-unit command must be issued to ensure that LV-DOS is logged on. If for any reason the Start-unit command fails, LV-DOS will respond with a 'check condition' status byte and a Request sense command will have either sense key = 02 (unit not ready) if the drive is physically not ready, or sense key = 03 (media error) if the drive is spinning but no data can be read from the disc.

It is mandatory that these commands are used if the media has to be changed. They can be issued to any logic unit, open or closed. The Test unit ready command can be used to determine whether the player is ready with the disc running or not.

# 03H Request sense

Allows the initiator to obtain more detailed information about the execution of the previous command to the specified logic unit, regardless of whether it was successful or not.

If a command is executed for a specified logic unit, the relevant sense information is stored and will be available for a subsequent Request sense command for that logic unit only. In other words, separate sense data is maintained for each logic unit. This command can be issued to any logic unit, open or closed. It will always be executed without error status. A data in phase is required to read the sense data.

The fourth command byte specifies the allocation length for the sense data in the host; this byte should be set to zero.

Non-extended sense data (length 4 bytes) will be returned.

# Data format:

|   | (MS bit) |   | (LS bit)  |   |
| --- | --- | --- | --- | --- |
|  Byte | 7 | 6 | 5 | 4  |
|  0 | Valid | Error class (0) | Error code  |   |
|  1 | Logic unit number |   | Logical block address (MSB)  |   |
|  2 | Logical block address  |   |   |   |
|  3 | Logical block address (LSB)  |   |   |   |

The valid bit is 1 if the logical block address bytes are valid (indicating the block where the error occurred).

LV-DOS supports the following error codes (in hex):

0 No error
2 Unit not ready
3 Media error
4 Hardware error
5 Illegal request
B Command aborted
D Volume exceeded

# 0 No error

No error means that the previous command was carried out correctly.

# 2 Unit not ready

Unit not ready means that there is no volume associated with the specified logic unit after a Test unit ready, Read or Write command. This reply will also occur after a Start-unit command has failed because the drive is physically not ready (no disc, not spinning etc.).

# 3 Media error

Media error occurs if it is not possible to read data from the disc, either after a Start-unit command when the disc is CLV or CAV without digital data, or when it is attempted to read from a logged on disc of the

39