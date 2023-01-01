"""Si crei uno script che una volta lanciato da terminale crei un folder, Prova3settimana,
all’interno crei un file txt prova nel quale verranno inserite le seguenti parole:
cane- casa- pane – frutta- cellulare – computer - candela – tv – quadro – gatto.
Ad ogni parola è associato un rispettivo peso, che coincide con la lunghezza della parola.
Una volta creato il file, si converta in un file csv e si trasformi in un DataFrame.
Stampare le prime 2 righe del dataframe.
Utilizzando una delle librerie per i grafici di Python, proiettare un istogramma che rappresenti
la parola e la sua lunghezza."""

import matplotlib.pyplot as plt
import numpy as np
import os
import pandas as pd

folder = os.mkdir("Prova3Settimana")    # per creare la cartella

file = open("esercizio3.txt", "w")
file.write("tabella:\ncane\ncasa\npane\nfrutta\ncellulare\ncomputer\ncandela\ntv\nquadro\ngatto")
file.close()


listaPeso = []
lista = open("esercizio3.txt", "r").readlines() # per creare la lista dal file di testo

i = 0
while i < len(lista):
    listaPeso.append(len(lista[i]))
    i+=1

print(lista)
print(listaPeso)


#converto in dataframe
df = pd.read_csv("esercizio3.txt")
df.to_csv("esercizio3.csv",header=None, sep=" ")

print(df)
print("*****************")
print(df.head(2))
plt.plot(listaPeso)
plt.show()

