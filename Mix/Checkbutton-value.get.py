from tkinter import *
from tkinter import ttk
from tkinter import messagebox


def click_me():
    s = Var.get()
    print(s)


class entry:
    def __init__(self, master):
        master.title('Label')
        master.geometry('200x200')

        global Var
        Var = IntVar()  # this variable most be declare inside the class as global variable and not out off the class.

        # when check, on value=1
        # when on check off value=0

        global E
        E = Checkbutton(master, text='Item 1', variable=Var)
        E.pack()

        B = ttk.Button(master, text='Print the Value', command=click_me)
        B.pack()


root = Tk()
app = entry(root)
root.mainloop()
