# AutoTT
This is the code used to steer the self driving car described in [this project](https://autottblog.wordpress.com). The car is control from an iPhone using [this app](https://github.com/task123/AutoTTApp).

## Describtion of the car
The got two electric motors, a swivel wheel on the back and to webcameras in the front. A Raspberry Pi 3 is used to steering the car with the help of one Arduino Uno and a Arduino Nano. 

## Capabilites

## Overview of what the different modules does

### Connection to the app 
####(TCP.py)

### Steering the app 
####(Modes.py, Steering.py, Motors.py and Tripmeter.py)

### Status and lights 
####(Status.py and Lights.py)

### Cameras 
####(Cameras.py and templates)

### Running the program 
####(mainLoop.py, controllerOfMainloop.py and startControllerOfMainLoopAtBoot.sh)

## Nanpy
Python library and Arduino program to control the Arduino from the Raspberry Pi. It is poorly documented, but work fine if you only want to control the ports. We have added 'analogReference(INTERNAL)' in the setup function of the Arduino program part of Nanpy, to get more accurate voltage readings.

## Arduino 
####(tripMeterArduino, CH341SER_MAC and CH341SER_WIN)

