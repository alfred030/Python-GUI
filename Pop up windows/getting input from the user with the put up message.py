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

        output = 'your name is {}, and you are {} years old.'.format(name, age)
        output += '\nThank you for using this program.'
        output += '\nHave a nice day or evening!'
        print(output)
        messagebox.showinfo('Result', output)


root = Tk()
app = info(root)
root.mainloop()
