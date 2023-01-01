"""
1 - Stampa solo la colonna Colore
2 - Associa in automatico valori al colore
3 - Stampare il tutto
4 - Si applichi il metodo one hot encoding sulla colonna che contiene le variabili categoriali.
5 - Si crei una nuova colonna e si applichi il metodo dummy alla colonna del colore, con prefisso
    colore.
6 - Ristampare il tutto"""

import sqlite3
import sys
db = sqlite3.connect("test.db")

db.execute("INSERT INTO Tabella (Prodotto, Azienda, Quantità, Colore) VALUES ( 'Penna', 'Bic', 10, 'Blu')")
db.execute("INSERT INTO Tabella (Prodotto, Azienda, Quantità, Colore) VALUES ( 'Penna', 'Bic', 15, 'Nera')")
db.execute("INSERT INTO Tabella (Prodotto, Azienda, Quantità, Colore) VALUES ( 'Penna', 'Bic', 30, 'Rossa')")

print("stampo tutto\n")
cur = db.execute("SELECT * FROM Tabella")
print(cur.fetchall())

print("*****")
# PUNTO 1
cur2 = db.execute("Select Colore From Tabella")
for i in cur2:
    print("colore: ", i[0])

# PUNTO 2










db.close()






""""
db.execute('''CREATE TABLE Tabella                        
            (Prodotto text, Azienda text, Quantità int, Colore text);''')
db.commit()

db.execute("INSERT INTO Tabella (Prodotto, Azienda, Quantità, Colore) VALUES ( 'Penna', 'Bic', 10, 'Blu')")
db.execute("INSERT INTO Tabella (Prodotto, Azienda, Quantità, Colore) VALUES ( 'Penna', 'Bic', 15, 'Nera')")
db.execute("INSERT INTO Tabella (Prodotto, Azienda, Quantità, Colore) VALUES ( 'Penna', 'Bic', 30, 'Rossa')")




cur = db.execute("SELECT * FROM Tabella")
print(cur.fetchall())

"""