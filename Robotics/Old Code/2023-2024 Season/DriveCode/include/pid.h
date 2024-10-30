#pragma once
#include "odometry.h"


class PID
{
    // Amount in inches the robot will drive
    double target = 0;
    // How far each side of the bot is from the target
    double lError = 0;
    double rError = 0;
    // Velocity of each side of the bot
    double lVelo = 0;
    double rVelo = 0;
    // Current Time
    double cTime = 1;

    // False when PID Loop is running
    bool complete = true;

    // Driving tuning values:
    static constexpr double driveKp = 1.525 / 100.0;
    static constexpr double driveKi = .1 / 100.0;
    static constexpr double driveKd = .225 / 100.0;

    // Turning tuning values
    static constexpr double turnKp = 0.31*2/3;
    static constexpr double turnKi = 0.01*2/3;
    static constexpr double turnKd = 0.02*2/3;

    // Time in milliseconds before the I variable kicks in
    double iDelay = 1000;
    // Minimum Speed of the Motor in volts
    double minSpeed = .275;
    // Maximum Speed of the Motor in volts
    double maxSpeed = 11;

    // Minimum time for the PID Loop to run in milliseconds
    double minTime = 200;
    // Maximum time for the PID Loop to run in milliseconds
    double maxTime = 4000;

    // When error >= maxError, velocity should be at max
    double maxError = 50000;

    // Multiply calculated velocity by:
    double multiplier = 1;

    // How long in milliseconds between iterations
    double loopBuffer = 10;

    // When transmission is enabled this should be set to false
    bool topMotorsEnabled = true;

    // Can disable left or right motors to turn using one side
    bool leftMotorsEnabled = true;
    bool rightMotorsEnabled = true;

    brakeType bt = brake;

    public: double getTarget()
    { return target; }

    public: double getLeftError()
    { return lError; }

    public: double getRightError()
    { return rError; }

    public: double getLeftVelocity()
    { return lVelo; }

    public: double getRightVelocity()
    { return rVelo; }

    public: double getAverageVelocity()
    { return (lVelo + rVelo) / 2.0; }

    public: double getTime()
    { return cTime; }

    public: double getIDelay()
    { return iDelay; }

    public: double setIDelay(double a)
    { return iDelay = a;}

    public: double getMinSpeed()
    { return minSpeed; }

    public: double setMinSpeed(double a)
    { return minSpeed = a; }

    public: double getMaxSpeed()
    { return maxSpeed; }

    public: double setMaxSpeed(double a)
    { return maxSpeed = a; }

    public: double getMultiplier()
    { return multiplier; }

    public: double setMultiplier(double a)
    {
        if(0 <= a && a <= 1) return multiplier = a;
        else return multiplier = 1;
    }

    public: bool getTopMotorsEnabled()
    { return topMotorsEnabled; }

    public: bool toggleTopMotors()
    { return topMotorsEnabled = !topMotorsEnabled; }

    public: bool getLeftMotorsEnabled()
    { return leftMotorsEnabled; }

    public: bool toggleLeftMotors()
    { return leftMotorsEnabled = !leftMotorsEnabled; }

    public: bool getRightMotorsEnabled()
    { return topMotorsEnabled; }

    public: bool toggleRightMotors()
    { return rightMotorsEnabled = !rightMotorsEnabled; }

    public: brakeType getBrakeType()
    { return bt; }

    public: brakeType setBrakeType(brakeType a)
    { return bt = a; }

    void pidEnd()
    {
        // Set target to 0
        double target = 0;
        // Set velocity to 0
        double lVelo = 0;
        double rVelo = 0;
        // Set time to 1
        double cTime = 1;
        // Stop robot with brake type bt
        driveStop(bt);
        // Set complete to true
        complete = true;
    }

    // Drive forwards or backwards (with negative target) using a PID. PID velocity
    // is multiplied by multVelo
    public: void drive(double target)
    {
        // Set complete to false at start of PID
        complete = false;

        // True if going backwards
        bool back = target < 0;

        if(back) // Change the direction to drive forward or reverse
        { changeDriveDirection("r"); }
        else
        { changeDriveDirection("f"); }

        // Using tracking wheels means we just need to account for the
        // circumference of those wheels

        // Get current position of the tracking wheels for measurement and
        // compairison, set it in degrees
        double targetL = (140 * target / M_PI) + LDW.position(degrees);
        double targetR = (140 * target / M_PI) + RDW.position(degrees);

        // Changing values:
        // These values will change in order to translate the PID into the robot's
        // motion
        lError = targetL - LDW.position(degrees);
        rError = targetR - RDW.position(degrees);

        if(back)
        {
            // It is easier to handle all positive numbers
            // for the loop conditions and calculations
            lError *= -1;
            rError *= -1;
        }

        cTime = 1;

        // Continue PID loop until both sides satisfy exit conditions
        while(((lError > 50 || rError > 50 || lError < -50 || rError < -50) || ((cTime * loopBuffer) < minTime)) && ((cTime * loopBuffer) < maxTime))
        {
            lError = targetL - LDW.position(degrees);
            rError = targetR - RDW.position(degrees);
            if(back)
            {
                lError *= -1;
                rError *= -1;
            }
            lVelo = driveKp * lError + (driveKi * lError * (std::max((cTime * loopBuffer) - iDelay, 0.0)))
            + (driveKd * lError / cTime);

            if(!(((lError > 25 || lError < -25) || ((cTime * loopBuffer) < minTime)) && ((cTime * loopBuffer) < maxTime)))
            {
                // If left wheel exit conditions are met
                // set velocity to 0
                lVelo = 0;
            }

            rVelo = driveKp * rError + (driveKi * rError * (std::max((cTime * loopBuffer) - iDelay, 0.0)))
            + (driveKd * rError / cTime);

            if(!(((rError > 25 || rError < -25) || ((cTime * loopBuffer) < minTime)) && ((cTime * loopBuffer) < maxTime)))
            {
                // If right wheel exit conditions are met
                // set velocity to 0
                rVelo = 0;
            }

            // Set velocities between min and max
            lVelo = std::min(std::max(lVelo, minSpeed), maxSpeed);
            rVelo = std::min(std::max(rVelo, minSpeed), maxSpeed);

            // Spin at velocity 'u' times a constant (Constant is for more/less speed)
            LFDM.spin(LW, lVelo * multiplier, volt);
            LBDM.spin(LW, lVelo * multiplier, volt);
            RFDM.spin(RW, rVelo * multiplier, volt);
            RBDM.spin(RW, rVelo * multiplier, volt);
            if(topMotorsEnabled)
            {
                LTDM.spin(LW, lVelo * multiplier, volt);
                RTDM.spin(LW, rVelo * multiplier, volt);
            }
            cTime++;
            Brain.Screen.printAt(138, 108, "num: %f", ((lError + rError) / 2.0));
            wait(loopBuffer, msec);
        }
        pidEnd();
    }

