LVROM

# VP415

# LaserVision

# ROM disc drive

Operating Instructions

PHILIPS

PHILIPS

# CONTENTS

Section 1 INTRODUCTION
INSTALLATION
FEATURES OF THE VP415
CONTROLS, INDICATORS AND CONNECTIONS

Section 2 PLAYING A DISC

Section 3 SPECIAL PLAY FUNCTIONS

Section 4 INTERACTIVE PLAY
OPERATION

Section 5 F-CODE PROGRAMMING

Section 6 F-CODE COMMANDS

Section 7 SCSI OPERATION

Section 8 MAINTENANCE
TECHNICAL DATA

3122 146 10101

Printed in Belgium

1

![img-0.jpeg](img-0.jpeg)

![img-1.jpeg](img-1.jpeg)

![img-2.jpeg](img-2.jpeg)

Fig. 1: VP415 controls and connections.

2

# VP415 (front)

EJECT button

STANDBY indicator

ON/STANDBY button

EJECT indicator

PAUSE indicator

REPLAY indicator

REPEAT indicator

AUDIO 1 indicator

AUDIO 2 indicator

CAV indicator

CLV indicator

REMOTE CONTROL indicator

# VP415 (rear)

1 ON/OFF switch
2 MAINS lead socket
3 REPLAY on/off switch
4 RCIR/EURO switch
5 WIRED RC socket
6 RS232C socket
7 BAUD RATE dip switches
8 AUDIO IN (1 & 2) sockets
9 AUDIO OUT (1 & 2) sockets
10 A/VEUROCONNECTOR
11 H-SHIFT control [for Genlock]
12 CVBS OUT socket
13 SYNC OUT socket
14 CVBSIN sockets
15 SYNCIN sockets
16 RGB (TTL) IN socket
17 SCSI address dip switches
18 SCSI socket

3

# SECTION 1

Page

Fig. 1: VP415 controls and connections 2

# INTRODUCTION 5

The LaserVision System 5

Types of LaserVision disc . . . 5

Interactive use 5

# FEATURES OF THE VP415 5

RGB output / PAL-RGB decoder 5

Sync pulse generator 5

Genlock 5

CVBS output / RGB-PAL encoder 5

Electronic timebase corrector 5

Video mixing 6

Instant jump 6

Fast random access 6

Wired remote control 6

# INSTALLATION 7

Siting the player 7

Connecting the player to the mains 7

Connecting the player to a monitor 7

Fig. 2: Connection and adaptor cables 8

Connection to peripheral audio equipment 7

Remote control handset 7

Fig. 3: Inserting batteries in remote control handset 7

# CONTROLS, INDICATORS AND CONNECTIONS 9

Summary of controls 9

Summary of front-panel indicators 9

Summary of connections 9

4

# INTRODUCTION

The VP415 LaserVision player (ROM disc drive) is primarily designed for use in interactive computer-controlled systems that exploit the capabilities of LaserVision as a versatile, high-quality storage/retrieval medium. Communication between the VP415 and a controlling computer is via standard RS232-C or SCSI interfaces, both of which are fitted to the player. The player can be used with ordinary LaserVision discs containing audiovisual information, or LV-ROM discs, which contain data as well as audiovisual information. This data takes the place of the audio channel on some or all sections of the disc.

The VP415 can of course be used for direct playback of LaserVision CAV (Active play) or CLV (Long play) discs. In this respect it has extensive program control, with search and memory facilities, conveniently operated from the remote control handset.

# THE LASERVISION SYSTEM

LaserVision is the only audiovisual playback system using optical (laser beam) readout. The laser beam, concentrated to an almost inconceivably fine point (60 times finer than a gramophone stylus), reads very densely-packed information under the transparent surface of the LaserVision disc.

The picture reproduced is of high quality with 2-channel mono or stereo sound. There is no wear to the disc or 'pick-up', and the discs are extremely resistant to scratches, dust and fingerprints.

# Types of LaserVision disc

Three types of disc are available and the player will operate with any of these:

1. Normal CAV (Active play) discs spin at a constant speed of 1500 r.p.m. They have a maximum capacity of 54000 pictures per side (36 minutes played at 25 pictures per second) and offer special LaserVision effects such as still, slow-motion, reverse play, fast forward, fast reverse and goto picture or chapter number.
2. CLV (Long play) discs spin at a speed which gradually decreases as the disc plays. They offer continuous forward play only, but with time and chapter search, and the advantage of an increased playing time of 1 hour per side.
3. LV-ROM. This is a type of CAV (Active play) disc, with data replacing some or all parts of the audio track. Their maximum capacity is 324 Mbytes of user data and 54000 pictures.

# INTERACTIVE USE

The VP415 allows all the facilities of the LaserVision system to be controlled by a computer. In this way, the computer can control the picture, sound and LV-ROM data. Play is controlled by picture numbers, chapter numbers, autostops or a computer program. The program can be activated by the VP415 remote control handset, or via the computer keyboard, or other computer peripheral.

Communication with the VP415 is achieved using either a special code known as F-code, or LV-DOS commands (via the SCSI interface).

The F-code instruction set enables commands to be sent (as ASCII characters) to the player; some of these commands causing responses to be returned to the computer. Using F-code commands, a VP415 can participate in an interactive program with any computer system that is loaded with the necessary program.

LV-DOS commands allow the VP415 to be used as an LV-ROM memory device in a computer system. Both data retrieval from disc and player control are possible.

# FEATURES OF THE VP415

# RGB output/PAL-RGB decoder

The VP415 allows the best possible picture quality to be obtained from a LaserVision disc, by employing a built-in PAL-RGB decoder. Within the LaserVision format, video information is stored on the disc in PAL encoded form. This can cause problems when the disc is played in 'still frame' or 'slow motion', or any other non-standard playing mode, because the PAL 8-field sequence becomes destroyed. In order to correct this sequence such that a monitor can understand it and reproduce correct colour, many players incorporate a 'PAL Modifier'. This piece of circuitry corrects the PAL sequence, but in doing so, reduces the video bandwidth, and introduces other unwanted effects, e.g. echoes.

The VP415 tackles this problem by employing a fast-locking PAL-RGB decoder. Having this device built-in, allows its characteristics to be fully optimised to give the highest possible picture quality from the disc, even in non-standard playing modes.

The result is an RGB output giving the full 5 MHz video bandwidth in all playing modes. The benefit is particularly valuable when viewing video material such as maps with fine text.

RGB output also lends itself to simpler mixing with computer graphic output (also RGB), in external equipment if required.

# Sync pulse generator

The VP415 contains an internal sync pulse generator (SPG) which may either free-run, or in the presence of a suitable reference signal, lock itself to the external reference (Genlock).

The SPG provides freshly-generated line and field sync pulses at the player's video output at all times. Following the decoding process from PAL to RGB (see above), fresh sync pulses are inserted into the RGB signal, which is available at the Euroconnector socket. Therefore a stable output from the player is guaranteed at all times.

# Genlock

Genlock allows the field and line sync pulses from the player output to be synchronised with an external reference signal. It ensures correct overlay of video signals and can also prevent picture jump or roll. The reference signal, comprising line and field syncs (negative-going) should be applied to (i) either of the two SYNC IN sockets or (ii) pin 4 of the RGB (TTL) IN socket. A horizontal shift of the overlay picture is achieved by adjusting the H-SHIFT control situated at the rear of the player.

Note: The player may take up to 2 seconds initially to effectively lock to a reference signal.

# CVBS output/RGB-PAL encoder

The VP415 contains an RGB-PAL encoder. This takes the RGB output from the player (prior to the video mixing stage) and encodes it into a CVBS signal using fresh sync pulses from the internal SPG. The signal available at the CVBS output is thus totally stable. It does however have a reduced bandwidth in all playing modes (approx 3 MHz).

# Electronic timebase corrector

A C.C.D. (charge coupled device) timebase corrector is employed to provide correction of timing errors always present in the signal read from the video disc. This replaces the more traditional tangential mirror (mechanical method) allowing for a smaller, lighter optical system. This reduction in mass allows the optical readout unit to track the disc faster and thus reduces picture access time.

5

# Video mixing

The VP415 has a built-in video mixer which is able to mix either the RGB signal derived from the video disc (via the PAL-RGB decoder) or an RGB signal derived from an external video signal (connected to one of the CVBS IN sockets), with an external TTL RGB signal from the RGB (TTL) IN socket.

This facility allows the TTL RGB graphics output of an external computer to be mixed with the off-disc video (or external video) in a number of ways. The mixed video is available at the Euroconnector socket:

Mode 1: Player RGB only

Mode 2: Computer RGB only

Mode 3: Key mode

Player output: 100% intensity

Computer output: 100% intensity

Mode 4: Mixed mode (transparent graphics)

Player output: 62% intensity

Computer output: 38% intensity

Mode 5: Enhanced video - 'highlighting'

(presence of graphics produces 100%

intensity video at that point;

elsewhere video is reduced)

Player output (in presence of graphics):

100% intensity

Player output (No graphics):

57% intensity

When mixing in this manner, the VP415 'genlocks' to the composite sync signal from the external computer.

# Instant jump

The VP415 also incorporates an 'Instant Jump' feature. Essentially this means that the radial mirror which points the laser beam at the required disc track can be made to 'twitch' and therefore jump a predetermined number of tracks (max. 50) in either direction during the vertical interval (field flyback time). Small jumps are invisible, as they can be performed within the video blanking. This gives the effect of an instant search to the required picture - almost as if it were immediately adjacent to the current picture.

This feature is valuable in for example map-walking, where each picture contains a map of an area and each successive picture shows adjacent areas. The user can 'scan' across map boundaries with no 'black picture' between maps while the player searches for the next picture.

It is also possible to interleave programmes on the disc such that by playing the disc and missing out (jumping over) every alternate picture, one particular storyline is followed, and then by offsetting this process by one picture, another storyline is immediately accessed and followed.

It must be realised that following a jump, the optical slide requires a finite time to 'catch up' and centralise the radial mirror. Thus a limit is imposed on how many jumps may be made in a given time. The limit occurs when the effective playing speed of the disc exceeds 20 times normal speed, i.e. it is possible to jump 20 tracks, display for a period of 1 picture, then jump another 20 tracks etc. continuously, without the optical slide falling behind.

Details of the types of jump possible, and their associated commands are given in the F-Code command list (see Section 6).

# Fast random access

The VP415 features a very fast random access time; this is the time needed for the optical readout unit to move from one point on the disc to another, which may be anywhere on the disc. Figures are typically 1 s for a CAV disc and 5 s for a CLV disc.

# Wired remote control

In some applications it may be required to hide the VP415. In such cases, the infra-red beam of the remote control handset may not be able to operate. For reliable working under such conditions, the wired connection should be used between the remote control handset and the WIRED RC socket at the rear of the player.

6

# INSTALLATION

# SITING THE PLAYER

