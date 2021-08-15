# flask-server

In order to have remote control over the robot, we create a flask server. The server will provide API for users to interact with the robot, either sending instructions to the robot or requesting information from sensors.

The pins selected for the different sensors (ultrasonic, motors, odometers) are considered fixed. The user can find the predefined connections in the wiki page. 

## /

This endpoint returns a string, signaling that the server is up and running. 

## /shutdown

This endpoint stops the server and provides a safe exit. 
The same routine is called with ^C.

## /dist

This endpoint returns the distance of the obstacle around. 
For the measurement, the ultrasonic sensor is being used. 

## /odometer/<action>

## /motor/<action>

This endpoint is used for controlling the motors of the robot. 
Available actions:
* `move`: instrctu motor to move forward
* `reverse`: instruct motor to move backward
* `stop`: stop the movement of the motor
  
The request also contains extra parameters for the get request:


## /state

Using this endpoint, a json object with information about the state and metrics of all sensors is returned. 
The object has the following attributes:

```
{ 
    "status": "ok",     // information 
    "dist_a": dist_a,   // distance motor_a has travelled (in centimeteres)
    "dist_b": dist_b,
    "rev_a": rev_a,     // revolutions of motor_a
    "rev_b": rev_b,
    "dist_u": dist_u,   // distance of closest obstacle, ultrasonic sensor (in centimeteres)
    "motor_a": motor_a, // state of motor_a; (moving forward, backward or stopped)
    "motor_b": motor_b  //
}
```

