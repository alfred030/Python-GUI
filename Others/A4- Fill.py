from tkinter import *

root = Tk()

one = Label(root, text = "One", bg="red", fg="white")
one.pack()
two = Label(root, text = "Two is my\n favorite\n number ", bg="green", fg="black")
two.pack(fill=X)
three = Label(root, text = "Three is my\n favorite\n number ", bg="gray", fg="white")
three.pack(side=LEFT, fill=Y)

three = Label(root, text = "Rice", bg="purple", fg="white")
three.pack(side=RIGHT, fill=Y)

three = Label(root, text = "Number ", bg="gray", fg="white")
three.pack(side=BOTTOM, fill=X)


root.mainloop()
