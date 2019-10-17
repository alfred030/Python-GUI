from tkinter import *


class Text_widget:
    def __init__(self, master):
        self.master = master
        master.title('Drawing')

        self.canvas = Canvas(self.master)
        self.canvas.pack()
        self.canvas.configure(width=640, height=480)
        line = self.canvas.create_line(160, 360, 480, 120, fill='blue', width=5)  # width is the width of the line
        self.canvas.itemconfigure(line, fill='green')
        print(self.canvas.coords(line))
        self.canvas.coords(line, 0, 0, 320, 240, 640, 0)

        self.canvas.itemconfigure(line, smooth=True)
        self.canvas.itemconfigure(line, splinesteps=5)  # the line is very rough line
        self.canvas.itemconfigure(line, splinesteps=150)  # we have a smooth line
        # self.canvas.delete(line)  # this is to delete the line

        # image = PhotoImage(file='PY.gif')
        # self.text.image_create(INSERT, image=image)


root = Tk()
app = Text_widget(root)
root.mainloop()
