
"""
Si scriva una classe Automobile, che consideri marca, modello e targa dell’auto. La classe deve anche
contenere il metodo di solo scrittura, set e di lettura, get.
Si effettui anche un esempio circa l’utilizzo della classe.
"""
class Automobile():
    def __init__(self, marca, modello, targa):
        self.marca = marca
        self.modello = modello
        self.targa = targa
    def set_auto(self):
        self.marca = marca      # hanno lo stesso nome di init
        self.modello = modello
        self.targa = targa
        return self.marca, self.modello, self.targa
    def get_auto(self):
        return self.marca, self.modello, self.targa
    attributo = property(get_auto, set_auto)

marca = input("inserire marca auto: ")
modello = input("inserire modello auto: ")
targa = input("inserire targa auto: ")
a = Automobile(marca, modello,targa)
print(a.get_auto())
print(a.set_auto())
print(a.attributo)  #attributo che contiene get e set
