from tkinter import *
from tkinter import ttk


class Display:
    def __init__(self, master):
        self.master = master
        master.title('GUI class')
        master.geometry('600x300')


class button:
    def __init__(self, master):
        self.master = master
        self.L1 = Button(self.master, text="TIA")
        self.L1.pack()


class entry:
    def __init__(self, master):
        self.master = master
        self.E1 = ttk.Entry(self.master)
        self.E1.pack()


class label:
    def __init__(self, master):
        self.master = master
        self.L1 = Label(self.master, text="Label class")
        self.L1.pack()


class label:
    def __init__(self, master):
        self.master = master
        self.L1 = Label(self.master, text="Label class")
        self.L1.pack()

class frames:
    def __init__(self, master):

        self.master = master
        self.F1 = ttk.Frame(self.master, width=400, height=150, relief=SUNKEN)
        self.F1.pack()
        # self.l = Button(self.F1, text = 'This is label frames')
        # self.l.grid(row=0, column=0)


root = Tk()
app = Display(root)
app = button(root)
app = label(root)
app = entry(root)
app = frames(root)
root.mainloop()
