#include "odometry.h"

namespace PID
{
    // Amount in inches the robot will drive
    double driveTarget = 0;
    // Amount in Degrees the robot will turn
    double turnTarget = 0;

    // How far each side of the bot is from the target
    double leftError = 0;
    double rightError = 0;
    // Velocity of each side of the bot (in volts)
    double leftVelo = 0;
    double rightVelo = 0;


    // Current Time
    double cTime = 1;

    // PID tuning values while driving straight
    constexpr double driveKp = 10.0 / 1000.0;
    constexpr double driveKi = 1 / 1000.0;
    constexpr double driveKd = 2.5 / 1000.0;
    // PID tuning values while turning
    constexpr double turnKp = 10.0 / 1000.0;
    constexpr double turnKi = 1 / 1000.0;
    constexpr double turnKd = 2.5 / 1000.0;

    // Time in milliseconds before the I variable kicks in
    double driveIDelay = 1000;
    double turnIDelay = 1000;

    // Minimum Speed of the Motor in volts
    double minSpeed = .25;
    // Maximum Speed of the Motor in volts
    double maxSpeed = 12;

    // Minimum time the PID Loop will run in milliseconds
    double minTime = 100;
    // Maximum time the PID Loop will run in milliseconds
    double maxTime = 10000; // 10 Seconds

    // Multiply the calculated velocity by this number
    double multiplier = 1;

    // How long between PID loops in milliseconds
    double loopBuffer = 10;

    // If False the motor will not run during the PID
    bool leftMotorsEnabled = true;
    bool rightMotorsEnabled = true;

    vex::brakeType bt = brake;

    // Get and Set methods

    double getDriveTarget()
    { return driveTarget; }

    double getTurnTarget()
    { return turnTarget; }

    double getLeftError()
    { return leftError; }

    double getRightError()
    { return rightError; }

    double getLeftVelocity()
    { return leftVelo; }

    double getRightVelocity()
    { return rightVelo; }

    double getAverageVelocity()
    { return (leftVelo + rightVelo) / 2.0; }

    double getTime()
    { return cTime; }

    double getDriveIDelay()
    { return driveIDelay; }

    double setIDelay(double iDelay)
    { return driveIDelay = iDelay;}

    double getTurnIDelay()
    { return turnIDelay; }

    double setTurnIDelay(double iDelay)
    { return turnIDelay = iDelay; }

    double getMinSpeed()
    { return minSpeed; }

    double setMinSpeed(double a)
    { return minSpeed = a; }

    double getMaxSpeed()
    { return maxSpeed; }

    double setMaxSpeed(double speed)
    { return maxSpeed = speed; }

    double getMultiplier()
    { return multiplier; }

    // Multiplier must be greater than 0 
    double setMultiplier(double mult)
    {
        if (mult > 0)
        { return multiplier = mult; }
        return multiplier = 1;
    }
    
    bool getLeftMotorsEnabled()
    { return leftMotorsEnabled; }

    bool toggleLeftMotors()
    { return leftMotorsEnabled = !leftMotorsEnabled; }

    bool getRightMotorsEnabled()
    { return rightMotorsEnabled; }

    bool toggleRightMotors()
    { return rightMotorsEnabled = !rightMotorsEnabled; }

    brakeType getBrakeType()
    { return bt; }

    brakeType setBrakeType(brakeType bType)
    { return bt = bType; }

    bool pidEnd()
    {
        // Set target to 0
        double target = 0;
        // Set velocity to 0
        double leftVelo = 0;
        double rightVelo = 0;
        // Set time to 1
        double cTime = 1;
        // Stop robot with brake type bt
        driveStop(bt);
        return true;
    }

