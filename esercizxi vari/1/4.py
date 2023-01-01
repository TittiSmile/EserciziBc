"""
In una particolare giurisdizione, le tariffe dei taxi consistono in una tariffa base di € 4,00,
più € 0,25 per ogni 140 metri percorsi. Scrivi una funzione che prenda la distanza percorsa
(in chilometri) come unico parametro e restituisca come unico risultato la tariffa totale.
Scrivi un programma principale che dimostri la funzione
"""
tariffaBase = 4
#tariffaExtra = 0.25    # se me la dichiaro fuori dalla funzione mi dà problemi...
chilometriPercorsi = 0.14
metriPercorsi = 140
limiteMaxKm = 100



def prezzoCorsa(distanzaPercorsa):
    tariffaExtra = 0.25
    tariffaTotale = 0
    i = 0
    cont = 2
    fascia = 0
    j = 1
    if (distanzaPercorsa <= chilometriPercorsi):
        tariffaTotale = tariffaBase
    elif (distanzaPercorsa > chilometriPercorsi):
        while i < distanzaPercorsa:
            print("sono nel while")
            print("chilometri: ", chilometriPercorsi + 0.01)    # non capisco perchè mi scrive 0.15000000000000002
            if distanzaPercorsa >= chilometriPercorsi+0.01:
            #if distanzaPercorsa <= chilometriPercorsi * cont:
                print("sono nell'if")
            i+=1
            j+=1


    return tariffaTotale




percorso = float(input("quanto hai percorso? (inserire la distanza in KM, massimo 100) "))
print("la tariffa totale è: ", prezzoCorsa(percorso))





""" if distanzaPercorsa <= chilometriPercorsi * cont and distanzaPercorsa >= chilometriPercorsi+1:
              tariffaExtra = tariffaExtra * j
              tariffaTotale = tariffaBase + tariffaExtra"""




"""
           print("distanza: ", distanzaPercorsa+0.01)
            print("chilometri: ", chilometriPercorsi + 0.01)"""






"""def prezzoCorsa(distanzaPercorsa):
    tariffaTotale = 0
    if distanzaPercorsa <= metriPercorsi:
        tariffaTotale = tariffaBase"""
