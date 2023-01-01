class A:
    pass    # serve a dichiarare "vuota" la classe...
    __myAttr=10


class B:
    x = 2


class C(A, B):
    y = 3


c = C()
print(c.x)  # stampa 2
# ATTENZIONE!!! se nessuna classe conteneva x, veniva dichiarato errore.


"""
in questo caso, il sistema MRO funziona alla stessa maniera. facendo c.x si va a vedere se la x è presente in C.
in caso NEGATIVO, si va a vedere nella classe A (quella dichiarata per prima come estensione di C). 
nella classe A non c'è nulla (solo pass) e quindi si va direttamente alla classe B riuscendo a stampare 2
"""