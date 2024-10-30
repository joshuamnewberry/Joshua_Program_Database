#include "vex.h"
#include "methods.cpp"
#include <algorithm>
#include <cmath>
#include <string>

using namespace vex;

competition Competition;

void pre_auton(void)
{
  Inertial.calibrate();       // Calibrate the inertial sensor.
  GPS.calibrate();            // Calibrate the GPS sensor.
  while(GPS.isCalibrating()) // whileit is calibrating wait.
  {
    wait(50, msec);
  }
  while(Inertial.isCalibrating())
  {
    wait(50, msec);
  }
}

void autonomous(void)
{
  side = 1;
  point = 2;
  if(side == 0)
  {
    if(point == 1) // Right Side Neutral Goal
    {
      FI.set(true);
      drivePID(45, 1);
      FI.set(false);
      wait(50, msec);
      LAM.rotateTo(0.37, rotationUnits::rev, false);
      RAM.rotateTo(0.37, rotationUnits::rev);
      drivePID(-40, 1);
    }
    else if(point == 2) // Right Side Neutral Goal and Win Point
    {
      FI.set(true);
      drivePID(45, 1);
      FI.set(false);
      wait(50, msec);
      LAM.rotateTo(0.37, rotationUnits::rev, false);
      RAM.rotateTo(0.37, rotationUnits::rev);
      drivePID(-26, 1);
      BI.set(true);
      turnPID(-86, 1);
      drivePID(-5, .85);
      BI.set(false);
      BAM.rotateTo(.76, rotationUnits::rev);
      RI.spin(directionType::rev, 35, percentUnits::pct);
      LAM.rotateTo(0.5, rotationUnits::rev, false);
      RAM.rotateTo(0.5, rotationUnits::rev);
      turnPID(90, .8);
      drivePID(10, .75);
      RI.stop();
      drivePID(-15, 1);
      BAM.rotateTo(0, rotationUnits::rev);
      BI.set(true);
      drivePID(1.5, 1);
    }
    else if(point == 3) // Right Side Neutral Goal, Middle Neutral Goal, and Win Point
    {
      tmr = vex::timer::system();
      FI.set(true);
      drivePID(45, 1);
      FI.set(false);
      wait(50, msec);
      LAM.rotateTo(0.37, rotationUnits::rev);
      drivePID(-25.5, 1);
      turnPID(-86, 1);
      drivePID(-2.5, .9);
      BAM.rotateTo(-.9, rotationUnits::rev);
      drivePID(10, 1);
      turnPID(8, 1.5);
      BAM.rotateTo(-1.81, rotationUnits::rev);
      drivePID(-14.5, 1);
      wait(50, msec);
      BAM.rotateTo(-1.41, rotationUnits::rev);
      drivePID(22, 1);
      if(vex::timer::system() - tmr < 10500)
      {
        LAM.rotateTo(0, rotationUnits::rev, false);
        RAM.rotateTo(0, rotationUnits::rev);
        FI.set(true);
        turnPID(30, 1.5);
        drivePID(36, 1);
        FI.set(false);
        wait(100, msec);
        LAM.rotateTo(0.37, rotationUnits::rev, false);
        RAM.rotateTo(0.37, rotationUnits::rev);
        drivePID(-48, 10);
        LAM.rotateTo(0.15, rotationUnits::rev, false);
        RAM.rotateTo(0.15, rotationUnits::rev);
      }
    }
  }
  if(side == 1)
  {
    if(point == 1) // Left Side Neutral Goal
    {
      FI.set(true);
      drivePID(48.5, 1);
      FI.set(false);
      wait(50, msec);
      LAM.rotateTo(.37, rotationUnits::rev, false);
      RAM.rotateTo(.37, rotationUnits::rev);
      drivePID(-48.5, 1);
    }
    else if(point == 2) // Left Side Neutral Goal and Win Point
    {
      FI.set(true);
      drivePID(48.5, 1);
      FI.set(false);
      wait(50, msec);
      LAM.rotateTo(.37, rotationUnits::rev, false);
      RAM.rotateTo(.37, rotationUnits::rev);
      drivePID(-31.5, 1);
      wait(100, msec);
      turnPID(-17.5, 2);
      drivePID(-7, .9);
      BAM.rotateTo(-.9, rotationUnits::rev);
      drivePID(5, .9);
      turnPID(92, 1.5);
      BAM.rotateTo(-.05, rotationUnits::rev);
    }
    else if(point == 3) // Left Side Neutral Goal, Middle Neutral Goal, and Win Point
    {
      FI.set(true);
      drivePID(48.5, 1);
      FI.set(false);
      wait(50, msec);
      LAM.rotateTo(.37, rotationUnits::rev, false);
      RAM.rotateTo(.37, rotationUnits::rev);
      drivePID(-31.5, 1);
      wait(100, msec);
      turnPID(-17.5, 2);
      drivePID(-7, .9);
      BAM.rotateTo(-.9, rotationUnits::rev);
      drivePID(5, .9);
      turnPID(93.5, 1.5);
      BAM.rotateTo(-.05, rotationUnits::rev);
      drivePID(18.5, 1);
      FI.set(true);
      LAM.rotateTo(0, rotationUnits::rev, false);
      RAM.rotateTo(0, rotationUnits::rev);
      drivePID(-1, 1);
      wait(125, msec);
      turnPID(-43, 1.6);
      drivePID(36, 1);
      FI.set(false);
      wait(100, msec);
      LAM.rotateTo(0.37, rotationUnits::rev, false);
      RAM.rotateTo(0.37, rotationUnits::rev);
      drivePID(-36.6, 1.1);
      LAM.rotateTo(0.15, rotationUnits::rev, false);
      RAM.rotateTo(0.15, rotationUnits::rev);
    }
    /*else if(point == 4) // Left Side Neutral Goal, Middle Neutral Goal with
    the Back, and Win Point
    {
      FI.set(true);
      drivePID(48.5, 1);
      FI.set(false);
      wait(50, msec);
      LAM.rotateTo(.37, rotationUnits::rev, false);
      RAM.rotateTo(.37, rotationUnits::rev);
      drivePID(-31.5, 1);
      wait(100, msec);
      turnPID(-20, 1);
      drivePID(-8, 1);
      BAM.rotateTo(-.9, rotationUnits::rev, false);
      RBAM.rotateTo(-.9, rotationUnits::rev);
      drivePID(10, .95);
      turnPID(-120, 1);
      BAM.rotateTo(-1.81, rotationUnits::rev, false);
      RBAM.rotateTo(-1.81, rotationUnits::rev);
      drivePID(-25, .85);
      wait(50, msec);
      BAM.rotateTo(-1.375, rotationUnits::rev, false);
      RBAM.rotateTo(-1.375, rotationUnits::rev);
      drivePID(30, 1);
    }*/
  }
  if(side == 2)
  {
    if(point == 1) // Skills
    {
      FI.set(true);
      drivePID(45, 1);
      FI.set(false);   // GRAB NEUTRAL GOAL
      wait(50, msec);
      LAM.rotateTo(0.37, rotationUnits::rev, false);
      RAM.rotateTo(0.37, rotationUnits::rev);
      drivePID(-25.5, 1);
      turnPID(-86, 1);  // TURN LEFT
      drivePID(7.5, .95);
      turnPID(10, 1);
      BAM.rotateTo(-1.81, rotationUnits::rev);
      drivePID(-14, .9); // BACK UP
      wait(50, msec);
      BAM.rotateTo(-1.41, rotationUnits::rev);
      //GRAB ALLIANCE GOAL
      // END OF 2 POINT 15 SEC
      drivePID(50, .6); // CLEAR RINGS
      drivePID(-6.5, .65);
      LAM.rotateTo(1.55, rotationUnits::rev, false);
      RAM.rotateTo(1.55, rotationUnits::rev);
      turnPID(-87, 1); // TURN LEFT TO FACE PLATFORM
      drivePID(15.75, 1);
      wait(50, msec);
      LAM.rotateTo(1, rotationUnits::rev, 100, velocityUnits::pct, false);
      RAM.rotateTo(1, rotationUnits::rev, 100, velocityUnits::pct);
      wait(100, msec);
      FI.set(true); // SET DOWN NEUTRAL MOBILE GOAL
      drivePID(-.7, 1);
      LAM.rotateTo(1.3, rotationUnits::rev, false);
      RAM.rotateTo(1.3, rotationUnits::rev);
      wait(100, msec);
      drivePID(-10, .95);
      wait(50, msec);
      LAM.rotateTo(0, rotationUnits::rev, false);
      RAM.rotateTo(0, rotationUnits::rev);
      wait(50, msec);
      turnPID(-90, .85); // TURN TO FACE THE MIDDLE MOBILE GOAL
      drivePID(-4, 1);
      turnPID(-96, .85); // TURN TO FACE THE MIDDLE MOBILE GOAL
      drivePID(25, .65);
      FI.set(false); // GRAB MIDDLE MOBILE GOAL
      wait(50, msec);
      LAM.rotateTo(0.35, rotationUnits::rev, false);
      RAM.rotateTo(0.35, rotationUnits::rev);
      drivePID(22, 1);
      LAM.rotateTo(0.15, rotationUnits::rev, false);
      RAM.rotateTo(0.15, rotationUnits::rev);
      turnPID(90, 1); //TURN RIGHT
      drivePID(6, 1);
      FI.set(true); // SET DOWN MIDDLE MOBILE GOAL
      wait(100, msec);
      LAM.rotateTo(0, rotationUnits::rev);
      wait(50, msec);
      drivePID(-4, .95);
      turnPID(180, .9); // TURN AROUND TO SET DOWN ALLIANCE GOAL
      BAM.rotateTo(-1.81, rotationUnits::rev);// SET DOWN ALLIANCE GOAL
      drivePID(12, 1);
      turnPID(-178, .9); // TURN AROUND TO GRAB ALLIANCE GOAL
      BAM.rotateTo(0, rotationUnits::rev);
      drivePID(12, .8);
      wait(50, msec);
      FI.set(false); // GRAB ALLIANCE GOAL
      wait(50, msec);
      LAM.rotateTo(.37, rotationUnits::rev, false);
      RAM.rotateTo(.37, rotationUnits::rev);
      drivePID(-8.4, 1);
      turnPID(-92, .9); // TURN TO FACE RAMP
      LAM.rotateTo(1.3, rotationUnits::rev, false);
      RAM.rotateTo(1.3, rotationUnits::rev);
      drivePID(16, .95); //DRIVE TO RAMP
      LAM.rotateTo(1, rotationUnits::rev, false);
      RAM.rotateTo(1, rotationUnits::rev);
      wait(50, msec);
      FI.set(true); // SET DOWN ALLIANCE GOAL
      wait(50, msec);
      LAM.rotateTo(1.3, rotationUnits::rev, false);
      RAM.rotateTo(1.3, rotationUnits::rev);
      drivePID(-10, 1);
      wait(50, msec);
      LAM.rotateTo(0, rotationUnits::rev, false);
      RAM.rotateTo(0, rotationUnits::rev);
      wait(50, msec);
      drivePID(3, .9);
      turnPID(-85, .9); // TURN LEFT TOWARD ALLIANCE GOAL
      drivePID(46, .9);
      wait(500, msec);
      FI.set(false); // GRAB RED GOAL
      wait(250, msec);
      drivePID(-6, 1);
      LAM.rotateTo(.37, rotationUnits::rev, false);
      RAM.rotateTo(.37, rotationUnits::rev);
      drivePID(-5.75, 1);
      turnPID(-89.5, .85); // TURN TO OTHER SIDE OF FIELD
      drivePID(65, .9);
    }
  }
}