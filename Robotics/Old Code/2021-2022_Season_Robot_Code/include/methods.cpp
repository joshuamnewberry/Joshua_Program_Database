#include "vex.h"
#include "variables.cpp"
#include <algorithm>
#include <cmath>
#include <string>

void changePicture(std::string newPicture, int newX, int newY)
{
  changeOldString = "NS";
  changeOldString += prevPicture;

  char* cNewPic = new char[newPicture.length() + 1];
  strcpy(cNewPic, newPicture.c_str());
  char* cOldPic = new char[changeOldString.length() + 1];
  strcpy(cOldPic, changeOldString.c_str());

  Brain.Screen.drawImageFromFile(cNewPic, newX, newY);
  Brain.Screen.drawImageFromFile(cOldPic, prevX, prevY);
  
  prevPicture = newPicture;
  prevX = newX;
  prevY = newY;
}

// Changes direction of drive base for the drive spin program
void changeDriveDirection(std::string direct)
{
  if(direct == "rev" || direct == "r") // Drive Backward
  {
    LF = reverse;
    RF = reverse;
    LB = reverse;
    RB = reverse;
  }
  else if(direct == "tl") // Turn Left
  {
    LF = reverse;
    RF = forward;
    LB = reverse;
    RB = forward;
  }
  else if(direct == "tr") // Turn Right
  {
    LF = forward;
    RF = reverse;
    LB = forward;
    RB = reverse;
  }
  else // Drive Forward
  {
    LF = forward;
    RF = forward;
    LB = forward;
    RB = forward;
  }
}

// Spin drive at pre-set direction at velocity velo
void driveSpin(double velo)
{
  LFDM.spin(LF, velo, percentUnits::pct);
  RFDM.spin(RF, velo, percentUnits::pct);
  LBDM.spin(LB, velo, percentUnits::pct);
  RBDM.spin(RB, velo, percentUnits::pct);
}

// Stop all drive motors with brake type BT
void driveStop(vex::brakeType BT)
{
  LFDM.stop(BT);
  RFDM.stop(BT);
  LBDM.stop(BT);
  RBDM.stop(BT);
}

// Drive forwards or backwards (with negative target) using a PID. PID velocity
// is multiplied by multVelo.
void drivePID(double target, double multVelo)
{
  // backwards boolean
  bool back = target < 0;

  if(back) // Change the direction to drive forward or reverse.
  {
    changeDriveDirection("rev");
  }
  else
  {
    changeDriveDirection("for");
  }

  // Kp * e(t) + Ki * intergral(e(t)) * changeError + Kd * changeError /
  // changeTime <-- Formula for PID

  // Get current position of the left front wheel for measurement and
  // compairison, set it in revolutions.
  double targetR = (target * 90 / M_PI) + RFDM.position(deg);
  double targetL = (target * 90 / M_PI) + LFDM.position(deg);

  // Changing values:
  // These values will change in order to translate the PID into the robot's
  // motion.
  double rError = targetR - RFDM.position(deg);
  double lError = targetL - LFDM.position(deg);
  if(back)
  {
    rError *= -1;
    lError *= -1;
  }
  double Time = 1;
  double startingAngle = Inertial.heading(deg);
  double currentAngle = Inertial.heading(deg);
  double vError = currentAngle - startingAngle;

  // Result:
  // This is the end speed the motors will be at when the calculations are
  // finished.
  double rU;
  double lU;

  while(rError > 1 || lError > 1)
  {
    rError = targetR - RFDM.position(deg);
    lError = targetL - LFDM.position(deg);

    currentAngle = Inertial.heading(deg);
    vError = currentAngle - startingAngle;
    if(vError <= .9 && vError >= -.9)
    {
      vError = 0;
    }

    if(back)
    {
      rError *= -1;
      lError *= -1;
    }
    rU = (driveKp * rError) + (driveKi * rError * Time) + (driveKd * rError / Time) - (driveKv * vError);
    if(rError <= .9)
    {
      rU = 0;
    }
    lU = (driveKp * lError) + (driveKi * lError * Time) + (driveKd * lError / Time) + (driveKv * vError);
    if(lError <= .9)
    {
      lU = 0;
    }
    // Spin at velocity 'u' times a constant (Constant is for more/less speed).
    LFDM.spin(LF, lU * multVelo, percentUnits::pct);
    RFDM.spin(RF, rU * multVelo, percentUnits::pct);
    LBDM.spin(LB, lU * multVelo, percentUnits::pct);
    RBDM.spin(RB, rU * multVelo, percentUnits::pct);
    Time++;
    wait(50, msec);
  }
  // Stop: (Breaktype is hold since we don't want it to coast past the point.)
  driveStop(hold);
}

