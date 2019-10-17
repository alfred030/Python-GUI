from tkinter import *
from tkinter import ttk, scrolledtext


class Scroll:
    def __init__(self, master):
        master.title('')
        master.geometry('500x500')

        frame= Frame(master)
        frame.pack()

        scroll = Scrollbar(frame)
        scroll.pack(side=RIGHT, fill=Y)

        # height=25 is to set 25 items in the listbox
        listbox = Listbox(frame, height=25,
                          yscrollcommand=scroll.set)  # yscroll command it is to make the scroll bar communique with the listbox
        for i in range(1, 101):
            listbox.insert(END, 'List ' + str(i))

        listbox.pack(side=LEFT)
        scroll.configure(command=listbox.yview)  # this yview is in the master windows


root = Tk()
app = Scroll(root)
root.mainloop()
