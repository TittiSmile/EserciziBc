"""
Scrivi una funzione che prenda le lunghezze dei due lati più corti di un triangolo rettangolo
come suoi parametri. Restituisce l'ipotenusa del triangolo, calcolata utilizzando il teorema
di Pitagora, come risultato della funzione. Includere un programma principale che legge le
lunghezze dei lati più corti di un triangolo rettangolo dall'utente, utilizza la funzione per
calcolare la lunghezza dell'ipotenusa e visualizza il risultato
"""
import math
def teoremaPitagora(cateto1, cateto2):
    ipotenusa = math.sqrt(math.pow(cateto1,2) + math.pow(cateto2,2))
    return ipotenusa

c1 = int(input("dammi il cateto 1: "))
c2 = int(input("dammi il cateto 2: "))
i = teoremaPitagora(c1,c2)
print("l'ipotenusa, dati i cateti, è: ", i)