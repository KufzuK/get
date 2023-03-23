import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)


dac = [26, 19, 13, 6, 5, 11, 9 , 10]
GPIO.setup(dac, GPIO.OUT)


def decimal2binary(value):
 
    return [int(bit) for bit in bin(value)[2:].zfill(8)]

t = int(input("print the period of signal \n"))
sl = t / 512
try:
    while(True):
        for i in range(256):
            GPIO.output(dac, decimal2binary(i))
            time.sleep(sl)

        for i in range(254, -1, -1):
            GPIO.output(dac, decimal2binary(i))
            time.sleep(sl)



finally:
    GPIO.output(dac, 0)
    GPIO.cleanup()