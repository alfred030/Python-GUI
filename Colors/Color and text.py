from tkinter import *
from tkinter import ttk

# this is the main root or main window
window = Tk()
window.geometry("600x400")
# this is the app title
window.title("Color in Tkinter")
# the app window here is 600x400 pixels
window.geometry("600x400")

window.config(background ='yellow')
label1 = ttk.Label(window, text ='hello Tia, it\'s been a while since we met a the gas station last time. Great to see you again!')
label1.pack()
label1.config(wraplength = 200)
label1.config(foreground = 'black', background = 'yellow')

# font is police in french
label1.config(foreground = 'black', font = 'times')

# bold is grad in french and time is police
label1.config(foreground = 'black', font = 'times 16 bold')

# this will keep the default font
label1.config(foreground = 'black', font = 'none 16 bold')

# 16 is the font size
label1.config(foreground ="red", background="white", font = 'times 16 bold italic underline')

window.mainloop()
