#!/usr/bin/python3
# menu.py by Barron Stone
# This is an exercise file from Python GUI Development with Tkinter on lynda.com

from tkinter import *
from tkinter import ttk        
    
root = Tk()
root.title("Menu Bar in Tkinter")
root.config(background ='black')
root.geometry("900x600")

# always include this on your before you start creating your menu to avoid unexpected resuld.
root.option_add('*tearOff', False)

# this to create the menu bar
menubar = Menu(root)
root.config(menu = menubar)

# these are items of the menu bar.
# Use underscore to avoid conflict because you might use key word such as format and help in tkinter.
file_ = Menu(menubar)
edit_ = Menu(menubar)
format_ = Menu(menubar)
run_ = Menu(menubar)
option_ = Menu(menubar)
window_ = Menu(menubar)
help_ = Menu(menubar)
# this to add the menu to the menu bar.
menubar.add_cascade(menu = file_, label = 'File')
menubar.add_cascade(menu = edit_, label = 'Edit')
menubar.add_cascade(menu = format_, label = 'Format')
menubar.add_cascade(menu = run_, label = 'Run')
menubar.add_cascade(menu = option_, label = 'Option')
menubar.add_cascade(menu = window_, label = 'Window')
menubar.add_cascade(menu = help_, label = 'Help')

# the seperator is to seperate the first submenu with others.
file_.add_command(label = 'New', command = lambda: print('New File'))
file_.add_separator()
file_.add_command(label = 'Open...', command = lambda: print('Opening File...'))
file_.add_command(label = 'Save...', command = lambda: print('Saving File...'))
file_.add_separator()
file_.add_command(label = 'Quit')

# this to add keyboard shot cut.
file_.entryconfig('New', accelerator = 'Ctrl+N')
file_.entryconfig('Open...', accelerator = 'Ctrl+O')
file_.entryconfig('Save...', accelerator = 'Ctrl+S')

logo = PhotoImage(file = "python3.gif").subsample(5, 5)
file_.entryconfig('Open...', image = logo, compound = 'left')

# this to desable Quit submenu so that yhe user cannot select it.
file_.entryconfig('Quit', state = 'disabled')

'''
# this to delete a file menu if i want.
file_.delete('Save')
'''

# this to add submenu to save.
save = Menu(file_)
file_.add_cascade(menu = save, label = 'Save')
save.add_command(label = 'Save As',command = lambda: print('Saving As...'))
save.add_command(label = 'Save All', command = lambda: print('Saving All...'))
save.add_command(label = 'Exit')

# this to check button on the menu bar edit.
choice = IntVar()
edit_.add_radiobutton(label = 'One', variable = choice, value = 1)
edit_.add_radiobutton(label = 'Two', variable = choice, value = 2)
edit_.add_radiobutton(label = 'Three', variable = choice, value = 3)

# this is to create a pop up menu at a specific location.
file_.post(400, 300)

root.mainloop()
