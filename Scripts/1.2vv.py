import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)

GPIO.setup(22, GPIO.OUT)
GPIO.setup(14, GPIO.IN)


GPIO.output(22, GPIO.input(14))
time.sleep(6)

GPIO.output(22, 0)
GPIO.cleanup()