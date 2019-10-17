from tkinter import *
from tkinter import ttk


class Text_widget:
    def __init__(self, master):
        self.master = master
        master.title('Drawing')
        master.resizable(0,0)

        self.canvas = Canvas(self.master)
        self.canvas.pack()
        self.canvas.configure(width=640, height=480)

        width_of_window = 640
        height_of_window = 480

        width_value = root.winfo_screenwidth()
        height_value = root.winfo_screenheight()

        X_coordinate = (width_value / 2) - (width_of_window / 2)
        Y_coordinate = (height_value / 2) - (height_of_window / 2)

        root.geometry("%dx%d+%d+%d" % (width_of_window, height_of_window,
                               X_coordinate, Y_coordinate))


        rectangle = self.canvas.create_rectangle(160, 120, 480, 360)  # width is the width of the line
        self.canvas.itemconfigure(rectangle, fill='yellow')
        arc = self.canvas.create_arc(160, 1, 480, 240, fill='green')
        self.canvas.itemconfigure(arc, start=0, extent=180)
        oval = self.canvas.create_oval(160, 120, 480, 360)

        polygon = self.canvas.create_polygon(160, 360, 320, 480, 480, 360, fill='blue')
        text = self.canvas.create_text(320, 240, text='Python', font=('Courier', 32, 'bold'))

        self.logo = PhotoImage(file='python_logo.gif')
        image = self.canvas.create_image(320, 240, image=self.logo)

        self.canvas.lift(text)
        self.canvas.lower(image)
        self.canvas.lower(image, text)  # this put the image bellow the text

        button = ttk.Button(self.canvas, text='Click me')
        self.canvas.create_window(320, 60, window=button)

        # self.canvas.itemconfigure(polygon, tag='shape')
        self.canvas.itemconfigure(rectangle, tag='shape')
        self.canvas.itemconfigure(oval, tags=('shape', round))

        self.canvas.itemconfigure('shape',
                                  fill='grey')  # this will change the bg off the rec and arc at the same time because we group them in the same tap
        print(self.canvas.gettags(oval))
        print(self.canvas.gettags(rectangle))


root = Tk()
app = Text_widget(root)
root.mainloop()
