from datetime import time, datetime
from tkinter import *
from tkinter import ttk, colorchooser
from tkinter import messagebox
from tkinter import filedialog
import webbrowser
from tkinter.font import families
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

    def __cut(self):
        self.text.event_generate("<<Cut>>")

    def paste_text(self, event=None):
        self.text.insert(INSERT, self.text.clipboard_get())

    def redo(self, event=None):
        self.text.edit_redo()

    def undo(self, event=None):
        self.text.edit_undo()

    def select_all(self, event=None):
        self.text.tag_add('sel', '1.0', 'end')
        return 'break'

    def Exit(self, event=None):
        T = messagebox.askyesnocancel('Exit', 'Do you want to save change to\n', icon="warning")
        print(T)

        if T is True:
            self.save_as()
            main().destroy()

        elif T is False:
            main().destroy()

        else:
            main()

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
            main()

    def bind_event(self, event):
        try:
            self.right_click_menu.tk_popup(event.x_root, event.y_root, 0)
        finally:
            self.right_click_menu.grab_release()

    def __init__(self, master):

        width_of_window = 1200
        height_of_window = 600

        width_value = master.winfo_screenwidth()
        height_value = master.winfo_screenheight()

        X_coordinate = (width_value / 2) - (width_of_window / 2)
        Y_coordinate = (height_value / 2) - (height_of_window / 2)

        master.geometry("%dx%d+%d+%d" % (width_of_window, height_of_window,
                                         X_coordinate, Y_coordinate))

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

        # TODO MENU
        master.option_add('*tearOff', False)
        self.menubar = Menu(master)
        master.config(menu=self.menubar)

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
        self.file_.add_command(label='Print...', command=self.bind_event)
        self.file_.add_separator()
        self.file_.add_command(label='Exit...', command=self.Exit)

        # this is to create a pop up menu at a specific location.
        # self.file_.post(400, 300)

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
        self.edit_.add_command(label='Find...', command=self.find_replace)
        self.edit_.add_command(label='Find Next...')
        self.edit_.add_command(label='Replace...')
        self.edit_.add_command(label='Go To...')
        self.edit_.add_separator()
        self.edit_.add_command(label='Select All', command=self.select_all)
        # edit_.add_command(label='Time/Date')

        # this to add submenu to save.
        self.others = Menu(self.edit_)
        self.edit_.add_cascade(menu=self.others, label='More Options')
        self.others.add_command(label='Time...')
        self.others.add_command(label='Date...')
        self.others.add_command(label='Calendar...')

        # this to add keyboard shot cut.
        self.edit_.entryconfig('Undo', accelerator='Ctrl+Z')
        self.edit_.entryconfig('Redo', accelerator='Ctrl+Y')
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
        self.format_.add_command(label='Font...', command=self.font_change)

        self.Colors = Menu(self.format_)
        self.format_.add_cascade(menu=self.Colors, label='Colors')
        self.Colors.add_command(label='Text Color', command=self.text_color)
        self.Colors.add_command(label='Background Color', command=self.background_color)

        self.view_.add_command(label='Status Bar')

        # TODO KEYBOARD EVENTS
        self.help_.add_command(label='View Help', command=view_help)
        self.help_.add_separator()
        self.help_.add_command(label='About Notepad', command=about_notepad)

        self.master.bind('<Control-n>', self.New_file)
        self.master.bind('<Control-N>', self.New_file)

        self.master.bind('<Control-s>', self.save_file)
        self.master.bind('<Control-S>', self.save_file)

        self.master.bind('<Control-o>', self.open_files)
        self.master.bind('<Control-O>', self.open_files)

        self.master.bind('<Control-s>', self.save_file)
        self.master.bind('<Control-S>', self.save_file)

        self.master.bind('<Control-c>', self.copy_text)
        self.master.bind('<Control-C>', self.copy_text)

        self.master.bind('<Control-v>', self.paste_text)
        self.master.bind('<Control-V>', self.paste_text)

        self.master.bind('<Control-x>', self.cut_text)
        self.master.bind('<Control-X>', self.cut_text)

        self.master.bind('<Control-r>', self.find_replace)
        self.master.bind('<Control-R>', self.find_replace)

        self.master.bind('<Control-e>', self.Exit)
        self.master.bind('<Control-E>', self.Exit)

        self.master.bind("<Button-3>", self.bind_event)

        # TODO CONTEXT MENU
        self.right_click_menu = Menu(master, tearoff=0, fg='black', bg='white')
        self.right_click_menu.add_command(label='New...', command=self.New_file)
        self.right_click_menu.add_separator()
        self.right_click_menu.add_command(label='Open...', command=self.open_files)
        self.right_click_menu.add_command(label='Save...', command=self.save_file)
        self.right_click_menu.add_command(label='Save As...', command=self.save_as)
        self.right_click_menu.add_separator()
        self.right_click_menu.add_command(label='Print Setup...')
        self.right_click_menu.add_command(label='Print...', command=self.bind_event)
        self.right_click_menu.add_separator()

        self.right_click_menu.entryconfig('New...', accelerator='Ctrl+N')
        self.right_click_menu.entryconfig('Open...', accelerator='Ctrl+O')
        self.right_click_menu.entryconfig('Save...', accelerator='Ctrl+S')
        self.right_click_menu.entryconfig('Print...', accelerator='Ctrl+P')

        self.right_click_menu.add_command(label='Undo', command=self.undo)
        self.right_click_menu.add_command(label='Redo', command=self.redo)
        self.right_click_menu.add_separator()
        self.right_click_menu.add_command(label='Cut', command=self.cut_text)
        self.right_click_menu.add_command(label='Copy', command=self.copy_text)
        self.right_click_menu.add_command(label='Paste', command=self.paste_text)
        self.right_click_menu.add_command(label='Delete')
        self.right_click_menu.add_separator()
        self.right_click_menu.add_command(label='Find...', command=self.find_replace)
        self.right_click_menu.add_command(label='Find Next...')
        self.right_click_menu.add_command(label='Replace...')
        self.right_click_menu.add_command(label='Go To...')
        self.right_click_menu.add_separator()
        self.right_click_menu.add_command(label='Select All', command=self.select_all)

        self.right_click_menu.entryconfig('Undo', accelerator='Ctrl+Z')
        self.right_click_menu.entryconfig('Redo', accelerator='Ctrl+Y')
        self.right_click_menu.entryconfig('Cut', accelerator='Ctrl+X')
        self.right_click_menu.entryconfig('Copy', accelerator='Ctrl+C')
        self.right_click_menu.entryconfig('Paste', accelerator='Ctrl+V')
        self.right_click_menu.entryconfig('Delete', accelerator='Del')
        self.right_click_menu.entryconfig('Find...', accelerator='Ctrl+F')
        self.right_click_menu.entryconfig('Find Next...', accelerator='F3')
        self.right_click_menu.entryconfig('Replace...', accelerator='Ctrl+H')
        self.right_click_menu.entryconfig('Go To...', accelerator='Ctrl+G')
        self.right_click_menu.entryconfig('Select All', accelerator='Ctrl+A')

        self.right_click_menu.add_cascade(menu=self.others, label='More Options')

        self.right_click_menu.add_cascade(menu=self.Colors, label='Colors')

        self.right_click_menu.add_command(label='Font...', command=self.font_change)
        self.right_click_menu.entryconfig('Font...', accelerator='Ctrl+F')

        self.right_click_menu.add_separator()
        self.right_click_menu.add_command(label='Exit...', command=self.Exit)
        self.right_click_menu.entryconfig('Exit...', accelerator='Ctrl+G')

        self.right_click_menu.post(300, 200)

    def find_replace(self, event=None):
        window1 = Toplevel(self.master)
        app = Find(window1)

    def font_change(self, event=None):
        window2 = Toplevel(self.master)
        app = fonts(window2)


