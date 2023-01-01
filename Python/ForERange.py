# uso di for con la funzione range (già vista con rand)
# range ritorna un oggetto iterabile con una sequenza di numeri progressivi.
# composto da: range(start, stop, step).
# start -> obbligatorio e parte da 0
# stop -> facoltativo (RICORDA che si ferma sempre alla lunghezza -1)
# step -> facoltativo e di default è 1
# non è necessario dichiarare un iterabile se si usa range. si tratta di lavorare con numeri interi

for i in range(10, 15, 2):  # stampa i pari da 10 a 15.
    print(i)

print("*****************")
for j in range (10, 15):
    print(j)            # si ferma a 14 perchè stop farà 15-1 = 14 (regola dello scarto di 1)

print("*****************")
for h in range(5):
    print(h)         # stamperà di default i valori che vanno da 0 a 4. ricorda che l'indice parte sempre da 0
                     # ricorda in parte come funzionano gli array che hanno indici da 0 a n-1 dove n è la lunghezza

print("*****************")
for k in range(10,16):      # così posso stampare 15 senza problemi
    print(k)

print("*****************")
q=2         # a quanto pare è legittimo farlo... ma è inutile ai fini del for sottostante!
for q in range(5):
    print(q)


"""
a quanto pare anche se imposto q fuori dal for, mi considererà sempre la variabile locale. 
questa cosa è super wtf
anche perchè in altri linguaggi (come java ma anche c) se utilizzo un nome per una variabile, non posso in nessun
modo dichiararmene una con lo stesso nome che fa cose diverse o.o
tutto ciò è assurdo lol

considera che tutti gli indici dichiarati finora (i, j, k....) sono dichiarati localmente al for. quindi vengono
utilizzati nel for e A QUANTO PARE possono essere richiamate anche da fuori lol. 
"""
""" ricorda che il for in python prende i e cicla su un iterabile... fare for i < 10 è sbagliato perchè 10 non è  un iterabile!!! """



print("*****************")
print(i)
"""
a differenza di Java (o C). la variabile i non viene eletta a garbage collection. è possibile stamparla anche 
al di fuori del suo ciclo for e, di conseguenza, avrà come valore l'ultimo valore preso dal range (14). 
in java questa cosa è illegale :D questo perchè la i viene allocata localmente al for e NON ha nessun uso al di fuori
del for stesso.
l'unica cosa che fa python è segnalarti un warning... gg
"""


"""
in range:
    se c'è start e stop, l'indice parte da start e finisce a stop-1
    se c'è start senza stop, l'indice parte da 0 (anche se l'ho inizializzato a millemila) e finisce a start
    range con 1 solo parametro lo considera come start. 
    range(5) si aspetta che prima ci sia un indice che indirettamente parte a 0.
"""