    // Drive forwards or backwards (with negative target) using a PID. PID velocity
    // is multiplied by multiplier variable
    void drive(double driveTarget)
    {
        // Get current position of the middle motor encoders for measurement, in degrees
        // Add converted target from inches traveled to degrees in respect to wheel size
        double targetL = LeftMiddleDrive.position(degrees) + (driveTarget * inchToDegreeConverter);
        double targetR = RightMiddleDrive.position(degrees) + (driveTarget * inchToDegreeConverter);

        // This is calculated in this order to show how error will be derived during the program
        leftError = targetL - LeftMiddleDrive.position(degrees);
        rightError = targetR - RightMiddleDrive.position(degrees);

        // Continue PID loop until both sides satisfy exit conditions
        while ( (abs(leftError) > 45 || abs(rightError) > 45 || ((cTime * loopBuffer) < minTime)) && ((cTime * loopBuffer) < maxTime) )
        {
            // Update the left and right Error values at the beginning of each loop
            leftError = targetL - LeftMiddleDrive.position(degrees);
            rightError = targetR - RightMiddleDrive.position(degrees);
            
            // If the left side meets all exit condidtions set the velocity to 0
            if ( (abs(leftError) > 45 || ((cTime * loopBuffer) < minTime)) && ((cTime * loopBuffer) < maxTime) )
            {
                leftVelo = 0;
            }
            else
            {
                // Calculate left side velocity using drive tuning values
                leftVelo = /*Calculate P*/ (driveKp * leftError) + 
                        /*Calculate I*/ (driveKi * leftError * 
                        /*Multiply by I after loop buffer otherwise by 0 */(std::max((cTime * loopBuffer) - driveIDelay, 0.0))) +
                        /*Calculate D*/ (driveKd * leftError / cTime);
            }

            // If the RIGHT side meets all exit condidtions set the velocity to 0
            if ( (abs(rightError) > 45 || ((cTime * loopBuffer) < minTime)) && ((cTime * loopBuffer) < maxTime) )
            {
                rightVelo = 0;
            }
            else
            {
                // Calculate left side velocity using drive tuning values
                rightVelo = /*Calculate P*/ (driveKp * rightError) + 
                        /*Calculate I*/ (driveKi * rightError * 
                        /*Multiply by I after loop buffer otherwise by 0 */(std::max((cTime * loopBuffer) - driveIDelay, 0.0))) +
                        /*Calculate D*/(driveKd * rightError / cTime);
            }

            // Multiply velocities by their multiplier
            // Set velocities between their minimum and maximum values
            leftVelo = std::min(std::max(leftVelo * multiplier, minSpeed), maxSpeed);
            rightVelo = std::min(std::max(rightVelo * multiplier, minSpeed), maxSpeed);

            // Spin at velocity leftVelo and rightVelo
            driveLeftForward(leftVelo, voltageUnits::volt);
            driveRightForward(rightVelo, voltageUnits::volt);
            cTime++;
            wait(loopBuffer, msec);
        }
        pidEnd();
    }

    // This function turns the bot left using a PID incorporating the inertial
    // sensor. PID velocity is multiplied by multiplier
    void turn(double turnTarget)
    {
        // Get current net Inertial rotation and add the target turning amount
        double target = Inertial.rotation() + turnTarget;

        // This is calculated in this order to show how error will be derived during the program
        double error = target - Inertial.rotation();

        // Continue PID loop until all exit conditions are satisfied
        while ( (abs(error) > 1 || ((cTime * loopBuffer) < minTime)) && ((cTime * loopBuffer) < maxTime) )
        {
            error = target - Inertial.rotation();

            // If all exit condidtions are met set the velocity to 0
            if ( (abs(error) > 1 || ((cTime * loopBuffer) < minTime)) && ((cTime * loopBuffer) < maxTime) )
            {
                leftVelo = 0;
                rightVelo = 0;
            }
            else
            {
                // Calculate velocity using turn tuning values
                leftVelo = /*Calculate P*/ (turnKp * error) + 
                        /*Calculate I*/ (turnKi * error * 
                        /*Multiply by I after loop buffer otherwise by 0 */(std::max((cTime * loopBuffer) - turnIDelay, 0.0))) +
                        /*Calculate D*/(turnKd * error / cTime);
                rightVelo = leftVelo;
            }
            
            // Multiply velocities by their multiplier
            // Set velocities between their minimum and maximum values
            leftVelo = std::min(std::max(leftVelo * multiplier, minSpeed), maxSpeed);
            rightVelo = std::min(std::max(rightVelo * multiplier, minSpeed), maxSpeed);

            // Spin at velocity leftVelo and rightVelo (turning right is positive)
            driveLeftForward(leftVelo, voltageUnits::volt);
            driveRightBackward(rightVelo, voltageUnits::volt);
            cTime++;
            wait(loopBuffer, msec);
        }
        pidEnd();
    }

    // Method to calculate path to a location
    void goTo(double x, double y)
    {
        
    }

};

using namespace PID;