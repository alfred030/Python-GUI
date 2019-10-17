import math
from tkinter import *
from tkinter import ttk


class Volume:
    def __init__(self, master):  # this is a constructor
        self.master = master
        master.title('Volume of cylinder')
        self.L1 = ttk.Label(self.master, text='Radius')
        self.L1.pack()

        self.E1 = ttk.Entry(self.master)
        self.E1.pack()
        self.E1.focus()

        self.L2 = ttk.Label(self.master, text='Height')
        self.L2.pack()

        self.E2 = ttk.Entry(self.master)
        self.E2.pack()

        self.B = ttk.Button(self.master, text='Calculate', command=self.calculate_volume)
        self.B.pack()
        self.master.bind('<Return>', self.calculate_volume)

        self.B1 = ttk.Button(self.master, text='Reset', command=self.reset)
        self.B1.pack()

        self.output = Text(self.master,
                           borderwidth=3,
                           relief=GROOVE,
                           font='Time, 12',
                           height=10,
                           width=45)
        self.output.configure(state=DISABLED)
        self.output.pack()

    def calculate_volume(self, event=None):
        r = float(self.E1.get())
        print(r)
        h = float(self.E2.get())
        print(h)
        v = math.pi * r ** 2 * h  # v = math.pi*r*r*h
        print(v)

        self.output.configure(state=NORMAL)  # most config the state to normal before inserting the result.

        Output_values = 'Given\nRadius:' + str(r) + ' units\n' \
                        + 'height: ' + str(h) + ' units\n'
        Output_values += 'The volume is: ' + str(v) + ' units cube'
        # Output_values = Output_values + 'The volume is :' + str(v) + ' units cube' # this is the second method

        self.output.insert(INSERT, Output_values)
        self.output.configure(state=DISABLED)

    def reset(self):
        self.output.configure(state=NORMAL)  # config the output to normal before resetting.
        self.output.delete(1.0, END)
        self.output.configure(state=DISABLED)  # disable the output resetting.

        self.E1.delete(0, END)
        self.E1.focus()
        self.E2.delete(0, END)


root = Tk()
Vol = Volume(root)
root.mainloop()
