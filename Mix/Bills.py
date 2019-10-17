from tkinter import *
from tkinter import ttk


def Total(event=None):
    rent = float(E0.get())
    electricity = float(E1.get())
    internet = float(E2.get())
    water = float(E3.get())

    rent1 = float(var0.get())
    electricity1 = float(var1.get())
    internet1 = float(var2.get())
    water1 = float(var3.get())

    # second method to calculate the bill
    Tia_bills1 = rent1 / 2 + water1 / 2 - \
                 electricity1 / 2 - \
                 internet1 / 2
    print(Tia_bills1)

    Standly_bills1 = rent1 + water1 - Tia_bills1
    print(Standly_bills1)

    Money_order1 = rent1 + water1
    print(Money_order1)

    # bills calculation
    Tia_bills = rent / 2 + water / 2 - electricity / 2 - internet / 2
    Standly_bills = rent + water - Tia_bills
    Money_order = rent + water

    E4.configure(state=NORMAL)
    E5.configure(state=NORMAL)
    E6.configure(state=NORMAL)

    var4.set(Tia_bills)
    var5.set(Standly_bills)
    var6.set(Money_order)

    E4.configure(state=DISABLED)
    E5.configure(state=DISABLED)
    E6.configure(state=DISABLED)


def reset_button():
    E0.delete(0, END)
    E1.delete(0, END)
    E2.delete(0, END)
    E3.delete(0, END)

    E4.configure(state=NORMAL)
    E5.configure(state=NORMAL)
    E6.configure(state=NORMAL)

    E4.delete(0, END)
    E5.delete(0, END)
    E6.delete(0, END)

    E4.configure(state=DISABLED)
    E5.configure(state=DISABLED)
    E6.configure(state=DISABLED)


class Bills:
    def __init__(self, master):
        master.title('Bills')
        master.resizable(FALSE, FALSE)


class label:
    def __init__(self, master):
        L0 = ttk.Label(master, text='House rent')
        L0.grid(row=0, column=0, sticky=W)

        L1 = ttk.Label(master, text='Electricity')
        L1.grid(row=1, column=0, sticky=W)

        L2 = ttk.Label(master, text='Internet')
        L2.grid(row=2, column=0, sticky=W)

        L3 = ttk.Label(master, text='Water')
        L3.grid(row=3, column=0, sticky=W)

        L4 = ttk.Label(master, text='Tia bills')
        L4.grid(row=4, column=0, sticky=W)

        L5 = ttk.Label(master, text='Standly bills')
        L5.grid(row=5, column=0, sticky=W)

        L6 = ttk.Label(master, text='Money order')
        L6.grid(row=6, column=0, sticky=W)


class entry:
    def __init__(self, master):
        global E0
        global E1
        global E2
        global E3
        global E4
        global E5
        global E6

        global var0
        global var1
        global var2
        global var3
        global var4
        global var5
        global var6
        var0 = StringVar()
        var1 = StringVar()
        var2 = StringVar()
        var3 = StringVar()
        var4 = StringVar()
        var5 = StringVar()
        var6 = StringVar()

        E0 = ttk.Entry(master, width=10, justify=RIGHT, textvariable=var0)
        E0.grid(row=0, column=1)
        E0.focus()

        E1 = ttk.Entry(master, width=10, justify=RIGHT, textvariable=var1)
        E1.grid(row=1, column=1)

        E2 = ttk.Entry(master, width=10, justify=RIGHT, textvariable=var2)
        E2.grid(row=2, column=1)

        E3 = ttk.Entry(master, width=10, justify=RIGHT, textvariable=var3)
        E3.grid(row=3, column=1)

        E4 = ttk.Entry(master, width=10, justify=RIGHT, textvariable=var4, state=DISABLED)
        E4.grid(row=4, column=1)

        E5 = ttk.Entry(master, width=10, justify=RIGHT, textvariable=var5, state=DISABLED)
        E5.grid(row=5, column=1)

        E6 = ttk.Entry(master, width=10, justify=RIGHT, textvariable=var6, state=DISABLED)
        E6.grid(row=6, column=1)


class button:
    def __init__(self, master):
        B = ttk.Button(master, text='REST', command=reset_button)
        B.grid(row=7, column=0)

        B1 = ttk.Button(master, text='TOTAL', command=Total)
        B1.grid(row=7, column=1)
        master.bind('<Return>', Total)

        master.wm_attributes('-topmost', 1)


root = Tk()
bill = Bills(root)
entry = entry(root)
label = label(root)
button = button(root)
root.mainloop()
