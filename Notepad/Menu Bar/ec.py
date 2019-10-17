from tkinter import *
from tkinter import ttk, colorchooser
from tkinter import filedialog


def open_file(self, event=None):
    self.open_result = filedialog.askopenfile(initialdir='/', title='Select file',
                                         filetype=(('text file', '.txt'), ('All files', '*.*')))

    # if open_result != None:
    if self.open_result is not None:
        self.text.delete(1.0, END)
        for line in self.open_result:
            self.text.insert(END, line)
    self.open_result.close()


def save_file(self, event=None):
    self.Save = filedialog.asksaveasfile(mode='w', defaultextension='.txt')
    if self.Save is None:
        return

    self.text_save = self.text.get(1.0, END)
    self.Save.write(self.text_save)
    self.Save.close()


class scale:
    def __init__(self, master):
        self.master = master
        self.master.title('')
        self.master.resizable(FALSE, FALSE)

        global text

        self.text = Text(master, wrap=WORD, font=('Time', 14))
        self.text.pack()
        self.text.focus()

        self.B = ttk.Button(master, text='Open', command=self.open_file)
        self.B.pack(side=LEFT)

        self.B1 = ttk.Button(master, text='Save', command=self.save_file)
        self.B1.pack(side=LEFT)



root = Tk()
app = scale(root)
root.mainloop()
