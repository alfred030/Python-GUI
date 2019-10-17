from tkinter import *
class text_editor:
    def __init__(self,master):
        self.master = master
        master.title("text pad")
        self.text_area = Text(font=("Time", 18))
        # Fill is to fill it in both X direction
        # expand is to expand the y Direction
        self.text_area.pack(fill=BOTH, expand=1, padx=10, pady=10)
        self.text_area.focus()






root = Tk()
app = text_editor(root)
root.mainloop()