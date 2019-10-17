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
        if answer == 'ok':
            open_result = filedialog.askopenfile(initialdir='/', title='Select file',
                                                 filetype=(('text file', '.txt'), ('All files', '*.*')))

        try:
            if open_result is not None:
                text.delete(1.0, END)
                for line in open_result:
                    text.insert(END, line)
        except:
            answer = messagebox.showerror('open file',
                                          'This is not txt file.\nPlease check your file extension and try again')
            if answer == 'ok':
                open_result = filedialog.askopenfile(initialdir='/', title='Select file',
                                                     filetype=(('text file', '.txt'), ('All files', '*.*')))
                try:  # this is the third time try
                    if open_result is not None:
                        text.delete(1.0, END)
                        for line in open_result:
                            text.insert(END, line)
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


def text_color():
    clr = colorchooser.askcolor(title='select color')
    print(clr)
    text.configure(fg=clr[1])


def font_choose():
    def font1():
        t1 = str(var1.get())
        t2 = str(var2.get())
        t3 = str(var3.get())
        print(t1)
        print(t2)
        print(t3)

        # my_font = Font(family=t1, size=t2, weight=t3)
        # family = 'Time New Roman'

        text.configure(font=(t1, t2, t3))
        # text.configure(font=('Time', t2, 'bold'))

    windows = Toplevel()
    windows.title('Font')
    windows.geometry('500x500')
    # clr = font.families()
    # print(clr)

    L1 = Label(windows, text='Font:')
    L2 = Label(windows, text='Size:')
    L3 = Label(windows, text='Font style:')
    # Font style: normal, bold, italic
    L1.grid(row=0, column=0)
    L2.grid(row=1, column=0)
    L3.grid(row=2, column=0)

    Button(windows, text='OK', command=font1).grid(row=3, column=1)

    var1 = StringVar()
    var2 = StringVar()
    var3 = StringVar()

    E1 = ttk.Entry(windows, textvariable=var1)
    E1.grid(row=0, column=1)

    E2 = ttk.Entry(windows, textvariable=var2)
    E2.grid(row=1, column=1)

    E3 = ttk.Entry(windows, textvariable=var3)
    E3.grid(row=2, column=1)


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

        B4 = ttk.Button(master, text='Font', command=font_choose)
        B4.pack(side=LEFT, padx=5, pady=2)

        B2 = ttk.Button(master, text='Choose background color', command=background_color)
        B2.pack(side=RIGHT, padx=5, pady=2)

        B3 = ttk.Button(master, text='Choose text color', command=text_color)
        B3.pack(side=RIGHT, padx=5, pady=2)

        master.bind('<Control-s>', save_file)
        master.bind('<Control-o>', open_file)


root = Tk()
app = scale(root)
root.mainloop()
