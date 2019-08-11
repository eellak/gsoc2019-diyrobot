# The mind of the Robot

Here you can find all the needed files (python libraries and scripts) for a smooth deployment. For instructions visit the [Wiki](https://github.com/eellak/gsoc2019-diyrobot/wiki) of the repository

An overview of my programming stuck.
![prog stuck](../assets/images/prog_stuck.png)


* Python robot library :white_check_mark::
  * Buzzer class :white_check_mark:
  * Dc motor class :white_check_mark:
  * Optical odometer class :white_check_mark:
  * Obstacle ir sensor  class :white_check_mark:
  * Servo motor class :white_check_mark:
  * Nokia 5110 screen :white_check_mark:
  * MPU6050 accelerometer :white_check_mark:
  * HMC5883L compass :white_check_mark:
  * Ultrasonic sensor :white_check_mark:
  * General input class (every sensor with digital output eg. light sensor) :white_check_mark:
  * General output class (led and every sensor with digital input eg.  relay shield) :white_check_mark:
  * Button class with software Pull Down parameter enabled :white_check_mark:
  * Timer class for usage on PID,logs or every usage with time elapsed needs :white_check_mark:
  * Log data class store data for plot or evaluation :white_check_mark:
  * Make csv class save measurements to csv :white_check_mark:
  * PID class :white_check_mark:
  * Inverse Kinematics for 2-DOF robotic arm :white_check_mark:

* Computer Vision library :white_check_mark:
  * Capture image class :white_check_mark:
  * Image preview class on Jupyter notebook :white_check_mark:
  * Aruco artifacts class :white_check_mark:
  * Line follower class (camera mode) :white_check_mark:
  * Face detection class  :white_check_mark:
  * Follow the target class (line,face or Aruco artifact) :white_check_mark:
  * Approach the target class (face or Aruco artifact) :white_check_mark:
  
* Special Classes for educational examples
  * Acceleration and Velocity experiment with graphs :white_check_mark:
  * Line follower robot :white_check_mark:
  * Collision avoidance :white_check_mark:

* Scripts section
  * create_hotspot.sh Make the Raspberry Pi a wireless Access Point. :white_check_mark:

* Browser interface
  * NodeJS app for robot management from your browser.:white_check_mark:

## :exclamation: **Important Notice** :exclamation:
:cop: The robot fully comply with the three laws of robotics:

**Asimov's Laws**

  * **First Law:** A robot may not injure a human being or, through inaction, allow a human being to come to harm.
  * **Second Law:** A robot must obey the orders given it by human beings except where such orders would conflict with the First Law.
  * **Third Law:** A robot must protect its own existence as long as such protection does not conflict with the First or Second Laws.

## Explanation of the marks
* :warning: Under Construction, probably errors not ready for use.
* :white_check_mark: Ready for usage.
* :construction: Upcoming release
