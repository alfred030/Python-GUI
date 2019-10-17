from tkinter import *
from tkinter import messagebox
from tkinter import ttk
import random
import time
import datetime

def main ():
    root = Tk()
    app = window1(root)
#==============================================================================================
# globe variables. it can be use in any class (this not local variable)
font_1 = "Helvertica"
h = 16
color = "grey"

#==============================================================================================
# master window
class window1:
    def __init__(self, master): # to initialize this window
        self.master = master
        self.master.resizable(False, False)
        self.master.title("HOSPITAL LOGIN SYSTEM")
        self.master.configure(bg= '#dbdbdb')
        
#==============================================================================================
# Variables declaration (for the rest button)
        self.entry_Username = StringVar()
        self.entry_Password = StringVar()


#==============================================================================================
        
        self.label=ttk.Label(self.master, text='Username',background = '#dbdbdb',font = ('Time', 10))
        self.label.grid(row=0, column=0, pady = 10, padx = 1)
        
        self.label=ttk.Label(self.master, text='Password',background = '#dbdbdb',font = ('Time', 10))
        self.label.grid(row=1, column=0, pady = 5, padx = 1)

        self.entry_Username = ttk.Entry(self.master, width = 25, font = ('Time', 10))
        self.entry_Username.focus() # this put the cursor in the entry name when we run the program
        self.entry_Password = ttk.Entry(self.master, width = 25, font = ('Time', 10))
        self.entry_Password.config(show = '*')# this is to hid the password
        self.entry_Username.grid(row = 0, column = 1, padx = 1, columnspan=3,sticky ='e'+'w')# to expand the Entry
        self.entry_Password.grid(row = 1, column = 1, padx = 1, columnspan=3,sticky ='e'+'w')

        self.btn1=ttk.Button(self.master, text='Login',command = self.Login_System)
        self.btn1.grid(row=2, column=0,sticky = 'e'+'w',pady = 5,padx = 1)
        self.btn2=ttk.Button(self.master, text='Reset',command = self.Reset)
        self.btn2.grid(row=2, column=1,sticky = 'e'+'w',pady = 5,padx = 1)
        self.btn3=ttk.Button(self.master, text='Sign out or exit',command = self.iExit)
        self.btn3.grid(row=2, column=2,sticky = 'e'+'w',pady = 5,padx = 1)
        self.btn3=ttk.Button(self.master, text='Calculator ', command = self.Cal)
        self.btn3.grid(row=2, column=3,sticky = 'e'+'w',pady = 5,padx = 1)
        
        # most use string while using lower case normal or disabled and no string with upper case latter
        # state = "disabled" or DISABLED, state = NORMAL or "normal"
        self.btnRegistration = ttk.Button(self.master, text="Patients Registration Systems",
                                      state=DISABLED,
                                      command=self.Registration_window)
        self.btnRegistration.grid(row=3, column=0,columnspan=2,sticky = 'e'+'w',pady = 5,padx = 1)

        self.btnHospital = ttk.Button(self.master, text="Hospital Management Systems",
                                      state=DISABLED,
                                      command=self.Hospital_window)
        self.btnHospital.grid(row=3, column=2,columnspan=2, sticky = 'e'+'w',pady = 1,padx = 1)

        
#==============================================================================================
# Login system
    def Login_System(self):
        username = (self.entry_Username.get())
        password = (self.entry_Password.get())

        if(username == str("tia12345")) and (password == str(12345)): #tia12345 most be a srting
            self.btnRegistration.config(state = NORMAL)
            self.btnHospital.config(state = NORMAL)

        elif(username == str("1")) and (password == str(1)): #tia12345 most be a srting
            self.btnRegistration.config(state = NORMAL)
            self.btnHospital.config(state = NORMAL)

        elif(username == str("2"))or(username == str("3")) and (password == str(2))or (password == str(3)): #tia12345 most be a srting
            self.btnRegistration.config(state = NORMAL)
            self.btnHospital.config(state = DISABLED)

        elif(username == str("4"))or(username == str("5")) and (password == str(4))or (password == str(5)): #tia12345 most be a srting
            self.btnRegistration.config(state = DISABLED)
            self.btnHospital.config(state = NORMAL)

        
        else:
            messagebox.askretrycancel("Hospital Login System", "Invalid password or username",
                                      icon = "error")# put this first
            self.btnRegistration.config(state = DISABLED)# this means keep the button disable because of wrong password
            self.btnRegistration.config(state = DISABLED)
            #self.entry_Username.set("")
            #self.entry_Password.set("")# this set the entry to zero if wrong password or username
            self.entry_Username.focus() #put the cursor in the username entry
            
#==============================================================================================
# Reset button function
#self.entry_Username = StringVar()
#self.entry_Password = StringVar()

    def Reset(self):
        self.entry_Username.delete(0, 'end')
        self.entry_Password.delete(0, 'end')
        self.btnRegistration.config(state = DISABLED)#these two lines of code will lock the user out
        self.btnHospital.config(state = DISABLED)    #if the user sign in and click on reset button
        self.entry_Username.focus() #this set the entry to zero if wrong password or username

#==============================================================================================
# Sign out button function

    def iExit(self):
        self.qExit = messagebox.askyesno("Hospital Login System",
                                    "This system is still running.\n"
                                    "Are you sure that you want to sign out?",
                                    icon = "warning")
        if self.qExit > 0:
            self.master.destroy()
            return
        
                        
#==============================================================================================
# Registration management system        
    def Registration_window(self):
        self.master_1 = Toplevel(self.master)
        self.app = PatientsRegistration(self.master_1)
        self.master_1.title("Patients Registration Systems")  #title of the window
        btn1=Button(self.master_1, text='Login',background = '#dbdbdb',relief = GROOVE,font = ('Arial', 12))
        btn1.grid(row=2, column=0,sticky = 'e'+'w',pady = 5,padx = 1)
        
#==============================================================================================         
# Hospital management system
    def Hospital_window(self):
        self.master_2 = Toplevel(self.master)
        self.app = HospitalRegistration(self.master_2)
        self.master_2.title("Hospital Registration Systems")
        
#==============================================================================================         
# calculator
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
# Classes for different windows
class PatientsRegistration:
    def __init__(self, master):
        self.master = master
        self.master.title("Patients Registration Systems")
    
        
class HospitalRegistration:
    def __init__(self, master):
        self.master = master
        self.master.title("Hospital Registration Systems")
        
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

