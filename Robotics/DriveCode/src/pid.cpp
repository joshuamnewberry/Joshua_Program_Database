#include "pid.h"
#include "vex.h"
#include "robot_config.h"
#include "robot.h"
#include "odometry.h"
using namespace Drive;
using namespace std;

namespace PID
{
    // How far each side of the bot is from the target
    double leftError = 0;
    double rightError = 0;
    // Velocity of each side of the bot (in volts)
    double leftVelo = 0;
    double rightVelo = 0;

    // Current Time
    int cTime = 1;

    // PID tuning values while driving straight
    double driveKp = 1.0 / 50.0;
    double driveKi = 1.0 / 200.0;
    double driveKd = 1.0 / 100.0;
    // PID tuning values while turning
    double turnKp = 1.0 / 10.0;
    double turnKi = 0.0;
    double turnKd = 0.0;

    // Time in milliseconds before the I variable kicks in
    double driveIDelay = 1000.0;
    double turnIDelay = 1000.0;

    // Minimum Speed of the Motor in volts
    double minSpeed = .25;
    // Maximum Speed of the Motor in volts
    double maxSpeed = 12.0;

    // Minimum time the PID Loop will run in milliseconds
    double minTime = 100.0;
    // Maximum time the PID Loop will run in milliseconds
    double maxTime = 10000.0; // 10 Seconds

    // Multiply the calculated velocity by this number
    double multiplier = 1.0;

    // How long between PID loops in milliseconds
    double loopBuffer = 10.0;

    // If False the motor will not run during the PID
    bool leftMotorsEnabled = true;
    bool rightMotorsEnabled = true;

    brakeType bt = brake;

    // Get and Set methods

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
        // Set time to 1
        cTime = 1;
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
        double targetL = odom.getLeftEncoder() + (driveTarget * inchToDegreeConverter * wheelToMotorConverter);
        double targetR = odom.getRightEncoder() + (driveTarget * inchToDegreeConverter * wheelToMotorConverter);

        // This is calculated in this order to show how error will be derived during the program
        leftError = targetL - odom.getLeftEncoder();
        rightError = targetR - odom.getRightEncoder();
        // Continue PID loop until both sides satisfy exit conditions
        while ( (abs(leftError) > 10 || abs(rightError) > 10 || ((cTime * loopBuffer) < minTime)) && ((cTime * loopBuffer) < maxTime) )
        {
            // Update the left and right Error values at the beginning of each loop
            leftError = targetL - odom.getLeftEncoder();
            rightError = targetR - odom.getRightEncoder();
            // If the left side meets all exit condidtions set the velocity to 0
            if (abs(leftError) <= 10)
            { 
                leftVelo = 0;
            }
            else
            {
                // Calculate left side velocity using drive tuning values
                leftVelo = /*Calculate P*/ (driveKp * leftError) + 
                        /*Calculate I*/ (driveKi * leftError * 
                        /*Multiply by I after loop buffer otherwise by 0 */(max((cTime * loopBuffer) - driveIDelay, 0.0))) +
                        /*Calculate D*/ (driveKd * leftError / cTime);
            }
            // If the RIGHT side meets all exit condidtions set the velocity to 0
            if (abs(rightError) <= 10)
            {
                rightVelo = 0;
            }
            else
            {
                // Calculate left side velocity using drive tuning values
                rightVelo = /*Calculate P*/ (driveKp * rightError) + 
                        /*Calculate I*/ (driveKi * rightError * 
                        /*Multiply by I after loop buffer otherwise by 0 */(max((cTime * loopBuffer) - driveIDelay, 0.0))) +
                        /*Calculate D*/(driveKd * rightError / cTime);
            }
            // Multiply velocities by their multiplier
            // Set velocities between their minimum and maximum values
            leftVelo = min(max(leftVelo * multiplier, minSpeed), maxSpeed);
            rightVelo = min(max(rightVelo * multiplier, minSpeed), maxSpeed);
            // Spin at velocity leftVelo and rightVelo
            driveLeftForward(leftVelo, volt);
            driveRightForward(rightVelo, volt);
            cTime++;
            this_thread::sleep_for(loopBuffer);
        }
        pidEnd();
    }

    // This function turns the bot left using a PID incorporating the inertial
    // sensor. PID velocity is multiplied by multiplier
    void turn(double turnTarget)
    {
        // Get current net Inertial rotation and add the target turning amount
        double target = odom.getH() + turnTarget;

        // This is calculated in this order to show how error will be derived during the program
        double error = target - odom.getH();

        // Continue PID loop until all exit conditions are satisfied
        while ( (abs(error) > 1 || ((cTime * loopBuffer) < minTime)) && ((cTime * loopBuffer) < maxTime) )
        {
            error = target - odom.getH();

            // If all exit condidtions are met set the velocity to 0
            if (abs(error) < 1)
            {
                leftVelo = 0;
                rightVelo = 0;
            }
            else
            {
                // Calculate velocity using turn tuning values
                leftVelo = /*Calculate P*/ (turnKp * error) + 
                        /*Calculate I*/ (turnKi * error * 
                        /*Multiply by I after loop buffer otherwise by 0 */(max((cTime * loopBuffer) - turnIDelay, 0.0))) +
                        /*Calculate D*/(turnKd * error / cTime);
                rightVelo = leftVelo;
            }
            
            // Multiply velocities by their multiplier
            // Set velocities between their minimum and maximum values
            leftVelo = min(max(leftVelo * multiplier, minSpeed), maxSpeed);
            rightVelo = min(max(rightVelo * multiplier, minSpeed), maxSpeed);

            // Spin at velocity leftVelo and rightVelo (turning right is positive)
            driveLeftForward(leftVelo, volt);
            driveRightBackward(rightVelo, volt);
            cTime++;
            this_thread::sleep_for(loopBuffer);
        }
        pidEnd();
    }

    // Drives to a certain point on the field using Odometry
    void goTo(double endingX, double endingY)
    {
        // Get the current position and rotation of the robot:
        double startingX = odom.getX();
        double startingY = odom.getY();
        double startingH = odom.getH(true);

        // Implement atan to calculate the heading that the robot needs to turn to
        // face the end point.
        double turnAngle = atan((endingX - startingX) / (endingY - startingY)) * radianToDegreeConverter;
        if(endingY - startingY < 0)
        {
            turnAngle += 180.0;
        }
        turnAngle -= startingH;

        // Optimize turn to take the shortest turn
        while(turnAngle > 180.0)
        {
            turnAngle -= 360.0;
        }
        while(turnAngle < -180.0)
        {
            turnAngle += 360.0;
        }

        turn(turnAngle); // Turn using the PID

        // Calculate the drive distance needed, then drive towards the target
        // position:
        double driveDistance = sqrt(pow((endingX - startingX), 2) + pow((endingY - startingY), 2));
        drive(driveDistance); // Drive forward using PID.
    }
};