Stand the player on a firm level surface, ensuring that the ventilation slots on the top and sides of the player are not obstructed. Do not stand a monitor directly on top of the player if this obstructs these ventilation slots; in this case, a properly designed rack should be used to support the monitor. Never stand the player directly on any electronic equipment that gives off a substantial amount of heat, or near to any heat source. Avoid any position where the player is subjected to direct sunlight for long periods.

# CONNECTING THE PLAYER TO THE MAINS

The VP415 is designed to operate from a 50/60 Hz a.c. mains supply with any voltage between 220 and 240 V. If your local mains supply does not fall into this category, contact your nearest Philips Organisation.

If necessary, fit a mains plug to the mains lead as described below.

Important note for U.K. users

WARNING: THIS APPARATUS MUST BE EARTHED

The wires in the mains lead are coloured in accordance with the following code:
Green-and-yellow: Earth

Blue: Neutral

Brown: Live.

These colours may not correspond with the colour markings identifying the terminals in your plug, so proceed as follows: Connect the Green-and-yellow wire to the terminal marked E or 1/2, or coloured Green or Green-and-yellow; Connect the Brown wire to the terminal marked L, or coloured Red; Connect the Blue wire to the terminal marked N, or coloured Black.

Insert the mains plug into a wall socket. If the player is not to be used for a long period of time, remove the mains plug from the wall socket.

# CONNECTING THE PLAYER TO A MONITOR

The VP415 has outputs suitable for both RGB monitors and CVBS monitors. Various connection possibilities are described below. Also refer to Fig. 2 - 'Connection and adaptor cables'.

Note: Some monitors have a 'time-constant' switch for use with a VCR; this should be set to the 'normal' (i.e. non-VCR) position for LaserVision use.

# Euroconnector to Euroconnector

This is a direct connection, ensuring the highest quality picture and, if the monitor is equipped for it, stereo sound.

It is also possible to use a TV receiver if it is fitted with a Euroconnector socket.

Connect the cable supplied between the A/V EUROCONNECTOR socket on the rear of the player and the corresponding socket on the monitor.

![img-3.jpeg](img-3.jpeg)

This connection carries both RGB and CVBS signals. Optimum picture quality is obtained if the RGB signals are used. Therefore if the monitor accepts both RGB and CVBS signals, ensure that it is switched to RGB input.

If no Euroconnector socket is available:

1. Euroconnector-to-DIN AV (audio/video) - CVBS only

If the monitor is fitted with a 6-pole DIN AV (Audio-Video) socket, the Euroconnector-to-DIN AV adaptor cable SBC 1012 (4822 321 20485, length 1.5 m) must be used. Connect the Euroconnector plug to the A/V EUROCONNECTOR socket of the player and the DIN AV plug to the monitor.

2. If the monitor is fitted with a coaxial BNC-type video input socket, there are two possibilities:

a. Euroconnector-to-BNC - CVBS only

Using Euroconnector-to-BNC adaptor cable SBC 1013 (4822 321 20484, length 1.5 m), connect the Euroconnector plug to the A/V EUROCONNECTOR socket of the player and one coaxial BNC plug to the video input of the monitor. Connect the 5-pole DIN Audio plug of this adaptor cable to the Audio input socket of your monitor or to an audio amplifier.

b. BNC-to-BNC (coaxial) - CVBS only

Using BNC-to-BNC connection cable SBC 1015 (4822 320 11003, length 1.5 m), connect between the CVBS OUT socket of the player and the video input of the monitor. The Audio signal must be taken from the AUDIO OUT sockets of the player using a connection cable SBC 044 (4822 321 20344, length 10 m).

# CONNECTION TO PERIPHERAL AUDIO EQUIPMENT

The AUDIO OUT sockets on the rear of the player can be connected through connection cable SBC 043 (4822 321 20308, length 2.5 m) or SBC 044 (4822 321 20344, length 10 m) to a linear input of the peripheral equipment. Either or both sound channels may be switched on or off by means of the AUDIO 1 and AUDIO 2 buttons on the remote control handset.

If a disc contains stereo sound, this will be reproduced stereophonically when both channels are in operation.

Note: If either audio channel is switched off, then the remaining audio signal is routed to both output channels. This avoids 'one-sided' sound from a dual-language disc.

# REMOTE CONTROL HANDSET (Figs. 1 and 3)

Normally, the VP415 operates by remote control from the infra-red remote control handset supplied. The control buttons on this handset have been grouped into logically-related sections.

The remote control handset controls all play functions, audio and memory controls and also accesses specified program parts.

The handset can be used in conjunction with the infra-red detector on the VP415 itself, or, when a Euroconnector connection is used, with the infra-red detector on the monitor (dependent on actual monitor model). In the latter case, the RC IR/EURO switch on the rear of the VP415 (see Fig. 1) must be set to EURO.

When using the handset, point it directly at the infra-red detector on the front of the player (or monitor). If this is not possible, or not convenient, the remote control cable supplied can be connected between the handset and the player (see 'Wired remote control' earlier in this section). The handset requires 4 X 1.5 volt batteries, type R03 or UM4, located in its base (See Fig. 3).

![img-4.jpeg](img-4.jpeg)

Fig. 3: Inserting batteries in remote control handset.

7

![img-5.jpeg](img-5.jpeg)

![img-6.jpeg](img-6.jpeg)

![img-7.jpeg](img-7.jpeg)

![img-8.jpeg](img-8.jpeg)

![img-9.jpeg](img-9.jpeg)

Fig. 2: Connection and adaptor cables.

8

# CONTROLS, INDICATORS AND CONNECTIONS (Fig. 1)

# SUMMARY OF CONTROLS

# Front of player

- EJECT button

For opening the disc-tray and ejecting a disc if one is loaded.

- ON/STANDBY button

For switching between 'standby' and 'on' modes. This button also effects a CPU reset.

# Rear of player (numbers refer to Fig. 1)

- ON/OFF switch (1)

Primary mains power switch.

- REPLAY on/off switch (3)

Switches the replay function on or off. See 'Replay' in Section 3.

- RC IR/EURO switch (4)

To switch between remote control commands being received directly by the VP415 (IR) or via the monitor (EURO).

- BAUD RATE dip switches (7)

For selecting the baud rate for RS232-C communication. See Section 5 - 'F-code programming'.

- H-SHIFT control (11)

To shift the horizontal position of the picture when using an external sync signal (connected to either of the SYNC IN sockets). See 'Genlock' in Section 1.

- SCSI address dip switches (17)

To set the SCSI bus address of the player. See Section 7 - 'SCSI operation'.

# SUMMARY OF FRONT-PANEL INDICATORS

The following indicators give status information about the VP415:

STANDBY (red) Lights in standby mode and flashes during start-up.

EJECT (green) Flashes during eject.

PAUSE (green) Lights during pause.

REPLAY (green) Lights when replay function is active.

REPEAT (green) Lights when repeat function is active.

AUDIO 1 (green) Lights when audio channel 1 is enabled.

AUDIO 2 (green) Lights when audio channel 2 is enabled.

CAV (green) Lights when playing CAV discs.

CLV (green) Lights when playing CLV discs.

REMOTE CONTROL (green) Flashes to confirm that player is receiving a remote control command.

# SUMMARY OF CONNECTIONS (numbers refer to Fig. 1)

- MAINS lead socket (2)

For connection of the mains lead.

- WIRED RC socket (5)

For wired connection of the remote control handset, using the remote control cable supplied. This permits the remote control to be used when the VP415 is hidden from view. (See 'Wired remote control' in Section 1.)

- RS232C socket (6)

Provides a serial connection for an external computer.

- AUDIO IN (1 and 2) sockets (8)

Used for connection of an external stereo or 2-channel sound source. AUDIO L = AUDIO 1;

AUDIO R = AUDIO 2.

- AUDIO OUT (1 and 2) sockets (9)

Used for connection of an external stereo or 2-channel sound source.

AUDIO L = AUDIO 1;

AUDIO R = AUDIO 2.

- A/V Euroconnector (10)

Provides connection for variety of inputs and outputs for a monitor. See Section 8 - 'Technical data' for full details.

- CVBS OUT socket (12)

Provides a video signal output suitable for a monitor. For further information, refer to 'CVBS output / RGB-PAL encoder' in Section 1.

- SYNC OUT socket (13)

Provides a synchronising signal for the host computer or a second VP415 connected in parallel.

- CVBS IN sockets (14)

These two sockets are internally connected; either of them may be used. They accept an external video input signal, e.g. from a second VP415. The signal may be looped through to other equipment using the second CVBS IN socket. If no such loop is used, the second socket must be properly terminated with a 75 ohm plug. To lock the CVBS signal to an external RGB signal (for mixing purposes), it must be looped through to one of the SYNC IN sockets.

- SYNC IN sockets (15)

These two sockets are internally connected; either of them may be used. They accept an external video synchronising signal which may be looped through to other equipment using the second SYNC IN socket. If no such loop is used, the second socket must be properly terminated with a 75 ohm plug.

Note: The reference signal must conform to broadcast standards in respect of pulse-shape and timing (a standard CVBS signal is suitable).

- RGB (TTL) IN socket (16)

DIN RGB input socket for video and sync input from an external computer. Refer to Section 8 - 'Technical data' for further details.

- SCSI socket (18)

Provides a connection to an external computer according to SCSI standards. Refer to Section 8 - 'Technical data' for further details.

9

SECTION 2

Page

PLAYING A DISC 11

Switching on 11

Inserting a disc 11

Automatic play 11

To stop play and remove the disc 11

10

# PLAYING A DISC (Refer to Fig. 1)

# SWITCHING ON

Switch on the player using the mains ON/OFF switch located at the rear. Check that the REPLAY switch is in the OFF position. The STANDBY indicator will light.

Press the ON/STANDBY button; the STANDBY indicator will then flash. A warning 'beep' is given to indicate that no disc has yet been loaded.

Note: The VP415 contains a fan to maintain correct operating temperature. If a certain temperature is exceeded, the speed of this fan will automatically increase; this is quite normal and not a fault indication.

# INSERTING A DISC

Press the EJECT button; the disc-tray will partly open. Pull out the disc-tray all the way. Remove the disc from its packaging and place it on the disc-tray with the desired label uppermost.

# AUTOMATIC PLAY

Gently push the disc-tray forward; it will be drawn inside automatically. The disc will build up to speed (1500 r.p.m.) in approx. 10 seconds. During the start-up period, the STANDBY indicator flashes.

As soon as the correct speed has been reached, the STANDBY indicator goes out and either the CAV or CLV indicator lights, according to the type of disc loaded. Play then commences. Also refer to Section 3 - 'Special play functions'.

When the end of the disc is reached, the player returns rapidly to the first track, gives a warning 'beep', and enters the pause mode. If no further command is given within 2 minutes, the player goes to standby.

If repeated playing of the disc is required, the REPLAY switch should be in the ON position. This will be confirmed by the REPLAY indicator. In this case, the controls on the front of the player are disabled.

