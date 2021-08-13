# ultrasonic sensor 

In this example, we make use of the ultrasonic sensor to measure distance between robot and surrounding objects.

We use the `ultrasonic_sensor_check.json` to measure the distance. 

Two versions of flows can be used for this example:
* the first version makes use of the http request node and returns the API response 
* the second version uses the custom made node that makes the http request automatically and returns a custom made object containing information about the distance measured. 

