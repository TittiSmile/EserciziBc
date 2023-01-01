"""
In una particolare giurisdizione, le tariffe dei taxi consistono in una tariffa base di € 4,00,
più € 0,25 per ogni 140 metri percorsi. Scrivi una funzione che prenda la distanza percorsa
(in chilometri) come unico parametro e restituisca come unico risultato la tariffa totale.
Scrivi un programma principale che dimostri la funzione
"""
# Postilla: ho avuto problemi con i float dei chilometri. ho usato i metri. (probabilmente c'è un problema di overflow)


tariffaBase = 4
metriPercorsi = 140



def prezzoCorsa(distanzaPercorsa):
    tariffaExtra = 0.25
    tariffaTotale = 0
    i = 0
    fasciaCorsa = 2
    fasciaTariffa= 1
    if (distanzaPercorsa <= metriPercorsi):
        tariffaTotale = tariffaBase
    elif (distanzaPercorsa > metriPercorsi):
        while i < distanzaPercorsa:
            if distanzaPercorsa >= metriPercorsi+1 and distanzaPercorsa <= metriPercorsi * fasciaCorsa:
                tariffaExtra = tariffaExtra * fasciaTariffa
                tariffaTotale = tariffaBase + tariffaExtra
                break
            i+=1
            fasciaTariffa+=1
            fasciaCorsa+=1


    return tariffaTotale




percorso = float(input("quanto hai percorso? (inserire la distanza in METRI) "))
print("la tariffa totale è: ", prezzoCorsa(percorso))

