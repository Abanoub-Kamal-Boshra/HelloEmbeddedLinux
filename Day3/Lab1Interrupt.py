import RPi.GPIO as GPIO

LED_pin = 14
SW_pin = 12
GPIO.setmode(GPIO.BOARD)
GPIO.setup(LED_pin, GPIO.OUT)
GPIO.setup(SW_pin, GPIO.IN, pull_up_down=GPIO.PUD.UP)


def ledOn(argument_pin_num):
	GPIO.output(LED_pin, GPIO.HIGH)
	
GPIO.add_event_detect(SW_pin, GPIO.FALLING, callback=ledOn)

while True:
	pass