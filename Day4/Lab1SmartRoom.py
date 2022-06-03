############################## RPi
#import RPi.GPIO as GPIO
#import threading

############ Initialization
LED_pin = 14
FAN_pin = 12
#GPIO.setmode(GPIO.BOARD)
#GPIO.setup(LED_pin, GPIO.OUT)
#GPIO.setup(FAN_pin, GPIO.OUT)
#FAN_pwm_handler = GPIO.pwm(FAN_pin, 50)
#FAN_pwm_handler.start(0)

############ functions
def turnOnLed():
	global LED_pin
	#GPIO.output(LED_pin, GPIO.HIGH)
	print("Led on")
	
def turnOffLed():
	global LED_pin
	#GPIO.output(LED_pin, GPIO.LOW)
	print("Led off")


def ledLevel1():
	global FAN_pwm_handler
	#FAN_pwm_handler.ChangeDutyCycle(25)
	print("DutyCycle(0.25)")
	
def ledLevel2():
	global FAN_pwm_handler
	#FAN_pwm_handler.ChangeDutyCycle(50)
	print("DutyCycle(0.5)")

def ledLevel3():
	global FAN_pwm_handler
	#FAN_pwm_handler.ChangeDutyCycle(100)
	print("DutyCycle(1)")

def closeFan():
	global FAN_pwm_handler
	#FAN_pwm_handler.ChangeDutyCycle(0)
	print("DutyCycle(0)")

def handleTime():
	global entry_time
	requiredTime = entry_time.get()
	#timerHandler = threading.Timer(requiredTime, closeFan)
	#timerHandler.start()
	print("close the fan after ", requiredTime, "sec")
	
	
############################## GUI	
import tkinter	

window = tkinter.Tk()
window.title("Smart Room using RPi")
#window.geometry("300x260")
	
label_light = tkinter.Label(window, text="Light: " )
label_light.grid(row=1, column=1)
Btn_turnOn = tkinter.Button(window, text="ON", bg="green", command=turnOnLed )
Btn_turnOn.grid(row=1, column=2)
Btn_turnOff = tkinter.Button(window, text="OFF", bg="red", command=turnOffLed )
Btn_turnOff.grid(row=1, column=3)

label_fan = tkinter.Label(window, text="Fan: " )
label_fan.grid(row=2, column=1)
Btn_lowLevel = tkinter.Button(window, text="Low", bg="green", command=ledLevel1 )
Btn_lowLevel.grid(row=2, column=2)
Btn_mediumLevel = tkinter.Button(window, text="Medium", bg="green", command=ledLevel2 )
Btn_mediumLevel.grid(row=2, column=3)
Btn_highLevel = tkinter.Button(window, text="High", bg="green", command=ledLevel3 )
Btn_highLevel.grid(row=2, column=4)
Btn_fanOff = tkinter.Button(window, text="OFF", bg="red", command=closeFan )
Btn_fanOff.grid(row=2, column=5)

label_time = tkinter.Label(window, text="Time: " )
label_time.grid(row=3, column=1)
entry_time = tkinter.Entry(window)
entry_time.grid(row=3, column=2)
Btn_enterTime = tkinter.Button(window, text="Enter", bg="green", command=handleTime )
Btn_enterTime.grid(row=4, column=2)

Btn_close = tkinter.Button(window, text="Close", bg="red", command=exit )
Btn_close.grid(row=5, column=5)


window.mainloop()
		
