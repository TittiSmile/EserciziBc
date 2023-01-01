#anche in python ci sono le funzioni lambda
# invece di scrivere tutta la funzione, si scrive tutto in un unico rigo

def funz(a,b):
    return a+b

funz2 = lambda a,b : a+b

print(funz(1,2))
print(funz2(3,4))