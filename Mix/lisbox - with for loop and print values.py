from tkinter import *
from tkinter import ttk, scrolledtext
from tkinter import messagebox


def click_me():
    select_items = L.curselection()
    print(select_items)

    for item in select_items:
        print(item)
        t = L.get(item)
        print(t)
        text.insert(INSERT, t)
        text.insert(INSERT, '\n\n')
        # text.insert(INSERT, '\t')

        L.configure(fg='blue')
        B.configure(text='Values were printed', foreground="red")


def clear():
    text.delete(1.0, END)
    L.configure(fg='black',  font=('arial',12,'italic'))
    B.configure(text='Values were printed', foreground="black")



def Delete():
    select_items = L.curselection()
    print(select_items)

    for item in select_items:
        print(item)
        L.delete(item)


def exit_now():
    answer = messagebox.askyesno('Exit', 'this application will close\nDo you want to exit now?')
    if answer:
        root.destroy()


class button:
    def __init__(self, master):
        master.title('Button')
        master.geometry('500x800')
        master.resizable(0, 0)

        global L
        L = Listbox(master, bg='white',
                    fg='black',
                    width=40,
                    height=15,
                    font=('Time', 12),
                    selectmode=MULTIPLE)  # BROWSE, SINGLE, MULTIPLE, EXTENDED

        L.insert(1, 'C++')
        L.insert(2, 'C#')
        L.insert(2, 'C')
        L.insert(3, 'Python')
        L.insert(4, 'Java')
        L.insert(5, 'Javascript')
        L.insert(6, 'Swift')
        L.insert(4, "PHP")
        L.insert(5, "JSP")
        L.insert(6, "Ruby")

        L.pack()

        global B
        B = Button(master, text='print the selection', command=click_me)
        B.pack(side=LEFT)  # ttk can not allow us to change the fg off a button

        B0 = ttk.Button(master, text='Delete', command=Delete)
        B0.pack(side=RIGHT)

        global text
        scroll_W = 500
        scroll_H = 20
        text = scrolledtext.ScrolledText(master,
                                         font=("Time", 14),
                                         width=scroll_W,
                                         height=scroll_H,
                                         wrap=WORD)
        text.pack()
        text.focus()

        B1 = ttk.Button(master, text='Clear', command=clear)
        B1.pack(side=LEFT)

        global B2
        B2 = ttk.Button(master, text='Exit', command=exit_now)
        B2.pack(side=RIGHT)

        master.wm_attributes('-topmost', 1)


root = Tk()
app = button(root)
root.mainloop()