# TO STOP PLAY AND REMOVE THE DISC

To terminate play at any time, press the EJECT button on the front of the player. When the disc comes to a standstill, the player ejects the disc and goes to the standby condition.

11

SECTION 3

Page

# SPECIAL PLAY FUNCTIONS 13

Standby 13

Play forward 13

Play reverse 13

Still 13

Step forward and reverse 13

Picture number, chapter number and time code display 13

Fig. 4: Picture number display 13

Fig. 5: Chapter number display 13

Fig. 6: Time code display 13

Player and disc status display 13

Fig. 7: Player and disc status display 13

Search 13

Pause 13

Slow 14

Fast 14

Audio 14

Goto picture number 14

Goto chapter number 14

Goto time position 14

Programming 14

Fig. 8: Programming display 14

Picture segment program entry 15

Chapter program entry 15

Time segment program entry 15

Playing a programmed sequence 15

Start/repeat 15

Replay 15

TXT button 16

12

# SPECIAL PLAY FUNCTIONS

All the functions described in this section may be performed using the remote control handset. Some functions have different effects depending upon the present mode (e.g. whether the player is currently playing a disc or not). CAV (Active play) and CLV (Long play) discs also have certain commands which can only be used with that type of disc.

If the remote control handset does not function, check that the RC IR/EURO switch on the rear of the player is in the IR position.

# STANDBY (also ON/STANDBY control on player)

Pressing this button during any play operation will cause the current action to cease. The player goes to the standby mode. Any on-screen display goes out and the STANDBY indicator on the front of the player lights. If programming was in progress, it is terminated. Pressing any playing mode button while the player is in standby, causes the player to commence that action.

Note: If the replay function is in operation, the STANDBY button is disabled.

# PLAY FORWARD

Pressing the ▶ section of the PLAY button starts forward play (at normal speed).

# PLAY REVERSE (CAV only)

Pressing the ◀ section of the PLAY button starts reverse play (at normal speed).

# STILL (CAV only)

When either section of the STILL button is pressed, the picture becomes stationary. A still picture is useful for the close examination of a situation (for example, in sport), or the study of details (in an instructional programme). It can also serve as a short interlude during playback.

# STEP FORWARD AND REVERSE

If the ▶ or ◀ section of the STILL button is pressed, the following or preceding picture appears respectively.

# PICTURE NUMBER, CHAPTER NUMBER AND TIME CODE DISPLAY

Each individual picture on a CAV disc has a number which is encoded on the disc. Discs may also be divided into chapters; these chapter numbers are also encoded on the disc. To display the current picture number on the monitor screen (Fig. 4), press the PNR button. The play mode is also displayed. Press the button again to remove the display. To display the chapter number on the screen (Fig. 5), press the CNR button. Press it again to remove the display.

STILL

PNR

1642

Fig. 4: Picture number display.

PLAY FWD

CNR 2

Fig. 5: Chapter number display.

In CLV discs, an elapsed time code is encoded on the disc. This time code may be in minutes only or in minutes and seconds, depending on the particular disc. Some CLV discs are also divided into chapters, and these chapter numbers encoded on the disc.

To display the current elapsed time on the screen (Fig. 6), press the PNR button. Press it again to remove the display.

To display the chapter number on the screen (Fig. 5), press the CNR button. Press it again to remove the display.

PLAY FWD TIME 11:23

Fig. 6: Time code display.

# PLAYER AND DISC STATUS DISPLAY

Pressing the DISPLAY button will cause the player and disc status to be displayed on the screen. Disc status (e.g. CAV/CLV, side, size, etc.) is shown on the right and player status (e.g. play mode) on the left. Pressing the button again switches the display off.

If, however, the picture number etc. was being displayed on the screen, the player enters the programming mode. See 'Programming' later in this section.

|  VIDEO | ON | STEREO  |
| --- | --- | --- |
|  AUDIO1 | ON |   |
|  AUDIO2 | ON |   |
|  SLOW 1/3 |  | CAV  |
|  FAST 3 |  | SIDE 1  |
|  9600 BAUD |  | 30 CM  |

Fig. 7: Player and disc status display.

# SEARCH

If only a part of a disc is required, it can be quickly found using the SEARCH button. Pressing and holding the appropriate section of this button moves the optical readout unit in the desired direction at approximately 20 times normal speed.

During this search action you will see on the screen a very rapid succession of pictures from the programme.

When the button is released, the player reverts to the mode which it was in prior to searching.

It is often useful to have the picture number etc. displayed while searching.

When searching a CAV disc containing chapter numbers and these numbers are being displayed, the player automatically reverts to its previous mode when it reaches the next chapter.

If it is desired to continue searching this next chapter, release the SEARCH button and press again. Searching then continues to the next chapter.

If chapter numbers are not being displayed, searching is uninterrupted throughout the disc.

With CLV discs, the SEARCH button operates in the same way as for CAV discs, but the display shows the elapsed time or chapter number, as appropriate.

# PAUSE

When the PAUSE button is pressed, both audio and video are muted and the PAUSE indicator lights.

To resume the previous action, press the PAUSE button once more. While in the pause mode, other functions may also be started by pressing the appropriate buttons (e.g. PLAY, STILL, SEARCH etc.).

13

# SLOW (CAV only)

Forward or reverse slow motion is obtained by pressing the SLOW button. The slow motion speed may be altered by means of the SPEED + and SPEED - buttons.

The speed can be adjusted in steps to 1/3, 1/10, 1/25, 1/50 or 1/100 of the normal speed (which is 25 frames per second); 1/3 of normal speed is the default value.

# FAST (CAV only)

Each time the ▶ or ◀ section of the FAST button is pressed, the optical readout unit moves at 3 (default value), 10 or 20 times its normal speed in forward or reverse, the effect on the screen being that of rapid motion. The speed is set using the SPEED + and - buttons.

# AUDIO

The LaserVision disc contains not only picture information, but can also accommodate two sound channels. These can provide stereo sound, or separate sound channels; for example, a commentary in two languages. Note that LV-ROM discs can contain data in place of the audio. In this case the audio is automatically muted.

When the player is switched on, it always assumes the forward play mode, with both sound channels enabled. In the case of separate sound channels, you can switch one of them off by pressing the relevant AUDIO button (1 or 2). In this case the enabled audio channel appears at both outputs.

To switch on again, press the appropriate button; the enabled channels are indicated by the AUDIO 1 and AUDIO 2 indicators on the front panel.

Note: Sound is audible in the forward play mode only.

# GOTO PICTURE NUMBER (CAV only)

1. If no picture number is currently displayed on the monitor, press the PNR button. A picture number appears.
2. Press the digit buttons (max. 5) corresponding to the picture number you want to go to (e.g. 2, 2, 1, 3, 5, if you want picture number 22135). If you make a mistake, press the CORR button and start again. As soon as you press the first digit the player assumes the still mode. The number you select is displayed below the current picture number.
3. Press the GOTO button. The player will quickly look for the number selected. During this action sound is muted, and the monitor screen is blank, but the selected number is displayed. On arrival at the selected picture number, the corresponding picture appears on the monitor in still mode. Now you can select any play mode by pressing the corresponding button.

# GOTO CHAPTER NUMBER

1. If no chapter number is currently displayed on the monitor, press the CNR button. The chapter number, if available on the disc, appears.
2. Press the digit buttons (max. 2) corresponding to the chapter number you want to go to (e.g. 2 if you want chapter 02). If you make a mistake, press the CORR button and start again. Note that with CAV discs, the player assumes the still mode as soon as you press the first digit. The number you select is displayed below the current chapter number.
3. Press the GOTO button. The player quickly looks for the first picture of the chapter selected. During this action, sound is muted and the monitor screen is blank. On reaching the required chapter, the player starts normal play forward.

# GOTO TIME POSITION (CLV only)

With CLV discs it is possible to go to a selected time position on the disc.

1. If no time position is currently displayed, press the PNR button. A time position appears on the screen.
2. Press the digit buttons corresponding to the minutes of the time position you want to go to; the number you select is displayed below the time code. If you make a mistake, press the CORR button and start again. Then press the ENTER button. Some new discs also allow you to enter seconds as well. To enter the seconds, again use the digit buttons followed by ENTER.
3. Press the GOTO button. The player will quickly look for the number selected. During this action sound is muted, and the selected time position is displayed. On arrival at the selected time position, play starts from that point.

# PROGRAMMING

It is possible to set up a sequence of picture numbers, chapter numbers or time codes by programming via the remote control handset.

1. Press either PNR (for picture number or time code programming) or CNR (for chapter number programming), so that the display appears on the screen.
2. Press the DISPLAY button. The current program (if any) is then displayed on the screen. See Fig. 8.

|  PROGRAM 1 PNR | 1642  |
| --- | --- |
|  1000 PLAY FWD | 2000  |
|  3200 FAST* 10 | 4500  |
|  2500 PLAY REV | 1000  |
|  51000 SLOW: 50 | 51500  |
|  2569 STILL 60 | 2579  |

|  PROGRAM | CNR | 2  |
| --- | --- | --- |
|  1.CNR 5 | 9.CNR |   |
|  2.CNR 7 | 10.CNR |   |
|  3.CNR 9 | 11.CNR |   |
|  4.CNR 16 | 12.CNR |   |
|  5.CNR 18 | 13.CNR |   |
|  6.CNR 20 | 14.CNR |   |
|  7.CNR | 15.CNR |   |
|  8.CNR | 16.CNR |   |

|  PROGRAM 1 TIME | 1:23  |
| --- | --- |
|  12:45 PLAY FWD | 17:20  |
|  23:00 PLAY FWD | 28:25  |
|  45:22 PLAY FWD | 56:55  |
|  58:00 PLAY FWD | 59:16  |

Fig. 8: Programming display.

14

The player is now in the programming mode. You are able to modify the existing program or enter a new program. A flashing cursor indicates the current entry position on the program table. The contents at this position may be changed.

# Picture segment program entry

A picture segment program may be up to two pages long, each page consisting of 8 segments. A segment is displayed as one line on the screen.

e.g. 15000 PLAY FWD 20500

Picture numbers may either be entered directly (using the 0 - 9 digit buttons) and then pressing ENTER, or by storing the current picture number. To correct numbers entered directly, use the CORR button. When the cursor is in an empty picture number position, the player can be controlled in the usual way with the PLAY, SLOW, FAST and STILL buttons. If during play you press the ENTER button, the player halts and the current picture number is stored.

The required action (PLAY, STILL, etc.) is selected by pressing the corresponding button on the remote control handset and then pressing ENTER. Until ENTER is pressed, the action may be changed simply by pressing another button instead.

With some functions (e.g. SLOW), extra information, such as the speed, may also be entered (e.g. 10 for 1/10 normal speed). Note that for STILL, it is necessary to enter the duration (in seconds). Pressing the ENTER button moves the cursor to the next entry position. If no action is entered, PLAY is assumed.

