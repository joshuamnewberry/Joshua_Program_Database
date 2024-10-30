// ---- START VEXCODE CONFIGURED DEVICES ----
// Robot Configuration:
// [Name]               [Type]        [Port(s)]
// LFDM                 motor         1               
// LBDM                 motor         11              
// RFDM                 motor         10              
// RBDM                 motor         20              
// Inertial             inertial      21              
// LAM                  motor         4               
// RAM                  motor         9               
// GPS                  gps           3               
// Controller1          controller                    
// FI                   digital_out   A               
// BAM                  motor         19              
// RI                   motor         12              
// BI                   digital_out   B               
// ---- END VEXCODE CONFIGURED DEVICES ----
#include "vex.h"
#include "autonomous.cpp"
#include <algorithm>
#include <cmath>
#include <string>

/*----------------------------------------------------------------------------*/
/*                              User Control Task                             */
/*----------------------------------------------------------------------------*/
void usercontrol(void)
{
  if(menu == 3)
  {
    if(point == 1)
    {
      Controller1.rumble("---");
      wait(500, msec);
      drivePID(val * 10.75 / 12.0, .75);
      wait(500, msec);
    }
    else if(point == 2)
    {
      Controller1.rumble("---");
      wait(500, msec);
      turnPID(val, 1);
      wait(500, msec);
    }
    else if(point == 3)
    {
      Controller1.rumble("---");
      wait(500, msec);
      goToTan(0, 0, 1, 1);
      wait(500, msec);
    }
  }
  if(skills == true)
  {
    FI.set(true);
    wait(200, msec);
    drivePID(6, 1.4);
    FI.set(false);
    wait(50, msec);
    LAM.rotateTo(.37, rotationUnits::rev, false);
    RAM.rotateTo(.37, rotationUnits::rev);
    drivePID(-4, 1.4);
    turnPID(-60, 1.4);
  }
  // User Control code here, inside the loop
  while(1)
  {
    // drive
    if(ramp)
    {
      LFDM.spin(directionType::fwd, Controller1.Axis3.position() / 2, velocityUnits::pct);
      RFDM.spin(directionType::fwd, Controller1.Axis2.position() / 2, velocityUnits::pct);
      LBDM.spin(directionType::fwd, Controller1.Axis3.position() / 2, velocityUnits::pct);
      RBDM.spin(directionType::fwd, Controller1.Axis2.position() / 2, velocityUnits::pct);
    }
    else
    {
      LFDM.spin(directionType::fwd, Controller1.Axis3.position(), velocityUnits::pct);
      RFDM.spin(directionType::fwd, Controller1.Axis2.position(), velocityUnits::pct);
      LBDM.spin(directionType::fwd, Controller1.Axis3.position(), velocityUnits::pct);
      RBDM.spin(directionType::fwd, Controller1.Axis2.position(), velocityUnits::pct);
    }

    // Moves 4Bar
    if(Controller1.ButtonL1.pressing() && (LAM.isDone() && RAM.isDone()))
    {
      LAM.spin(directionType::fwd, 100, velocityUnits::pct);
      RAM.spin(directionType::fwd, 100, velocityUnits::pct);
    }
    else if(Controller1.ButtonL2.pressing() && (LAM.isDone() && RAM.isDone()))
    {
      LAM.spin(directionType::rev, 100, velocityUnits::pct);
      RAM.spin(directionType::rev, 100, velocityUnits::pct);
    }
    else if(LAM.isDone() && RAM.isDone())
    {
      LAM.stop();
      RAM.stop();
    }

    // Moves Back Arm
    if(Controller1.ButtonR1.pressing() && (BAM.isDone()))
    {
      BAM.spin(directionType::fwd, 100, velocityUnits::pct);
    }
    else if(Controller1.ButtonR2.pressing() && (BAM.isDone()))
    {
      BAM.spin(directionType::rev, 100, velocityUnits::pct);
    } else if(BAM.isDone())
    {
      BAM.stop();
    }

    // Moves Front Pneumatics
    if(Controller1.ButtonUp.pressing() && frontWaiting <= 0)
    {
      FI.set(!FI.value());
      frontWaiting = 60;
    }
    frontWaiting--;

    // Moves Back Pneumatics
    if(Controller1.ButtonDown.pressing() && backWaiting <= 0)
    {
      BI.set(!BI.value());
      backWaiting = 60;
    }
    backWaiting--;

    if(Controller1.ButtonLeft.pressing())
    {
      BI.set(false);
      BAM.rotateTo(.76, rotationUnits::rev, false);
    }

    if(Controller1.ButtonRight.pressing())
    {
      BAM.rotateTo(0, rotationUnits::rev, false);
    }

    //Moves Converyor Belt for Rings
    if(Controller1.ButtonA.pressing() && ringWaiting <= 0)
    {
      ringActive = !ringActive;
      ringWaiting = 60;
    }
    ringWaiting--;

    if(ringActive && LAM.rotation(degrees) > 70 && RAM.rotation(degrees) > 70)
    {
      RI.spin(directionType::rev, 35, percentUnits::pct);
    }
    else
    {
      RI.stop();
    }

    if(Controller1.ButtonB.pressing())
    {
      allMotorStop();
    }

    if(Controller1.ButtonX.pressing() && rampWaiting <= 0)
    {
      ramp = !ramp;
      rampWaiting = 60;
    }
    rampWaiting--;

    if(Controller1.ButtonY.pressing())
    {
      FI.set(true);
      LAM.rotateTo(0, rotationUnits::rev, false);
      RAM.rotateTo(0, rotationUnits::rev, false);
    }

    // Sleep for 10 milliseconds as to not overwork the brain
    task::sleep(10);
  }
}

