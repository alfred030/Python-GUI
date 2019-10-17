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

        self.LabelTitle = Label(self.frame, text = "Pharmacy Management System",
                                                    font=('arial', 50, 'bold'),
                                                    bd = 20)
        self.LabelTitle.grid(row=0, column=0, columnspan=2,pady=40)

        self.Loginframe1=Frame(self.frame, width=1010, heigh=300, bd=20, relief='ridge')
        self.Loginframe1.grid(row=1, column=0)

        self.Loginframe2=Frame(self.frame, width=1000, heigh=100, bd=20, relief='ridge')
        self.Loginframe2.grid(row=2, column=0)

        self.Loginframe3=Frame(self.frame, width=1000, heigh=200, bd=20, relief='ridge')
        self.Loginframe3.grid(row=3, column=0, pady=2)

      
        
        self.btnRegistration = Button(self.Loginframe3, text="Patients Registration Systems",
                                      font=('arial', 14, 'bold'),
                                      command=self.Registration_window)
        self.btnRegistration.grid(row=0, column=0)

        self.btnHospital = Button(self.Loginframe3, text="Hospital Rigistration Systems",
                                      font=('arial', 14, 'bold'),
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
   
