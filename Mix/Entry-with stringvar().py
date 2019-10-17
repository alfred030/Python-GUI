from tkinter import *
from tkinter import ttk
from tkinter import messagebox


def click_me(event=''):
    E.configure(state=NORMAL)
    Var.set('')
    Var.set('Welcome')
    s = E.get()
    print(s)
    if s == 'Welcome':
        messagebox.showinfo('message', 'Wow!')


class entry:
    def __init__(self, master):
        master.title('Label')
        master.geometry('200x200')

        global Var
        Var = StringVar()

        global E
        E = Entry(master, textvariable=Var, justify=RIGHT, state=DISABLED)
        Var.set('0')  # do not put ttk theme. if you add ttk theme, you will not be able to set the text
        E.pack()
        E.focus()
        E.bind('<Return>', click_me)

        B = ttk.Button(master, text='click me', command=click_me)
        B.pack()


root = Tk()
app = entry(root)
root.mainloop()
