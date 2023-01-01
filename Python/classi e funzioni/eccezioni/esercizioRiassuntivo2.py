
"""
Scrivere un programma che legga da tastiera un valore
nell'intervallo [1,12], la cui corrispondenza al numero è
il rispettivo mese e, stampi la stagione relativa al mese
inserito.
Il codice deve cercare di intercettare possibili situazioni di
errore dovute a input fuori dall’intervallo predefinito
"""
intervallo = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
mese = int(input("inserisci un mese (da 1 a 12): "))
try:
    if mese == 1 or mese == 2 or mese == 12:
        print("inverno")
    elif mese >= 3 and mese <=5:
        print("primavera")
    elif mese >= 6 and mese <= 8:
        print("estate")
    elif mese >=9 and mese <= 11:
        print("autunno")
    else:  # se non valgono tutte le casistiche precedenti, lancia un'eccezione che verrà catturata in except
        raise
except:
    print("mese fuori dall'intervallo")