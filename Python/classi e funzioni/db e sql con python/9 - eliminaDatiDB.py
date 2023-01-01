import sqlite3

db = sqlite3.connect("test.db")
print("apro il db senza problemi")
print("adesso elimino i dati dal db...")

db.execute("delete from studente where codice = 15 ")
db.commit()
print("righe eliminate: ", db.total_changes)
cur = db.execute("SELECT name, cognome, codice FROM studente")
for row in cur:
    print("nome: ", row[0])
    print("\t\tcognome: ", row[1])
    print("\t\t\tcodice: ",row[2])
db.close()