from tkinter import *
from tkinter import messagebox

root = Tk()
root.geometry("600x300")


def Left_click(event=None):
    print('Left')
    messagebox.showwarning("Left click", "You click on left button")



def Middle_click(event=""):
    print('Middle')
    messagebox.showerror("Left click", "You click on middle button")


def Right_click(event=''):
    print('Right')
    messagebox.showinfo("Left click", "You click on right button")


b1 = Button(root, text='Left click', command=Left_click)
b1.pack(anchor = W)
root.bind("<Button-1>", Left_click)

b2 = Button(root, text='middle click', command=Middle_click)
b2.pack()
root.bind("<Button-2>", Middle_click)

b3 = Button(root, text='right click', command=Right_click)
b3.pack()
root.bind("<Button-3>", Right_click)

root.mainloop()
