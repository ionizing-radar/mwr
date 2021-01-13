# mwr
Mobile Wheeled Robot library

I'm making a robot, and I want the code to be in more than one place.


Joystick Controls for Two Wheels

rover_server.py takes (r, theta) as an input. These polar coordinates assume UP on the joystick is 0 degrees for forwards, and DOWN is π and -π degrees for backwards. (Negative and postive π are equal in terms of the direction of the joystick). LEFT and RIGHT are hard turns to the LEFT and RIGHT, while 45 degrees LEFT and RIGTH are slow turns. The difference between hard and slow turn is that the motor on the side to turn towards is either reversing or stopped. So for a hard turn LEFT the left motor is full reverse and the right motor is full forwards, and the opposite for a hard turn RIGHT.

For any left turn between 45 degrees and directly forwards, the left motor will slowly increase to full from stop, and between 45 and 90 degrees left the motor will slowly increase reverse speed to full reverse. For forwards movement on the joystick this can be modeled as cos(2θ) and for backwards on the joystick it is sin(2θ-π/2).



In Wolfram Alpha this looks like:
Right Motor: Plot[Piecewise[{{sin(2*θ-π/2),θ > pi/2}, {1, pi/2 > θ > 0},{cos(2θ), -pi/2 < θ <0}, {-1, θ < -pi/2}}], {θ, -pi, pi}]

Left Motor: Plot[Piecewise[{{-1,θ > pi/2}, {cos(2θ), pi/2 > θ > 0},{1, -pi/2 < θ <0}, {sin(2*θ-π/2), θ < -pi/2}}], {θ, -pi, pi}]

					if (theta > (math.pi/2)): # back left
						setMotor(r, math.sin(2*theta-math.pi/2), -1)
					elif (theta > 0): # forward left
						setMotor(r, 1, math.cos(2*theta))
					elif (theta > (-1 * math.pi/2)): # forward right
						setMotor(r, math.cos(2*theta), 1)
					else: # back right
						setMotor(r, -1, math.sin(2*theta-math.pi/2))
