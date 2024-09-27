#include "autonomous.h"

void drivercontrol(void)
{
    while(1)
    {
        // Tank Drive
        axis2 = Controller.Axis2.value(percent);
        axis3 = Controller.Axis3.value(percent);

        // If Controller joystick is beyond deadband
        if(axis3 > 5 || axis3 < -5)
        {
            // Translate the joystick values for better control using a power function
            // Run the left side motors at the calculated speed
            driveLeftForward(pow(axis3, 2) * .12 / 100.0 * Math.sign(axis3), volt);
        }
        else
        {
            // Brake when motors are over 50 rpm
            if(abs(LeftDriveGroup.velocity(rpm)) > 50)
            {
                driveLeftStop(brake);
            }
            else
            {
                driveLeftStop(coast);
            }
        }

        // If Controller joystick is beyond deadband
        if(axis2 > 5 || axis2 < -5)
        {
            // Translate the joystick values for better control using a power function
            // Run the left side motors at the calculated speed
            driveRightForward(pow(axis3, 2) * .12 / 100.0 * Math.sign(axis3), volt);
        }
        else
        {
            // Brake when motors are over 50 rpm
            if(abs(RightDriveGroup.velocity(rpm)) > 50)
            {
                driveRightStop(brake);
            }
            else
            {
                driveRightStop(coast);
            }
        }

        // Arcade Drive
        axis1 = Controller.Axis1.value(percent);
        axis3 = Controller.Axis3.value(percent);

        if(axis1 > 5 || axis1 > -5 || axis3 > 5 || axis 3 < -5)
        {
            turnVolt = axis1 * 0.12;
            forwardVolt = axis3 * .12 * (1 - std::abs(turnVolt / 12.0) * .5);

            driveLeftForward(forwardVolt - turnVolt, volt);
            driveRightForward(forwardVolt + turnVolt, volt);
        }
        else
        {
            // Brake when motors are over 50 rpm
            if(abs(LeftDriveGroup.velocity(rpm)) > 50)
            {
                driveLeftStop(brake);
            }
            else
            {
                driveLeftStop(coast);
            }
            // Brake when motors are over 50 rpm
            if(abs(LeftDriveGroup.velocity(rpm)) > 50)
            {
                driveLeftStop(brake);
            }
            else
            {
                driveLeftStop(coast);
            }
        }

        // Debug - print a specified value to the brain, updating it every 200 milliseconds
        if(printWaiting <= 0)
        {
            Brain.Screen.printAt(138, 108, "num: %d", (abs(LeftDriveGroup.velocity(rpm)) + abs(RightDriveGroup.velocity(rpm))) / 2.0);
            printWaiting = 20;
        }
        printWaiting--;

        // Sleep for 10 milliseconds in between loops
        task::sleep(10);
    }
}