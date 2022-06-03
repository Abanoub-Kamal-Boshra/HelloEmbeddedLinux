import tkinter
import RPi.GPIO as GPIO

window = tkinter.Tk()
window.title("Toggle pin of RPi")
window.geometry("200x260")

LED_state = 0
LED_pin

def init():
	global LED_pin
	LED_pin = int(entry_pinNumber.get())
	GPIO.setmode(GPIO.BOARD)
	GPIO.setup(LED_pin, GPIO.OUT)
	GPIO.output(LED_pin, GPIO.LOW)

def toggleLed():
	global LED_state
	global LED_pin
	LED_pin = int(entry_pinNumber.get())
	LED_state ^= 1 	#toggle the variable
	if LED_state == 0:
		GPIO.output(LED_pin, GPIO.HIGH)
	elif LED_state == 1:
		GPIO.output(LED_pin, GPIO.LOW
	else:
		print("invalid input")
		
		
label_pinNumber = tkinter.Label(window, text="Pin: " )
label_pinNumber.grid(row=1, column=1)
entry_pinNumber = tkinter.Entry(window)
entry_pinNumber.grid(row=1, column=2)
#add place holder in entry
entry_pinNumber.insert(0, "Enter the BOARD pin number")

Btn_config = tkinter.Button(window, text="Config", bg="blue", command=init )
Btn_config.grid(row=2, column=1)
	
Btn_toggle = tkinter.Button(window, text="Toggle", bg="green", command=toggleLed )
Btn_toggle.grid(row=2, column=2)

Btn_close = tkinter.Button(window, text="Close", bg="red", command=exit )
Btn_close.grid(row=3, column=2)


window.mainloop()
		
