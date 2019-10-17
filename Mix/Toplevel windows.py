from tkinter import *
from tkinter import ttk


def new_windows():
    new = Toplevel()
    new.geometry('200x200')
    new.title('rest')

    L = Label(new, text='I was reset')
    L.pack()


def Cal():
    cal = Toplevel()
    cal.geometry('800x800')
    cal.title('Calculator')

    def click_me():
        v = var1.get()
        print(v)

        if v == 1:
            print('You are male')
        else:
            print('You are female')

    global var1
    var1 = StringVar()

    r1 = Radiobutton(cal, text='Male', value='radio 1', variable=var1)
    r1.pack()

    r2 = Radiobutton(cal, text='Female', value='radio 2', variable=var1)
    r2.pack()

    B = Button(cal, text='print', command=click_me)
    B.pack()


def Restaurant():
    rest = Toplevel()
    rest.geometry('500x500')
    rest.title('Restaurant')
    label = Label(rest, text='Rice')
    label.pack()

    frame = LabelFrame(rest, text='Dinner', bd=5, relief=SUNKEN, width=300, height=200)
    frame.pack()
    B1 = ttk.Button(rest, text='Rest', command=new_windows)
    B1.pack()


class Login:
    def __init__(self, master):
        master.title('')
        master.geometry('300x300+0+0')

        B = ttk.Button(master, text='Calculator', command=Cal)
        B.pack()

        B1 = ttk.Button(master, text='Restaurant', command=Restaurant)
        B1.pack()


root = Tk()
app = Login(root)
root.mainloop()
