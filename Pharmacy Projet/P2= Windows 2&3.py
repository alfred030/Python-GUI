from tkinter import *
import tkinter.messagebox
from tkinter import ttk
import random
import time;
import datetime

def main ():
    root = Tk()
    app = window1(root)

#==============================================================================================
class window1:
    def __init__(self, master): # to initillaze this window
        self.master = master
        self.master.title("Pharmacy Management System")
        self.master.geometry("1350x750+0+0")
        self.frame = Frame(self.master)
        self.frame.pack()

        # this is to text if those windows are working well.
        self.btnRegistration = Button(self.frame, text="Patients Registration Systems",
                                      command=self.Registration_window)
        self.btnRegistration.grid(row=0, column=0)

        self.btnHospital = Button(self.frame, text="Hospital Rigistration Systems",
                                      command=self.Hospital_window)
        self.btnHospital.grid(row=0, column=1)

    def Registration_window(self):
        self.new_window = Toplevel(self.master)
        self.app = window2(self.new_window)
        self.new_window.title("Patients Registration Systems")  #title of the window
        self.btn = Button(self.new_window, text = "Tia").pack() #first button inside this window
        
    def Hospital_window(self):
        self.new_window = Toplevel(self.master)
        self.app = window3(self.new_window)
        self.new_window.title("Hospital Rigistration Systems")
        
#==============================================================================================   
class window2:
    def __init__(self, master):
        self.master = master
        self.master.title("Patients Registration Systems")
        self.master.geometry("1350x750+0+0")
        self.frame = Frame(self.master)
        self.frame.pack()

#==============================================================================================
class window3:
    def __init__(self, master):
        self.master = master
        self.master.title("Hospital Rigistration Systems")
        self.master.geometry("1350x750+0+0")
        self.frame = Frame(self.master)
        self.frame.pack()
        
#==============================================================================================    
def main ():
    root = Tk()
    app = window1(root)
    root.mainloop()

if __name__ == '__main__':  main()
   
