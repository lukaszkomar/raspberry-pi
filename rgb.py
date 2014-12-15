import RPi.GPIO as GPIO

GREEN = 18; 
BLUE  = 17; 

#GPIO.setmode(GPIO.BOARD);
GPIO.setmode(GPIO.BCM);

GPIO.setup(BLUE , GPIO.OUT);
GPIO.setup(GREEN, GPIO.OUT);

#GPIO.output(BLUE, 1);
#GPIO.output(BLUE, 1);

try:
    while(True):
        request = raw_input("_GB ");
        if (len(request) == 2):
            GPIO.output(GREEN, int(request[0]));
            GPIO.output(BLUE , int(request[1]));

except KeyboardInterrupt:
    GPIO.cleanup();
