import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)


dac = [26, 19, 13, 6, 5, 11, 9 , 10]
GPIO.setup(dac, GPIO.OUT)

def decimal2binary(value):
 
    return [int(bit) for bit in bin(value)[2:].zfill(8)]




try:
    while(True):
        a = input('print integer number in range 0 - 255 : \n')


        if a == 'q':
            break

        if not a.isnumeric():
            print("it's not an integer number, try again")
            continue

        a = int(a)
            

        if 0 <= a <= 255:
            GPIO.output(dac, decimal2binary(a))
            print("Max voltage is 3.3 v. Current voltage \
            is 3.3 *", a, "/ 255. Current voltage is", a * 3.3 / 255, "v")
 
            
            
            time.sleep(4)
            continue

            
        elif not (0 <= a <= 255):
            print("your number is out of range")
            continue

        


finally:
    GPIO.output(dac, 0)
    GPIO.cleanup()