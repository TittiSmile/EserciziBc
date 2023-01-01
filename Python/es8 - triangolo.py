# Affinché tre numeri possano essere le misure dei lati di un
# triangolo è necessario che siano tutti positivi e che
# ciascuno sia inferiore alla somma degli altri due.

a = eval(input("definisci lato 1: "))
b = eval(input("definisci lato 2: "))
c = eval(input("definisci lato 3: "))

if a < 0 or b < 0 or c < 0:
    print("errore. i lati devono essere tutti positivi")

if a > b + c:
    print(a, "maggiore di b + c. triangolo fallito")
elif b > a + c:
    print(b, "maggiore di a + c. triangolo fallito")
elif c > b + a:
    print(c, "maggiore di b + a. triangolo fallito")
else:
    print("creazione triangolo valida")