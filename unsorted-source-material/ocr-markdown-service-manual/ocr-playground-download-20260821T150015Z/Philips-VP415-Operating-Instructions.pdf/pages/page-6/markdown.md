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