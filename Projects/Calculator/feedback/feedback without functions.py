#!/usr/bin/python3
# feedback_template.py by Barron Stone
# This is an exercise file from Python GUI Development with Tkinter on lynda.com
import random
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
root = Tk()

root.resizable(False, False)
root.title('Explore California Feedback')
root.configure(background = '#e1d8b9')

#------------------------------------------------frames-------------------------------------------------
f1 = Frame(root,  background = '#e1d8b9')
f1.pack(side = TOP)
f2 = Frame(root,  background = '#e1d8b9')
f2.pack(side = TOP)
f3 = Frame(root,  background = '#e1d8b9')
f3.pack(side = TOP)


labeimage = ttk.Label(f1, background = '#e1d8b9', text ='')
labeimage.grid(row = 0, column = 0, rowspan = 2,)

logo = PhotoImage(file ='tour_logo2.gif').subsample(1, 1)
labeimage.config(image = logo)

labeimage.config(compound = 'center')

l1 = ttk.Label(f1 ,text = 'Thanks for Exploring!',
               background = '#e1d8b9',
               font = ('time', 18, 'bold'),).grid(row = 0, column = 1)
               
l2 = ttk.Label(f1, wraplength = 350,
               font = ('time', 12, ''),
               background = '#e1d8b9',
                  text = ("We're glad you chose Explore California for your recent adventure.  "
                          "Please tell us what you thought about the 'Desert to Sea' tour.\n"))
l2.grid(row = 1, column = 1)


labelname = ttk.Label(f2,
                      background = '#e1d8b9',
                      text = 'Name:').grid(row = 0, column = 0, padx = 5, sticky = 'sw')

labelemail = ttk.Label(f2,
                       background = '#e1d8b9',
                       font = (),
                       text = 'Email:').grid(row = 0, column = 1, padx = 5, sticky = 'sw')

labelcontent = ttk.Label(f2,
                         background = '#e1d8b9',
                         text = 'Comments:').grid(row = 2, column = 0, padx = 5, sticky = 'sw')

entry_name = ttk.Entry(f2, width = 30,
                       font = ('Arial', 10)).grid(row = 1, column = 0, padx = 5, sticky = 'sw')

entry_email = ttk.Entry(f2, width = 30,
                        font = ('Arial', 10)).grid(row = 1, column = 1, padx = 5, sticky = 'sw')

text_comments = Text(f2, width = 48,
                     height = 10,
                     font = ('Arial', 12)).grid(row = 3, column = 0, padx = 5,columnspan=2)



ttk.Button(f3, text = 'Submit',
                   ).grid(row = 4, column = 0, padx = 5, pady = 5, sticky = 'w')

    

ttk.Button(f3, text = 'Clear',
                   ).grid(row = 4, column = 1, padx = 5, pady = 5, sticky = 'ns')



from tkinter import messagebox

def iExit():
    qExit = messagebox.askyesno("Feedback",
                                "You program is still runing!\n"
                                "Do you want to quit?")
    if qExit > 0:
        root.destroy()
        return
        
ttk.Button(f3,text = 'Exit',
           command=lambda: iExit()).grid(row=4, column=2,padx = 5, pady = 5, sticky = 'e')
            
                

       
    
root.mainloop()
    

