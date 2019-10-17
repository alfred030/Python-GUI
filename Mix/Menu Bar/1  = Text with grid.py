from tkinter import *


class text_editor:
    def __init__(self, master):
        master = master
        master.title("text pad")
        text_area = Text(width=50, heigh=10, font=("Time", 14))
        text_area.grid(column=0, row=0, padx=10, pady=10)
        text_area.focus()


root = Tk()
app = text_editor(root)
root.mainloop()
