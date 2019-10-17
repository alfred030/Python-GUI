from tkinter import *


def click_me():
    v = var1.get()
    print(v)

    if v == 'radio 1':
        print('You are male')
    else:
        print('You are female')


class button:
    def __init__(self, master):
        master.title('Button')
        root.geometry('300x300')

        # value works only with radiobutton and text variable with checkbutton
        global var1
        var1 = StringVar()  # with IntVar, the value can only be a number and both with StringVar(words and number)

        r1 = Radiobutton(master, text='Male', value='radio 1',
                         variable=var1)  # value allow us tp select only one button at the same time
        r1.pack()

        r2 = Radiobutton(master, text='Female', value='radio 2', variable=var1)
        r2.pack()

        B = Button(master, text='print', command=click_me)
        B.pack()


root = Tk()
app = button(root)
root.mainloop()
