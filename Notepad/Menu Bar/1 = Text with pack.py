from tkinter import *


class text_editor:
    def __init__(self, master):
        master = master
        master.title("text pad")
        text_area = Text(width=50, heigh=10)
        text_area.pack()
        text_area.focus()


root = Tk()
app = text_editor(root)
root.mainloop()
