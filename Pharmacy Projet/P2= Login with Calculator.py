from tkinter import *
from tkinter import messagebox
from tkinter import ttk
import random
import time
import datetime

def main ():
    root = Tk()
    app = window1(root)
#==============================================================================================
# globe variables for login. it can be use in any class (this not local variable)
font_1 = "Helvertica"
h1 = 16
#color = "grey"

# master window
class window1:
    def __init__(self, master): # to initialize this window
        self.master = master
        self.master.resizable(False, False)
        self.master.title("HOSPITAL LOGIN SYSTEM")
        self.master.configure(bg= '#dbdbdb')


# Variables declaration (for the rest button)
        self.entry_Username = StringVar()
        self.entry_Password = StringVar()


        self.label=ttk.Label(self.master, text='Username',background = '#dbdbdb',font = ('Time', 10))
        self.label.grid(row=0, column=0, pady = 10, padx = 1)

        self.label=ttk.Label(self.master, text='Password',background = '#dbdbdb',font = ('Time', 10))
        self.label.grid(row=1, column=0, pady = 5, padx = 1)

        self.entry_Username = ttk.Entry(self.master, width = 25, font = ('Time', 10))
        self.entry_Username.focus() # this put the cursor in the entry name when we run the program
        self.entry_Password = ttk.Entry(self.master, width = 25, font = ('Time', 10))
        self.entry_Password.config(show = '*')# this is to hid the password
        self.entry_Username.grid(row = 0, column = 1, padx = 1, columnspan=3,sticky ='e'+'w')# to expand the Entry
        self.entry_Password.grid(row = 1, column = 1, padx = 1, columnspan=3,sticky ='e'+'w')

        self.btn1=ttk.Button(self.master, text='Login',command = self.Login_System)
        self.btn1.grid(row=2, column=0,sticky = 'e'+'w',pady = 5,padx = 1)
        self.btn2=ttk.Button(self.master, text='Reset',command = self.Reset)
        self.btn2.grid(row=2, column=1,sticky = 'e'+'w',pady = 5,padx = 1)
        self.btn3=ttk.Button(self.master, text='Sign out or exit',command = self.iExit_1)
        self.btn3.grid(row=2, column=2,sticky = 'e'+'w',pady = 5,padx = 1)
        self.btn3=ttk.Button(self.master, text='Calculator ', command = self.Cal)
        self.btn3.grid(row=2, column=3,sticky = 'e'+'w',pady = 5,padx = 1)

        # most use string while using lower case normal or disabled and no string with upper case latter
        # state = "disabled" or DISABLED, state = NORMAL or "normal"
        self.btnRegistration = ttk.Button(self.master, text="Patients Registration Systems",
                                      state=DISABLED,
                                      command=self.Registration_window)
        self.btnRegistration.grid(row=3, column=0,columnspan=2,sticky = 'e'+'w',pady = 5,padx = 1)

        self.btnHospital = ttk.Button(self.master, text="Hospital Management Systems",
                                      state=DISABLED,
                                      command=self.Hospital_window)
        self.btnHospital.grid(row=3, column=2,columnspan=2, sticky = 'e'+'w',pady = 1,padx = 1)



# Login system
    def Login_System(self):
        username = (self.entry_Username.get())
        password = (self.entry_Password.get())

        if(username == str("tia12345")) and (password == str(12345)): #tia12345 most be a srting
            self.btnRegistration.config(state = NORMAL)
            self.btnHospital.config(state = NORMAL)

        elif(username == str("1")) and (password == str(1)): #tia12345 most be a srting
            self.btnRegistration.config(state = NORMAL)
            self.btnHospital.config(state = NORMAL)

        elif(username == str("2"))or(username == str("3")) and (password == str(2))or (password == str(3)): #tia12345 most be a srting
            self.btnRegistration.config(state = NORMAL)
            self.btnHospital.config(state = DISABLED)

        elif(username == str("4"))or(username == str("5")) and (password == str(4))or (password == str(5)): #tia12345 most be a srting
            self.btnRegistration.config(state = DISABLED)
            self.btnHospital.config(state = NORMAL)


        else:
            messagebox.askretrycancel("Hospital Login System", "Invalid password or username",
                                      icon = "error")# put this first
            self.btnRegistration.config(state = DISABLED)# this means keep the button disable because of wrong password
            self.btnRegistration.config(state = DISABLED)
            #self.entry_Username.set("")
            #self.entry_Password.set("")# this set the entry to zero if wrong password or username
            self.entry_Username.focus() #put the cursor in the username entry


