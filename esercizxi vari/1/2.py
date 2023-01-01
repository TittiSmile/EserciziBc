"""
Un particolare rivenditore ha uno sconto del 60% su una varietà di prodotti fuori
produzione. Il rivenditore desidera aiutare i propri clienti a determinare il prezzo ridotto
della merce disponendo di una tabella di sconti stampata sullo scaffale che mostra i prezzi
originali e i prezzi dopo l'applicazione dello sconto. Scrivi un programma che utilizzi un ciclo
per generare questa tabella, che mostri il prezzo originale, l'importo dello sconto e il nuovo
prezzo per acquisti di € 4,95, € 9,95, € 14,95, € 19,95 e € 24,9
"""

sconto = 60/100
listaPrezzi = [4.95, 9.95, 14.95, 19.95, 24.95]
i = 0
dimensioneLista = len(listaPrezzi)
while i < dimensioneLista:
    nuovoPrezzo = sconto * listaPrezzi[i]
    print("\nprezzo originale: ", listaPrezzi[i],
          "\tsconto applicabile: ", sconto,
          "\tnuovo prezzo: ", nuovoPrezzo)
    i+=1
