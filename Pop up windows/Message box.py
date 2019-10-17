from tkinter import *
from tkinter import messagebox
from tkinter import ttk


def call_me():
    a = messagebox.showinfo('message', 'Installation complete')
    print(a)
    c = messagebox.showwarning('message', 'Installation complete')
    print(c)
    b = messagebox.showerror('message', 'Installation complete')
    print(b)
    d = messagebox.askokcancel('message', 'Installation complete')
    print(d)
    f = messagebox.askquestion('message', 'Installation complete')
    print(f)
    g = messagebox.askretrycancel('message', 'Installation complete')
    print(g)
    r = messagebox.askyesno('message', 'Installation complete')
    print(r)
    w = messagebox.askyesnocancel('message', 'Installation complete')
    print(w)


class message_box:
    def __init__(self, master):
        master.title('Message box')

        self.b = ttk.Button(master, text='message', command=call_me)
        self.b.pack()


root = Tk()
message = message_box(root)
root.mainloop()
