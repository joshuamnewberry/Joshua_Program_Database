#include "vex.h"

// Define Brain
extern brain Brain;

// Define Controller
extern controller Controller = controller(primary);

// Define Left Drive Motors
extern motor LeftFrontDrive = motor(PORT1, ratio6_1, false);
extern motor LeftMiddleDrive = motor(PORT1, ratio6_1, false);
extern motor LeftBackDrive = motor(PORT1, ratio6_1, false);
extern motor LeftTopDrive = motor(PORT1, ratio6_1, false);
motor_group LeftDriveGroup = motor_group(LeftFrontDrive, LeftMiddleDrive, LeftBackDrive, LeftTopDrive);

// Define Right Drive Motors
extern motor RightFrontDrive = motor(PORT1, ratio6_1, true);
extern motor RightMiddleDrive = motor(PORT1, ratio6_1, true);
extern motor RightBackDrive = motor(PORT1, ratio6_1, true);
extern motor RightTopDrive = motor(PORT1, ratio6_1, true);
motor_group RightDriveGroup = motor_group(RightFrontDrive, RightMiddleDrive, RightBackDrive, RightTopDrive);

// Define Sensors
extern inertial Inertial = inertial(PORT1);
extern distance Distance = distance(PORT1);

// Create variable for field control
bool RemoteControlCodeEnabled = true;

// Define Wheel size of the robot in inches (Used for PID and Odometry functions)
double wheel_diameter = 2.75;
double wheel_circ = wheel_diameter * M_PI;
// Define Wheel Distance from center of robot ()
double dist_from_center = 2.5;
// Define Unit Converters
double inchToDegreeConverter = 360 / wheel_circ;
double degreeToInchConverter = wheel_circ / 360;
double radianToDegreeConverter = 180.0 / M_PI;
double degreeToRadianConverter = M_PI / 180.0;

// Create Joystick Value variables (Used for Tank Drive and Arcade drive)
double axis1 = Controller.Axis1.value(percent);
double axis2 = Controller.Axis2.value(percent);
double axis3 = Controller.Axis3.value(percent);
double axis4 = Controller.Axis4.value(percent);

// Create Arcade Drive variables
double forwardVolt = 0;
double turnVolt = 0;