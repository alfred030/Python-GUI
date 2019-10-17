from tkinter import *
from tkinter import ttk
from tkinter import messagebox

# foreground="white"
# bg='black'

class text_editor:
    def __init__(self,master):
        self.master=master
        master.title("text pad")
        self.text_area = Text(font=("Time", 18))
        # Fill is to fill it in both X direction
        # expand is to expand the y Direction
        self.text_area.pack(fill=BOTH, expand=1, padx=10, pady=1)
        self.text_area.focus()

        self.main_menu=Menu()
        self.master.config(menu=self.main_menu)

        self.file_menu=Menu(self.main_menu)
        self.main_menu.add_cascade(label="File",menu=self.file_menu)

        self.file_menu = Menu(self.main_menu)
        self.main_menu.add_cascade(label="Edit", menu=self.file_menu)



        #self.yscroll = Scrollbar(master, orient=VERTICAL, command=self.text_area.yview)
        #self.text_area.config(yscrollcommand=self.yscroll.set)


        #self.yscroll.pack(side=RIGHT, fill='y')


root = Tk()
app = text_editor(root)
root.mainloop()