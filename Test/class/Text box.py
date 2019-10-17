from tkinter import *


class text:
    def __init__(self, master):
        self.master = master
        master.title('Text')

        self.text1 = Text(self.master, height=10, width=50)
        self.text1.pack()

        self.text1.configure(state=NORMAL)  # always config the state to normal before insetting anything
        self.text1.insert(INSERT, 'Line 1.........\n\n')
        self.text1.insert(INSERT, 'Line 2.........')

        self.text1.configure(state=DISABLED) # you can now disable it after insetting the text


root = Tk()
app = text(root)
root.mainloop()
