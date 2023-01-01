"""
Un triangolo può essere classificato in base alle lunghezze
dei suoi lati come equilatero, isoscele o scaleno. Scrivere un
programma che legga le lunghezze dei tre lati di un
triangolo dall'utente.
Quindi visualizza un messaggio che indica il tipo di triangolo
"""
a = int(input("inserisci lunghezza lato a: "))
b = int(input("inserisci lunghezza lato b: "))
c = int(input("inserisci lunghezza lato c: "))

if a == b and a == c and b == c:
    print("triangolo equilatero")
elif (a==b or a==c) or (b==a or b==c ) or (c==b or c==a ) :
    print("triangolo isoscele")
else:
    print("triangolo scaleno")