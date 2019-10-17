from tkinter import *
from tkinter import messagebox
from tkinter import ttk


def call_me():
    answer = messagebox.askyesnocancel('message', 'Installation complete')
    print(answer)
    if answer:
        print(answer)

    if answer == True:
        print(answer)
        root.destroy()


class message_box:
    def __init__(self, master):
        master.title('Message box')

        self.b = ttk.Button(master, text='Exit', command=call_me)
        self.b.pack()


root = Tk()
message = message_box(root)
root.mainloop()
