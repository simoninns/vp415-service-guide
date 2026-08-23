# Control Routes

The control and drive section of the VP415 disc drive is determined by two modules, viz CONTROL PROCESSOR MODULE S and DRIVE PROCESSOR MODULE R. These modules determine the actions of the disc drive which is composed of a number of functional modules. See the block diagram of the control routes in Fig. CR1. The control processor and the drive processor communicate via the S-bus.

- The control processor has interactions with the outer world: via a communication similar to the RS232 bus (RS232-2 bus) with the sandwich part of the disc drive, CPU and data grabber module W and thus via the SCSI connector with a computer to be connected externally. Moreover, the RS232 connector (RS232-1 bus) is directly connected to module S. The control processor controls the remote control communication (RCS), namely the infrared or wired RCS commands, and the SCART-RCS commands. Via lines DLEN, SDAT and SCLT the control processor drives the LEDS on display + keyboard module N. On behalf of the different video mixing possibilities which are realized on video mixer module Y in the sandwich section, the control processor gives signals VP0, VP1 and VP2. The NPL signal is not used.

- The drive processor has various main tasks:

a) To accept and interpret commands from control module S
b) Radial tracking and access
c) Manchester code reading
d) Display on screen drive
e) Start-up sequence of the disc drive
f) Local control: 'stand-by' and 'eject'
g) Audio and video switching
h) Service diagnostics

sub a) Command inputs from and responses to module S go via the S-bus. Please refer to the S-bus section for detailed information on the operation of the S-bus.

sub b) During start-up the voltage on the radial mirror is studied. By means of the actual mirror position the slide is displaced, if necessary, under certain conditions. The required signals of radial module M are SP-POS and CL-RAD.

sub c) The manchester code is present in the video read from the disc and gives information on picture numbers, chapter code, stop code and CLV code. This information is necessary for the drive processor i.a. to give the index contents, search actions and instant jump. The required signals of ETBC-C module I are VMANCH, HMANCH and CL-VID.

sub d) To give index information on a connected picture screen a character generator is present on the drive processor. Synchronized to the video signal present an index background signal (VOBN) and an index information signal (VOW) are inserted in the video on module C.

sub e) Start-up sequence. The drive processor takes care of and checks the start-up procedure. After the disc has been inserted on the tray and the tray has been pushed in the start-up procedure is actuated, provided the disc drive is in stand-by. The start-up sequence has been elaborated in timing diagrams, to be seen in Fig. CR2. The numbered steps in this sequence can be found back in the block diagram of the control routes in Fig. CR1. In this way one can see in which sequence the various modules are energized by drive processor module R. In the story below the required signals have been named followed by the number corresponding with the timing diagrams.

After the start, the pushing in of the tray with 'start-stop' (ST-ST: 1) as command, we see the following:

* The pulling in of the front loader (LMOT-L: 2a) with as control the 'tray inside' (TI: 2b) signal.

* Bringing the slide to the initial position (SL-PWR: 3a and COMM-1.2.3.4: 3b) with as control the 'slide position indication' (SPI: 3c) signal.

* Detection of the presence of a disc by means of a photo-sensor and control signal 'disc reflection' (DR: 4).

* Activation of the tilt control (TLS: 5a) with as control the 'tilt ok' (TILTOK: 5b) signal.

* Switching on of the laser (LA: 6a) with as control the 'laser status' (LA-STA: 6b) signal.

* Activation of the focus control by means of the 'focus enable' (FOC-EN: 7a) signal. If focus is found, the deck electronics, module 2, give the 'focus position indication' (PR: 7b) signal to focus module J. This PR signal gives together with the zero crossing of the 'focus error' (FOC-ER: 7c) signal, the control command for the drive processor, namely the 'focus indication' (FOC-IND: 7d) signal.

* The turntable motor is brought to the correct speed after the 'turntable motor' (TTM: 8a) command. The control is the '0 rpm' (0-RPM: 8b) signal.

