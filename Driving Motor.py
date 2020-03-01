import RPi.GPIO as GPIO
from time import sleep

EN1, IN1, IN2 = 3, 5, 7
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
GPIO.setup(EN1, GPIO.OUT, initial = GPIO.HIGH)
GPIO.setup(IN1, GPIO.OUT, initial = GPIO.HIGH)
GPIO.setup(IN2, GPIO.OUT, initial = GPIO.HIGH)
p = GPIO.PWM(EN1, 100)
'''
while True:
    p.start(30)
    GPIO.output(IN1, 1)
    GPIO.output(IN2, 0)
    GPIO.output(EN1, 1)
    sleep(3)
    GPIO.output(IN1, 0)
    GPIO.output(IN2, 1)
    GPIO.output(EN1, 1)
    sleep(3)
'''
