from tkinter import *
from tkinter import messagebox
from tkinter import simpledialog


class info:
    def __init__(self, master):
        self.master = master
        self.master.withdraw()  # this line of code withdraw the master windows or root
        master.title('Info')
        master.geometry('600x300')
        self.w = Label(master, text='Program Title')
        self.w.pack()

        messagebox.showinfo('Welcome', 'Welcome to the program.....')
        name = simpledialog.askstring('Name', 'What is your name?')
        age = simpledialog.askinteger('Age', 'How old are you?')

        # WE must use string on age because we can only concatenate string or link strings together
        output = 'Your name is ' + name + ' ,and you are ' + str(age) + ' years old.'
        output += '\nThank you for using this program.'
        output += '\nHave a nice day or evening!'
        messagebox.showinfo('Result', output)


root = Tk()
app = info(root)
root.mainloop()