# Reset button function
#self.entry_Username = StringVar()
#self.entry_Password = StringVar()

    def Reset(self):
        self.entry_Username.delete(0, 'end')
        self.entry_Password.delete(0, 'end')
        self.btnRegistration.config(state = DISABLED)#these two lines of code will lock the user out
        self.btnHospital.config(state = DISABLED)    #if the user sign in and click on reset button
        self.entry_Username.focus() #this set the entry to zero if wrong password or username


# Sign out button function

    def iExit_1(self):
        self.qExit = messagebox.askyesno("Hospital Login System",
                                    "This system is still running.\n"
                                    "Are you sure that you want to sign out?",
                                    icon = "warning")
        if self.qExit > 0:
            self.master.destroy()
            return


#==============================================================================================
# Registration management system
    def Registration_window(self):
        self.master_1 = Toplevel(self.master)
        self.app = PatientsRegistration(self.master_1)
        self.master_1.title("Patients Registration Systems")  #title of the window


        # globe variable.
        font_1 = "time"
        h = 12
        style = ""

        bg_1 = "powder blue"
        fg_off = "blue"
        fg_exit = "light blue"
        color = "grey"

        bd_Frames = 5
        bd_MainFrames = 5
        relief_1 = GROOVE

        padx_1 = 2
        pady_1 = 4

        Width_Label = "0"
        Width_Entry = 25

        sticky_label = 'w'
        sticky_Entry = 'e' + 'w'

        # FLAT, RAISED, SUNKEN, GROOVE, RIDGE
        # style = "italic"
        # style = "


# Variables declaration
        cmbNameTablets = StringVar()
        Ref = StringVar()
        NumberTablets = StringVar()
        Lot = StringVar()
        Dose = StringVar()
        IssueDate = StringVar()
        ExpDate = StringVar()
        DailyDose = StringVar()
        PossibleSideEffects = StringVar()
        FurtherInformation = StringVar()
        StorageAdvice = StringVar()
        DrivingUsingMachines = StringVar()
        HowToUseMedication = StringVar()
        PatientID = StringVar()
        PatientNHSNO = StringVar()
        PatientName = StringVar()
        DateOfBirth = StringVar()
        PatientAddress = StringVar()
        Prescription = StringVar()


# Frames
        MainFrame = ttk.Frame(self.master_1)
        MainFrame.grid()

        TitleFrame = ttk.Frame(MainFrame)
        TitleFrame.pack(side=TOP)

        ButtonFrame = ttk.Frame(MainFrame)
        ButtonFrame.pack(side=BOTTOM)

        DataFrame = Frame(MainFrame, bd=bd_MainFrames, relief=RIDGE)
        DataFrame.pack(side=BOTTOM)

        DataFrameLEFT = LabelFrame(DataFrame,
                                   relief=relief_1,
                                   font=(font_1, h, style),
                                   bd=bd_Frames, text="Prescription")
        DataFrameLEFT.pack(side=LEFT)

        DataFrameRIGHT = LabelFrame(DataFrame,
                                    relief=relief_1,
                                    bd=bd_Frames,
                                    height=330,
                                    width=300,
                                    font=(font_1, h, style),
                                    text="Patient Information")
        DataFrameRIGHT.pack(side=RIGHT)


