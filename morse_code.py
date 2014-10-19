import RPi.GPIO as GPIO
import time


CODE = {' ': ' ',
        "'": '.----.',
        '(': '-.--.-',
        ')': '-.--.-',
        ',': '--..--',
        '-': '-....-',
        '.': '.-.-.-',
        '/': '-..-.',
        '0': '-----',
        '1': '.----',
        '2': '..---',
        '3': '...--',
        '4': '....-',
        '5': '.....',
        '6': '-....',
        '7': '--...',
        '8': '---..',
        '9': '----.',
        ':': '---...',
        ';': '-.-.-.',
        '?': '..--..',
        'A': '.-',
        'B': '-...',
        'C': '-.-.',
        'D': '-..',
        'E': '.',
        'F': '..-.',
        'G': '--.',
        'H': '....',
        'I': '..',
        'J': '.---',
        'K': '-.-',
        'L': '.-..',
        'M': '--',
        'N': '-.',
        'O': '---',
        'P': '.--.',
        'Q': '--.-',
        'R': '.-.',
        'S': '...',
        'T': '-',
        'U': '..-',
        'V': '...-',
        'W': '.--',
        'X': '-..-',
        'Y': '-.--',
        'Z': '--..',
        '_': '..--.-'}

greenPin=17
redPin=22
GPIO.setmode(GPIO.BCM)
GPIO.setup(greenPin,GPIO.OUT)
GPIO.setup(redPin,GPIO.OUT)

def dot(speed=1): 
	GPIO.output(greenPin,1)
	time.sleep(0.1*speed)
	GPIO.output(greenPin,0)
	time.sleep(0.1*speed)

def dash(speed=1):
	GPIO.output(redPin,1)
	time.sleep(0.3*speed)
	GPIO.output(redPin,0)
	time.sleep(0.1*speed)

while True:
	input = raw_input('What would you like to send? ')
	speed = int(raw_input('Choose speed (1-5, 1 fastest, 5 slowest) '))
	for letter in input:
			for symbol in CODE[letter.upper()]:
				if symbol == '-':
					dash(speed)
				elif symbol == '.':
					dot(speed)
				else:
					time.sleep(0.3*speed)
			time.sleep(0.3*speed)
