#include "robot.h"

class Odometry
{
    private:
        // Odometry variables:
        //const int ticks_per_rotation = 3600;
        double x;
        double y;
        double h;
        double startH;
        double deltaX;
        double deltaY;
        double deltaH;
        double totalLDist;
        double totalRDist;
        double deltaLDist;
        double deltaRDist;
        double deltaAvgDist;
        double currentLMDPosition;
        double currentRMDPosition;
        double currentInertialRotation;

        void Odometry()
        {
            x = 0;
            y = 0;
            h = 0;
            startH = 0;
            deltaX = 0;
            deltaY = 0;
            deltaH = 0;
            totalLDist = 0;
            totalRDist = 0;
            deltaLDist = 0;
            deltaRDist = 0;
            deltaAvgDist = 0;
            currentLMDPosition = 0;
            currentRMDPosition = 0;
            currentInertialRotation = 0;
            LeftMiddleDrive.resetPosition();
            RightMiddleDrive.resetPosition();
            Inertial.resetRotation();
        }
    
    public:

        double getX()
        { return x; }

        double getY()
        { return y; }

        double getH()
        { return h; }

        void setPosition(double ax, double ay)
        {
            x = ax;
            y = ay;
            startH = h;
            currentLMDPosition = 0;
            currentRMDPosition = 0;
            currentInertialRotation = h;
            LeftMiddleDrive.resetPosition();
            RightMiddleDrive.resetPosition();
            Inertial.setRotation(h);
        }

        void setPosition(double ax, double ay, double ah)
        {
            x = ax;
            y = ay;
            h = ah;
            startH = h;
            currentLMDPosition = 0;
            currentRMDPosition = 0;
            currentInertialRotation = h;
            LeftMiddleDrive.resetPosition();
            RightMiddleDrive.resetPosition();
            Inertial.setRotation(h);
        }

        void resetHeading()
        {
            h = 0;
            startH = 0;
            currentLMDPosition = 0;
            currentRMDPosition = 0;
            currentInertialRotation = 0;
            LeftMiddleDrive.resetPosition();
            RightMiddleDrive.resetPosition();
            Inertial.resetHeading();
        }

        double getLeftEncoder()
        { return LeftMiddleDrive.position(degrees); }

        double getRightEncoder()
        { return RightMiddleDrive.position(degrees); }

        double getInertialRotation()
        { return Inertial.rotation(degrees); }

    private:

        // Update the change in distance of both wheels as well as average of both wheels
        void updateDeltaDist()
        {
            // Store previous positions in temporary variable
            double leftPrev = currentLMDPosition;
            double rightPrev = currentRMDPosition;
            // Update global previous variable
            currentLMDPosition = getLeftEncoder();
            currentRMDPosition = getRightEncoder();
            // Update total distance
            totalLDist = currentLMDPosition * degreeToInchConverter;
            totalRDist = currentRMDPosition * degreeToInchConverter;
            // Current value - Previous value equals change
            deltaLDist = (currentLMDPosition - leftPrev) * degreeToInchConverter;
            deltaRDist = (currentRMDPosition - rightPrev) * degreeToInchConverter;
            deltaAvgDist = ((deltaLDist + deltaRDist) / 2.0) * degreeToInchConverter;
        }

        // Update the Heading of the robot by averaging the inertial sensor and two wheel odometry values
        double updateHeading()
        {
            double rotationPrev = currentInertialRotation;
            currentInertialRotation = Inertial.heading();
            h = ( (startH + ((totalLDist - totalRDist) / dist_from_center) * radianToDegreeConverter) + currentInertialRotation) / 2.0;
            deltaH = ( ( ((deltaLDist - deltaRDist) / dist_from_center) * radianToDegreeConverter) + (currentInertialRotation - rotationPrev) ) / 2.0;
        }

    public:

        // Set as a task during auton
        // Always running in a loop
        void calculatePosition()
        {
            // Calculate change in wheel positions
            updateDeltaDist();
            // Calculate overall heading and change in heading
            updateHeading();
            // Calculate the input for the cos and sin functions for the odometry equations
            double cos_sin_input = degreeToRadianConverter * (h + (deltaH / 2.0) );
            // Calculate the Change in x and change in y
            deltaX = deltaAvgDist * cos(cos_sin_input);
            deltaY = deltaAvgDist * sin(cos_sin_input);
            // Add to previous x and y values
            x += deltaX;
            y += deltaY;
        }
};

Odometry odom = Odometry();

// global variable to store task instance
thread odometryTask;

// a task started by usercontrol
void odometryFunction()
{
    while(true)
    {
        odom.calculatePosition();
        this_thread::sleep_for(10);
    }
}
