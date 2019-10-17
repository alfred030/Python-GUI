from tkinter import *
from tkinter import ttk

# this is the main root or main window
root = Tk()
root.title("The Most Smiling Girl in My Whole Family" )
label1 = ttk.Label(root, text ='Hello, Tkinter!')
label1.pack()

root.resizable(False, False)


# this code will change the text in the label
label1.config(text = 'hello Tia')
# this will stretch the label as more text is added to the label.
label1.config(text = 'hello Tia, it\'s been a while since we met a the gas station last time. Great to see you again!')
label1.config(wraplength = 150)

label1.config(text = '''Education is the most important aspect of our life. It is also the key that unlocks the door of 
opportunity. It determines our future and our level of success. The most famous learning association is the university. Some people believe 
that university education should be free, others disagree. In my point of view, college education should be free and supported
by governments because it will reduce crime, avoid students from dropping out from school and joining gangs, help students  to
have peace of mind after graduation without thinking about how they are going to do to pat back their student loans because
a degree does not always guaranty a job at the end.''')

# this means each line of the text will be 150 pixels
label1.config(wraplength = 500)
# position
label1.config(justify = RIGHT)
label1.config(justify = CENTER)
label1.config(justify = LEFT)

label1.config(text = 'hello Tia, it\'s been a while since we met a the gas station last time. Great to see you again!')
label1.config(wraplength = 150)
label1.config(foreground = 'white', background = 'green', font = "courier, 14")
#e1d8b9

label1.config(text = 'Tchinda Vanessa')
label1.config(compound = 'bottom')

# photo start with upper case and Image too. Right click on the image location-properties and copy the path
# choice \ to \\
logo = PhotoImage(file = 'G:\\All programing\\Python\\VA.PNG').subsample(5, 5)
label1.config(image = logo)


label2 = ttk.Label(root,
                   font = "courier, 17",
                   foreground = 'white', background = 'green',
                   text =' This Girl really know how to laugh ohoooo.\n\t I love this smile. ').pack()

'''
# this to display the text
label1.config(compound = 'text')
# this will display the text in the center of the image
label1.config(compound = 'center')
# this will display the text at the right of the image
label1.config(compound = 'center')
'''
# this configuration will store the image into tk.
label1.img = logo
label1.config(image = label1.img)
 

root.mainloop()
