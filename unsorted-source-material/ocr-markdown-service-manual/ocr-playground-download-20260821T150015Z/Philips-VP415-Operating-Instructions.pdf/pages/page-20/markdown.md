# INTERACTIVE PLAY OPERATION

# INTRODUCTION

Interactive operation requires the use of a computer program. Virtually any computer with an RS232-C or SCSI interface can control the VP415 using a high-level language such as BASIC or PASCAL. The relevant connection at the rear of the VP415 should be used to connect the host computer. The required program is loaded into the computer system in the usual way.

It is not possible to simultaneously control the player via both the RS232-C and the SCSI bus. Mode selection must be made by the master (host computer) to determine the mode of communication; the player itself cannot make this selection. Initially the player is in the F-code communication mode (via RS232-C) and the SCSI bus is switched off.

# F-CODE OPERATION VIA RS232-C

This mode is automatically selected by the player unless you issue a Start-unit command, as described in Section 7 - 'SCSI operation'. The player is in the slave mode, whereby it executes the commands received from the computer, and sends back confirmatory responses.

An F-code consists of one or more 8-bit bytes, coded in ASCII, terminated by a carriage return. These codes provide interactive control of the player for the user.

# Mode selection

This is only necessary if you have selected SCSI operation and then want to switch to RS232-C operation.

The transmission protocol for RS232-C mode selection is described below. Note that carriage returns should not be sent. ACK refers to a Positive acknowledgement 'A' and NACK to a Negative acknowledgement 'N'.

1. The master sends two spaces.
2. The master awaits ACK from the player. If this is not received within 200 ms, retry.
3. The master sends the mode select byte for F-code communication, which is F.
4. The master awaits ACK from the player. If this is not received within 200 ms, retry mode selection.

See Section 5 - 'F-code programming'.

# SCSI OPERATION

SCSI operation provides communication between the player and the host computer, allowing the VP415 to be used as an LV-ROM memory device. Both data retrieval from the disc, and control of the player are possible. (It is also possible to use F-codes to control the player via SCSI.)

# Mode selection

The SCSI mode is selected by issuing a Start-unit command to the player. See Section 7 - 'SCSI operation'.

19