#include "pid.h"
#include <string.h>
#include <string>
using namespace std::string;

std::string alliance = "Red";
std::string side = "Positive";
int variation = 1;
bool start = false;

void printScreen()
{
    Controller.Screen.print("Alliance: " + alliance);
    Controller.Screen.print("Side: " + side);
    Controller.Screen.print("Variation" + (std::string) variation);
}

// Selects the auton the robot will run during autonomous using the controller
void auton_selector()
{
    printScreen();
    while(!start)
    {
        if(Controller.ButtonA.pressing())
        {
            start = true;
        }
        else if(Controller.ButtonLeft.pressing() || Controller.ButtonRight.pressing())
        {
            if(alliance == "Red")
            {
                alliance == "Blue";
            }
            else
            {
                alliance = "Red";
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
        else if(Controller.ButtonX.pressing() || Controller.ButtonY.pressing())
        {
            if(side == "Positive")
            {
                side = "Negative";
            }
            else
            {
                side = "Positive";
            }
            printScreen();
            while(Controller.ButtonX.pressing() || Controller.ButtonY.pressing())
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