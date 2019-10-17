from tkinter import *
from tkinter import ttk


class Restaurant:
    def __init__(self, master):
        self.master = master
        master.title('LEO')
        self.logo = PhotoImage(file="calculator.PNG").subsample(5, 5)
        self.calculator = ttk.Button(master, image=self.logo, text="TIA")
        self.calculator.grid(row=0, column=0)


root = Tk()
my_gui = Restaurant(root)
root.mainloop()
