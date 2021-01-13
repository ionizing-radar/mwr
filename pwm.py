import RPi.GPIO as GPIO
from time import sleep

GPIO.setmode(GPIO.BOARD)

Motor1A = 31
Motor1B = 29
Motor1E = 33

Motor2A = 13
Motor2B = 11
Motor2E = 15

MOTORS = [Motor1A, Motor1B, Motor1E, Motor2A, Motor2B, Motor2E]

GPIO.setup(Motor1A,GPIO.OUT)
GPIO.setup(Motor1B,GPIO.OUT)
GPIO.setup(Motor1E,GPIO.OUT)

GPIO.setup(Motor2A,GPIO.OUT)
GPIO.setup(Motor2B,GPIO.OUT)
GPIO.setup(Motor2E,GPIO.OUT)

pwmM1_F = GPIO.PWM(Motor1A, GPIO.OUT) 
pwmM1_R = GPIO.PWM(Motor1B, GPIO.OUT)

dutyCycle = 0

pwmM1_F.start(dc)

# enable M1, init motor at OFF
GPIO.output(Motor1E, GPIO.HIGH)
GPIO.output(Motor1B, GPIO.LOW)

try:    
    while True:
            for dutyCycle in range(0,101,5):
                pwmM1_F.ChangeDutyCycle(dutyCycle)
                print(dutyCycle)
                time.sleep(0.05)
            for dutyCycle in range(95,0,-5):
                pwmM1_F.ChangeDutyCycle(dutyCycle)
                print(dutyCycle)
                time.sleep(0.05)
except KeyboardInterrupt:
        print("Ctrl C")

pwn.stop()
GPIO.cleanup
