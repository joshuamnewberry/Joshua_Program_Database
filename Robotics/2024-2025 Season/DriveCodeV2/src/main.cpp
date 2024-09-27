#include "drivercontrol.h"

int main()
{
    // Run the pre-autonomous function
    pre_auton();

    // Run the auton selection function
    auton_selector();

    // Run the autonomous function
    Competition.autonomous(autonomous);

    // Run the driver control function
    Competition.drivercontrol(drivercontrol);

    // Prevent main from exiting with an infinite loop.
    while(1)
    {
        task::sleep(100);
    }
}