from tkinter import *
from tkinter import ttk
from tkinter import colorchooser


def color():
    clr = colorchooser.askcolor(title='select color')
    print(clr)
    L.configure(fg=clr[1])
    root.configure(bg=clr[1])
    # L1.configure(bg=clr[1])


class course:
    def __init__(self, master):
        master.title('')
        master.geometry('300x300')

        B1 = ttk.Button(master, text='choose color', command=color)
        B1.pack()

        global L
        L = Label(master, text='Change color', fg='green')
        L.pack()

        global L1
        L1 = Label(master, text='\n\n\n\n\n\nChange color', fg='blue')
        L1.pack()


root = Tk()
app = course(root)
root.mainloop()
