'''
https://www.youtube.com/watch?v=4McKSuuUQ-0&index=28&t=
285s&list=PLrafTkhP5sZza-dNA8ZmLTZO3GzsKNUrA
'''

from tkinter import *
from tkinter import messagebox

window = Tk()

#showinfo: info icon
#showerror: error icon
#showwarning: warning icon
#askyesno
#askokcancel
#askretrycancel

#this line remove the tkinter root window
#window.withdraw()

#messagebox.askyesno("Question", "do you have brown hair")


'''
window.withdraw()
if messagebox.askretrycancel("Question", "do you have brown hair", icon = "error")== True:
    print("Yes")
else:
    print("No")

window.deiconify()
window.destroy()
window.quit()
'''

#===================================message box=======================================================
from tkinter import messagebox

def iExit():
    qExit = messagebox.askyesno("Fast Food",
                                "This system is still running.\n\n"
                                "Do you want to quit?", icon = "warning")
    if qExit > 0:
        window.destroy()
        return

btnExit=Button(window,
                padx = 16,
                pady = 1,
                font = ('Time', 16),
                width = 5,
                text = 'Exit', command=lambda: iExit()).pack()


window.mainloop()






