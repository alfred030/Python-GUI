from tkinter import *
from tkinter import ttk

# this is the main root or main window
root = Tk()
root.geometry("600x400")

label_1 = Label(root, text ="Enter your user name:")
label_2 = Label(root, text ="Enter your password:")

# this means that we need a blank where user can type something in and in the main root
# this means the user name will be 40 visible characters length and the password 30 visible characters lenght.
entry_1 = Entry(root, width = 40)
entry_2 = Entry(root, width = 40)
# to hid the password
entry_2.config(show = '*')
#to get the password. 
entry_2.get()

label_1.grid(row=0)
label_2.grid(row=1)

entry_1.grid(row=0, column=1)
entry_2.grid(row=1, column=1)

button_3 = ttk.Button(root, text ='Click here to submit.')
button_3.grid(row=2, column=1)

root.mainloop()
