from Articolo import *
from Magazzino import *


a.aumenta(3)
print("1*******")
print("numero pezzi articolo: ", a.pezzi)

print("2*******")
codice = 0
print("articolo: ", m.articoloPerCodice(codice), "\ncodice: ", codice)
print("3*******")
m.pezziDescrizione(0, numPezzi, descPezzi)
print("4*******")
print("aggiungo un nuovo articolo...")
newArticolo = "gomma"
m.nuovoArticolo(newArticolo)
m.stampaArticolo()
print("5*******")
print("inserisco articoli (torna true o false): ", m.entraArticolo(4, 0))
print("6*******")
print("escono tot numero di articoli: ",m.esceArticolo(2,0))
print(a.numeroPezzi())  # ne diminuisce di 2 per i pennarelli
print("7*******")
print("elimino i pezzi", m.scaricaArticolo(0))
