"""
Implementa il metodo __str__ della classe Squadra,
riportando il nome della squadra, l’anno di fondazione, il
nome dell’allenatore e il nome del presidente e istanzia un oggetto dello stesso tipo.
"""
import calendar
from datetime import time
from datetime import datetime

class Squadra():
    def __init__(self, nomeSquadra, annoFondazione, nomeAllenatore, nomePresidente):
        self.nomeSquadra = nomeSquadra
        self.annoFondazione = annoFondazione
        self.nomeAllenatore = nomeAllenatore
        self.nomePresidente = nomePresidente
    def __str__(self):
        return "nome squadra: {n} " \
               " anno fondazione {a}" \
               " allenatore {al} " \
               " presidente {p} ".format(n=self.nomeSquadra, a=self.annoFondazione, al=self.nomeAllenatore,
                                        p=self.nomePresidente)


class Calciatore():
    def __init__(self,nome, nomeSquadra, numeroMaglia, ruolo, anni):
        self.nome = nome
        self.nomeSquadra = nomeSquadra
        self.numeroMaglia = numeroMaglia
        self.ruolo = ruolo
        self.anni = anni
    def __str__(self):
        return "nome: {n}" \
               " squadra: {s}" \
               " maglia: {m}" \
               " ruolo: {r}" \
               " anni: {a}".format(n=self.nome, s=self.nomeSquadra, m=self.numeroMaglia, r=self.ruolo, a=self.anni)


class Data():
    def __init__(self,giorno, mese, anno):
        self.giorno = giorno
        self.mese = mese
        self.anno = anno




class Incontro():
    def __init__(self, incontro, data, ora, nomeSquadraC, nomeSquadraT, goalC, goalT):
        self.incontro = incontro
        self.data = data
        self.ora = ora
        self.nomeSquadraC = nomeSquadraC
        self.nomeSquadraT = nomeSquadraT
        self.goalC = goalC
        self.goalT = goalT

    def __str__(self):
        return "incontro: {i}" \
               " data: {d}" \
               " ora: {o}" \
               " nomeSquadraCasa: {c}" \
               " nomeSquadraTrasferta: {t}" \
               " goalCasa: {gc}" \
               " goalTrasferta: {gt}".format(i=self.incontro,
                                            d=self.data,
                                            o=self.ora,
                                            c=self.nomeSquadraC,
                                            t=self.nomeSquadraT,
                                            gc=self.goalC,
                                            gt=self.goalT)


data = datetime(2021, 5, 31)
ora = time(15, 0, 0)
s = Squadra("Napoli", 1926, "Gattuso", "ADL")
c = Calciatore("Lorenzo", "Napoli", 24, "ala", "28")
i = Incontro(1, data, ora, "Napoli", "Fiorentina", 4, 0)    # 0->andata 1->ritorno

print(s.__str__())
print(c.__str__())
print(i.__str__())