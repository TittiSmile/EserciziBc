# uso di funzioni con parametri kwargs (cioè come args ma invece di considerarti la tupla ti considera il dizionario)

def f(**kwargs):
    print(kwargs)


f(a=1,b=2,c=3)      # qui la chiamata di funzione cambia perchè, chiaramente, va trovando la coppia chiave valore (chiave->a,valore->1)


# uso kwargs con parametri posizionali e non

def f2(a,b,**kwargs):
    print(a,b,kwargs)


f(a=1,b=2,c=4,d=4)  # bisogna considerare SEMPRE l'accesso posizionale!!!
#f(a=1, b=2, a=222)  # è chiaramente errore perchè a è già stato preso come parametro all'inizio!!!! il nostro dizionario
                    # non può avere uno stesso valore a.


def f3(x,y,**kwargs):
    print(x,y,kwargs)

#f3(a=1,b=2,c=4)     # ERRORE!!! f3 ha chiamato i parametri x,y quindi non possiamo metterci a e b perchè non sa chi sono.
f3(x=1,y=2,a=4)     # no problem!!!! in f3 abbiamo dichiarato x ed y... quindi la posizione si riferisce, al più, a quei 2 parametri
                    # non possiamo rimettere x ed y in posizioni diverse da quelle stabilite dall'ordine della funzione f3!!!!