import os
import tkinter
from tkinter import *
from tkinter import filedialog


def find_text(event=None):
    global search_toplevel
    search_toplevel = Toplevel(root)
    search_toplevel.title('Find Text')
    search_toplevel.transient(root)
    search_toplevel.resizable(False, False)
    Label(search_toplevel, text="Find All:").grid(row=0, column=0,
                                                  sticky='e')
    search_entry_widget = Entry(search_toplevel, width=25)
    search_entry_widget.grid(row=0, column=1, padx=2, pady=2,
                             sticky='we')
    search_entry_widget.focus_set()
    ignore_case_value = IntVar()
    Checkbutton(search_toplevel, text='IgnoreCase', variable=ignore_case_value).grid(
        row=1, column=1, sticky='e', padx=2, pady=2)
    Button(search_toplevel, text="Find All", underline=0, command=lambda: search_output(search_entry_widget.get(),
                                                                                        ignore_case_value.get(),
                                                                                        content_text, search_toplevel,
                                                                                        search_entry_widget)).grid(
        row=0, column=2, sticky='e' + 'w', padx=2, pady=2)


def close_search_window():
    content_text.tag_remove('match', '1.0', END)
    search_toplevel.destroy()
    search_toplevel.protocol('WM_DELETE_WINDOW', close_search_window)
    return "break"


def search_output(needle, if_ignore_case, content_text, search_toplevel, search_box):
    content_text.tag_remove('match', '1.0', END)
    matches_found = 0
    if needle:
        start_pos = '1.0'
        while True:
            start_pos = content_text.search(needle, start_pos,
                                            nocase=if_ignore_case, stopindex=END)
            if not start_pos:
                break
            end_pos = '{}+{}c'.format(start_pos, len(needle))
            content_text.tag_add('match', start_pos, end_pos)
            matches_found += 1
            start_pos = end_pos
            content_text.tag_config(
                'match', foreground='red', background='yellow')
            search_box.focus_set()
            search_toplevel.title('{} matches found'.format(matches_found))


def open_file(event=None):
    input_file_name = tkinter.filedialog.askopenfilename(defaultextension=".txt",
                                                         filetypes=[("All Files", "*.*"), ("Text Documents",
                                                                                           "*.txt")])
    if input_file_name:
        global file_name
    file_name = input_file_name
    root.title('{} - {}'.format(os.path.basename(file_name),
                                PROGRAM_NAME))
    content_text.delete(1.0, END)
    with open(file_name) as _file:
        content_text.insert(1.0, _file.read())


def save(event=None):
    global file_name
    if not file_name:
        save_as()
    else:
        write_to_file(file_name)
    return "break"


def save_as(event=None):
    input_file_name = tkinter.filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("All Files", "*.*"), (
        "Text Documents", "*.txt")])
    if input_file_name:
        global file_name
    file_name = input_file_name
    write_to_file(file_name)
    root.title('{} - {}'.format(os.path.basename(file_name),
                                PROGRAM_NAME))
    return "break"


def write_to_file(file_name):
    try:
        content = content_text.get(1.0, 'end')
        with open(file_name, 'w') as the_file:
            the_file.write(content)
    except IOError:
        pass
    # pass for now but we show some warning - we do this innext iteration


def new_file(event=None):
    root.title("Untitled")
    global file_name
    file_name = None
    content_text.delete(1.0, END)


root = Tk()
my_menu = Menu(root)

menu_bar = Menu(root)
# my_menu = Menu(parent, **options)
file_menu = Menu(menu_bar, tearoff=0)
edit_menu = Menu(menu_bar, tearoff=0)
view_menu = Menu(menu_bar, tearoff=0)
about_menu = Menu(menu_bar, tearoff=0)

menu_bar.add_cascade(label='File', menu=file_menu)
menu_bar.add_cascade(label='Edit', menu=edit_menu)
menu_bar.add_cascade(label='View', menu=view_menu)
menu_bar.add_cascade(label='About', menu=about_menu)
root.config(menu=menu_bar)

edit_menu.add_command(label='Find', underline=0, accelerator='Ctrl+F', command=find_text)
file_menu.add_command(label='New', underline=0, accelerator='Ctrl+N', command=new_file)
file_menu.add_command(label='Open', underline=0, accelerator='Ctrl+O', command=open_file)
file_menu.add_command(label='Save', underline=0, accelerator='Ctrl+S', command=save)
file_menu.add_command(label='Save as', underline=0, accelerator='Ctrl+A', command=save_as)

PROGRAM_NAME = " Footprint Editor "
root.title(PROGRAM_NAME)

shortcut_bar = Frame(root, height=25, background='light sea green')
shortcut_bar.pack(expand='no', fill='x')
line_number_bar = Text(root, width=4, padx=3, takefocus=0,
                       border=0,
                       background='khaki', state='disabled', wrap='none')
line_number_bar.pack(side='left', fill='y')

content_text = Text(root, wrap='word')
content_text.pack(expand='yes', fill='both')
scroll_bar = Scrollbar(content_text)
content_text.configure(yscrollcommand=scroll_bar.set)
scroll_bar.config(command=content_text.yview)
scroll_bar.pack(side='right', fill='y')

content_text.bind('<Control-f>', find_text)
content_text.bind('<Control-F>', find_text)

# icons = ('new_file', 'open_file', 'save', 'cut', 'copy', 'paste',
#          'undo', 'redo')
# for i, icon in enumerate(icons):
#     tool_bar_icon = PhotoImage(file='icons/{}.ico'.format(icon))
#     cmd = eval(icon)
#     tool_bar = Button(shortcut_bar, image=tool_bar_icon, command=cmd)
#     tool_bar.image = tool_bar_icon
#     tool_bar.pack(side='left')

root.mainloop()
