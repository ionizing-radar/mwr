import RPi.GPIO as GPIO
from time import sleep

class Wheel(object):
   'Generate demand signals using and L293D (or similiar) motor driver'
   # Wheel assumes you're using a L293D motor driver, so you have to have an enable signal and at least one of fwd/rev demand signals.

   DEBUG = False

   def __init__ (self, enable_pin, forward_pin, reverse_pin):
      # set interval variables from parameters
      self.enable_pin = enable_pin
      self.forward_pin = forward_pin
      self.reverse_pin = reverse_pin
      # debug output
      if Wheel.DEBUG:
         print "Initializing "+ str(self)+" with:"
         print "   enable_pin: " + str(enable_pin) + " as " + str(self.enable_pin)
         print "   forward_pin: "+ str(forward_pin) + " as " + str(self.forward_pin)
         print "   reverse_pin: "+ str(reverse_pin) + " as " + str(self.reverse_pin)
      # initialize GPIO to do things
      GPIO.setup(self.enable_pin, GPIO.OUT)
      GPIO.setup(self.forward_pin, GPIO.OUT)
      GPIO.setup(self.reverse_pin, GPIO.OUT)
      # enable motor
      GPIO.output(self.enable_pin, True)

   def test_func(self):
      if Wheel.DEBUG:
         print "test_func " + str(self)

   # stop the motor by turning off the enable signal
   def stop(self):
      if Wheel.DEBUG:
         print "stopping " + str(self)
      GPIO.output(self.enable_pin, False)
      return

   # go forward (includes turning enable to HIGH)
   def start(self):
      if Wheel.DEBUG:
         print "starting " + str(self)
         print self.enable_pin
         print self.forward_pin
         print self.reverse_pin
      GPIO.output(self.enable_pin, True)
      GPIO.output(self.forward_pin, True)
      GPIO.output(self.reverse_pin, False)
      return

   # go forward (includes turning enable to HIGH)
   def reverse(self):
      if Wheel.DEBUG:
         print "reversing " + str(self)
      GPIO.output(self.enable_pin, True)
      GPIO.output(self.reverse_pin, True)
      GPIO.output(self.forward_pin, False)
      return

