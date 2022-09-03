import RPi.GPIO as GPIO
import time


class Servo():
    def __init__(self):
        self.GPIO = GPIO
        print('active init')

    def attach(self, pin, hz):
        self.GPIO.setmode(self.GPIO.BCM)
        self.GPIO.setup(pin, self.GPIO.OUT)
        self.pwm = GPIO.PWM(pin, hz)
        print('active attach')

    def start(self):
        self.pwm.start(0.52/20*100)
        print('active start')

    def end(self):
        self.pwm.stop()
        self.GPIO.cleanup()
        print('active end')

    def theta2duty(self, theta):
        print('active theta2duty')
        return (0.52+0.0075*theta)*5

    def write(self, theta):
        if theta > 270:
            raise ValueError('Theta must be less than 270')
        if theta < 0:
            raise ValueError('Theta must be more than 0')

        self.pwm.ChangeDutyCycle(self.theta2duty(theta))
        print('active write')