class fonts:
    def __init__(self, master, **kwargs):
        width_of_window = 790
        height_of_window = 350

        width_value = master.winfo_screenwidth()
        height_value = master.winfo_screenheight()

        X_coordinate = (width_value / 2) - (width_of_window / 2)
        Y_coordinate = (height_value / 2) - (height_of_window / 2)

        master.geometry("%dx%d+%d+%d" % (width_of_window, height_of_window,
                                         X_coordinate, Y_coordinate))

        self.master = master
        master.title('Choose Font and Size')
        master.resizable(FALSE, FALSE)

        # ------------------------------------------------------------------------------
        self.frame_void1 = LabelFrame(self.master, width=20)
        self.frame_void1.pack(side=LEFT)

        self.frame = LabelFrame(self.master, text='Choose Text Font', font=('Time', 16))
        self.frame.pack(side=LEFT)
        self.scrollbar = Scrollbar(self.frame)

        self.font_list = Listbox(self.frame, font=('Time', 12),
                                 width=25,
                                 height=15,
                                 exportselection=FALSE,
                                 yscrollcommand=self.scrollbar.set)

        self.available_fonts = sorted(families())
        for family in self.available_fonts:
            self.font_list.insert(END, family)

        self.E = ttk.Entry(self.frame, width=40)
        self.E.pack()
        self.E.focus()

        self.font_list.pack(side=LEFT)
        self.scrollbar.pack(side=RIGHT, fill=Y)
        self.scrollbar.config(command=self.font_list.yview)

        # -----------------------------------------------------------------------

        self.frame_void2 = LabelFrame(self.master, width=35)
        self.frame_void2.pack(side=LEFT)

        self.frame4 = LabelFrame(self.master,
                                 text='font Style:',
                                 font=('Time', 16))
        self.frame4.pack(side=LEFT)

        self.E3 = ttk.Entry(self.frame4, width=27)
        self.E3.pack()

        self.listbox2 = Listbox(self.frame4, bg='white',
                                fg='black',
                                width=15,
                                height=12,
                                font=('Time', 14),
                                selectmode=SINGLE)  # BROWSE, SINGLE, MULTIPLE, EXTENDED

        self.listbox2.insert(1, 'regular')
        self.listbox2.insert(2, 'bold')
        self.listbox2.insert(2, 'italic')
        self.listbox2.insert(3, 'bold italic')
        self.listbox2.pack(side=LEFT)

        # --------------------------------------------------------------------------

        self.frame_void3 = LabelFrame(self.master, width=35)
        self.frame_void3.pack(side=LEFT)

        self.frame3 = LabelFrame(self.master,
                                 text='Size',
                                 font=('Time', 16))
        self.frame3.pack(side=LEFT)

        self.E2 = ttk.Entry(self.frame3, width=18)
        self.E2.pack()

        self.scroll = Scrollbar(self.frame3)
        self.scroll.pack(side=RIGHT, fill=Y)

        # height=25 is to set 25 items in the listbox
        self.listbox2 = Listbox(self.frame3, height=15, width=10, font=('Time', 12),
                                yscrollcommand=self.scroll.set)  # yscroll command it is to make the scroll bar communique with the listbox
        for i in range(5, 99):
            self.listbox2.insert(END, str(i))

        self.listbox2.pack(side=LEFT)
        self.scroll.configure(command=self.listbox2.yview)  # this yview is in the master windows

        self.frame5 = Frame(self.master)
        self.frame5.pack(side=BOTTOM)
        self.b = ttk.Button(self.frame5, text='Save')
        self.b.grid(row=0, column=0, pady=5)

        self.b = ttk.Button(self.frame5, text='Cancel')
        self.b.grid(row=0, column=1, pady=5)


