import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)
GPIO.setup(11, GPIO.OUT)

def flash():
    GPIO.output(11, True)
    time.sleep(0.1)
    GPIO.output(11, False)

def flashTwice():
    flash()
    time.sleep(0.1)
    flash()

def flashFourTimes():
    flashTwice()
    time.sleep(0.1)
    flashTwice()

while True:
    flashTwice()
    time.sleep(1)
    flash()
    time.sleep(1)
    flashFourTimes()
    time.sleep(1)
