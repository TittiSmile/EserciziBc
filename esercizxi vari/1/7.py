"""
Scrivere
una classe Python chiamata Cerchio costruita da un raggio e un metodo per:
a. calcolare il diametro
b. calcolare l’area del cerchio
c. calcolare la circonferenza del cerchio
d. calcolare il raggio del cerchio dato l’area
e. calcolare il raggio del cerchio data la circonferenz
"""
import math

class Cerchio():
    raggio = 0
    def calcolare(self, raggio):
        self.raggio = raggio
        diametro = raggio * 2
        area = 3.14 * (math.pow(raggio,2))
        circonferenza = 2 * 3.14 * raggio
        raggio2 = math.sqrt(area/3.14)
        raggio3 = (2*circonferenza)/(2*3.14)
        print("raggio: ", raggio,
              "\ndiametro: ", diametro,
              "\narea: ", area,
              "\ncirconferenza (perimetro): ", circonferenza,
              "\nraggio del cerchio data l'area: ", raggio2,
              "\nraggio del cerchio dato il perimetro: ", raggio3
        )


r = eval(input("inserisci raggio: "))
c = Cerchio()
c.calcolare(r)