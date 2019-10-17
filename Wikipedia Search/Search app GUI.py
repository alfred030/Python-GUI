from tkinter import *
from tkinter import ttk, scrolledtext
import wikipedia  # Pip install  wikipedia first


# def click_me(event=None):
#     entry_value = entry.get()
#     answer_value = wikipedia.summary(entry_value)
#     answer.delete(1.0, END)  # this line off code delete the previous search and insert the new search
#     answer.insert(INSERT, answer_value)

def click_me(event=None):
    entry_value = entry.get()
    answer.delete(1.0, END)  # this line off code delete the previous search and insert the new search
    try:
        answer_value = wikipedia.summary(entry_value)
        answer.insert(INSERT, answer_value)
        print(answer_value)
    except:
        answer.insert(INSERT, 'Please check your input or internet connexion')



def Clear():
    answer.delete(1.0, END)
    entry.delete(0, END)


class Scroll:
    def __init__(self, master):
        master.title('')
        master.geometry('800x500')

        top_frame = Frame(master)
        top_frame.pack(side=TOP)

        bottom_frame = Frame(master)
        bottom_frame.pack()

        global entry
        button = ttk.Button(top_frame, text='Search', command=click_me)
        button.pack(side=LEFT)

        entry = ttk.Entry(top_frame, width=58, font=("Time", 14))
        entry.pack(side=LEFT)
        entry.focus()
        entry.bind('<Return>', click_me)

        button2 = ttk.Button(top_frame, text='Clear', command=Clear)
        button2.pack(side=LEFT)

        scroll = Scrollbar(bottom_frame)
        scroll.pack(side=RIGHT, fill=Y)

        global answer
        answer = Text(bottom_frame,
                      yscrollcommand=scroll.set,
                      wrap=WORD,
                      font=("Time", 14))
        answer.pack()
        scroll.configure(command=answer.yview)


root = Tk()
app = Scroll(root)
root.mainloop()
