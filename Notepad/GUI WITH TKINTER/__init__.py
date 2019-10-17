from tkinter import *
from tkinter import ttk


def scroll_text(self, *args):
    self.text_area.yview_moveto(args[1])


class TextArea(Text):
    def __init__(self, master, **kwargs):
        super().__init__(**kwargs)
        self.master = master
        self.configure(wrap=WORD)


class MainWindow(Tk):
    def __init__(self):
        super().__init__()
        self.text_area = TextArea(self, bg='white', fg='black', undo=True)
        self.scrollbar = ttk.Scrollbar(orient=VERTICAL, command=self.scroll_text)
        self.text_area.configure(yscrollcommand=self.scrollbar.set)

        self.scrollbar.pack(side=LEFT, fill=Y)
        self.text_area.pack(side=LEFT, fill=BOTH, expand=1)



if __name__ == "__main__":
    mw = MainWindow()
    mw.mainloop()
