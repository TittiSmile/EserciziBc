# funziona pari pari al try catch solo che c'è except invece di catch

a = int(input("inserisci un numero a:  "))
b = int(input("inserisci un numero b:  "))
try:                    # prova a fare questa porzione di codice. se qualcosa non va, va nell'except
    d = a/b     # il try va a verificare se effettivamente qui ci sono dei problemi
    print(d)
except:     # se non avessi messo try except COMUNQUE avrebbe dichiarato errore dal compilatore
    print("errore")
# posso avere più except