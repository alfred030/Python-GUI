from tkinter import *
from tkinter import ttk
from tkinter import messagebox


# foreground="white"
# bg='black'

class text_editor:
    def __init__(self, master):
        master.title("text pad")
        text_area = Text(font=("Time", 18))

        text_area.pack(fill=BOTH, expand=1, padx=10, pady=1)
        text_area.focus()

        main_menu = Menu()
        master.config(menu=main_menu)

        file_menu = Menu(main_menu, tearoff=0)
        main_menu.add_cascade(label="File", menu=file_menu)

        file_menu = Menu(main_menu, tearoff=0)
        main_menu.add_cascade(label="Edit", menu=file_menu)


root = Tk()
app = text_editor(root)
root.mainloop()
