from tkinter import *
from tkinter import ttk, colorchooser
from tkinter import filedialog
from tkinter import messagebox
from tkinter.font import Font


def open_file(event=None):
    open_result = filedialog.askopenfile(initialdir='/', title='Select file',
                                         filetype=(('text file', '.txt'), ('All files', '*.*')))

    # if open_result != None:
    try:
        if open_result is not None:
            text.delete(1.0, END)
            for line in open_result:
                text.insert(END, line)
    except:
        answer = messagebox.showerror('open file',
                                      'This is not txt file.\nPlease check your file extension and try again')


def save_file(event=None):
    Save = filedialog.asksaveasfile(mode='w', defaultextension='.txt')
    if Save is None:
        return

    text_save = text.get(1.0, END)
    Save.write(text_save)
    Save.close()


def copy_text(event=None):
    text.clipboard_clear()
    text.clipboard_append(text.selection_get())


def cut_text(event=None):
    text.clipboard_clear()
    text.clipboard_append(text.selection_get())
    text.delete("first", "last")  # first index and last index


def paste_text(event=None):
    text.insert(INSERT, text.clipboard_get())


def redo(event=None):
    text.edit_redo()


def undo(event=None):
    text.edit_undo()


class scale:
    def __init__(self, master):
        master.title('')
        master.resizable(FALSE, FALSE)

        global text
        text = Text(master, wrap=WORD, undo=True)
        text.pack()
        text.focus()

        B = ttk.Button(master, text='Open', command=open_file)
        B.pack(side=LEFT, padx=5, pady=2)

        B1 = ttk.Button(master, text='Save', command=save_file)
        B1.pack(side=LEFT, padx=5, pady=2)

        B4 = ttk.Button(master, text='Copy', command=copy_text)
        B4.pack(side=LEFT, padx=5, pady=2)

        B2 = ttk.Button(master, text='Cut', command=cut_text)
        B2.pack(side=RIGHT, padx=5, pady=2)

        B3 = ttk.Button(master, text='Paste', command=paste_text)
        B3.pack(side=LEFT, padx=5, pady=2)

        B5 = ttk.Button(master, text='Undo', command=undo)  # most put undo=True in  the text area
        B5.pack(side=RIGHT, padx=5, pady=2)

        B6 = ttk.Button(master, text='Redo', command=redo)
        B6.pack(side=RIGHT, padx=5, pady=2)

        master.bind('<Control-s>', save_file)
        master.bind('<Control-o>', open_file)
        master.bind('<Control-c>', copy_text)
        master.bind('<Control-v>', paste_text)
        master.bind('<Control-x>', cut_text)
        master.bind('<Control-y>', cut_text)  # undo
        master.bind('<Control-z>', cut_text)  # redo


root = Tk()
app = scale(root)
root.mainloop()
