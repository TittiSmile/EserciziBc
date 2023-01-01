# Si considerino 3 numeri inseriti dall’utente e si stampi il maggiore.
a = eval(input("inserisci numero 1: "))
b = eval(input("inserisci numero 2: "))
c = eval(input("inserisci numero 3: "))

# provo una soluzione diversa da quella proposta (più complicata eheh)

if a >= b and a >= c:
    print(a, " è il valore più grande")
elif b >= a and b >= c:
    print(b, " è il valore più grande")
elif c >= a and c >= b:
    print(c, " è il valore più grande")
