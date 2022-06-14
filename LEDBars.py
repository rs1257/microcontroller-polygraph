def setup():
    import RPi.GPIO as GPIO
    GPIO.setmode(GPIO.BCM)
    
    L0 = 5
    L1 = 6
    L2 = 12
    L3 = 13
    L4 = 16
    L5 = 19
    L6 = 20
    L7 = 26
    
    
    GPIO.setup(L0, GPIO.OUT)
    GPIO.setup(L1, GPIO.OUT)
    GPIO.setup(L2, GPIO.OUT)
    GPIO.setup(L3, GPIO.OUT)
    GPIO.setup(L4, GPIO.OUT)
    GPIO.setup(L5, GPIO.OUT) 
    GPIO.setup(L6, GPIO.OUT)
    GPIO.setup(L7, GPIO.OUT)

 
#light up the bar chart to the correct value
def bars(value):
    import RPi.GPIO as GPIO
    L0 = 5
    L1 = 6
    L2 = 12
    L3 = 13
    L4 = 16
    L5 = 19
    L6 = 20
    L7 = 26
    
    if(value>=25):
        GPIO.output(L0, 1)
        if(value>=50):
            GPIO.output(L1, 1)
            if(value>=75):
                GPIO.output(L2, 1)
                if(value>=100):
                    GPIO.output(L3, 1)
                    if(value>=125):
                        GPIO.output(L4, 1)
                        if(value>=150):
                            GPIO.output(L5, 1)
                            if(value>=175):
                                GPIO.output(L6, 1)
                                if(value>=200):
                                    GPIO.output(L7, 1)
                                                           
    if(value<200):
        GPIO.output(L7, 0)
        if(value<175):
            GPIO.output(L6, 0)
            if(value<150):
                GPIO.output(L5, 0)
                if(value<125):
                    GPIO.output(L4, 0)
                    if(value<100):
                        GPIO.output(L3, 0)
                        if(value<75):
                            GPIO.output(L2, 0)
                            if(value<50):
                                GPIO.output(L1, 0)
                                if(value<25):
                                    GPIO.output(L0, 0)
                        
