from tkinter import *
from tkinter import ttk

# this is the main root or main window
root = Tk()
root.geometry("600x400")

# checkbutton work the same as button. we can enable, disable, put pictures etc.
checkbutton = ttk.Checkbutton(root, text='Coffee')
'''
checkbutton1 = ttk.Checkbutton(root, text = 'Rice')
checkbutton2 = ttk.Checkbutton(root, text = 'Tomatoes')
checkbutton3 = ttk.Checkbutton(root, text = 'Banana')
'''
checkbutton.pack()
'''
checkbutton1.pack()
checkbutton2.pack()
checkbutton3.pack()
'''
# this to at image to the button and display it to the left off the button.
# NB: LEFT is in upper case
logo = PhotoImage(file='G:\\All programing\\Python\\python_logo.gif')
checkbutton.config(image=logo, compound=LEFT)

# this to reduce the size of the image in both direction.
# 5 pixels in X and 5 pixels in Y direction.
small_logo = logo.subsample(3, 3)
checkbutton.config(ima=small_logo)

# let configure the checkbutton to do something.
# we need to set a variable equal the the content of the checkbutton.
# on value means to show the content of the value when the checkbutton is check.
# off value means to show the value when the check button is not check.
# we have to set the content of the check button equal to StringVar
Coffee = StringVar()
checkbutton.config(variable=Coffee, onvalue='Coffee please!', offvalue='Nothing is selected')

''' to get the content of the checkbutton while it selected, we
have to type the following commend on the Python shell when we run the program already'''
Coffee.get()
# and the same comment get the content while it not selected
Coffee.get()

breakfast = StringVar()
ttk.Radiobutton(root, text='SPAM', variable=breakfast, value='SPAM').pack()
ttk.Radiobutton(root, text='Eggs', variable=breakfast, value='Eggs').pack()
ttk.Radiobutton(root, text='Sausage', variable=breakfast, value='Sausage').pack()
ttk.Radiobutton(root, text='Chicken', variable=breakfast, value='Chicken').pack()
ttk.Radiobutton(root, text='SPAM', variable=breakfast, value='SPAM').pack()

root.mainloop()
