import RPi.GPIO as GPIO
from time import*
from math import*

#distance traveled
distance = 0.00
distanceMiles = 0.00
#kilometers per hour
kph = float(0)
#miles per hour
mph = float(0)
# rotations per minute
rpm = 0
# time 
t = 0
# GPIO pin being used
pin = 16
#number of roatations
rotation = 0
# timer for logging
timer = time()
# to allow an easier time logging the numbers
check = 0

#Initializes the GPIO inputs
def init_GPIO():                                        
        GPIO.setmode(GPIO.BCM)
        GPIO.setwarnings(False)
        GPIO.setup(pin,GPIO.IN,GPIO.PUD_UP)

# calculates the time between each roation
def tElapsed(channel):                          
        global rotation
        global timer
        global t
        rotation += 1                                                            
        t = time() - timer              
        timer = time()
        
# calculates the velocity using radius as a parameter
# radius will be in cm
def velocity(r):
        global rotation
        global t
        global rpm
        global rotationDist
        global distance
        global distanceMiles
        global kph
        global mph
        if t !=0:                                                       
                rpm = 1/t * 60
                #Standard equation for circumference
                circumference = (2*pi)*r
                #Converts wheel radius to Km
                rotationDist = circumference/100000
                #Calculates Kilometers per hour
                kph = (rotationDist / t)* 3600
                #optional print for conversion to miles per hour
                mph = kph *.621371
                # gives the distance traveled in Km
                distance = (rotationDist*rotation)*1000
                #optional print for distance in miles
                distanceMiles = distance *.621371/1000 
                return kph,mph

def init_interrupt():
        GPIO.add_event_detect(pin, GPIO.FALLING, callback = tElapsed, bouncetime = 20)
try:
    if __name__ == '__main__':
            init_GPIO()
            init_interrupt()
            while True:
                velocity(25.4)
                if (check == 0):
                        text = open("measurements", "w").write("{0:.0f}, {1:.0f}, {2:.0f}, {3:.3f}, {4:4f}, {5}\n".format(rotation, rpm, kph, mph, distance, distanceMiles))
                        check += 1
                else:
                        text = open("measurements", "a").write("{0:.0f}, {1:.0f}, {2:.0f}, {3:.3f}, {4:4f}, {5}\n".format(rotation, rpm, kph, mph, distance, distanceMiles))
##                print('{0:.0f}-RPM     {1:.0f}-KMH     {2:.0f}-MPH     distance:{3:.3f}m     distanceMiles:{4:4f}miles     rotation:{5}'.format(rpm,kph,mph,distance,distanceMiles,rotation))
                sleep(0.1)
except KeyboardInterrupt:
    GPIO.cleanup()
