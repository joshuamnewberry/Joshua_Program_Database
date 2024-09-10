#pragma once
#include "autonomous.h"

/*----------------------------------------------------------------------------*/
/*                              User Control Task                             */
/*----------------------------------------------------------------------------*/
void drivercontrol(void)
{
    // If skills is active, auto shoot for first half of drivercontrol
    if(side == 2)
    {
        pid.drive(-10);
        pid.turnPID(22.5, 1.25);
        RAP.set(true);
        wait(250, msec);
        shotCount = 0;
        CM.spin(forward, 100, percent);
        LS1.pressed(count);
        LS2.pressed(count);
        while(shotCount <= 45)
        {
            Brain.Screen.printAt(138, 108, "num: %d", shotCount);
            shotWait--;
            task::sleep(10);
        }
        LS1.pressed(cata);
        LS2.pressed(cata);
        RAP.set(false);
    }

    while(1)
    {
        // Tank Drive
        if(Controller1.Axis3.value() > 5 || Controller1.Axis3.value() < -5)
        {
            leftDriveVelocity = (sin(Controller1.Axis3.value() * M_PI / 400.0)) * 100.0;
            LFDM.spin(forward, leftDriveVelocity, percent);
            LBDM.spin(forward, leftDriveVelocity, percent);
            if(!nineBar)
            LTDM.spin(forward, leftDriveVelocity, percent);
        }
        else
        {
            if(LFDM.velocity(rpm) > 75 || LFDM.velocity(rpm) < -75)
            {
                LFDM.setBrake(brake);
                LBDM.setBrake(brake);
                if(!nineBar)
                LTDM.setBrake(brake);
            }
            else
            {
                LFDM.setBrake(coast);
                LBDM.setBrake(coast);
                if(!nineBar)
                LTDM.setBrake(coast);
            }
            LFDM.stop();
            LBDM.stop();
            if(!nineBar)
            LTDM.stop();
        }
        if(Controller1.Axis2.value() > 5 || Controller1.Axis2.value() < -5)
        {
            rightDriveVelocity = (sin(Controller1.Axis2.value() * M_PI / 400.0)) * 100.0;
            RFDM.spin(forward, rightDriveVelocity, percent);
            RBDM.spin(forward, rightDriveVelocity, percent);
            if(!nineBar)
            RTDM.spin(forward, rightDriveVelocity, percent);
        }
        else
        {
            if(RFDM.velocity(rpm) > 75 || RFDM.velocity(rpm) < -75)
            {
                RFDM.setBrake(brake);
                RBDM.setBrake(brake);
                if(!nineBar)
                RTDM.setBrake(brake);
            }
            else
            {
                RFDM.setBrake(coast);
                RBDM.setBrake(coast);
                if(!nineBar)
                RTDM.setBrake(coast);
            }
                RFDM.stop();
                RBDM.stop();
                if(!nineBar)
                RTDM.stop();
        }

        //Toggle Open and Closed blocker
        if(Controller1.ButtonR1.pressing() && FBM.isDone() && BBM.isDone())
        {
            if(blockerOpen)
            {
                FBM.setBrake(coast);
                // Set timeout:
                FBM.setTimeout(2, sec);
                BBM.setTimeout(2, sec);
                BBM.spinFor(-100, degrees, 15, velocityUnits::pct, false);
                wait(100, msec);
                FBM.spinFor(-100, degrees, 100, velocityUnits::pct, false);
                blockerOpen = false;
            }
            else
            {
                FBM.spinFor(100, degrees, 100, velocityUnits::pct, false);
                BBM.spinFor(100, degrees, 100, velocityUnits::pct, false);
                blockerOpen = true;
            }
        }

        cataWaiting--;
        // Spin Intake and Roller
        if(Controller1.ButtonR2.pressing())
        {
            cataWaiting = 5;
            shotCount++;
            CM.spin(forward, 100, percent);
        }

        // If either Limit switch is activated, stop the Catapult motor
        LS1.pressed(cata);
        LS2.pressed(cata);

        if(Controller1.ButtonUp.pressing())
        {
            LAP.set(true);
            RAP.set(true);
        }
        if(Controller1.ButtonDown.pressing())
        {
            LAP.set(false);
            RAP.set(false);
        }

        // Callbacks to activate side arms
        Controller1.ButtonLeft.pressed(leftArm);
        Controller1.ButtonRight.pressed(rightArm);

        // Callback to activate front arm
        Controller1.ButtonA.pressed(frontArm);

        // Callback to stop all motors while you press B
        Controller1.ButtonB.pressed(allDriveStop);

        // Callback that toggles the transmission on and off
        Controller1.ButtonX.pressed(transmission);

        if(nineBar)
        {
            if(Controller1.ButtonL1.pressing())
            {
                LTDM.spin(reverse, 100, percent);
                RTDM.spin(reverse, 100, percent);
            }
            else if(Controller1.ButtonL2.pressing())
            {
                LTDM.spin(forward, 100, percent);
                RTDM.spin(forward, 100, percent);
            }
            else
            {
                LTDM.stop(hold);
                RTDM.stop(hold);
            }
        }

        // Debug - print a specified value to the brain, updating it every 500 milliseconds
        if(printWaiting <= 0)
        {
            Brain.Screen.printAt(138, 108, "num: %d", 0.0);
            printWaiting = 20;
        }
        printWaiting--;

        // Sleep for 10 milliseconds to not overwork the brain
        task::sleep(10);
    }
}
