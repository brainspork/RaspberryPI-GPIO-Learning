import RPi.GPIO as GPIO
import time

# Sets up for pin numbers (alt GPIO.BCM)
GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)

# True, False
in_list = [36, 32]

# Green, Red
out_list = [22, 40]

GPIO.setup(in_list, GPIO.IN)
GPIO.setup(out_list, GPIO.OUT)

questions = [
    ["Is 3 > 4?", False], 
    ["Is the sky blue?", True], 
    ["You can convert a int to a string in python with string concatination", False]
]
correct_count = 0

def validate_input(answer, actual):
    correct = answer == actual
    c = 0
    if correct:
        GPIO.output(22, True)
        c = 1
    else:
        GPIO.output(40, True)
    
    return c

for q in questions:
    answered = False

    print(q[0])

    while answered == False:
        true_in = GPIO.input(36)
        false_in = GPIO.input(32)

        if true_in == False:
            print('Pressed True')
            correct_count += validate_input(True, q[1])
            answered = True

            while true_in == False:
                true_in = GPIO.input(36)

        if false_in == False:
            print('Pressed False')
            correct_count += validate_input(False, q[1])
            answered = True

            while false_in == False:
                false_in = GPIO.input(32)

        if answered == True:
            time.sleep(1)
            GPIO.output(22, False)
            GPIO.output(40, False)

print("Quiz complete, score " + str(correct_count) + "/" + str(len(questions)))
GPIO.cleanup(in_list + out_list)