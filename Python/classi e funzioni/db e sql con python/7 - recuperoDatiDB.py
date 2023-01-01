import sqlite3

db = sqlite3.connect("test.db")
print("apro il db senza problemi")
print("adesso recupero i dati dal db...")

cur = db.execute("SELECT name, cognome FROM studente")
for row in cur:
    print("nome: ", row[0])             # la stampa di tutti i nomi
    print("\t\tcognome: ", row[1])      #  la stampa dei cognomi
    # le row sono considerate come le colonne della tabella con nome cognome codice... 

db.close()