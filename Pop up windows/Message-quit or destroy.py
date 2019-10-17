from tkinter import *
from tkinter import messagebox
from tkinter import ttk


def call_me():
    answer = messagebox.askquestion('Exit', 'Do you want exit?')
    if answer:
        print(answer)

    if answer == 'yes':
        print(answer)

        root.quit()
    else:
        print('this program is running')


class message_box:
    def __init__(self, master):
        master.title('Message box')

        self.b = ttk.Button(master, text='message', command=call_me)
        self.b.pack()


root = Tk()
message = message_box(root)
root.mainloop()
