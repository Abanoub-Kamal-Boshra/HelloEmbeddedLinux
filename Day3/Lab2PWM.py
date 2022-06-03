#import RPi.GPIO as GPIO


def init():
	global LED_pwm_controller
	LED_pin = int(entry_pinNumber.get())
	#GPIO.setmode(GPIO.BOARD)
	#GPIO.setup(LED_pin, GPIO.OUT)
	#LED_pwm_controller = GPIO.pwm(LED_pin, 50)
	#LED_pwm_controller.start(0)

def ledLevel1():
	global LED_pwm_controller
	#LED_pwm_controller.ChangeDutyCycle(25)
	print("DutyCycle(0.25)")
	
def ledLevel2():
	global LED_pwm_controller
	#LED_pwm_controller.ChangeDutyCycle(50)
	print("DutyCycle(0.5)")

def ledLevel3():
	global LED_pwm_controller
	#LED_pwm_controller.ChangeDutyCycle(100)
	print("DutyCycle(1)")

	
############################## GUI	
import tkinter	

window = tkinter.Tk()
window.title("PWD of RPi")
window.geometry("300x260")
	
label_pinNumber = tkinter.Label(window, text="Pin: " )
label_pinNumber.grid(row=1, column=1)
entry_pinNumber = tkinter.Entry(window)
entry_pinNumber.grid(row=1, column=2)
#add place holder in entry
entry_pinNumber.insert(0, 14)

Btn_config = tkinter.Button(window, text="Config", bg="blue", command=init )
Btn_config.grid(row=1, column=3)
	
Btn_toggle = tkinter.Button(window, text="Level1", bg="green", command=ledLevel1 )
Btn_toggle.grid(row=2, column=1)
Btn_toggle = tkinter.Button(window, text="Level2", bg="green", command=ledLevel2 )
Btn_toggle.grid(row=2, column=2)
Btn_toggle = tkinter.Button(window, text="Level3", bg="green", command=ledLevel3 )
Btn_toggle.grid(row=2, column=3)

Btn_close = tkinter.Button(window, text="Close", bg="red", command=exit )
Btn_close.grid(row=3, column=3)


window.mainloop()
		
