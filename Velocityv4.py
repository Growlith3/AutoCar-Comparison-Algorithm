import RPi.GPIO as GPIO
from time import*
from math import*

#distance traveled
distance = 0.00
#kilometers oer hour
kph = float(0)
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
		distanceMiles = distance *.621371 
		return kph,mph

def init_interrupt():
	GPIO.add_event_detect(pin, GPIO.FALLING, callback = tElapsed, bouncetime = 20)
try:
    if __name__ == '__main__':
            init_GPIO()
            init_interrupt()
            while True:
                    velocity(20)	
                    print('{0:.0f}-RPM     {1:.0f}-KMH     distance traveled:{2:.2f}m     rotation:{3}'.format(rpm,kph,distance,rotation))
                    sleep(0.1)
except KeyboardInterrupt:
    GPIO.cleanup()
