a = int(input("inserisci valore 1: "))
b = int(input("inserisci valore 2: "))

print(a,b)
if a == b:
    print(a," uguale a ",b)
elif a == 5:
    print(a, " è esattamente 5")
else :
    print(a, b, " sono diversi ")


# RICORDA!!!!! l'esempio è semplice ma in generale, se stai confrontando degli interi da tastiera, è buona norma
# mettere un cast ad int/float/ eval. questo perchè, altrimenti, i confronti con dati immessi da tastiera possono
# essere sbagliati!! ricorda che input, normalmente, salva i dati come STRINGHE

# esempio esplicativo del concetto:

"""x = input("inserisci valore 1: ")
y = input("inserisci valore 2: ")

print(x,y)

if x < y:
    print(x, " è minore di ", y)
elif x == 5:
    print(x, " è esattamente 5")
else :
    print(x, " è maggiore di ", y)"""

# qui i risultati saranno sballati. non entrerà mai nella condizione x=5 e non funzionerà a dovere.

# chiaramente, se impostiamo i valori x y noi (manualmente) e li poniamo uguali ad un intero, non c'è nessun problema