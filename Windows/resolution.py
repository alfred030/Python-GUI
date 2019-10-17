from tkinter import *

root = Tk()

# root.geometry('1600x1200+0+0')
root.update_idletasks()
width_value = root.winfo_screenwidth()
height_value = root.winfo_screenheight()
root.geometry("%dx%d+0+0" % (width_value, height_value))

print(width_value)
print(height_value)
root.mainloop()
