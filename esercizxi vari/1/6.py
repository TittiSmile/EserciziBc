"""
Scrivere una classe Python per trovare una coppia di elementi (considerando l’indice del
valore presente nella lista) di una lista contenente n valori, la cui somma è uguale.
Si effettui un esempio pratico
"""
# ho avuto difficoltà con la ricerca delle coppie.


def inserimentoLista():
    listaFunzione = []
    dimensioneLista = int(input("quanti elementi vuoi nella lista? "))
    for i in range(dimensioneLista):
        valore = int(input("inserisci valore: "))
        listaFunzione.append(valore)
    return listaFunzione



class Coppie():
    def trovaCoppie(self,lista):
        somma = 0
        somma2 = 0
        temp = []
        dimensioneLista = len(lista)
        i = 0
        j = 1
        while i < dimensioneLista:
             if lista[0]+lista[2] == lista[1]+ lista[3]:    # non è corretto ma non riuscivo a trovare una strategia.
                    print("trovato")
                    break
             else:
                    print("non trovato")
        i+=1









c = Coppie()
# lista = inserimentoLista()
# print(lista)
lista = [1,2,4,3]
c.trovaCoppie(lista)