# DataFrameLEFT Label 1
        self.lblTitle = ttk.Label(MainFrame,
                                  font=("arial", 18, "bold"),
                                  text=("Hospital Management System"))
        self.lblTitle.pack()

        self.lblTitle = ttk.Label(DataFrameLEFT,
                                  font=("arial", 18, "bold"),
                                  text=("\t\t\tPatient Prescription"))
        self.lblTitle.grid(row=0, column=0, columnspan=3, sticky="NWNESWSE")

        self.lblNameOfTablet = Label(DataFrameLEFT,
                                     font=(font_1, h, style),
                                     padx=padx_1,
                                     pady=pady_1,
                                     width=Width_Label,
                                     # textvariable = NumberTablets,
                                     text="Name of Tablets")
        self.lblNameOfTablet.grid(row=1, column=0, sticky=sticky_label)

        self.lblRef = Label(DataFrameLEFT,
                            font=(font_1, h, style),
                            padx=padx_1,
                            pady=pady_1,
                            width=Width_Label,
                            text="Reference No:")
        self.lblRef.grid(row=2, column=0, sticky=sticky_label)

        self.lblDose = Label(DataFrameLEFT,
                             font=(font_1, h, style),
                             padx=padx_1,
                             pady=pady_1,
                             width=Width_Label,
                             text="Dose:")
        self.lblDose.grid(row=3, column=0, sticky=sticky_label)

        self.lblNo = Label(DataFrameLEFT,
                           font=(font_1, h, style),
                           padx=padx_1,
                           pady=pady_1,
                           width=Width_Label,
                           text="No of tablet:")
        self.lblNo.grid(row=4, column=0, sticky=sticky_label)

        self.lblLot = Label(DataFrameLEFT,
                            font=(font_1, h, style),
                            padx=padx_1,
                            pady=pady_1,
                            width=Width_Label,
                            text="Lot:")
        self.lblLot.grid(row=5, column=0, sticky=sticky_label)

        self.lblIssueDate = Label(DataFrameLEFT,
                                  font=(font_1, h, style),
                                  padx=padx_1,
                                  pady=pady_1,
                                  width=Width_Label,
                                  text="Issue Date:")
        self.lblIssueDate.grid(row=6, column=0, sticky=sticky_label)

        self.lblEpxDate = Label(DataFrameLEFT,
                                font=(font_1, h, style),
                                padx=padx_1,
                                pady=pady_1,
                                width=Width_Label,
                                text="Exp Date:")
        self.lblEpxDate.grid(row=7, column=0, sticky=sticky_label)

        self.lblDailyDose = Label(DataFrameLEFT,
                                  font=(font_1, h, style),
                                  padx=padx_1,
                                  pady=pady_1,
                                  width=Width_Label,
                                  text="Daily Dose:")
        self.lblDailyDose.grid(row=8, column=0, sticky=sticky_label)

        self.lblSideEffects = Label(DataFrameLEFT,
                                    font=(font_1, h, style),
                                    padx=padx_1,
                                    pady=pady_1,
                                    width=Width_Label,
                                    text="Side Effects:")
        self.lblSideEffects.grid(row=9, column=0, sticky=sticky_label)

