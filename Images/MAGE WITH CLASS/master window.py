from tkinter import *
from tkinter import messagebox
from tkinter import ttk
import random
import time
import datetime

# ==============================================================================================
# master window
class window1:
    def __init__(self, master):  # to initialize this window
        self.master = master
        self.master.title("LOGIN SYSTEM")
        # self.master.resizable(False, False)
        master.title('LEO')
        self.logo = PhotoImage(file="calculator.PNG").subsample(12, 12)
        self.calculator = ttk.Button(master, image=self.logo, text="Calculator")
        self.calculator.grid(row=0, column=0)
        self.calculator.configure(image=self.logo, compound=BOTTOM)


# ==============================================================================================
def main():
    root = Tk()
    app = window1(root)
    root.mainloop()


if __name__ == '__main__':  main()
