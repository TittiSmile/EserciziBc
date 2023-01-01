
"""Utilizzando il modulo Tkinten si crei una nuova classe
Finestra.
Si crei il widget di primo livello nella gerarchia di widget.
Si imposti il titolo della finestra che verrà visualizzata a
video.
Si imposti la dimensione della finestra in modo che non sia
possibile ridimensionarla e si eviti che il frame si
ridimensioni attorno alla label.
Il from deve contenere 3 frame:
• Due pulsanti.
• Un’immagine.
• Una barra di descrizione"""
# continua.....

import tkinter as tk
from tkinter import *

class Finestra():
    root = Tk()
    root.title("titolo finestra")
    # root.resizable(False, False) # per non ridimensionare la finestra

    #larghezza, lunghezza, dimensione bordo
    frame1 = tk.Frame(root, width="400", height="40", bd="1")
    frame2 = tk.Frame(root, width="300", height="30", bd="1")
    frame3 = tk.Frame(root, width="200", height="20", bd="1")
    button1 = tk.Button(root)
    button2 = tk.Button(root)
    button1.configure(text="bottone1")
    button2.configure(text="bottone2")

    button1.pack()

    img = tk.PhotoImage(file="Rio.jpg")
    root.mainloop()


Finestra()