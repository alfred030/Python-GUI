# https://www.youtube.com/watch?v=gjU3Lx8XMS8&t=768s
from tkinter import *
from tkinter import ttk

root = Tk()

width_of_window = 400
height_of_window = 200

width_value = root.winfo_screenwidth()
height_value = root.winfo_screenheight()

X_coordinate = (width_value / 2) - (width_of_window / 2)
Y_coordinate = (height_value / 2) - (height_of_window / 2)

root.geometry("%dx%d+%d+%d" % (width_of_window, height_of_window,
                               X_coordinate, Y_coordinate))

b = ttk.Button(root, text='Rice')
b.grid(row=0, column=0)

print(X_coordinate)
print(Y_coordinate)

print('\n')

print(width_value)
print(height_value)

root.mainloop()
