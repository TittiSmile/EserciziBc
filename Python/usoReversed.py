# il metodo reversed stampa al contrario la liste o quel che è

l = [1, 2, 3]
l2 = [5, 1, 67]

for i in reversed(l):
    print(i)

print("*******")
for i in reversed(l2):  # ricorda che è buona norma dichiarare indici di nomi DIVERSI!!!
    print(i)


print("*******")
print(i)    # dà warning. salva l'ultimo valore calcolato nel ciclo.




