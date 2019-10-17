from tkinter import *
from tkinter import ttk

# this is the main root or main window
root = Tk()
root.geometry("600x400")

# this will look different from the windows button

'''button = Button(root, text = "click me")
button.pack()'''

# this will look like windows button because off ttk
button =ttk.Button(root, text = "click me")
button.pack()

# this function is to configure the button to write Tia Leo when we click on it.
# this to make this button functional.
def calback():
    print ('Tia Leo')
button.config(command = calback)

# this will the content of this button
button.invoke()

# this to disable the button so that it will not respond again.
button.state(["disabled"])

# this will check to see if the button is disable or enable.
# this will return true because the button is disable.
button.instate(["disabled"])

# this to enable the button again.
button.state(["!disabled"])

#this will return true because the button is enable.
button.instate(["disabled"])


# this to at image to the button and display it to the left off the button.
# NB: LEFT is in upper case
logo = PhotoImage(file = 'python1.gif')
button.config(image = logo, compound = LEFT)

# this to reduce the size of the image in both direction.
# 5 pixels in X and 5 pixels in Y direction.
small_logo = logo.subsample(5,5)
button.config(ima = small_logo)

root.mainloop()







