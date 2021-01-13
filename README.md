# mwr
## Mobile Wheeled Robot library

I'm making a robot, and I want the code to be in more than one place.


## Joystick Controls for Two Wheels

Motor control takes the vector (r, θ) as an input from the joystick, where r spans (0,1) and θ spans (-π, π).

These polar coordinates are translated from (x,y) coordinates of the joystick control, where θ = arctan(Y-offset/X-offset).
###### Note: thats written in Java, so it's Math.arctan**2**(y,x) and not straight up arctan because of course it isn't. X and Y offset have also been translated -π/2, aka 90 degrees counter-clockwise by (x,y) -> (-y,x) so it's actually arctan(x,-y). Confusing at first, but since arctan takes a fraction it saves having to translate the polar coordinate by giving arctan translated cartesian coordinates.

R, or radius, is the strength of the joystick direction. So 1 is full power and 0 is of course full stop, with any value in between.

These polar coordinates assume UP on the joystick is 0 degrees for forwards, and DOWN is π and -π degrees for backwards. (Negative and postive π are equal in terms of the direction of the joystick). LEFT and RIGHT are hard turns to the LEFT and RIGHT, while 45 degrees LEFT and RIGTH are slow turns. The difference between hard and slow turn is that the motor on the side to turn towards is either reversing or stopped. So for a hard turn LEFT the left motor is full reverse and the right motor is full forwards, and the opposite for a hard turn RIGHT.

For any left turn between 45 degrees and directly forwards, the left motor will slowly increase to full from stop, and between 45 and 90 degrees left the motor will slowly increase reverse speed to full reverse. For forwards movement on the joystick this can be modeled as cos(2θ) and for backwards on the joystick it is sin(2θ-π/2).

![Alt Text](pictures/joystick%20to%20motor%20power%20graph.png?raw=true "Joystick-Motor power graph")

###### For more reading on polar coordinates check out https://www.mathsisfun.com/polar-cartesian-coordinates.html and https://mathworld.wolfram.com/PolarCoordinates.html
