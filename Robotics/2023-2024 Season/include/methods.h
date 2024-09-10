#pragma once
#include "variables.h"

// Change direction of drive base, used for the drive spin program
void changeDriveDirection(std::string a)
{
    // Drive Backward
    if(a == "r")
    {
        LW = directionType::rev;
        RW = LW;
    }
    // Turn Left
    else if(a == "tl")
    {
        LW = directionType::rev;
        RW = directionType::fwd;
    }
    // Turn Right
    else if(a == "tr")
    {
        LW = directionType::fwd;
        RW = directionType::rev;
    }
    // Drive Forward
    else if(a == "f")
    {
        LW = directionType::fwd;
        RW = LW;
    }
}

// Spin drive at pre-set direction at velocity velo
void driveSpin(double velo)
{
    LFDM.spin(LW, velo, percent);
    LTDM.spin(LW, velo, percent);
    LBDM.spin(LW, velo, percent);
    RFDM.spin(RW, velo, percent);
    RTDM.spin(RW, velo, percent);
    RBDM.spin(RW, velo, percent);
}

// Stop all drive motors with brake type BT
void driveStop(vex::brakeType BT)
{
    LFDM.stop(BT);
    LTDM.stop(BT);
    LBDM.stop(BT);
    RFDM.stop(BT);
    RTDM.stop(BT);
    RBDM.stop(BT);
}

void cata()
{
    if(!Controller1.ButtonR2.pressing() && cataWaiting <= 0)
    {
        CM.stop(hold);
    }
}

void count()
{
    if(shotWait <= 0)
    {
        shotCount++;
        shotWait = 5;
    }
}

// Toggle Left Arm
void leftArm()
{ LAP.set(!LAP.value());}

// Toggle Left Arm
void rightArm()
{ RAP.set(!RAP.value()); }

// Toggle Front Arm
void frontArm()
{ FAP.set(!FAP.value()); }

// Toggle transmission
void transmission()
{
    nineBar = !nineBar;
    TP.set(nineBar);
}

// Stop all motors on hold to prevent any movement
void allDriveStop()
{
    while(Controller1.ButtonB.pressing())
    {
        // stop
        LFDM.stop(hold);
        LTDM.stop(hold);
        LBDM.stop(hold);
        RFDM.stop(hold);
        RTDM.stop(hold);
        RBDM.stop(hold);
        wait(50, msec);
    }
    // Reset stopping of motors
    LFDM.setStopping(brake);
    LTDM.setStopping(brake);
    LBDM.setStopping(brake);
    RFDM.setStopping(brake);
    RTDM.setStopping(brake);
    RBDM.setStopping(brake);
}
