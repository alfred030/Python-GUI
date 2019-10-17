# https://www.youtube.com/watch?v=xcX6IRzsMvQ
from tkinter import *


class Drawing:
    def __init__(self, master):
        self.master = master
        master.title('Canvas Drawing')
        # master.resizable(0, 0)  # or master.resizable(False, false)
        master.maxsize(400, 700)
        master.minsize(200, 300)

        self.canvas1 = Canvas(self.master, width=300, height=500, bg='black')
        self.canvas1.pack()

        self.canvas1.create_polygon(10, 10, 20, 30, 30, 20, fill='red')
        self.canvas1.create_line(10, 10, 100, 100, fill='red')
        self.canvas1.create_text(125, 100, text='Origin', fill='white', font=('Time', 12))

        self.canvas1.create_line(20, 40, 20, 200, fill='red')
        self.canvas1.create_polygon(15, 200, 25, 200, 20, 230, fill='red')
        self.canvas1.create_text(30, 235, text='Pos Y', fill='white', font=('Time', 12))

        self.canvas1.create_line(40, 20, 220, 20, fill='green')
        self.canvas1.create_polygon(200, 15, 200, 25, 230, 20, fill='green')
        self.canvas1.create_text(250, 20, text='Pos X', fill='green', font=('Time', 12))

        self.canvas1.create_rectangle(150, 400, 220, 480, fill='green')
        self.canvas1.create_oval(146, 396, 154, 404, fill='red')
        self.canvas1.create_oval(216, 476, 224, 484, fill='red')
        self.canvas1.create_text(110, 400, text='(150,400)', fill='white')
        self.canvas1.create_text(260, 480, text='(220,480)', fill='white')


root = Tk()
canvas = Drawing(root)
root.mainloop()
