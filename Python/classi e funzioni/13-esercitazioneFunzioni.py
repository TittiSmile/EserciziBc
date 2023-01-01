"""
Si definisca una funzione che prende in input due liste l1 e
l2 e ritorna una lista l3.
l3 contiene la differenza delle due liste.
Il parametro l2 deve avere come parametri di default valori
da 1 a 5
"""

def f(l1,l2=[1,2,3,4,5]):
    l3 = []
    for i in l1:
        if not i in l2:
            l3.append(i)
    return l3


l1=[1,5,9,44]
print("differenza tra l1 ed l2: ", f(l1))






"""
#COME SALVO IL VALORE DI UNA LISTA????? CIOè COME SI FA UN COSO DEL GENERE?
dimL1 = int(input("inserisci dimensione l1: "))
i = 0
while i < dimL1:
    l=input("inserisci elemento: ")
    i+=1

print(l)
"""
