import RPi.GPIO as GPIO
from time import sleep

GPIO.setmode(GPIO.BOARD)

LED = 37

GPIO.setup(LED,GPIO.OUT)

GPIO.output(LED,GPIO.HIGH)

sleep(1)

GPIO.output(LED,GPIO.LOW)
