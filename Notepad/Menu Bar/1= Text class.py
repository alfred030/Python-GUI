from tkinter import *


class text_editor:
    def __init__(self, master):
        master.title("Notepad")


root = Tk()
app = text_editor(root)
root.mainloop()
