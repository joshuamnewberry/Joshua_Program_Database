#include "autonomous.h"

void drivercontrol(void)
{
    while(1)
    {
        // Tank Drive

        // If Controller joystick is beyond deadband
        if(Controller1.Axis3.value() > 5 || Controller1.Axis3.value() < -5)
        {
            // Translate the joystick values for better control using a power function
            // Run the left side motors at the calculated speed
            driveLeftForward( (sin(Controller1.Axis3.value() * M_PI / 400.0)) * 100.0 );
        }
        else
        {
            // Brake when motors are over 50 rpm
            if(LeftDriveGroup.velocity(rpm) > 50 || LeftDriveGroup.velocity(rpm) < -50)
            {
                driveLeftStop(brake)
            }
            else
            {
                driveLeftStop(coast)
            }
        }

        // If Controller joystick is beyond deadband
        if(Controller1.Axis2.value() > 5 || Controller1.Axis2.value() < -5)
        {
            // Translate the joystick values for better control using a power function
            // Run the left side motors at the calculated speed
            driveRightForward( (sin(Controller1.Axis2.value() * M_PI / 400.0)) * 100.0 );
        }
        else
        {
            // Brake when motors are over 50 rpm
            if(RightDriveGroup.velocity(rpm) > 50 || RightDriveGroup.velocity(rpm) < -50)
            {
                driveRightStop(brake)
            }
            else
            {
                driveRightStop(coast)
            }
        }

        // Debug - print a specified value to the brain, updating it every 500 milliseconds
        if(printWaiting <= 0)
        {
            Brain.Screen.printAt(138, 108, "num: %d", 0.0);
            printWaiting = 20;
        }
        printWaiting--;

        // Sleep for 10 milliseconds in between loops
        task::sleep(10);
    }
}