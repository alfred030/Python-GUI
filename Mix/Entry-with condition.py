from tkinter import *
from tkinter import ttk
from tkinter import messagebox


def click_me(event=''):
    s = E.get()
    if s == 'tia':
        print(s)
        print('good')
        messagebox.showinfo('message', 'You got it')
    else:
        print(s)
        print('bad')
        messagebox.showinfo('message', 'Invalid input')



class entry:
    def __init__(self, master):
        master.title('Label')
        master.geometry('200x200')
        global E
        E = ttk.Entry(master)
        E.pack()
        E.focus()
        E.bind('<Return>', click_me)

        B = ttk.Button(master, text='click me', command=click_me)
        B.pack()


root = Tk()
app = entry(root)
root.mainloop()