The program is displayed on the screen below the playing mode. To move on to the next line of the program, press the NEXT button. Pressing this button on the last line of the program moves the cursor back to the first line again.

To clear the program displayed, press both CLEAR buttons at the same time.

To move to the start of page 2 while page 1 is displayed, press the DISPLAY button. Pressing the DISPLAY button when on page 2 ends programming and returns to normal play mode.

To play this sequence see 'Playing a programmed sequence' below.

The program is saved by the player until it is cleared (by pressing both CLEAR buttons when the program is displayed) or until it is updated.

# Chapter program entry

This is performed in a similar way to 'Picture segment program entry' described above. Up to 16 chapters may be stored in any order; repetition of a chapter in the program is also allowed. Chapter numbers must be entered directly using the 0 - 9 digit buttons. To correct an entry, use the CORR button.

The ENTER and NEXT buttons both move the cursor to the next line, except when at the last line, when they move the cursor to the first line again.

To clear an entire sequence, press both CLEAR buttons at the same time.

To end programming mode, press DISPLAY. Any empty positions in the chapter sequence will be ignored when the sequence is played back.

To play this sequence see 'Playing a programmed sequence' below.

The program is saved by the player until it is cleared (by pressing both CLEAR buttons when the program is displayed) or until it is updated.

# Time segment program entry

This is carried out in a similar way to 'Picture segment program entry' described above. A time segment sequence may be up to 2 pages long, each page consisting of 8 segments. The format is:

time 1 PLAY FWD time 2

Where the time is in minutes and seconds (e.g. 23:30).

The time is entered either directly, using the 0 - 9 digit buttons, or by storing the current time position during play. If during play you press the ENTER button, the current time position is stored. When entering the time directly, the CORR button may be used for correction. Depending on the disc used, the seconds entered may be ignored.

To move on to the next line of the program, press the NEXT button. Pressing this button on the last line of the program moves the cursor back to the first line again.

To clear the complete program, press both CLEAR buttons at the same time.

To move to the start of page 2 while page 1 is displayed, press the DISPLAY button. Pressing the DISPLAY button when on page 2 ends programming and returns to normal play mode.

To play this sequence see 'Playing a programmed sequence' below.

The program is saved by the player until it is cleared (by pressing both CLEAR buttons when the program is displayed) or until it is updated.

# Playing a programmed sequence

To play a sequence which has been stored in the memory as described above, press the START/REPEAT button, while the picture number etc. is displayed on the screen. The player quickly searches for the first picture of the sequence stored and then starts the required action. The actions stored are carried out successively in the order in which they are stored. At the end of the last item the player halts (CAV) or goes to pause (CLV). During search actions between items, sound is muted and the screen is blank.

A sequence can be stopped by pressing any action button (e.g. Play, Fast, Still).

# START/REPEAT

Pressing the START/REPEAT button either starts playing a programmed sequence (if one has been set up) while the picture number etc. is displayed on the screen, or starts playing the entire disc from the start. If the button is pressed again, play returns once more to the start of the disc or programmed sequence.

# REPLAY

The REPLAY switch is situated at the rear of the player.

If the player is switched on when the REPLAY switch is on, the player automatically starts up in the replay mode. If the player is already on and the REPLAY switch is switched on, play immediately starts at the beginning of a programmed sequence, or returns to the start of the disc.

In the replay mode, the player is in a continuous play loop. If a programmed sequence is in memory, that sequence will be played over and over again. (A picture number or time code sequence has priority over a chapter number sequence.) If there is no sequence in memory, the whole disc will be played over and over again. The REPLAY indicator on the front of the player lights.

Note: In the replay mode, all controls except the following are disabled:

15

START/REPEAT, which moves play back to the start of the sequence (or disc).

NEXT, which moves play to the next segment (or chapter) in a sequence.

PNR and CNR

AUDIO 1 & 2

TXT

To exit the Replay mode, press the REPLAY switch at the rear of the player.

# TXT BUTTON

This button is only effective if the player is connected to a TV set with Teletext and Euroconnector remote control facilities.

Pressing the TXT button switches the monitor display between: TV mode, TXT mode and mixed mode.

16

17

SECTION 4

Page

# INTERACTIVE PLAY OPERATION 19

Introduction 19

F-code operation via RS232-C. 19

Mode selection 19

SCSI operation 19

Mode selection 19

18

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

SECTION 5

Page

# F-CODE PROGRAMMING 21

General introduction 21

RS232-C Interface connection 21

DTR (Data Terminal Ready) pin 20 21

CTS (Clear To Send) pin 5 . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 21

Data format 21

Baud rate setting 21

Fig. 9: Baud rate dip switches 21

Commands to the player 21

Player registers 21

Picture number stop register 21

Picture number information register 21

Time code information register 21

# TABLE 1 - F-CODE COMMAND LIST 22

# TABLE 2 - RESPONSES TO COMPUTER ON COMMANDS FROM REMOTE CONTROL HANDSET 23

# TABLE 3 - ACKNOWLEDGEMENTS BACK TO EXTERNAL COMPUTER 24

20

# F-CODE PROGRAMMING

# GENERAL INTRODUCTION

The VP415 player is designed to allow control of all functions from an external computer. Connection to a computer is via the RS232-C serial interface or the SCSI interface on the rear of the VP415.

The interface allows two-way communication between player and computer. Some commands sent to the player are followed by corresponding acknowledgements back to the computer.

# RS232-C INTERFACE CONNECTION

This is a serial computer interface, in accordance with international communication standards. Communication is full duplex, with a selectable baud rate.

The player is fitted with a 25-pole female D-connector with the following pin connections:

PIN SIGNAL

2 (TxD) transmitted data from player to computer
3 (RxD) received data from computer to player
5 (CTS) clear to send:- a signal from computer to player indicating the computer is ready to receive data
7 (GND) logic ground
9 \(+12\mathrm{V} / 100\mathrm{mA}\)
10 -12V/10mA
20 (DTR) data terminal ready: a signal from player to computer indicating the player is ready to receive data

# DTR (DATA TERMINAL READY) PIN 20

Whenever the player is in a condition to receive data from the computer it signals this to the computer, by setting the DTR line to a high level (> +3V).

Conversely, when the player is busy processing data it is unable to receive data and indicates this to the computer by setting the DTR line to a negative level (< -3 V).

It is important to ensure that the data output of the computer is accurately controlled by the DTR line so as to prevent partial loss of data.

# CTS (CLEAR TO SEND) PIN 5

On the serial interface of many computers there is a control line which may be used to tell the player when the computer is ready to receive data. Whenever the player wishes to transmit data back to the computer it first checks the status of the CTS line. If the CTS line is greater than +3 Volts the player assumes that the computer is ready to receive data, which is therefore transmitted.

If the CTS line is less than -3 Volts, the player delays transmission indefinitely until the correct CTS status is seen.

If the computer cannot control the CTS line, it is recommended that the 'Transmission delay on')1 command is sent to the player. This results in a transmission rate of 50 characters per second, giving the computer more time to execute the characters. In this case the CTS line (pin 5) should be kept active (e.g. by leaving the connection open).

# DATA FORMAT

Data format is 8 data bits and 1 stop bit (parity ignored).

Data sent to the player should comprise a string of characters plus carriage return (CR).

Each byte sent to the player is checked for validity. ASCII codes lower than 32, and all other bytes of the string, are rejected. ASCII codes higher than 127 are accepted. In this case, the MSB (most-significant bit) is always read as having a value of zero.

For ASCII values greater than 127 the player effectively subtracts 128 from the ASCII value. A computer which transmits only seven data bits per ASCII code may therefore be used. In this case at least two stop bits must be sent.

The player actions the commands after receiving (CR).

# BAUD RATE SETTING (RS232-C only) (Fig. 9)

Data transmission speed may be set to 1200/2400/4800/9600 baud according to the positions of the two baud rate dip switches (numbers 1 and 2) at the rear of the player.

![img-10.jpeg](img-10.jpeg)

![img-11.jpeg](img-11.jpeg)

Fig. 9: Baud rate dip switches.

When altering the positions of these dip switches, it is useful to first switch on the player and disc status display using the DISPLAY button on the remote control handset. The baud rate setting is then displayed on the screen.

# COMMANDS TO THE PLAYER

The F-code commands that are sent to the player to carry out particular functions are listed in Tables 1 and 2. Functional explanations of these commands are given in Section 6 'F-CODE COMMANDS'.

Table 3 lists acknowledgements sent from the player to the computer on receipt of certain commands.

# PLAYER REGISTERS

There are two picture number registers in the player; each can hold a five-digit number from 1 to 79999. Normally a disc can contain up to around 54 000 pictures (or frames) so numbers beyond this are not used. There is also a time code register which can store a time code of the form mm:ss in the range 00:00 to 59:59.

# Picture number stop register

This register is automatically cleared to zero when the player reaches the picture number stored and enters the still mode.

# Picture number information register

When the player passes the number stored, an acknowledgement is sent back to the computer and the register is automatically cleared. The playing mode does not change.

# Time code information register

When the player passes the time code stored, an acknowledgement is sent back to the computer and the register is automatically cleared. The playing mode does not change.

21

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

25

SECTION 6

Page

# F-CODE COMMANDS 28

Sound insert (beep) 28

RC-5 output via Euroconnector 28

Replay switch disable 28

Replay switch enable 28

Eject 28

Transmission delay off 28

Transmission delay on 28

Halt 28

Halt & jump forward 28

Halt & jump reverse 28

Instant jump forward 28

Instant jump reverse 29

Standby 29

On 29

Pause 29

Reset to default 29

Picture number request 29

Chapter number request 29

Disc program status request 29

Player status request 30

User code request 30

Revision level request 30

Audio 1 off 31

Audio 1 on 31

Audio 2 off 31

Audio 2 on 31

Chapter number display off 31

Chapter number display on 31

Picture number/time code display off 31

Picture number/time code display on 31

Video off 31

Video on 31

Load picture number info. register 31

Load picture number stop register 31

Goto picture number and halt 31

Goto picture number and play 32

Goto picture number and continue 32

RC to computer off 32

RC to computer on 32

Local control off 32

Local control on 32

Remote control off 32

Remote control on 32

Still forward 32

Still reverse 32

Play forward 32

Play forward and jump forward 32

Play forward and jump reverse 33

Play reverse 33

Play reverse and jump forward 33

Play reverse and jump reverse 33

Goto chapter and halt 33

Goto chapter and play 33

Play chapter (sequence) 33

Set fast speed 33

Set slow speed 34

Goto time code 34

Load time code info. register 34

Slow motion forward 34

Slow motion reverse 34

Fast forward 34

Fast reverse 34

Clear 34

Video overlay 34

Audio 1 from internal 35

Audio 1 from external 35

26

Video from internal 35
Video from external 35
Audio 2 from internal 35
Audio 2 from external 35
TXT from disc off 35
TXT from disc on 35

27

# F-CODE COMMANDS

SOUND INSERT (beep)

Syntax: !xy

