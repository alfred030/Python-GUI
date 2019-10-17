from tkinter import *
from tkinter import ttk, messagebox
from tkinter.ttk import Combobox


def submit():
    T = Combo.get()
    print(T)
    Combo.delete(0, END)
    messagebox.showinfo(title='Languages',
                        message='You chose was Submitted!\nand it was ' + T)
    Combo.set('Select your language')


class entry:
    def __init__(self, master):
        master.title('Label')
        master.geometry('300x300')

        global V
        V = ['C++', 'C',
             'C#',
             'Python',
             'Java',
             'Javascript',
             'Swift',
             "PHP",
             "JSP",
             "Ruby"]
        # height=5 means i want to see only 5 items and use the scrollbar to navigate

        global Combo
        Combo = ttk.Combobox(master, value=V, height=5, width=30)
        Combo.pack()
        Combo.set('Select your language')

        ttk.Button(master, text='Submit', command=submit).pack()


root = Tk()
app = entry(root)
root.mainloop()
