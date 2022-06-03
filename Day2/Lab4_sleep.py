import RPi.GPIO as GPIO
from time import sleep

GPIO.setmode(GPIO.BOARD)
GPIO.setup(14, GPIO.OUT)


while True:
	GPIO.output(14, GPIO.LOW)
	sleep(1)

	GPIO.output(14, GPIO.HIGH)
	sleep(1)