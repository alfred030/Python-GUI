from tkinter import *
from tkinter import ttk


class Display:
    def __init__(self, master):
        self.master = master
        master.title('GUI class')
        master.geometry('600x300')


root = Tk()
app = Display(root)
root.mainloop()
