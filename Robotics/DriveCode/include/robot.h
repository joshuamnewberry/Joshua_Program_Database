#pragma once
#include "vex.h"

namespace Drive
{
    // Drive forward at velocity "velo" with default of 100
    void driveForward(double velo = 100, velocityUnits unit = velocityUnits::pct);

    // Drive forward at velocity "velo" in volts
    void driveForward(double velo, voltageUnits unit);

    // Drive backward at velocity "velo" with default of 100
    void driveBackward(double velo = 100, velocityUnits unit = velocityUnits::pct);

    // Drive backward at velocity "velo" in volts
    void driveBackward(double velo, voltageUnits unit);

    // Turn Left at velocity "velo" with default of 100
    void turnLeft(double velo = 100, velocityUnits unit = velocityUnits::pct);

    // Turn Left at velocity "velo" in volts
    void turnLeft(double velo, voltageUnits unit);

    // Turn Right at velocity "velo" with default of 100
    void turnRight(double velo = 100, velocityUnits unit = velocityUnits::pct);

    // Turn Right at velocity "velo" in volts
    void turnRight(double velo, voltageUnits unit);

    // Drive Left Motors forward at velocity "velo" with default of 100
    void driveLeftForward(double velo = 100, velocityUnits unit = velocityUnits::pct);

    // Drive Left Motors forward at velocity "velo" in volts
    void driveLeftForward(double velo, voltageUnits unit);

    // Drive Left Motors reverse at velocity "velo" with default of 100
    void driveLeftBackward(double velo = 100, velocityUnits unit = velocityUnits::pct);

    // Drive Left Motors reverse at velocity "velo" in volts
    void driveLeftBackward(double velo, voltageUnits unit);
    
    // Drive Left Motors forward at velocity "velo" with default of 100
    void driveRightForward(double velo = 100, velocityUnits unit = velocityUnits::pct);

    // Drive Left Motors forward at velocity "velo" in volts
    void driveRightForward(double velo, voltageUnits unit);

    // Drive Right Motors reverse at velocity "velo" with default of 100
    void driveRightBackward(double velo = 100, velocityUnits unit = velocityUnits::pct);

    // Drive Right Motors reverse at velocity "velo" in volts
    void driveRightBackward(double velo, voltageUnits unit);

    void driveStop(brakeType bt = brakeType::brake);

    void driveLeftStop(brakeType bt = brakeType::brake);

    void driveRightStop(brakeType bt = brakeType::brake);
};