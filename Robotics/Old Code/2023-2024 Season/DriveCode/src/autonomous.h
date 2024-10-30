#pragma once
#include "odometry.h"

// Task to run odometry (not currently running)
int calcPosTask()
{
    while(odomEnabled)
    {
        odom.calculatePosition();
        task::sleep(10);
    }
    return 1;
}

void pre_auton(void)
{
    // Set all pistons to false:
    TP.set(false);
    LAP.set(false);
    RAP.set(false);
    FAP.set(false);

    // Set stopping:
    LFDM.setStopping(brake);
    LTDM.setStopping(brake);
    LBDM.setStopping(brake);
    RFDM.setStopping(brake);
    RTDM.setStopping(brake);
    RBDM.setStopping(brake);
    FBM.setStopping(hold);
    BBM.setStopping(hold);
    CM.setStopping(hold);

    // Set velocity:
    LFDM.setVelocity(100, percent);
    LTDM.setVelocity(100, percent);
    LBDM.setVelocity(100, percent);
    RFDM.setVelocity(100, percent);
    RTDM.setVelocity(100, percent);
    RBDM.setVelocity(100, percent);
    FBM.setVelocity(100, percent);
    BBM.setVelocity(100, percent);
    CM.setVelocity(100, percent);

    // Calibrate the inertial sensor.
    Inert.calibrate();
    while(Inert.isCalibrating())
    { wait(10, msec); }
}

void autonomous(void)
{
    // Variables for testing to skip Auton menu
    side = 0;
    point = 3;

    if(side == 0) // Close Autons
    {
        if(point == 1) // Ball in opponent goal
        {
            pid.drive(21);
            pid.turnPID(42.5, 1.1);
            pid.drive(11);
            wait(100, msec);
            pid.drive(-10);
        }
        else if(point == 2) // Win point without opponent goal
        {
            FAP.set(true);
            driveSpin(50);
            wait(150, msec);
            pid.turnPID(-40, 1.1);
            FAP.set(false);
            pid.turnPID(-45, 1.1);
            pid.drive(10);
            pid.turnPID(-45, 1.1);
            pid.drive(32.5);
        }
        else if(point == 3) // Win point with opponet goal
        {
            pid.toggleRightMotors();
            FAP.set(true);
            driveSpin(50);
            RAP.set(true);
            wait(75, msec);
            driveStop(brake);
            RAP.set(false);
            pid.turnPID(-40, 2);
            pid.toggleRightMotors();
            FAP.set(false);
            pid.turnPID(130, 1.1);
            pid.drive(25);
            pid.turnPID(42.5, 1.1);
            changeDriveDirection("f");
            driveSpin(80);
            wait(1000, msec);
            pid.drive(-10);
            pid.turnPID(140, 1.2);
            pid.drive(23.5);
            pid.turnPID(-45, 1.1);
            pid.drive(35);
        }
        else if(point == 4)
        {
            pid.drive(21.25);
            pid.turnPID(43.5, 1.1);
            changeDriveDirection("f");
            driveSpin(100);
            wait(1250, msec);
            pid.drive(-10);
            pid.turnPID(90, 1.1);
            pid.drive(24);
            pid.turnPID(-90, 1.1);
            pid.drive(30);
            LAP.set(true);
            RAP.set(true);
            pid.turnPID(90, 1.1);
            pid.drive(30);
        }
    }
    if(side == 1) // Far Autons
    {
        if(point == 1) // Ball in goal
        {
            driveSpin(100);
            wait(7.5, sec);
            driveSpin(-50);
            wait(2.5, sec);
            driveStop(brake);
        }
        else if(point == 2)
        {
            FAP.set(true);
            driveSpin(50);
            wait(150, msec);
            pid.turnPID(-40, 1.1);
            FAP.set(false);
            pid.turnPID(-45, 1.1);
            driveSpin(100);
            wait(7.5, sec);
            driveSpin(-50);
            wait(2.5, sec);
            driveStop(brake);
        }
        else if(point == 3)
        {

        }
    }
    if(side == 2) // Skills - shoot 45 times
    {
        pid.drive(-10);
        pid.turnPID(22.5, 1.25);
        RAP.set(true);
        wait(250, msec);
        shotCount = 0;
        CM.spin(forward, 95, percent);
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
    }
}