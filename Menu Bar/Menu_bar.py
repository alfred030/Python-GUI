from tkinter import *
from tkinter import Menu
from tkinter import ttk
import time
from tkinter import messagebox

root = Tk()


# Exit GUI cleanly
def _quit():
    root.quit()
    root.destroy()
    exit()

def exit():
    qExit = messagebox.askyesno("Fast Food",
                                "This system is still running.\n\n"
                                "Do you want to quit?", icon="warning")
    if qExit > 0:
        root.destroy()
        return

# Creating a Menu Bar
menuBar = Menu(root)
root.config(menu=menuBar)

## Add menu items
fileMenu = Menu(menuBar, tearoff=0)
fileMenu.add_command(label="New")
fileMenu.add_separator()
fileMenu.add_command(label="Exit", command=exit)
menuBar.add_cascade(label="File", menu=fileMenu)

# Add another Menu to the Menu Bar and an item
helpMenu = Menu(menuBar, tearoff=0)
helpMenu.add_command(label="About")
menuBar.add_cascade(label="Help", menu=helpMenu)

# Tab Control introduced here -----------------------------------------
tabControl = ttk.Notebook(root)  # Create Tab Control

tab1 = ttk.Frame(tabControl)  # Create a tab
tabControl.add(tab1, text='Find and replace')  # Add the tab

tab2 = ttk.Frame(tabControl)  # Add a second tab
tabControl.add(tab2, text='Time & Date')  # Make second tab visible

tab3 = ttk.Frame(tabControl)  # Add a second tab
tabControl.add(tab3, text='Text Entry')  # Make second tab visible

tabControl.pack(expand=1, fill="both")  # Pack to make visible
# ~ Tab Control introduced here -----------------------------------------


root.title('Find & Replace')
# root.resizable(0,0)
Label(tab1, text="Find:").grid(row=0, column=0, sticky='e')
Entry(tab1, width=60).grid(row=0, column=1,
                           padx=2, pady=2, sticky='we', columnspan=9)
Label(tab1, text="Replace:").grid(row=1, column=0, sticky='e')
Entry(tab1).grid(row=1, column=1, padx=2, pady=2, sticky='we',
                 columnspan=9)
Button(tab1, text="Find").grid(
    row=0, column=10, sticky='e' + 'w', padx=2, pady=2)
Button(tab1, text="Find All").grid(
    row=1, column=10, sticky='e' + 'w', padx=2)
Button(tab1, text="Replace").grid(row=2, column=10, sticky='e' +
                                                           'w', padx=2)
Button(tab1, text="Replace All").grid(
    row=3, column=10, sticky='e' + 'w', padx=2)
Checkbutton(tab1, text='Match whole word only').grid(
    row=2, column=1, columnspan=4, sticky='w')
Checkbutton(tab1, text='Match Case').grid(
    row=3, column=1, columnspan=4, sticky='w')
Checkbutton(tab1, text='Wrap around').grid(
    row=4, column=1, columnspan=4, sticky='w')
Label(tab1, text="Direction:").grid(row=2, column=6, sticky='w')
Radiobutton(tab1, text='Up', value=1).grid(
    row=3, column=6, columnspan=6, sticky='w')
Radiobutton(tab1, text='Down', value=2).grid(
    row=3, column=7, columnspan=2, sticky='e')

Date_1 = StringVar()
Time_1 = StringVar()

Date_1.set(time.strftime("%d/%m/%y"))
Time_1.set(time.strftime("%H:%M:%S"))

label_time = Label(tab2, textvariable=Time_1,
                   font=("arial", 30, "bold"),
                   bd=5,
                   fg="black",
                   bg="Cadet Blue",
                   padx=10,
                   pady=10)
label_time.pack()

label_date = Label(tab2, textvariable=Date_1,
                   font=("arial", 30, "bold"),
                   bd=5,
                   fg="red",
                   bg="white",
                   padx=10,
                   pady=10)
label_date.pack()


# ---------------------------------------------------------------------------------------------
def tick():
    time_string = time.strftime("%H:%M:%S")
    clock.config(text=time_string)
    clock.after(200, tick)


clock = Label(tab2, font=("arial", 30, "bold"),
              bg="Cadet Blue",
              bd=5,
              fg="black",
              padx=10,
              pady=10
              )
clock.pack()
tick()  # we just call the tick function so that it ca display the time.

text = Text(tab3, width=100, heigh=20)
text.pack()

root.mainloop()
