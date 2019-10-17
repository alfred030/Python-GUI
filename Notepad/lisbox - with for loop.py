from tkinter import *
from tkinter import ttk


def click_me():
    select_items = L.curselection()
    print(select_items)
    
    for item in select_items:
        print(item)



class button:
    def __init__(self, master):
        master.title('Button')
        root.geometry('400x400')

        global L
        L = Listbox(master, bg='gray',
                    fg='white',
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

        B = ttk.Button(master, text='print the selection', command=click_me)
        B.pack()


root = Tk()
app = button(root)
root.mainloop()
