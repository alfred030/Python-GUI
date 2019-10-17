from tkinter import *
from tkinter import ttk, colorchooser
from tkinter import filedialog


def open_file(event=None):
    open_result = filedialog.askopenfile(initialdir='/', title='Select file',
                                         filetype=(('text file', '.txt'), ('All files', '*.*')))

    # if open_result != None:
    if open_result is not None:
        text.delete(1.0, END)
        for line in open_result:
            text.insert(END, line)
    open_result.close()


def save_file(event=None):
    Save = filedialog.asksaveasfile(mode='w', defaultextension='.txt')
    if Save is None:
        return

    text_save = text.get(1.0, END)
    Save.write(text_save)
    Save.close()


def color():
    clr = colorchooser.askcolor(title='select color')
    print(clr)
    text.configure(bg=clr[1])


class scale:
    def __init__(self, master):
        master.title('')
        master.resizable(FALSE, FALSE)

        global text
        text = Text(master, wrap=WORD, font=('Time', 14))
        text.pack()
        text.focus()

        B = ttk.Button(master, text='Open', command=open_file)
        B.pack(side=LEFT)

        B1 = ttk.Button(master, text='Save', command=save_file)
        B1.pack(side=LEFT)

        B2 = ttk.Button(master, text='Choose text zone color', command=color)
        B2.pack(side=RIGHT)

        master.bind('<Control-s>', save_file)
        master.bind('<Control-o>', open_file)


root = Tk()
app = scale(root)
root.mainloop()
