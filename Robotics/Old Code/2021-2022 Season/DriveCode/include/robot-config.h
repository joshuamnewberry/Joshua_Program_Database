using namespace vex;

extern brain Brain;

// VEXcode devices
extern motor LFDM;
extern motor LBDM;
extern motor RFDM;
extern motor RBDM;
extern inertial Inertial;
extern motor LAM;
extern motor RAM;
extern gps GPS;
extern controller Controller1;
extern digital_out FI;
extern motor BAM;
extern motor RI;
extern digital_out BI;

/**
 * Used to initialize code/tasks/devices added using tools in VEXcode Pro.
 * 
 * This should be called at the start of your int main function.
 */
void  vexcodeInit( void );