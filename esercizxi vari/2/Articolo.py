class Articolo():
    descrizione = ""
    pezzi = 0
    def __init__(self, descrizione, pezzi):
        self.descrizione = descrizione
        self.pezzi = pezzi
    def numeroPezzi(self):
        # print("il numero di pezzi è: ", self.pezzi)
        return self.pezzi
    def descrizionePezzi(self):
        #print("la descrizione degli oggetti è: ", self.descrizione)
        return self.descrizione
    def aumenta(self, n):
        if n > 0:
            self.pezzi+=n
            return True
        else:
            return False
    def diminuisci(self, n):
        if n > 0:
            self.pezzi -= n
            return True
        else:
            return False


pezzi = 10
descrizione = "pennarello"
a = Articolo(descrizione, pezzi)