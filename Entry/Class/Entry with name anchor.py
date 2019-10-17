from tkinter import *
from tkinter import ttk


class label:
    def __init__(self, master):
        self.master = master
        master.title('Label')

        self.L = ttk.Label(self.master, text='Name:')
        self.L.pack(anchor=W)

        self.E = ttk.Entry(self.master)
        self.E.pack()
        self.E.focus()


root = Tk()
app = label(root)
root.mainloop()
