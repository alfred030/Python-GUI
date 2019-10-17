
import tkinter.messagebox
import tkinter.messagebox as tmb
tmb.showinfo(title="Show Info", message="This is FYI")
tmb.showwarning(title="Show Warning", message="Don't be silly")
tmb.showerror(title="Show Error", message="It leaked")
tmb.askquestion(title="Ask Question", message="Can you read this?")
tmb.askokcancel(title="Ask OK Cancel", message="Say Ok or Cancel?")
tmb.askyesno(title="Ask Yes-No", message="Say yes or no?")
tmb.askyesnocancel(title="Yes-No-Cancel", message="Say yes nocancel")
tmb.askretrycancel(title="Ask Retry Cancel", message="Retry orwhat?")

def display_about_messagebox(event=None):
    tkinter.messagebox.showinfo("About", "{}{}".format(PROGRAM_NAME, "\nTkinter GUI Application\n Development Blueprints"))
def display_help_messagebox(event=None):
    tkinter.messagebox.showinfo("Help", "Help Book: \nTkinter GUI Application\n Development Blueprints", icon='question')

about_menu.add_command(label='About',command=display_about_messagebox)
about_menu.add_command(label='Help', command=display_help_messagebox)
