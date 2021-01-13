# mwr
Mobile Wheeled Robot library

I'm making a robot, and I want the code to be in more than one place.


Joystick Controls for Two Wheels

Motor control takes the vector (r, θ) as an input from the joystick, where r spans (0,1) and θ spans (-π, π).

R, or radius, is the strength of the joystick direction. So 1 is full power and 0 is of course full stop, with any value in between.

These polar coordinates assume UP on the joystick is 0 degrees for forwards, and DOWN is π and -π degrees for backwards. (Negative and postive π are equal in terms of the direction of the joystick). LEFT and RIGHT are hard turns to the LEFT and RIGHT, while 45 degrees LEFT and RIGTH are slow turns. The difference between hard and slow turn is that the motor on the side to turn towards is either reversing or stopped. So for a hard turn LEFT the left motor is full reverse and the right motor is full forwards, and the opposite for a hard turn RIGHT.

For any left turn between 45 degrees and directly forwards, the left motor will slowly increase to full from stop, and between 45 and 90 degrees left the motor will slowly increase reverse speed to full reverse. For forwards movement on the joystick this can be modeled as cos(2θ) and for backwards on the joystick it is sin(2θ-π/2).

![Alt Text](joystick%20to%20motor%20power%20graph.png?raw=true "Joystick-Motor power graph")
