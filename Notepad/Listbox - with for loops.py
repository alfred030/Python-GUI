from tkinter import *
from tkinter import ttk, scrolledtext


class scroll:
    def __init__(self, master):
        master.title('')

        listbox = Listbox(master)
        for i in range(1, 100):
            listbox.insert(END, 'List ' + str(i))

        listbox.pack()


root = Tk()
app = scroll(root)
root.mainloop()
