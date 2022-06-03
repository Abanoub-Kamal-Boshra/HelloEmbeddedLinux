import RPi.GPIO as GPIO
import threading

GPIO.setmode(GPIO.BOARD)
GPIO.setup(14, GPIO.OUT)


LED_state = 0

def toggleLed():
	global LED_state
	LED_state ^= 1
	if LED_state:
		GPIO.output(14, GPIO.HIGH)
	else:
		GPIO.output(14, GPIO.LOW)
	
	timerHandler = threading.Timer(1, toggleLed)
	timerHandler.start()

	
timerHandler = threading.Timer(1, toggleLed)
timerHandler.start()

