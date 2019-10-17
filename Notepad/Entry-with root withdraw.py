from tkinter import *
from tkinter import ttk
from tkinter import messagebox


def click_me(event=''):
    E.configure(state=NORMAL)
    s = E.get()
    print(s)
    E.delete(1, END)
    Var.set('0')

    root.withdraw()  # you have to withdraw the root before the message box pop up

    answer = messagebox.askquestion('Message', 'Welcome ' + s + '!')
    print('Welcome ' + s + '!')
    print(answer)
    E.configure(state=DISABLED)
    B.configure(state=DISABLED)


class entry:
    def __init__(self, master):
        master.title('Label')
        # master.geometry('200x200')

        L = Label(master, text='Enter your name')
        L.pack(side=LEFT)
        global Var
        Var = StringVar()
        global E
        E = Entry(master, justify=LEFT, textvariable=Var)
        E.pack(side=LEFT)
        E.focus()
        E.bind('<Return>', click_me)

        global B
        B = ttk.Button(master, text='click me', command=click_me)
        B.pack(side=RIGHT)


root = Tk()
app = entry(root)
root.mainloop()
