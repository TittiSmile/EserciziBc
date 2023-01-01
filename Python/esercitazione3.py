"""Inseriti due interi da tastiera, a e b, si stampino tutti i
numeri nell’intervallo [A,B] (estremi inclusi"""

a = int(input("inserisci un numero a: "))
b = int(input("inserisci un numero b: "))

if a > b:
    for i in range(b, a + 1):
        print(i)
else:                       # se metto elif b > a non funge. probabilmente perchè si aspetta un else?
    for j in range(a, b + 1):
        print(j)