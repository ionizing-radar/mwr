import RPi.GPIO as GPIO
import time

class MotorController:

    MOTOR_PWM_FREQ = 100

    Motor1A = None
    Motor1B = None
    Motor1E = None
    Motor2A = None
    Motor2B = None
    Motor2E = None
    Motors = None


    motor1_forward = None
    motor1_reverse = None
    motor2_forward = None
    motor2_reverse = None
    def __init__(self, Motor1A, Motor1B, Motor1E, Motor2A, Motor2B, Motor2E):
        # RUSSEL 1.0 used this pinout:
        #   Motor1A=31, Motor1B=29, Motor1E=33, Motor2A=13 ,Motor2B=11, Motor2E=15
        # GPIO pin definitions
        GPIO.setmode(GPIO.BOARD)
        self.Motor1A = Motor1A
        self.Motor1B = Motor1B
        self.Motor1E = Motor1E
        self.Motor2A = Motor2A
        self.Motor2B = Motor2B
        self.Motor2E = Motor2E        
        self.MOTORS = [Motor1A, Motor1B, Motor1E, Motor2A, Motor2B, Motor2E]
        for motor in self.MOTORS:
            GPIO.setup(motor,GPIO.OUT)       

        self.motor1_forward = GPIO.PWM(self.Motor1A, MotorController.MOTOR_PWM_FREQ) 
        self.motor1_reverse = GPIO.PWM(self.Motor1B, MotorController.MOTOR_PWM_FREQ)

        self.motor2_forward = GPIO.PWM(self.Motor2A, MotorController.MOTOR_PWM_FREQ) 
        self.motor2_reverse = GPIO.PWM(self.Motor2B, MotorController.MOTOR_PWM_FREQ)

    def __del__(self):
        # stop all the motors
        self.motor1_forward.stop()
        self.motor1_reverse.stop()
        self.motor2_reverse.stop()
        self.motor2_forward.stop()
        # set the GPIO free, to roam in the wild surviving on stray voltage and kind strangers
        GPIO.cleanup()

    def dothings(self):
        print("doing a thing!")

    # helper function to stop motors, directly calls setMotor with 0's as inputs
    def stop(self):
        self.setMotor()

    # set speed of motor, assumes using L293 driver
    #  - motorX_forward and motorX_reverse shouldn't be both be on as the +/- motor terminals
    def setMotor(self, power=0, motor1=0, motor2=0):
        print("setMotor ({0},{1},{2})".format(power, motor1, motor2))
        if (power > 1): power == 1
        power *= 100
        if (power == 0):
            GPIO.output(self.Motor1E,GPIO.LOW)
            self.motor1_forward.stop()
            self.motor1_reverse.stop()
            GPIO.output(self.Motor2E,GPIO.LOW)
            self.motor2_forward.stop()
            self.motor2_reverse.stop()
            return
        if (motor1 == 0):            
            GPIO.output(self.Motor1E,GPIO.LOW)
            self.motor1_forward.stop()
            self.motor1_reverse.stop()
        elif (motor1 > 0):            
            GPIO.output(self.Motor1E,GPIO.HIGH)
            self.motor1_forward.start(power*motor1)
            self.motor1_reverse.stop()
        elif (motor1 < 1):            
            GPIO.output(self.Motor1E,GPIO.HIGH)
            self.motor1_reverse.start(abs(power*motor1))
            self.motor1_forward.stop()
        if (motor2 == 0):
            GPIO.output(self.Motor2E,GPIO.LOW)
            self.motor2_forward.stop()
            self.motor2_reverse.stop()
        elif (motor2 > 0):
            GPIO.output(self.Motor2E,GPIO.HIGH)
            self.motor2_forward.start(power*motor2)
            self.motor2_reverse.stop()
        elif (motor2 < 1):
            GPIO.output(self.Motor2E,GPIO.HIGH)
            self.motor2_reverse.start(abs(power*motor2))
            self.motor2_forward.stop()


# # enable M1, init motor at OFF
# GPIO.output(Motor1E, GPIO.HIGH)
# GPIO.output(Motor1B, GPIO.LOW)

# try:    
#     while True:
#             for dutyCycle in range(0,101,20):
#                 motor1_forward.ChangeDutyCycle(dutyCycle)
#                 print(dutyCycle)
#                 time.sleep(0.5)
#             for dutyCycle in range(95,0,-5):
#                 motor1_forward.ChangeDutyCycle(dutyCycle)
#                 print(dutyCycle)
#                 time.sleep(0.1)
# except KeyboardInterrupt:
#         print("Ctrl C")

# motor1_forward.stop()
# GPIO.cleanup