First code: !(33D = 21H)

Response: None

Function: To insert a beep tone in both audio channels

The values x and y range from 0 to 9 (in ASCII). x represents the pitch (although this is fixed in the VP415) and y represents the duration of the beep (approx. 0.3-3 s).

The beep is not influenced by on/off switching of Audio channels 1 or 2, or the audio controls.

RC-5 OUTPUT VIA EUROCONNECTOR

Syntax: #xy

First code: # (35D = 23H)

Response: None

Function: The specified RC-5 command is transmitted via pin 8 of the Euroconnector, to control certain types of monitor.

The value x (40H - 5FH) defines the RC-5 system number (40H = system 0, 41H = system 1, etc.) and the value y (40H - 7FH) defines the RC-5 command number (40H = command 0, 41H = command 1, etc.)

REPLAY SWITCH DISABLE

Syntax: $0

First code: $(36D = 24H)

Response: None

Function: To disable the REPLAY switch.

REPLAY SWITCH ENABLE

Syntax: $1

First code: $(36D = 24H)

Response: None

Function: To enable the REPLAY switch.

This is the power-on default state. The replay function is only active if the REPLAY switch is ON AND it is ENABLED.

EJECT

Syntax:

Code: '(39D = 27H)

Response: O when tray is opened

Function: To stop the current action and open the disc-tray.
The response is then given and the player goes to standby.

All defaults are reloaded (except for communication protocol) and the stop and info registers are cleared.

TRANSMISSION DELAY OFF

Syntax: )0

First code: )(41D = 29H)

Response: None

Function: To switch the transmission delay off (default) when sending response characters from player.

This delay only affects the RS232-C bus.

TRANSMISSION DELAY ON

Syntax: )1

First code: )(41D = 29H)

Response: None

Function: To switch the transmission delay on when sending response characters from player.

This delay only affects the RS232-C bus. When the delay is on, response characters are sent at 20 ms intervals, resulting in a transmission rate of 50 characters per second. Such a delay may prevent loss of data if a host cannot control the handshake signal CTS (from the player) which must then be kept active continuously.

HALT (CAV only)

Syntax: •

Code: • (42D = 2AH)

Response: None

Function: Player enters still mode.

This command is not applicable to CLV discs.

HALT & JUMP FORWARD (CAV only)

Syntax: •xxxxx+yy

Codes: • (42D = 2AH)

+ (43D = 2BH)

Response: None

Function: Still picture mode for duration xxxxx times 40 ms, followed by a jump forward over yy pictures.

The function is repeated until: another mode command is received, a clear command is received, or lead-out is entered.

The following limits apply:

xxxxx > 0

yy = 1 ... 50 AND yy <= 20 X xxxxx

This command is not applicable to CLV discs.

HALT & JUMP REVERSE (CAV only)

Syntax: •xxxxx-yy

Codes: • (42D = 2AH)

-(45D = 2DH)

Response: None

Function: Still picture mode for duration xxxxx times 40 ms, followed by a jump back over yy pictures.

The function is repeated until: another mode command is received, a clear command is received, or lead-in is entered.

The following limits apply:

xxxxx > 0

yy = 1 ... 50 AND yy <= 20 X xxxxx

This command is not applicable to CLV discs.

INSTANT JUMP FORWARD

Syntax: +yy

First code: + (43D = 2BH)

Response: None

Function: Jump forward over yy pictures.

The jump is performed at the end of the first video field. Small jumps are invisible, as they can be performed within the video blanking.

After this command, the player continues its previous operation.

The following limits apply:

yy = 1...50

28

# INSTANT JUMP REVERSE

Syntax: -yy

First code: -(45D = 2DH)

Response: None

Function: Jump back over yy pictures.

The jump is performed at the end of the first video field. Small jumps are invisible, as they can be performed within the video blanking.

After this command, the player continues its previous operation.

The following limits apply:

yy = 1...50

# STANDBY

Syntax: ,0

First code: ,(44D = 2CH)

Response: None

Function: Enter standby condition.

The spinning motor is decelerated and the optical readout unit goes to 'lead-in' (home position). The player is then switched to standby. All defaults are reloaded except for communication protocol, and the STOP and INFO registers are cleared.

# ON

Syntax: ,1

First code: ,(44D = 2CH)

Response: Positive ack: S

Negative ack: O (if disc-tray is open)

Function: CAV - Display first picture

CLV - Start play

CAV discs: The player is started and goes to the first picture after lead-in (still mode). The positive acknowledge signal is then given.

CLV discs: The player is started and goes to the first time code after lead-in. The positive acknowledge signal is then given and normal play forward commences.

If the player is already on, this command performs a Goto the first picture, the positive acknowledge signal is given and then still (CAV) or play (CLV) occurs.

# PAUSE

Syntax: /

Code: /(47D = 2FH)

Response: None

Function: CAV - Enter still mode with audio and video muted

CLV - Pause, audio and video muted

(optical readout unit stays in current position)

# RESET TO DEFAULT

Syntax: :

Code: : (58D = 3AH)

Response: None

Function: Reset to initial conditions.

The player is reset to initial power-on conditions, except that the communication protocol remains unchanged. The STOP and INFO registers are not affected.

# PICTURE NUMBER REQUEST (CAV only)

Syntax: ?F

Codes: ? (63D = 3FH)

F (70D = 46H)

Response: Positive ack: F xxxxx

Negative ack:

X if picture no. is not available

O if disc-tray is open

Function: To return the current picture number as five ASCII digits (00001...59999).

If this command is attempted when a CLV disc is loaded, a negative acknowledge signal (X) is returned.

# CHAPTER NUMBER REQUEST

Syntax: ?C

Codes: ? (63D = 3FH)

C (67D = 43H)

Response: Positive ack: C xx

Negative ack:

X if chapter no. is not available

O if disc-tray is open

Function: To return the current chapter number as two

ASCII digits (00...79).

# DISC PROGRAM STATUS REQUEST

Syntax: ?D

Codes: ? (63D = 3FH)

D (68D = 44H)

Response: Positive ack: D x1 x2 x3 x4 x5

Negative ack:

X if disc status not available

O if disc-tray is open

Function: To return the disc program status

(as recorded on the disc).

Each status byte (x1 to x5) is in the form 0011yyyy.

These bytes are specified below:

# Response specification

# First status byte (x1)

bit 7: 0

bit 6: 0

bit 5: 1

bit 4: 1

bits 3-0: 1101 = D (Hex)

or

bits 3-0: 1011 = B (Hex)

# Second status byte (x2)

bit 7: 0

bit 6: 0

bit 5: 1

bit 4: 1

bits 3-0: 1100 = C (Hex)

or

bits 3-0: 1010 = A (Hex)

From x1 and x2:

DC = CX noise reduction present

BA = No CX noise reduction

# Third status byte (x3)

bit 7: 0

bit 6: 0

bit 5: 1

bit 4: 1

bit 3: 0 = 12" disc 1 = 8" disc

bit 2: 0 = side 1 1 = side 2

bit 1: 0 = no TXT present 1 = TXT present

bit 0: 0 = FM-FM mpx. off 1 = FM-FM mpx. on

# Fourth status byte (x4)

bit 7: 0

bit 6: 0

bit 5: 1

bit 4: 1

29

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

The response bytes x1 to x5 are made up of ASCII digits.

x1 = 0

x2 = major revision level of drive software

x3 = minor revision level of drive software

x4 = major revision level of control software

x5 = minor revision level of control software

# AUDIO 1 OFF

Syntax: A0

First code: A (65D = 41H)

Response: None

Function: Disable internal audio channel 1 (from disc)

If audio channel 2 is on, both audio outputs are supplied by audio channel 2.

# AUDIO 1 ON

Syntax: A1

First code: A (65D = 41H)

Response: None

Function: Enable internal audio channel 1 (from disc)

This is the power-on default state. Audio is on only during normal play forward.

# AUDIO 2 OFF

Syntax: B0

First code: B (66D = 42H)

Response: None

Function: Disable internal audio channel 2 (from disc)

If audio channel 1 is on, both audio outputs are supplied by audio channel 1.

# AUDIO 2 ON

Syntax: B1

First code: B (66D = 42H)

Response: None

Function: Enable internal audio channel 2 (from disc)

This is the power-on default state. Audio is on only during normal play forward.

# CHAPTER NUMBER DISPLAY OFF

Syntax: C0

First code: C (67D = 43H)

Response: None

Function: Cancel chapter number display.

This is the power-on default state.

# CHAPTER NUMBER DISPLAY ON

Syntax: C1

First code: C (67D = 43H)

Response: None

Function: Display chapter number on screen.

This is disabled during lead-in/lead-out and during Goto. The picture number/time code display (if on) is switched off.

# PICTURE NUMBER/TIME CODE DISPLAY OFF

Syntax: D0

First code: D (68D = 44H)

Response: None

Function: CAV - Cancel picture number display

CLV - Cancel time code display

This is the power-on default state.

# PICTURE NUMBER/TIME CODE DISPLAY ON

Syntax: D1

First code: D (68D = 44H)

Response: None

Function: CAV - Display picture number on screen

CLV - Display time code on screen

This is disabled during lead-in/lead-out and during Goto. The chapter number display (if on) is switched off.

# VIDEO OFF

Syntax: E0

First code: E (69D = 45H)

Response: None

Function: Switch off internal video (from disc)

# VIDEO ON

Syntax: E1

First code: E (69D = 45H)

Response: None

Function: Switch on internal video (from disc)

This is the power-on default state. The video is also switched off by the player when not in the active area of the disc, or when pause, ready or Goto are active.

# LOAD PICTURE NUMBER INFO REGISTER (CAV only)

Syntax: FxxxxxI

Codes: F (70D = 46H)

I (73D = 49H)

Response: Positive ack: A3

Negative ack: AN if CLV disc

O if disc-tray is open

Function: The positive acknowledge signal is given when the specified picture number is passed by any play or step action.

The INFO register is cleared after the response.

If a CLV disc is loaded, the negative acknowledge (AN) will be given.

# LOAD PICTURE NUMBER STOP REGISTER (CAV only)

Syntax: FxxxxxS

Codes: F (70D = 46H)

S (83D = 53H)

Response: Positive ack: A2

Negative ack: AN if CLV disc

O if disc-tray is open

Function: The player halts at the specified picture number when reached by any play or step action. The positive acknowledge signal is then given.

The STOP register is cleared after the response.

If a CLV disc is loaded, the negative acknowledge (AN) will be given.

# GOTO PICTURE NUMBER AND HALT (CAV only)

Syntax: FxxxxxR

Codes: F (70D = 46H)

R (82D = 52H)

Response: Positive ack: A0

Negative ack: AN if Goto fails

O if disc-tray is open

Function: Search for picture number and display in still mode.

The specified picture is searched for. When found, the picture is displayed in still mode and the positive acknowledge signal is given. If the picture number is not found, the negative response (AN) is given.

31

