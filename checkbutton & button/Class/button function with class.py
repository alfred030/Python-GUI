from tkinter import *
from tkinter import ttk


class Display:
    def __init__(self, master):
        self.master = master
        master.title("Leo")
        master.geometry("600x300")

        self.b1 = ttk.Button(self.master, text='Enable', command=lambda: on_click(1))
        self.b1.pack()
        self.b2 = ttk.Button(self.master, text='Disable', command=lambda: on_click(2))
        self.b2.pack()
        self.b3 = ttk.Button(self.master, text='Check', command=lambda: on_click(3))
        self.b3.pack()
        self.b4 = ttk.Button(self.master, text='Uncheck', command=lambda: on_click(4))
        self.b4.pack()

        self.b5 = Checkbutton(self.master, text='Button', state=DISABLED)
        self.b5.pack()

        def on_click(args):
            if args == 1:
                print("Button was enabled")
                self.b5.configure(state=NORMAL)
            if args == 2:
                print("Button was disabled")
                self.b5.configure(state=DISABLED)
            if args == 3:
                print("Button was checked")
                self.b5.select()
            if args == 4:
                print("Button was unchecked")
                self.b5.deselect()


root = Tk()
app = Display(root)
root.mainloop()
