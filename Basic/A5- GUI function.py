from tkinter import *

root = Tk()

def printName():
    print("Hello, my name is Tia")

button_1 = Button(root, text="print my name", command = printName)
button_1.pack()


def printAge(event):
    print("Hello, I am 24")
    print('My sister is 20')
    print('My uncle is 50')
    print('My mother is 45')
    print('My father is 55')

button_2 = Button(root, text="print my family ages")
button_2.bind('<Button-1>',printAge) # we call the function here call bind which take 2 parameters
button_2.pack()                      # "<Button-1>" represent the left click. this means whenever
                                     # we right click,print the function Age.

# this is how we can our computer programming functioning by binning functions to widgets
root.mainloop()
