from tkinter import *


class text_editor:
    def __init__(self, master):
        master.title("text pad")
        text_area = Text(font=("Time", 18))
        # Fill is to fill it in both X direction
        # expand is to expand the y Direction
        text_area.pack(fill=BOTH, expand=1, padx=10, pady=10)
        text_area.focus()


root = Tk()
app = text_editor(root)
root.mainloop()
