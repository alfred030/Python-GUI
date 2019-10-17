from tkinter import *
from tkinter import ttk
from tkinter import filedialog


def open_file():
    pass


def save_file(event=None):
    Save = filedialog.asksaveasfile(mode='w', defaultextension='.txt')
    if Save is None:
        return

    Save.write('1820 election, Andrew Jackson was elected president.'
               'When he came to the office, he has almost the philosophy as Thomas'
               'Jefferson. His ideology was that he believes in the small federal'
               'government that does not interfere with the small farmers. He really'
               'wants to use the federal government to benefit supporters which was the'
               'small farmers. He believes that that the federal should be small in theory'
               'and extent in practice to benefit his supports.')


class scale:
    def __init__(self, master):
        master.title('')

        B1 = ttk.Button(master, text='Save as', command=save_file)
        B1.pack()
        master.bind('<Control-s>', save_file)


root = Tk()
app = scale(root)
root.mainloop()
