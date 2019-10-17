from tkinter import *
from tkinter import ttk
from tkinter import filedialog


def open_file(event=''):
    result = filedialog.askopenfile(initialdir='/', title='Select file',
                                    filetype=(('text file', '.txt'), ('All files', '*.*')))

    for c in result:
        print(result)
        # text.delete(1.0, END)
        text.insert(INSERT, c)


class scale:
    def __init__(self, master):
        master.title('')

        global text
        text = Text(master, wrap=WORD, font=('Time', 14))
        text.pack()
        text.focus()

        B = ttk.Button(master, text='Open', command=open_file)
        B.pack()
        master.bind('<Control-o>', open_file)


root = Tk()
app = scale(root)
root.mainloop()
