import RPi.GPIO as GPIO


class Wheel:
   # Wheel assumes you're using a L293D motor driver, so you have to have an enable signal and fwd/rev demand signals.
   def __init__ (self, enable_pin, forward_pin, reverse_pin)
      #set interval variables from parameters
      self.enable = enable_pin
      self.forward = forward_pin
      self.reverse = reverse_pin
      #initialize GPIO to do things
      GPIO.setmode(GPIO.BOARD)
      GPIO.setup(self.enable, GPIO.OUT)
      GPIO.setup(self.forward, GPIO.OUT)
      GPIO.setup(self.reverse, GPIO.OUT)
      #enable motor
      GPIO.ouput(self.enable, GPIO.HIGH)

   def stop(self)
      #stop the motor by turning off the enable signal
      GPIO.output(self.enable, GPIO.LOW)

   def forward(self)
      #go forward (includes turning enable to HIGH)
      GPIO.output(self.enable, GPIO.HIGH)
      GPIO.output(self.forward, GPIO.HIGH)
      GPIO.output(self.reverse, GPIO.LOW)

   def reverse(self)
      #go forward (includes turning enable to HIGH)
      GPIO.output(self.enable, GPIO.HIGH)
      GPIO.output(self.reverse, GPIO.HIGH)
      GPIO.output(self.forward, GPIO.HIGH)

