from tkinter import *      
    
window = Tk()
window.title('New Window')

window.geometry('640x480')
window.maxsize(640, 480)
window.minsize(300, 200)

'''
window.resizable(False, False)
window.resizable(True, True)
'''

window.mainloop()
