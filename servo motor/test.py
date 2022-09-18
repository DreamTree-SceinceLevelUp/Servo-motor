import RPi.GPIO as GPIO
import time

servo = 18
hz = 50

GPIO.setmode(GPIO.BCM)
GPIO.setup(servo, GPIO.OUT)

pwm = GPIO.PWM(servo,hz)
pwm.start(3.0)
time.sleep(2)

pwm.ChangeDutyCycle(1.5/20*100)
time.sleep(2)

pwm.ChangeDutyCycle(2.5/20*100)
time.sleep(2)

pwm.stop()
GPIO.cleanup()