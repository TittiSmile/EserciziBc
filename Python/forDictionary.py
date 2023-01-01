# uso di for in un dizionario (sarebbe una Map in Java...)

# stampa del dizionario con indice
dic = {1: "ciao", 2: "come", 3: "stai?"}
for i in dic:
    print(i)    # se facessi print(dic)  mi stamperebbe il dizionario così com'è.

print("*****")
# stampa dei valori tramite for.
for j in dic.values():  # vado a contare j come contatore dei valori!
    print(j)

print("*****")
# stampa delle chiavi (così come il 1 caso) del dizionario
for h in dic.keys():    # come con i. qui mi ritorna tutte le key di h. di default, quindi, dic.keys e dic prendono
                        # le stesse cose (cioè stampano le keys)
    print(h)

print("*****")
# stampa delle coppie chiave - valore attraverso il ciclo
for k in dic.items():
    print(k)
