
from tkinter import *
from tkinter import ttk        
    
root = Tk()

frame = ttk.Frame(root)
frame.pack()

frame.config(height = 100, width = 200)
# there 6 different type of frames
# FLAT, RAISED, SUNKEN, SOLID, RIDGE, GROOVE
frame.config(relief = RAISED)

button = ttk.Button(frame, text = 'Rescare SEA')
button.pack()
# x direction is 10 and y direction is 10
frame.config(padding = (10, 10))
'''
logo = PhotoImage(file = 'C:\\Users\\Leo\\Desktop\\Python\\tour_logo.gif')
# text position, we can use TOP, RIGHT,LEFT, and BOTTOM
button.config(image = logo, compound = BOTTOM)
small_logo = logo.subsample(1,1)
button.config(ima = small_logo)
'''
ttk.LabelFrame(root, height = 100, width = 300, text = 'My Frame').pack()

root.mainloop()
