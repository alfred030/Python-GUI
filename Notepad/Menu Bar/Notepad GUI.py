from tkinter import *
from tkinter import ttk
from tkinter import messagebox


class text_editor:
    def __init__(self, master):
        master.title("Notepad")

        scroll = Scrollbar(master)
        scroll.pack(side=RIGHT, fill=Y)

        text = Text(master, wrap=WORD, font=("Time", 14),
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
        file_.add_command(label='New...')
        file_.add_separator()
        file_.add_command(label='Open...')
        file_.add_command(label='Save...')
        file_.add_command(label='Save As...')
        file_.add_separator()
        file_.add_command(label='Print Setup...')
        file_.add_command(label='Print...')
        file_.add_separator()
        file_.add_command(label='Exit...')

        # this to add keyboard shot cut.
        file_.entryconfig('New...', accelerator='Ctrl+N')
        file_.entryconfig('Open...', accelerator='Ctrl+O')
        file_.entryconfig('Save...', accelerator='Ctrl+S')
        file_.entryconfig('Print...', accelerator='Ctrl+P')
        file_.entryconfig('Exit...', accelerator='Ctrl+E')

        # the separator is to separator the first submenu with others.
        edit_.add_command(label='Undo')
        edit_.add_separator()
        edit_.add_command(label='Cut')
        edit_.add_command(label='Copy')
        edit_.add_command(label='Paste')
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
        others.add_command(label='Time...')
        others.add_command(label='Date...')
        others.add_command(label='Calendar...')

        # this to add keyboard shot cut.
        edit_.entryconfig('Undo', accelerator='Ctrl+Z')
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
        Colors.add_command(label='Text Color')
        Colors.add_command(label='Background Color')

        view_.add_command(label='Status Bar')

        help_.add_command(label='View Help')
        help_.add_separator()
        help_.add_command(label='About Notepad')


root = Tk()
app = text_editor(root)
root.mainloop()
