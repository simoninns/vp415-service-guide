# Repair Method VP415

# 1. Introduction

The object of this repair method is to facilitate faultfinding in a defective set for the service technician. The method is set up in such a way that the fault diagnosis in a set under repair is made via a test procedure. In this test procedure several operations should be carried out sequentially and decisions should be made on various points. Via a yes/no decision, the technician is led to a defective module or part of it. A central role in the repair method is played by the Diagnostic Software, which has been implemented in the Drive Processor.

# 2. Diagnostic Software

In the control of the various functions in the set, an important role is played by Drive Processor module R. For this reason the diagnostic software forms an integral part of the drive software of this module.

# a. Set-up

The diagnostic software has been integrated in the drive software in such a way that many of the tasks of the drive are checked for proper performance. If a fault is detected in the execution of a task, an error code is shown on the screen as video overlay.

The error code meets the following priority rule:

1 - 30 fatal fault

31 - 59 major fault

60 - 80 behaviour fault

81 - 99 minor fault

100 - 254 for development

255 initial value (Display - - - )

The lower the error code, the more serious the fault.

# b. Switching on the Diagnostic Software

A fault can be detected in two different modes:

# 1. Check mode

The error code is shown on the screen during manual- or computercontrolled use.

You can enable this check mode by switching on the mains switch while keeping the STAND-BY key on the front panel depressed. Do not release the STAND-BY key until 3 horizontal stripes are visible in the right-hand bottom corner of the picture screen.

# 2. Self-test mode

Now the drive is controlled in a programme loop while the normal operating functions are inoperative.

You can enable the self-test mode by pressing the mains switch while keeping both the EJECT and the STAND-BY key depressed. Do not release the two keys until the word DIAGNOSTICS appears on the screen.

Now the screen not only shows the error code, but also the position of the loop counter and the text DIAGNOSTICS.

The occurrence of minor faults (error code > 60) does not influence the execution of the programme loops; on the other hand, faults having an error code < 60 will interrupt the programme loop and switch the drive into position STAND-BY while keeping the last LDU-slide position.

Both modes are reset again after the mains switch is switched off.

It is advisable to switch off the set only when it is in STAND-BY mode.

CS 8 111