from tkinter import *
from tkinter import messagebox
from tkinter import ttk
from tkinter import simpledialog


def call_me():
    answer = messagebox.askquestion('personal information', 'Do you want to\nyour personal information?')
    if answer == 'yes':
        N = simpledialog.askstring("Name", " please enter your name")
        H = simpledialog.askfloat("Height", " please enter your height")
        P = simpledialog.askinteger("Phone", " please enter your phone number")
        S = simpledialog.askinteger("Social", " please enter your social")
        E = simpledialog.askstring("Email", " please enter your email")
        A = simpledialog.askstring("Address", " please enter your address")

        # output = 'Name: ' + str(N)
        # output += '\nHeight: ' + float(H)

        n = 'Name: '
        h = 'Height: '
        p = "Phone: "
        s = "Social: "
        e = "Email: "
        a = "Address: "

        print(n + N)
        print(h + H)
        print(p + P)
        print(s + S)
        print(e + E)
        print(a + A)

        # N = 'Name: ' + str(N)
        # H = 'Height: ' + float(H)
        # P = "Phone: " + int(P)
        # S = "Social: " + S
        # E = "Email: " + E
        # A = "Address: " + A

        # print('Name: ' + N)
        # print('Height: ' + H)
        # print("Phone: " + P)
        # print("Social: " + S)
        # print("Email: " + E)
        # print("Address: " + A)

    else:
        print('He/She do not want to submit his personal information')


class message_box:
    def __init__(self, master):
        master.title('Message box')

        self.b = ttk.Button(master, text='information', command=call_me)
        self.b.pack()


root = Tk()
message = message_box(root)
root.mainloop()
