"""Utilizzando la libreria Sqlite3
1 - Si crei uno script che effettui la connessione al db Giornalisti e lo si popoli con 5 giornalisti:
    le iniziali da considerare per il cognome sono: B, C; D; R; P.
L’oggetto giornalista è caratterizzato da un campo per il nome, cognome e numero di articoli.
2 - Si stampi il contenuto.
3 - Si aggiorni il numero degli articoli scritti da uno dei giornalisti.
4 - Si elimini il giornalista che ha il cognome che inizi con D.
5 - Si ristampi il tutto."""
import sqlite3
import sys
db = sqlite3.connect("Giornalisti.db")

# PUNTO 1
""""db.execute('''CREATE TABLE Giornalisti                        
            (Nome text, Cognome text, NumeroArticoli int);''')
db.commit()
db.execute("INSERT INTO Giornalisti (Nome, Cognome, NumeroArticoli) VALUES ( 'Paolo', 'Bianchi', 10)")
db.execute("INSERT INTO Giornalisti (Nome, Cognome, NumeroArticoli) VALUES ( 'Maria', 'Chiari', 4)")
db.execute("INSERT INTO Giornalisti (Nome, Cognome, NumeroArticoli) VALUES ( 'Luca', 'Diori', 7)")
db.execute("INSERT INTO Giornalisti (Nome, Cognome, NumeroArticoli) VALUES ( 'Luigi', 'Rossi', 14)")
db.execute("INSERT INTO Giornalisti (Nome, Cognome, NumeroArticoli) VALUES ( 'Sara', 'Pecotti', 2)")"""



# PUNTO 2
cur = db.execute("SELECT * FROM Giornalisti")
print(cur.fetchall())

# PUNTO 3
db.execute("UPDATE Giornalisti set NumeroArticoli = 20 WHERE Nome = 'Sara' ")
db.commit()
print("*****")
print("righe aggiornate: \n", db.total_changes)

# PUNTO 4
print("****")
db.execute("DELETE FROM Giornalisti WHERE Cognome = 'Diori' ")
db.commit()
print("righe eliminate: \n", db.total_changes)

# PUNTO 5
cur2 = db.execute("SELECT * FROM Giornalisti")
print(cur2.fetchall())




db.close()
