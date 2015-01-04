import RPi.GPIO as GPIO
import time

D1_A  = 0
D1_B  = 0
D1_C  = 17
D1_D  = 18
D1_E  = 27
D1_F  = 22
D1_G  = 0
D1_DP = 0

DIOD_ON = 0
DIOD_OFF= 1

sleeptime = 0.200
frameSpeed = 1

#GPIO.setmode(GPIO.BOARD)
GPIO.setmode(GPIO.BCM)

GPIO.setup(D1_C , GPIO.OUT)
GPIO.setup(D1_D , GPIO.OUT)
GPIO.setup(D1_E , GPIO.OUT)
GPIO.setup(D1_F , GPIO.OUT)

frame = {
    D1_C: DIOD_ON,
    D1_D: DIOD_ON,
    D1_E: DIOD_ON,
    D1_F: DIOD_ON,
}

try:
    while True:
        if sleeptime > 0.011:
            sleeptime -= 0.010
        else:
            if sleeptime > 0.002:
                sleeptime -= 0.001 

        print sleeptime

        for i in range(frameSpeed):
            for pin, val in frame.iteritems():
                GPIO.output(pin, val)
                time.sleep(sleeptime)
                GPIO.output(pin, DIOD_OFF)

except KeyboardInterrupt:
    GPIO.cleanup()
