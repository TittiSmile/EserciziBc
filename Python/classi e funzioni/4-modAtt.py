# possiamo notare come non vengono modificati gli attributi
class A:
    x = 10
    y = 4


a = A()
a2 = A()

a.x=77
print(a.x)
print(a2.x)
# notiamo come, nonostante abbia assegnato x il valore 77, alla chiamata di a2 su x, x resterà sempre 10.
# questo perchè la modifica è "interna" alla chiamata a.x
# se un'istanza modifica un attributo, non lo va a cambiare definitivamente
