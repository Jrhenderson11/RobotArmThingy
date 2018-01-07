# RobotArmThingy
Robot arm controlled with a leap motion via a network connection

Has 2 parts:


###Server

This part is connected to the leap, and provides movement commands to the raspberry pi across a network


###Client

Runs on a raspberry pi, recieves commands from network and executes them by turning off an on relays using the GPIO pins.


##Network

for this project I connected my laptop and raspberry pi using an etherenet cable to create a local network with static IPs on both ends.
The interfaces file for both devices can be found in the repo as server-interfaces and client-interfaces.



