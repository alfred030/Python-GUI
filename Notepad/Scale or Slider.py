from tkinter import *
from tkinter import ttk


def Print():
    print(s.get())
    print(s1.get())

    T1 = str(s.get())
    T2 = str(s1.get())
    L1.configure(text='Horizontal scale result is: ' + T1)
    L2.configure(text='vertical scale result is: ' + T2)


class scale:
    def __init__(self, master):
        global s
        global s1
        global L1
        global L2

        master.title('')
        master.geometry('300x300')

        s = Scale(master, from_=0,
                  to=100,
                  length=200,
                  width=5,
                  sliderlength=60,  # slider length=30 by default
                  orient=HORIZONTAL)
        s.pack()

        s1 = Scale(master, from_=0,
                   to=100,
                   length=200,
                   width=10,
                   sliderlength=50,
                   orient=VERTICAL)
        s1.pack()
        s1.set(70)

        B = ttk.Button(master, text='Print', command=Print)
        B.pack()

        L1 = ttk.Label(master, text='result 1:')
        L1.pack()

        L2 = ttk.Label(master, text='result 2:')
        L2.pack()


root = Tk()
app = scale(root)
root.mainloop()
