# esempio di come, le chiamate alle funzioni, non modificano la variabile

def funz(x):
    return x*x

x=eval(input("inserisci un numero x: "))
print("il doppio di x è: ", funz(x))
print("valore di x: ", x)
x=10
print("cambio il valore di x: ",x)

# questo perchè x, per come è fatto, è immutabile (a meno che non lo cambio io volontariamente, riga 9)