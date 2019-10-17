# !/usr/bin/python3

'''
You could use one of the following functions with dialogue box −

showinfo()

showwarning()

showerror ()

askquestion()

askokcancel()

askyesno ()

askretrycancel ()
'''



from tkinter import *

from tkinter import messagebox

top = Tk()
top.geometry("100x100")
def hello():
   messagebox.showinfo("Say Hello", "Hello World")

B1 = Button(top, text = "Say Hello", command = hello)
B1.place(x = 35,y = 50)

top.mainloop()
