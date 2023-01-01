import msaccessdb
import pyodbc

dbFile = r'percorsoLocazioneDb'
msaccessdb.create(dbFile)
conn = pyodbc.connect(
        r'percorsoLocazioneDb')
cur = conn.cursor()