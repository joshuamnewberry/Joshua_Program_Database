#pragma once
#include "vex.h"

// Menu variables:
int side = 0;
int point = 2;
int start = 0;
bool skills = false;
int menuPause = 0;
int menu = 0;
int rln = 0;
int debug = 1;
double val = 0;
int brX = 0;
int brY = 0;


// Autonomous variables:
int shotCount = 0;
int shotWait = 0;
bool odomEnabled = false;


// User control variables:
int printWaiting = 0;
int cataWaiting = 0;
double leftDriveVelocity = 0;
double rightDriveVelocity = 0;
bool blockerOpen = false;
bool nineBar = false;


// Timer variable:
uint32_t tmr = vex::timer::system();


// Picture variables:
int prevX = 0;
int prevY = 0;
std::string prevPicture = "";
std::string changeOldString = "NS";


// Auton variables:
vex::directionType LW;
vex::directionType RW;
