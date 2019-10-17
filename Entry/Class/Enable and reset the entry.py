from tkinter import *
from tkinter import ttk


class Display:
    def __init__(self, master):
        self.master = master
        master.title("Leo")
        master.geometry("600x300")

        self.b1 = ttk.Button(self.master, text='Enable', command=lambda: on_click(1))
        self.b1.pack()
        self.b2 = ttk.Button(self.master, text='Reset', command=lambda: on_click(2))
        self.b2.pack()

        V1 = IntVar()
        V2 = IntVar()
        self.b5 = ttk.Entry(self.master, text='Button',
                            state=DISABLED,
                            justify=RIGHT,
                            textvariable=V1)
        self.b5.pack()

        self.b6 = ttk.Entry(self.master, text='Button',
                            state=DISABLED,
                            justify=RIGHT,
                            textvariable=V2)
        self.b6.pack()

        def on_click(args):
            if args == 1:
                print("Entry was enabled")
                self.b5.configure(state=NORMAL)
                self.b5.focus()
                self.b5.delete(0, END)
            if args == 2:
                print("Entry was disabled")
                self.b5.configure(state=DISABLED)
                V1.set("I was reset")
            if args == 2:
                print("Entry was disabled")
                self.b6.configure(state=NORMAL)
                V2.set("I was enable")


root = Tk()
app = Display(root)
root.mainloop()
