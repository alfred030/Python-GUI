#!/usr/bin/python3
# scrollbar.py by Barron Stone
# This is an exercise file from Python GUI Development with Tkinter on lynda.com

from tkinter import *
from tkinter import ttk        
    
root = Tk()

text = Text(root, width = 60,
            height = 15,
            font = ('Arial', 12),
            bg = 'white')

xscroll = ttk.Scrollbar(root, orient = HORIZONTAL, command = text .xview)
yscroll = ttk.Scrollbar(root, orient = VERTICAL, command = text .yview)
text .config(xscrollcommand = xscroll.set, yscrollcommand = yscroll.set)

text .grid(row = 0, column = 0, padx = 10, pady = 5)
xscroll.grid(row = 1, column = 0, sticky = 'ew')
yscroll.grid(row = 0, column = 1, sticky = 'ns')


root.mainloop()
