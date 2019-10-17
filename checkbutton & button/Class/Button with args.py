from tkinter import *


def on_click(args):
    if args == 1:
        print("Button1 clicked")
    if args == 2:
        print("Button2 clicked")


class Display:
    def __init__(self, master):
        self.master = master
        master.title("Leo")
        master.geometry("600x300")

        self.b1 = Button(self.master, text='Button1', command=lambda: on_click(1))
        self.b1.pack()
        self.b2 = Button(self.master, text='Button2', command=lambda: on_click(2))
        self.b2.pack()


root = Tk()
app = Display(root)
root.mainloop()
