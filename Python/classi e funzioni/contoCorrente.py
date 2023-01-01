
"""
Si progetti una classe conto corrente bancario
1) Definire una classe ContoCorrente
2) All’interno della classe definire un inizializzatore per la
classe conto corrente, con tre parametri(nome, conto e
importo)
3) La classe deve avere tre attributi di istanza(nome, conto e
importo)
4) Definire un metodo «preleva» con parametro «importo»
5) Definire un metodo di istanza «deposita» con parametro
«importo»
6) Definire un metodo «descrizione», che non ha parametri
ma che deve visualizzare in una sequenza il nome, il conto e
il saldo
"""
class Contocorrente():
    def __init__(self, nome, conto, importo):       # l'importo è un po' il saldo
        self.nome = nome
        self.conto = conto
        self.importo = importo

    def preleva(self, importoP):
        if importoP > self.importo:
            print("non puoi prelevare più di quanto hai sul conto")
        elif importoP <= self.importo:
            self.importo-=importoP
            print("prelievo effettuato")
    def deposita(self,depositoP):
        if depositoP < 0:
            print("non puoi depositare un numero inferiore a 0")
        elif depositoP > 0:
            self.importo+=depositoP
            print("deposito effettuato")

    def stampa (self):
        print(self.nome, self.conto, self.importo)



conto = Contocorrente("pippo",123,5000)
soldiP = int(input("quanti soldi vuoi prelevare?  "))
soldiD = int(input("quanti soldi vuoi depositare?  "))
conto.preleva(soldiP)
conto.deposita(soldiD)
conto.stampa()
