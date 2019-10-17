from tkinter import *
from tkinter import ttk
from tkinter import scrolledtext

root = Tk()

# Using a scrolled Text control
scroll_W = 50
scroll_H = 20
scr = scrolledtext.ScrolledText(root, width=scroll_W, height=scroll_H, wrap=WORD)
scr.grid(column=0, sticky='WE', columnspan=3)

root.mainloop()
