import tkinter
from tkinter import *

root = Tk()
widget = Button(None, text="clicca qua", command=root.quit)
widget.pack()
widget.mainloop()   # va bene anche se ci metto root