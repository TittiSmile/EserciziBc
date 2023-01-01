
"""
Scrivere del codice in Python per calcolare la radice
quadrata di un numero intero positivo, inserito da
tastiera. Il codice deve gestire anche un caso di errore, cioè viene
inserito un valore non intero.
"""

import math

numero = eval(input("inserisci un numero intero: "))
numeroFloat = isinstance(numero,float)

try:
    if numeroFloat == True:
        print("hai inserito un float")
    else:
        radiceQuadrata = math.sqrt(numero)
        print("la radice di", numero, "è: ", radiceQuadrata)

except:
    print("hai inserito un numero negativo!!!")
