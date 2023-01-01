"""
Si scriva un piccolo programma che:
• Crei una lista contenente i numeri interi pari tra 10 e 25.
•Utilizza un for loop che utilizzi un range tra 10 e 30 e scartare i numeri dispari e contemporaneamente i
 numeri minori di 25.
•È possibile utilizzare il metodo append
"""
l = []
for i in range(10, 31):
    if i % 2 == 0 and i <= 25:
        l.append(i)
print("stampo la lista: ", l)