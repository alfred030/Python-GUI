from datetime import time, datetime
from tkinter import *
from tkinter import ttk, colorchooser
from tkinter import messagebox
from tkinter import filedialog
import webbrowser
from turtledemo import clock


def about_notepad():
    webbrowser.open('https://www.youtube.com/watch?v=RXge_eMkSvU')


def view_help():
    webbrowser.open(
        'https://www.bing.com/search?q=get+help+with+notepad+in+windows+10&filters=guid:%224466414-en-dia%22%20lang:%22en%22&form=T00032&ocid=HelpPane-BingIA')


class text_editor:

    def open_files(self, event=None):
        open_result = filedialog.askopenfile(initialdir='/', title='Select file',
                                             filetype=(('text file', '.txt'), ('All files', '*.*')))

        # if open_result != None:
        try:
            if open_result is not None:
                self.text.delete(1.0, END)
                for line in open_result:
                    self.text.insert(END, line)
                self.current_open_ile = open_result.name
                open_result.close()
        except:
            answer = messagebox.showerror('open file',
                                          'This is not txt file.\nPlease check your file extension and try again')

    def save_as(self):
        f = filedialog.asksaveasfile(mode='w', defaultextension='.txt')
        if f is None:
            return
        text_save_as = self.text.get(1.0, END)
        self.current_open_ile = f.name
        f.write(text_save_as)
        f.close()

    def save_file(self, event=None):
        if self.current_open_ile is None:
            f = filedialog.asksaveasfile(mode='w', defaultextension='.txt')
            if f is None:
                return
            text_save_as = self.text.get(1.0, END)
            self.current_open_ile = f.name
            f.write(text_save_as)
            f.close()

        else:
            f = open(self.current_open_ile, 'w+')
            f.write(self.text.get(1.0, END))
            f.close()

    # def save_file(self, event=None):
    #     #     current_file = self.open_file if self.open_file else None
    #     #     if current_file:
    #     #         current_file = filedialog.askopenfilename()
    #     #     else:
    #     #         contents = self.text.get(1.0, END)
    #     #         with open(current_file, 'w') as file:
    #     #             file.write(contents)

    def background_color(self):
        global clr
        clr = colorchooser.askcolor(title='select color')
        self.text.configure(bg=clr[1])

    def text_color(self):
        global clr
        clr = colorchooser.askcolor(title='select color')
        self.text.configure(fg=clr[1])

    def copy_text(self, event=None):
        self.text.clipboard_clear()
        self.text.clipboard_append(self.text.selection_get())

    def cut_text(self, event=None):
        self.text.clipboard_clear()
        self.text.clipboard_append(self.text.selection_get())
        self.text.delete("first", "last")  # first index and last index

    def paste_text(self, event=None):
        self.text.insert(INSERT, self.text.clipboard_get())

    def redo(self, event=None):
        self.text.edit_redo()

    def undo(self, event=None):
        self.text.edit_undo()

    def Exit(self, event=None):
        T = messagebox.askyesnocancel('Exit', 'Do you want to save change to\n', icon="warning")
        print(T)

        if T is True:
            self.save_as()
            root.destroy()

        elif T is False:
            root.destroy()

        else:
            root.mainloop()

    def New_file(self, event=None):
        T = messagebox.askyesnocancel('Exit', 'Do you want to save change to\n', icon="warning")
        print(T)

        if T is True:
            self.save_as()
            self.text.delete(1.0, END)
            self.text.focus()

        elif T is False:
            self.text.delete(1.0, END)
            self.text.focus()

        else:
            root.mainloop()

    def Time(self):
        pass

    def on_find(self):
        self.master.find(self.text_to_find.get())

    def on_replace(self):
        self.master.replace(self.text_to_find.get(), self.text_to_replace.get())

    def __init__(self, master):

        self.current_open_ile = None

        self.open_file = None
        self.master = master
        self.master.title("Notepad")
        self.scroll = Scrollbar(master)
        self.scroll.pack(side=RIGHT, fill=Y)

        self.text = Text(self.master, wrap=WORD, undo=True, font=("Time", 14),
                         yscrollcommand=self.scroll.set)
        self.text.pack(fill=BOTH, expand=1, padx=5, pady=5)
        self.text.focus()
        self.text.pack(side=LEFT)
        self.scroll.configure(command=self.text.yview)

        root.option_add('*tearOff', False)
        self.menubar = Menu(root)
        root.config(menu=self.menubar)

        self.file_ = Menu(self.menubar)
        self.edit_ = Menu(self.menubar)
        self.format_ = Menu(self.menubar)
        self.view_ = Menu(self.menubar)
        self.help_ = Menu(self.menubar)
        # this to add the menu to the menu bar.
        self.menubar.add_cascade(menu=self.file_, label='File')
        self.menubar.add_cascade(menu=self.edit_, label='Edit')
        self.menubar.add_cascade(menu=self.format_, label='Format')
        self.menubar.add_cascade(menu=self.view_, label='View')
        self.menubar.add_cascade(menu=self.help_, label='Help')

        # the separator is to separator the first submenu with others.
        self.file_.add_command(label='New...', command=self.New_file)
        self.file_.add_separator()
        self.file_.add_command(label='Open...', command=self.open_files)
        self.file_.add_command(label='Save...', command=self.save_file)
        self.file_.add_command(label='Save As...', command=self.save_as)
        self.file_.add_separator()
        self.file_.add_command(label='Print Setup...')
        self.file_.add_command(label='Print...')
        self.file_.add_separator()
        self.file_.add_command(label='Exit...', command=self.Exit)

        # this to add keyboard shot cut.
        self.file_.entryconfig('New...', accelerator='Ctrl+N')
        self.file_.entryconfig('Open...', accelerator='Ctrl+O')
        self.file_.entryconfig('Save...', accelerator='Ctrl+S')
        self.file_.entryconfig('Print...', accelerator='Ctrl+P')
        self.file_.entryconfig('Exit...', accelerator='Ctrl+E')

        # the separator is to separator the first submenu with others.
        self.edit_.add_command(label='Undo', command=self.undo)
        self.edit_.add_command(label='Redo', command=self.redo)
        self.edit_.add_separator()
        self.edit_.add_command(label='Cut', command=self.cut_text)
        self.edit_.add_command(label='Copy', command=self.copy_text)
        self.edit_.add_command(label='Paste', command=self.paste_text)
        self.edit_.add_command(label='Delete')
        self.edit_.add_separator()
        self.edit_.add_command(label='Find...', command=self.Find_windows)
        self.edit_.add_command(label='Find Next...')
        self.edit_.add_command(label='Replace...')
        self.edit_.add_command(label='Go To...')
        self.edit_.add_separator()
        self.edit_.add_command(label='Select All')
        # edit_.add_command(label='Time/Date')

        # this to add submenu to save.
        self.others = Menu(self.edit_)
        self.edit_.add_cascade(menu=self.others, label='More Options')
        self.others.add_command(label='Time...', command=self.Time)
        self.others.add_command(label='Date...')
        self.others.add_command(label='Calendar...')

        # this to add keyboard shot cut.
        self.edit_.entryconfig('Undo', accelerator='Ctrl+Z')
        self.edit_.entryconfig('Redo', accelerator='Ctrl+y')
        self.edit_.entryconfig('Cut', accelerator='Ctrl+X')
        self.edit_.entryconfig('Copy', accelerator='Ctrl+C')
        self.edit_.entryconfig('Paste', accelerator='Ctrl+V')
        self.edit_.entryconfig('Delete', accelerator='Del')
        self.edit_.entryconfig('Find...', accelerator='Ctrl+F')
        self.edit_.entryconfig('Find Next...', accelerator='F3')
        self.edit_.entryconfig('Replace...', accelerator='Ctrl+H')
        self.edit_.entryconfig('Go To...', accelerator='Ctrl+G')
        self.edit_.entryconfig('Select All', accelerator='Ctrl+A')
        # edit_.entryconfig('Time/Date', accelerator='Ctrl+G')

        self.format_.add_command(label='Word Wrap')
        self.format_.add_separator()
        self.format_.add_command(label='Font...')

        self.Colors = Menu(self.format_)
        self.format_.add_cascade(menu=self.Colors, label='Colors')
        self.Colors.add_command(label='Text Color', command=self.text_color)
        self.Colors.add_command(label='Background Color', command=self.background_color)

        self.view_.add_command(label='Status Bar')

        self.help_.add_command(label='View Help', command=view_help)
        self.help_.add_separator()
        self.help_.add_command(label='About Notepad', command=about_notepad)

        master.bind('<Control-n>', self.New_file)
        master.bind('<Control-s>', self.save_file)
        master.bind('<Control-o>', self.open_files)
        master.bind('<Control-s>', self.save_file)
        master.bind('<Control-o>', self.open_files)
        master.bind('<Control-c>', self.copy_text)
        master.bind('<Control-v>', self.paste_text)
        master.bind('<Control-x>', self.cut_text)

        # master.bind('<Control-z>', self.undo)  # undo
        # master.bind('<Control-y>', self.redo)  # redo

    def Find_windows(self):
        global text_to_find
        global text_to_replace
        self.text_to_find = StringVar()
        self.text_to_replace = StringVar()

        self.window_find = Toplevel(self.master)
        FindWindow(self.window_find)

        label1 = Label(self.window_find, text='Find')
        label1.grid(row=0, column=0)

        label2 = Label(self.window_find, text='Replace')
        label2.grid(row=1, column=0)

        entry1 = ttk.Entry(self.window_find, textvariable=self.text_to_find, width=40)
        entry1.grid(row=0, column=1)

        entry2 = ttk.Entry(self.window_find, textvariable=self.text_to_replace, width=40)
        entry2.grid(row=1, column=1)

        button1 = ttk.Button(self.window_find, text='Find', command=self.on_find)
        button1.grid(row=2, column=1, sticky=E)

        button1 = ttk.Button(self.window_find, text='Replace', command=self.on_find)
        button1.grid(row=2, column=1, sticky=W)


class FindWindow:
    def __init__(self, master):
        self.master = master
        self.master.geometry('350x100')
        self.master.title('Find and Replace')


root = Tk()
app = text_editor(root)
root.mainloop()
