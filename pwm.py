import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)

Motor1A = 31
Motor1B = 29
Motor1E = 33

Motor2A = 13
Motor2B = 11
Motor2E = 15

MOTOR_PWM_FREQ = 100

MOTORS = [Motor1A, Motor1B, Motor1E, Motor2A, Motor2B, Motor2E]

GPIO.setup(Motor1A,GPIO.OUT)
GPIO.setup(Motor1B,GPIO.OUT)
GPIO.setup(Motor1E,GPIO.OUT)

GPIO.setup(Motor2A,GPIO.OUT)
GPIO.setup(Motor2B,GPIO.OUT)
GPIO.setup(Motor2E,GPIO.OUT)

pwmM1_F = GPIO.PWM(Motor1A, MOTOR_PWM_FREQ) 
pwmM1_R = GPIO.PWM(Motor1B, MOTOR_PWM_FREQ)

dutyCycle = 0

pwmM1_F.start(dutyCycle)

# enable M1, init motor at OFF
GPIO.output(Motor1E, GPIO.HIGH)
GPIO.output(Motor1B, GPIO.LOW)

try:    
    while True:
            for dutyCycle in range(0,101,20):
                pwmM1_F.ChangeDutyCycle(dutyCycle)
                print(dutyCycle)
                time.sleep(0.5)
            for dutyCycle in range(95,0,-5):
                pwmM1_F.ChangeDutyCycle(dutyCycle)
                print(dutyCycle)
                time.sleep(0.1)
except KeyboardInterrupt:
        print("Ctrl C")

pwmM1_F.stop()
GPIO.cleanup
