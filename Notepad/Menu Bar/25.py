from datetime import time, datetime
from tkinter import *
from tkinter import ttk, colorchooser
from tkinter import messagebox
from tkinter import filedialog
import webbrowser
from turtledemo import clock

current_open_file = 'no_file'


def view_help():
    webbrowser.open(
        'https://www.bing.com/search?q=get+help+with+notepad+in+windows+10&filters=guid:%224466414-en-dia%22%20lang:%22en%22&form=T00032&ocid=HelpPane-BingIA')


def about_notepad():
    webbrowser.open('https://www.youtube.com/watch?v=RXge_eMkSvU')


def open_file(event=None):
    open_result = filedialog.askopenfile(initialdir='/', title='Select file',
                                         filetype=(('text file', '.txt'), ('All files', '*.*')))

    # if open_result != None:
    try:
        if open_result is not None:
            text.delete(1.0, END)
            for line in open_result:
                text.insert(END, line)
            open_result.close()
    except:
        answer = messagebox.showerror('open file',
                                      'This is not txt file.\nPlease check your file extension and try again')


def save_as(self):
    self.f = filedialog.asksaveasfile(mode='w', defaultextension='.txt')
    if self.f is None:
        return
    text_save_as = text.get(1.0, END)
    self.f.write(text_save_as)
    self.f.close()


def save_file(event=None):
    current_open_file = 'no_file'
    if current_open_file == 'no_file':
        save_as()
    else:
        F2 = open(current_open_file, 'w+')
        F2.write(text.get(1.0, END))
        F2.close()


# def save_file(event=None):
#     current_file = open_file if open_file else None
#     if not current_file:
#         current_file = filedialog.askopenfilename()
#     else:
#         contents = text.get(1.0, END)
#         with open(current_file, 'w') as file:
#             file.write(contents)


def background_color():
    global clr
    clr = colorchooser.askcolor(title='select color')
    text.configure(bg=clr[1])


def text_color():
    global clr
    clr = colorchooser.askcolor(title='select color')
    text.configure(fg=clr[1])


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


def Exit(event=None):
    T = messagebox.askyesnocancel('Exit', 'Do you want to save change to\n', icon="warning")
    print(T)

    if T == True:
        save_file()
        root.destroy()

    elif T == False:
        root.destroy()

    else:
        root.mainloop()


def New_file(event=None):
    T = messagebox.askyesnocancel('Exit', 'Do you want to save change to\n', icon="warning")
    print(T)

    if T == True:
        save_file()
        text.delete(1.0, END)
        text.focus()

    elif T == False:
        text.delete(1.0, END)
        text.focus()

    else:
        root.mainloop()


def Time():
    pass


class text_editor:
    def __init__(self, master):
        master.title("Notepad")
        global text

        scroll = Scrollbar(master)
        scroll.pack(side=RIGHT, fill=Y)

        text = Text(master, wrap=WORD, undo=True, font=("Time", 14),
                    yscrollcommand=scroll.set)
        text.pack(fill=BOTH, expand=1, padx=5, pady=5)
        text.focus()
        text.pack(side=LEFT)
        scroll.configure(command=text.yview)

        root.option_add('*tearOff', False)
        menubar = Menu(root)
        root.config(menu=menubar)

        file_ = Menu(menubar)
        edit_ = Menu(menubar)
        format_ = Menu(menubar)
        view_ = Menu(menubar)
        help_ = Menu(menubar)
        # this to add the menu to the menu bar.
        menubar.add_cascade(menu=file_, label='File')
        menubar.add_cascade(menu=edit_, label='Edit')
        menubar.add_cascade(menu=format_, label='Format')
        menubar.add_cascade(menu=view_, label='View')
        menubar.add_cascade(menu=help_, label='Help')

        # the separator is to separator the first submenu with others.
        file_.add_command(label='New...', command=New_file)
        file_.add_separator()
        file_.add_command(label='Open...', command=open_file)
        file_.add_command(label='Save...', command=save_file)
        file_.add_command(label='Save As...', command=save_as)
        file_.add_separator()
        file_.add_command(label='Print Setup...')
        file_.add_command(label='Print...')
        file_.add_separator()
        file_.add_command(label='Exit...', command=Exit)

        # this to add keyboard shot cut.
        file_.entryconfig('New...', accelerator='Ctrl+N')
        file_.entryconfig('Open...', accelerator='Ctrl+O')
        file_.entryconfig('Save...', accelerator='Ctrl+S')
        file_.entryconfig('Print...', accelerator='Ctrl+P')
        file_.entryconfig('Exit...', accelerator='Ctrl+E')

        # the separator is to separator the first submenu with others.
        edit_.add_command(label='Undo', command=undo)
        edit_.add_command(label='Redo', command=redo)
        edit_.add_separator()
        edit_.add_command(label='Cut', command=cut_text)
        edit_.add_command(label='Copy', command=copy_text)
        edit_.add_command(label='Paste', command=paste_text)
        edit_.add_command(label='Delete')
        edit_.add_separator()
        edit_.add_command(label='Find...')
        edit_.add_command(label='Find Next...')
        edit_.add_command(label='Replace...')
        edit_.add_command(label='Go To...')
        edit_.add_separator()
        edit_.add_command(label='Select All')
        # edit_.add_command(label='Time/Date')

        # this to add submenu to save.
        others = Menu(edit_)
        edit_.add_cascade(menu=others, label='More Options')
        others.add_command(label='Time...', command=Time)
        others.add_command(label='Date...')
        others.add_command(label='Calendar...')

        # this to add keyboard shot cut.
        edit_.entryconfig('Undo', accelerator='Ctrl+Z')
        edit_.entryconfig('Redo', accelerator='Ctrl+y')
        edit_.entryconfig('Cut', accelerator='Ctrl+X')
        edit_.entryconfig('Copy', accelerator='Ctrl+C')
        edit_.entryconfig('Paste', accelerator='Ctrl+V')
        edit_.entryconfig('Delete', accelerator='Del')
        edit_.entryconfig('Find...', accelerator='Ctrl+F')
        edit_.entryconfig('Find Next...', accelerator='F3')
        edit_.entryconfig('Replace...', accelerator='Ctrl+H')
        edit_.entryconfig('Go To...', accelerator='Ctrl+G')
        edit_.entryconfig('Select All', accelerator='Ctrl+A')
        # edit_.entryconfig('Time/Date', accelerator='Ctrl+G')

        format_.add_command(label='Word Wrap')
        format_.add_separator()
        format_.add_command(label='Font...')

        Colors = Menu(format_)
        format_.add_cascade(menu=Colors, label='Colors')
        Colors.add_command(label='Text Color', command=text_color)
        Colors.add_command(label='Background Color', command=background_color)

        view_.add_command(label='Status Bar')

        help_.add_command(label='View Help', command=view_help)
        help_.add_separator()
        help_.add_command(label='About Notepad', command=about_notepad)

        master.bind('<Control-s>', save_file)
        master.bind('<Control-o>', open_file)
        master.bind('<Control-s>', save_file)
        master.bind('<Control-o>', open_file)
        master.bind('<Control-c>', copy_text)
        master.bind('<Control-v>', paste_text)
        master.bind('<Control-x>', cut_text)
        master.bind('<Control-y>', cut_text)  # undo
        master.bind('<Control-z>', cut_text)  # redo


root = Tk()
app = text_editor(root)
root.mainloop()
