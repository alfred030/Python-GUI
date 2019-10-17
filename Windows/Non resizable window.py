from tkinter import *      
    
window = Tk()
window.title('New Window')
window.geometry("300x200")
# this is for non resizable
window.resizable(False, False)

'''
# this to put the window into resizable state again.
window.resizable(True, True)
'''
window.mainloop()
