from tkinter import *
from tkinter import ttk, scrolledtext, messagebox


def submit():
    # root.withdraw()
    T = text.get(1.0, END)
    print(T)
    text.delete(1.0, END)
    messagebox.showinfo(title='Languages', message='You chose was Submitted!')


class entry:
    def __init__(self, master):
        master.title('Label')
        master.geometry('500x800')

        global text
        text = Text(master,
                    padx=10,
                    pady=10,
                    selectbackground='green',
                    wrap=WORD,
                    width=40,
                    height=20)
        text.pack()

        ttk.Button(master, text='Submit', command=submit).pack()


root = Tk()
app = entry(root)
root.mainloop()
