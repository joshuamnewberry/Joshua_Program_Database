#include "robot_config.h"
#include "vex.h"

// Define Brain
brain Brain = brain();

// Define Controller
controller Controller = controller(primary);

// Define Left Drive Motors
//motor LeftFrontDrive = motor(PORT11, ratio6_1, true);
motor LeftMiddleDrive = motor(PORT15, ratio6_1, true);
motor LeftBackDrive = motor(PORT14, ratio6_1, true);
motor LeftTopDrive = motor(PORT16, ratio6_1, false);
motor_group LeftDriveGroup = motor_group(LeftMiddleDrive, LeftBackDrive, LeftTopDrive);

// Define Right Drive Motors
motor RightFrontDrive = motor(PORT1, ratio6_1, false);
motor RightMiddleDrive = motor(PORT2, ratio6_1, false);
motor RightBackDrive = motor(PORT3, ratio6_1, false);
motor RightTopDrive = motor(PORT4, ratio6_1, true);
motor_group RightDriveGroup = motor_group(RightFrontDrive, RightMiddleDrive, RightBackDrive, RightTopDrive);

// Define Sensors
inertial Inertial = inertial(PORT21);
////distance Distance = distance(PORT1);

// Create variable for field control
bool RemoteControlCodeEnabled = true;

// Define Wheel size of the robot in inches (Used for PID and Odometry functions)
double wheel_diameter = 2.75;
double wheel_circ = wheel_diameter * M_PI;
// Define Wheel Distance from center of robot
double dist_from_center = 10.5;
// Define Unit Converters
double inchToDegreeConverter = 360.0 / wheel_circ;
double degreeToInchConverter = wheel_circ / 360.0;
double radianToDegreeConverter = 180.0 / M_PI;
double degreeToRadianConverter = M_PI / 180.0;
double motorToWheelConverter = 360.0 / 600.0;
double wheelToMotorConverter = 600.0 / 360.0;

// Create Tank/Arcade drive boolean variable
bool tankDrive = true;

// Create Joystick Value variables (Used for Tank Drive and Arcade drive)
double axis1 = Controller.Axis1.position(percent);
double axis2 = Controller.Axis2.position(percent);
double axis3 = Controller.Axis3.position(percent);
double axis4 = Controller.Axis4.position(percent);

// Create Arcade Drive variables
double forwardVolt = 0;
double turnVolt = 0;