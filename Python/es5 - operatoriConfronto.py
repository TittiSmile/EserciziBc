"""
gli operatori di confronto in python sono sia quelli bit a bit (bitwise) che quelli logici (and, or, not)
chiarmente svolgono 2 ruoli diversi.
operatori di confronto: <, >, !=, ==, ...
operatori relazionali: and, or, not
operatori bitwise: &, |             questi qui agiscono solo sui bit dell'oggetto.
la dichiarazione di un oggetto è sempre VERA
"""

a = 10
b = 4
if a and b:     # se avessi messo a and b == True sarebbe stato falso perchè True è booleano e sono dei numeri interi...
    print("vero")
else:
    print("falso")

if (not(a and b)):
    # sto negando sia a che b. RICORDA che se non avessi messo la parentesi davanti al not,
    # lo avrebbe considerato come if not (statement diverso) credo...?
    print("vero")
else:
    print("falso")