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
            LeftMiddleDrive.resetPosition();
            RightMiddleDrive.resetPosition();
        }
    
    public:

        double getX()
        { return x; }

        double getY()
        { return y; }

        double getH()
        { return h; }

        void setPosition(double ax, double ay, double ah)
        {
            x = ax;
            y = ay;
            h = ah;
            startH = h;
            currentLMDPosition = 0;
            currentRMDPosition = 0;
            LeftMiddleDrive.resetPosition();
            RightMiddleDrive.resetPosition();
        }

        void resetHeading()
        {
            h = 0;
            startH = 0;
            currentLMDPosition = 0;
            currentRMDPosition = 0;
            LeftMiddleDrive.resetPosition();
            RightMiddleDrive.resetPosition();
        }

        double getLeftEncoder()
        { return LeftMiddleDrive.position(degrees); }

        double getRightEncoder()
        { return RightMiddleDrive.position(degrees); }

    private:

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
            deltaAvgDist = (deltaLDist + deltaRDist) / 2.0;
        }

        double updateHeading()
        {
            h = startH + ((totalLDist - totalRDist) / dist_from_center) * radianToDegreeConverter;
            deltaH = ((deltaLDist - deltaRDist) / dist_from_center) * radianToDegreeConverter;
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
            double cos_sin_input = degreeToRadianConverter * (h + (deltaH / 2.0) );
            deltaX = deltaAvgDist * cos(cos_sin_input);
            deltaY = deltaAvgDist * sin(cos_sin_input);
            x += deltaX;
            y += deltaY;
        }
};

Odometry odom = Odometry();