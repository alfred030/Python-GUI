from tkinter import *
from tkinter import ttk


class tabs:
    def __init__(self, master):
        self.value = ''
        self.master = master
        master.title('Tabs')
        master.geometry('600x300')

        self.tab_control = ttk.Notebook(self.master)

        self.tab1 = ttk.Frame(self.tab_control)
        self.tab_control.add(self.tab1, text='First Tab')

        self.tab2 = ttk.Frame(self.tab_control)
        self.tab_control.add(self.tab2, text='Second Tab')

        self.tab_control.pack(expand=1, fill='both')

        self.E1 = ttk.Entry(self.tab1)
        self.E1.pack()
        self.E1.focus()
        self.E1.bind('<Return>', self.return_hit)

        self.B1 = ttk.Button(self.tab2, text='Tab 2 button', command=self.button_click)
        self.B1.pack()

    def return_hit(self, *args):  # i can pass in *args or and event
        self.value = self.E1.get()
        print(self.value)
        self.E1.delete(0, END)

    @staticmethod
    def button_click():
        print('You have clicked on the button')


root = Tk()
Tabs = tabs(root)
root.mainloop()