// Main program will call up pre-auton, autonomous, and the driver portion of
// the program This part of the program also sets up the default timeouts, brake
// types, and velocties for the motors at the beginning and the default speed for
// the motors. After this the program prints buttons on the touch screen so that
// we can choose our autonomous with this. Once we press the white start button
// it will the screen. Then pre auton occurs to callibrate the Inertial sensor.
// After that the autonomous can begin with whatever auton we chose using the
// select screen.

int main()
{
  //vex initialize
  vexcodeInit();

  // stopping
  LFDM.setStopping(brakeType::brake);
  RFDM.setStopping(brakeType::brake);
  LBDM.setStopping(brakeType::brake);
  RBDM.setStopping(brakeType::brake);
  LAM.setStopping(brakeType::hold);
  RAM.setStopping(brakeType::hold);
  BAM.setStopping(brakeType::hold);
  RI.setStopping(brakeType::coast);

  // velocity
  LFDM.setVelocity(100, percentUnits::pct);
  RFDM.setVelocity(100, percentUnits::pct);
  LBDM.setVelocity(100, percentUnits::pct);
  RBDM.setVelocity(100, percentUnits::pct);
  LAM.setVelocity(100, percentUnits::pct);
  RAM.setVelocity(100, percentUnits::pct);
  BAM.setVelocity(100, percentUnits::pct);
  RI.setVelocity(100, percentUnits::pct);

  // set GPS
  GPS.setLocation(0, 0, 0);

  // Run the pre-autonomous function
  pre_auton();

  // Run the autonomous function
  Competition.autonomous(autonomous);

  // Default Values
  side = 0;
  point = 2;
  skills = false;

  start = 0; // For testing.

  while(start == 0)
  {
    // --> Matches || Skills
    //     Side/No Auton || Select/Start

    // Draw Matches picture to selected
    // Draw Skills picture to unSelected
    // Draw Side/No picture
    // Draw Selected/Start
    Brain.Screen.drawImageFromFile("Matches.png", 18, 18);
    Brain.Screen.drawImageFromFile("NSSkills.png", 262, 18);
    Brain.Screen.drawImageFromFile("RightSide.png", 18, 129);
    Brain.Screen.drawImageFromFile("SelectAuton.png", 387, 129);
    Brain.Screen.drawImageFromFile("Debug.png", 202, 129);
    rln = 0;
    while(start == 0 && menu == 0)
    {
      menuPause++;
      if(Controller1.ButtonB.pressing())
      {
        start = 1;
        menu = 2;
        Brain.Screen.clearScreen();
        wait(500, msec);
        break;
      }
      if(Brain.Screen.pressing())
      {
        brX = Brain.Screen.xPosition();
        brY = Brain.Screen.yPosition();
        if(brX >= 18 & brX <= 218 & skills == true) // Matches 200px wide x 75px tall
        {
          if(brY >= 18 & brY <= 93)
          {
            rln = 0;
            skills = false;
            side = 0;
            // --> Matches || Skills
            //     Side/No Auton || Select/Start

            // Draw Matches picture to selected
            Brain.Screen.drawImageFromFile("Matches.png", 18, 18);
            // Draw Skills picture to unSelected
            Brain.Screen.drawImageFromFile("NSSkills.png", 262, 18);
            // Draw Side/No picture
            Brain.Screen.drawImageFromFile("RightSide.png", 18, 129);
            // Draw Selected/Start
            Brain.Screen.drawImageFromFile("SelectAuton.png", 387, 129);
          }
        }
        if(brX >= 262 & brX <= 462 & skills == false) // Skills 200px wide x 75px tall
        {
          if(brY >= 18 & brY <= 93)
          {
            skills = true;
            side = 2;
            //     Matches || Skills <--
            //     Driver || Auton

            // Draw Skills picture to selected
            // Draw Match piture to unSelected
            // Draw Driver picture
            // Draw Auton picture
            Brain.Screen.drawImageFromFile("NSMatches.png", 18, 18);
            Brain.Screen.drawImageFromFile("Skills.png", 262, 18);
            Brain.Screen.drawImageFromFile("StartSkillsDriver.png", 18, 129);
            Brain.Screen.drawImageFromFile("StartSkillsAuton.png", 387, 129);
          }
        }
        if(brX >= 18 && brX <= 93 && menuPause >= 640000)
        {
          if(brY >= 129 & brY <= 204)
          {
            if(skills == true) // Driver Button for skills
            {
              side = 2;
              point = 3; // No Autonomous
              menu = 2;
              start = 1;
              Brain.Screen.clearScreen();
              Brain.Screen.printAt(18, 18, "Skills - Driver");
            }
            if(skills == false) // Right side, Left side, or no Autonomous Button for matches
            {
              rln++;
              if(rln == 3)
              {
                rln = 0;
              }

              if(rln == 0)
              {
                // Draw right side of field
                Brain.Screen.drawImageFromFile("RightSide.png", 18, 129);
                // Draw Select Autonomous button (To the right)
                Brain.Screen.drawImageFromFile("SelectAuton.png", 387, 129);
                side = 0;
              }
              else if(rln == 1)
              {
                // Draw left side of field
                Brain.Screen.drawImageFromFile("LeftSide.png", 18, 129);
                // Draw Select Autonomous button (To the right)
                Brain.Screen.drawImageFromFile("SelectAuton.png", 387, 129);
                side = 1;
              }
              else if(rln == 2)
              {
                // Draw no autonomous
                // Draw Start button (To the right)
                Brain.Screen.drawImageFromFile("NoAuton.png", 18, 129);
                Brain.Screen.drawImageFromFile("StartButton.png", 387, 129);
                side = 2;
                point = 2; // No Autonomous
              }
            }
            menuPause = 0;
          }
        }
        if(brX >= 387 & brX <= 462)
        {
          if(brY >= 129 & brY <= 204)
          {
            if(skills == true) // Skills Autonomous Start Button
            {
              side = 2;
              point = 1; // Skills Autonomous
              menu = 2;
              start = 1;
              Brain.Screen.clearScreen();
              Brain.Screen.printAt(18, 18, "Skills - Autonomous");
            }
            if(skills == false) // Select Autonomous / Start button for matches
            {
              if(rln == 2)
              {
                menu = 2;
                start = 1;
              }
              else
              {
                menu = 1;
              }
            }
          }
        }
        if(brX >= 202 & brX <= 277)
        {
          if(brY >= 129 & brY <= 204)
          {
            menu = 3;
          }
        }
      }
    }

    if(menu == 2)
    {
      break;
    }
    // Draw Menu setup here
    // Menu row 1

    prevX = 204;
    prevY = 18;
    prevPicture = "Point2.png";

    Brain.Screen.clearScreen();
    if(menu == 3)
    {
      Brain.Screen.printAt(18, 113, "(Debug)");
    }
    else if(side == 0)
    {
      Brain.Screen.printAt(18, 113, "(On Right)");
    }
    else if(side == 1)
    {
      Brain.Screen.printAt(18, 113, "(On Left)");
    }
    else if(side == 2)
    {
      if(point == 2)
      {
        Brain.Screen.printAt(18, 18, "Match - No Autonomous");
      }
      break;
    }
    if(menu == 1)
    {
      Brain.Screen.printAt(128, 113, "|");
      Brain.Screen.printAt(138, 108, "Grab Neutral Mobile Goal, then get");
      Brain.Screen.printAt(138, 128, "the Autonomous Win Point.");
      Brain.Screen.drawImageFromFile("GoBack.png", 18, 18);
      Brain.Screen.drawImageFromFile("NSPoint1.png", 111, 18);   // Slot 1
      Brain.Screen.drawImageFromFile("Point2.png", 204, 18);     // Slot 2
      Brain.Screen.drawImageFromFile("NSPoint3.png", 297, 18);   // Slot 3
      Brain.Screen.drawImageFromFile("EmptyPoint.png", 390, 18); // Slot 4

      // Menu row 2
      Brain.Screen.drawImageFromFile("StartButton.png", 18, 129); // Start
      Brain.Screen.drawImageFromFile("EmptyPoint.png", 111, 129); // Slot 5
      Brain.Screen.drawImageFromFile("EmptyPoint.png", 204, 129); // Slot 6
      Brain.Screen.drawImageFromFile("EmptyPoint.png", 297, 129); // Slot 7
      Brain.Screen.drawImageFromFile("EmptyPoint.png", 390, 129); // Slot 8
    }
    while(start == 0 && menu == 1) // Matches Menu
    {
      // Change Side || Auton 1 || Auton 2 || Auton 3
      // Start || Auton 4 || Auton 5 || Auton 6
      if(Brain.Screen.pressing())
      {
        brX = Brain.Screen.xPosition();
        brY = Brain.Screen.yPosition();
        // Change sides ifneeded. --> Goes to previous Menu
        if(brX >= 18 & brX <= 93)
        {
          if(brY >= 18 & brY <= 93)
          {
            // Take back to previous Menu
            Brain.Screen.clearScreen();
            side = 0;
            point = 2;
            menu = 0;
            menuPause = 0;
            wait(500, msec);
          }
        }
        // Auton 1
        if(point != 1)
        {
          if(brX >= 111 & brX <= 186)
          {
            if(brY >= 18 & brY <= 93)
            {
              changePicture("Point1.png", 111, 18);
              Brain.Screen.printAt(138, 108, "                                  ");
              Brain.Screen.printAt(138, 128, "                                  ");
              Brain.Screen.printAt(138, 108, "Grab the Neutral Mobile Goal.");
              point = 1;
              wait(500, msec);
            }
          }
        }
        // Auton 2
        if(point != 2)
        {
          if(brX >= 204 & brX <= 279)
          {
            if(brY >= 18 & brY <= 93)
            {
              changePicture("Point2.png", 204, 18);
              Brain.Screen.printAt(138, 108, "Grab Neutral Mobile Goal, then get");
              Brain.Screen.printAt(138, 128, "the Autonomous Win Point.");
              point = 2;
              wait(500, msec);
            }
          }
        }
        // Auton 3
        if(point != 3)
        {
          if(brX >= 297 & brX <= 372)
          {
            if(brY >= 18 & brY <= 93)
            {
              changePicture("Point3.png", 297, 18);
              point = 3;
              wait(500, msec);
            }
          }
        }
        // Auton 4 - Not used since we don't have an Autonomous for slot 4.
        /*if(point != 4)
        {
          if(brX() >= 390 & brX() <= 465)
          {
            if(brY >= 18 & brY <= 93)
            {
              changePicture("Point4.png", 390, 18);
              point = 4;
              wait(500);
            }
          }
        }*/
        // Start button
        if(brX >= 18 & brX <= 93)
        {
          if(brY >= 129 & brY <= 204)
          {
            start = 1;
            menu = 2;
            Brain.Screen.clearScreen();
            Brain.Screen.printAt(18, 18, "Match - Autonomous %d", point);
          }
        }
        // Auton 5 - Not used since we don't have an Autonomous for slots 5-8.
        /*if(point != 5)
        {
          if(brX() >= 111 & brX() <= 186)
          {
            if(brY >= 129 & brY <=
        204)
            {
              changePicture("Point5.png", 111, 129);
              point = 5;
              wait(500);
            }
          }
        }
        //Auton 6
        if(point != 6)
        {
          if(brX() >= 204 & brX() <= 279)
          {
            if(brY >= 129 & brY <=
        204)
            {
              changePicture("Point6.png", 204, 129);
              point = 6;
              wait(500);
            }
          }
        }
        //Auton 7
        if(point != 7)
        {
          if(brX() >= 297 & brX() <= 372)
          {
            if(brY >= 129 & brY <=
        204)
            {
              changePicture("Point7.png", 297, 129);
              point = 7;
              wait(500);
            }
          }
        }
        //Auton 8
        if(point != 8)
        {
          if(brX() >= 390 & brX() <= 465)
          {
            if(brY >= 129 & brY <=
        204)
            {
              changePicture("Point8.png", 390, 129);
              point = 8;
              wait(500);
            }
          }
        }
      */
      }
    }
    if(menu == 3)
    {
      prevX = 111;
      prevY = 18;
      prevPicture = "DrivePID.png";
      Brain.Screen.printAt(128, 113, "|");
      Brain.Screen.printAt(138, 108, "                                  ");
      Brain.Screen.printAt(138, 128, "                                  ");
      Brain.Screen.printAt(138, 108, "Drive forward x inches with a PID");
      Brain.Screen.printAt(138, 128, "that incorporates motor encoders");
      Brain.Screen.drawImageFromFile("GoBack.png", 18, 18);
      Brain.Screen.drawImageFromFile("DrivePID.png", 111, 18);   // Slot 1
      Brain.Screen.drawImageFromFile("NSTurnPID.png", 204, 18);     // Slot 2
      Brain.Screen.drawImageFromFile("NSGoToPID.png", 297, 18);   // Slot 3
      Brain.Screen.drawImageFromFile("NSRobotInfo.png", 390, 18); // Slot 4

      // Menu row 2
      Brain.Screen.drawImageFromFile("StartButton.png", 18, 129); // Start
      Brain.Screen.drawImageFromFile("Up.png", 111, 141); // Slot 7
      Brain.Screen.drawImageFromFile("Down.png", 284, 141); // Slot 8
      Brain.Screen.printAt(164, 166, "            ");
      Brain.Screen.printAt(164, 166, "Value = %d", (int)val);
      point = 1;
    }
    while(start == 0 && menu == 3) // Debug Menu
    {
      if(Brain.Screen.pressing())
      {
        brX = Brain.Screen.xPosition();
        brY = Brain.Screen.yPosition();
        // Go Back if needed. --> Goes to previous Menu
        if(brX >= 18 & brX <= 93)
        {
          if(brY >= 18 & brY <= 93)
          {
            // Take back to previous Menu
            Brain.Screen.clearScreen();
            side = 0;
            point = 2;
            menu = 0;
            menuPause = 0;
            val = 0;
            wait(500, msec);
          }
        }
        // Debug 1
        if(point != 1)
        {
          if(brX >= 111 & brX <= 186)
          {
            if(brY >= 18 & brY <= 93)
            {
              changePicture("DrivePID.png", 111, 18);
              Brain.Screen.printAt(138, 108, "                                  ");
              Brain.Screen.printAt(138, 128, "                                  ");
              Brain.Screen.printAt(138, 108, "Drive forward x inches with a PID ");
              Brain.Screen.printAt(138, 128, "that incorporates motor encoders  ");
              point = 1;
              wait(500, msec);
            }
          }
        }
        // Debug 2
        if(point != 2)
        {
          if(brX >= 204 &brX <= 279)
          {
            if(brY >= 18 & brY <= 93)
            {
              changePicture("TurnPID.png", 204, 18);
              Brain.Screen.printAt(138, 108, "                                  ");
              Brain.Screen.printAt(138, 128, "                                  ");
              Brain.Screen.printAt(138, 108, "Turn x degrees with a PID that    ");
              Brain.Screen.printAt(138, 128, "incorporates inertial heading     ");
              point = 2;
              wait(500, msec);
            }
          }
        }
        // Debug 3
        if(point != 3)
        {
          if(brX >= 297 & brX <= 372)
          {
            if(brY >= 18 & brY <= 93)
            {
              changePicture("GoToPID.png", 297, 18);
              Brain.Screen.printAt(138, 108, "                                  ");
              Brain.Screen.printAt(138, 128, "                                  ");
              Brain.Screen.printAt(138, 108, "Go to (0,0) with the GPS Sensor   ");
              Brain.Screen.printAt(138, 128, "Using the turn and drive PID      ");
              point = 3;
              wait(500, msec);
            }
          }
        }
        // Debug 4
        if(point != 4)
        {
          if(brX >= 390 & brX <= 465)
          {
            if(brY >= 18 & brY <= 93)
            {
              changePicture("RobotInfo.png", 390, 18);
              Brain.Screen.printAt(138, 108, "                                  ");
              Brain.Screen.printAt(138, 128, "                                  ");
              Brain.Screen.printAt(138, 108, "Battery: %d%% Heading: %f ", Brain.Battery.capacity(), (((int)(Inertial.heading() * 100))/100));
              Brain.Screen.printAt(138, 128, "X: %f Y: %f", GPS.xPosition(), GPS.yPosition());
              point = 4;
              wait(500, msec);
            }
          }
        }
        // Debug Up
        if(brX >= 111 & brX <= 161)
        {
          if(brY >= 141 & brY <= 191)
          {
            val += 2;
            Brain.Screen.printAt(164, 166, "           ");
            Brain.Screen.printAt(164, 166, "Value = %d", (int)val);
            wait(200, msec);
          }
        }
        // Debug Down
        if(brX >= 284 & brX <= 334)
        {
          if(brY >= 141 & brY <= 191)
          {
            val -= 2;
            Brain.Screen.printAt(164, 166, "            ");
            Brain.Screen.printAt(164, 166, "Value = %d", (int)val);
            wait(200, msec);
          }
        }
        if(point == 4)
        {
          Brain.Screen.printAt(138, 108, "                                  ");
          Brain.Screen.printAt(138, 128, "                                  ");
          Brain.Screen.printAt(138, 108, "Battery: %d%% Heading: %f ", Brain.Battery.capacity(), (((int)(Inertial.heading() * 100))/100));
          Brain.Screen.printAt(138, 128, "X: %f Y: %f", GPS.xPosition(), GPS.yPosition());
        }
        // Start button
        if(brX >= 18 & brX <= 93)
        {
          if(brY >= 129 & brY <= 204)
          {
            start = 1;
            Brain.Screen.clearScreen();
            break;
          }
        }
      }
    }
  }
  if(side == 0)
  {
    Controller1.Screen.print("Side: Right, Auton: %d", point);
  }
  else if(side == 1)
  {
    Controller1.Screen.print("Side: Left, Auton: %d", point);
  }

  // Run the driver control function
  Competition.drivercontrol(usercontrol);

  // Prevent main from exiting with an infinite loop.
  while(1) 
  {
    task::sleep(100);
  }
}
