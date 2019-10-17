from tkinter import *
from tkinter import simpledialog

def get_me():
    S = simpledialog.askstring("info", " please enter your name")
    A = simpledialog.askfloat("info", " please enter your age")
    
    print(S)
    print(A)
    

root = Tk()

button = Button(root, text = "popup",  command = get_me)
button.pack()

root.geometry("300x300")
root.mainloop()
