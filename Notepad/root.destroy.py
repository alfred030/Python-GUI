from tkinter import *


def open_windows():
    windows_1 = Toplevel()
    windows_1.title('Top windows')
    windows_1.geometry('500x500')

    b1 = Button(windows_1, text='Close', command=windows_1.destroy)  # quit close only the top level windows
    b1.pack()


class course:
    def __init__(self, master):
        master.geometry('300x300')

        b = Button(master, text='Open windows', command=open_windows)
        b.pack()


root = Tk()
app = course(root)
root.mainloop()
