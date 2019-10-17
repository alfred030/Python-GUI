from tkinter import *
from tkinter import ttk


# this is the main root or main window
root = Tk()
# this is the app title
root.title("TIA CALCULATOR")
root.resizable(0, 0)
               
# globe variable.
font_1 = "Helvertica"
h = 16
style = "italic"

fg_1 = "white"
fg_2 = "black"
fg_on = "red"
fg_off = "blue"
fg_exit = "light blue"
color = "grey"
borderwidth_1 = 2

# bold
# italic

# white
# beige
# light blue
# grey
# lavender
# olive

class Application(Frame):
    def __init__(self, master): # to initillaze this window
        self.master = master


        # dISPLAY
        self.display=Entry(self.master,
                           font=(font_1 ,45,style),
                           relief=SUNKEN,
                           justify=RIGHT,
                           bg="light blue",bd=5, width = 8)
        self.display.insert(0, "")
        self.display.focus()
        self.display.grid(row=0, column=0, columnspan=4)
        self.master.iconbitmap('m1.ico')
        
        # ROW 1
        self.but1=Button(self.master,
                         bg=color,
                         text="sin",fg=fg_1,
                         font=(font_1 ,h, style),
                         borderwidth=borderwidth_1)
        self.but1.grid(row=2, column=0,sticky="NWNESWSE")

        self.but2=Button(self.master,
                         bg=color,
                         text="cos",
                         fg=fg_1,
                         font=(font_1 ,h, style),
                         borderwidth=borderwidth_1)
        self.but2.grid(row=2, column=1,sticky="NWNESWSE")
        
        self.but3=Button(self.master,
                         bg=color,
                         text="tan",fg=fg_1,
                         font=(font_1 ,h, style),
                         borderwidth=borderwidth_1)
        self.but3.grid(row=2, column=2,sticky="NWNESWSE")

        self.but4=Button(self.master,
                         bg=color,
                         text="  on  ",
                         fg=fg_on,
                         font=(font_1 ,h, style),
                         borderwidth=borderwidth_1)
        self.but4.grid(row=2, column=3,sticky="NWNESWSE")
        

        # ROW 2 
        self.but5=Button(self.master,
                         bg=color,
                         text="csc",
                         fg=fg_1,
                         font=(font_1 ,h, style),
                         borderwidth=borderwidth_1)
        self.but5.grid(row=3, column=0,sticky="NWNESWSE")

        self.but6=Button(self.master,
                         bg=color,
                         text="sec",
                         fg=fg_1,
                         font=(font_1 ,h, style),
                         borderwidth=borderwidth_1)
        self.but6.grid(row=3, column=1,sticky="NWNESWSE")
        
        self.but7=Button(self.master,
                         bg=color,
                         text="cot",
                         fg=fg_1,
                         font=(font_1 ,h, style),
                         borderwidth=borderwidth_1)
        self.but7.grid(row=3, column=2,sticky="NWNESWSE")

        self.but8=Button(self.master,
                         bg=color,
                         text="  off  ",
                         fg=fg_off,
                         font=(font_1 ,h, style),
                         borderwidth=borderwidth_1)
        self.but8.grid(row=3, column=3,sticky="NWNESWSE")



        # ROW 3
        self.but9=Button(self.master,
                         bg=color,
                         text="asinh ",
                         fg=fg_1,
                         font=(font_1 ,h, style),
                         borderwidth=borderwidth_1)
        self.but9.grid(row=4, column=0,sticky="NWNESWSE")

        self.but10=Button(self.master,
                          bg=color,
                          text="acosh",
                          fg=fg_1,
                          font=(font_1 ,h, style),
                          borderwidth=borderwidth_1)
        self.but10.grid(row=4, column=1,sticky="NWNESWSE")
        
        self.but11=Button(self.master,
                          bg=color,
                          text="atanh",
                          fg=fg_1,
                          font=(font_1 ,h, style),
                          borderwidth=borderwidth_1)
        self.but11.grid(row=4, column=2,sticky="NWNESWSE")

        self.but12=Button(self.master,
                          bg=color,
                          text="exit",
                          fg=fg_exit,
                          font=(font_1 ,h, style),
                          borderwidth=borderwidth_1)
        self.but12.grid(row=4, column=3,sticky="NWNESWSE")



        # ROW 4
        self.but13=Button(self.master,
                          bg=color,
                          text="exp",
                          fg=fg_1,
                          font=(font_1 ,h, style),
                          borderwidth=borderwidth_1)
        self.but13.grid(row=5, column=0,sticky="NWNESWSE")

        self.but14=Button(self.master,
                          bg=color,
                          text="deg",
                          fg=fg_1,
                          font=(font_1 ,h, style),
                          borderwidth=borderwidth_1)
        self.but14.grid(row=5, column=1,sticky="NWNESWSE")
        
        self.but15=Button(self.master,
                          bg=color,
                          text="←",
                          fg=fg_1,
                          font=(font_1 ,h, style),
                          borderwidth=borderwidth_1)
        self.but15.grid(row=5, column=2,sticky="NWNESWSE")

        self.but16=Button(self.master,
                          bg=color,
                          text="  C  ",
                          fg=fg_1,
                          font=(font_1 ,h, style),
                          borderwidth=borderwidth_1)
        self.but16.grid(row=5, column=3,sticky="NWNESWSE")

        

        # ROW 5
        self.but17=Button(self.master,
                          bg=color,
                          text="e",
                          fg=fg_1,
                          font=(font_1 ,h, style),
                          borderwidth=borderwidth_1)
        self.but17.grid(row=6, column=0,sticky="NWNESWSE")

        self.but18=Button(self.master,
                          bg=color,
                          text="log",
                          fg=fg_1,
                          font=(font_1 ,h, style),
                          borderwidth=borderwidth_1)
        self.but18.grid(row=6, column=1,sticky="NWNESWSE")
        
        self.but19=Button(self.master,
                          bg=color,
                          text="π",
                          fg=fg_1,
                          font=(font_1 ,h, style),
                          borderwidth=borderwidth_1)
        self.but19.grid(row=6, column=2,sticky="NWNESWSE")

        self.but20=Button(self.master,
                          bg=color,
                          text="  %  ",
                          fg=fg_1,
                          font=(font_1 ,h, style),
                          borderwidth=borderwidth_1)
        self.but20.grid(row=6, column=3,sticky="NWNESWSE")

       

        # ROW 6
        self.but21=Button(self.master,
                          bg=color,
                          text="√",
                          fg=fg_2,
                          font=(font_1 ,h, style),
                          borderwidth=borderwidth_1)
        self.but21.grid(row=7, column=0,sticky="NWNESWSE")

        self.but22=Button(self.master,
                          bg=color,
                          text="(" ,
                          fg=fg_2,
                          font=(font_1 ,h, style),
                          borderwidth=borderwidth_1)
        self.but22.grid(row=7, column=1,sticky="NWNESWSE")
        
        self.but23=Button(self.master,
                          bg=color,
                          text=")",
                          fg=fg_2,
                          font=(font_1 ,h, style),
                          borderwidth=borderwidth_1)
        self.but23.grid(row=7, column=2,sticky="NWNESWSE")

        self.but24=Button(self.master,
                          bg=color,
                          text="  +  ",
                          fg=fg_2,
                          font=(font_1 ,h, style),
                          borderwidth=borderwidth_1)
        self.but24.grid(row=7, column=3,sticky="NWNESWSE")

        

        # ROW 7
        self.but25=Button(self.master,
                          bg=color,
                          text="7",
                          fg=fg_2,
                          font=(font_1 ,h, style),
                          borderwidth=borderwidth_1)
        self.but25.grid(row=8, column=0,sticky="NWNESWSE")

        self.but26=Button(self.master,
                          bg=color,
                          text="8",
                          fg=fg_2,
                          font=(font_1 ,h, style),
                          borderwidth=borderwidth_1)
        self.but26.grid(row=8, column=1,sticky="NWNESWSE")
        
        self.but27=Button(self.master,
                          bg=color,
                          text="9",
                          fg=fg_2,
                          font=(font_1 ,h, style),
                          borderwidth=borderwidth_1)
        self.but27.grid(row=8, column=2,sticky="NWNESWSE")

        self.but28=Button(self.master,
                          bg=color,
                          text="  ÷  ",
                          fg=fg_2,
                          font=(font_1 ,h, style),
                          borderwidth=borderwidth_1)
        self.but28.grid(row=8, column=3,sticky="NWNESWSE")
        


        # ROW 8
        self.but29=Button(self.master,
                          bg=color,
                          text="4",
                          fg=fg_2,
                          font=(font_1 ,h, style),
                          borderwidth=borderwidth_1)
        self.but29.grid(row=9, column=0,sticky="NWNESWSE")

        self.but30=Button(self.master,
                          bg=color,
                          text="5",
                          fg=fg_2,
                          font=(font_1 ,h, style),
                          borderwidth=borderwidth_1)
        self.but30.grid(row=9, column=1,sticky="NWNESWSE")
        
        self.but31=Button(self.master,
                          bg=color,
                          text="6",
                          fg=fg_2,
                          font=(font_1 ,h, style),
                          borderwidth=borderwidth_1)
        self.but31.grid(row=9, column=2,sticky="NWNESWSE")

        self.but32=Button(self.master,
                          bg=color,
                          text="  x  ",
                          fg=fg_2,
                          font=(font_1 ,h, style),
                          borderwidth=borderwidth_1)
        self.but32.grid(row=9, column=3,sticky="NWNESWSE")

        

        # ROW 9
        self.but33=Button(self.master,
                          bg=color,
                          text="1",
                          fg=fg_2,
                          font=(font_1 ,h, style),
                          borderwidth=borderwidth_1)
        self.but33.grid(row=10, column=0,sticky="NWNESWSE")

        self.but34=Button(self.master,
                          bg=color,
                          text="2",
                          fg=fg_2,
                          font=(font_1 ,h, style),
                          borderwidth=borderwidth_1)
        self.but34.grid(row=10, column=1,sticky="NWNESWSE")
        
        self.but35=Button(self.master,
                          bg=color,
                          text="3",
                          fg=fg_2,
                          font=(font_1 ,h, style),
                          borderwidth=borderwidth_1)
        self.but35.grid(row=10, column=2,sticky="NWNESWSE")

        self.but36=Button(self.master,
                          bg=color,
                          text="  -  ",
                          fg=fg_2,
                          font=(font_1 ,h, style),
                          borderwidth=borderwidth_1)
        self.but36.grid(row=10, column=3,sticky="NWNESWSE")

        

        # ROW 10
        self.but37=Button(self.master,
                          bg=color,
                          text="0",
                          fg=fg_2,
                          font=(font_1 ,h, style),
                          borderwidth=borderwidth_1)
        self.but37.grid(row=11, column=0,sticky="NWNESWSE")

        self.but38=Button(self.master,
                          bg=color,
                          text="±",
                          fg=fg_2,
                          font=(font_1 ,h, style),
                          borderwidth=borderwidth_1)
        self.but38.grid(row=11, column=1,sticky="NWNESWSE")

        self.but39=Button(self.master,
                          bg=color,text=".",
                          fg=fg_2,
                          font=(font_1 ,h, style),
                          borderwidth=borderwidth_1)
        self.but39.grid(row=11, column=2,sticky="NWNESWSE")
        
        self.but40=Button(self.master,
                          bg=color,
                          text="  =  ",
                          fg=fg_2,
                          font=(font_1 ,h, style),
                          borderwidth=borderwidth_1)
        self.but40.grid(row=11, column=3,sticky="NWNESWSE")

            


def main ():
    app = Application(root)
    root.mainloop()

if __name__ == '__main__':  main()
   




