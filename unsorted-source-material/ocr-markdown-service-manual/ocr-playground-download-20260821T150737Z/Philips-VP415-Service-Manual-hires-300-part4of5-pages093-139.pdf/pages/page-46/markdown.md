11

# The servo block diagram

For the blockdiagram of the servo signals see Fig.SE1. This diagram is a survey of all modules which are necessary for a correct functioning of the optical deck.

The modules are:

- The deck electronics Z
- Focus module J
- Radial drive module M
- Drive processor R
- Slide motor drive E
- Motor + Sequence module F
- Genlock module G

# Short description

From the laser source a beam of laser light is projected on photodiodes A-D and R1-R2 on the optical unit. The laser light is converted into electrical signals and applied to the servo preamplifier and the radial amplifier. From the servo preamplifier a signal FPI (objective focussed) and the focus error signal are fed to focus drive module J via connectors 8Z42J1 and 9Z4-1J1. In the focus drive module focus drive signal FOC-ACT is generated and fed back to the objective via 5J1-3Z4. This module can only operate when focus enable signal FOC-EN which is coming via 22aR2 7J1 from the drive processor is "H". When the objective is focussed, the focus indication signal FOCIND "L" is fed via 6J1-21aR2 to the drive processor R.

From the radial part of the servo preamplifier radial error signal RAD-ER is applied to radial drive module M via 7Z4-2M2 and tracking position indication signal TPI via 6Z4-3M2. The output of radial drive RAD-ACT, which is fed via 6M2-2Z4 to the deck, controls the radial mirror. The radial module only operates when radial loopswitch signal RLS coming from the drive processor is "L". In case of jumps over one or more tracks, a CP1 or CP2 "L" signal is coming from the drive processor via 26aR2-7M1 or 27aR28M1 and at the same time clipped radial signal CL-RAD is fed back to the drive processor.

The drive processor controls the start of the turntable motor by means of the TTM signal which is via 22cR1-1F1 fed to the motor and sequence module F and when the motor is running a 2PPR (2 pulses per revolution) signal is fed back via 4F1-23cR1.

The drive processor also controls the position of the slide. This is executed by the output expander which feeds 4 commutating signals via 12aR1-15aR1 to 5E1-2E1 and a slide power signal SLPWR via 16aR1-1E1 to the slide motor drive module E. In the slide motor drive module the commutating signals are converted into drive signals for the slide motor and via plugs 1E2-6E2 supplied to the deck.

Motor+sequence module F takes care of the drive of the turntable motor. For control of this motor various signals are used, depending on the conditions. For running condition the TTM signal is "H" and is fed to the block start/stop sequence. The start/stop sequence block also gets information from the Hall elements in the motor via plugs 2-11F3 and the comparator block. During acceleration only the TTM signal is operating and via the motor control block converted in a pulse width modulated signal PWM with a minimum duty-cycle. The PWM-signal controls the commutation block which is supplying 6 drive voltages to the three output stages in the motor drive block. The output stages are connected via plug 5-7F1 to the motor. When the motor reaches the speed of 1500 RPM, the acceleration is stopped by the D/A converter and the motor control is taken over by LPWM, a frequency control signal coming from the block line speed measurement. In this block the line frequency of the video signal on the disc is

measured by means of LPO pulses supplied by the GENLOCK module via 9G1-4F2. After a short time, when the speed is within 5% of the correct speed, the motor control will be switched over to phase control. This is performed by the sequence circuit which then delivers the motor control enable signal MCO-EN and via the Genlock module and plug 8G1-5F2 the 15625 Hz dutycycle controlled MCO- signal is supplied to the motor control block. The motor control will be switched back to frequency control in case of search mode on a CLV disc. In that case the CLV-TC signal from the drive processor, fed via 22aR1-2F1 to the sequence circuit will be "H". In case there is a loss of focus during search, the drive processor delivers a MEM-SU signal via 22cR1-5F1, which activates a memory in the tachocircuit and the information of the last motor speed will be stored. As soon as focus is correct again, the motor will speed up to the original velocity.

CS 7 884