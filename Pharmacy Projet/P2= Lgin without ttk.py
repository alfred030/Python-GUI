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
        self.master.resizable(False, False)
        self.master.title("LOGIN SYSTEM")
        master.configure(background = '#dbdbdb')
        
        
        label=ttk.Label(self.master, text='Usename',background = '#dbdbdb',font = ('Arial', 12))
        label.grid(row=0, column=0, pady = 10, padx = 10)
        label=ttk.Label(self.master, text='Password',background = '#dbdbdb',font = ('Arial', 12))
        label.grid(row=1, column=0, pady = 5, padx = 10)

        entry_Usename = ttk.Entry(self.master, width = 25, font = ('Arial', 12))
        entry_Password = ttk.Entry(self.master, width = 25, font = ('Arial', 12))
        entry_Usename.grid(row = 0, column = 1, padx = 1, columnspan=2)
        entry_Password.grid(row = 1, column = 1, padx = 1, columnspan=2)

        btn1=Button(self.master, text='Login',background = '#dbdbdb',relief = GROOVE,font = ('Arial', 12))
        btn1.grid(row=2, column=0,sticky = 'e'+'w',pady = 5,padx = 1)
        btn2=Button(self.master, text='Reset',background = '#dbdbdb',relief = GROOVE,font = ('Arial', 12))
        btn2.grid(row=2, column=1,sticky = 'e'+'w',pady = 5,padx = 10)
        btn3=Button(self.master, text='Exit ',background = '#dbdbdb',relief = GROOVE,font = ('Arial', 12))
        btn3.grid(row=2, column=2,sticky = 'e'+'w',pady = 5,padx = 1)
        
        
        # this is to text if those windows are working well.
        btnRegistration = Button(self.master, text="Patients Registration Systems ",
                                      font = ('Time', 16),
                                      relief = GROOVE,
                                      background = '#dbdbdb',
                                      #state='disable',
                                      command=self.Registration_window)
        btnRegistration.grid(row=3, column=0,columnspan=3,sticky = 'e'+'w',pady = 5,padx = 1)

        btnHospital = Button(self.master, text="Hospital Rigistration Systems",
                                      font = ('Time', 16),
                                      relief = GROOVE,
                                      background = '#dbdbdb',
                                      #state='disable',
                                      command=self.Hospital_window)
        btnHospital.grid(row=4, column=0,columnspan=3, sticky = 'e'+'w',pady = 1,padx = 1)
        


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
def main ():
    root = Tk()
    app = window1(root)
    root.mainloop()

if __name__ == '__main__':  main()
   
