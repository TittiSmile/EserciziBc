import sqlite3


nome = "Piero"
codice = 6
db = sqlite3.connect("test.db")
print("apro il db senza problemi")
with db:
    cur = db.cursor()
    cur.execute("UPDATE studente set name=? where codice=?", (nome,codice))    # cambio nome da paolo a piero
db.commit()
print("righe aggiornate: ", db.total_changes)
#stampo quello che ho aggiornato
cur = db.execute("SELECT name, cognome, codice FROM studente")
for row in cur:
    print("nome: ", row[0])
    print("\t\tcognome: ", row[1])
    print("\t\t\tcodice: ",row[2])
db.close()