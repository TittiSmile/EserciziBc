import tkinter as tk
from tkinter import *

def somma():
    print("la somma tra i due numeri è: ", 1+2)

root = tk.Tk()
widget = Label(text="clicca per somma o esci")
widget.pack(side=TOP)
button = tk.Button(text="somma", command = somma())
button.pack(side=RIGHT)
button = tk.Button(text="esci", command = root.destroy)
button.pack(side=LEFT)

root.mainloop()


# versione alternativa
"""root = tk.Tk()
Label (text= "clicca per somma o esci").pack(side=TOP)
button = tk.Button(text="esci", command = root.destroy).pack(side=RIGHT)
button = tk.Button(text="somma", command = somma()).pack(side=LEFT)
root.mainloop()"""