# ==============================================================================================
# DataFrameLEFT Entry 1

        self.cboNameTablet = ttk.Combobox(DataFrameLEFT,
                                          textvariable=cmbNameTablets,
                                          state="readonly",
                                          font=(font_1, h, style),
                                          width=Width_Entry)
        self.cboNameTablet["value"] = ("", "Ibuprofen", "Co-codamol")
        self.cboNameTablet.current(0)
        self.cboNameTablet.grid(row=1, column=1, sticky=sticky_Entry)

        self.txtRef = Entry(DataFrameLEFT,
                            font=(font_1, h, style),
                            width=Width_Entry,
                            textvariable=Ref)
        self.txtRef.grid(row=2, column=1, sticky=sticky_Entry)

        self.txtDose = Entry(DataFrameLEFT,
                             font=(font_1, h, style),
                             width=Width_Entry,
                             textvariable=Dose)
        self.txtDose.grid(row=3, column=1, sticky=sticky_Entry)

        self.txtNo = Entry(DataFrameLEFT,
                           font=(font_1, h, style),
                           width=Width_Entry,
                           textvariable=Dose)
        self.txtNo.grid(row=4, column=1, sticky=sticky_Entry)

        self.txtLot = Entry(DataFrameLEFT,
                            font=(font_1, h, style),
                            width=Width_Entry,
                            textvariable=Dose)
        self.txtLot.grid(row=5, column=1, sticky=sticky_Entry)

        self.txtIssueDate = Entry(DataFrameLEFT,
                                  font=(font_1, h, style),
                                  width=Width_Entry,
                                  textvariable=Dose)
        self.txtIssueDate.grid(row=6, column=1, sticky=sticky_Entry)

        self.txtExp = Entry(DataFrameLEFT,
                            font=(font_1, h, style),
                            width=Width_Entry,
                            textvariable=Dose)
        self.txtExp.grid(row=7, column=1, sticky=sticky_Entry)

        self.txtDailyDose = Entry(DataFrameLEFT,
                                  font=(font_1, h, style),
                                  width=Width_Entry,
                                  textvariable=Dose)
        self.txtDailyDose.grid(row=8, column=1, sticky=sticky_Entry)

        self.txtSideEffects = Entry(DataFrameLEFT,
                                    font=(font_1, h, style),
                                    width=Width_Entry,
                                    textvariable=Dose)
        self.txtSideEffects.grid(row=9, column=1, sticky=sticky_Entry)

        # ==============================================================================================
# DataFrameLEFT Label 2

        self.lblFurtherIinfo = Label(DataFrameLEFT,
                                     font=(font_1, h, style),
                                     padx=padx_1,
                                     pady=pady_1,
                                     width=Width_Label,
                                     # textvariable = FurtherInformation,
                                     text="Further Information")
        self.lblFurtherIinfo.grid(row=1, column=2, sticky=sticky_label)

        self.lblStorage = Label(DataFrameLEFT,
                                font=(font_1, h, style),
                                padx=padx_1,
                                pady=pady_1,
                                width=Width_Label,
                                text="Storage Advise:")
        self.lblStorage.grid(row=2, column=2, sticky=sticky_label)

        self.lblDrivingMachines = Label(DataFrameLEFT,
                                        font=(font_1, h, style),
                                        padx=padx_1,
                                        pady=pady_1,
                                        width=Width_Label,
                                        text="Driving Machines:")
        self.lblDrivingMachines.grid(row=3, column=2, sticky=sticky_label)

        self.lblMedication = Label(DataFrameLEFT,
                                   font=(font_1, h, style),
                                   padx=padx_1,
                                   pady=pady_1,
                                   width=Width_Label,
                                   text="Medication:")
        self.lblMedication.grid(row=4, column=2, sticky=sticky_label)

        self.lblPatientID = Label(DataFrameLEFT,
                                  font=(font_1, h, style),
                                  padx=padx_1,
                                  pady=pady_1,
                                  width=Width_Label,
                                  text="Patient ID:")
        self.lblPatientID.grid(row=5, column=2, sticky=sticky_label)

        self.lblNHSNumber = Label(DataFrameLEFT,
                                  font=(font_1, h, style),
                                  padx=padx_1,
                                  pady=pady_1,
                                  width=Width_Label,
                                  text="NHS Number:")
        self.lblNHSNumber.grid(row=6, column=2, sticky=sticky_label)

        self.lblPatientName = Label(DataFrameLEFT,
                                    font=(font_1, h, style),
                                    padx=padx_1,
                                    pady=pady_1,
                                    width=Width_Label,
                                    text="Patient Name:")
        self.lblPatientName.grid(row=7, column=2, sticky=sticky_label)

        self.lblDateOfBirth = Label(DataFrameLEFT,
                                    font=(font_1, h, style),
                                    padx=padx_1,
                                    pady=pady_1,
                                    width=Width_Label,
                                    text="Date of Birth:")
        self.lblDateOfBirth.grid(row=8, column=2, sticky=sticky_label)

        self.lblPatientAddress = Label(DataFrameLEFT,
                                       font=(font_1, h, style),
                                       padx=padx_1,
                                       pady=pady_1,
                                       width=Width_Label,
                                       text="Patient Address:")
        self.lblPatientAddress.grid(row=9, column=2, sticky=sticky_label)

