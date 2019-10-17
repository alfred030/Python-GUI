

# ======================
# imports
# ======================
import tkinter as tk
from tkinter import ttk
from tkinter import Spinbox
from tkinter import scrolledtext

# Create instance
win = tk.Tk()

# Add a title
win.title("Python GUI")

# Disable resizing the GUI
# win.resizable(0,0)

# Modify adding a Label
aLabel = ttk.Label(win, text="A Label")
aLabel.grid(column=0, row=0)


# Modified Button Click Function
def clickMe():
    action.configure(text='Hello ' + name.get() + ' your number is ' + numberChosen.get())


# Changing our Label
ttk.Label(win, text="Enter a name:").grid(column=0, row=0)

# Adding a Textbox Entry widget
name = tk.StringVar()
nameEntered = ttk.Entry(win, width=10, textvariable=name)
nameEntered.grid(column=0, row=1)

# Adding a Button
action = ttk.Button(win, text="Click Me!", command=clickMe)
action.grid(column=2, row=1)
# action.configure(state='disabled')    # Disable the Button Widget

ttk.Label(win, text="Choose a number:").grid(column=1, row=0)
number = tk.StringVar()
numberChosen = ttk.Combobox(win, width=12, textvariable=number)
numberChosen['values'] = ("", 1, 2, 4, 42, 100)
numberChosen.grid(column=1, row=1)
numberChosen.current("0")

# Spinbox callback
def _spin():
    value = spin.get()
    print(value)
    scr.insert(tk.INSERT, value + '\n')

# Adding a Spinbox widget
spin = Spinbox(win, from_=0, to=10, width = 10, bd = 6) # bd=border width
spin.grid(column=0, row=2)
# ======================
win.mainloop()
