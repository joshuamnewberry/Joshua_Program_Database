#include "robot_config.h"

namespace Drive
{
    // Drive forward at velocity "velo" with default of 100
    void driveForward(double velo = 100, velocityUnits unit = velocityUnits::pct)
    { 
        LeftDriveGroup.spin(forward, velo, unit);
        RightDriveGroup.spin(forward, velo, unit);
    }

    // Drive forward at velocity "velo" in volts
    void driveForward(double velo, voltageUnits unit)
    { 
        LeftDriveGroup.spin(forward, velo, unit);
        RightDriveGroup.spin(forward, velo, unit);
    }

    // Drive backward at velocity "velo" with default of 100
    void driveBackward(double velo = 100, velocityUnits unit = velocityUnits::pct)
    { 
        LeftDriveGroup.spin(reverse, velo, unit);
        RightDriveGroup.spin(reverse, velo, unit);
    }

    // Drive backward at velocity "velo" in volts
    void driveBackward(double velo, voltageUnits unit)
    { 
        LeftDriveGroup.spin(reverse, velo, unit);
        RightDriveGroup.spin(reverse, velo, unit);
    }

    // Turn Left at velocity "velo" with default of 100
    void turnLeft(double velo = 100, velocityUnits unit = velocityUnits::pct)
    {
        LeftDriveGroup.spin(reverse, velo, unit);
        RightDriveGroup.spin(forward, velo, unit);
    }

    // Turn Left at velocity "velo" in volts
    void turnLeft(double velo, voltageUnits unit)
    {
        LeftDriveGroup.spin(reverse, velo, unit);
        RightDriveGroup.spin(forward, velo, unit);
    }

    // Turn Right at velocity "velo" with default of 100
    void turnRight(double velo = 100, velocityUnits unit = velocityUnits::pct)
    { 
        LeftDriveGroup.spin(forward, velo, unit);
        RightDriveGroup.spin(reverse, velo, unit);
    }

    // Turn Right at velocity "velo" in volts
    void turnRight(double velo, voltageUnits unit)
    { 
        LeftDriveGroup.spin(forward, velo, unit);
        RightDriveGroup.spin(reverse, velo, unit);
    }

    // Drive Left Motors forward at velocity "velo" with default of 100
    void driveLeftForward(double velo = 100, velocityUnits unit = velocityUnits::pct)
    {
        LeftDriveGroup.spin(forward, velo, unit);
    }

    // Drive Left Motors forward at velocity "velo" in volts
    void driveLeftForward(double velo, voltageUnits unit)
    {
        LeftDriveGroup.spin(forward, velo, unit);
    }

    // Drive Left Motors reverse at velocity "velo" with default of 100
    void driveLeftBackward(double velo = 100, velocityUnits unit = velocityUnits::pct)
    {
        LeftDriveGroup.spin(reverse, velo, unit);
    }

    // Drive Left Motors reverse at velocity "velo" in volts
    void driveLeftBackward(double velo, voltageUnits unit)
    {
        LeftDriveGroup.spin(reverse, velo, unit);
    }
    
    // Drive Left Motors forward at velocity "velo" with default of 100
    void driveRightForward(double velo = 100, velocityUnits unit = velocityUnits::pct)
    {
        RightDriveGroup.spin(forward, velo, unit);
    }

    // Drive Left Motors forward at velocity "velo" in volts
    void driveRightForward(double velo, voltageUnits unit)
    {
        RightDriveGroup.spin(forward, velo, unit);
    }

    // Drive Right Motors reverse at velocity "velo" with default of 100
    void driveRightBackward(double velo = 100, velocityUnits unit = velocityUnits::pct)
    {
        RightDriveGroup.spin(reverse, velo, unit);
    }

    // Drive Right Motors reverse at velocity "velo" in volts
    void driveRightBackward(double velo, voltageUnits unit)
    {
        RightDriveGroup.spin(reverse, velo, unit);
    }

    void driveStop(brakeType bt = brake)
    {
        LeftDriveGroup.stop(bt);
        RightDriveGroup.stop(bt);
    }

    void driveLeftStop(brakeType bt = brake)
    {
        LeftDriveGroup.stop(bt);
    }

    void driveRightStop(brakeType bt = brake)
    {
        RightDriveGroup.stop(bt);
    }
};

using namespace Drive;