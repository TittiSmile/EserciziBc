"""2) Si definisca una classe Cerchio, utilizzando le funzioni
set e get che passato il raggio, è possibile calcolare
l’area, la circonferenza e le proprietà del raggio.
Si effettui anche un esempio circa l’utilizzo della classe."""
import math
class Cerchio():
    def __init__(self,raggio):
        self.raggio = raggio
    def getRaggio(self,raggio):
        return self.raggio
    def setRaggio(self,raggio):
        self.raggio = raggio
    raggioAttr = property(getRaggio,setRaggio)

