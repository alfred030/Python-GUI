# https://www.youtube.com/watch?v=OCoIhsFN1kI&index=1&list=PLonlF40eS6nyjI_OlR21se8aE1LTtNH1g
# on python shell, try to import webbrowser first. if you do not have any error, you are good to go.

from tkinter import *
from tkinter import ttk
import webbrowser


def Callback(self):
    webbrowser.open('http://google.com/search?q=' + self.entry1.get())


def get(self, event):
    webbrowser.open('http://google.com/search?q=' + self.entry1.get())


class Universal_search:
    def __init__(self, master):
        self.master = master
        master.title('Universal Search Bar')

        self.label1 = ttk.Label(self.master, text='Query')
        self.label1.grid(row=0, column=0)

        self.entry1 = ttk.Entry(self.master, width=50)
        self.entry1.grid(row=0, column=1)


root = Tk()
app = Universal_search(root)
root.mainloop()
