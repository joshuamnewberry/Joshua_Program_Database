#pragma once
#include "methods.h"


class Odometry
{
    // Odometry variables:
    //const int ticks_per_rotation = 3600;
    static constexpr double dist_from_center = 2.5;
    static constexpr double wheel_circ = 2.75 * M_PI;
    double x = 0;
    double y = 0;
    double h = 0;
    double startH = 0;
    double deltaX = 0;
    double deltaY = 0;
    double deltaH = 0;
    double totalLDist = 0;
    double totalRDist = 0;
    double deltaL = 0;
    double deltaR = 0;
    double LDW_prev = 0;
    double RDW_prev = 0;

    public: Odometry()
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
        deltaL = 0;
        deltaR = 0;
        LDW_prev = 0;
        RDW_prev = 0;
        LDW.resetPosition();
        RDW.resetPosition();
    }

    public: double getX()
    { return x; }

    public: double getY()
    { return y; }

    public: double getH()
    { return h; }

    public: void setPosition(double ax, double ay, double ah)
    {
        x = ax;
        y = ay;
        h = ah;
        startH = h;
        LDW.resetPosition();
        RDW.resetPosition();
    }

    public: void resetHeading()
    {
        h = 0;
        startH = h;
        LDW.resetPosition();
        RDW.resetPosition();
    }

    double getLeftEncoder()
    { return LDW.position(degrees); }

    double getRightEncoder()
    { return RDW.position(degrees); }

    double updateDeltaL()
    {
        // Store previous in temporary variable
        double prev = LDW_prev;
        // Update global previous variable
        LDW_prev = getLeftEncoder();
        // New value - Old value equals change
        return (deltaL = (LDW_prev - prev) / wheel_circ);
    }

    double updateDeltaR()
    {
        // Store previous in temporary variable
        double prev = LDW_prev;
        // Update global previous variable
        RDW_prev = getRightEncoder();
        // New value - Old value equals change
        return (deltaR = (RDW_prev - prev) / wheel_circ);
    }

    // Set as a task during auton
    // Always running in a loop
    public: void calculatePosition()
    {
        // Calculate change in left and right wheel
        updateDeltaL();
        updateDeltaR();
        // Update total distance
        totalLDist = getLeftEncoder();
        totalRDist = getRightEncoder();
        // Store new heading in temporary variable and convert to degrees
        double newH = startH + ((totalLDist - totalRDist) / (2 * dist_from_center)) * 1.0 / 57.2958;
        // Calculate change in heading
        deltaH = newH - h;
        // Update heading
        h = newH;
    }
};

Odometry odom = Odometry();
