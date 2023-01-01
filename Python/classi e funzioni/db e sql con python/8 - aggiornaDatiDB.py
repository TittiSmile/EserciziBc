import sqlite3

db = sqlite3.connect("test.db")
print("apro il db senza problemi")
print("adesso aggiorno i dati dal db...")

db.execute("UPDATE studente set  codice = 1 WHERE name = 'mario' ") # vado a modificare i codici dei tizi che si chiamano mario
db.commit()
print("righe aggiornate: ", db.total_changes)
cur = db.execute("SELECT name, cognome, codice FROM studente")
for row in cur:
    print("nome: ", row[0])
    print("\t\tcognome: ", row[1])
    print("\t\t\tcodice: ",row[2])
db.close()