During the Goto action, the audio and video are muted. However, the video is not muted if the Goto can be performed within the instant jump region of 50 tracks.

If a CLV disc is loaded, the negative acknowledge signal (AN) is returned.

# GOTO PICTURE NUMBER AND PLAY (CAV only)

Syntax: FxxxxxN

Codes: F(70D = 46H)

N(78D = 4EH)

Response: Positive ack: A1

Negative ack: AN if Goto fails

O if disc-tray is open

Function: Search for picture number and commence play from that picture number.

The specified picture is searched for. When found, normal play forward commences from that picture and the positive acknowledge signal is given. If the picture number is not found, the negative response (AN) is given. During the Goto action, the audio and video are muted. However, the video is not muted if the Goto can be performed within the instant jump region of 50 tracks.

If a CLV disc is loaded, the negative acknowledge signal (AN) is returned.

# GOTO PICTURE NUMBER AND CONTINUE (CAV only)

Syntax: FxxxxxQ

Codes: F(70D = 46H)

Q(81D = 51H)

Response: Positive ack: A0

Negative ack: AN if Goto fails

O if disc-tray is open

Function: Search for picture number and continue with previous play mode from that picture number.

The specified picture is searched for. When found, the previous play mode continues from that picture and the positive acknowledge signal is given. If the picture number is not found, the negative response (AN) is given. During the Goto action, the audio and video are muted. However, the video is not muted if the Goto can be performed within the instant jump region of 50 tracks.

If a CLV disc is loaded, the negative acknowledge signal (AN) is returned.

# RC TO COMPUTER OFF

Syntax: H0

First code: H(72D = 48H)

Response: None

Function: Remote control commands NOT routed to host computer.

This is the power-on default state.

# RC TO COMPUTER ON

Syntax: H1

First code: H(72D = 48H)

Response: None

Function: Remote control commands routed to host computer.

Only one response is given for each RC command.

# LOCAL CONTROL OFF

Syntax: I0

First code: I(73D = 49H)

Response: None

Function: Disable player front-panel controls.

# LOCAL CONTROL ON

Syntax: I1

First code: I(73D = 49H)

Response: None

Function: Enable player front-panel controls.

This is the power-on default state.

# REMOTE CONTROL OFF

Syntax: J0

First code: J(74D = 4AH)

Response: None

Function: RC commands NOT executed by player.

# REMOTE CONTROL ON

Syntax: J1

First code: J(74D = 4AH)

Response: None

Function: RC commands executed by player.

This is the power-on default state.

# STILL FORWARD (CAV only)

Syntax: L

Code: L(76D = 4CH)

Response: None

Function: Halt and display next picture.

The time between two subsequent still commands (forward or reverse) must be at least 40 ms to be sure of execution. This command is not applicable to CLV discs.

# STILL REVERSE (CAV only)

Syntax: M

Code: M(77D = 4DH)

Response: None

Function: Halt and display previous picture.

The time between two subsequent still commands (forward or reverse) must be at least 40 ms to be sure of execution. This command is not applicable to CLV discs.

# PLAY FORWARD

Syntax: N

Code: N(78D = 4EH)

Response: None

Function: Normal play forward.

# PLAY FORWARD AND JUMP FORWARD (CAV only)

Syntax: Nxxxxx+yy

Codes: N(78D = 4EH)

+(43D = 2BH)

Response: None

Function: After normal play forward of xxxxx pictures, a jump forward of yy pictures is performed.

This is repeated until a Clear command or another mode command is received, or lead-out is reached.

The following limits apply:

xxxxx > 0

yy = 1...50

yy <= 20 X xxxxx

This command is not applicable to CLV discs.

32

# PLAY FORWARD AND JUMP REVERSE (CAV only)

Syntax: Nxxxxx-yy

Codes: N (78D = 4EH)

-(45D = 2DH)

Response: None

Function: After normal play forward of xxxxx pictures, a jump back of yy pictures is performed.

This is repeated until a Clear command or another mode command is received, or lead-in or lead-out is reached.

The following limits apply:

xxxxx > 0

yy = 1...50

yy <= 20 X xxxxx

This command is not applicable to CLV discs.

# PLAY REVERSE (CAV only)

Syntax: O

Code: O (79D = 4FH)

Response: None

Function: Normal play reverse.

This command is not applicable to CLV discs.

# PLAY REVERSE AND JUMP FORWARD (CAV only)

Syntax: Oxxxxx+yy

Codes: O (79D = 4FH)

+ (43D = 2BH)

Response: None

Function: After normal play reverse of xxxxx pictures, a jump forward of yy pictures is performed.

This is repeated until a Clear command or another mode command is received, or lead-in/lead-out is reached.

The following limits apply:

xxxxx > 0

yy = 1...50

yy <= 20 X xxxxx

This command is not applicable to CLV discs.

# PLAY REVERSE AND JUMP REVERSE (CAV only)

Syntax: Oxxxxx-yy

Codes: O (79D = 4FH)

-(45D = 2DH)

Response: None

Function: After normal play reverse of xxxxx pictures, a jump back of yy pictures is performed.

This is repeated until a Clear command or another mode command is received, or lead-in is reached.

The following limits apply:

xxxxx > 0

yy = 1...50

yy <= 20 X xxxxx

This command is not applicable to CLV discs.

# GOTO CHAPTER AND HALT

Syntax: QxxR

Codes: Q (81D = 51H)

R (82D = 52H)

Response: Positive ack: A6

Negative ack: AN if Goto fails

O if disc-tray is open

Function: Search for start of specified chapter and display first picture.

When found, the first picture of the chapter is displayed and the positive acknowledge signal is given.

Note: With CLV discs, play starts at that chapter.

# GOTO CHAPTER AND PLAY

Syntax: QxxN

Codes: Q (81D = 51H)

N (78D = 4EH)

Response: Positive ack: A6

Negative ack: AN if Goto fails

O if disc-tray is open

Function: Search for start of specified chapter and commence play.

Following a successful search, normal play forward starts from the first picture of the chapter and the positive acknowledge signal is given. If the search fails, the negative response (AN) is given. Video and audio are muted during the Goto.

# PLAY CHAPTER (SEQUENCE)

Syntax: QxxyyzzS

Codes: Q (81D = 51H)

S (83D = 53H)

Response: Positive ack: A7

Negative ack: AN if Goto fails

O if disc-tray is open

Function: Play the specified chapter or sequence of chapters.

The start of the first specified chapter is searched for. When found, this chapter is played (normal play forward). When the end of the chapter is reached, the next specified chapter is searched for, and played, etc., until the last specified chapter has been played. The positive ack. signal is then given and the player either halts (CAV) or enters pause mode (CLV).

A maximum of 7 chapters is allowed in a sequence. If more than one chapter is specified, two digits per chapter must be specified.

e.g. Q3S plays chapter 3

Q0312S plays chapter 3 then 12

If a chapter search fails, a negative ack. signal is given and the chapter sequence is terminated.

During a Goto, the video and audio are muted.

# SET FAST SPEED (CAV only)

Syntax: SxxxF

Codes: S (83D = 53H)

F (70D = 46H)

Response: None

Function: Fast speed is set to the specified value.

Limits: xxx = 2...40

where 2 is normal speed

3 is 3/2 times normal speed

40 is 40/2 (i.e. 20) times normal speed.

The default value is 6, i.e. 3 times normal speed.

Fast play action is initiated with command W for forward, or command Z for reverse.

This command is not applicable to CLV discs.

33

# SET SLOW SPEED (CAV only)

Syntax: SxxxS

Codes: S (83D = 53H)

Response: None

Function: Slow speed is set to the specified value.

Limits: xxx = 2...250

where 2 is normal speed

3 is 2/3 times normal speed

250 is 2/250 times normal speed (i.e. 5 sec per picture)

The default value is 6, i.e. 1/3 normal speed.

Slow play action is initiated with command U for forward, or command V for reverse.

For compatibility reasons, the command Sxxx is equivalent to SxxxS.

This command is not applicable to CLV discs.

# GOTO TIME CODE (CLV only)

Syntax: TxxyyN

Codes: T (84D = 54H)

N (78D = 4EH)

Response: Positive ack: A8

Negative ack: AN if Goto fails

O if disc-tray is open

Function: The specified time code is searched for and when found, normal play forward is performed.

When the specified time code is found, the positive acknowledge signal is given. If the time code is not found then the negative response is given. xx defines the minutes, and yy the seconds. Minutes are mandatory, and the seconds are optional. If the seconds are specified, the minutes must be given as a two digit number e.g. 07.

If the seconds are not specified, or a disc without line 16 manchester code is played, a search to the start of the specified minute is performed.

If performed with CAV discs, the negative response (AN) is given.

# LOAD TIME CODE INFO REGISTER (CLV only)

Syntax: xxyyl

Codes: T (84D = 54H)

I (73D = 49H)

Response: Positive ack: A9

Negative ack: AN if CAV disc

O if disc-tray is open

Function: The positive acknowledge signal is given when the specified time code is passed during normal play forward.

xx defines the minutes, yy the seconds. The minutes are mandatory, the seconds are optional. If the seconds are specified, the minutes must be given as a two digit number e.g. 07.

If the seconds are not specified or a disc without line 16 manchester code is played, the acknowledge signal appears on the first second of the specified minute.

If performed with CAV discs, the negative ack. signal (AN) will be returned immediately.

# SLOW MOTION FORWARD (CAV only)

Syntax: U

Code: U (85D = 55H)

Response: None

Function: Play forward at slow speed is started, conforming to the SxxxS setting.

This command is not applicable to CLV discs.

# SLOW MOTION REVERSE (CAV only)

Syntax: V

Code: V (86D = 56H)

Response: None

Function: Play reverse at slow speed is started conforming to the SxxxS setting.

This command is not applicable to CLV discs.

# FAST FORWARD (CAV only)

Syntax: W

Code: W (87D = 57H)

Response: None

Function: Play forward at fast speed is started conforming to the SxxxS setting.

This command is not applicable to CLV discs.

# FAST REVERSE (CAV only)

Syntax: Z

Code: Z (90H = 5AH)

Response: None

Function: Play reverse at fast speed is started conforming to the SxxxS setting.

This command is not applicable to CLV discs.

# CLEAR

Syntax: X

Code: X (88D = 58H)

Response: None

Function: CAV: Any play action is stopped and the player is put into still mode. A chapter play (sequence) is cancelled. The picture number INFO and STOP registers will be cleared. CLV: Any chapter play (sequence) is cancelled. The timecode INFO and STOP registers will be cleared.

The cancelled chapter play (sequence) does not send a response to the host computer.

# VIDEO OVERLAY

Syntax: VPy

Codes: V (86D = 56H)

P (80D = 50H)

Response: None on commands VP1 - VP5

VP1 - VP5 on command VPX

Function: To control the mode of the video processor.

y = 1...5 or X

VP1 = LaserVision video only.

This is the power-on default state.

VP2 = External (computer) RGB only.

