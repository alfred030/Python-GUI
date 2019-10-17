from tkinter import *
from tkinter import ttk        
    
root = Tk()
root.geometry("600x400")

# this is to  create a combobox
# always set the text variable
month = StringVar()
combobox = ttk.Combobox(root, width = 40, textvariable = month)
combobox.pack()

# this will be display in the drop down menu.
# the first want '', means you can choice a blank if you do not want any selection.
combobox.config(values = ( '','Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun',
                          'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec',))
'''
# to get the value of the curent year
print(month.get())
# to se the value of the year
month.set('Dec')
# to set a value of the Not a moth at the top level
month.set('Not a month!')
'''

# will put underscore after from 1190 to avoid confusion with from tkinter.
# this because from is a special character that we use to import.
year = StringVar()
spinbox = Spinbox(root, width = 30, from_ = 1990, to = 2018, textvariable = year)  
spinbox.pack()

year1 = StringVar()
combobox1 = ttk.Combobox(root, width = 40, textvariable = year1)
combobox1.pack()
combobox1.config(values = ('', '2010','2011','2012','2013','2014','2015','2016',
                    '2017','2018','2019','2020','2021',))

# this is to print the current year.
print(year.get())

root.mainloop()
