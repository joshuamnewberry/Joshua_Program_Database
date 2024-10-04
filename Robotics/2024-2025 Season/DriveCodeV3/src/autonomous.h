#include "auton_selector.h"

void pre_auton(void)
{
    // Calibrate the inertial sensor
    Inertial.calibrate(2);
    // Wait to finish calibrating
    while(Inertial.isCalibrating())
    { this_thread::sleep_for(10); }
    odom = Odometry();
}

void autonomous(void)
{
    // Variables for testing to skip Auton menu
    alliance = "Red";
    side = "Positive";
    variation = 1;
    start = true;
    odometryTask = thread(odometryFunction);

    if(alliance == "Red") // Red Side Autons
    {
        if(side == "Positive")
        {
            if(variation == 1) // 
            {
                drive(10);
                turn(90);
                drive(10);
                drive(-10);
                turn(-90);
                turn(180);
                drive(10);
                turn(270);
                drive(25);
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
    if(alliance == "Red") // Red Side Autons
    {
        if(side == "Positive")
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
    else if(alliance == "Skills") // Skills
    {
        if(variation == 1) // 
        {
            
        }
        else if(variation == 2) // 
        {
            
        }
    }
}