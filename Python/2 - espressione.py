import math

a = eval(input("inserisci numero: "))
b = eval(input("inserisci numero: "))
if b <= 0:
    print("impossibile fare la divisione")
divisione = a/b
x = math.sqrt(divisione)            # quando si usano le funzioni di math, bisogna usare chiaramente math.funzione()
print("la radice quadrata di ", a , "/", b, "è : ",x)