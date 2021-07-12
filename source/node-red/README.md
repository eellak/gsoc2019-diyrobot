# node-red

This direcotry contains two sub-directories:
* example-flows
* node-red-contrib-diyrobot

## example-flows

The directory contains examples of flows that can be copied and pasted directly to the node-red platform. This helps the users get started with using the diyrobot and controling it through node-red.

## node-red-contrib-diyrobot

This directory contains the custom nodes that can be used throught the platform for handling the diyrobot. 

To get the custom nodes appearing in the node-red runtime interface we first need to install the package. On Mac OS or Linux, the installation happens as follows: 

```
cd ~/.node-red
npm install ~/<path-to-diyrobot-project>/source/node-red/node-red-contrib-diyrobot
```
