# esempio funzioni con args (anche detti parametri indefiniti)

def f (*args):       # in questo modo, tutti i parametri che passo ad f quando la invoco,
                     # verranno raggruppati in una tupla(=lista immutabile e, chiaramente, indicizzata).
                     # args posso chiamarlo come mi pare...
    print(args)      # stampo args che, in questo caso, è considerata una tupla

f(1,2,3,4)      # posso mettere quanti parametri voglio... verranno tutti raggruppati in num senza problemi
f(1,2)
f("ciao", "amici")      # chiaramente possono essere anche stringhe...
f(1,"ciao")             #... misti...
f([44,1,"c"], "bello", 6)   #...super misti!!



# posso usare anche args e parametri normali insieme
print("\n\nesempio parametri normali ed args")
def f2(a,b,c=1,*args):
    print(a,b,c,args)


f2(1,2,99,901,999)      # i primi 2 sono a e b (c non viene dichiarato perchè è di default). da 9 in poi sono in args
f2(11,22,33,9,9,9,9,9,9)    # i primi 3 sono a,b,c(sovrascritto). tutti i 9 sono args (e quindi la tupla




