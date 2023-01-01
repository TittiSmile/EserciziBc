"""
Definisci una classe Veicolo e le sue due sottoclassi: Auto e Moto. Tutte le classi hanno un
metodo "getTipo" che può stampare "Auto" per la classe Auto e "Moto" per la classe Moto
"""

class Veicolo():
    def getTipo(self):
        print("Veicolo")

class Auto(Veicolo):
    def getTipo(self):
        print("Auto")

class Moto(Veicolo):
    def getTipo(self):
        print("Moto")


v = Veicolo()
a = Auto()
m = Moto()

a.getTipo()
m.getTipo()
