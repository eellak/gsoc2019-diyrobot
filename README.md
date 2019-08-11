:rocket: GSOC 2019 - A DIY robot kit for educators 
===============

## Introduction
With that project designed an easy to assembly and program robot. The designs is 3D printable and all the electronics parts are easy to find in any electronic equipment store. The robot have the  Raspberry Pi 3+  as the main computer with Raspbian operating system combined with Jupyter Notebook as programing interface and a Node.js application as front end main control page. You can program and control the robot through your browser using the Proteas wireless access Point. 

[View the project on Google Summer of Code website](https://summerofcode.withgoogle.com/projects/#6536613096587264).

You can see the detailed timeline [here](https://github.com/eellak/gsoc2019-diyrobot/blob/master/gsoc-timeline.md).



![proteas robot advance](./assets/images/advance.png)

Final Report
------------

You can visit this [gist](https://gist.github.com/chronis10/9d069c56b3df9c92693ac8d24270a62a) that summarizes in a few words, the work which was done during the Google Summer of Code working period.

Synopsis
--------

With that project you can construct a modular robot, easy to use with cheap electronics parts  and 3D printed parts. The procedure to construct is explained detailed on the [Wiki](https://github.com/eellak/gsoc2019-diyrobot/wiki) of the project. The main procedure is:

1. Read the wiki and choose the type of robot you want
2. Gather all the needed electronic parts
3. Print the parts
4. Preassembly the blocks
5. Burn the custom Raspbian image and load it to the Raspberry PI
6. Assembly the robot
7. Power on the robot 
8. Connect to  proteas network and have fun.

Challenges -> Problems -> Solutions
--------

The main challenge of the project it was the requirement to avoided the usage of tools on the assembly stage. The first days of the project designed and tested about ten different designs of the socket system. An other problem it was the voltages of the electronic parts, most of the parts it was designed to work with the Arduino 5V voltages but the Raspberry Pi voltages it was 3V and for that reason used a Bidirectional Logic Level Converter.  Also the investigation of  a stable and capable power source it was crucial because nobody wants a robot with short working time, finally selected a custom build power block (BMS, Li-ion batteries and stepdown circuit) which offers excellent performance, recharging capability, usage of the robot with external power supply and long working time. Finally because the robot needed to be easy to programmed form people with low experience on programming, decided to use a object oriented way. The code for the electronic parts in some cases it was complicated for a new user and using the object oriented way the code transformed from 50 lines to 3 lines easy to understand and use code. 




GSoC Deliverables
------------

1. 3D printed parts ready to print
2. Python library for easy usage and control the robot
3. Integration with Jupyter
4. Easy way to access the robot
5. Custom Raspbian image with OpenCV, Jupyter, Node.js, Python libraries, instructions and configuration intergraded.
6. Extensive instruction for the assembly and usage
7. Jupyter Notebooks with examples and educational material

Future Work
------------

There is still a lot work that may be done, in order the Proteas robot to be a direct competitive to any commercial alternative on education robotics and I believe, with the support of the Open Source community, that goal can be reached. Feel free, to contribute and participate on that project, any suggestion and improvement are welcomed. 

Some thoughts for future expansion:

1. Support of analogue sensors
2. More 3D printed components
3. More electronic sensors support
4. Improvements on designs
5. Integration with Scratch, Node-RED
6. Compatibility with Arduino
7. Better wireless connection ways
8. Companion app for Android/IOS
9. Custom build PCB for easy connection of the electronic components



### Student

* Christos Chronis

### GSoC Mentors

* Iraklis Varlamis
* Theodoros Karounos
* Konstantinos Kalovrektis

### Organization :  Open Technologies Alliance - GFOSS 

<a rel="license" href="http://creativecommons.org/licenses/by-sa/4.0/"><img alt="Creative Commons License" style="border-width:0" src="https://i.creativecommons.org/l/by-sa/4.0/88x31.png" /><br></a>The 3D designs, educational material and text is licensed under a <a rel="license" href="http://creativecommons.org/licenses/by-sa/4.0/">Creative Commons Attribution-ShareAlike 4.0 International License</a>.