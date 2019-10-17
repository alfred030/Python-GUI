from tkinter import *
from tkinter import ttk


root = Tk()

logo = PhotoImage(file="calculator.PNG").subsample(1, 1)
calculator = ttk.Button(root, text="CALCULATOR", image=logo)
calculator.grid(row=0, column=0)

calculator.configure(image=logo, compound=BOTTOM)


root.mainloop()