# ==============================================================================================
# DataFrameLEFT Entry 2

        self.txtFurtherInformation = Entry(DataFrameLEFT,
                                           font=(font_1, h, style),
                                           width=Width_Entry,
                                           textvariable=Ref)
        self.txtFurtherInformation.grid(row=1, column=3, sticky=sticky_Entry)

        self.txtStorageAdvice = Entry(DataFrameLEFT,
                                      font=(font_1, h, style),
                                      width=Width_Entry,
                                      textvariable=Ref)
        self.txtStorageAdvice.grid(row=2, column=3, sticky=sticky_Entry)

        self.txtDrivingMachine = Entry(DataFrameLEFT,
                                       font=(font_1, h, style),
                                       width=Width_Entry,
                                       textvariable=Ref)
        self.txtDrivingMachine.grid(row=3, column=3, sticky=sticky_Entry)

        self.txtPatientID = Entry(DataFrameLEFT,
                                  font=(font_1, h, style),
                                  width=Width_Entry,
                                  textvariable=Ref)
        self.txtPatientID.grid(row=4, column=3, sticky=sticky_Entry)

        self.txtNHS = Entry(DataFrameLEFT,
                            font=(font_1, h, style),
                            width=Width_Entry,
                            textvariable=Ref)
        self.txtNHS.grid(row=5, column=3, sticky=sticky_Entry)

        self.txtPatientName = Entry(DataFrameLEFT,
                                    font=(font_1, h, style),
                                    width=Width_Entry,
                                    textvariable=Ref)
        self.txtPatientName.grid(row=6, column=3, sticky=sticky_Entry)

        self.txtDateOfBirth = Entry(DataFrameLEFT,
                                    font=(font_1, h, style),
                                    width=Width_Entry,
                                    textvariable=Ref)
        self.txtDateOfBirth.grid(row=7, column=3, sticky=sticky_Entry)

        self.txtAddress = Entry(DataFrameLEFT,
                                font=(font_1, h, style),
                                width=Width_Entry,
                                textvariable=Ref)
        self.txtAddress.grid(row=8, column=3, sticky=sticky_Entry)



#==============================================================================================
# Hospital management system
    def Hospital_window(self):
        self.master_2 = Toplevel(self.master)
        self.app = HospitalRegistration(self.master_2)
        self.master_2.title("Hospital Registration Systems")

