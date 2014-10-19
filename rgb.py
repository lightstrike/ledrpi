import RPi.GPIO as GPIO
import time


GPIO.setmode(GPIO.BCM)

greenPin=12
redPin=23
bluePin=16

RGB = [redPin, greenPin, bluePin]
for pin in RGB:
	GPIO.setup(pin, GPIO.OUT)
	GPIO.output(pin, 1)


def shine(red=1, green=1, blue=1, speed=1):
	GPIO.output(redPin,1*red) 
	GPIO.output(greenPin,1*green) 
	GPIO.output(bluePin,1*blue) 
	time.sleep(0.5*speed)
	GPIO.output(redPin,0) 
	GPIO.output(greenPin,0) 
	GPIO.output(bluePin,0) 

try:
	while True:
		color = raw_input('Enter RGB (ex. 100 is red) --> ')
		if len(color) == 3:
			red = int(color[0])
			green = int(color[1])
			blue = int(color[2])
			speed = int(raw_input('Choose speed (1-5, 1 fastest, 5 slowest) '))

			shine(red, green, blue, speed)	
except KeyboardInterrupt:
	GPIO.cleanup()
