#pragma once
#include "vex.h"
using namespace std;

extern string alliance;
extern string side;
extern int variation;
extern bool start;

void printScreen();

void printEndScreen();

// Selects the auton the robot will run during autonomous using the controller
void auton_selector();