from tkinter import *
from tkinter import ttk, messagebox


def submit():
    root.withdraw()
    T = Combo.get()
    print(T)
    Combo.delete(0, END)
    messagebox.showinfo(title='Languages', message='You chose was Submitted!\nand it was ' + T)


class entry:
    def __init__(self, master):
        master.title('Label')
        master.geometry('300x300')

        V = list(range(0, 50))

        # height=15 means i want to see only 15 items and use the scrollbar to navigate
        global Combo
        Combo = ttk.Combobox(master, value=V, height=15, width=30)
        Combo.pack()

        Combo.set('Select')

        ttk.Button(master, text='Submit', command=submit).pack()


root = Tk()
app = entry(root)
root.mainloop()
