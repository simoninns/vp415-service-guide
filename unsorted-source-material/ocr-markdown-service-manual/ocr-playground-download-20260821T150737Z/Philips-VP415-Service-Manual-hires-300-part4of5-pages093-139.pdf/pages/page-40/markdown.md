# CHAPTER 2 VP400 series

# Introduction

The VP400 series is a new generation of LaserVision disc drives with all the versatile LaserVision facilities, such as picture or chapter search, moving pictures, still frames, forward, reverse and variable speed. These facilities can be programmed through a separate computer for interactive applications.

characteristic of these disc drives:

- Front loading
- Solid-state laser
- Computer control via RS232C interface.
- RGB output for full-bandwidth moving or still pictures.
Functional modular design.
- Average random access time \(\leqslant 1\) sec.
- Instant jump of up to 50 frames in either direction.
Electronic timebase correction.
- Genlock external video synchronisation.
- Infra-red/wired or SCART RC-5 remote control.
- Programmable with the remote control handset.
- Auto replay via replay switch.

Depending on the specific type of the VP400 generation, more features are created.

# Audio/video signal path

The audio and video information on the video disc has been fixed in the form of pits. The information can be read by means of a laser beam having a wavelength of 780nm. The laser light modulated by the disc falls on the photodiode present and is thus converted into an electrical signal. This signal is a high frequency signal which is amplified on module Z, see the block diagram of the audio/video signal path. The output signal of this module, HF-OUT 1, goes to module K where it is in the first instance split into an h.f. audio and an h.f. video signal. The h.f. audio signal goes as HF-AUD to module H on behalf of timebase correction. The h.f. video signal is also demodulated on module K and gets amplification correction by means of the MTF signal. The demodulated composite video signal, CV-DEM, goes to module L where drop-out correction takes place.

Drop-out correction is realized on module L by filling it in on a video line which contains a drop-out, together with the video contents of the preceding video line. To achieve this the video signal is delayed one line time (64μs) and, if a drop-out is detected, filled in in the passing video signal. This is possible because a switch, operated by the drop-out detector, can select the "direct" video or the delayed video. On this module the MTF signal is created too. This is done by measuring the amplitude of the colour burst signal in the video signal and realizing a dc voltage dependent on this value (the MTF signal). The output signal of module L is fed to module H to obtain timebase correction just like the h.f. signal.

On module H the h.f. signal (HF-AUD) and the composite video signal (CV-DOC) are both led through a CCD memory IC and as a result the signals get a delay which depends on the clock frequency offered. The clock frequency is determined by the VCO present which is controlled by the TANG-ER signal (tangential or timebase error signal). The correction which takes place by the TANG-ER signal is the coarse correction. Next the audio and video signal is led through a variable LC delay line with a delay that depends on the BURST-ER signal. This BURST-ER signal is the result of a phase comparison of the disc video signal (CV-TBM) with a reference signal derived from the reference source on module D. The timebase correction by means of the BURST-ER signal is a fine adjustment. The timebase corrected h.f. audio signal (HFATBC) and composite video signal (CV-TBC) are processed further on modules A and C resp.

On module A the HFATBC is split into two paths on behalf of demodulation of the two audio channels. On this module drop-out detection takes place too where, in the case of a drop-out, the l.f. audio signal is kept at the last level just before the dropout (track and hold principle). The two output signals (AUD1 and AUD2) go to analog I/O module U.

The two low-frequency signals AUD1 and AUD2 enter at the analog I/O module U where selection takes place between the externally offered audio signals (EXT AUD1 and EXT AUD2) and the internal audio signals. The audio signals can also be switched off by means of switching signals AUD1ON and AUD2ON. A beep can be added to the audio signals dependent on the A-SYNT command of the drive processor (module R). The two audio signals are available on 2 BNC connectors at the rear of the disc drive and also on the Euroconnector.

The composite video signal (CV-TBC) goes from module H to module C where it is processed further. First of all there is selection possible between the internal video and composite sync (CS-REF) of reference source module D. This among other things in connection with sync during mute. Next switching is possible between the internal video or reference sync and the externally offered composite video signal (CV-EXT), coming from analog I/O module U.

The signal further receives a required black level clamping and, if desired, the index insert. For this purpose there are two signals VOBN to see to an index background and VOW for the insert of the index information lying at white level. From the video signal the line frequency sandcastle signal (SC) is generated by means of a sync separator and with the VBL (vertical blanking) signal this signal also receives the frame frequency component. The video signal is buffered along two paths, with one CVBS signal going to module B and the other CVBS signal being stripped of the special burst signal, which is a standard presence in the video signal. The latter signal goes to analog I/O module U.

The dc level of the CVBS2 signal which arrives at module U is restored and goes as TXT CVBS to the TXT section of this module. Moreover, a possible selection takes place between the externally connected video signal (CVBS IN) and the TXT CVBS signal. Selection can be done by means of switching signal CV-E/I. The output signal of this switch goes to manual switch SK2 and is as CVBS OUT available on a BNC connector at the rear of the disc drive. With switch SK2 a selection can take place between "not encoded" video and "encoded" video. The internal composite signal CVBS2 is transferred directly from the disc but is as such not suited for connection to monitors when use is made of the special playing possibilities of the disc drive. The encoded CVBS is suited for monitor use but has a limited bandwidth (3 MHz).

The CVBS signal of module C (with special burst) is on module B decoded into RGB with complete bandwidth. For this purpose the CVBS signal is split into a luminance and a chrominance part. The chroma signal is decoded into the colour difference signals R-Y and B-Y. Together with the luminance signal LUM encoding into CVBS takes place on module U. Colour signals R, G and B come from the RGB matrix on module B and go, via module U, to the video mixer module Y in the sandwich section of VP415.

Whether or not on module Y mixed with the RGB signals of a computer to be connected externally, where the mode of mixing depends on signals VP0, VP1 and VP2 the outgoing RGB signals go to the Euroconnector via module U. Thus the RGB signals are with complete bandwidth (5 MHz) available for a monitor to be connected, just like the encoded CVBS signal (bandwidth 3 MHz).