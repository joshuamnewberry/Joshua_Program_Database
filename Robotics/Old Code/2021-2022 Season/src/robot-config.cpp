#include "vex.h"

using namespace vex;
using signature = vision::signature;
using code = vision::code;

// A global instance of brain used for printing to the V5 Brain screen
brain  Brain;

// VEXcode device constructors
motor LFDM = motor(PORT1, ratio18_1, false);
motor LBDM = motor(PORT11, ratio18_1, false);
motor RFDM = motor(PORT10, ratio18_1, true);
motor RBDM = motor(PORT20, ratio18_1, true);
inertial Inertial = inertial(PORT21);
motor LAM = motor(PORT4, ratio36_1, false);
motor RAM = motor(PORT9, ratio36_1, true);
gps GPS = gps(PORT3, -247.65, -25.40, mm, 180);
controller Controller1 = controller(primary);
digital_out FI = digital_out(Brain.ThreeWirePort.A);
motor BAM = motor(PORT19, ratio36_1, true);
motor RI = motor(PORT12, ratio18_1, false);
digital_out BI = digital_out(Brain.ThreeWirePort.B);

// VEXcode generated functions
// define variable for remote controller enable/disable
bool RemoteControlCodeEnabled = true;

/**
 * Used to initialize code/tasks/devices added using tools in VEXcode Pro.
 * 
 * This should be called at the start of your int main function.
 */
void vexcodeInit( void ) {
  // nothing to initialize
}