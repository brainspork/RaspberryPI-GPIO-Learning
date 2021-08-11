import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BOARD)
GPIO.setup(12, GPIO.IN)

while True:
    input_value = GPIO.input(12)
    print(input_value)
    if input_value == False:
        print('AUDIO?')
        while input_value == False:
            input_value = GPIO.input(12)
    else:
        print('NO AUDIO?')
        while input_value == True:
            input_value = GPIO.input(12)