class Find:
    def __init__(self, master):
        width_of_window = 310
        height_of_window = 115

        width_value = master.winfo_screenwidth()
        height_value = master.winfo_screenheight()

        X_coordinate = (width_value / 2) - (width_of_window / 2)
        Y_coordinate = (height_value / 2) - (height_of_window / 2)

        master.geometry("%dx%d+%d+%d" % (width_of_window, height_of_window,
                                         X_coordinate, Y_coordinate))
        self.master = master
        # self.master.geometry('350x100')
        self.master.title('Find and Replace')

        self.text_to_find = StringVar()
        self.text_to_replace = StringVar()

        label1 = Label(self.master, text='Find')
        label1.grid(row=0, column=0, padx=5, pady=10)

        label2 = Label(self.master, text='Replace')
        label2.grid(row=1, column=0)

        entry1 = ttk.Entry(self.master, textvariable=self.text_to_find, width=40)
        entry1.grid(row=0, column=1, padx=5, pady=10)
        entry1.focus()

        entry2 = ttk.Entry(self.master, textvariable=self.text_to_replace, width=40)
        entry2.grid(row=1, column=1, padx=5, pady=10)

        button1 = ttk.Button(self.master, text='Find', command=self.on_find)
        button1.grid(row=2, column=1, sticky=E)

        button1 = ttk.Button(self.master, text='Replace', command=self.on_find)
        button1.grid(row=2, column=1, sticky=W)

    def on_find(self):
        self.master.find(self.text_to_find.get())

    def on_replace(self):
        self.master.replace(self.text_to_find.get(), self.text_to_replace.get())


def main():
    root = Tk()
    app = text_editor(root)
    root.mainloop()


if __name__ == '__main__':
    main()