    // This function turns the bot left using a PID incorporating the inertial
    // sensor. PID velocity is multiplied by multVelo
    void turnLeft(double target, double multVelo)
    {
        // Defining variables:
        double reading = Inert.heading(deg);
        double dest = 0.0;
        bool stillGo = true;
        double lowRange = 0.0;
        double highRange = 0.0;
        double u;
        // Turn left
        dest = reading - target;
        while(dest < 0)
        { dest = dest + 360; }
        while(dest > 360)
        { dest = dest - 360; }
        lowRange = dest - 2;
        highRange = dest + 2;

        // These values will change in order to translate the PID into the robot's
        // motion
        double Error = reading - dest;
        if(Error < 0)
        { Error += 360; }
        double Time = 1;

        while(stillGo == true)
        {
            reading = Inert.heading(degrees);
            double Error = reading - dest;
            if(Error < 0)
            { Error += 360; }
            u = (turnKp * Error) + (turnKi * Error * Time) + (turnKd * Error / Time);

            // Spin at velocity 'u' times a constant (Constant is for more/less speed)
            if(leftMotorsEnabled)
            {
                LFDM.spin(LW, u * multVelo, percentUnits::pct);
                if(topMotorsEnabled)
                { LTDM.spin(LW, u * multVelo, percentUnits::pct); }
                LBDM.spin(LW, u * multVelo, percentUnits::pct);
            }
            if(rightMotorsEnabled)
            {
                RFDM.spin(RW, u * multVelo, percentUnits::pct);
                if(topMotorsEnabled)
                { RTDM.spin(RW, u * multVelo, percentUnits::pct); }
                RBDM.spin(RW, u * multVelo, percentUnits::pct);
            }
            Time++;
            if(reading >= lowRange && reading <= highRange)
            {
                // Stop: (Breaktype is hold since we don't want it to coast past the point)
                driveStop(brake);
                stillGo = false;
                return;
            }
            if(Error < 1)
            {
                // Stop: (Breaktype is hold since we don't want it to coast past the point)
                driveStop(brake);
                stillGo = false;
                return;
            }
            wait(50, msec);
        }
    }

    // This function turns the bot left using a PID incorporating the inertial
    // sensor. PID velocity is multiplied by multVelo
    void turnRight(double target, double multVelo)
    {
        // Defining variables:
        double reading = Inert.heading(deg);
        double dest = 0.0;
        bool stillGo = true;
        double lowRange = 0.0;
        double highRange = 0.0;
        double u;
        // Turn left
        dest = reading + target;
        while(dest < 0)
        { dest = dest + 360; }
        while(dest > 360)
        { dest = dest - 360; }
        lowRange = dest - 2;
        highRange = dest + 2;

        // These values will change in order to translate the PID into the robot's
        // motion
        double Error = dest - reading;
        if(Error < 0)
        { Error += 360; }
        double Time = 1;

        while(stillGo == true)
        {
            reading = Inert.heading(degrees);
            double Error = dest - reading;
            if(Error < 0)
            { Error += 360; }
            u = (turnKp * Error) + (turnKi * Error * Time) + (turnKd * Error / Time);

            // Spin at velocity 'u' times a constant (Constant is for more/less speed)
            if(leftMotorsEnabled)
            {
                LFDM.spin(LW, u * multVelo, percentUnits::pct);
                if(topMotorsEnabled)
                { LTDM.spin(LW, u * multVelo, percentUnits::pct); }
                LBDM.spin(LW, u * multVelo, percentUnits::pct);
            }
            if(rightMotorsEnabled)
            {
                RFDM.spin(RW, u * multVelo, percentUnits::pct);
                if(topMotorsEnabled)
                { RTDM.spin(RW, u * multVelo, percentUnits::pct); }
                RBDM.spin(RW, u * multVelo, percentUnits::pct);
            }
            Time++;
            if(reading >= lowRange && reading <= highRange)
            {
                // Stop: (Breaktype is hold since we don't want it to coast past the point)
                driveStop(brake);
                stillGo = false;
                return;
            }
            if(Error < 1)
            {
                // Stop: (Breaktype is hold since we don't want it to coast past the point)
                driveStop(brake);
                stillGo = false;
                return;
            }
            wait(50, msec);
        }
    }

    // Helper method for the turn methods where turn left is a negative input
    void turnPID(double target, double multVelo)
    {
        if(target < 0)
        {
            changeDriveDirection("tl");
            turnLeft(-target, multVelo);
        }
        else if(target > 0)
        {
            changeDriveDirection("tr");
            turnRight(target, multVelo);
        }
    }
};

PID pid = PID();