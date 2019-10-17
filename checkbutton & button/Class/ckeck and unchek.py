from tkinter import *


class Restaurant:
    def __init__(self, master):
        self.master = master
        master.title('Restaurant Management System')
        frame = Frame(master)
        frame.pack()

        self.button = Button(frame, text="QUIT", command=frame.quit)
        self.button.pack(side=LEFT)

        self.en = Button(frame, text="Enable", command=self.enable_cb)
        self.en.pack(side=LEFT)

        self.dis = Button(frame, text="Disable", command=self.disable_cb)
        self.dis.pack(side=LEFT)

        self.B1 = Button(frame, text="check", command=self.Check)
        self.B1.pack(side=LEFT)

        self.B2 = Button(frame, text="uncheck", command=self.Uncheck)
        self.B2.pack(side=LEFT)

        self.cb = Checkbutton(frame, text="button")
        self.cb.pack(side=LEFT)

    def enable_cb(self):
        self.cb.configure(state='normal')

    def disable_cb(self):
        self.cb.configure(state='disabled')

    def Uncheck(self):
        self.cb.deselect()

    def Check(self):
        self.cb.select()


root = Tk()
Restaurant = Restaurant(root)
root.mainloop()