# ==============================================================================================
# calculator
    def Cal(self):
        self.master_3 = Toplevel(self.master)
        self.app = Calculator(self.master_3)
        self.master_3.title("Calculator")
        self.display = Entry(self.master_3,
                             font=(font_1, 35),
                             relief=SUNKEN,
                             justify=RIGHT,
                             bg='#ddffee', bd=8, width=9)
        # self.display.insert(0,"0")
        # self.display.focus()
        self.display.grid(row=1, column=0, columnspan=4)
        # self.master_3.iconbitmap(r'G:\\All programing\\Python\\music96x96.ico')


        # local variables for Calc
        font_2 = "Helvertica"
        h = 18
        style = "italic"

        fg_1 = "white"
        fg_2 = "black"
        fg_on = "red"
        fg_off = "blue"
        fg_exit = "light blue"
        color = "grey"
        borderwidth_1 = 3
        relief_1 = "ridge"


        # '#454545' ,
        #flat, groove, raised, ridge, solid, or sunken
        # bold
        # italic
        # Helvertica
        # white
        # beige
        # light blue
        # grey
        # lavender
        # olive


        # ROW 1
        self.but1 = Button(self.master_3,
                           bg=color,
                           text="on",
                           fg=fg_on,
                           font=(font_2, h, style),
                           relief=relief_1,
                           command=lambda: self.Onbuttom(),
                           borderwidth=borderwidth_1)
        self.but1.grid(row=5, column=0, sticky="NWNESWSE")

        self.but2 = Button(self.master_3,
                           bg=color,
                           text="off",
                           fg=fg_off,
                           font=(font_2, h, style),
                           relief=relief_1,
                           command=lambda: self.Offbuttom(),
                           borderwidth=borderwidth_1)
        self.but2.grid(row=5, column=1, sticky="NWNESWSE")

        self.but3 = Button(self.master_3,
                           bg=color,
                           text="E",
                           fg=fg_exit,
                           font=(font_2, h, style),
                           relief=relief_1,
                           command=self.iExit_2,
                           borderwidth=borderwidth_1)
        self.but3.grid(row=5, column=2, sticky="NWNESWSE")

        self.but4 = Button(self.master_3,
                           bg=color,
                           text="C",
                           fg=fg_1,
                           font=(font_2, h, style),
                           relief=relief_1,
                           command=lambda: self.clearText(),
                           borderwidth=borderwidth_1)
        self.but4.grid(row=5, column=3, sticky="NWNESWSE")

        # ROW 2
        self.but5 = Button(self.master_3,
                           bg=color,
                           text="%",
                           fg=fg_1,
                           font=(font_2, h, style),
                           relief=relief_1,
                           command=lambda: self.appendeTodisplay("%"),
                           borderwidth=borderwidth_1)
        self.but5.grid(row=7, column=0, sticky="NWNESWSE")

        self.but6 = Button(self.master_3,
                           bg=color,
                           text="(",
                           fg=fg_2,
                           font=(font_2, h, style),
                           relief=relief_1,
                           command=lambda: self.appendeTodisplay("("),
                           borderwidth=borderwidth_1)
        self.but6.grid(row=7, column=1, sticky="NWNESWSE")

        self.but7 = Button(self.master_3,
                           bg=color,
                           text=")",
                           fg=fg_2,
                           font=(font_2, h, style),
                           relief=relief_1,
                           command=lambda: self.appendeTodisplay(")"),
                           borderwidth=borderwidth_1)
        self.but7.grid(row=7, column=2, sticky="NWNESWSE")

        self.but8 = Button(self.master_3,
                           bg=color,
                           text="+",
                           fg=fg_2,
                           font=(font_2, h, style),
                           relief=relief_1,
                           command=lambda: self.appendeTodisplay("+"),
                           borderwidth=borderwidth_1)
        self.but8.grid(row=7, column=3, sticky="NWNESWSE")

        # ROW 3
        self.but9 = Button(self.master_3,
                           bg=color,
                           text="7",
                           fg=fg_2,
                           font=(font_2, h, style),
                           relief=relief_1,
                           command=lambda: self.appendeTodisplay("7"),
                           borderwidth=borderwidth_1)
        self.but9.grid(row=8, column=0, sticky="NWNESWSE")

        self.but10 = Button(self.master_3,
                            bg=color,
                            text="8",
                            fg=fg_2,
                            font=(font_2, h, style),
                            relief=relief_1,
                            command=lambda: self.appendeTodisplay("8"),
                            borderwidth=borderwidth_1)
        self.but10.grid(row=8, column=1, sticky="NWNESWSE")

        self.but11 = Button(self.master_3,
                            bg=color,
                            text="9",
                            fg=fg_2,
                            font=(font_2, h, style),
                            relief=relief_1,
                            command=lambda: self.appendeTodisplay("9"),
                            borderwidth=borderwidth_1)
        self.but11.grid(row=8, column=2, sticky="NWNESWSE")

        self.but12 = Button(self.master_3,
                            bg=color,
                            text="÷",
                            fg=fg_2,
                            font=(font_2, h, style),
                            relief=relief_1,
                            command=lambda: self.appendeTodisplay("/"),
                            borderwidth=borderwidth_1)
        self.but12.grid(row=8, column=3, sticky="NWNESWSE")

        # ROW 4
        self.but13 = Button(self.master_3,
                            bg=color,
                            text="4",
                            fg=fg_2,
                            font=(font_2, h, style),
                            relief=relief_1,
                            command=lambda: self.appendeTodisplay("4"),
                            borderwidth=borderwidth_1)
        self.but13.grid(row=9, column=0, sticky="NWNESWSE")

        self.but14 = Button(self.master_3,
                            bg=color,
                            text="5",
                            fg=fg_2,
                            font=(font_2, h, style),
                            relief=relief_1,
                            command=lambda: self.appendeTodisplay("5"),
                            borderwidth=borderwidth_1)
        self.but14.grid(row=9, column=1, sticky="NWNESWSE")

        self.but15 = Button(self.master_3,
                            bg=color,
                            text="6",
                            fg=fg_2,
                            font=(font_2, h, style),
                            relief=relief_1,
                            command=lambda: self.appendeTodisplay("6"),
                            borderwidth=borderwidth_1)
        self.but15.grid(row=9, column=2, sticky="NWNESWSE")

        self.but16 = Button(self.master_3,
                            bg=color,
                            text="x",
                            fg=fg_2,
                            font=(font_2, h, style),
                            relief=relief_1,
                            command=lambda: self.appendeTodisplay("*"),
                            borderwidth=borderwidth_1)
        self.but16.grid(row=9, column=3, sticky="NWNESWSE")

        # ROW 7
        self.but17 = Button(self.master_3,
                            bg=color,
                            text="1",
                            fg=fg_2,
                            font=(font_2, h, style),
                            relief=relief_1,
                            command=lambda: self.appendeTodisplay("1"),
                            borderwidth=borderwidth_1)
        self.but17.grid(row=10, column=0, sticky="NWNESWSE")

        self.but18 = Button(self.master_3,
                            bg=color,
                            text="2",
                            fg=fg_2,
                            font=(font_2, h, style),
                            relief=relief_1,
                            command=lambda: self.appendeTodisplay("2"),
                            borderwidth=borderwidth_1)
        self.but18.grid(row=10, column=1, sticky="NWNESWSE")

        self.but19 = Button(self.master_3,
                            bg=color,
                            text="3",
                            fg=fg_2,
                            font=(font_2, h, style),
                            relief=relief_1,
                            command=lambda: self.appendeTodisplay("3"),
                            borderwidth=borderwidth_1)
        self.but19.grid(row=10, column=2, sticky="NWNESWSE")

        self.but20 = Button(self.master_3,
                            bg=color,
                            text="-",
                            fg=fg_2,
                            font=(font_2, h, style),
                            relief=relief_1,
                            command=lambda: self.appendeTodisplay("-"),
                            borderwidth=borderwidth_1)
        self.but20.grid(row=10, column=3, sticky="NWNESWSE")

        # ROW 8
        self.but21 = Button(self.master_3,
                            bg=color,
                            text="0",
                            fg=fg_2,
                            font=(font_2, h, style),
                            relief=relief_1,
                            command=lambda: self.appendeTodisplay("0"),
                            borderwidth=borderwidth_1)
        self.but21.grid(row=11, column=0, sticky="NWNESWSE")

        self.but22 = Button(self.master_3,
                            bg=color,
                            text="←",
                            fg=fg_1,
                            font=(font_2, h, style),
                            command=lambda: self.Rbutton(),
                            relief=relief_1,
                            borderwidth=borderwidth_1)
        self.but22.grid(row=11, column=1, sticky="NWNESWSE")

        self.but23 = Button(self.master_3,
                            bg=color, text=".",
                            fg=fg_2,
                            font=(font_2, h, style),
                            relief=relief_1,
                            command=lambda: self.appendeTodisplay("."),
                            borderwidth=borderwidth_1)
        self.but23.grid(row=11, column=2, sticky="NWNESWSE")

        self.but24 = Button(self.master_3,
                            bg=color,
                            text="=",
                            fg=fg_2,
                            font=(font_2, h, style),
                            relief=relief_1,
                            command=lambda: self.CalculateExpression(),
                            borderwidth=borderwidth_1)
        self.but24.grid(row=11, column=3, sticky="NWNESWSE")

        self.label = Label(self.master_3, text="", bg='#b5b5b5')
        self.label.grid(row=0, column=0, sticky="NWNESWSE", columnspan=4)


    def Offbuttom(self):
        self.display.delete(0, END)
        self.display.insert(0, "")
        # self.but1.config(state = DISABLED)
        # self.but2.config(state = DISABLED)
        self.but3.config(state=DISABLED)
        self.but4.config(state=DISABLED)
        self.but5.config(state=DISABLED)
        self.but6.config(state=DISABLED)
        self.but7.config(state=DISABLED)
        self.but8.config(state=DISABLED)
        self.but9.config(state=DISABLED)
        self.but10.config(state=DISABLED)
        self.but11.config(state=DISABLED)
        self.but12.config(state=DISABLED)
        self.but13.config(state=DISABLED)
        self.but14.config(state=DISABLED)
        self.but15.config(state=DISABLED)
        self.but16.config(state=DISABLED)
        self.but17.config(state=DISABLED)
        self.but18.config(state=DISABLED)
        self.but19.config(state=DISABLED)
        self.but20.config(state=DISABLED)
        self.but21.config(state=DISABLED)
        self.but22.config(state=DISABLED)
        self.but23.config(state=DISABLED)
        self.but24.config(state=DISABLED)

    def Onbuttom(self):
        self.display.insert(0, "0")
        # self.but1.config(state = NORMAL)
        # self.but2.config(state = NORMAL)
        self.but3.config(state=NORMAL)
        self.but4.config(state=NORMAL)
        self.but5.config(state=NORMAL)
        self.but6.config(state=NORMAL)
        self.but7.config(state=NORMAL)
        self.but8.config(state=NORMAL)
        self.but9.config(state=NORMAL)
        self.but10.config(state=NORMAL)
        self.but11.config(state=NORMAL)
        self.but12.config(state=NORMAL)
        self.but13.config(state=NORMAL)
        self.but14.config(state=NORMAL)
        self.but15.config(state=NORMAL)
        self.but16.config(state=NORMAL)
        self.but17.config(state=NORMAL)
        self.but18.config(state=NORMAL)
        self.but19.config(state=NORMAL)
        self.but20.config(state=NORMAL)
        self.but21.config(state=NORMAL)
        self.but22.config(state=NORMAL)
        self.but23.config(state=NORMAL)
        self.but24.config(state=NORMAL)

    def Rbutton(self):
        # self.display.delete(0,END)
        # self.display.configure(justify=LEFT)
        self.display.delete(0, 1)

    def replaceText(self, text):
        self.display.delete(0, END)
        self.display.insert(0, text)

    def appendeTodisplay(self, text):
        self.EntryText = self.display.get()
        self.textLength = len(self.EntryText)

        if self.EntryText == "0":
            self.replaceText(text)

        else:
            self.display.insert(self.textLength, text)

    def clearText(self):
        self.replaceText("0")

    def CalculateExpression(self):
        self.expression = self.display.get()
        self.expression = self.expression.replace("%",
                                                  "/100")  # we have to replace all the %/100 so that typton will not considere it as modulo.
        self.result = eval(self.expression)
        # self.replaceText(self.result)# this will put the result on the screen

        try:
            self.result = eval(self.expression)
            self.replaceText(self.result)

        except:
            messagebox.showinfo("Error", "Invalid Input")

        # print(self.result)# it will print the result on the consel when we press equal for verification

    def pi(self):
        self.result = False
        self.current = math.pi
        self.displad(self.current)

       # Sign out button function

    def iExit_2(self):
        self.qExit = messagebox.askyesno("Calculator",
                                         "Are you sure that you want to close?",
                                         icon="warning")
        if self.qExit > 0:
            self.master_3.destroy()
            return

#==============================================================================================
# Classes for different windows
class PatientsRegistration:
    def __init__(self, master):
        self.master = master
        self.master.title("Patients Registration Systems")


class HospitalRegistration:
    def __init__(self, master):
        self.master = master
        self.master.title("Hospital Registration Systems")

class Calculator:
    def __init__(self, master):
        self.master = master
        self.master.title("Calculator")

#==============================================================================================
def main ():
    root = Tk()
    app = window1(root)
    root.mainloop()

if __name__ == '__main__':  main()

