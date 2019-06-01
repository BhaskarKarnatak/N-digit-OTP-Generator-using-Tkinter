import tkinter as tk
from random import randrange
from tkinter import messagebox
from tkinter import *

root=tk.Tk()

head=tk.Label(root,text=" N-DIGIT OTP Generator",font=("Verdana 18 bold underline"),fg="purple",pady=30,padx=130).pack()

value=tk.Label(root,text="How many digit do you want in your OTP",font=("Verdana 12 bold"),pady=20).pack()
valueEntry=tk.Entry(root,)
valueEntry.pack(pady=20)

buttonv=tk.Button(root,text="Generate OTP",command=(lambda:display()))
buttonv.pack()


result=tk.Label(root,text="")
result.pack()



def display():


    if valueEntry.index("end")==0:
        messagebox.showerror("Error","Field Can't be Empty")
    else:
        try:
            check=int(valueEntry.get())
            compute(check)
        except ValueError:
            messagebox.showerror("Error", "TypeError : \nEnter Integer value only")
            valueEntry.delete(0, END)
            valueEntry.insert(0, "")

def compute(value):
    if value>=3 and value<99:

        otp = str(getotp(value))
        result.config(text="Your OTP is : " + otp, font=("verdana 14 bold"))
    else:
        messagebox.showinfo("Information","LimitError : \nPlease Enter Number Greater Than Two.")







def getotp(otp):
    string = ""

    for i in range(otp):
        string =string + str(randrange(0,9))


    return string

tk.mainloop()