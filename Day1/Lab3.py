import tkinter
window = tkinter.Tk()
window.title("AVR Configuration")
window.geometry("200x260")

DDRvalue= "00000000"

def generateDDR():
    print("DDRA=0b"+DDRvalue)
    
def generatePin0():
    global pin0
    global DDRvalue
    if pin0.get() == "0":
        DDRvalue = DDRvalue[:7] + "0"
    else:
        DDRvalue = DDRvalue[:7] + "1"

def generatePin1():
    global pin1
    global DDRvalue
    if pin1.get() == "0":
        DDRvalue = DDRvalue[:6] +"0" + DDRvalue[7:]
    else:
        DDRvalue = DDRvalue[:6] +"1" + DDRvalue[7:]

def generatePin2():
    global pin2
    global DDRvalue
    if pin2.get() == "0":
        DDRvalue = DDRvalue[:5] +"0" + DDRvalue[6:]
    else:
        DDRvalue = DDRvalue[:5] +"1" + DDRvalue[6:]

def generatePin3():
    global pin3
    global DDRvalue
    if pin3.get() == "0":
        DDRvalue = DDRvalue[:4] +"0" + DDRvalue[5:]
    else:
        DDRvalue = DDRvalue[:4] +"1" + DDRvalue[5:]
 

def generatePin4():
    global pin4
    global DDRvalue
    if pin4.get() == "0":
        DDRvalue = DDRvalue[:3] +"0" + DDRvalue[4:]
    else:
        DDRvalue = DDRvalue[:3] +"1" + DDRvalue[4:]

def generatePin5():
    global pin5
    global DDRvalue
    if pin5.get() == "0":
        DDRvalue = DDRvalue[:2] +"0" + DDRvalue[3:]
    else:
        DDRvalue = DDRvalue[:2] +"1" + DDRvalue[3:]
        
def generatePin6():
    global pin6
    global DDRvalue
    if pin6.get() == "0":
        DDRvalue = DDRvalue[:1] +"0" + DDRvalue[2:]
    else:
        DDRvalue = DDRvalue[:1] +"1" + DDRvalue[2:]       

def generatePin7():
    global pin7
    global DDRvalue
    if pin7.get() == "0":
        DDRvalue = "0" + DDRvalue[1:]
    else:
        DDRvalue = "1" + DDRvalue[1:]

label_port = tkinter.Label(window, text="PORTA" )
label_port.grid(row=1, column=2)

pin0 = tkinter.StringVar()
pin0.set("0")
label_pin0 = tkinter.Label(window, text="Pin0:  " )
label_pin0.grid(row=2, column=1)
radio_pin0input = tkinter.Radiobutton(window, text="input", variable=pin0, value="0", command=generatePin0)
radio_pin0input.grid(row=2, column=2)
radio_pin0output = tkinter.Radiobutton(window, text="output", variable=pin0, value="1", command=generatePin0)
radio_pin0output.grid(row=2, column=3)

pin1 = tkinter.StringVar()
pin1.set("0")
label_pin1 = tkinter.Label(window, text="Pin1:  " )
label_pin1.grid(row=3, column=1)
radio_pin1input = tkinter.Radiobutton(window, text="input", variable=pin1, value="0", command=generatePin1)
radio_pin1input.grid(row=3, column=2)
radio_pin1output = tkinter.Radiobutton(window, text="output", variable=pin1, value="1", command=generatePin1)
radio_pin1output.grid(row=3, column=3)

pin2 = tkinter.StringVar()
pin2.set("0")
label_pin2 = tkinter.Label(window, text="Pin2:  " )
label_pin2.grid(row=4, column=1)
radio_pin2input = tkinter.Radiobutton(window, text="input", variable=pin2, value="0", command=generatePin2)
radio_pin2input.grid(row=4, column=2)
radio_pin2output = tkinter.Radiobutton(window, text="output", variable=pin2, value="1", command=generatePin2)
radio_pin2output.grid(row=4, column=3)

pin3 = tkinter.StringVar()
pin3.set("0")
label_pin3 = tkinter.Label(window, text="Pin3:  " )
label_pin3.grid(row=5, column=1)
radio_pin3input = tkinter.Radiobutton(window, text="input", variable=pin3, value="0", command=generatePin3)
radio_pin3input.grid(row=5, column=2)
radio_pin3output = tkinter.Radiobutton(window, text="output", variable=pin3, value="1", command=generatePin3)
radio_pin3output.grid(row=5, column=3)

pin4 = tkinter.StringVar()
pin4.set("0")
label_pin4 = tkinter.Label(window, text="Pin4:  " )
label_pin4.grid(row=6, column=1)
radio_pin4input = tkinter.Radiobutton(window, text="input", variable=pin4, value="0", command=generatePin4)
radio_pin4input.grid(row=6, column=2)
radio_pin4output = tkinter.Radiobutton(window, text="output", variable=pin4, value="1", command=generatePin4)
radio_pin4output.grid(row=6, column=3)

pin5 = tkinter.StringVar()
pin5.set("0")
label_pin5 = tkinter.Label(window, text="Pin5:  " )
label_pin5.grid(row=7, column=1)
radio_pin5input = tkinter.Radiobutton(window, text="input", variable=pin5, value="0", command=generatePin5)
radio_pin5input.grid(row=7, column=2)
radio_pin5output = tkinter.Radiobutton(window, text="output", variable=pin5, value="1", command=generatePin5)
radio_pin5output.grid(row=7, column=3)

pin6 = tkinter.StringVar()
pin6.set("0")
label_pin6 = tkinter.Label(window, text="Pin6:  " )
label_pin6.grid(row=8, column=1)
radio_pin6input = tkinter.Radiobutton(window, text="input", variable=pin6, value="0", command=generatePin6)
radio_pin6input.grid(row=8, column=2)
radio_pin6output = tkinter.Radiobutton(window, text="output", variable=pin6, value="1", command=generatePin6)
radio_pin6output.grid(row=8, column=3)

pin7 = tkinter.StringVar()
pin7.set("0")
label_pin7 = tkinter.Label(window, text="Pin2:  " )
label_pin7.grid(row=9, column=1)
radio_pin7input = tkinter.Radiobutton(window, text="input", variable=pin7, value="0", command=generatePin7)
radio_pin7input.grid(row=9, column=2)
radio_pin7output = tkinter.Radiobutton(window, text="output", variable=pin7, value="1", command=generatePin7)
radio_pin7output.grid(row=9, column=3)


Btn_enter = tkinter.Button(window, text="Generate", bg="green", command=generateDDR )
Btn_enter.grid(row=11, column=3)

window.mainloop()