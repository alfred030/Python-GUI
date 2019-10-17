from tkinter import *
from tkinter import ttk


def do_nothing():
    print("I was press......")


root = Tk()
root.geometry("800x500")

# ----------------------------------------------------------------------------------------
# TODO MENU BAR
menu = Menu(root)
root.configure(menu=menu)

sub_menu = Menu(menu)
menu.add_cascade(label="File", menu=sub_menu)
sub_menu.add_command(label='Open', command=do_nothing)
sub_menu.add_separator()
sub_menu.add_command(label='Save ', command=do_nothing)
sub_menu.add_separator()
sub_menu.add_command(label='Print', command=do_nothing)

edit_menu = Menu(menu)
menu.add_cascade(label='Edit', menu=edit_menu)
edit_menu.add_command(label='Redo', command=do_nothing)
edit_menu.add_separator()
edit_menu.add_command(label='Undo', command=do_nothing)

# ----------------------------------------------------------------------------------------
# TODO MENU BAR

toolbar = Frame(root, bg="gray")

logo1 = PhotoImage(file='printer.png').subsample(1, 1)
printButton = ttk.Button(toolbar, command=do_nothing, width=1)
printButton.pack(side=LEFT, padx=2, pady=2)
printButton.config(image=logo1, compound=LEFT, command=do_nothing)

button = ttk.Button(toolbar, text='Python', command=do_nothing, width=6)
button.pack(side=LEFT, padx=2, pady=2)
logo = PhotoImage(file='P.gif').subsample(6, 6)
button.config(image=logo, compound=LEFT, command=do_nothing)


toolbar.pack(fill=X, side=TOP)

# ----------------------------------------------------------------------------------------
# TODO STATUS BAR

status = Label(root, text="preparing to do nothing..................................",
               bd=2,
               anchor=W,
               relief=SUNKEN)
status.pack(fill=X, side=BOTTOM)
# ----------------------------------------------------------------------------------------
#
root.mainloop()
