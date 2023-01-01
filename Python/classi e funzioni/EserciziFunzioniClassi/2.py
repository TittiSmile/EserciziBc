"""
Creare una classe Operazioni
che contiene
i seguenti metodi:
a. somma
b. sottrazione
c. divisione
d. moltiplicazione
e. teoremaPitagora , per calcolare l’ipotenusa
 i= rad(  c1^2  + c2^2)
"""

import math

class Operazioni():
    def somma(self, a, b):
        print("somma: ", a+b)
    def sottrazione(self, a, b):
        print("sottrazione: ", a - b)
    def divisione(self, a, b):
        print("divisione: ", a / b)
    def moltiplicazione(self, a, b):
        print("moltiplicazione: ", a * b)
    def teoremaPitagora(self, a, b, c):
        ipotenusa = 0
        if a > b + c:
            ipotenusa = math.sqrt((b**2)+(c**2))
        elif b > a+c:
            ipotenusa = math.sqrt((a**2)+(c**2))
        else:
            ipotenusa = math.sqrt((a ** 2) + (b ** 2))
        print("terorema di Pitagora: ", ipotenusa)



o = Operazioni()
o.somma(1,2)
o.sottrazione(5,2)
o.divisione(10,2)
o.moltiplicazione(2,2)
o.teoremaPitagora(16, 2, 2)


# vedi come fare a far prendere numeri da tastiera e salvarli da qualche parte....
"""dim = int(input("quanti numeri vuoi inserire? "))
i = 0
while i < dim:
    a = input()"""


