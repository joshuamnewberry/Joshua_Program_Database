#include "driver_control.h"
#include "vex.h"
#include "robot_config.h"
#include "robot.h"
#include "odometry.h"
#include "pid.h"
using namespace std;
using namespace Drive;
using namespace PID;

void driver_control(void)
{
    // Start the odometry thread
    odometryTask = thread(odometryFunction);
    while(1)
    {
        if(tankDrive)
        {
            // Tank Drive
            axis2 = Controller.Axis2.position(percent);
            axis3 = Controller.Axis3.position(percent);

            // If Controller joystick is beyond deadband
            if(axis3 > 5 || axis3 < -5)
            {
                // Translate the joystick values for better control using a power function
                // Run the left side motors at the calculated speed
                driveLeftForward(pow(axis3, 2) * .12 / 100.0 * copysign(1, axis3), volt);
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
                driveRightForward(pow(axis2, 2) * .12 / 100.0 * copysign(1, axis2), volt);
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
        }
        else
        {
            // Arcade Drive
            axis1 = Controller.Axis1.position(percent);
            axis3 = Controller.Axis3.position(percent);

            if(axis1 > 5 || axis1 < -5 || axis3 > 5 || axis3 < -5)
            {
                turnVolt = axis1 * 0.12;
                forwardVolt = axis3 * .12 * (1 - abs(turnVolt / 12.0) * 0.5);

                driveLeftForward(forwardVolt + turnVolt, volt);
                driveRightForward(forwardVolt - turnVolt, volt);
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
                if(abs(RightDriveGroup.velocity(rpm)) > 50)
                {
                    driveRightStop(brake);
                }
                else
                {
                    driveRightStop(coast);
                }
            }
        }

        // Sleep for 20 milliseconds in between loops
        task::sleep(10);
    }
}