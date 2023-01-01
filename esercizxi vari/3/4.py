"""
Si crei una classe Studente. All’interno sono definiti diversi metodi:
metodo inizializzatore che riceve il nome, il cognome e l’età come parametro.
Il metodo DurataPercorso, che accetta come parametro la data d’iscrizione e la data corrente e
ne calcoli la differenza (da quanto tempo è iscritto all’università).
Il metodo esame che indica quanti esami ha effettuato lo studente.
Si crei uno script di utilizzo di questa classe.
Si crei un test TDD associato a questa classe che verifichi il corretto istanziamento dei valori,
quelli stringa, date e interi.
"""
from datetime import datetime, date
import time
import unittest

class Studente():
    def __init__(self, nome, cognome, anni):
        self.nome = nome
        self.cognome = cognome
        self.anni = anni
    def durataPercorso(self, dataIscrizione, dataCorrente):
        differenza = dataCorrente-dataIscrizione
        return differenza
    def esame(self, nEsami):
        return nEsami








dataI = date(year=2015, month=10, day=4)
dataC = date(year=2021, month=6, day=7)

s = Studente("Mario", "Rossi", 25)

dataDiff = s.durataPercorso(dataI, dataC)
print("lo studente è iscritto da: ", dataDiff)
print("esami dati: ", s.esame(15))




class TestClass(unittest.TestCase):
    s = Studente("Mario", "Rossi", 25)
    dataI = date(year=2015, month=10, day=4)
    dataC = date(year=2021, month=6, day=7)
    def verificaStringa(self):
        self.assertEqual(type("Mario"), str)
    def verificaIntero(self):
        self.assertEqual(type(s.esame(10)), int)
    def verificaData(self):
        self.assertEqual(type(s.durataPercorso(dataI, dataC)), datetime.date)



t = TestClass()
print(t.verificaStringa())
print(t.verificaIntero())
print(t.verificaData())



