import sqlite3
import sys
db = sqlite3.connect("test.db")
print("apro il db")
db.execute('''CREATE TABLE studente                         
            (name text, cognome text, codice int);''')  # funziona come sql in basi di dati. text = varchar
db.commit()

print("tabella creata")
db.close()