* The loop for the radial tracking is closed with the 'radial loop switch' (RLS: 9) signal.

* The motor is locked to the read-out video of the disc with as indication to timebase correction module I, the 'motor lock' (M-LOCK: 10) signal.

* The synchronization of the video signal of the disc is then locked to the reference source on module D with as control to the drive processor the 'frame lock' (FRLOCK: 11) signal.

* The control of the timebase correction becomes active, resulting in a correcting signal, namely the 'tangential error' (TANGER: 12) signal. This signal goes from module I to ETBC-B module H.

* The lead-in code is read by the drive processor by means of the HMANCH, VMANCH and CL-VID signals. The drive processor will give course pulses for the radial mirror up to picture 1 to radial module M, which results in the 'radial error' signal as indicated (RAD-ER: 13).

* During start-up a sync signal is present on each video and sync output, derived from reference source module D. With the 'composite video / composite sync' (CV/CS: 14) command the video read from the disc is put on the outputs. On a connected monitor a locked picture with colour will appear.

* The audio lines switch over, because of the 'audio 1 on' and 'audio 2 on' (AUD1ON, AUD2ON: 15) signals. The audio LEDs will light up just like the CAV or CLV LED, dependent on the disc.

sub f) On the front of the disc drive you will find two keys, 'eject' and 'stand-by', which pass the related commands directly to the drive processor via display + keyboard module N.

sub g) The drive processor also takes care of the switching of the audio and video signals e.g. the muting of the signals during search actions.

sub h) The diagnostic software has been integrated in the drive software in such a way that many of the tasks of the drive are checked for proper performance. If a fault is detected in the execution of a task, an error code is shown on the screen as video overlay (like the index information). The software program is very useful on behalf of service diagnosing. The working and the use of this diagnosis software will be dealt with extensively in the REPAIR METHOD description.

# S-bus

In the VP415, communication between the control module ( S ) and the drive processor module ( R ) is via the S-BUS.

The S-BUS is a synchronous communication link intended for use between a LaserVision drive and a host controller. The bus is bi-directional with handshake and is byte serial.

Bus activity is not continuous but is confined to a 'window' occurring in each video field. The window is of 8msec duration in each 20msec field period. Communications may not extend beyond the limits of the window. Execution of commands will commence following the termination of a window.

Commands are allocated a priority order:

Priority 1 More than one command may be sent during a window but only the last one accepted will be executed.

Priority 2 As for priority 1 but if a priority 1 command is included the priority 2 command will be ignored.

Priority 3 These commands will always be executed.

# Constraints on operation

For the S-BUS to operate, the video from the disc must be locked to either the internal or an external reference in both line and field. Also the Manchester codes must be readable.

# Command and response structure

The data is organised as packets each consisting of a three byte string.

A command from controller to drive processor module consists of 1 packet.

Responses may have a length of 0 to 5 packets, the length of a response being defined by a command from the controller in the form of - 05 00 0x where x is the number of packets required in the response. In the VP415 the initialising sequence calls for 4 packets.

By way of example the contents of these packets are :

Packet 1 Manchester code from line 18.

Packet 2 Byte 1 Disc loaded - CAV/CLV.

Byte 2 Player mode.

Byte 3 Error status.

Packet 3 Manchester code from line 16.

Packet 4 Byte 1 Laservision deck status.

Byte 2 Audio/video status.

Byte 3 Miscellaneous status.

If the fifth packet is requested this will contain the Manchester code from line 17.

In the case of the packets containing Manchester code information all zero's will be returned if the Manchester codes are not readable.

9

# S-bus signals

Databus:

SDG-7 SD7 is MSB.

Signals to LaserVision drive:

WREN Write enable (Write data to drive).
RDEN Read enable (Read data from drive).

Signals from LaserVision drive:

DAK Data acknowledge (Data has been read by drive).
DAV Data available.
WINDOW Drive can communicate.

CS 7 883