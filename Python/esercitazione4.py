"""
Come il precedente (esercitazione3) ma escludendo i multipli di 3 e
scambiando in automatico i valori di A e B nel caso B fosse
minore di A
"""

a = int(input("inserisci un numero a: "))
b = int(input("inserisci un numero b: "))
if a > b:
    for i in range(b, a + 1):
        if i % 3 == 0:
            print(i)
else:                       # se metto elif b > a non funge. probabilmente perchè si aspetta un else?
    for j in range(a, b + 1):
        if j % 3 == 0:
            print(j)
