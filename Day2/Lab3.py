import tkinter
import RPi.GPIO as GPIO

window = tkinter.Tk()
window.title("Toggle pin of RPi")
window.geometry("200x260")

LED_state = 0
LED_pin
SW_pin

def handleSW():
	while True:
		SW_state = not GPIO.input(SW_pin)
		if SW_state:
			GPIO.output(LED_pin, GPIO.HIGH)
		else:
			GPIO.output(LED_pin, GPIO.LOW)

def init():
	global LED_pin
	global SW_pin
	LED_pin = int(entry_pinNumber.get())
	SW_pin = int(entry_swPinNumber.get())
	GPIO.setmode(GPIO.BOARD)
	
	GPIO.setup(LED_pin, GPIO.OUT)
	GPIO.output(LED_pin, GPIO.LOW)
	
	GPIO.setup(SW_pin, GPIO.IN, pull_up_down=GPIO.PUD_UP)
	
	handleSW()
	


label_pinNumber = tkinter.Label(window, text="Pin: " )
label_pinNumber.grid(row=1, column=1)
entry_pinNumber = tkinter.Entry(window)
entry_pinNumber.grid(row=1, column=2)
#add place holder in entry
entry_pinNumber.insert(0, "Enter the Led pin number")

label_swPinNumber = tkinter.Label(window, text="Pin: " )
label_swPinNumber.grid(row=2, column=1)
entry_swPinNumber = tkinter.Entry(window)
entry_swPinNumber.grid(row=2, column=2)
#add place holder in entry
entry_swPinNumber.insert(0, "Enter the SW pin number")

Btn_config = tkinter.Button(window, text="Config", bg="blue", command=init )
Btn_config.grid(row=2, column=1)
	

Btn_close = tkinter.Button(window, text="Close", bg="red", command=exit )
Btn_close.grid(row=3, column=2)


window.mainloop()
		
