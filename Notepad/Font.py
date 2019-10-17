from tkinter import *
from tkinter.font import Font


def submit():
    pass


class My_Font:
    def __init__(self, master):
        master.title('Label')
        master.geometry('500x500')

        # family = 'Helvetica'
        global my_font
        my_font = Font(size=18,
                       family='Time New Roman',
                       weight='bold',
                       slant='italic',
                       underline=1)

        label = Label(master, text='Restaurant Management System', font=my_font)
        label.pack()


root = Tk()
app = My_Font(root)
root.mainloop()
