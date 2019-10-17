from tkinter import *
from tkinter import ttk


def Print(event=None):
    Z = E.get()
    print(Z)
    label.configure(text='Hello ' + Z + '! ' + '\nHow was yo day?')


class frame:
    def __init__(self, master):
        global E
        global label
        master.title('')
        master.geometry('300x300')

        F = LabelFrame(master, text='Input your name', padx=5, pady=5)
        F.pack()

        E = ttk.Entry(F, width=30)
        E.pack()
        E.focus()

        E.bind('<Return>', Print)

        B = ttk.Button(F, text='Print name', command=Print)
        B.pack(anchor=W)

        label = Label(F, text='Result:')
        label.pack(anchor=W)


root = Tk()
app = frame(root)
root.mainloop()
