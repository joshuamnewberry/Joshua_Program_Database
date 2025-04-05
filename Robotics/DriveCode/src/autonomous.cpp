#include "autonomous.h"
#include "vex.h"
#include "robot_config.h"
#include "robot.h"
#include "odometry.h"
#include "pid.h"
#include "auton_selector.h"
using namespace Drive;
using namespace PID;

void pre_auton(void)
{
    // Calibrate the inertial sensor
    Inertial.calibrate(.25);
    // Wait to finish calibrating
    while(Inertial.isCalibrating())
    { this_thread::sleep_for(10); }
}

void autonomous(void)
{
    // Start the odometry thread
    odometryTask = thread(odometryFunction);

    // Variables for testing to skip Auton menu
    alliance = "R";
    side = "P";
    variation = 1;

    if(alliance == "R") // Red Side Autons
    {
        if(side == "P")
        {
            if(variation == 1) // 
            {
                turn(90);
                drive(24);
                drive(-24);
                turn(-90);
                turn(180);
                drive(24);
                turn(270);
                drive(48);
                turn(-360);
            }
            else if(variation == 2) // 
            {
                goTo(10, 10);
                goTo(0, 0);
            }
            else if(variation == 3) // 
            {
                
            }
        }
        else
        {
            if(variation == 1) // 
            {
                
            }
            else if(variation == 2) // 
            {
                
            }
            else if(variation == 3) // 
            {
                
            }
        }
    }
    if(alliance == "B") // Blue Side Autons
    {
        if(side == "N")
        {
            if(variation == 1) // 
            {

            }
            else if(variation == 2) // 
            {
                
            }
            else if(variation == 3) // 
            {
                
            }
        }
        else
        {
            if(variation == 1) // 
            {

            }
            else if(variation == 2) // 
            {
                
            }
            else if(variation == 3) // 
            {
                
            }
        }
    }
    else if(alliance == "S") // Skills
    {
        if(variation == 1) // 
        {
            
        }
        else if(variation == 2) // 
        {
            
        }
    }
}