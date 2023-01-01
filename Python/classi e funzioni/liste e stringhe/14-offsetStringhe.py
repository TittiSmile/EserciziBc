# gli offset stanno anche per le stringhe. [start:stop:step]
s = "comeStaiFratOkVaBene"
s2 = "ciao"
print(s[2:6:2]) # inizia dal carattere di pos 2 (ricorda che si parte da 0).
                # finisce a 6 (non compreso) e va di 2 in 2
print(s[:-3])   # stampa tutta la stringa e finisce al terzultimo carattere
print(s[:17])   # in maniera analoga a sopra
# le stringhe (ma anche le liste) se vai a farci -x non va in errore ma fa il giro dietro :D
print(s[-1:])   # inizia da -1 (e) e finisce là. lo stop non c'è
print(s[1])     # solo start. stampa il primo carattere (cioè o)
print(s[0:1])   # inizio e fine. stampa c. perchè parto dall'elemento di posizione 0 e finisco all'elemento 1-1 non compreso
print(s[0:3])




"""
posso avere:
[start:stop:step]    inizio-finisco-salti
[start]              inizio senza fine (quindi inizia e finisce là)
[start:stop]         inizio e finisco. stop finisce con x-1
 


"""