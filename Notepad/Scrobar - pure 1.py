from tkinter import *
from tkinter import ttk, scrolledtext


class entry:
    def __init__(self, master):
        master.title('Label')
        scroll_W = 35
        scroll_H = 25
        scr = scrolledtext.ScrolledText(master,
                                        font=("Time", 14),
                                        width=scroll_W,
                                        height=scroll_H,
                                        wrap=WORD)
        scr.grid(column=0, sticky='WE', row=0)
        scr.focus()

        message = '''The early computers were limited in their functions. It was the fusion of automatic calculation and programmability that produced the first computers that were recognized in 1837. Charles Babbage in 1837 was the first to introduce and design a fully programmed mechanical computer, his analytical engine. Due to limited finances and inability of resisting tinkering with the design, he could not complete his work and it was later completed by his son Henry Babbage who made it into a simplified version of the analytical engine’s computing unit.


                    The original objective of inventing a computer was to create a fast calculating machine. During the World War II, it became very essential to understand and locate the direction and speed of the enemy weapons. Calculations had to be done accurately and mathematically and without an advanced machine it would not be possible. To defend the enemy , the front line soldiers required firing tables and only a computer could produce such firing tables with speed and accuracy at that time.

                    To produce the technology then, high sums of money and brain power was required. The first computer was produced by the Moore School of Engineering called the ENIAC, on behalf of the US Army which was in 1946. The ENIAC was able to produce the firing tables, by carrying out large number of calculations accurately.

                    Over a period of time computers have evolved and toady with the Artificial Intelligence technology, we use the most advanced kind of computers that have helped man in every sectors of life. At every generations of the computers or in fact during the evolution, each time computers are being launched that are lighter, smaller, speedier and more powerful. The computers have been a dominating factor since the 1970`s and today it has conquered almost all walks of life.'''

        scr.insert(INSERT, 'Thanks for clicking on submit button!\n\n')
        scr.insert(INSERT, message)


root = Tk()
app = entry(root)
root.mainloop()
