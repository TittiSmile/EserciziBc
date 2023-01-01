
"""
Si trasformi l’attributo saldo e si renda privato, creando
una property per accedere a questo saldo sia in lettura che
in scrittura.
Nascondere l’attributo «saldo».
• Si definisca una property getter, di nome «saldo», che
ritorna l’attributo nascosto «saldo».
• Definire una property setter, di nome «saldo», che
modifica l’attributo nascosto «saldo».
• Invoca il metodo preleva, con importo pari al saldo
attuale.
• Invoca il metodo deposita, con importo pari al nuovo
saldo fornito dal parametro.
"""
class Contocorrente():
    def __init__(self, nome, conto, importo):       # l'importo è un po' il saldo
        self.nome = nome
        self.conto = conto
        self.__importo = importo

    def preleva(self, importoP):
        if importoP > self.__importo:
            print("non puoi prelevare più di quanto hai sul conto")
        elif importoP <= self.__importo:
            self.__importo-=importoP
            print("prelievo effettuato")
    def deposita(self,depositoP):
        if depositoP < 0:
            print("non puoi depositare un numero inferiore a 0")
        elif depositoP > 0:
            self.__importo+=depositoP
            print("deposito effettuato")

    @property
    def saldo(self):
        return self.__importo

    @importo.property
    def saldo(self,importo):
        self.preleva(self.__importo)
        self.deposita(importo)


    def stampa (self):
        print(self.nome, self.conto, self.importo)



conto = Contocorrente("pippo",123,5000)
soldiP = int(input("quanti soldi vuoi prelevare?  "))
soldiD = int(input("quanti soldi vuoi depositare?  "))
conto.preleva(soldiP)
conto.deposita(soldiD)
conto.stampa()
conto.saldo()