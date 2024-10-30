#include "vex.h"
#include <algorithm>
#include <cmath>
#include <string>

using namespace vex;

// Tuning values:
const double driveKp = 0.275;
const double driveKi = 0.01;
const double driveKd = 0.02;
const double driveKv = 0;

// Tuning values:
const double turnKp = 0.31;
const double turnKi = 0.015;
const double turnKd = 0.02;

int side = 0;
int point = 2;
int start = 0;
bool skills = false;
int menuPause = 0;
int menu = 0;
int rln = 0;
int debug = 1;
double val = 0;
int brX;
int brY;

int frontWaiting = 0;
int backWaiting = 0;
int ringWaiting = 0;
bool ringActive = false;
int rampWaiting = 0;
bool backArmStop = true;
bool ramp = false;
double platVelo;
int platWaiting;
int platCount = 0;
vex::directionType LF;
vex::directionType RF;
vex::directionType LB;
vex::directionType RB;

uint32_t tmr = vex::timer::system();

int prevX = 0;
int prevY = 0;
std::string prevPicture = "";
std::string changeOldString = "NS";