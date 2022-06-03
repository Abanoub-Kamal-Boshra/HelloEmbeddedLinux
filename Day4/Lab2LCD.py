import RPi.GPIO as GPIO
import requests
from RPLCD import CharLCD


lcd = CharLCD(cols=16, rows=2,
                pin_rw=None,
                pin_rs=7,
                pin_e=8,
                pins_data=[25,24,23,18],
                numbering_mode=GPIO.BCM)
				
				
while True:
	data = requests.get("http://akamal.pythonanywhere.com/")
	if data.text == "1":
		lcd.clear()
		lcd.cursor_pos = (0, 0)
		lcd.write_string("Hello Abanoub")
		lcd.cursor_pos = (1, 0)
		lcd.write_string('This is line 2')
	else:
		lcd.clear()
		lcd.cursor_pos = (0, 0)
		lcd.write_string("incorrect sentence")