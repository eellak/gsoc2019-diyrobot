# Motos Movement

In this example, we move the robot remotely using Node-Red.
To connect to the Node-Red platform, you can just use the browser and go to the local IP address using the port `1880`. Also make sure that the flask server, responsible for answering requests, is up and running. 

You can copy and paste the `flows_backward_and_forward_movement.json` file to move the robot backwards and than forward. 
The flow uses http requests to move the wheels forward and backwards, with pred-defined amount of time between switching tasks. The amount of time can be adjusted.