// This function turns the bot left using a PID incorporating the inertial
// sensor. PID velocity is multiplied by multVelo.
void turnLeft(double target, double multVelo)
{
  // defining variables
  double reading = Inertial.heading(deg);
  double dest = 0.0;
  bool stillGo = true;
  double lowRange = 0.0;
  double highRange = 0.0;
  double u;
  // Turn left
  dest = reading - target;
  while(dest < 0)
  {
    dest = dest + 360;
  }
  while(dest > 360)
  {
    dest = dest - 360;
  }
  lowRange = dest - 2;
  highRange = dest + 2;

  // These values will change in order to translate the PID into the robot's
  // motion.
  double Error = reading - dest;
  if(Error < 0)
  {
    Error += 360;
  }
  double Time = 1;

  while(stillGo == true)
  {
    reading = Inertial.heading(degrees);
    double Error = reading - dest;
    if(Error < 0)
    {
      Error += 360;
    }
    u = (turnKp * Error) + (turnKi * Error * Time) + (turnKd * Error / Time);

    // Spin at velocity 'u' times a constant (Constant is for more/less speed).
    LFDM.spin(LF, u * multVelo, percentUnits::pct);
    RFDM.spin(RF, u * multVelo, percentUnits::pct);
    LBDM.spin(LB, u * multVelo, percentUnits::pct);
    RBDM.spin(RB, u * multVelo, percentUnits::pct);
    Time++;
    if(reading >= lowRange && reading <= highRange)
    {
      driveStop(hold);
      stillGo = false;
    }
    if(Error < .9)
    {
      driveStop(hold);
      stillGo = false;
    }
    wait(50, msec);
  }
  Error = 0;
  u = 0;
}

// This function turns the bot left using a PID incorporating the inertial
// sensor. PID velocity is multiplied by multVelo.
void turnRight(double target, double multVelo)
{
  // defining variables
  double reading = Inertial.heading(deg);
  double dest = 0.0;
  bool stillGo = true;
  double lowRange = 0.0;
  double highRange = 0.0;
  double u;
  // Turn left
  dest = reading + target;
  while(dest < 0)
  {
    dest = dest + 360;
  }
  while(dest > 360)
  {
    dest = dest - 360;
  }
  lowRange = dest - 2;
  highRange = dest + 2;

  // These values will change in order to translate the PID into the robot's
  // motion.
  double Error = dest - reading;
  if(Error < 0)
  {
    Error += 360;
  }
  double Time = 1;

  while(stillGo == true)
  {
    reading = Inertial.heading(degrees);
    double Error = dest - reading;
    if(Error < 0)
    {
      Error += 360;
    }
    u = (turnKp * Error) + (turnKi * Error * Time) + (turnKd * Error / Time);

    // Spin at velocity 'u' times a constant (Constant is for more/less speed).
    LFDM.spin(LF, u * multVelo, percentUnits::pct);
    RFDM.spin(RF, u * multVelo, percentUnits::pct);
    LBDM.spin(LB, u * multVelo, percentUnits::pct);
    RBDM.spin(RB, u * multVelo, percentUnits::pct);
    Time++;
    if(reading >= lowRange && reading <= highRange)
    {
      driveStop(hold);
      stillGo = false;
    }
    if(Error < .9)
    {
      driveStop(hold);
      stillGo = false;
    }
    wait(50, msec);
  }
  Error = 0;
  u = 0;
}

// Helper method for the turn methods where turn left is a negative input.
void turnPID(double target, double multVelo)
{
  if(target < 0)
  {
    changeDriveDirection("tl");
    turnLeft(-target, multVelo);
  }
  else if(target > 0)
  {
    changeDriveDirection("tr");
    turnRight(target, multVelo);
  }
}

// Drives to a certain point on the field using the GPS sensor.
void goToTan(double endingX, double endingY, double turnVelo, double driveVelo)
{
  // Get the current position and rotation of the robot:
  double startingX = GPS.xPosition(inches);
  double startingY = GPS.yPosition(inches);
  double startingH = GPS.heading();

  if(startingH >= 180)
  {
    startingH = startingH - 360;
  }

  // Implement atan to calculate the heading that the robot needs to turn to
  // face the end point.
  float turnAngle = atan((endingX - startingX) / (endingY - startingY)) * 180 / M_PI;
  if(endingY - startingY < 0)
  {
    turnAngle = turnAngle + 180;
  }

  float degreesLeft = turnAngle - startingH;

  if(degreesLeft > 180)
  {
    degreesLeft = degreesLeft - 360;
  }
  if(degreesLeft < -180)
  {
    degreesLeft = degreesLeft + 360;
  }

  turnPID(degreesLeft, turnVelo);

  // Calculate the drive distance needed, then drive towards the target
  // position:
  double driveDistance = sqrt(((endingX - startingX) * (endingX - startingX)) + ((endingY - startingY) * (endingY - startingY)));

  drivePID(driveDistance, driveVelo); // Drive forward using PID.
}

// Moves the lift motors an amount of rotations at velocity velo.
void moveLift(double rotations, double velo)
{
  LAM.rotateTo(rotations, rotationUnits::rev, velo, velocityUnits::pct, false);
  RAM.rotateTo(rotations, rotationUnits::rev, velo, velocityUnits::pct);
}

// Stops all motors to prevent moving from outside forces.
void allMotorStop()
{
  while(true)
  {
    // stop
    LFDM.stop(brakeType::hold);
    RFDM.stop(brakeType::hold);
    LBDM.stop(brakeType::hold);
    RBDM.stop(brakeType::hold);
    LAM.stop(brakeType::hold);
    RAM.stop(brakeType::hold);
    BAM.stop(brakeType::hold);
    wait(750, msec);
    // Breaks out of loop back to user control
    if(Controller1.ButtonB.pressing())
    {
      // reset stopping of motors
      LFDM.setStopping(brakeType::brake);
      RFDM.setStopping(brakeType::brake);
      LBDM.setStopping(brakeType::brake);
      RBDM.setStopping(brakeType::brake);
      wait(750, msec);
      return;
    }
  }
}