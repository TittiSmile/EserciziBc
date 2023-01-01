import sqlite3

db = sqlite3.connect("test.db")
print("apro il db senza problemi")
print("adesso popolo il db...")

db.execute("INSERT INTO studente(name, cognome, codice) VALUES ( 'mario', 'rossi', 5)")
db.execute("INSERT INTO studente(name, cognome, codice) VALUES ( 'luca', 'verdi', 15)")
db.execute("INSERT INTO studente(name, cognome, codice) VALUES ( 'paolo', 'bianchi', 6)")
db.execute("INSERT INTO studente(name, cognome, codice) VALUES ( 'filippo', 'nerii', 9)")
db.commit()
print("\npopolazione avvenuta con successo")
db.close()