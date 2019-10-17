from tkinter import *
from tkinter import ttk, scrolledtext


class Scroll:
    def __init__(self, master):
        master.title('')
        master.geometry('500x500')

        scroll = Scrollbar(master)
        scroll.pack(side=RIGHT, fill=Y)

        listbox = Listbox(master,
                          yscrollcommand=scroll.set)  # yscroll command it is to make the scroll bar communique with the listbox
        for i in range(1, 100):
            listbox.insert(END, 'List ' + str(i))

        listbox.pack(side=LEFT)
        scroll.configure(command=listbox.yview)  # this yview is in the master windows


root = Tk()
app = Scroll(root)
root.mainloop()
