#include "odometry.h"
#include "vex.h"
#include "robot_config.h"
#include "robot.h"

Odometry::Odometry()
{
    x = 0;
    y = 0;
    h = 0;
    deltaX = 0;
    deltaY = 0;
    deltaH = 0;
    totalLDist = 0;
    totalRDist = 0;
    deltaLDist = 0;
    deltaRDist = 0;
    deltaAvgDist = 0;
    currentInertialRotation = 0;
    Inertial.resetRotation();
}

double Odometry::getX()
{ return x; }

double Odometry::getY()
{ return y; }

double Odometry::getH(bool bounded)
{
    if(bounded)
    {
        return fmod(h, 360);
    }
    return h;
}

void Odometry::setPosition(double ax, double ay)
{
    x = ax;
    y = ay;
    currentInertialRotation = h;
    Inertial.setRotation(h, degrees);
}

void Odometry::setPosition(double ax, double ay, double ah)
{
    x = ax;
    y = ay;
    h = ah;
    currentInertialRotation = h;
    Inertial.setRotation(h, degrees);
}

void Odometry::resetHeading()
{
    h = 0;
    currentInertialRotation = 0;
    Inertial.resetHeading();
}

double Odometry::getLeftEncoder()
{ return LeftMiddleDrive.position(degrees); }

double Odometry::getRightEncoder()
{ return RightMiddleDrive.position(degrees); }

double Odometry::getInertialRotation()
{ return Inertial.rotation(degrees); }

// Update the change in distance of both wheels as well as average of both wheels
void Odometry::updateDeltaDist()
{
    // Store previous positions in temporary variable
    double leftPrev = totalLDist;
    double rightPrev = totalRDist;
    // Update current positions
    totalLDist = getLeftEncoder() * motorToWheelConverter * degreeToInchConverter;
    totalRDist = getRightEncoder() * motorToWheelConverter * degreeToInchConverter;
    // Calculate change in position
    deltaLDist = (totalLDist - leftPrev);
    deltaRDist = (totalRDist - rightPrev);
    // Calculate average change in position
    deltaAvgDist = ((deltaLDist + deltaRDist) / 2.0);
}

// Update the Heading of the robot using the inertial sensor
void Odometry::updateHeading()
{
    currentInertialRotation = getInertialRotation();
    deltaH = currentInertialRotation - h;
    h = currentInertialRotation;
}

// Set as a task during auton
// Always running in a loop
void Odometry::calculatePosition()
{
    // Calculate change in wheel positions
    updateDeltaDist();
    // Calculate overall heading and change in heading
    updateHeading();
    // Calculate the input for the cos and sin functions for the odometry equations
    double cos_sin_input = (h + (deltaH / 2.0) ) * degreeToRadianConverter;
    // Calculate the change in x and change in y
    deltaX = deltaAvgDist * cos(cos_sin_input);
    deltaY = deltaAvgDist * sin(cos_sin_input);
    // Add to previous x and y values
    x += deltaX;
    y += deltaY;
}

// Global variable to store odometry object
Odometry odom = Odometry();

// Global variable to store task instance
thread odometryTask;

int odomPrintWait = 0;
// a task started by usercontrol
void odometryFunction()
{
    while(true)
    {
        odom.calculatePosition();
        if (odomPrintWait >= 20)
        {
            printf("x:%f y:%f h:%f \n", odom.getX(), odom.getY(), odom.getH());
            odomPrintWait = 0;
        }
        odomPrintWait++;
        this_thread::sleep_for(10);
    }
}