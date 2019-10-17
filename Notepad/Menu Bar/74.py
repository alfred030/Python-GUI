from datetime import time, datetime
from tkinter import *
from tkinter import ttk, colorchooser
from tkinter import messagebox
from tkinter import filedialog
import webbrowser


class text_editor:
    def __init__(self, master):
        self.current_open_ile = None

        self.open_file = None
        self.master = master
        self.master.title("Notepad")
        self.scroll = Scrollbar(master)
        self.scroll.pack(side=RIGHT, fill=Y)

        self.text = Text(self.master, wrap=WORD, undo=True, font=("Time", 14),
                         yscrollcommand=self.scroll.set)
        self.text.pack(fill=BOTH, expand=1, padx=5, pady=5)
        self.text.focus()
        self.text.pack(side=LEFT)
        self.scroll.configure(command=self.text.yview)

        master.option_add('*tearOff', False)
        self.menubar = Menu(master)
        master.config(menu=self.menubar)

        self.file_ = Menu(self.menubar)
        self.edit_ = Menu(self.menubar)
        self.format_ = Menu(self.menubar)
        self.view_ = Menu(self.menubar)
        self.help_ = Menu(self.menubar)
        # this to add the menu to the menu bar.
        self.menubar.add_cascade(menu=self.file_, label='File')
        self.menubar.add_cascade(menu=self.edit_, label='Edit')
        self.menubar.add_cascade(menu=self.format_, label='Format')
        self.menubar.add_cascade(menu=self.view_, label='View')
        self.menubar.add_cascade(menu=self.help_, label='Help')


def main():
    root = Tk()
    app = text_editor(root)
    root.mainloop()


if __name__ == '__main__':  main()
