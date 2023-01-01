import tkinter
from tkinter import *

root = Tk()      # sarebbe la classe di questa libreria
widget = Label(root)
widget.config(text="eeeeeee")   # quello che scrivo nella finestra
widget.pack(side=TOP, expand=YES, fill=BOTH)
root.mainloop()