
#Python 3 version

from tkinter import filedialog
from tkinter import *
 
root = Tk()
root.filename =  filedialog.asksaveasfilename(initialdir = "/",title = "Select file",
                 filetypes = (("jpeg files","*.jpg"),("all files","*.*")))
print (root.filename)

root.mainloop()