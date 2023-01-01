import sqlite3
import sys
db = None

try:
    db = sqlite3.connect("test2.db")    # se non esiste il db, ne crea uno ad hoc

    cur = db.cursor()
    cur.execute("SELECT SQLITE_VERSION()")
    data = cur.fetchone()
    print("SQLite version: ", data)
except:
    print("errore")
finally:
    if db:
        db.close()