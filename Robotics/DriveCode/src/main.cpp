#include "vex.h"
#include "auton_selector.h"
#include "autonomous.h"
#include "driver_control.h"

competition Competition;

int main()
{
    // Run the pre-autonomous function
    pre_auton();
    
    // Run the auton selection function
    //auton_selector();

    // Set up Callbacks for autonomous and drivercontrol
    Competition.autonomous(autonomous);
    Competition.drivercontrol(driver_control);

    // Prevent main from exiting with an infinite loop.
    while(1)
    {
        // Brain.Screen.printAt(138, 108, "num: %d", (abs(LeftDriveGroup.velocity(rpm)) + abs(RightDriveGroup.velocity(rpm))) / 2.0);
        this_thread::sleep_for(100);
    }
}