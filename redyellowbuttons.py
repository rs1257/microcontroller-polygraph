'''
     
    yellow = 18
    red = 17
    
    
'''



def setupgpio():
    '''
    This function is used for setting up the GPIO pins on the pi
    
    this is required before using them
    '''
    import RPi.GPIO as GPIO
    
    
    GPIO.setmode(GPIO.BCM)

     
    GPIO.setup(17, GPIO.IN)
    GPIO.setup(18, GPIO.IN)
    


def yellowPressed():
    '''
    Will return True only when the yellow button is pressed
    '''
    import RPi.GPIO as GPIO
    
    if GPIO.input(18) == 0:
        return True
    else:
        return False
    
def redPressed():
    '''
    Will return True only when the red button is pressed
    '''
    import RPi.GPIO as GPIO
    
    if GPIO.input(17) == 0:
        return True
    else:
        return False
