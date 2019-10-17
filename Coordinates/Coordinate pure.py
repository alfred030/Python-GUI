
from tkinter import *
from tkinter import ttk        
    
root = Tk()
root.geometry("800x450")
# this is the app title
root.title("Coordinate In Python GUI")


# anchor  vary between 0 and 1 in the x and y direction.
label_1 = Label(root,
                text = "anchor = center\nrelx = 0.5, rely = 0.5\nrelief = solid",
                bd = 1,
                relief = "solid",
                background = "grey",
                font = "Times 12",
                width = 15,
                height = 4
               )
label_1.place(relx = 0.5,
              rely = 0.5,
              anchor = 'center',
              )


# This the 0,0 coordinate
label_2 = Label(root,
                text = "anchor = nw\nrelx = 0, rely = 0\nrelief = raised\nx = 5, y = 5",
                bd = 1,
                relief = "raised",
                background = "tan",
                font = "Times 12",
                width = 15,
                height = 4
               )
label_2.place(relx = 0, x = 5, rely = 0, y = 5, anchor = "nw")



label_3 = Label(root,
                text = "anchor = sw\nrelx = 0, rely = 1\nrelief = groove\nx = 5, y = -5",
                bd = 1,
                relief = "groove",
                background = "cyan",
                font = "Times 12",
                width = 15,
                height = 4
               )
label_3.place(relx = 0, x = 5, rely = 1, y = -5, anchor = "sw")



label_4 = Label(root,
                text = "anchor = ne\nrelx = 1.0, rely = 0\nrelief = ridge\nx = -5, y = 5",
                bd = 1,
                relief = "ridge",
                background = "beige",
                font = "Times 12",
                width = 15,
                height = 4
               )
label_4.place(relx = 1.0, x= -5, rely = 0, y = 5, anchor = "ne")


label_5 = Label(root,
                text = "anchor = se\nrelx = 1.0, rely = 1.0\nrelief = sunken\nx = -5, y = -5",
                bd = 1,
                relief = "sunken",
                background = "yellow",
                font = "Times 12",
                width = 15,
                height = 4
               )
label_5.place(relx = 1.0, x = -5, rely = 1.0, y = -5, anchor = "se")


label_6 = Label(root,
                text = "anchor = n\nrelx = 0.5, rely = 0\nrelief = flat\nx = 0, y = 5",
                bd = 1,
                relief = "flat",
                background = "lavender",
                font = "Times 12",
                width = 15,
                height = 4
               )
label_6.place(relx = 0.5, x = 0, rely = 0, y = 5, anchor = "n")


label_7 = Label(root,
                text = "anchor = s\nrelx = 0.5, rely = 1.0\nrelief = sunken\nx = 0, y = -5",
                bd = 1,
                relief = "sunken",
                background = "pink",
                font = "Times 12",
                width = 15,
                height = 4
               )
label_7.place(relx = 0.5, x = 0, rely = 1.0, y = -5, anchor = "s")



label_8 = Label(root,
                text = "anchor = w\nrelx = 0, rely = 0.5\nrelief = raised\nx = 5, y = 0",
                bd = 1,
                relief = "raised",
                background = "light green",
                font = "Times 12",
                width = 15,
                height = 4
               )
label_8.place(relx = 0, x = 5, rely = 0.5, y = 0, anchor = "w")


label_9 = Label(root,
                text = "anchor = e\nrelx = 1.0, rely = 0.5\nrelief = raised\nx = -5, y = 0",
                bd = 1,
                relief = "raised",
                background = "light blue",
                font = "Times 12",
                width = 15,
                height = 4
               )
label_9.place(relx = 1, x = -5, rely = 0.5, y = 0, anchor = "e")


label_10 = Label(root,
                text = "relx = 0.25\nrely = 0.25",
                bd = 1,
                relief = "raised",
                background = "plum",
                font = "Times 12",
                width = 10,
                height = 2
               )
label_10.place(relx = 0.25, rely = 0.25, )



label_11 = Label(root,
                text = "relx = 0.25\nrely = 0.75",
                bd = 1,
                relief = "raised",
                background = "olive",
                font = "Times 12",
                width = 10,
                height = 2
               )
label_11.place(relx = 0.25, rely = 0.75, )


label_12 = Label(root,
                text = "relx = 0.75\nrely = 0.25",
                bd = 1,
                relief = "raised",
                background = "purple",
                font = "Times 12",
                width = 10,
                height = 2
               )
label_12.place(relx = 0.75, rely = 0.25, )



label_13 = Label(root,
                text = "relx = 0.5, rely = 0.5\nrelief = ridge\nx = 100, y = 50",
                bd = 1,
                relief = "ridge",
                background = "salmon",
                font = "Times 12",
                width = 15,
                height = 4
               )
label_13.place(relx = 0.5,
              x = 100,
              rely = 0.5,
              y = 50,
              )

root.mainloop()
'''
label_14 = Label(root,
                text = "relx = 0.5, rely = 0.5\nrelief = ridge\nx = -250, y = 50",
                bd = 1,
                relief = "ridge",
                background = "salmon",
                font = "Times 12",
                width = 15,
                height = 4
               )
label_14.place(relx = 0.5,
              x = -250,
              rely = 0.5,
              y = 50,
              )
              
'''

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

'''
root.mainloop()
