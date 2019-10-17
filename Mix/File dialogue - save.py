from tkinter import *
from tkinter import ttk, colorchooser
from tkinter import filedialog
from tkinter import messagebox
from tkinter.font import Font


def open_file(event=None):
    current_openfile='no_file'
    open_result = filedialog.askopenfile(initialdir='/', title='Select file',
                                         filetype=(('text file', '.txt'), ('All files', '*.*')))

    # if open_result != None:
    try:
        if open_result is not None:
            text.delete(1.0, END)
            for line in open_result:
                text.insert(END, line)
        current_openfile = open_result.name
        open_result.close()

    except:
        answer = messagebox.showerror('open file',
                                      'This is not txt file.\nPlease check your file extension and try again')
        if answer == 'ok':
            open_result = filedialog.askopenfile(initialdir='/', title='Select file',
                                                 filetype=(('text file', '.txt'), ('All files', '*.*')))


def save_file(event=None):
    Save = filedialog.asksaveasfile(mode='w', defaultextension='.txt')
    if Save is None:
        return

    text_save = text.get(1.0, END)
    Save.write(text_save)
    Save.close()


def background_color():
    clr = colorchooser.askcolor(title='select color')
    print(clr)
    text.configure(bg=clr[1])


class scale:
    def __init__(self, master):
        master.title('')
        master.resizable(FALSE, FALSE)

        global text
        text = Text(master, wrap=WORD)
        text.pack()
        text.focus()

        B = ttk.Button(master, text='Open', command=open_file)
        B.pack(side=LEFT, padx=5, pady=2)

        B1 = ttk.Button(master, text='Save', command=save_file)
        B1.pack(side=LEFT, padx=5, pady=2)

        master.bind('<Control-s>', save_file)
        master.bind('<Control-o>', open_file)


root = Tk()
app = scale(root)
root.mainloop()
