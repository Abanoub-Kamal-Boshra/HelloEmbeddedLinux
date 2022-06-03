import tkinter
window = tkinter.Tk()
#window.geometry("200x200")

def checkEntery():
    username = entry_name.get()
    pasword = entry_password.get()
    if username == "abanoub" and pasword == "123":
        print("Hello abanoub")
    else:
        print("incorrect username or password")



label_name = tkinter.Label(window, text="User name" )
label_name.grid(row=1, column=1)
entry_name = tkinter.Entry(window)
entry_name.grid(row=1, column=2)

label_password = tkinter.Label(window, text="Password" )
label_password.grid(row=2, column=1)
entry_password = tkinter.Entry(window , show="*")
entry_password.grid(row=2, column=2)

Btn_enter = tkinter.Button(window, text="Enter", bg="green", command=checkEntery )
Btn_enter.grid(row=4, column=3)


window.mainloop()