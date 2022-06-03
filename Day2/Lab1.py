import tkinter
import RPi.GPIO as GPIO

window = tkinter.Tk()
window.title("Toggle pin of RPi")
window.geometry("200x260")

GPIO.setmode(GPIO.BOARD)
GPIO.setup(14, GPIO.OUT)
LED_state = 0
LED_pin = 14

def toggleLed():
	global LED_state
	global LED_pin
	#toggle the variable
	LED_state ^= 1 
	if LED_state == 0:
		GPIO.output(LED_pin, GPIO.HIGH)
	elif LED_state == 1:
		GPIO.output(LED_pin, GPIO.LOW
	else:
		print("invalid input")
		
	
Btn_toggle = tkinter.Button(window, text="Toggle", bg="blue", command=toggleLed )
Btn_toggle.grid(row=3, column=2)

window.mainloop()