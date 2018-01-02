import RPi.GPIO as GPIO

class Wheel:
   # Wheel assumes you're using a L293D motor driver, so you have to have an enable signal and fwd/rev demand signals.

   DEBUG = False

   def __init__ (self, enable_pin, forward_pin, reverse_pin):
      # set interval variables from parameters
      self.enable = enable_pin
      self.forward = forward_pin
      self.reverse = reverse_pin
      # debug output
      if Wheel.DEBUG:
         print "Initializing "+ str(self)+" with:"
         print "   enable_pin: " + str(enable_pin) + " as " + str(self.enable)
         print "   forward_pin: "+ str(forward_pin) + " as " + str(self.forward)
         print "   reverse_pin: "+ str(reverse_pin) + " as " + str(self.reverse)
      # initialize GPIO to do things
      GPIO.setup(self.enable, GPIO.OUT)
      GPIO.setup(self.forward, GPIO.OUT)
      GPIO.setup(self.reverse, GPIO.OUT)
      # enable motor
      GPIO.output(self.enable, True)

   def test_func(self):
      if Wheel.DEBUG:
         print "test_func " + str(self)

   # stop the motor by turning off the enable signal
   def stop(self):
      if Wheel.DEBUG:
         print "stopping " + str(self)
      GPIO.output(self.enable, False)

   # go forward (includes turning enable to HIGH)
   def start(self):
      if Wheel.DEBUG:
         print "starting " + str(self)
         print self.enable
         print self.forward
         print self.reverse
      GPIO.output(self.enable, True)
      GPIO.output(self.forward, True)
      GPIO.output(self.reverse, False)

   # go forward (includes turning enable to HIGH)
   def reverse(self):
      if Wheel.DEBUG:
         print "reversing " + str(self)
      GPIO.output(self.reverse, True)
      GPIO.output(self.forward, True)

