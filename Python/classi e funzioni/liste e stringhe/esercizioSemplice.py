"""
Scrivere un programma che definisca una classe Punto2D,
che rappresenti un punto del piano e definire un metodo
distanza_origine(), che ritorni la distanza del punto dall'origine."""

import  math
class Punto2D:
    def distanza_origine(self,x,y):
        xOrigine = 0    # facoltativo
        yOrigine = 0
        self.x = x      # si possono fare anche in init...
        self.y = y
        distanzaPunti = math.sqrt((self.x - xOrigine)**2 + (self.y - yOrigine)**2 )
        return distanzaPunti

x = int(input("inserisci ascissa: "))
y = int(input("inserisci ordinata: "))
p = Punto2D()
print("la distanza tra (", x, ",", y, ") e l'origine è: ",p.distanza_origine(x,y) )
