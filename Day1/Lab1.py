import tkinter
window = tkinter.Tk()

def printName():
	print("I am Abanoub Kamal")

def printOk():
	print("Ok")



Btn_name = tkinter.Button(window, text="Print_Name", bg="yellow", command=printName )
Btn_name.place(x=10, y=10)

Btn_ok = tkinter.Button(window, text="Ok", bg="green", command=printOk )
Btn_ok.place(x=200, y=200)


Btn_close = tkinter.Button(window, text="close", bg="red", command=exit )
Btn_close.place(x=200, y=250)

window.mainloop()