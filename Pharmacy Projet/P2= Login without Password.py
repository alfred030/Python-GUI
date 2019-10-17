from tkinter import *
import tkinter.messagebox
from tkinter import ttk
import random
import time;
import datetime

def main ():
    root = Tk()
    app = window1(root)
    
font_1 = "Helvertica"
h = 16
color = "grey"
#==============================================================================================
class window1:
    def __init__(self, master): # to initillaze this window
        self.master = master
        self.master.resizable(False, False)
        self.master.title("HOSPITAL LOGIN SYSTEM")
        master.configure(bg= '#dbdbdb')
        
        
        
        label=ttk.Label(self.master, text='Usename',background = '#dbdbdb',font = ('Time', 10))
        label.grid(row=0, column=0, pady = 10, padx = 1)
        
        label=ttk.Label(self.master, text='Password',background = '#dbdbdb',font = ('Time', 10))
        label.grid(row=1, column=0, pady = 5, padx = 1)

        entry_Usename = ttk.Entry(self.master, width = 25, font = ('Time', 10))
        entry_Password = ttk.Entry(self.master, width = 25, font = ('Time', 10))
        entry_Usename.grid(row = 0, column = 1, padx = 1, columnspan=3,sticky ='e'+'w')# to expand the Entry
        entry_Password.grid(row = 1, column = 1, padx = 1, columnspan=3,sticky ='e'+'w')

        btn1=ttk.Button(self.master, text='Login')
        btn1.grid(row=2, column=0,sticky = 'e'+'w',pady = 5,padx = 1)
        btn2=ttk.Button(self.master, text='Reset')
        btn2.grid(row=2, column=1,sticky = 'e'+'w',pady = 5,padx = 1)
        btn3=ttk.Button(self.master, text='Sign out')
        btn3.grid(row=2, column=2,sticky = 'e'+'w',pady = 5,padx = 1)
        btn3=ttk.Button(self.master, text='Calculator ', command = self.Cal)
        btn3.grid(row=2, column=3,sticky = 'e'+'w',pady = 5,padx = 1)
        
        
        btnRegistration = ttk.Button(self.master, text="Patients Registration Systems",
                                      #state='disable',
                                      command=self.Registration_window)
        btnRegistration.grid(row=3, column=0,columnspan=2,sticky = 'e'+'w',pady = 5,padx = 1)

        btnHospital = ttk.Button(self.master, text="Hospital Rigistration Systems",
                                      #state='disable',
                                      command=self.Hospital_window)
        btnHospital.grid(row=3, column=2,columnspan=2, sticky = 'e'+'w',pady = 1,padx = 1)

        
        


    def Registration_window(self):
        self.master_1 = Toplevel(self.master)
        self.app = PatientsRegistration(self.master_1)
        self.master_1.title("Patients Registration Systems")  #title of the window
        btn1=Button(self.master_1, text='Login',background = '#dbdbdb',relief = GROOVE,font = ('Arial', 12))
        btn1.grid(row=2, column=0,sticky = 'e'+'w',pady = 5,padx = 1)
        
    def Hospital_window(self):
        self.master_2 = Toplevel(self.master)
        self.app = HospitalRigistration(self.master_2)
        self.master_2.title("Hospital Rigistration Systems")
        
    def Cal(self):
        self.master_3 = Toplevel(self.master)
        self.app = Calculator(self.master_3)
        self.master_3.title("Calculator")
        self.display=Entry(self.master_3,font=(font_1 ,h),relief=SUNKEN,justify=RIGHT,
                           bg="white",bd=20)
        self.display.insert(0, "0")
        self.display.grid(row=0, column=0, columnspan=5)

        # FIRST ROW
        self.but7=Button(self.master_3,bg=color,text="7",font=(font_1 ,h),borderwidth=2)
        self.but7.grid(row=1, column=0,sticky="NWNESWSE")

        self.but8=Button(self.master_3,bg=color,text="8",font=(font_1 ,h),borderwidth=2)
        self.but8.grid(row=1, column=1,sticky="NWNESWSE")
        
        self.but9=Button(self.master_3,bg=color,text="9",font=(font_1 ,h),borderwidth=2)
        self.but9.grid(row=1, column=2,sticky="NWNESWSE")

        self.div=Button(self.master_3,bg=color,text="/",font=(font_1 ,h),borderwidth=2)
        self.div.grid(row=1, column=3,sticky="NWNESWSE")

        self.clear=Button(self.master_3,bg=color,text="C",font=(font_1 ,h),borderwidth=2)
        self.clear.grid(row=1, column=4,sticky="NWNESWSE")
        
#==============================================================================================   
class PatientsRegistration:
    def __init__(self, master):
        self.master = master
        self.master.title("Patients Registration Systems")
    
        

#==============================================================================================
class HospitalRigistration:
    def __init__(self, master):
        self.master = master
        self.master.title("Hospital Rigistration Systems")
        
#==============================================================================================
class Calculator:
    def __init__(self, master):
        self.master = master
        self.master.title("Calculator")
    
        
        
#==============================================================================================    
def main ():
    root = Tk()
    app = window1(root)
    root.mainloop()

if __name__ == '__main__':  main()
   
