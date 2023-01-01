"""
Una ruota della roulette ha 38 spazi su di essa. Di questi spazi, 18 sono neri, 18 sono rossi e
due sono verdi. Gli spazi verdi sono numerati con 0 e 00. Gli spazi rossi sono numerati 1, 3,
5, 7, 9, 12, 14, 16, 18, 19, 21, 23, 25, 27, 30 32, 34 e 36. I restanti numeri interi compresi tra
1 e 36 vengono utilizzati per numerare gli spazi neri.
Molte scommesse diverse possono essere piazzate nella roulette. Si consideri solo il seguente sottoinsieme:
• Numero singolo (da 1 a 36, 0 o 00)
• Rosso contro Nero
• Dispari contro Pari (Nota che 0 e 00 non pagano per pari)
•Da 1 a 18 contro 19 a 36
Scrivi un programma che simuli un giro di una ruota della roulette utilizzando il generatore
di numeri casuali di Python. Visualizza il numero selezionato e tutte le scommesse che
devono essere pagate. Ad esempio, se si seleziona 13, il programma dovrebbe visualizzare:
• Il giro ha prodotto 13 ...
• Paga 13
• Paga nero
• Paga dispari
• Paga da 1 a 18
• Se la simulazione risulta 0 o 00, il programma dovrebbe visualizzare
    Paga 0 o Paga 00 senza ogni ulteriore output
"""

import random
rulette = [1, 3, 5, 7, 9, 12, 14, 16, 18, 19, 21, 23, 25, 27, 30, 32, 34, 36,
           2, 4, 6, 8, 10,  11, 13, 15, 17, 20, 22, 24, 26, 28, 29, 31, 33, 35,
           0, 00]
spazioRosso = [1, 3, 5, 7, 9, 12, 14, 16, 18, 19, 21, 23, 25, 27, 30, 32, 34, 36]
spazioNero = [2, 4, 6, 8, 10, 11, 13, 15, 17, 20, 22, 24, 26, 28, 29, 31, 33, 35]
spazioVerde = [0,00]

scelta = input("iniziare la simulazione? s/n ")
if scelta == "s":
    print("giro la ruota...")
    numeroCasuale = random.choice(rulette)
    print("paga ",numeroCasuale)
    if numeroCasuale in spazioNero:
        print("paga nero")
        if numeroCasuale % 2 == 0:
            print("paga pari")
        else:
            print("paga dispari")
        if numeroCasuale >= 1 and numeroCasuale <=18:
            print("paga da 1 a 18")
    elif numeroCasuale in spazioRosso:
        print("paga rosso")
        if numeroCasuale % 2 == 0:
            print("paga pari")
        else:
            print("paga dispari")
        if numeroCasuale >= 1 and numeroCasuale <=18:
            print("paga da 1 a 18")
    elif numeroCasuale in spazioVerde:
        if numeroCasuale == 0 :
            print("paga 0")
        elif  numeroCasuale == 00:
            paga("paga 00")

else:
    print("arrivederci")