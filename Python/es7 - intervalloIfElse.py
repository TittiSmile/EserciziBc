# Si scriva un codice che dato un intervallo, ed un numero n,  è interno o esterno all’intervallo.
a = eval(input("definisci limite superiore: "))
b = eval(input("definisci limite inferiore: "))
n = eval(input("definisci un intero n: "))

if a < b:
    print("errore. limite superiore minore limite inferiore")

if n < a and n > b:
    print("valore n nell'intervallo")
elif n == a or n == b:
    print("valore n come limite")
else:
    print("valore n al di fuori dell'intervallo")