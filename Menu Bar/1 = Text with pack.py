from tkinter import *
class text_editor:
    def __init__(self,master):
        self.master = master
        master.title("text pad")
        self.text_area = Text(width=50, heigh=10)
        self.text_area.pack()
        self.text_area.focus()




root = Tk()
app = text_editor(root)
root.mainloop()