VP3 = Hard-keyed.

External RGB overlayed on LaserVision video.

At screen positions where external RGB is

suppressed (black), LV video only is displayed.

Where the external RGB is not suppressed, only

the external RGB is displayed.

VP4 = Mixed.

Transparent overlay of external RGB and LV video.

Both images are simultaneously displayed, each at reduced intensity.

VP5 = Enhanced.

LV video is highlighted by external RGB.

At screen positions where external RGB is

black, the LV video is displayed at

reduced intensity. Where the external RGB is

not black, the LV video is displayed at normal intensity.

34

VPX = This command interrogates the system for its current video mode. The reply code is identical to the appropriate video command i.e. VP1 to VP5.

# AUDIO 1 FROM INTERNAL

Syntax: 0

First code: (91D = 5BH)

Response: None

Function: The internal audio 1 signal is selected.

This is the power-on default state.

# AUDIO 1 FROM EXTERNAL

Syntax: 1

First code: (91D = 5BH)

Response: None

Function: The internal audio 1 signal is inhibited in favour of the audio source on the audio 1 input connector.

The audio 1 on/off switch and the audio 1 mute do not have a function in this mode.

# VIDEO FROM INTERNAL

Syntax: 0

First code: (92D = 5CH)

Response: None

Function: The internal video signal is selected.

This is the power-on default state.

# VIDEO FROM EXTERNAL

Syntax: 1

First code: (92D = 5CH)

Response: None

Function: The internal video signal is inhibited in favour of the external video source on the CVBS video input connector.

The video on/off switch and the video mute do not have a function in this mode.

# AUDIO 2 FROM INTERNAL

Syntax: 0

First code: (93D = 5DH)

Response: None

Function: The internal audio 2 signal is selected.

This is the power-on default state.

# AUDIO 2 FROM EXTERNAL

Syntax: 1

First code: (93D = 5DH)

Response: None

Function: The internal audio 2 signal is inhibited in favour of the audio source on the audio 2 input connector.

The audio 2 on/off switch and the audio 2 mute do not have a function in this mode.

# TXT FROM DISC OFF

Syntax: _0

First code: _ (95D = 5FH)

Response: None

Function: The video lines that may contain teletext information are muted (internal video signal from LV disc).

# TXT FROM DISC ON

Syntax: _1

First code: _ (95D = 5FH)

Response: None

Function: The teletext information in the raster blanking lines of the internal video signal (LV disc) is enabled.

This is the power-on default state.

35

SECTION 7

Page

# SCSI OPERATION

Introduction 37

Volumes 37

The SCSI interface 37

General 37

VP415 issues 38

Default conditions 38

Default start-up conditions 38

Default stop-unit conditions 38

LV-DOS commands 38

The status byte 38

Group 0 (6-byte) commands 38

Test unit ready 39

Rezero unit 39

Read 39

Write 39

Start/Stop unit 39

Request sense 39

Group 6 (Vendor-unique) commands 40

Write F-code command 40

Read F-code reply 40

Search modes 40

Slow read 40

Fast read 41

Special issues 41

SCSI address setting 41

Fig. 10: SCSI address dip switches . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 41

Condition after Start-unit 41

Initiator powered off 41

Loss of sync 41

Retries 41

Two computers trying to take control 41

Changing disc while under initiator control 41

36

# SCSI OPERATION

## INTRODUCTION

The VP415 contains a microprocessor to access the data on a LaserVision disc and make it available to an industry standard SCSI (Small Computer System) Interface. This interface is used to connect the LaserVision player (the target) to a host computer (the initiator), allowing the host to read data from the disc, as well as providing the usual player control functions. The software running in the microprocessor in the player is called LV-DOS, and it is with LV-DOS that the host computer communicates via the SCSI interface.

A LaserVision disc currently has a storage capacity of 324 Mbytes. It is subdivided into a number of volumes which are managed by LV-DOS. The following diagram shows how a disc might be structured:

|  System table for LV-DOS  |
| --- |
|  Volume directory  |
|  Volume 'JIM'  |
|  Volume 'HENRY'  |
|  300 Mbytes  |

The system table contains information for internal use by LV-DOS and the volume directory contains an entry for each volume on the disc. An entry for a volume contains the volume name, its whereabouts on the disc, and some other control information.

The volumes themselves contain applications developers want to put in them. LV-DOS does not manipulate this data and therefore does not care what format it is in.

Blocks on the disc are not interleaved; consecutive logical blocks are in consecutive physical order, with an interleave value of 1.

Detection and correction of errors are carried out fully by the resident LV-DOS firmware such that data transferred to the initiator is error free.

Currently the pre-mastering system must supply all of the data to be mastered onto the disc (including the system table and volume directory).

## VOLUMES

The LaserVision disc has a high storage capacity, with the ability to store 54 000 pictures and 324 Mbytes of data on each side. To divide the total capacity and to enable the storage of more than one independent application of interactive LaserVision on one side of the disc, the concept of volumes has been adopted. This concept is totally transparent to the host computer since communication between the host computer and the LaserVision player refers to logical pictures and logical blocks. The translation from logical to physical pictures and data blocks is carried out by LV-DOS.

After having received the Start-unit command from the host computer (the initiator), LV-DOS reads information from the disc about the physical location of data and pictures of a specific volume. Once Start-unit is completed, the volumes are automatically opened, provided the relevant digital data can be read from the disc.

Volumes on disc are accessible as logic units. The SCSI command format allows only 8 logic units to be specified in a command. Currently, LV-DOS supports up to 7 volumes (excluding the directory volume) on a disc.

Logic unit numbers 0 - 6 will be assigned to the volumes in the order they are specified in the volume directory. If there are less than seven volumes on a disc, the unused logic units are closed by definition. Logic unit 7 is intended for absolute F-code read/write (I/O) and for access to the volume directory.

## THE SCSI INTERFACE

### General

The SCSI interface is usually used to connect a microcomputer to one or more floppy and/or Winchester disc drives. It is a bussed system of a very general nature and makes few assumptions about the pieces of equipment being connected. It is therefore well-suited to the requirements of LV-DOS, and allows the transport of both player control commands and disc data over the same physical link.

The SCSI standard provides a number of ways of communicating between the host computer and its peripherals. However, only the information necessary to use the SCSI interface in conjunction with the VP415 is covered here. For full details of the SCSI standard, refer to the ANSI standard X3T9.2.

Consider a system consisting of a single initiator (the host computer) and a number of targets (of which the LaserVision player is one):

![img-12.jpeg](img-12.jpeg)

When the host computer wants the player to do something, it must first gain control of the SCSI bus. This is the arbitration phase, and is only necessary to allow for the possible extension of the system to multiple initiators in the future. If the arbitration phase fails, some other device has control of the bus, and the host computer must wait until it is free and retry.

The host computer must then gain the attention of the target with which it wishes to communicate (i.e. the player). This it does in the selection phase, in which it outputs the SCSI address of the player (each device on the bus has a unique address in the range 0 - 7) and waits for a response. Should the selection phase fail, a "No response from player" error must be returned to the higher level software. The SCSI address of the player is set by means of the SCSI ADDRESS dip switches at the rear of the player. See SCSI address setting, under 'Special issues' later in this section.

Assuming that the arbitration phase is successful, the host computer must then tell the player what it wants to do. This is in the form of a command phase, in which the host computer sends a command descriptor block containing the command that it wishes the player to carry out and any additional information required (e.g. the block number to be read).

The command phase is followed, where appropriate, by a data in or data out phase in which the requested information is transferred from the player to the host computer (e.g. when reading a disc block) or vice versa. On a read, there may be a delay of several seconds before this data is available, depending on how long it takes to execute the command in question. Note that both parties must usually know in advance how much data is to be transferred.

37

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

# FAST READ

Syntax: R1

First code: R (82D = 52H)

Response: None

Function: Fast Read mode, without picture restore after search.
Video switched off after search.

This is the power-on default state.

# SPECIAL ISSUES

# SCSI address setting (Fig. 10)

Each device connected to the SCSI bus must have its own unique address. This is in the range 0 - 7. If the address is not that expected by the host computer, the VP415 will not be recognised. The factory setting is address 0.

![img-13.jpeg](img-13.jpeg)

Fig. 10: SCSI address dip switches.

The SCSI bus address of the VP415 may be altered by changing the positions of the SCSI ADDRESS dip switches situated at the rear of the player. A switch in the up position is OFF. Switches 1 - 4 and switch 8 should be OFF. Switches 5 - 7 determine the SCSI address as follows:

|  address | switch 5 | switch 6 | switch 7  |
| --- | --- | --- | --- |
|  0 | OFF | OFF | OFF  |
|  1 | OFF | OFF | ON  |
|  2 | OFF | ON | OFF  |
|  3 | OFF | ON | ON  |
|  4 | ON | OFF | OFF  |
|  5 | ON | OFF | ON  |
|  6 | ON | ON | OFF  |
|  7 | ON | ON | ON  |

# Condition after Start-unit

Successful execution of the Start-unit command always brings the system to the same condition regardless of the conditions present immediately before.

# Initiator powered off

If an initiator, connected to the SCSI bus is not powered up, it is possible that the reset line will be pulled active low and the LV-DOS control will be in its reset condition. As such the LV-DOS controller will not take control of the player which will subsequently behave as if there is no controller at all.

# Loss of sync

Any action that affects the sync signal from the initiator to which the player is genlocked e.g. a change of video mode, will cause the player to genlock by changing the disc speed. During a speed change it is possible that the tolerances for reading digital data are exceeded, in which case the system may retry to read data, or even register a media error.

# Retries

If necessary, LV-DOS will make a number of retries. However it is very unlikely that an unsuccessful command will be successful on a retry from the host, and it is recommended that the initiator does not issue retries if a command fails.

# Two computers trying to take control

The RS232-C serial interface of the player also enables an external system to control the player. The system can only 'listen' to one channel

at a time, and if two systems are simultaneously trying to control the player, it is possible that the SCSI initiator may lose control.

Any subsequent command, with the exception of mode select - F-codes, will then be ignored. Initiator control of the player may be resumed by issuing a Start-unit command to the LV-DOS controller. The command may return a 'media error' or 'unit not ready' sense key, but in either case the SCSI initiator now has control of the player.

# Changing disc while under initiator control

To change the disc, issue the Stop-unit command followed by the Eject command. Poll the player status by sending the Player status command ?P and read the reply code until the reply code acknowledges that the disc-tray is closed again. Then issue the Start-unit command to log on the disc. You may verify that the disc is logged on with the Test unit ready command. This is not necessary however if the Start-unit returned no error. Verify the identity of the disc and be sure that all the player modes are set according to your application.

41

# SECTION 8

Page

# MAINTENANCE 43

Care of the player 43

Care of discs 43

Trouble symptoms and possible causes 43

# TECHNICAL DATA 44

LaserVision Disc 44

Professional LaserVision Player VP415 44

General 44

Video 44

Audio 44

Genlock 44

