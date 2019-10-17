
from tkinter import *
from tkinter import ttk        
    
root = Tk()
root.geometry("800x450")
# this is the app title
root.title("Coordinate In Python GUI")

'''
label_0 = Label(root,
                text = "Hello world\nHello Tia\nHello Leo",
                bd = 1,
                relief = "solid",
                background = "grey",
                font = "Times 18",
                width = 15,
                height = 5
               )
label_0.pack()
'''

label_2 = Label(root,
                text = "Hello world\nHello Tia\nHello Leo",
                bd = 1,
                relief = "solid",
                background = "red",
                font = "Times 18",
                width = 15,
                height = 3
               )
label_2.place(relx = 0.5,rely = 0.5, anchor = "center")


label_3 = Label(root,
                text = "Hello world\nHello Tia\nHello Leo",
                bd = 1,
                relief = "solid",
                background = "red",
                font = "Times 18",
                width = 15,
                height = 3
               )
label_3.place(relx = 1.0, x= -5, rely = 0, y = 5, anchor = "ne")

'''
label_4 = Label(root,
                text = "Hello world\nHello Tia\nHello Leo",
                bd = 1,
                relief = "solid",
                background = "green",
                font = "Times 18",
                width = 15,
                height = 3
               )

label_4.place(relx = 0.5,
              x = 100,
              rely = 0.5,
              y = 50,
              )
'''
       

label_5 = Label(root,
                text = "Hello world\nHello Tia\nHello Leo",
                bd = 1,
                relief = "solid",
                background = "yellow",
                font = "Times 18",
                width = 15,
                height = 3
               )

label_5.place(relx = 0.5,
              x = -100,
              rely = 0.5,
              y = 240,
              )


              
label_6 = Label(root,
                text = "Hello world\nHello Tia\nHello Leo",
                bd = 1,
                relief = "solid",
                background = "yellow",
                font = "Times 18",
                width = 15,
                height = 3
               )
label_6.place(relx = 0, x = 5, rely = 0, y = 5, anchor = "nw")

label_6 = Label(root,
                text = "Hello world\nHello Tia\nHello Leo",
                bd = 1,
                relief = "solid",
                background = "yellow",
                font = "Times 18",
                width = 15,
                height = 3
               )
label_6.place(relx = 0, x = 5, rely = 1, y = -5, anchor = "sw")


label_7 = Label(root,
                text = "Hello world\nHello Tia\nHello Leo",
                bd = 1,
                relief = "solid",
                background = "yellow",
                font = "Times 18",
                width = 15,
                height = 3
               )

label_7.place(relx = 0.5, x = 0, rely = 0, y = 5, anchor = "n")


label_7 = Label(root,
                text = "Hello world\nHello Tia\nHello Leo",
                bd = 1,
                relief = "solid",
                background = "yellow",
                font = "Times 18",
                width = 15,
                height = 3
               )

label_7.place(relx = 1, x = -5, rely = 0.5, y = 0, anchor = "e")


label_8 = Label(root,
                text = "Hello world\nHello Tia\nHello Leo",
                bd = 1,
                relief = "solid",
                background = "yellow",
                font = "Times 18",
                width = 15,
                height = 3
               )

label_8.place(relx = 1.0, x = -5, rely = 1.0, y = -5, anchor = "se")



label_9 = Label(root,
                text = "Hello world\nHello Tia\nHello Leo",
                bd = 1,
                relief = "solid",
                background = "yellow",
                font = "Times 18",
                width = 15,
                height = 3
               )

label_9.place(relx = 0.5, x = 0, rely = 1.0, y = -5, anchor = "s")


label_10 = Label(root,
                text = "Hello world\nHello Tia\nHello Leo",
                bd = 1,
                relief = "solid",
                background = "yellow",
                font = "Times 18",
                width = 15,
                height = 3
               )

label_10.place(relx = 0, x = 5, rely = 0.5, y = 0, anchor = "w")


root.mainloop()
