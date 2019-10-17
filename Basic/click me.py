# this all of the function and variables from tkinter.
from tkinter import * 

# this to import the theme from tkinter. theme is like a background color or font.
from tkinter import ttk

# this will create the top parent windows which i can use as a parent windows for others widgets.
# the reference for the parent windows will be store d in the variable call root
root = Tk()
# NB: the tkinter will always begin with this 3 lines of code.
root.geometry("600x400")

# now we have a windows. Let create a button to at to it.
# the first parameter is the root and the second parameter is the test that we want display.
# this will not display if we execute this command because we need to pack it on the parent windows using the pack command.
# this is because tk do ont know where to put it yet.
button = ttk.Button(root, text = 'Click Me')

# this will look like at standard windows button because we use the theme function.
# pack is to display the click  me button on the screen.
button.pack()
# this to print the content of the label test in python IDE.
print(button['text'])

# this to print the content of the label test in python Shell.
button['text']

# this to change the test in the label.  first method
button['text'] = 'Press Me'
button['text'] = 'Press Here'
button['text'] = 'Press Here User'

# this to change the test in the label.  Second method
button.config(text = 'Push Me')
button.config(text = 'Press Here User')

# This command will pack the label on the screen without storing it in any variable.
# this can not be use later in the program because we it is not being stored in the  variable
# this just to pack Hello, tk on tke screen at on ce
ttk.Label(root, text ='Hello, Tkinter!').pack()

# proper way
label1 = ttk.Label(root, text ='Hello, Tkinter!')
label1.pack()

button = ttk.Button(root, text ='Hello, Tkinter!')
button.pack()

# this the different between the button and the label
# NB: button most be use for every button that we want to create.
Label = ttk.Label(root, text ='Hello, Tkinter!')
Label.pack()

button1 = ttk.Button(root, text ='Hello, Tkinter!')
button1.pack()

labe2 = ttk.Label(root, text ='Final exam  for the end of the semester.')
labe2.pack()

button2 = ttk.Button(root, text ='click here to upload your final.')
button2.pack()

button3 = ttk.Button(root, text ='Click here to submit your  final.')
button3.pack()

root.mainloop()
