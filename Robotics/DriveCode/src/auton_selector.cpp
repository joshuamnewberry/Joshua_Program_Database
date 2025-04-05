#include "auton_selector.h"
#include "vex.h"
#include "robot_config.h"

string alliance = "R";
string side = "P";
int variation = 1;
bool start = false;

void printScreen()
{
    Controller.Screen.setCursor(10, 0);
    Controller.Screen.print("CLR:%s SIDE:%s VSION:%d   ", alliance.c_str(), side.c_str(), variation);
}

void printEndScreen()
{
    Controller.Screen.setCursor(10, 0);
    Controller.Screen.print("C:%s, S:%s, V:%d, START     ", alliance.c_str(), side.c_str(), variation);
}

// Selects the auton the robot will run during autonomous using the controller
void auton_selector()
{
    printScreen();
    while(!start)
    {
        if(Controller.ButtonA.pressing())
        {
            printEndScreen();
            start = true;
        }
        else if(Controller.ButtonLeft.pressing() || Controller.ButtonRight.pressing())
        {
            if(alliance == "R")
            {
                alliance = "B";
            }
            else
            {
                alliance = "R";
            }
            printScreen();
            while(Controller.ButtonLeft.pressing() || Controller.ButtonRight.pressing())
            {
                this_thread::sleep_for(10);
            }
        }
        else if(Controller.ButtonUp.pressing())
        {
            variation++;
            if(variation > 3)
            {
                variation = 1;
            }
            printScreen();
            while(Controller.ButtonUp.pressing())
            {
                this_thread::sleep_for(10);
            }
        }
        else if(Controller.ButtonDown.pressing())
        {
            variation--;
            if(variation < 1)
            {
                variation = 3;
            }
            printScreen();
            while(Controller.ButtonDown.pressing())
            {
                this_thread::sleep_for(10);
            }
        }
        else if(Controller.ButtonX.pressing())
        {
            if(side == "P")
            {
                side = "N";
            }
            else
            {
                side = "P";
            }
            printScreen();
            while(Controller.ButtonX.pressing())
            {
                this_thread::sleep_for(10);
            }
        }
        else if(Controller.ButtonY.pressing())
        {
            tankDrive == !tankDrive;
            if(tankDrive)
            {
                Controller.rumble("...");
            }
            else
            {
                Controller.rumble("--");
            }
            while(Controller.ButtonY.pressing())
            {
                this_thread::sleep_for(10);
            }
        }
        this_thread::sleep_for(10);
    }

    // Wait for release of Button A that exits the auton selector to continue
    while(Controller.ButtonA.pressing())
    {
        this_thread::sleep_for(10);
    }
}