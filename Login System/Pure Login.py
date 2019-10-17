from tkinter import *
from tkinter import messagebox
from tkinter import ttk
import random
import time
import datetime


def main():
    root = Tk()
    app = window1(root)


# ==============================================================================================
# master window

class login:
    def __init__(self, master):  # to initialize this window
        self.master = master
        self.master.resizable(False, False)
        self.master.title("LOGIN SYSTEM")
        self.master.config(bg="powder blue")

        # ==============================================================================================
        # Variables declaration (for the rest button)
        self.entry_Username = StringVar()
        self.entry_Password = StringVar()

        # ==============================================================================================
        self.label = ttk.Label(self.master, text='Username', background="powder blue", font=('Time', 10))
        self.label.grid(row=0, column=0, pady=10, padx=1)

        self.label = ttk.Label(self.master, text='Password', background="powder blue", font=('Time', 10))
        self.label.grid(row=1, column=0, pady=5, padx=1)

        self.entry_Username = ttk.Entry(self.master, width=25, font=('Time', 10))
        self.entry_Username.focus()  # this put the cursor in the entry name when we run the program
        self.entry_Password = ttk.Entry(self.master, width=25, font=('Time', 10))
        self.entry_Password.config(show='*')  # this is to hid the password
        self.entry_Username.grid(row=0, column=1, padx=1, columnspan=2, sticky='e' + 'w')  # to expand the Entry
        self.entry_Password.grid(row=1, column=1, padx=1, columnspan=2, sticky='e' + 'w')

        self.label = Label(self.master, text='', background="powder blue")
        self.label.grid(row=2, column=0, columnspan=3, sticky='e' + 'w')

        self.btn1 = ttk.Button(self.master, text='Login', command=self.Login_System)
        self.btn1.grid(row=3, column=0, sticky='e' + 'w', pady=1, padx=1)
        self.btn2 = ttk.Button(self.master, text='Reset', command=self.Reset)
        self.btn2.grid(row=3, column=1, sticky='e' + 'w', pady=1, padx=30)
        self.btn3 = ttk.Button(self.master, text='Exit', command=self.iExit)
        self.btn3.grid(row=3, column=2, sticky='e' + 'w', pady=1, padx=1)

    # ==============================================================================================
    # Login system
    def Login_System(self):
        username = (self.entry_Username.get())
        password = (self.entry_Password.get())

        if (username == str("merluise.tia")) and (password == str("tia12345")):  # tia12345 most be a string
            self.restaurant_window = Toplevel(self.master)
            self.app = Restaurant(self.restaurant_window)

        elif (username == str("1")) and (password == str(1)):  # tia12345 most be a string
            self.restaurant_window = Toplevel(self.master)
            self.app = Restaurant(self.restaurant_window)

        elif (username == str("2")) or (username == str("3")) and (password == str("2")) or (
                password == str(3)):  # tia12345 most be a srting
            self.restaurant_window = Toplevel(self.master)
            self.app = Restaurant(self.restaurant_window)

        elif (username == str("4")) or (username == str("5")) and (password == str(4)) or (
                password == str(5)):  # tia12345 most be a srting
            self.restaurant_window = Toplevel(self.master)
            self.app = Restaurant(self.restaurant_window)

        elif (username == str("5")) and (password == str(5)):
            self.restaurant_window = Toplevel(self.master)
            self.app = Restaurant(self.restaurant_window)


        else:
            messagebox.askretrycancel("Hospital Login System", "Invalid password or username",
                                      icon="error")  # put this first

            # self.entry_Username.set("")
            # self.entry_Password.set("")# this set the entry to zero if wrong password or username
            self.entry_Username.focus()  # put the cursor in the username entry

    # ==============================================================================================

    def Restaurant_System(self):
        self.restaurant_window = Toplevel(self.master)
        self.app = Restaurant(self.restaurant_window)

    # ==============================================================================================
    # Sign out button function

    def iExit(self):
        self.qExit = messagebox.askyesno("Hospital Login System",
                                         "This system is still running.\n"
                                         "Are you sure that you want to sign out?",
                                         icon="warning")
        if self.qExit > 0:
            self.master.destroy()
            return

    # ==============================================================================================
    # Reset button function
    # self.entry_Username = StringVar()
    # self.entry_Password = StringVar()

    def Reset(self):
        self.entry_Username.delete(0, 'end')
        self.entry_Password.delete(0, 'end')
        self.entry_Username.focus()  # this set the entry to zero if wrong password or username


# ==============================================================================================
class Restaurant:
    def __init__(self, master):  # to initialize this window
        self.master = master
        # self.master.resizable(False, False)
        self.master.title("LOGIN SYSTEM")
        self.master.config(bg="")


# ==============================================================================================
def main():
    root = Tk()
    app = login(root)
    root.mainloop()


if __name__ == '__main__':  main()
