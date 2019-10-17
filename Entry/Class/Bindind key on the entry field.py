from tkinter import *
from tkinter import ttk


class Display:
    def __init__(self, master):
        # global variable
        self.value = ''  # this can be access in any function in the program

        self.master = master
        master.geometry('200x100')
        master.title('Display')
        self.entry = ttk.Entry(self.master)
        self.entry.bind('<Return>', self.On_return)
        self.entry.pack()
        self.entry.focus()

    def On_return(self, event):
        self.value = self.entry.get()
        print(self.value)
        self.entry.delete(0, END)


root = Tk()
app = Display(root)
root.mainloop()
