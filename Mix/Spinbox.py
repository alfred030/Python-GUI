from tkinter import *
from tkinter import ttk
from tkinter import messagebox


def Print():
    print(S1.get())
    print(S2.get())

    T1 = str(S1.get())
    T2 = str(S2.get())
    L1.configure(text='Spinbox 1 result is: ' + T1)
    L2.configure(text='Spinbox 2 result is: ' + T2)
    total = T1 + T2
    Sum.configure(text='The sum off spinbox 1 and 2 is: ' + total)


class spinbox:
    def __init__(self, master):
        global S1
        global S2
        global s1
        global L1
        global L2
        global Sum

        master.title('')
        master.geometry("400x400")

        S1 = Spinbox(master, from_=2000, to=2020)
        S1.pack()

        S2 = Spinbox(master, from_=0, to=20)
        S2.pack()

        B = ttk.Button(master, text='Print result', command=Print)
        B.pack()

        L1 = ttk.Label(master, text='result 1:')
        L1.pack()

        L2 = ttk.Label(master, text='result 2:')
        L2.pack()

        Sum = ttk.Label(master, text='Sum:')
        Sum.pack()


root = Tk()
app = spinbox(root)
root.mainloop()
