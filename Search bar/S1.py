from tkinter import *
from tkinter import ttk
import webbrowser


class Universal_search:
    def __init__(self, master):
        self.master = master

        # ------------------------------------------------------------------------------------------------
        # TODO: FUNCTIONS
        def Callback():
            webbrowser.open('http://google.com/search?q=' + self.entry1.get())

        def get(event):
            webbrowser.open('http://google.com/search?q=' + self.entry1.get())

        # ------------------------------------------------------------------------------------------------
        # TODO: FUNCTIONS
        width_of_window = 840
        height_of_window = 125

        width_value = master.winfo_screenwidth()
        height_value = master.winfo_screenheight()

        X_coordinate = (width_value / 2) - (width_of_window / 2)
        Y_coordinate = (height_value / 2) - (height_of_window / 2)

        master.geometry("%dx%d+%d+%d" % (width_of_window, height_of_window,
                                         X_coordinate, Y_coordinate))

        # ------------------------------------------------------------------------------------------------
        # TODO: APP
        master.title('Universal Search Bar')
        master.iconbitmap('search.png')

        # ------------------------------------------------------------------------------------------------
        # TODO: APP

        self.logo = PhotoImage(file='search.png').subsample(5, 5)
        self.label_image = Label(master, image=self.logo, text='TIA')
        self.label_image.grid(row=0, column=0, pady=10)

        self.label1 = ttk.Label(master, text='oogle', font=('Tme', 25, 'bold'))
        self.label1.grid(row=0, column=1, padx=5)

        self.entry1 = ttk.Entry(master, width=45, font=('Time', 16))
        self.entry1.grid(row=0, column=2)
        self.entry1.bind('<Return>', get)
        self.entry1.focus()

        self.my_button1 = ttk.Button(master, text='Search', width=10, command=Callback)
        # master.bind('<Return>', get)
        self.my_button1.grid(row=0, column=3, padx=10)

        master.wm_attributes('-topmost', 1)  # it is to put this windows on top off all open applications.


root = Tk()
app = Universal_search(root)
root.mainloop()
