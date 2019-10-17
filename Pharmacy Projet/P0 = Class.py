
from tkinter import *
from tkinter import ttk

class App:

    def __init__(self, master):    
        pass # pass is to let Tk know that you create a class; however, you will use it later.
             # this is to avoid errors while runinig this program because the class is empty.

            
def main():            
    
    root = Tk()
    window = App(root)
    root.mainloop()
    
if __name__ == "__main__": main()
