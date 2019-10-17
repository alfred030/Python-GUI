from tkinter import *
from tkinter import ttk


class Slider:
    def __init__(self, master):
        self.master = master
        master.title('Slider')

        self.slider1 = Scale(self.master, from_=10, to=170, orient=HORIZONTAL)
        self.slider1.pack()

        self.B = ttk.Button(self.master, text='result', command=self.result)
        self.B.pack()

    def result(self):
        result = self.slider1.get()
        print(result)
        print(result * 2)


root = Tk()
slider = Slider(root)
root.mainloop()
