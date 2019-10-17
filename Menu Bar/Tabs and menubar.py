from tkinter import *
from tkinter import Menu
from tkinter import ttk
import time
import tkinter.messagebox as tm

root = Tk()

# Exit GUI cleanly
def _quit():
    root.quit()
    root.destroy()
    exit()

def exit():
    tm.showinfo('This is a Title', 'A Python GUI created using tkinter:\nThe year is 2015')
# Creating a Menu Bar
menuBar = Menu(root)
root.config(menu=menuBar)

## Add menu items
fileMenu = Menu(menuBar, tearoff=0)
fileMenu.add_command(label="New")
fileMenu.add_separator()
fileMenu.add_command(label="Exit", command=_quit)
menuBar.add_cascade(label="File", menu=fileMenu)

# Add another Menu to the Menu Bar and an item
helpMenu = Menu(menuBar, tearoff=0)
helpMenu.add_command(label="About")
menuBar.add_cascade(label="Help", menu=helpMenu)

# Tab Control introduced here -----------------------------------------
tabControl = ttk.Notebook(root)          # Create Tab Control

tab1 = ttk.Frame(tabControl)            # Create a tab
tabControl.add(tab1, text='Calculator')      # Add the tab

tab2 = ttk.Frame(tabControl)            # Add a second tab
tabControl.add(tab2, text='Restaurant')      # Make second tab visible


tab3 = ttk.Frame(tabControl)            # Add a second tab
tabControl.add(tab3, text='Login')      # Make second tab visible

tabControl.pack(expand=1, fill="both")  # Pack to make visible
# ~ Tab Control introduced here -----------------------------------------




root.mainloop()