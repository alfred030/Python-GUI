from tkinter import *
from tkinter import ttk


root = Tk()
calculator = ttk.Button(root, text="CALCULATOR")
calculator.grid(row=0, column=0)
logo = PhotoImage(file="calculator.PNG").subsample(5, 5)
calculator.configure(image=logo, compound=BOTTOM)


root.mainloop()
