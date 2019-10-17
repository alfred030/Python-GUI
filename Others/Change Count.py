

import tkinter
from tkinter import ttk

root = tkinter.Tk()
root.title("Change Counter")

#separator line
ttk.Separator(root).grid(row=2, columnspan=5, sticky="ew")

#Input Integers
dollarCoins = tkinter.IntVar()
halfDollars = tkinter.IntVar()
quarters = tkinter.IntVar()
dimes = tkinter.IntVar()
nickels = tkinter.IntVar()
pennies = tkinter.IntVar()

#Output Floats on right Side
dollarCoinsTotal = tkinter.DoubleVar()
dollarCoinsTotal.set('0.00')
halfDollarTotal = tkinter.DoubleVar()
halfDollarTotal.set('0.00')
quartersTotal = tkinter.DoubleVar()
quartersTotal.set('0.00')
dimesTotal = tkinter.DoubleVar()
dimesTotal.set('0.00')
nickelsTotal = tkinter.DoubleVar()
nickelsTotal.set('0.00')
penniesTotal = tkinter.DoubleVar()
penniesTotal.set('0.00')
allTotal = tkinter.DoubleVar()
allTotal.set('0.00')

#Title Document
titleLabel = tkinter.Label(root, text = "Change Counter", font = "-weight bold")
titleLabel.grid(row=1, column=1, columnspan = 4)

#Define Function for Button
#Format to be a floating point number of 2 decimals
def Totals():
    dollarCoinsTotal.set("{:.2f}".format(float(dollarCoins.get())))
    halfDollarTotal.set("{:.2f}".format(float(halfDollars.get()* 0.50)))
    quartersTotal.set("{:.2f}".format(float(quarters.get()* 0.25)))
    dimesTotal.set("{:.2f}".format(float(dimes.get()* 0.10)))
    nickelsTotal.set("{:.2f}".format(float(nickels.get()* 0.05)))
    penniesTotal.set("{:.2f}".format(float(pennies.get()* 0.01)))
    allTotal.set("{:.2f}".format(float(dollarCoinsTotal.get() + halfDollarTotal.get() + quartersTotal.get() + dimesTotal.get() + nickelsTotal.get() + penniesTotal.get())))

#Input statment for user
titleLabel = tkinter.Label(root, text = "Enter the number of each coin type and hit compute", font="-size 11")
titleLabel.grid(row=3, column=1, columnspan =4)

#Input Labels for Integers
dollarCoinsLabel = tkinter.Label(root, text = "Dollar Coins")
dollarCoinsLabel.grid(row=4, column=1, pady= 5)

dollarCoinsEntry = tkinter.Entry(root, textvariable = dollarCoins)
dollarCoinsEntry.grid(row=4, column=2, pady= 5, padx = 10)

halfDollarsLabel = tkinter.Label(root, text = "Half Dollars")
halfDollarsLabel.grid(row=5, column=1, pady= 5, padx = 10)

halfDollarsEntry = tkinter.Entry(root, textvariable = halfDollars)
halfDollarsEntry.grid(row=5, column=2, pady= 5)

quartersLabel = tkinter.Label(root, text = "Quarters")
quartersLabel.grid(row=6, column=1, pady= 5, padx = 10)

quartersEntry = tkinter.Entry(root, textvariable = quarters)
quartersEntry.grid(row=6, column=2, pady= 5)

dimesLabel = tkinter.Label(root, text = "Dimes")
dimesLabel.grid(row=7, column=1, pady= 5, padx = 10)

dimesEntry = tkinter.Entry(root, textvariable = dimes)
dimesEntry.grid(row=7, column=2, pady= 5)

nickelsLabel = tkinter.Label(root, text = "Nickels")
nickelsLabel.grid(row=8, column=1, pady= 5)

nickelsEntry = tkinter.Entry(root, textvariable = nickels)
nickelsEntry.grid(row=8, column=2, pady= 5, padx = 10)

penniesLabel = tkinter.Label(root, text = "Pennies")
penniesLabel.grid(row=9, column=1, pady= 5, padx = 10)

penniesEntry = tkinter.Entry(root, textvariable = pennies)
penniesEntry.grid(row=9, column=2, pady= 5)

#Output Labels for DoubleVars
dollarCoinsLabelText = tkinter.Label(root, text = "Dollar Coins Value: $")
dollarCoinsLabelText.grid(row=4, column=3, pady= 5, padx = 10)

dollarCoinsLabelValue = tkinter.Label(root, textvariable = dollarCoinsTotal)
dollarCoinsLabelValue.grid(row=4, column=4, pady= 5)

halfDollarLabelText = tkinter.Label(root, text = "Half Dollar Value: $")
halfDollarLabelText.grid(row=5, column=3, pady= 5, padx = 10)

halfDollarLabelValue = tkinter.Label(root, textvariable = halfDollarTotal)
halfDollarLabelValue.grid(row=5, column=4, pady= 5)

quartersLabelText = tkinter.Label(root, text = "Quarters Value: $")
quartersLabelText.grid(row=6, column=3, pady= 5, padx = 10)

quartersLabelValue = tkinter.Label(root, textvariable = quartersTotal)
quartersLabelValue.grid(row=6, column=4, pady= 5)

dimesLabelText = tkinter.Label(root, text = "Dimes Value: $")
dimesLabelText.grid(row=7, column=3, pady= 5, padx = 10)

dimesLabelValue = tkinter.Label(root, textvariable = dimesTotal)
dimesLabelValue.grid(row=7, column=4, pady= 5)

nickelsLabelText = tkinter.Label(root, text = "Nickels Value: $")
nickelsLabelText.grid(row=8, column=3, pady= 5, padx = 10)

nickelsLabelValue = tkinter.Label(root, textvariable = nickelsTotal)
nickelsLabelValue.grid(row=8, column=4, pady= 5)

penniesLabelText = tkinter.Label(root, text = "Pennies Value: $")
penniesLabelText.grid(row=9, column=3, pady= 5, padx = 10)

penniesLabelValue = tkinter.Label(root, textvariable = penniesTotal)
penniesLabelValue.grid(row=9, column=4, pady= 5)

allTotalLabelText = tkinter.Label(root, text = "Total Change Value: $", font="-weight bold -size 10", )
allTotalLabelText.grid(row=10, column=3, pady= 5, padx = 10)

allTotalLabelValue = tkinter.Label(root, textvariable = allTotal)
allTotalLabelValue.grid(row=10, column=4, pady= 5)

#Button to run calculations
calculateButton = tkinter.Button(root, text = "Compute", relief="raised", fg="red", font="-weight bold", command = Totals)
calculateButton.grid(row=10, column=1, columnspan =2, sticky = "EW", padx=5)


root.mainloop()
