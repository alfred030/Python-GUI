
from tkinter import *
from tkinter import ttk
import webbrowser


def Callback(self):
    webbrowser.open('http://google.com/search?q=')



class Universal_search:
    def __init__(self, master):
        self.master = master
        self.master.withdraw()

        self.my_button1 = ttk.Button(self.master, text='',command=Callback(self))



root = Tk()
app = Universal_search(root)
root.mainloop()
