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

sleeptime = 1000
frameSpeed = 1

GPIO.cleanup()

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
        if sleeptime > 10:
            sleeptime = sleeptime - 10

        for i in range(frameSpeed):
            for pin, val in frame.iteritems():
                GPIO.output(pin, val)
                time.sleep(sleeptime/1000)
                GPIO.output(pin, DIOD_OFF)


except KeyboardInterrupt:
    GPIO.cleanup()
