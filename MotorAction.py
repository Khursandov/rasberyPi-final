import wiringpi


class MotorAction:
    IN1_PIN = 1
    IN2_PIN = 4
    IN3_PIN = 5
    IN4_PIN = 6
    MAX_SPEED = 35
    ECHO_PIN = 29
    TRIG_PIN = 28
    MIN_SPEED = 0
    SOFT_PWM_OUTPUT = 4
    OUTPUT = 1
    INPUT = 0

    def __init__(self):
        wiringpi.wiringPiSetup()
        pass

    def initDCMotor(self):
        wiringpi.softPwmCreate(self.IN1_PIN, self.MIN_SPEED, self.MAX_SPEED)
        wiringpi.softPwmCreate(self.IN2_PIN, self.MIN_SPEED, self.MAX_SPEED)
        wiringpi.softPwmCreate(self.IN3_PIN, self.MIN_SPEED, self.MAX_SPEED)
        wiringpi.softPwmCreate(self.IN4_PIN, self.MIN_SPEED, self.MAX_SPEED)
        wiringpi.pinMode(self.IN1_PIN, self.SOFT_PWM_OUTPUT)
        wiringpi.pinMode(self.IN2_PIN, self.SOFT_PWM_OUTPUT)
        wiringpi.pinMode(self.IN3_PIN, self.SOFT_PWM_OUTPUT)
        wiringpi.pinMode(self.IN4_PIN, self.SOFT_PWM_OUTPUT)

    def goForward(self):
        wiringpi.softPwmWrite(self.IN1_PIN, self.MAX_SPEED)
        wiringpi.softPwmWrite(self.IN2_PIN, self.MIN_SPEED)
        wiringpi.softPwmWrite(self.IN3_PIN, self.MAX_SPEED)
        wiringpi.softPwmWrite(self.IN4_PIN, self.MIN_SPEED)

    def  goRight(self):
        wiringpi.softPwmWrite(self.IN1_PIN, self.MAX_SPEED)
        wiringpi.softPwmWrite(self.IN2_PIN, self.MIN_SPEED)
        wiringpi.softPwmWrite(self.IN3_PIN, self.MIN_SPEED)
        wiringpi.softPwmWrite(self.IN4_PIN, self.MAX_SPEED)

    def goLeft(self):
        wiringpi.softPwmWrite(self.IN1_PIN, self.MIN_SPEED)
        wiringpi.softPwmWrite(self.IN2_PIN, self.MAX_SPEED)
        wiringpi.softPwmWrite(self.IN3_PIN, self.MAX_SPEED)
        wiringpi.softPwmWrite(self.IN4_PIN, self.MIN_SPEED)

    def stopDCMotor(self):

        wiringpi.softPwmStop(self.IN1_PIN)
        wiringpi.softPwmStop(self.IN2_PIN)
        wiringpi.softPwmStop(self.IN3_PIN)
        wiringpi.softPwmStop(self.IN4_PIN)

    def signalHandler(self, signal):
        self.stopDCMotor()
        exit(0)