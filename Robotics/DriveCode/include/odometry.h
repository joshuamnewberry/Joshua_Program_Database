#pragma once
#include "vex.h"

class Odometry
{
    private:
    
        // Odometry variables:
        //const int ticks_per_rotation = 3600;
        double x;
        double y;
        double h;
        double deltaX;
        double deltaY;
        double deltaH;
        double totalLDist;
        double totalRDist;
        double deltaLDist;
        double deltaRDist;
        double deltaAvgDist;
        double currentInertialRotation;
    
    public:

        Odometry();

        double getX();

        double getY();

        double getH(bool bounded = false);

        void setPosition(double ax, double ay);

        void setPosition(double ax, double ay, double ah);

        void resetHeading();

        double getLeftEncoder();

        double getRightEncoder();

        double getInertialRotation();

    private:

        // Update the change in distance of both wheels as well as average of both wheels
        void updateDeltaDist();

        // Update the Heading of the robot by averaging the inertial sensor and two wheel odometry values
        void updateHeading();

    public:

        // Set as a task during auton
        // Always running in a loop
        void calculatePosition();
};

// Global variable to store odometry object
extern Odometry odom;

// Global variable to store task instance
extern thread odometryTask;

extern int odomPrintWait;
// a task started by usercontrol
void odometryFunction();