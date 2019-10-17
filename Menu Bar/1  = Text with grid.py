from tkinter import *
class text_editor:
    def __init__(self,master):
        self.master = master
        master.title("text pad")
        self.text_area = Text(width=50, heigh=10,font=("Time", 14))
        self.text_area.grid(column=0, row=0, padx=10, pady=10)







root = Tk()
app = text_editor(root)
root.mainloop()