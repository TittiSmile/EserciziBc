"""
Scrivere una classe
Lista che contenga al suo interno un metodo , nel quale si dichiari una lista di interi
l=[16,32,13,24,95] e si calcoli la media dei valori contenuti nella lista e si
stampino il tutto a schermo
"""

class myList():
    var = 10
    def mediaLista(self):
        lista = [16, 32, 13, 24, 95]
        somma = 0
        media = 0.0
        i = 0
        while i < len(lista):
            somma += lista[i]
            media = somma/len(lista)
            i+=1
        print("la media è: ", media)

# mi dà problemi col for!!!! dice che esco fuori dalla dimensione della lista
"""
        for i in lista:     
            somma+=lista[i]
            media = somma/len(l)
"""

# creo oggetto di myList
obj = myList()
# richiamo la funzione mediaLista
obj.mediaLista()
