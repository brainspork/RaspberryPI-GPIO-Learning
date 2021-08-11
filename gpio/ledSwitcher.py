import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BOARD)
# red
GPIO.setup(11, GPIO.OUT)
# green
GPIO.setup(16, GPIO.OUT)
# blue
GPIO.setup(15, GPIO.OUT)
# button
GPIO.setup(22, GPIO.IN)

def redOn():
    GPIO.output(16, False)
    GPIO.output(15, False)
    GPIO.output(11, True)

def greenOn():
    GPIO.output(11, False)
    GPIO.output(15, False)
    GPIO.output(16, True)

def blueOn():
    GPIO.output(11, False)
    GPIO.output(16, False)
    GPIO.output(15, True)

def allOff():
    GPIO.output(11, False)
    GPIO.output(16, False)
    GPIO.output(15, False)

options = {
    0: blueOn,
    1: greenOn,
    2: redOn
}

count = 0
while True:
    input_value = GPIO.input(22)

    if input_value == False:
        count += 1
        options[count % 3]()
        while input_value == False:
            input_value = GPIO.input(22)
    else:
        allOff()
        while input_value == True:
            input_value = GPIO.input(22)
