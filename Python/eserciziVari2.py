"""
Utilizzando la libreria random si devono generare
numeri casuali interi tra A e B, con a =20 e b=50
calcolando la loro somma finchè , il numero uscito non
sarà esattamente il numero 27 (da non includere nella
somma)
"""
import random
a = 20
b = 50
s = 0
i = 0
while True:
    i = random.randint(20, 50)
    if(i!=27):
        print("valore di i: ", i)
        s += i
    else:
        break
print(s)


# non credo che funzioni...
