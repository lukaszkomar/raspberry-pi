import RPi.GPIO as GPIO
from datetime import time

GREEN = 18
BLUE  = 17

#GPIO.setmode(GPIO.BOARD)
GPIO.setmode(GPIO.BCM)

GPIO.setup(BLUE , GPIO.OUT)
GPIO.setup(GREEN, GPIO.OUT)

#GPIO.output(BLUE, 1);
#GPIO.output(BLUE, 1);

try:
    while True:
        GPIO.output(GREEN, 1)
        time.sleep(2)
        GPIO.output(GREEN, 0)
        GPIO.output(BLUE , 1)
        time.sleep(2)
        GPIO.output(BLUE , 0)

except KeyboardInterrupt:
    GPIO.cleanup()
