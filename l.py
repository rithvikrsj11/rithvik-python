# Simple Digital Clock
# Download font: https://www.dafont.com/ds-digital.font

from tkinter import *
from tkinter.ttk import *
from time import strftime

root = Tk()
root.title("Clock")

def time():
     string = strftime("%I:%M:%S %p")
     label.config(text=string)
     label.after(1000,time)
     
label = Label(root,font=("Baskerville Old Face",240), background = "#009bde", foreground="cyan")
label.pack(anchor="center")
time()

mainloop()