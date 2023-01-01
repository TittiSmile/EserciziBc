
"""
Si crei una nuova lista mylist, e si inizializzi con i valori 1 2 3 4 e 5.
Usando la notazione degli slice per estrarre i primi due elementi della lista mylist.
Allo stesso modo estrai gli elementi alla posizione 2 e 3.
Inserisci il valore 6 come elemento alla posizione 2 senza sostituire gli elementi presenti.
Accoda alla lista il valore intero 10.
Infine elimina dalla lista il valore contenuto alla quarta posizione.
"""

myList = [1, 2, 3, 4, 5]
print("primi 2 elementi: ", myList[:2]) # prende gli elmenti 0 e 1 (tutti quelli fino alla pos 2, 2 NON compreso)
print("posizione 2 e 3: ", myList[1:3]) # parte da elemento pos 2 e finisce ad elemento pos 3 (3 non compreso)
myList.insert(2,6)
print("aggiungo elemento 6 in posizione 2: ", myList)
myList.append(10)
print("inserisco in coda il valore 10: ", myList)
del myList[4]
print("elimino elemento di posizione 4", myList)