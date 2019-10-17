from tkinter import *
import tkinter.messagebox
from tkinter import ttk
import random
import time;
import datetime



class window1:
    def __init__(self, master):
        self.master = master
        self.master.title("Pharmacy Management System")
        self.master.geometry("1350x750+0+0")
        self.frame = Frame(self.master)
        self.frame.pack()


def main ():
    root = Tk()
    app = window1(root)
    root.mainloop()

    
if __name__ == '__main__':
    main()
