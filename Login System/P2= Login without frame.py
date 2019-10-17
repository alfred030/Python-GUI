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

class login:
    def __init__(self, master): # to initillaze this window
        self.master = master
        #self.master.resizable(False, False)
        self.master.title("LOGIN SYSTEM")
        self.master.config(bg="powder blue")
        

        self.btnLogin=Button(self.master,
                                 text='Login',
                                 #bg="blue",
                                 command = self.Restaurant_System)
        self.btnLogin.grid(row=3, column=0)

    def Restaurant_System(self):
        self.restaurant_window = Toplevel(self.master)
        self.app = Restaurant(self.restaurant_window)
                                  
        

class Restaurant:
    def __init__(self, master): # to initillaze this window
        self.master = master
        #self.master.resizable(False, False)
        self.master.title("LOGIN SYSTEM")
        self.master.config(bg="blue")
        


#==============================================================================================    
def main ():
    root = Tk()
    app = login(root)
    root.mainloop()

if __name__ == '__main__':  main()
   
