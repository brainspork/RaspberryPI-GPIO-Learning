import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BOARD)
GPIO.setup(12, GPIO.IN)
GPIO.setup(11, GPIO.OUT)

while True:
    input_value = GPIO.input(12)

    if input_value == False:
        print("The button was pressed")
        GPIO.output(11, True)

        while input_value == False:
            input_value = GPIO.input(12)
    else:
        GPIO.output(11, False)
        while input_value == True:
            input_value = GPIO.input(12)

# while True:
#     input_value = GPIO.input(12)
#     if input_value == False:
#         print("The button has been pressed.")
#         while input_value == False:
#             input_value = GPIO.input(12)