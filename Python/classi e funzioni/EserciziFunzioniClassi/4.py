"""
Scrivere una classe che contenga al suo interno un metodo nel quale si chiede all'utente di
inserire una lista di numeri reali si calcolano il valore minimo e il secondo minimo,
infine, si stampino il tutto a schermo
"""

class myClass():
    def findMaxMin(self):
        lista = []
        max = -1000
        min = 1000
        dimensione = int(input("quanti elementi vuoi nella lista?  "))
        for i in range (dimensione):
            elemento = int(input("inserisci elemento: "))
            lista.append(elemento)
        # metodo furbo
        """     lista.sort()
                print("la lista è: ", lista,
                      "\nelemento massimo: ", lista[dimensione-1],
                      "\nelemento minimo: ", lista[0])
        """
        # metodo più onesto
        for i in lista:
            if i > max:
                max = i
            if i < min:
                min = i

        print("la lista è: ", lista,
           "\nelemento massimo: ", max,
           "\nelemento minimo: ", min)



obj = myClass()
obj.findMaxMin()