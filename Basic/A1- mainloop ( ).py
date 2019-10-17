# this to import everything that we need from Tkinter
from tkinter import *
# this for label
from tkinter import ttk

# root is just a blank window
root = Tk()

# this line of code is actually saying put this text in the main window.
label = Label(root, text ="I will not be able to go to school tomorrow\n because I am not feeling well")

# this line of code is to really display what we wrote on the screen
label.pack()

# this line of code make sure the your window will constantly display until you close it yourself.
# this going to continue looping until we brake the loop by closing the program.
root.mainloop()
