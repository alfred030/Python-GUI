from tkinter import *
from tkinter import ttk, messagebox
import webbrowser


class Universal_search:
    def __init__(self, master):
        self.master = master

        master.resizable(0, 0)

        # ------------------------------------------------------------------------------------------------
        # TODO: FUNCTIONS
        # we will create only one variable and share it between buttons because we do not 2 button to be selected at once.
        # we on want only one button to be selected
        self.var = StringVar()

        def Clear():
            self.entry1.delete(0, END)
            self.entry1.focus()

        def Callback():
            if self.var.get() == '':
                messagebox.showwarning('Universal search', 'Please select\nThe search engine')
            if self.var.get() == 'google':
                webbrowser.open('http://google.com/search?q=' + self.entry1.get())
            elif self.var.get() == 'youtube':
                webbrowser.open('https://www.youtube.com/search?q=' + self.entry1.get())
            elif self.var.get() == 'map':
                webbrowser.open('https://www.google.com/maps/@29.6895871,-95.5669888,15z/search?q=' + self.entry1.get())

        def get(event):
            if self.var.get() == '':
                messagebox.showwarning('Universal search', 'Please select\nThe search engine')
            elif self.var.get() == 'google':
                webbrowser.open('http://google.com/search?q=' + self.entry1.get())
            elif self.var.get() == 'youtube':
                webbrowser.open('https://www.youtube.com/search?q=' + self.entry1.get())
            elif self.var.get() == 'map':
                webbrowser.open('https://www.google.com/maps/@29.6895871,-95.5669888,15z/search?q=' + self.entry1.get())

        # ------------------------------------------------------------------------------------------------
        # TODO: FUNCTIONS
        width_of_window = 525
        height_of_window = 75

        width_value = master.winfo_screenwidth()
        height_value = master.winfo_screenheight()

        X_coordinate = (width_value / 2) - (width_of_window / 2)
        Y_coordinate = (height_value / 2) - (height_of_window / 2)

        master.geometry("%dx%d+%d+%d" % (width_of_window, height_of_window,
                                         X_coordinate, Y_coordinate))

        # ------------------------------------------------------------------------------------------------
        # TODO: APP
        master.title('Universal Search Bar')
        # master.iconbitmap('globe.png')

        # ------------------------------------------------------------------------------------------------
        # TODO: APP

        # self.logo = PhotoImage(file='search.png').subsample(20, 20)
        # self.label_image = Label(master, image=self.logo, text='TIA')
        # self.label_image.grid(row=0, column=0, pady=5)

        self.label1 = ttk.Label(master,
                                text='Search\nEngine',
                                foreground='blue',
                                font=('Tme', 14, 'bold'))
        self.label1.grid(row=0, column=1, padx=2)

        self.entry1 = ttk.Entry(master, width=40, font=('Time', 12))
        self.entry1.grid(row=0, column=2)
        self.entry1.bind('<Return>', get)
        self.entry1.focus()

        self.my_button_button = ttk.Button(master, text='Search', width=10, command=Callback)
        # master.bind('<Return>', get)
        self.my_button_button.grid(row=0, column=3, padx=5, sticky=W + E)

        self.map_button = ttk.Radiobutton(self.master,
                                          value='map',
                                          variable=self.var,
                                          text='Map')
        self.map_button.grid(row=2, column=2, sticky=W)

        self.google_button = ttk.Radiobutton(self.master,
                                             value='google',
                                             variable=self.var,
                                             text='Google')
        self.google_button.grid(row=2, column=2)

        self.youtube_button = ttk.Radiobutton(self.master,
                                              value='youtube',
                                              variable=self.var,
                                              text='YouTube')
        self.youtube_button.grid(row=2, column=2, sticky=E)

        self.L1 = Label(self.master, text='>>>>>>>', foreground='red')
        self.L1.grid(row=2, column=0, columnspan=2, sticky=W)

        self.L1 = ttk.Button(self.master, text='Clear', command=Clear)
        self.L1.grid(row=2, column=3, sticky=E, padx=5)

        master.wm_attributes('-topmost', 1)  # it is to put this windows on top off all open applications.


root = Tk()
app = Universal_search(root)
root.mainloop()