Video mixer 44

LV-ROM 44

A/V Euroconnector 44

RGB (TTL) IN socket 45

RS232-C interface 45

SCSI interface 45

42

# MAINTENANCE

# Care of the player

The player requires no special maintenance. It is, however, advisable to clean the objective lens from time to time with a piece of wadding dipped in alcohol.

# Care of discs

No special care is needed in handling discs. For best results however, you are recommended to keep the playing surface clean and free from dust, grease, etc. When cleaning is required, gently wipe the disc surface with a soft, dry cloth. Use no solvents!

Always remove discs after playing, replacing them in their protective jackets.

Discs should be stored vertically, in their original jackets. Keep them away from extreme heat or moisture and avoid exposure to direct sunlight.

# TROUBLE SYMPTOMS AND POSSIBLE CAUSES

Disc does not rotate, no indicators light up

- Automatic overload protection circuit is in operation. Switch off the player at the rear, wait for approx. 30 seconds then switch on again.

Disc does not rotate

- Check that the player is receiving power: the STANDBY indicator should be lit.
- Check that the disc-tray is properly closed.

Disc rotates but picture is weak or absent

- Check the connection between monitor and player.
- Check that the disc has been loaded correctly (label up) on the disc-tray. (Some discs have programme content on one side only.)
- Press the ▶ section of the SEARCH button.
- The player is in the pause mode: Press the ▶ section of the PLAY button.

Player sticks at particular point on disc

- Press the ▶ section of the SEARCH button momentarily to skip over the affected part.
- Remove the disc and wipe both surfaces clean with a soft, dry cloth to remove possible opaque surface marks.

Special effects (still, slow, reverse, fast) do not function

- Check that a CAV disc is being played; when playing CLV discs, the special-effects buttons do not function.

Unstable still picture

- If still pictures taken from a fast moving scene sometimes flicker, this is no fault of the player but results from the basic programme material used for disc production.

Good picture but no sound

- Make sure that the player is in its forward playing mode (in all other modes there is no sound).
- Check that the sound channels AUDIO 1 and/or AUDIO 2 are switched on (the indicators should be lit).
- If an LV-ROM disc is being played, there may be data and therefore no sound on the disc. Try a non-LV-ROM disc.

Digit buttons are inoperative

- Check whether the picture number or chapter number is displayed on the monitor. If not, press PNR or CNR.

Remote control does not function correctly

- Check that the RC IR/EURO switch on the rear of the player is set to IR.

- Make sure that the distance between player and remote control handset is not more than \(10\mathrm{m}\).
- Make sure that remote control handset is aimed at the front of the player and there is no obstacle between player and remote control handset.
- Check batteries in remote control handset.
- If the player is in the Replay mode, most controls are disabled.

The player fails to respond when under computer control

- Check the connections to the relevant interface.
- Ensure that DATA IN and DATA OUT are the right way around (RS232-C).
- Check that the DTR signal from the player is being received by the computer (RS232-C).
- To reset, press the ON/STANDBY button on the front of the player.

It is possible sometimes for the microprocessor in the player to 'lock-up' if it receives spurious or corrupted data. In this case, switch the player power OFF for a few seconds. This will reset the microcomputer to its correct state.

43

# TECHNICAL DATA

# LASERVISION DISC

Disc diameter 30 cm (12") or 20 cm (8")

Disc thickness 2.7 mm (0.1")

Disc speed CAV disc: 1500 r.p.m

CLV disc: 1500-570 r.p.m

Maximum capacity

(30cm - 12" disc) CAV disc: 54 000 pictures per side
LV-ROM disc (CAV): 324 Mbyte (max.)
user data per side (in place of audio)

Max. playing time

(30cm - 12" disc) CAV disc: 36 minutes per side
CLV disc: 1 hour per side

Average track pitch 1.6 - 1.8 um

# PROFESSIONAL LASERVISION PLAYER VP415

# General

Front loading motor-powered disc-tray

startup time < 13 s

unload time (time

between Eject command

and disc out of player) < 15 s

SSL (solid state laser)

Laser type AlGaAs semiconductor

Wavelength 780 nm

Aperture 0.5

Output of laser 3 - 5 mW

Random access time CAV: max. 3 s (≤ 1 s average)

CLV: max. 15 s (≤ 5 s average)

Instant jump up to 50 frames (forward or reverse)
within vertical interval time

On-board programming Up to 16 picture number / chapter
number segments

Program retention

with no mains supply > 1 week

Mains voltage 220 - 240 V (± 10%) a.c.

Mains frequency 50 to 60 Hz

Power consumption 60 W approx.

Electrical safety acc. to IEC 65

operational conditions 10 to 35 °C

Rel. humidity 20 - 80%

storage conditions -40 to 70 °C

Rel. humidity 10 - 95%

Dimensions 420 x 160 x 400 mm

disc-tray open 420 x 160 x 740 mm

Weight 15 kg (approx.)

TV system 625/50 PAL

# Video

CVBS input (BNC) 1 V into 75 ohm, loop-through

CVBS output (BNC) 1 V into 75 ohm

CVBS output

(Euroconnector pin 19) 1 V into 75 ohm

RGB output

(Euroconnector)

R (pin 15) 0.7 V into 75 ohm

G (pin 11) "

B (pin 7) "

Video bandwidth RGB: 5 MHz (-3 dB)

CVBS: 3 MHz (-3 dB), encoded

Signal-to-noise ratio 40 dB typ. unweighted

(disc dependent)

50 dB typ. weighted

(disc dependent)

Timebase instability less than 10 ns (normal play)

# Audio

Audio input (cinch) 3 Vpp (load 47 k)

Audio output (cinch) 650 mV r.m.s. into 1 k (max. deviation)

Audio output

(Euroconnector

pins 1 & 3) 650 mV r.m.s. into 1 k

Audio bandwidth 40-20 000 Hz

Signal-to-noise ratio ≥ 50 dB typ. weighted

(disc dependent)

Channel separation better than 55 dB

# Genlock

Sync input (BNC) 0.3 - 2.0 Vpp 75 ohm, loop-through

(waveform acc. to CCIR standards)

Sync input (DIN pin 4) line freq. 15 625 Hz ± 100 ppm

field freq. 50 Hz locked to line freq.,

interlaced, with or without equalising

pulses, negative-going,

logic 0: 0 - 1 V, logic 1: 2.2 - 4.2 V

Sync output (BNC) 2.0 Vpp 75 ohm, negative-going

Genlock lock-in time 5 s

# Video mixer

RGB mixing / keying modes:

Player RGB only

Computer output RGB only

Mixed mode: player 62%, computer 38%

Key mode: player 100%, computer 100%

Enhanced mode: Player 57% / 100%

# LV-ROM

User data capacity Max. 324 Mbyte per disc side

User data per frame 6 kbyte

User data transfer rate
from disc 150 kbyte/s (depending on computer)

Data integrity
(error rate) ≤ 10⁻¹⁶

Internal C.P.U. 4 X 6 kbyte cache memory for user data

System compatible with floppy disc and hard
disc systems

# A/V Euroconnector

# pin signal

1 audio out (right) 650 mV rms/1 k
2 not connected
3 audio out (left) 650 mV rms/1 k
4 audio earth
5 blue earth
6 not connected
7 blue out 700 mV/75 ohm
8 player status (player in standby: 2 V, player on: 12 V)
9 green earth
10 not connected
11 green out 700 mV/75 ohm
12 not connected
13 red earth
14 earth
15 red out 700 mV/75 ohm
16 fast blanking: 2.5 V into 75 ohm (RGB status)
17 CVBS earth
18 RGB status earth
19 CVBS out 1 V/75 ohm (also acts as sync out when using RGB)
20 not connected
21 socket earth

44

# RGB (TTL) IN socket (DIN)

6-pole female connector, 270 degrees

# pin

1 Red signal
2 Green signal
3 Blue signal
4 Composite sync
5 Ground
6 Not connected

(Logic 0: 0 - 1 V, logic 1: 2.2. - 4.2 V. Sync instability better than +/- 100 ppm, interlaced, with or without equalising pulses, negative-going.)

# RS232-C interface

Serial computer interface, in accordance with international communication standards.

Full duplex

8 data bits, 1 stop bit, no parity

Data transmission speed may be set to 1200/2400/4800/9600 baud according to the positions of the two baud rate dip switches (numbers 1 and 2) at the rear of the player.

|  baud rate | switch 1 | switch 2  |
| --- | --- | --- |
|  1200 | UP | UP  |
|  2400 | UP | DOWN  |
|  4800 | DOWN | UP  |
|  9600 | DOWN | DOWN  |

The player is fitted with a 25-pole female D-connector with the following pin connections:

# pin signal

\(\wedge 2\) (TxD) transmitted data from player to computer
\(\times 3\) (RxD) received data from computer to player
\(\times 5\) (CTS) clear to send: a signal from computer to player indicating the computer is ready to receive data \((\geq +3\mathrm{V}\) means O.K. to transmit)

7 (GND) logic ground

9 +12 V/100 mA

10 -12 V/10 mA

20 (DTR) data terminal ready: a signal from player to computer indicating that player is ready to receive data (≥ + 3 V means O.K. for data)

# SCSI interface

A computer interface in accordance with SCSI standards. The player is fitted with a 50-pole unshielded connector consisting of two rows of 25 male pins on 100 mil centres.

Single-ended cable pin assignments:

# pin signal

2 -DB(0)
4 -DB(1)
6 -DB(2)
8 -DB(3)
10 -DB(4)
12 -DB(5)
14 -DB(6)
16 -DB(7)
18 -DB(P)
20 GROUND
22 GROUND
24 GROUND
26 \*TERMPWR (not connected to internal power supply)
28 GROUND
30 GROUND
32 -ATN
34 GROUND
36 -BSY
38 -ACK
40 -RST
42 -MSG
44 -SEL
46 -C/D
48 -REQ
50 -I/O

# Notes

All odd pins except pin 25 are connected to ground.

Pin 25 should be left open, but may be connected to ground.

A minus sign indicates active low.

Maximum cable length is 6 m.

Address dip switches at rear of player. Dip switch in up position = OFF. Switches 1 - 4 and switch 8 should be OFF. Switches 5 - 7 determine the SCSI bus address of the player as follows:

|  address | switch 5 | switch 6 | switch 7  |
| --- | --- | --- | --- |
|  0 | OFF | OFF | OFF  |
|  1 | OFF | OFF | ON  |
|  2 | OFF | ON | OFF  |
|  3 | OFF | ON | ON  |
|  4 | ON | OFF | OFF  |
|  5 | ON | OFF | ON  |
|  6 | ON | ON | OFF  |
|  7 | ON | ON | ON  |

(Factory setting: address 0)

Termination according to SCSI: 330 ohms to +5 V
220 ohms to 0 V

If you have more than one device connected to the host computer via the SCSI bus, the SCSI bus termination in the player has to be altered. Refer to Philips Service for further information.

45