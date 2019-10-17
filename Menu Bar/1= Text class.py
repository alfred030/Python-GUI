from tkinter import *
class text_editor:
    def __init__(self,master):
        self.master = master
        master.title("text pad")


root = Tk()
app = text_editor(root)
root.mainloop()