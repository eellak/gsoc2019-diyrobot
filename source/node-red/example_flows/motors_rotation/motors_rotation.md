# Motos Rotation

In this example, we rotate the robot remotely using Node-Red.
To connect to the Node-Red platform, you can just use the browser and go to the local IP address using the port `1880`. Also make sure that the flask server, responsible for answering requests, is up and running. 

You can copy and paste the `rotate_anticlockwise_version_A.json` and `rotate_clockwise_version_A.json` files to rotate the robot anticlockwise and clockwise respectively. 
The two flows use http requests to move the wheels forward and backwards for specific amount of time. The amount of time can be adjusted.
