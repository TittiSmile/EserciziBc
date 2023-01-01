# uso di while col break

i = 10
while i:        # equivale ad un while True (i è sempre vera).
    val = int(input("inserisci valore:"))
    if val == 4:
        break
    print(i)
