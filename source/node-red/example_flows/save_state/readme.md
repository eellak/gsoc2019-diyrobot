# save state

Using this flow, we create a csv file that holds information about the measurements of all the sensors that the diyrobot contains and information about the state the robot. 
More specifically, we hold information about the direction of movement of each motor, the distance that each motor has travelled measured in centimeters and revolutions and the distance that the ultarsonic sensor measures.

Using the `state.csv`, we can make analysis and visulaise different information. For example, using the `show_route.py` file, we produce a visualisation of the route that the robot follows. 

In the node-red flow, we can define the delay time, that means the duration between each record of state. 
