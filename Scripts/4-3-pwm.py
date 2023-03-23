import RPi.GPIO as GPIO


GPIO.setmode(GPIO.BCM)

GPIO.setup( 3, GPIO.OUT)
GPIO.setup(21, GPIO.OUT)

p  = GPIO.PWM(3, 1000)
p. start(0)

p1 = GPIO.PWM(21, 1000)
p1.start(100)

try:
    while (True):
        dc = int(input("Enter the duty cycle \n"))
        p.ChangeDutyCycle(dc)
        p1.ChangeDutyCycle(dc)

        u = 3.3 * dc / 100
        GPIO.output(21, dc)
        print("The theoretical value of voltage is", u)
finally:
    p.ChangeDutyCycle(0)
    p1.ChangeDutyCycle(0)
    p.stop()
    p1.stop()