// ---- START VEXCODE CONFIGURED DEVICES ----
// Robot Configuration:
// [Name]               [Type]        [Port(s)]
// Controller1          controller                   
// LFDM                 motor         1              
// LTDM                 motor         8              
// LBDM                 motor         3              
// RFDM                 motor         4              
// RTDM                 motor         6              
// RBDM                 motor         5              
// CM                   motor         20             
// Inert                inertial      9              
// LDW                  rotation      19             
// RDW                  rotation      13             
// LS1                  limit         D              
// TP                   digital_out   A              
// LAP                  digital_out   B              
// RAP                  digital_out   C              
// FAP                  digital_out   E              
// FBM                  motor         11             
// BBM                  motor         12             
// LS2                  limit         F              
// ---- END VEXCODE CONFIGURED DEVICES ----

#include "driver_control.h"

using namespace vex;
competition Competition;

int main()
{
    // Run the pre-autonomous function
    pre_auton();

    // Run the autonomous function
    Competition.autonomous(autonomous);

    // Wait for release of Button A to start drivercontrol
    while(Controller1.ButtonA.pressing())
    { vex::task::sleep(50); }

    // Run the driver control function
    Competition.drivercontrol(drivercontrol);

    // Prevent main from exiting with an infinite loop.
    while(1)
    { task::sleep(100); }
}