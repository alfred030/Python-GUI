from tkinter import *
from tkinter import ttk, messagebox


def Restaurant():
    rest = Toplevel()
    rest.geometry('500x500')
    rest.title('Restaurant')
    label = Label(rest, text='Rice')
    label.pack()

    frame = LabelFrame(rest, text='Dinner', bd=5, relief=SUNKEN, width=300, height=200)
    frame.pack()
    B1 = ttk.Button(rest, text='Rest', command=new_windows)
    B1.pack()


def new_windows():
    new = Toplevel()
    new.geometry('200x200')
    new.title('rest')

    L = Label(new, text='I was reset')
    L.pack()


class Login:
    def __init__(self, master):
        global entry_Username
        global entry_Password

        # ---------------------------------------------------------------------------------------------
        # Login system
        def Login_System(event=''):
            username = (entry_Username.get())
            password = (entry_Password.get())

            if (username == str("merluise.tia")) and (password == str("tia12345")):  # tia12345 most be a string
                Restaurant()


            elif (username == str("1")) and (password == str(1)):  # tia12345 most be a string
                Restaurant()


            elif (username == str("2")) or (username == str("3")) and (password == str("2")) or (
                    password == str(3)):  # tia12345 most be a string
                Restaurant()

            elif (username == str("4")) or (username == str("5")) and (password == str(4)) or (
                    password == str(5)):  # tia12345 most be a string
                Restaurant()


            elif (username == str("5")) and (password == str(5)):
                Restaurant()

            else:
                messagebox.askretrycancel("Hospital Login System", "Invalid password or username",
                                          icon="error")
                entry_Username.focus()  # put the cursor in the username entry

        # ---------------------------------------------------------------------------------------------
        # Functions
        def iExit():
            answer = messagebox.askyesno("Hospital Login System",
                                         "This system is still running.\n"
                                         "Are you sure that you want to sign out?",
                                         icon="warning")
            if answer:
                root.destroy()

        def Reset():
            entry_Username.delete(0, 'end')
            entry_Password.delete(0, 'end')
            entry_Username.focus()  # this set the entry to zero if wrong password or username

        # ---------------------------------------------------------------------------------------------
        # Login GUI
        master.resizable(False, False)
        master.title("LOGIN SYSTEM")
        master.config(bg="powder blue")

        entry_Username = StringVar()
        entry_Password = StringVar()

        label = ttk.Label(master, text='Username', background="powder blue", font=('Time', 10))
        label.grid(row=0, column=0, pady=10, padx=1)

        label = ttk.Label(master, text='Password', background="powder blue", font=('Time', 10))
        label.grid(row=1, column=0, pady=5, padx=1)

        entry_Username = ttk.Entry(master, width=25, font=('Time', 10))
        entry_Username.focus()
        entry_Password = ttk.Entry(master, width=25, font=('Time', 10))
        entry_Password.config(show='*')

        entry_Username.grid(row=0, column=1, padx=1, columnspan=2, sticky='e' + 'w')  # to expand the Entry
        entry_Password.grid(row=1, column=1, padx=1, columnspan=2, sticky='e' + 'w')

        label = Label(master, text='', background="powder blue")
        label.grid(row=2, column=0, columnspan=3, sticky='e' + 'w')

        btn1 = ttk.Button(master, text='Login', command=Login_System)
        btn1.grid(row=3, column=0, sticky='e' + 'w', pady=1, padx=1)
        btn2 = ttk.Button(master, text='Reset', command=Reset)
        btn2.grid(row=3, column=1, sticky='e' + 'w', pady=1, padx=30)
        btn3 = ttk.Button(master, text='Exit', command=iExit)
        btn3.grid(row=3, column=2, sticky='e' + 'w', pady=1, padx=1)

        master.bind('<Return>', Login_System)


root = Tk()
app = Login(root)
root.mainloop()
