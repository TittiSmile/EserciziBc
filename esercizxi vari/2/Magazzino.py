import ast
import math

from Articolo import *
class Magazzino():
    elemento = a.descrizionePezzi()
    capacity = 0
    listaArticoli = [elemento]
    def __init__(self, capacity):
        self.__capacity = capacity
    def articoloPerCodice(self,codice):
        try:
            return self.listaArticoli[codice]
        except:
            print("errore, indice non presente")
    def pezziDescrizione(self, codice, numPezzi, descPezzi):
       if codice < len(self.listaArticoli):
           print("codice: ", codice, "\ndescrizione: ", descPezzi, "\npezzi: ", numPezzi)
       else:
           print("indice non valido")
    def nuovoArticolo(self, articolo):
        self.listaArticoli.append(articolo)
    def entraArticolo(self, pezzi, codice):
        try:
            if pezzi > 0 and codice < len(self.listaArticoli):
                aumentoPezzi = a.aumenta(pezzi)
                return aumentoPezzi
            else:
                raise
        except:
            print("pezzi negativi o codice inesistente")
    def esceArticolo(self, pezzi, codice):
        try:
            if pezzi > 0 and codice < len(self.listaArticoli) and pezzi < a.numeroPezzi():
                diminuisciPezzi = a.diminuisci(pezzi)
                return diminuisciPezzi
            else:
                raise
        except:
            print("pezzi negativi o codice inesistente o numero di pezzi da sottrarre incompatibile")
    def scaricaArticolo(self, codice):
        print(a.numeroPezzi())
        try:
            if a.numeroPezzi() > 0:
                self.listaArticoli.remove(self.listaArticoli[codice])
            else:
                raise
        except Exception as e:
                print(e)

    def stampaArticolo(self):
        print("stampo lista articoli: ", self.listaArticoli)





m = Magazzino(3)
numPezzi = a.numeroPezzi()
descPezzi = a.descrizionePezzi()

