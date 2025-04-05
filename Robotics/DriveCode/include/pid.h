#pragma once
#include "vex.h"

namespace PID
{
    // Amount in inches the robot will drive
    extern double driveTarget;
    // Amount in Degrees the robot will turn
    extern double turnTarget;

    // How far each side of the bot is from the target
    extern double leftError;
    extern double rightError;
    // Velocity of each side of the bot (in volts)
    extern double leftVelo;
    extern double rightVelo;

    // Current Time
    extern int cTime;

    // PID tuning values while driving straight
    extern double driveKp;
    extern double driveKi;
    extern double driveKd;
    // PID tuning values while turning
    extern double turnKp;
    extern double turnKi;
    extern double turnKd;

    // Time in milliseconds before the I variable kicks in
    extern double driveIDelay;
    extern double turnIDelay;

    // Minimum Speed of the Motor in volts
    extern double minSpeed;
    // Maximum Speed of the Motor in volts
    extern double maxSpeed;

    // Minimum time the PID Loop will run in milliseconds
    extern double minTime;
    // Maximum time the PID Loop will run in milliseconds
    extern double maxTime;

    // Multiply the calculated velocity by this number
    extern double multiplier;

    // How long between PID loops in milliseconds
    extern double loopBuffer;

    // If False the motor will not run during the PID
    extern bool leftMotorsEnabled;
    extern bool rightMotorsEnabled;

    extern brakeType bt;

    // Get and Set methods

    double getDriveTarget();

    double getTurnTarget();

    double getLeftError();

    double getRightError();

    double getLeftVelocity();

    double getRightVelocity();

    double getAverageVelocity();

    double getTime();

    double getDriveIDelay();

    double setIDelay(double iDelay);

    double getTurnIDelay();

    double setTurnIDelay(double iDelay);

    double getMinSpeed();

    double setMinSpeed(double a);

    double getMaxSpeed();

    double setMaxSpeed(double speed);

    double getMultiplier();

    // Multiplier must be greater than 0 
    double setMultiplier(double mult);
    
    bool getLeftMotorsEnabled();

    bool toggleLeftMotors();

    bool getRightMotorsEnabled();

    bool toggleRightMotors();

    brakeType getBrakeType();

    brakeType setBrakeType(brakeType bType);

    bool pidEnd();

    // Drive forwards or backwards (with negative target) using a PID. PID velocity
    // is multiplied by multiplier variable
    void drive(double driveTarget);

    // This function turns the bot left using a PID incorporating the inertial
    // sensor. PID velocity is multiplied by multiplier
    void turn(double turnTarget);

    // Drives to a certain point on the field using Odometry
    void goTo(double endingX, double endingY);
};