import random

print("numeri randomici: ", random.random())    # genera un numero casuale
print("numeri randomici in un intervallo: ",random.randint(10, 15))   # genera un numero casuale da 10 a 15 (compresi)


list1 = [1, 2, 5, 21, 66]
print("viene scelto un numero (randomicamente) dalla lista l: ", random.choice(list1)) # sceglie un numero randomico da l

list2 = ["ciao", "come", 'va', "tutto", 'bene']
print("viene scelto un numero (randomicamente) dalla lista l: ", random.choice(list2)) # sceglie un numero randomico da l

list3 = [1, "ciao", 2, "mondo"] # lista mista
print("ritorna un numero dato un certo range", random.randrange(1,5,2))
"randomrange(start, stop, step)" \
"start -> punto di inizio (compreso)" \
"stop -> punto di fine (non compreso)" \
"step -> step aggiunti al numero per scegliere quello randomico." \
"in questo caso, prendo 1 (salto il 2 perchè c'è step 2), 3 (salto 4 perchè c'è step 2) e salto anche 5 perchè stop non comprende" \
"il valore stesso (quindi salta il 5)"