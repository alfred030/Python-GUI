from tkinter import *
from tkinter import messagebox
from tkinter import ttk
import random
import time;
import datetime

def main ():
    root = Tk()
    app = window1(root)

#==============================================================================================
# master window

class login_window:
    def __init__(self, master): # to initillaze this window
        self.master = master
        #self.master.resizable(False, False)
        self.master.title("LOGIN SYSTEM")
        self.master.geometry('1350x750+0+0')
        self.master.config(bg="powder blue")
        self.frame=Frame(self.master, bg="powder blue")
        self.frame.pack()
                         




#==============================================================================================    
def main ():
    root = Tk()
    app = login_window(root)
    root.mainloop()

if __name__ == '__main__':  main()
   
