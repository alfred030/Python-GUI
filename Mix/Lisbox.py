from tkinter import *


def click_me():
    pass


class button:
    def __init__(self, master):
        master.title('Button')
        root.geometry('300x300')

        '''
        The width of the widget in characters. The default is 20.
        Height: Number of lines (not pixels!) shown in the listbox. Default is 10.
        SINGLE − You can only select one line
        MULTIPLE − You can select any number of lines at once
        '''

        L = Listbox(master, bg='gray',
                    fg='white',
                    width=40,
                    height=15,
                    font=('Time', 12),
                    selectmode=EXTENDED)  # BROWSE, SINGLE, MULTIPLE, EXTENDED

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


root = Tk()
app = button(root)
root.mainloop()
