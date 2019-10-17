from tkinter import *
from tkinter import ttk, messagebox
from tkinter.ttk import Combobox


def submit():
    T = Combo.get()
    print(T)
    Combo.delete(0, END)
    answer = messagebox.showinfo(title='Languages',
                                 message='You chose was Submitted!\nand it was ' + T)
    Combo.set('Select')
    if answer == 'ok':
        root.quit()


class entry:
    def __init__(self, master):
        master.title('Label')
        master.geometry('300x300')

        V = list(range(2000, 2021))

        # height=15 means i want to see only 15 items and use the scrollbar to navigate
        global Combo
        Combo = ttk.Combobox(master, value=V, height=15, width=30)
        Combo.pack()
        Combo.set('Select')

        Combo.set('Select')

        ttk.Button(master, text='Submit', command=submit).pack()


root = Tk()
app = entry(root)
root.mainloop()
