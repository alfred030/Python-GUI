from tkinter import*
import random
import time
from tkinter import ttk

root = Tk()
root.title("Calculator")
root.resizable(False, False)
operator=""
text_Input = StringVar()

#=================================== frame======================================================


f1 = Frame(root, width = 300, height = 700, bg = "white", relief = SUNKEN)
f1.pack(side = RIGHT)




#==============Button function===================

# the first line the the tell python to display the out put on the screen when the button in click
# the third is the convert those numbers into strings
# this because python consider every input from the user as a string and not as numbers.
# the last line is to actually set thh operator on the screen.

def btnClick(numbers):
    global operator
    operator = operator + str(numbers)
    text_Input.set(operator)
    
#==============Equal button function==============
    
# the third line is to always display zero on the screen when it is clear.
def Clearbutton():
    global operator
    operator = ""
    text_Input.set("0")

#==============Clear button function=============
    
# the second line is to evaluate the operator
# the third is to input the result on the screen.
def Equalbutton():
    global operator
    sumup = str(eval(operator))
    text_Input.set(sumup)
    operator = ""

#=======================================Variables===============================================
insertwidth_1 ="0"
font_1 = ""
height_text = 20
height_text1 = 16
bd_1 = "3"
bd_2 = 1
bg_1 = "gray"
bg_2 = "white"
padx_1 = "4"
pady_1 = "4"
# this is the color of the text
fg_1 = "black"
bold_1 = ""
width_1 = 2 
height_1 = 1 

#===============================Calculator=======================================================
text_Input = StringVar()
txtDisplay = Entry(f1,font=(font_1, 50, bold_1),
                   textvariable=text_Input,
                   bd="17",
                   insertwidth=insertwidth_1,
                   width =4,
                   bg="powder blue",
                   ).grid(columnspan=4)

#==============Button function===================
btn7=Button(f1,padx=padx_1,pady=pady_1,
            font=(font_1, height_text, bold_1),
            bd=bd_1,
            bg=bg_1,
            text = "7",
            width=width_1,
            height=height_1,
            command = lambda:btnClick(7)).grid(row=2,column=0)

                         #===============First row===================              
btn8=Button(f1,padx=padx_1,pady=pady_1,
            font=(font_1, height_text, bold_1),
            bd=bd_1,
            bg=bg_1,
            text = "8",
            width=width_1,
            height=height_1,
            command = lambda:btnClick(8)).grid(row=2,column=1)       

btn9=Button(f1,padx=padx_1,pady=pady_1,
            font=(font_1, height_text, bold_1),
            bd=bd_1,
            bg=bg_1,
            text = "9",
            width=width_1,
            height=height_1,
            command = lambda:btnClick(9)).grid(row=2,column=2)

Addition=Button(f1,padx=padx_1,pady=pady_1,
            font=(font_1, height_text, bold_1),
            bd=bd_1,
            bg=bg_1,
            text = "+",
            width=width_1,
            height=height_1,    
            command = lambda:btnClick("+")).grid(row=2,column=3)

                        #===============Second row===================   
btn4=Button(f1,padx=padx_1,pady=pady_1,
            font=(font_1, height_text, bold_1),
            bd=bd_1,
            bg=bg_1,
            text = "4",
            width=width_1,
            height=height_1,
            command = lambda:btnClick(4)).grid(row=3,column=0)
            
btn5=Button(f1,padx=padx_1,pady=pady_1,
            font=(font_1, height_text, bold_1),
            bd=bd_1,
            bg=bg_1,
            text = "5",
            width=width_1,
            height=height_1,
            command = lambda:btnClick(5)).grid(row=3,column=1)       

btn6=Button(f1,padx=padx_1,pady=pady_1,
            font=(font_1, height_text, bold_1),
            bd=bd_1,
            bg=bg_1,
            text = "6",
            width=width_1,
            height=height_1,
            command = lambda:btnClick(6)).grid(row=3,column=2)

Subtractin=Button(f1,padx=padx_1,pady=pady_1,
            font=(font_1, height_text, bold_1),
            bd=bd_1,
            bg=bg_1,
            text = "-",
            width=width_1,
            height=height_1,
            command = lambda:btnClick("-")).grid(row=3,column=3)


                     # ===============third row===================
btn1=Button(f1,padx=padx_1,pady=pady_1,
            font=(font_1, height_text, bold_1),
            bd=bd_1,
            bg=bg_1,
            text = "1",
            width=width_1,
            height=height_1,
            command = lambda:btnClick(1)).grid(row=4,column=0)
            
btn2=Button(f1,padx=padx_1,pady=pady_1,
            font=(font_1, height_text, bold_1),
            bd=bd_1,
            bg=bg_1,
            text = "2",
            width=width_1,
            height=height_1,
            command = lambda:btnClick(2)).grid(row=4,column=1)       

btn3=Button(f1,padx=padx_1,pady=pady_1,
            font=(font_1, height_text, bold_1),
            bd=bd_1,
            bg=bg_1,
            text = "3",
            width=width_1,
            height=height_1,
            command = lambda:btnClick(3)).grid(row=4,column=2)

Multiplication=Button(f1,padx=padx_1,pady=pady_1,
            font=(font_1, height_text, bold_1),
            bd=bd_1,
            bg=bg_1,
            text = "*",
            width=width_1,
            height=height_1,
            command = lambda:btnClick("*")).grid(row=4,column=3)

                     #===============Fought row===================   
btn0=Button(f1,padx=padx_1,pady=pady_1,
            font=(font_1, height_text, bold_1),
            bd=bd_1,
            bg=bg_1,
            text = "0",
            width=width_1,
            height=height_1,
            command = lambda:btnClick(0)).grid(row=5,column=0)
            
btnClear=Button(f1,padx=padx_1,pady=pady_1,
            font=(font_1, height_text, bold_1),
            bd=bd_1,
            bg=bg_1,
            text = "C",
            width=width_1,
            height=height_1,
            command = Clearbutton).grid(row=5,column=1)       

btnEqual=Button(f1,padx=padx_1,pady=pady_1,
            font=(font_1, height_text, bold_1),
            bd=bd_1,
            bg=bg_1,
            text = "=",
            width=width_1,
            height=height_1,
            command = Equalbutton).grid(row=5,column=2)

Division=Button(f1,padx=padx_1,pady=pady_1,
            font=(font_1, height_text, bold_1),
            bd=bd_1,
            bg=bg_1,
            text = "/",
            width=width_1,
            height=height_1,
            command = lambda:btnClick("/")).grid(row=5,column=3)


root.mainloop()
                
