"""1. Si crei un piccolo file txt, contenete 10 parole:
leone – zebra – tigre – gatto – cane – criceto – asino – cavallo – mucca – topo.
Aperto il file bisogna inserire in una lista le parole con indice pari, e nell’altra lista le parole con
indice dispari. Infine si stampi il contenute delle due liste separatamente"""

# SCRITTURA SU FILE
file = open("esercizio1.txt", "w")
file.write("leone\nzebra\ntigre\ngatto\ncane\ncriceto\nasino\ncavallo\nmucca\ntopo")
file.close()



listaPari = []
listaDispari = []
# LETTURA SU FILE
"""file = open("esercizio1.txt", "r")
for i in file:
    i = i.splitlines()
    lista.append(i)
file.close()"""
lista = open("esercizio1.txt", "r").readlines() # per creare la lista dal file di testo


i = 0
# CREAZIONE LISTE PARI E DISPARI
while i < len(lista):
    if i % 2 == 0 :
        listaPari.append(lista[i])
    else:
        listaDispari.append(lista[i])
    i+=1

print("lista con le parole del file:\n", lista)
print("******")
print("lista con le parole di indice pari:\n", listaPari)
print("******")
print("lista con le parole di indice dispari:\n",listaDispari)


