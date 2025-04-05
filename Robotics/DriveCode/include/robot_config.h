#pragma once
#include "vex.h"

// Define Brain
extern brain Brain;

// Define Controller
extern controller Controller;

// Define Left Drive Motors
extern motor LeftFrontDrive;
extern motor LeftMiddleDrive;
extern motor LeftBackDrive;
extern motor LeftTopDrive;
extern motor_group LeftDriveGroup;

// Define Right Drive Motors
extern motor RightFrontDrive;
extern motor RightMiddleDrive;
extern motor RightBackDrive;
extern motor RightTopDrive;
extern motor_group RightDriveGroup;

// Define Sensors
extern inertial Inertial;
//////extern distance Distance;

// Create variable for field control
extern bool RemoteControlCodeEnabled;

// Define Wheel size of the robot in inches (Used for PID and Odometry functions)
extern double wheel_diameter;
extern double wheel_circ;
// Define Wheel Distance from center of robot
extern double dist_from_center;
// Define Unit Converters
extern double inchToDegreeConverter;
extern double degreeToInchConverter;
extern double radianToDegreeConverter;
extern double degreeToRadianConverter;
extern double motorToWheelConverter;
extern double wheelToMotorConverter;

// Create Tank/Arcade drive boolean variable
extern bool tankDrive;

// Create Joystick Value variables (Used for Tank Drive and Arcade drive)
extern double axis1;
extern double axis2;
extern double axis3;
extern double axis4;

// Create Arcade Drive variables
extern double forwardVolt;
extern double turnVolt;