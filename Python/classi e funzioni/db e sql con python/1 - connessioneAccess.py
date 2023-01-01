import pyodbc
import msaccessdb

try:
    conn = pyodbc.connect('percorsoDaDefinire')
    cur = conn.cursor()
    cursor.execute('select * from Tabella2')

    for row in cursor.fetchall():
        print(row)
except:
    print("errore connessione")