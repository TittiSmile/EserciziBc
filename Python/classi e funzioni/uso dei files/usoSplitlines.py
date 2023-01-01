# splitlines elimina gli spazi. si usa nei contesti di readlines (quindi lista per roba letta da file)

file = open("text1.txt", "r")
for riga in file:   # sto scorrendo il file utilizzando un iteratore (riga)
    print(riga.splitlines())    # mi stampa liste in base a ciò che trova sulle righe
file.close()





print("\n*****\n")
lista = []      # gli associo direttamente la lista
file2 = open("text1.txt", "r")
for riga in file2:
    riga = riga.splitlines()
    lista.append(riga)
file2.close()

print(lista)