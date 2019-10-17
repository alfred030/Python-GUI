from tkinter import *
from tkinter import ttk


def print_message():
    print('button was click')


class my_button:
    def __init__(self, master):
        # self.master = master
        master.title('print message')

        self.B = ttk.Button(master, text='Print', command=print_message)
        self.B.pack(side=LEFT)

        self.quit = ttk.Button(master, text='Quit', command=master.quit)  # master.quit or master.destroy
        self.quit.pack()


root = Tk()
app = my_button(root)
root.mainloop()
